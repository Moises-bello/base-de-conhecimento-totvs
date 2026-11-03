---
article_id: 39469019449879
category: eConsignado (Crédito do Trabalhador)
content_hash: ff5ff7d2b5c30257d0324f3b071cb50f5d509072d2476ed112bbae2a6ce19f39
fetched_at: '2026-06-28T22:43:07.347957+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Parcela do eConsignado sendo descontada duas vezes
  na folha para funcionário que esteve de férias
type: support-article
updated_at: '2026-04-02T12:51:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39469019449879-RH-Linha-Protheus-GPE-Parcela-do-eConsignado-sendo-descontada-duas-vezes-na-folha-para-funcion%C3%A1rio-que-esteve-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39469035879191) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Após a criação da verba id. **1979 - Dev. eConsignado Férias**, além do desconto de Id **1979**, o Sistema continua descontando a **parcela do mês** do eConsignado. Isso resulta em um desconto **maior** no salário do funcionário  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - Todas as versões  
  
**Solução**  
O desconto na férias não é o desconto do empréstimo em si, mas sim uma **provisão** deste valor, o qual é devolvido na folha de pagamento na através do Id 1973 - eConsignado Provisionado nas Férias.  
   
Na folha de pagamento o Sistema precisa **zerar** o valor das férias, porque elas já foram pagas, e também fazer com que o valor descontado do eConsignado nas férias **sobre positivamente**, para evitar que ele não tenha uma insuficiência de saldo. Para isso, o Sistema leva a verba de provento (id **1973**) no **mesmo valor** descontado nas **férias** (soma dos id's **1971** e **1972**), mas também apresenta a verba de desconto (id **1979**) para conta bater.  
   
Então na folha o Sistema usa a seguinte fórmula:  
   
Soma **todas as verbas de provento** de férias + a **devolução da provisão do eConsignado** na folha (id 1973) - **INSS férias** que consta no **recibo de férias** - **líquido pago** nas férias - **IR** de férias - a **devolução do eConsignado** (id **1979**).

**Exemplo**  
  
Folha de Pagamento  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39469019439767)

Recibo de Férias  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39469019440279)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39469019441431)

Aplicando a fórmula:

Soma **todas as verbas de provento** de férias (2.517,73) +   
D**evolução da provisão do eConsignado** na folha (598,25) -   
**INSS férias** que consta no **recibo de férias** (176,99 + 25,28 = **202,27**) -   
L**íquido pago** nas férias (1.717,21) -   
**IR** de férias (0,00) -   
D**evolução do eConsignado** (598,25)  
  
2.517,73 + 598,25 - 202,27 - 1.717,21 - 598,25 = **598,25**  
  
Veja que o valor final da fórmula é exatamente o valor da provisão descontada nas férias, ou seja, o valor está de fato sendo devolvido na folha do funcionário.

Desta forma é garantido que o valor descontado nas férias seja **devolvido** e ainda **sobre positivamente** na folha dos funcionários de forma correta.  
   
Se a verba com id 1979 não for considerada, o funcionário terá um valor **dobrado** indevidamente, o que **prejudica o empregador**.  
  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Verba de líquido das férias é demonstrada na folha com valor maior que o calculado no recibo de férias para funcionários que tiveram provisão do eConsignado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34732356784279-RH-Linha-Protheus-GPE-Verba-de-l%C3%ADquido-das-f%C3%A9rias-%C3%A9-demonstrada-na-folha-com-valor-maior-que-o-calculado-no-recibo-de-f%C3%A9rias-para-funcion%C3%A1rios-que-tiveram-provis%C3%A3o-do-eConsignado)

[RH - Linha Protheus - GPE - eConsignado - Conferencia de Valores no Provisionamento com Férias Partidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35864184082199-RH-Linha-Protheus-GPE-eConsignado-Conferencia-de-Valores-no-Provisionamento-com-F%C3%A9rias-Partidas)

[RH - Linha Protheus - GPE - Como cadastrar as verbas de Provisionamento nas Férias e Adiantamento referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)
