---
article_id: 360019827572
category: RH - 13º salário
content_hash: c685012ab104748a967fb58221e69e3c9a47338bd06235707f84d9bd99e1050e
fetched_at: '2026-06-28T22:44:00.723829+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a conferência do IRRF referente ao
  Complemento da 2ª parcela de 13º na folha de dezembro
type: support-article
updated_at: '2025-07-30T12:36:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019827572-RH-Linha-Protheus-GPE-Como-realizar-a-confer%C3%AAncia-do-IRRF-referente-ao-Complemento-da-2%C2%AA-parcela-de-13%C2%BA-na-folha-de-dezembro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29274280859415) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como realizar a conferência do **IRRF** referente ao **Complemento da 2ª parcela de 13º** na folha de dezembro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para calcular o valor do **IRRF referente ao Complemento da 2ª parcela do 13º**, precisamos primeiro identificar como foi composto o valor do **complemento da 2ª parcela 13º (id 0028).**A partir da verba lançada com incidência para média de 13º, após o cálculo e fechamento da 2ª parcela do 13º, este valor será dividido por 12 para se chegar ao valor da média. O resultado desta divisão irá compor os id 0028 (Diferença 2ª parcela 13º).

Com o valor do id0028 (Diferença 2ª parcela 13º) na folha, subtraímos deste valor, o INSS 13º (id 0070). Desta subtração, chegaremos ao valor da verba com id 0027 (Base IRRF 13º).   
  
Com o valor do id 0027 (Base IRRF 13º) localizado no cálculo da folha referente a dezembro, **aplicamos o mesmo percentual de desconto que foi utilizado sobre a verba com id 0027 no cálculo da 2ª parcela do 13º (neste cálculo não deverá ser aplicado o desconto da dedução da tabela de IRRF, uma vez que já foi aplicada no cálculo da 2ª parcela do 13º).**

**Exemplo (verificar a explicação e os valores nos prints):**  
Valor da verba de prêmio (que possui incidência para média de 13º) lançado após o cálculo e fechamento da 2ª parcela do 13º no roteiro FOL: R$1200,00  
  
Como é necessário realizar a média dos 12 meses do ano, é realizada a divisão do valor por 12: R$1200,00 / 12= R$100,00 **(este valor será gravado na verba de id 0028)**

Para identificarmos a base do IRRF 13º e desconto de IRRF 13º no cálculo da folha referente ao período de dezembro, realizamos o seguinte cálculo:  
R$100,00 (Dif. 2ª Parc. 13º, verba com id 0028) - 11,00 (INSS 13º, verba com id 0070)= R$89,00  
R$89,00 \* 15%(mesmo percentual utilizado no cálculo da 2ª parcela do 13º)= **R$13,35 (Valor da verba de desconto IRRF 13º, id 0071)**

Cálculo da 2ª parcela do 13º  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015741191)

Cálculo da folha referente do período de dezembro ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015694172)

**Saiba Mais**  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>

[RH - Linha Protheus - GPE - Como cadastrar o ID 0348 Diferença Negativa 13° Salario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11222354283927-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-0348-Diferen%C3%A7a-Negativa-13-Salario?source=search)  
[RH - Linha Protheus - GPE - Por que pode ser apresentada a verba de desconto Diferença de 13º Negativo (id 0348) no cálculo da folha referente ao mês de dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019906431-RH-Linha-Protheus-GPE-Por-que-pode-ser-apresentada-a-verba-de-desconto-Diferen%C3%A7a-de-13%C2%BA-Negativo-id-0348-no-c%C3%A1lculo-da-folha-referente-ao-m%C3%AAs-de-dezembro?source=search)  
[RH - Linha Protheus - GPE - Complemento 13º negativo impede a transmissão do S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062332213-RH-Linha-Protheus-GPE-Complemento-13%C2%BA-negativo-impede-a-transmiss%C3%A3o-do-S-1200?source=search)  
[RH - Linha Protheus - GPE - Cálculo de Complemento de 13º salário na Folha de Dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019750511-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Complemento-de-13%C2%BA-sal%C3%A1rio-na-Folha-de-Dezembro?source=search)  
[RH - Linha Protheus - GPE - Como configurar o sistema para gerar automaticamente valores de complemento de 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016519791-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-gerar-automaticamente-valores-de-complemento-de-13%C2%BA-Sal%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Como realizar a conferência do FGTS calculado referente ao Complemento da 2ª parcela de 13º na folha de dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019820072-RH-Linha-Protheus-GPE-Como-realizar-a-confer%C3%AAncia-do-FGTS-calculado-referente-ao-Complemento-da-2%C2%AA-parcela-de-13%C2%BA-na-folha-de-dezembro?source=search)  
[RH - Linha Protheus - GPE - Como realizar a conferência do INSS calculado referente ao Complemento da 2ª parcela de 13º na folha de dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020042351-RH-Linha-Protheus-GPE-Como-realizar-a-confer%C3%AAncia-do-INSS-calculado-referente-ao-Complemento-da-2%C2%AA-parcela-de-13%C2%BA-na-folha-de-dezembro?source=search)
