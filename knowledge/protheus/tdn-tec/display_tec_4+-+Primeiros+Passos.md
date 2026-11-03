---
content_hash: 2d9358c69267d356fc64a6225507253babc54200b39902d68ef49005e20bca01
fetched_at: '2026-07-02T19:24:26.810031+00:00'
page_id: '654947468'
product: protheus
source: tdn-tec
title: 4 - Primeiros Passos
type: documentation
url: https://tdn.totvs.com/display/tec/4+-+Primeiros+Passos
version: 6
---

#### 1 - Criando código-fonte teste

Agora que seu ambiente está pronto, já podemos escrever o primeiro arquivo-fonte de teste.

> Para esse exemplo, iremos construir um teste verificando se a função valtype() está retornando conforme esperado.

Notem que é extremamente simples:

c#

```
Elementos exclusivos do PROBAT
```

* #include "[tlpp-probat.th](http://tlpp-probat.th)"
* @TestFixture()
* tlpp.probat.assertEquals()

> Notas:
>
> * A função sempre deve retornar .T., ao menos que você queira estruturar seu teste para que alguns casos retorne .F., gerando erro automático ao final da execução.
> * Para gerar resultado dos testes, é necessário executar ao menos 1 (uma) função de Assert() do acervo do **PROBAT**.
> * É possível escrever os testes com classes também, inclusive através de classe teremos mais recursos disponíveis. O uso de função de testes é limitado porém mais simples.

Ao final, compile esse fonte no mesmo ambiente onde foi aplicado o patch.

#### 2 - Executando Testes

Agora que temos ao menos um teste criado e compilado, podemos então solicitar a execução, sendo assim basta executar a seguinte função:

Essa função é do tipo *Main Function*, portanto pode ser chamada diretamente na execução pelo VsCode ou por linha de comando do appserver.

Exemplo de Linha de comando:

bash

---

# 

Acesse também o vídeo aula com esse mesmo tema.

[1 - PROBAT - Primeiros Passos](https://www.youtube.com/watch?v=covZWUvXwRA)

```

```
