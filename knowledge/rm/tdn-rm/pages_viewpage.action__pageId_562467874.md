---
content_hash: b09ca53aace85645de341067ecca2022b3a706721e9d04f68355960ffd27becc
fetched_at: '2026-06-29T00:10:50.636175+00:00'
page_id: '562467874'
product: rm
source: tdn-rm
title: 7534564 FISCAL01-12022 DT Lançamento Fiscal - Controle de Ativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562467874
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Lançamento Fiscal |
| Ticket: | 7534564 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12022 |

## **02. SITUAÇÃO/REQUISITO**

O cliente ao realizar a transferência de ativo imobilizado entre filiais de MG para Maranhão por força de legislação deve usar alíquota de tributação em 7% por se tratar de operação interestadual; Porém na entrada do ativo foi uma operação interna, onde no livro CIAP foi calculado crédito de ICMS de 18% conforme alíquota interna de MG, sendo o crédito divido em 48 parcelas por se tratar de ativo.

A entrada foi efetuada em setembro e saída em outubro, o que permite o aproveitamento de 1 parcela do crédito e transferência do restante para o aproveitamento da filial.

Porém ao efetuar o lançamento de transferência para a outra filial, pelo fato do valor baixado no CIAP é com no valor preenchido nos itens, acaba por baixar o valor a menor nos créditos e não em sua totalidade para poder transferir para a filial.

## **03. SOLUÇÃO**

Alteração no  lançamento fiscal para que salve o valor do ICMS de entrada na saída do ativo na tabela DATIVO.

Alteração no Sped Fiscal para que gere o registro G125 SI quando o patrimônio for baixado filial de origem.
