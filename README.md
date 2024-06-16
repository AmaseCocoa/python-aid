# python-aid
python-aidはMisskeyのaid/aidxのPython向けの実装です。

aidは[この実装](https://github.com/misskey-dev/misskey/blob/c1514ce91dc08481a092a789ee37da546cdb4583/packages/backend/src/misc/id/aid.ts)、aidxは[この実装](https://github.com/misskey-dev/misskey/blob/c1514ce91dc08481a092a789ee37da546cdb4583/packages/backend/src/misc/id/aidx.ts)に基づいています。

## aid/aidxとは？
Misskeyで利用されているID生成アルゴリズムです。

## Example
### aid
```python
from python_aid import aid

generated = aid.genAid()
print("aid: " + generated)

print("time: " + aid.parseAid(generated).strftime('%Y-%m-%d %H:%M:%S.%f'))
```
### aidx
```python
from python_aid import aidx

generated = aidx.genAidx()
print("aidx: " + generated)

print("time: " + aidx.parseAid(generated).strftime('%Y-%m-%d %H:%M:%S.%f'))
```
## 試す
[python-aid sandbox](https://codepiece.pages.dev/?state=N4Igxg9gJgpiBcIBmAnCBbABABwJ4BcALCAOwH0BDASykyvWwhX02qgA8AdE7gcxhIwUFfDFoBeVjXYA6fiQCC0gBQBKbthRUS%2BZZxBt28TPswBqTPKEix6niU3bd%2B%2FPRjHTFwzOwUUAZxglDmUrYVEoVRl%2FfBQkV3QYZQByAFIATQBaVPRs2lSACXhUgFligGUZVKRk1VUQABoQXzAAawp%2BfwQAbWaCYhJMthAAXSb8P358BBAYqAgAV2mm%2BYB3EgAbCAooLvhukYBfIA%3D%3D)
