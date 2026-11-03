---
content_hash: 05bafb636ca57aeb57ee859b0223fe514d239c83b31d3d2a12f253e73ebe2e44
fetched_at: '2026-06-29T00:06:16.402110+00:00'
page_id: '212897451'
product: rm
source: tdn-rm
title: TIN005_7_Conversão dos Aditivos com XML para Tabelas (versionamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212897451
version: 10
---

|  |  |
| --- | --- |
| Descrição | ADITIVOS NA VERSÃO 3.0 |
| Observações | Este processo valida se a versão dos aditivos se encontra na mais atual.  Em versões anteriores houveram modificações onde a funcionalidade de aditivos deixaram de salvar seus parâmetros em um XML serializado e passou a guardá-los em uma nova estrutura de campos e tabelas. Esta conversão era executada quando o usuário acessava pela primeira vez a visão de aditivos. A partir da versão de revitalização serão migrados todos os aditivos através da ferramenta "Conversor da Revitalização"      Para verificar se a migração ocorreu corretamente a **Ferramenta** valida o parâmetro imobiliário “NOVOMODELOADITIVO” que deve estar presente na tabela “XPARAMS”, se o valor encontrado na coluna “VALOR” for igual a “1” significa que o aditivo já está na versão ideal.  A ferramenta executa o seguinte select  *select VALOR from XPARAMS where NOME = 'NOVOMODELOADITIVO'*  Se o resultado da consulta for VALOR = 0 ou se a consulta não trouxer nenhum registro, então a ferramenta migra os aditivos para a nova estrutura . |
