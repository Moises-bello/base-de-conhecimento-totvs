---
article_id: 360015451892
category: RH - Folha de Pagamento
content_hash: 8e042767bc15bc39c19351d4493bac9e7dcd37263d051dfa94d78f94eb58e03f
fetched_at: '2026-06-28T22:44:16.106221+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - O sistema está considerando 30 dias de referência
  no calculo da folha, para funcionário afastado em meses de 31 dias
type: support-article
updated_at: '2025-09-12T14:38:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015451892-RH-Linha-Protheus-GPE-O-sistema-est%C3%A1-considerando-30-dias-de-refer%C3%AAncia-no-calculo-da-folha-para-funcion%C3%A1rio-afastado-em-meses-de-31-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26264802519959) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**No módulo **Gestão de Pessoal**, ao incluir um afastamento em meses de 31 dias (GPEA240), o calculo da folha apresenta referência de 30 e não 31 dias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**O sistema respeita o parâmetro MV\_DIASPER, onde o mesmo está configurado para pagar 30 dias e não os dias do mês.  
  
**Solução**O funcionário em questão é mensalista, e se não estivesse afastado receberia por 30 e não 31, a soma dos dias trabalhados tem que dar 30 de acordo com  **MV\_DIASPER** e a baixa na SR8 (tabela de afastamentos) dias corridos, pois é assim que o INSS conta dias corridos.

Dessa forma, a soma dos dias trabalhados e auxilio será 30 dias.

Ou seja, será **reduzido** um dia de afastamento nos meses de 31 dias, para que não seja pago 1 dia a mais de salário. Porém, para o **INSS serão considerados os dias corridos**.

Na versão 11, reduzíamos 1 dia de salário para que fosse apresentado os 15 dias de afastamento. Na versão 12 foi executado o processo inverso devido a não podermos inibir 1 dia do total de dias trabalhados.

Outra opção seria informar nos tipos de afastamento (Ausência), a verba de salário, desta forma será apresentado os 30 dias como salário, uma vez que a verba de auxílio é apresentada somente para mostrar os dias pagos referente ao **período de afastamento.**

Caso a empresa queira pagar 31 dias no mês de afastamento, deverá ajustar o parâmetro MV\_DIASPER para considerar os dias do mês, ou efetuar uma customização por meio do roteiro para que em caso de afastamento considere 31 dias, independente da configuração do parâmetro.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[TUKE03\_Calculo\_Folha\_de\_Pagamento\_MV\_DIASPER\_Afastamentos](http://tdn.totvs.com/display/PROT/TUKE03_Calculo_Folha_de_Pagamento_MV_DIASPER_Afastamentos)
