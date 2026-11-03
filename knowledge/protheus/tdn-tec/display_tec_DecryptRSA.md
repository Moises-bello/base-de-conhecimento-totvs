---
content_hash: 1e48b1666d7a6c5e8e6e5c972639bfb0fd7cf6aea3f215ed1f844d1c79e7f1f1
fetched_at: '2026-07-02T19:24:28.676147+00:00'
page_id: '807208697'
product: protheus
source: tdn-tec
title: DecryptRSA
type: documentation
url: https://tdn.totvs.com/display/tec/DecryptRSA
version: 4
---

DecryptRSA

Realiza a descriptografia de uma string criptografada utilizando o algoritmo RSA.

## Sintaxe

false, < cInfo > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cKeyFile | character | Indica o nome do arquivo que contém a chave privada que será usada para descriptografar o dado. | X |  |
| cInfo | character | Indica a string criptografada que será descriptografada. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cRet | character | Retorna a string <**cInfo**> descriptografada com o algoritmo RSA, utilizando a chave privada apontada por <**cKeyFile**>. |

## Observações

* O arquivo apontado por <**cKeyFile**> deve estar localizado no path relativo do Application Server e ter o formato ".pem". Caso não esteja no Application Server, o retorno será Nil.
* Caso a string encriptada tenha sido codificada em base64, através do terceiro parâmetro da função , é necessário realizar a decodificação antes de submeter a string encriptada para a função DecryptRSA. Para realizar a decodificação utilize a função .

## Exemplos

cppEclipsetruefalse

## Abrangência

Application Server 20.3.2.3
