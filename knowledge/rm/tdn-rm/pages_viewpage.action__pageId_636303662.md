---
content_hash: 92b4fba70d4340755ad2cb233b13c5c01dc36362fd95fd4436a1f41bd902a161
fetched_at: '2026-06-29T00:11:06.887441+00:00'
page_id: '636303662'
product: rm
source: tdn-rm
title: 'FISCAL01-16486 - O Campo nDraw: conteúdo não obedece o esquema da NF-e'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=636303662
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Nota Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16486 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar nota ﬁscal de importação sem o preenchimento do Número do Ato concessório (nDRAW) é apresentada a seguinte inconsistência:

Enviar NF-e: Erro no envio da NF-e. TSS - Erro na validação desta nota. Motivo:Campo: nDraw': Conteúdo do campo não obedeceao Esquema da NF-e. O campo tem tamanho: '0'; O Tamanho mínimo aceito é: '1'.

O problema ocorre porque a partir da NT 2020.005 a tag nDraw foi alterada para o tamanho mínimo de 1.Então, quando não houver valor, a tag não deve ser gerada(a tag não pode ser gerada vazia).

## **03. SOLUÇÃO.**

Foi alterada a geração da tag nDraw para que não seja gerada caso o campo do RM esteja vazio. A tag será gerada somente quando o campo correspondente ao Drawback no RM possuir algum valor preenchido.
