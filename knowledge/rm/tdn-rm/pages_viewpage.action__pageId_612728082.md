---
content_hash: dc9728a0d0e3df4a54d79f24f45a408a91a95f6a04d431096ee3000d896f55dd
fetched_at: '2026-06-29T00:10:59.203639+00:00'
page_id: '612728082'
product: rm
source: tdn-rm
title: 11080022 FISCAL01-15231 DT Apuração CRB - Geração de guia aut. - Lançamento
  não foi encontrado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=612728082
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Período de Apuração |
| País: | Brasil |
| Ticket: | 11080022 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15231 |

## **02. SITUAÇÃO/REQUISITO**

Ao encerrar o Período de Apuração do Tributo CPRB, o Campo **“Saldo Anterior do Tributos”** é preenchido e como consequência não é gerado a guia ocorrendo a seguinte mensagem:

**> Erro no processo: Nenhum lançamento foi encontrado! <**

Isto ocorre quando temos lançamentos Fiscais de Outros Débitos\Credito, feito para ajuste da Base de Cálculo do Tributo CPRB.

O valor destes lançamentos é considerado no Encerrado do Período como Credito do Imposto e este comportamento não deve ser aplicado ao **Tributo CPRB**.

Este comportamento só deve ser aplicado para Tributos que faz apuração de Debito e Credito (exemplo **Tributos ICMS** e **IPI**).

## **03. SOLUÇÃO**

O problema relatado "Nenhum lançamento encontrado" no processo de geração de guia automática, se deve ao fato do Código de Receita não ter sido preenchido no Período de Apuração. Preenchendo este campo no Período de Apuração ou no Lançamento de Outros Débitos/Créditos (e encerrando o período novamente) a guia será gerada corretamente pelo processo.

Porém foi necessário um ajuste no processo de Encerramento do Período de Apuração, para a Contribuição Previdenciária, que estava calculando o campo Saldo Anterior do Tributo. Devido a isto, foi feito uma alteração para que este campo não seja calculado para CPRB.
