---
content_hash: 9ccbaae10db33e54569315851cbeb4deb0f85c9fcc5f4bb8ab4bc8fa076bf7bf
fetched_at: '2026-06-29T00:10:42.998611+00:00'
page_id: '549489125'
product: rm
source: tdn-rm
title: 8430030 FISCAL01-12754 DT ROTINA LEGAL DSRE - RECIFE
type: documentation
url: https://tdn.totvs.com/display/LRM/8430030+FISCAL01-12754+DT+ROTINA+LEGAL+DSRE+-+RECIFE
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotina Legal DSRE |
| Ticket: | 8430030 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12754 |

## **02. SITUAÇÃO/REQUISITO**

Cliente solicita que a rotina DSRE não sejam gerados as notas fiscais eletrônicas de prestadores situados no município de Recife, esta demanda visa atender o manual da rotina página 3:

[https://nfse.recife.pe.gov.br/arquivos/NFSE\_declaracao.pdf](https://nfse.recife.pe.gov.br/arquivos/NFSE_declaracao.pdf "Follow link")

## **03. SOLUÇÃO**

Ajuste no layout da DSRE para não gerar para lançamentos de entrada que o modelo do documento seja 55 e o município seja Recife. Lançamentos com a seguinte parametrização não serão considerados:

* Código Modelo Documento 55 + Chave de acesso preenchida + Município igual a Recife- Não considerar lançamento

* Código Modelo Documento 55 + Chave de acesso não preenchida + Município igual a Recife - Não considerar lançamento

* Documento Sem Modelo Documento + chave de acesso preenchida + Município igual a Recife - Não considerar lançamento
