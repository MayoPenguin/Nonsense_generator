"""A collection of function for doing my project."""
import random
import json

#Access the lists stored in json files
with open('scripts/Famous_quotes.json') as a:
    Famous_quotes = json.load(a)
with open('scripts/Replacer_for_famous.json') as b:
    Replacer_for_famous = json.load(b)
with open('scripts/Interlanguage_first_part.json') as c:
    Interlanguage_first_part = json.load(c)
with open('scripts/Connection_word.json') as d:
    Connection_word = json.load(d)
with open('scripts/Interlanguage_second_part.json') as e:
    Interlanguage_second_part = json.load(e)

def introduction_maker(keyword):
    """A perfect essay will always begin with a nice introduction.
    
    Parameters
    ----------
    keyword : string
        Keyword you want it appear in the essay.
        
    Returns
    -------
    output_introduction : string
        Introduction of an essay containing the keyword.
    """ 
    
    #Check type of input 
    if not isinstance(keyword, str):
        raise ValueError("Please provide the keyword as a string")
    else:
        output_introduction = ''
    
    #Compose the introduction sentence by combining randomly-selected sentence fragments from two lists 
    first_sentence = random.choice(Interlanguage_first_part) + random.choice(Interlanguage_second_part)
    output_introduction += first_sentence
    
    #Replace the $ with the input keyword
    output_introduction = output_introduction.replace('$', keyword)
    
    return output_introduction

def content_filler(keyword):
    """A perfect essay will always have enough content.
    
    Parameters
    ----------
    keyword : string
        Keyword you want it appear in the essay.
        
    Returns
    -------
    output_content : string
        Content of an essay containing the keyword.
    """ 
    
    #Check type of input
    if not isinstance(keyword, str):
        raise ValueError("Please provide the keyword as a string")
    else:
        output_content = ''
    
        #Randomly select a famous quotes from the target list
        output_content += random.choice(Famous_quotes)
    
        #Add interlanguage for random times
        for repeat in range(random.choice([1,2,3])):
            sentence = random.choice(Interlanguage_first_part) + random.choice(Interlanguage_second_part)
            output_content += sentence
    
        #Add another famous quotes and interlanguage, which are connected with connection word    
        output_content += random.choice(Connection_word)
        output_content += random.choice(Famous_quotes)
        output_content += random.choice(Connection_word)
        output_content += random.choice(sentence)
    
    #Replace the $ with the input keyword and @ with a word randomly selected from target list
    output_content = output_content.replace('$', keyword)
    output_content = output_content.replace('@', random.choice(Replacer_for_famous))
    
    return output_content

def conclusion_creator(keyword):
    """Also, a perfect essay will always end with a nice conclusion.
    
    Parameters
    ----------
    keyword : string
        Keyword you want it appear in the essay.
        
    Returns
    -------
    output_conclusion : string
         Conclusion of an essay containing the keyword.
    """  
    
    #Check type of input
    if not isinstance(keyword, str):
        raise ValueError("Please provide the keyword as a string")
    else:
        output_conclusion = ''
    
    #Conclusion will always begin with connection word
    output_conclusion += random.choice(Connection_word)
    
    #Compose the conclusion by combining randomly-selected sentence fragments from two lists
    last_sentence = random.choice(Interlanguage_first_part) + random.choice(Interlanguage_second_part)
    output_conclusion += last_sentence
    
    #Replace the $ with the input keyword
    output_conclusion = output_conclusion.replace('$', keyword)
    
    return output_conclusion

def nonsense_generator(keyword, length, paragraph, genre):
    """This is a generator which will generate a bunch of nonsense to you.
    
    Parameters
    ----------
    keyword : string
    number : integer
    paragraph : integer
    genre : string(either essay or letter)
        Your requirement for a perfect essay.
        
    Returns
    -------
    perfect_essay : string
         A perfect_essay which satisfies all your requirements.
    """ 
    
    #Check type of input
    if not isinstance(keyword, str) and isinstance(length, int) and isinstance(paragraph, int) and isinstance(genre, int):
        raise ValueError("Please provide the keyword as a string, length and paragraph as the integer, and genre as either essay or letter")
    else:
        perfect_essay = ''
        Recipient = ''
        Sender = ''
        counter = 1
        
        #Specify type of article you want to generate
        if genre == 'letter':
            
            #Assign the recipient's name
            Recipient_name =  input('Recipient :\t')
            Recipient += '\n' + 'Dear ' + Recipient_name + ',' + '\n' +'\n'
            
            #Assign the sender's name
            Sender_name = input('Sender :\t')
            Sender += '\n' + 'Sincerely' + ',' + '\n' + Sender_name
            
            #Check the length of article you want to generate; if length is not met, the process will keep going until input number is achieved
            while len(perfect_essay) < length: 
                perfect_essay += introduction_maker(keyword)
                perfect_essay += content_filler(keyword)
                perfect_essay += conclusion_creator(keyword)
                
                #This part will generate the paragraph; length of each paragraph will be length/paragraph
                if len(perfect_essay) > ((length//paragraph) * counter):
                    perfect_essay += '\n'
                    perfect_essay += '\n'
                    counter += 1
            perfect_essay = Recipient + perfect_essay + Sender
        
        
        #Same process for essay-type of article    
        elif genre == 'essay':
            while len(perfect_essay) < length:
                perfect_essay += introduction_maker(keyword)
                perfect_essay += content_filler(keyword)
                perfect_essay += conclusion_creator(keyword)
                if len(perfect_essay) > ((length//paragraph) * counter):
                    perfect_essay += '\n'
                    perfect_essay += '\n'
                    counter += 1
        else:
            raise TypeError('please input the genre as either letter or essay')
    
    #Replace the keyword
    perfect_essay = perfect_essay.replace('$', keyword)
    perfect_essay = perfect_essay.replace('@', random.choice(Replacer_for_famous))
    
    return print(perfect_essay)
