import json

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from llm_helper import llm





def process_posts(raw_file_path,processed_file_path="data/processed_posts.json"):
    enriched_posts=[]

    with open (raw_file_path,encoding='utf-8') as  file:
        posts=json.load(file)
        
        for post in posts:
            metadata=extract_metadata(post["text"])
            post_with_metadata=post | metadata
            enriched_posts.append(post_with_metadata)
    
    unified_tags=get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags=post['tags']
        new_tags={unified_tags.get(tag,tag) for tag in current_tags}

        post['tags']=list(new_tags)

    with open(processed_file_path,encoding="utf-8",mode="w") as outfile:
        json.dump(enriched_posts,outfile,indent=4)





def get_unified_tags(posts_with_metadata):
    unique_tags=set()
    for post in posts_with_metadata:
        unique_tags.update(post["tags"])
    unique_tags_list=', '.join(unique_tags)



    template='''
    I will give a list of tags.You need to unify tags with the following requirements,
    1.Tags are unified and merged to create a shorter list.
      Example 1:"jobseekers","job hunting" can be all merged into a single tag "job search".
      Example 2:"motivation",inspiration","Drive" can be mapped to "motivation".
      Example 3:"personal growth","personal Development","self improvement" can be mapped  into "self improvement".

      Example 4:"scam alert","job scam" etc. can be mapped to scams
    2.Each tag should be follow title case convention ,example:"motivation","job search",
    3. Your response must be valid JSON — return **only the JSON object**,no explanation,No preamble. 
    4.Output should have mapping of original tag and the unified tag.
       For exmaple:{{"jobseekers":"job seaarch,"job hunting ":"job search","motivation":"motivation"}}

    Here is the list of tags:
    {tags}
    '''

    pt=PromptTemplate.from_template(template)


    

    chain=  pt | llm

    response=chain.invoke(input={'tags':str(unique_tags_list)})

    try:

        json_parser=JsonOutputParser()

        res=json_parser.parse(response.content)  #content actually is used prints the content retrived from the llm 
    except OutputParserException:
        raise OutputParserException("Content too big .Unable to parse jobs")
    return res


def extract_metadata(post):
    template='''

    You  are given a LinkedIn Post .You need to extract number of Lines,language of the post and tags.
    1.Your response must be valid JSON — return **only the JSON object**,no explanation,No preamble.
    2.JSON object should have exactly three keys:linecount,language and tags.
    3.tags  is an array of text tags .Extract maximum two tags.
    4.Language should be English or Hinglish(Hinglish means hindi + english)

      Here is the actual post on which  you need to perform this task:
      {post}
      '''    

    pt=PromptTemplate.from_template(template)


    

    chain=  pt | llm

    response=chain.invoke(input={'post':post})

    try:

        json_parser=JsonOutputParser()

        res=json_parser.parse(response.content)  #content actually is used prints the content retrived from the llm 
    except OutputParserException:
        raise OutputParserException("Content too big .Unable to parse jobs")
    return res





    
  
    


if __name__=='__main__':
    process_posts("data/raw_posts.json","data/processed_posts.json")