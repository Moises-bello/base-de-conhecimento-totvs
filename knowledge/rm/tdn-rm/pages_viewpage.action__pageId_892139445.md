---
content_hash: 815c5057f0accdec4fab9515ba5c621ae0e1c3056d7f9775a9d27f766f0dfa6e
fetched_at: '2026-06-29T00:12:01.293265+00:00'
page_id: '892139445'
product: rm
source: tdn-rm
title: DT - eSocial - Códigos de Cálculo para lançar o valor do IRRF Simplificado
  em evento de Base para enviar para o S-1200
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=892139445
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo da folha de pagamento |
| País: | Brasil |
| Issue: | [DRHCALCRM-6824](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6824) |

## **02.** **VERSÕES**

Liberado a partir das versões:

12.1.2402.255

12.1.2406.200

12.1.2410.130

12.1.2502 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

o eSocial criou a tabela 21, no grupo 'Dedução do rendimento tributável do IRRF', o código '**68 - Desconto Simplificado Mensal**'. Este código deve ser utilizado para enviar um evento/verba informando que o colaborador teve o desconto simplificado, com o valor do dedutível utilizado conforme a tabela de valores fixos de finalidade '**Valor a deduzir no IRRF Simplificado'** vigente, por período/envelope lançado.

Atualmente, no produto, a informação deste desconto é registrada nos campos IRRFSIMPLIFICADO, IRRFFERSIMPLIFICADO, IRRF13SIMPLIFICADO da tabela PFPERFF e IRRFSIMPLIFICADO da tabela PFUFERIASRECIBO, preenchendo com indicativo = 1 quando é utilizado o desconto simplificado na base de imposto de renda. No entanto, o eSocial exige que a informação seja enviada através de rubrica com o código de incidência **68 - Desconto Simplificado Mensal** quando o mesmo for utilizado.

## **04. SOLUÇÃO**

Foi criado novos códigos de cálculo para lançar o valor do desconto simplificado quando o mesmo for utilizado:

* Código de cálculo 477 -  Valor a Deduzir de IRRF Simplificado Folha
* Código de cálculo 478 - Valor a Deduzir de IRRF  Simplificado Férias
* Código de cálculo 479 - Valor a Deduzir de IRRF  Simplificado 13º Salário

Quando for Férias será lançado no recibo e no envelope de pagamento.

No e-Social será validado no parametrizador para desconsiderar o evento para o envio do xml, caso o cliente não queira enviar, uma vez que este evento não é obrigatório.

IMPORTANTE

Esses códigos de cálculos serão lançados por período no envelope de pagamento e serão usados exclusivamente para o envio no XML do eSocial.

É de responsabilidade do usuário informar o código de incidência 68 no cadastro de eventos vinculados aos códigos de cálculo acima.

O processo de cálculo continuará preenchendo os campos indicativos do período da ficha financeira e recibo de férias quando for utilizado o desconto simplificado.

Esses códigos de cálculos não serão usados no processo da DIRF.

Caso não queira enviar esse evento no XML do eSocial, insira no Paramertrizador / eSocial / Registros Inativos / Eventos a Desconsiderar.

## **05. ASSUNTOS RELACIONADOS**

* [Cálculo do IRRF Simplificado](https://tdn.totvs.com/pages/releaseview.action?pageId=761006653)
* [Código de Cálculo 477 - Valor a Deduzir de IRRF Simplificado Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139184)
* [Código de Cálculo 478 - Valor a Deduzir de IRRF Simplificado Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139208)
* [Código de Cálculo 479 - Valor a Deduzir de IRRF Simplificado 13º Salário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139220)
