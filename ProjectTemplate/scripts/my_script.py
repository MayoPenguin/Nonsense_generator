"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import my_func, my_other_func

###
###

# PYTHON SCRIPT HERE

import json

Famous_quotes = [
    
"Nelson Mandela @, The greatest glory in living lies not in never falling, but in rising every time we fall.",

"Walt Disney @, The way to get started is to quit talking and begin doing.",

"Steve Jobs @, Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",

"Eleanor Roosevelt @, If life were predictable it would cease to be life, and be without flavor.",

"Oprah Winfrey @, If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",

"James Cameron @, If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",

"John Lennon @, Life is what happens when you're busy making other plans.",

"Mother Teresa @, Spread love everywhere you go. Let no one ever come to you without leaving happier.",

"Franklin D. Roosevelt @, When you reach the end of your rope, tie a knot in it and hang on.",

"Margaret Mead @, Always remember that you are absolutely unique. Just like everyone else.",

"Robert Louis Stevenson @, Don't judge each day by the harvest you reap but by the seeds that you plant.",

"Eleanor Roosevelt @, The future belongs to those who believe in the beauty of their dreams.",

"Benjamin Franklin @, Tell me and I forget. Teach me and I remember. Involve me and I learn.",

"Helen Keller @, The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",

"Aristotle @, It is during our darkest moments that we must focus to see the light.",

"Anne Frank @, Whoever is happy will make others happy too.",

"Ralph Waldo Emerson @, Do not go where the path may lead, go instead where there is no path and leave a trail.",

"Mother Teresa @, Spread love everywhere you go. Let no one ever come to you without leaving happier.",

"Franklin D. Roosevelt @, When you reach the end of your rope, tie a knot in it and hang on.",

"Margaret Mead @, Always remember that you are absolutely unique. Just like everyone else.",

"Robert Louis Stevenson @, Don't judge each day by the harvest you reap but by the seeds that you plant.",

"Eleanor Roosevelt @, The future belongs to those who believe in the beauty of their dreams.",

"Benjamin Franklin @, Tell me and I forget. Teach me and I remember. Involve me and I learn.",

"Helen Keller @, The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",

"Aristotle @, It is during our darkest moments that we must focus to see the light.",

"Anne Frank @, Whoever is happy will make others happy too.",

"Ralph Waldo Emerson @, Do not go where the path may lead, go instead where there is no path and leave a trail.",

"Maya Angelou @, You will face many defeats in life, but never let yourself be defeated.",

"Nelson Mandela @, The greatest glory in living lies not in never falling, but in rising every time we fall.",

"Abraham Lincoln @, In the end, it's not the years in your life that count. It's the life in your years.",

"Babe Ruth @, Never let the fear of striking out keep you from playing the game.",

"Helen Keller @, Life is either a daring adventure or nothing at all.",

"Thomas A. Edison @, Many of life's failures are people who did not realize how close they were to success when they gave up.",

"Dr. Seuss @, You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.",

"Eleanor Roosevelt @, If life were predictable it would cease to be life and be without flavor.",

"Abraham Lincoln @, In the end, it's not the years in your life that count. It's the life in your years.",

"Ralph Waldo Emerson @, Life is a succession of lessons which must be lived to be understood.",

"Maya Angelou @, You will face many defeats in life, but never let yourself be defeated.",

"Babe Ruth @, Never let the fear of striking out keep you from playing the game.",

"Oscar Wilde @, Life is never fair, and perhaps it is a good thing for most of us that it is not.",

"Tony Robbins @, The only impossible journey is the one you never begin.",

"Mother Teresa @, In this life we cannot do great things. We can only do small things with great love.",

"Albert Einstein @, Only a life lived for others is a life worthwhile.",

"Dalai Lama @, The purpose of our lives is to be happy.",

"John Lennon @, Life is what happens when you're busy making other plans.",

"Mae West @, You only live once, but if you do it right, once is enough.",

"Ralph Waldo Emerson @, Live in the sunshine, swim the sea, drink the wild air.",

"Henry David Thoreau @, Go confidently in the direction of your dreams! Live the life you've imagined.",

"Henry David Thoreau @, The greatest glory in living lies not in never falling, but in rising every time we fall.",

"Confucius @, Life is really simple, but we insist on making it complicated.",

"Jonathan Swift @, May you live all the days of your life.",

"Hans Christian Andersen @, Life itself is the most wonderful fairy tale.",

"John Wooden @, Do not let making a living prevent you from making a life.",

"D. H. Lawrence @, Life is ours to be spent, not to be saved.",

"Marilyn Monroe @, Keep smiling, because life is a beautiful thing and there's so much to smile about.",

"James M. Barrie @, Life is a long lesson in humility.",

"Robert Frost @, In three words I can sum up everything I've learned about life: it goes on.",

"Bob Marley @, Love the life you live. Live the life you love.",

"Helen Keller @, Life is either a daring adventure or nothing at all.",

"Dr. Seuss @, You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.",

"Charles Dickens @, Life is made of ever so many partings welded together.",

"Steve Jobs @, Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma -- which is living with the results of other people's thinking.",

"Ray Bradbury @, Life is trying things to see if they work.",

"Thomas A. Edison @, Many of life's failures are people who did not realize how close they were to success when they gave up.",

"Winston S. Churchill @, Success is not final; failure is not fatal: It is the courage to continue that counts.",

"Henry David Thoreau @, Success usually comes to those who are too busy to be looking for it.",

"Walt Disney @, The way to get started is to quit talking and begin doing.",

"Steve Jobs @, If you really look closely, most overnight successes took a long time.",
    
"John D. Rockefeller Jr. @, The secret of success is to do the common thing uncommonly well.",

"Thomas Jefferson @, I find that the harder I work, the more luck I seem to have."

"Barack Obama @, The real test is not whether you avoid this failure, because you won't. It's whether you let it harden or shame you into inaction, or whether you learn from it; whether you choose to persevere.",

"John D. Rockefeller Jr. @, The secret of success is to do the common thing uncommonly well.",

"Thomas Jefferson @, I find that the harder I work, the more luck I seem to have.",

"Winston S. Churchill @, Success is not final; failure is not fatal: It is the courage to continue that counts.",

"Walt Disney @, The way to get started is to quit talking and begin doing.",

"Zig Ziglar @, Don't be distracted by criticism. Remember -- the only taste of success some people get is to take a bite out of you.",

"Henry David Thoreau @, Success usually comes to those who are too busy to be looking for it.",

"Estee Lauder @, I never dreamed about success, I worked for it.",

"Conrad Hilton @, Success seems to be connected with action. Successful people keep moving. They make mistakes but they don't quit.",

"Colin Powell @, There are no secrets to success. It is the result of preparation, hard work, and learning from failure.",

"Barack Obama @, The real test is not whether you avoid this failure, because you won't. It's whether you let it harden or shame you into inaction, or whether you learn from it; whether you choose to persevere.",

"Franklin D. Roosevelt @, The only limit to our realization of tomorrow will be our doubts of today.",

"Herman Melville @, It is better to fail in originality than to succeed in imitation.",

"Jim Rohn @, Successful people do what unsuccessful people are not willing to do. Don't wish it were easier; wish you were better.",

"Colin R. Davis @, The road to success and the road to failure are almost exactly the same.",

"Thomas Edison @, I failed my way to success.",

"James Cameron @, If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",

"Steve Jobs @, If you really look closely, most overnight successes took a long time.",

"David Brinkley @, A successful man is one who can lay a firm foundation with the bricks others have thrown at him.",

"John Wooden @, Things work out best for those who make the best of how things work out.",

"Albert Einstein @, Try not to become a man of success. Rather become a man of value.",

"John D. Rockefeller @, Don't be afraid to give up the good to go for the great.",

"Abraham Lincoln @, Always bear in mind that your own resolution to success is more important than any other one thing.",

"Winston Churchill @, Success is walking from failure to failure with no loss of enthusiasm.",

"Oprah Winfrey @, You know you are on the road to success if you would do your job and not be paid for it.",

"Thomas J. Watson @, If you want to achieve excellence, you can get there today. As of this second, quit doing less-than-excellent work.",

"Gurbaksh Chahal @, If you genuinely want something, don't wait for it -- teach yourself to be impatient.",

"Vidal Sassoon @, The only place where success comes before work is in the dictionary.",

"Jim Rohn @, If you are not willing to risk the usual, you will have to settle for the ordinary.",

"Alexander Graham Bell @, Before anything else, preparation is the key to success.",

"Tony Robbins @, People who succeed have momentum. The more they succeed, the more they want to succeed and the more they find a way to succeed. Similarly, when someone is failing, the tendency is to get on a downward spiral that can even become a self-fulfilling prophecy.",

"Wayne Gretzky @, You miss % of the shots you don't take.",

"Henry Ford @, Whether you think you can or you think you can't, you're right.",

"Rosa Parks @, I have learned over the years that when one's mind is made up, this diminishes fear.",

"Mother Teresa @, I alone cannot change the world, but I can cast a stone across the water to create many ripples.",

"Audrey Hepburn @, Nothing is impossible, the word itself says, ‘I'm possible!'",

"Ayn Rand @, The question isn't who is going to let me; it's who is going to stop me.",

"Ralph Waldo Emerson @, The only person you are destined to become is the person you decide to be.",

"Theodore Roosevelt @, Believe you can and you're halfway there.",

"Ralph Waldo Emerson @, The only person you are destined to become is the person you decide to be.",

"Maya Angelou @, I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",

"Ayn Rand @, The question isn't who is going to let me; it's who is going to stop me.",

"Vince Lombardi @,  Winning isn't everything, but wanting to win is.",

"Henry Ford @, Whether you think you can or you think you can't, you're right.",

"Wayne Gretzky @, You miss % of the shots you don't take.",

"Mother Teresa @, I alone cannot change the world, but I can cast a stone across the water to create many ripples.",

"Oprah Winfrey @, You become what you believe.",

"Amelia Earhart @, The most difficult thing is the decision to act, the rest is merely tenacity.",

"Anne Frank @, How wonderful it is that nobody need wait a single moment before starting to improve the world.",

"Socrates @, An unexamined life is not worth living.",

"George Addair @, Everything you've ever wanted is on the other side of fear.",

"Norman Vaughan @, Dream big and dare to fail.",

"Beverly Sills @, You may be disappointed if you fail, but you are doomed if you don't try.",

"Charles Swindoll @, Life is % what happens to me and % of how I react to it.",

"Audrey Hepburn @, Nothing is impossible, the word itself says, ‘I'm possible!'",

"Confucius @, It does not matter how slowly you go as long as you do not stop.",

"Henry Ford @, When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.",

"Les Brown @, Too many of us are not living our dreams because we are living our fears.",

"Rosa Parks @, I have learned over the years that when one's mind is made up, this diminishes fear.",

"Benjamin Franklin @, I didn't fail the test. I just found  ways to do it wrong.",

"Sheryl Sandberg @, If you're offered a seat on a rocket ship, don't ask what seat! Just get on.",

"Florence Nightingale @, I attribute my success to this: I never gave or took any excuse.",

"Vincent van Gogh @, I would rather die of passion than of boredom.",

"Oprah Winfrey @, If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",

"Gloria Steinem @, Dreaming, after all, is a form of planning.",

"-Napoleon Hill @, Whatever the mind of man can conceive and believe, it can achieve.",

"Aristotle @, First, have a definite, clear practical ideal; a goal, an objective. Second, have the necessary means to achieve your ends; wisdom, money, materials, and methods. Third, adjust all your means to that end.",

"Mark Twain @, Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So, throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover.",

]

