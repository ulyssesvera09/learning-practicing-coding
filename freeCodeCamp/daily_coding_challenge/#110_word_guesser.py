def compare(word, guess):
    #returned string = '#'*len(word)
    evaluation = '# '*len(word)
    evaluation = evaluation.split()
  
    #look for exact matches & substitute '2' on index
  
    exact = [[-1], '']
    for i, ch in enumerate(word):
        if word[i] == guess[i]:
            evaluation[i] = '2'
            exact[0].append(i)
            exact[1] += word[i] 
          
    #ignore indexes of exact matches & 
    #evaluate if ch exists in the secret word
  
    secret = {}
    for ch in word:
        if ch not in secret:
            secret[ch] = 0
        secret[ch] += 1
    for ch in exact[1]:
        if ch in secret:
            secret[ch] -= 1
    for i, ch in enumerate(guess):
        if i in exact[0]:
            continue
        if ch in secret and secret[ch] > 0:
            secret[ch] -= 1
            evaluation[i] = '1'
        else:
            evaluation[i] = '0'
    return ''.join(evaluation)

if __name__ == '__main__':
  guess = compare("WIRELESS", "ETHERNET")
  print(guess)
