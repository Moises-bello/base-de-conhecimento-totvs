---
content_hash: f68325d9fef74b7ee3b76ed4a04fe2cf72bf47615ca46ac2283c3517bfcfa261
fetched_at: '2026-06-29T00:11:28.486274+00:00'
page_id: '731884756'
product: rm
source: tdn-rm
title: DT - Convocação Intermitente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=731884756
version: 3
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Convocação Intermitente |
| País: | Brasil |
| Releases: | a partir da 12.1.2302 |
| Issue: | DRHROTRM-206 |

## **02. SITUAÇÃO/REQUISITO**

Atualmente, ao incluir um novo registro no cadastro de convocação para trabalho intermitente, o campo “Situação da Convocação” está vindo preenchido com um default, o que evita que o usuário tenha que pensar sobre a verdadeira situação da convocação. Esse comportamento pode facilmente induzir a inconsistências no cadastro.

## **03. SOLUÇÃO**

Na inclusão de um novo registro o sistema passou a apresentar o campo “Situação da Convocação” em branco, para que o usuário defina qual é a situação, evitando assim o preenchimento incorreto da informação. Campo também passou a ser de preenchimento obrigatório no cadastro.

## **04. DEMAIS INFORMAÇÕES**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719267>
