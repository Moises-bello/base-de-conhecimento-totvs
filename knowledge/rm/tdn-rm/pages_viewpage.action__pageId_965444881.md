---
content_hash: 1f52b052c4e6fb6ed563d4f2654691f8470812e826aaa7e4ec015a67ea9c5fe4
fetched_at: '2026-06-29T00:12:14.101303+00:00'
page_id: '965444881'
product: rm
source: tdn-rm
title: DT - eSocial - Empréstimo Crédito Trabalhador - Adequação na validação do XML
  S-1200, S-2299 e S-2399
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=965444881
version: 7
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | eSocial - Empréstimo Crédito Trabalhador - Adequação na validação do XML S-1200, S-2299 e S-2399 |
| País: | Brasil |
| Issue: | [DRHROTRM-13849](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13849) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.269
* 12.1.2502.171
* 12.1.2506.115 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ajustar a validação do XML dos eventos eSocial S-1200, S-2299 e S-2399 para que o sistema passe a verificar quando o campo "**Comp final Desc**" estiver preenchido com zero, além de validar se a data informada nesse campo está fora do período de apuração correspondente aos eventos.

## **04. SOLUÇÃO**

Implementada tratativa para que, ao gerar o XML dos eventos S-1200, S-2299 e S-2399, o sistema passe a validar se o campo **"Comp final Desc"** do cadastro de empréstimo está preenchido com 0 (zero).

Nessa situação, a tag **`<descFolha>`** não será gerada, e o sistema exibirá a seguinte mensagem de erro:

O sistema também valida se a competência em que o período de apuração está sendo gerado está dentro do intervalo informado no campo **"Comp final Desc"** do cadastro de Empréstimo.

Se a data estiver dentro do período informado, a tag `<descFolha>` será gerada no XML.  
Caso contrário, a tag **`<descFolha>`** não será gerada.

**Exemplo de geração do XML – Evento S-1200:**

* + **Período de apuração: 10/2024**  
    A tag **`<descFolha>`** **será gerada** no XML, conforme demonstrado abaixo:

* + **Período de apuração: 09/2024**  
    A tag **`<descFolha>`** **não será gerada** no XML.

## **05. DOCUMENTAÇÃO**
