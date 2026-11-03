---
content_hash: f1ef67ab2c9cfb2a08d29cf6c1b6be706a1171da283a331567c3b7d189b75ee2
fetched_at: '2026-06-29T00:05:47.406990+00:00'
page_id: '1012942208'
product: rm
source: tdn-rm
title: DT - Integração RM x Feedz – Melhoria na mensagem de erro relacionada ao campo
  “Cargo”
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1012942208
version: 6
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Integração RM x Feedz - Melhoria na mensagem de erro relacionada ao campo “Cargo” |
| País: | Brasil |
| Issue: | [DRHROTRM-14083](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14083) |

## **02. VERSÃO**

* 12.1.2502.233
* 12.1.2506.182
* 12.1.2510.116 e superiores.

## **03. S****ITUAÇÃO/REQUISITO**

Tratar a mensagem na Integração RM x Feedz quando o campoCargo no cadastro de função do menu Administração Pessoal | Cargos/ Funções | Funções estiver nulo.

## **04. SOLUÇÃO**

Foi implementada uma tratativa na Integração RM x Feedz para que, ao identificar funções com o campo Cargo nulo, o sistema apresente uma mensagem informativa, listando as matrículas dos colaboradores vinculados a essas funções.

**Mensagem exibida ao final da integração:**

> Chapa xxxx não processada, pois o campo “Cargo” no cadastro da função está nulo.

## **05. DEMAIS INFORMAÇÕES**

* [Integração RM X Feedz](https://tdn.totvs.com/pages/viewpage.action?pageId=785614408)
