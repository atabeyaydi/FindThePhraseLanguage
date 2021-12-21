# FindThePhraseLanguage
  This question is asked in one of the interviews of Company for Data Engineer.
  
  Write a function that, for a string phrase as an argument, returns a string that indicates the language to which this phrase      belongs. 
  If you can't determine the language or an error occurs - your function should return unknown.

Note:
   Please avoid using any libraries or functions (langdetect, Polyglot, etc.) for detecting a language. The task is about you writing an algorithm based on the input data and dataset you have.
  
lang_dataset = { 

                "lang1": "The gladdest moment in life is a departure into unknown lands. Travel makes one modest. You see what a tiny place you occupy in the world. Better to see something once than hear about it a thousand times.", 
                
                "lang2": "İnsan hayatındaki en mutlu an, bilinmeyen topraklara doğru yola çıkmaktır. Seyahat bir mütevazı yapar. Dünyada ne kadar küçük bir yer işgal ett", 
                
                "lang3": "Радісний момент у житті людини це опинитися на невідомих землях. Подорож робить тебе скромним. Ти бачиш, яке маленьке місце займаєш у світі. Краще побачити щось один раз, ніж почути про це тисячу разів."
                
}

phrase = "ThIs Is hAppy Life"

...

def solution(phrase):

...

print(solution(phrase))
