---
content_hash: 951d6fd951a58176f5c4cc2fab05edf12718865014a0a45900838f1b096f5841
fetched_at: '2026-07-02T19:24:23.166025+00:00'
page_id: '270917620'
product: protheus
source: tdn-tec
title: RecSize
type: documentation
url: https://tdn.totvs.com/display/tec/RecSize
version: 1
---

RecSize

Retorna o tamanho de um registro da tabela aberta.

## Sintaxe

false

## Observações

* O valor retornado é a soma dos tamanhos de todos os campos da tabela mais 1 byte pelo flag de exclusão, tratado pela função .
* **RecSize** desconsidera os campos de controle adicionados pelo DBAccess.
* Caso não haja tabela aberta, a função retornará **0** (zero).
* A existência de mais de uma conexão no mesmo programa para o mesmo SGBD não influencia o funcionamento da função.
* Verifique a função  para considerações sobre os tamanhos dos campos.

## Exemplos

O exemplo abaixo utiliza a RDD "**TOPCONN**", mas a função pode ser utilizada com qualquer uma das RDDs válidas.

cppEclipsetruefalse

## Veja também
