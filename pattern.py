#check if the string starts with hello
import re #regular expression library
pattern = r"Hello|name"
text="Hello,world!,hello my name rame  Hello"
match=re.match(pattern,text)
print(f"found:{bool(match)}")
print("found:{match}")
# found:True 