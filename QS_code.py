# Data Engineering - Interview Question - 2nd techical interview
 
# Write a function that, for a string phrase as an argument, returns a string that indicates the language to which this phrase belongs.
# If you can't determine the language or an error occurs - your function should return unknown.
 
# Note:
 
# Please avoid using any libraries or functions (langdetect, Polyglot, etc.) for detecting a language.
# The task is about you writing an algorithm based on the input data and dataset you have.
# We are looking for a clean and efficient solution: when you are done
 
lang_dataset = {
        "lang1": "The gladdest moment in life is a departure into unknown lands. Travel makes one modest. You see what a tiny place you occupy in the world. Better to see something once than hear about it a thousand times.",
        "lang2": "İnsan hayatındaki en mutlu an, bilinmeyen topraklara doğru yola çıkmaktır. Seyahat bir mütevazı yapar. Dünyada ne kadar küçük bir yer işgal ett",
        "lang3": "Радісний момент у житті людини це опинитися на невідомих землях. Подорож робить тебе скромним. Ти бачиш, яке маленьке місце займаєш у світі. Краще побачити щось один раз, ніж почути про це тисячу разів."
}
 
phrase = "ThIs Is hAppy Life"
 
def solution(phrase):
  dictionary_score = {}
  
  # Lower
  counter_list = phrase.split(" ")
  
  # phrase = phrase.lower().split(" ")
  # dataset = [] 
  # for keyword in range(len(lang_dataset)):
  #     dataset.append(list(lang_dataset.values())[keyword].lower())
  # counter_list = []
  
  for lang, sentence in lang_dataset.items(): 
    score = 0
    
    for keyword in counter_list:
      # Lower
      if keyword in sentence:
        score = score + 1
        dictionary_score[lang] = score
    
    maxScore = max(dictionary_score.values())
    maxLang = max(dictionary_score, keyword = dictionary_score.get)
  
  if maxScore == 0:
    return 'No Language Found!'
  else:
    return maxLang
  
print(solution(phrase));