Replacer_for_famous = [
    
    'said',
    'thought',
    'claimed',
    'stated',
    'argued',
    'clarified',
    'declared',
    'asserted',
    'professed',
    'pointed',
    'debated',
    'stressed',
    'talked',
    'explained',
    'discussed',
    'underscored',
]

Interlanguage_first_part = [
    'In my mind,'
    'In my perspective,'
    'I have to say that'
    'Without doubts,',
    'A proverb says,',
    'at present,',
    'As the proverb says,',
    'Currently,',
    'Generally speaking,',
    'Now,',
    'In general,',
    'On the Whole,',
    'It is clear that,',
    'Recently,',
    'It is often said that,', 
    'First of all,',
    'Moreover,',
    'Firstly,',
    'No one can deny that,',
    'In the first place,',
    'Obviously,',
    'To begin with,',
    'Of course,',
    'We should realize that,',
    'Certainly,',
    'There is no doubt that,',
    'In fact,',
    'It can be easily proved,' 
]
    
Connection_word = [    
    'In addition,',
    'Furthermore,',
    'Again,',
    'Also,',
    'Besides,',
    'Moreover,',
    'What’s more,',
    'Similarly,',
    'Next,', 
    'Finally,',
    'In the same way,',
    'Likewise,',
    'Similarly,',
    'Equally,',
    'In comparison,',
    'Just as,',
    'Whereas,', 
    'In contras,',
    'On the other hand,',
    'Instead,',
    'However,',
    'Nevertheless,',
    'Unlike, even though,',
    'On the contrary,', 
    'While,',
    'Because,',
    'Because of,',
    'For,',
    'Since,',
    'Due to,',
    'Owing to,',
    'Thanks to,',
    'As a result,',
    'Accordingly,',
    'Hence,',
    'So,',
    'Thus,',
    'Certainly,',
    'Above all,',
    'Indeed,',
    'Of course,', 
    'Surely,',
    'Actually,',
    'As a matter of fact,',
    'Chiefly,',
    'Especially,',
    'Primarily,',
    'In particular,',
    'Undoubtedly,',
    'Absolutely,',
    'Most important,',
    'Although,',
    'Though,',
    'After all,',
    'In spite of,',
    'Nevertheless,',
    'Still,',
    'Provided,',
    'For example,', 
    'For instance,',
    'That is,',
    'Namely,',
    'Such as,',
    'In other words,',
    'In this case,',
    'By way of illustration,',
    'To sum up,',
    'To conclude,',
    'In a word,',
    'In short,',
    'In brief,',
    'All in all,',
    'In all,',
    'To put it,',
    'In a nutshell,',
    'In summary,',
    'Therefore,',
    'As a result of,',
    'Consequent,',
    'Accordingly,',
    'Otherwise,',
    'Afterward,',
    'After,',
    'First,',
    'Later,',
    'Then,',
    'Soon,',
    'Outside,',
    'Near,',
    'Beyond,',
    'Above,',
    'Below,',
    'In the middle,',
    'Opposite,',
    'In front of,'
]
    
