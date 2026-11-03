---
content_hash: 042b82622aacdcb07acfb0ec122e5cb14781f230ba0bd920c2df029a5a847b3b
fetched_at: '2026-06-29T00:05:49.855486+00:00'
page_id: '1042909879'
product: rm
source: tdn-rm
title: DT - DOCELETRONICOS-582 - Erro durante a tradução do XML - CliFor com CNPJ
  repetido mas é o CNPJ da FIlial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1042909879
version: 7
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Inclusão de Movimento através de XML - CTe |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DOCELETRONICOS-582 |

## **02. SITUAÇÃO/REQUISITO**

Inclusão de Movimento através de XML - CTe (Erro Durante a Tradução do XML)

**Validação:**

Erro durante a tradução do XML.  
Chave de Acesso: XXXXXXXX  
Mensagem Original: Erro ao incluir Movimento: Há mais de um Cliente/Fornecedor com o CNPJ XX.XXX.XXX/0001-XX

O Sistema está validando a existência de dois Fornecedores com o mesmo CNPJ quando no XML está preenchido o Grupo toma4 - Outros.

## **03. SOLUÇÃO/COMPORTAMENTO**

Identificamos que o Comportamento do Sistema está correto.

Para este tipo de tomador, (toma4) - Outros

A informação contida no campo CNPJ do grupo e utilizada no campo do Movimento (Cliente/Fornecedor Tomador) Tipo Tomador "Outros" na aba Transporte/Identificação.

Neste caso quando existe mais de um Fornecedor Ativo o sistema não consegue identificar qual e o Código de Fornecedor Correto.

Para o correto funcionamento do sistema deve-se deixar apenas um Fornecedor Ativo.
