---
content_hash: aa6854606324dd8711fe05cd7dfa0322fdf9af4c9bea113dc3e304ee36de080c
fetched_at: '2026-07-02T19:24:19.545985+00:00'
page_id: '223172407'
product: protheus
source: tdn-tec
title: TMSGraphic:SaveToImage
type: documentation
url: https://tdn.totvs.com/display/tec/TMSGraphic%3ASaveToImage
version: 1
---

SaveToImage

Salva o gráfico atual, no formato pré-determinado, no servidor.

## Sintaxe

, ,  )]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório |
| --- | --- | --- | --- |
| cImgName | Caracter | Indica o nome da imagem que será salva. | x |
| cPath | Caracter | Indica o diretório, no servidor, onde a imagem será armazenada. | x |
| cImgType | Caracter | Indica o formato com que a imagem será salva. Suporta: png, bmp e jpg (default) | x |

## Retorno

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| lRet | Lógico | Retorna se a imagem foi salva com sucesso.  (.T.) - Imagem salva com sucesso. (.F) - A imagem não foi salva com sucesso. |

## Observação

A gravação em disco somente ocorrerá após o gráfico já ter sido exibido em tela.

## Exemplo
