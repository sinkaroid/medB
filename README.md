
# Jandabooru
[![](https://img.shields.io/pypi/v/beautifulsoup4)](https://pypi.org/project/beautifulsoup4/) [![CodeFactor](https://www.codefactor.io/repository/github/sinkaroid/jandabooru/badge)](https://www.codefactor.io/repository/github/sinkaroid/jandabooru) [![Build Status](https://travis-ci.com/sinkaroid/jandabooru.svg?branch=main)](https://travis-ci.com/sinkaroid/jandabooru)  


- [bash version](https://github.com/sinkaroid/Scathachsh) (outdated)

## Getting started

----

    git clone https://github.com/sinkaroid/jandabooru.git
    cd jandabooru;pip install -r requirements.txt;cd src


## Usage example

```
./r34.py 1 fate%2fgrand_order,yuri,blush

<booru> <aggregated> <tags>
  │         │          │
  │         │          └─⫸ sys.argv[2] (spell):  
  |         |            short_spell, multiple tags separated by (comma)
  |         |     
  │         │
  │         └─⫸ sys.argv[1] (pid): The page number: 1-100 afaik
  |
  └─⫸ sys.argv[0]
```

Default `<aggregated>` is 1, which default limit retrieved 50images/pages, you can adjust in the parameter.  
Then fill [spell](/src/spell) default last_tags is `>10` (greater than X that mean will retrieved images with score above X)  
you can fill it with long tags or leave it blank with (space)  
> eg: safebooru didn't supported score tags and danbooru isn't supported multiple tags iirc.

## Directory Tree

```
jandabooru/
├── example/
│   └── awesome-booru/
|
└── src/
    ├── gelbooru
    ├── konachan
    ├── lolibooru
    ├── r34
    ├── safebooru
    ├── xbooru
    ├── yande.re
    └──────── spell
```

### Todo
- [X] gelbooru
- [X] konachan
- [X] lolibooru
- [X] r34 
- [X] safebooru
- [X] xbooru
- [X] yandere
- [ ] danbooru 
- [ ] tbib
- [ ] realbooru
- [ ] furrybooru

### Further
Please check [awesome-booru](/example/awesome-booru/boorus.json) then look around related booru sites to get the correct spelling.  
Pls keep in mind some site isn't supported multiple tags eg: [danbooru](https://danbooru.donmai.us/) iirc.

 <h2>Powered By</h2>
  <a href="https://www.jetbrains.com/?from=sinkaroid"><img alt="JetBrains" src="src/jetbrains.svg"></a>