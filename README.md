# senya
dead simple flask api with face recognition

# usage
```sh
curl http://127.0.0.1:5000/check \
    -H 'Content-Type: image/jpeg' \
    --data-binary @photo1.jpg
```

```python
with open('photo2.jpg', 'rb') as f:
    r = requests.post('http://127.0.0.1:5000/check', f, headers={
        'content-type': 'application/octet-stream',
    })
    print(r.json())
```

# license
MIT
