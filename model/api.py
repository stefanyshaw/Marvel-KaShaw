try:
    import requests
    import pendulum
    import hashlib
    from model.marvel import public_key, private_key
    from flask import Flask, render_template, request
except ImportError as err:
    print(f"Failed to import required packages: {err}")


def get_character(public_key, private_key, name):
    # Data/hora necessário para a autenticação da API
    now = pendulum.now('Europe/London')
    now = now.to_iso8601_string()

    # GHash necessário para a autenticação da API
    m = hashlib.md5()
    m.update(now.encode('utf8'))
    m.update(private_key.encode('utf8'))
    m.update(public_key.encode('utf8'))

    endpoint = f"https://gateway.marvel.com:443/v1/public/characters?nameStartsWith={name}&limit=1"
    resp = requests.get(endpoint, params={"apikey": public_key, "ts": now, "hash": m.hexdigest()}).json()
    # Colete os dados necessários de resp.
    try:
        name = resp["data"]["results"][0]["name"]
        description = resp["data"]["results"][0]["description"]
        thumbnail = resp["data"]["results"][0]["thumbnail"]["path"]
        extension = resp["data"]["results"][0]["thumbnail"]["extension"]
        # URL de formato para imagem de resp
        thumbnail = f"{thumbnail}/landscape_incredible.{extension}"
        return {"name": name, "description": description, "thumbnail": thumbnail}
    except IndexError:
        return render_template("index.html")
