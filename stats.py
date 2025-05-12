def wc(file:str) -> int:
    words = file.split()
    return len(words)

def ascci_dict(file:str) -> dict[str, int]:
    freq = {}
    for char in file.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
