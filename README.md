Whiterose, a DateTime Toolkit
===

_"The concept of waiting bewilders me. There are always deadlines. There are always ticking clocks. That's why you must manage your time"_

---

+ [localtime()](#localtime--)
+ [today()](#today--)
+ [Unix Timestamps Toolkit](#unix-timestamps-toolkit)
    * [Epoch.dump()](#epochdump--)
    * [Epoch.load()](#epochload--)
    * [Epoch.now()](#epochnow--)
    * [Epoch.strfload()](#epochstrfload--)

---

### localtime()

```python
>>> localtime()
time.struct_time(...)
```

### today()

```python
>>> today('UTC')
'2020/12/18T22:24:58'
>>> today('MX')
'2020/12/18T16:24:58'
```

### Unix Timestamps Toolkit

##### Epoch.dump()

```python
>>> Epoch.dump(2020, 12, 18, 16)
1608328800.0
```

##### Epoch.load()

```python
>>> tms = Epoch.load(epoch)
'2020-12-18 16:24:58.109826'
>>> type(tms)
"<class 'datetime.datetime'>"
```

##### Epoch.now()

```python
>>> Epoch.now()
1608330298.110156
```

##### Epoch.strfload()

```python
>>> Epoch.strfload(1608330298.110156, datetime=True)
'2020/12/18T16:24:58'
>>> Epoch.strfload(1608330298.110156, datetime=False)
'2020/12/18'
```