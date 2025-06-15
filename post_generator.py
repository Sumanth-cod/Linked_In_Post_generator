from llm_helper import llm
from few_shot import Few_Shots_Post

few_shot=Few_Shots_Post()

def get_length_str(length):
    if length=="Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 55 lines"
    
def get_prompt(length,language,tag):
    length_str=get_length_str(length)

    prompt=f'''
    Generate a Linkedin post using the below information .No preamble
    
    1)Topic:{tag}
    2)Length:{length}
    3)Language:{language}
    if Language is Hinglish then it means it is a mix of Hindi and english.
    The script for the generatiion post should always be English and the script is ready to post in linked in


    '''
    example=few_shot.get_filtered_posts(length,language,tag)
    if len(example)>0:
        prompt+="4)use the writing style as per the following examples."
        for i,post in enumerate(example):
            post_text=post['text']
            prompt+="\n\n Example{i} \n\n{post_text}"

            if i==1:
                break


    
    return prompt


def generate_post(length,language,tag):

    prompt=get_prompt(length,language,tag)
    length_str=get_length_str(length)

    prompt=f'''
    Generate a Linkedin post using the below information .No preamble
    
    1)Topic:{tag}
    2)Length:{length}
    3)Language:{language}
    if Language is Hinglish then it means it is a mix of Hindi and english.
    The script for the generatiion post should always be English and the script is ready to post in linked in


    '''
    example=few_shot.get_filtered_posts(length,language,tag)
    if len(example)>0:
        prompt+="4)use the writing style as per the following examples."
        for i,post in enumerate(example):
            post_text=post['text']
            prompt+="\n\n Example{i} \n\n{post_text}"

            if i==1:
                break


    response=llm.invoke(prompt)
    return response.content
if __name__=="__main__":
    post= generate_post("Short","English","Job search")
    print(post)