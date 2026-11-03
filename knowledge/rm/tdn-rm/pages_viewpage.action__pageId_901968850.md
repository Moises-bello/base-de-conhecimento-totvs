---
content_hash: a6b072ba0486c10224eb8b6dc54dd0ef9ab7ddc75be6ef61a8c0394fc41ffdd5
fetched_at: '2026-06-29T00:12:02.649155+00:00'
page_id: '901968850'
product: rm
source: tdn-rm
title: DT - Encargos - Base de Cálculo de INSS Dissídio Negativa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901968850
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Base de Cálculo de INSS Dissídio Negativo |
| País: | Brasil |
| Ticket: | [21390309](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2221390309%22 "21390309") |
| Issue: | [DRHCALCRM-6649](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6649) |

## **02. SITUAÇÃO/REQUISITO**

No cálculo do encargo tipo R-Base, referente à incidência de INSS Dissídio, foi identificado que, quando há um mês com base de INSS negativa, o sistema está abatendo esse valor no total geral do cálculo. Isso resulta em discrepâncias nos valores gerados para a contabilização, que não conferem com os valores transmitidos ao eSocial.

## **03. SOLUÇÃO**

Foi ajustado o comportamento do sistema para que, quando o valor da base do encargo do tipo R - Base INSS Dissídio e S - Base INSS de 13º Salário Dissídio for negativo, este seja considerado como **zero**, em conformidade com o comportamento esperado pelo eSocial.  
Além disso, foi garantido o zeramento da base de INSS dissídio para folha, férias e 13º salário nas competências com base negativa, abrangendo os encargos 3, H, T e U, assegurando a correta contabilização e alinhamento dos valores com os transmitidos ao eSocial.

Exemplo:   
  
Quando gerarmos um encargo com o valor positivo, ele irá se manter da forma correta, exibindo o perfeitamente no log da geração de encargos  
  
  
  
Quando o valor da base for negativa, a geração de encargos irá desprezar esse valor na somataria geral do encargo:

## **04. ASSUNTOS RELACIONADOS**

* [Encargos](https://tdn.totvs.com.br/display/public/LRM/Encargos+-+Folha+de+Pagamento?draft=true)
