---
content_hash: 9f3f51e8e91360ec8dd737d3213faaf2ec6be5713fc6bd86842a215e3a939120
fetched_at: '2026-06-29T00:10:26.852581+00:00'
page_id: '515278997'
product: rm
source: tdn-rm
title: FISCAL01-10614 DT Lentidão - Sped Contribuições (Coligada 3)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515278997
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Contribuições |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10614 |

## **02. SITUAÇÃO/REQUISITO**

Melhora de performance na geração da EFD Contribuições.

## **03. SOLUÇÃO**

Alterada a forma de geração do campo "IND\_PAGTO" do registro C100 da EFD Contribuições. O mesmo passou a ser gerado utilizando-se o mesmo serviço de Materiais utilizado para geração da NF-e. Caso o Lançamento não seja proveniente do Movimento, será verificada a Data de Vencimento. Se for igual à Data de Emissão, o campo será gerado como "A Vista"; Se for diferente, o campo será gerado como "A prazo"; Se não estiver preenchida, será gerado como "Outros".

Esta alteração, além de manter a compatibilidade com o envio da NF-e, foi realizada para melhorar a performance da rotina, uma vez que não é mais realizado um select oneroso para o Banco de Dados, para verificar as faturas vinculadas ao Lançamento Fiscal.
