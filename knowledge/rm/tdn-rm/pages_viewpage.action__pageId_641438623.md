---
content_hash: 1a2870ceb338439af4a26e30def7deb6ae8c1fd35bb387cf1c31a57e90526c2b
fetched_at: '2026-06-29T00:11:10.081468+00:00'
page_id: '641438623'
product: rm
source: tdn-rm
title: Validação "Mesmo prestador, função diferente, mesmo procedimento na mesma data"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641438623
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Essa validação consiste na seguinte regra:

* Procedimento deve estar na faixa de codificação cirúrgica ou anestesiologia
* Prestador pessoa física
* Existir lançamento nas condições acima, ou seja  "Mesmo prestador, função diferente, mesmo procedimento na mesma data"
* Caso o usuário possua permissão no parâmetro de perfil "Lançamento de honorário para o mesmo prestador em funções diferentes no mesmo procedimento", será emitido somente um aviso. Caso contrário, a mensagem será impeditiva para encerrar a parcial.

## **02.****TABELAS UTILIZADAS**

* SZATENDHONORARIO