Interlanguage_second_part = [
    'I have several reasons to support my point of view about $.',
    'I agree with $, which I will explain in the following essay.',
    'I will explain my argument about $ in the following paragraphs.',
    '$ is really important.',
    'I would definitely agree with $.',
    'I truly believe about $.',
    'I will explain my point of view about $.',
    'we cannot ignore $.',
    'the importance of $ cannot be overlooked.',
    'I cannot image the consequnce if we do not pay enough attention to $.',
    'the thing I want to discuss is $.',
    'in this artcile, I will mainly talk about $.',
    'the thing I want to argue is $.',
    'I want to argue about $.',
    'the importance of $ cannot be ignored.',
    'I always think aboub $.',
    'I believe that $ will become more and more important.',
    'the very first thing I want to talk about is $.',
    'without $, we cannot work efficiently as usual.',
    'clearly, $ is important.',
    'the importance of $ has been stressed many times by different people but I still want to talk more about $.',
    'I am willing to address $ in the article.',
    'I really want to illustrate the meaning of $.',
    'I present you what I think about $.',
    'it is really important for us to realize something about $.'
    'how might $ work?',
    
]

with open('Famous_quotes.json', 'w') as jsonfile:
    json.dump(Famous_quotes, jsonfile)
with open('Replacer_for_famous.json', 'w') as jsonfile:    
    json.dump(Replacer_for_famous, jsonfile)
with open('Interlanguage_first_part.json', 'w') as jsonfile:    
    json.dump(Interlanguage_first_part, jsonfile)
with open('Connection_word.json', 'w') as jsonfile:    
    json.dump(Connection_word, jsonfile)
with open('Interlanguage_second_part.json', 'w') as jsonfile:    
    json.dump(Interlanguage_second_part, jsonfile)
