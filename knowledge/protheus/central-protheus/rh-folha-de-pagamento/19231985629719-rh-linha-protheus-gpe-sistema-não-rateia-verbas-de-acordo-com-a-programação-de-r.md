---
article_id: 19231985629719
category: RH - Folha de Pagamento
content_hash: 1e6eaa73d3bfd91bffe49a5e886df4946fd26a058a4bd33c7f9a846974b8ef7f
fetched_at: '2026-06-28T22:44:16.390163+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não rateia verbas de acordo com a programação
  de rateio do funcionário, quando no cálculo existe verba informada ou gerada
type: support-article
updated_at: '2024-09-03T17:41:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19231985629719-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-rateia-verbas-de-acordo-com-a-programa%C3%A7%C3%A3o-de-rateio-do-funcion%C3%A1rio-quando-no-c%C3%A1lculo-existe-verba-informada-ou-gerada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19231982711063) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Sistema não rateia verbas de acordo com a programação de rateio do funcionário, quando no cálculo existe verba informada ou gerada.  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Verbas de origem I ou G estão com o campo **RV\_ENCARCC = B,** pois nessa configuração será considerado apenas os centros de custo **incluídos,** ou seja, a programação de rateio será **desprezada.**

Atualizações - Definições de Cálculo - Verbas - aba **Contabilização**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19232000545303)  
  
**Solução**Verbas de origem **I ou G não** devem ter o campo **RV\_ENCARCC = B,** precisam estar com o conteúdo **S:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19232012619031)**

**Observações**

1. Além da parametrização correta do campo **RV\_ENCARCC = S**, o mnemônico **P\_LRATINFO** deve estar com o conteúdo **.T.**, para que a verba informada (origem I) ou gerada (origem G) seja rateada de acordo com a programação de rateio.
2. Se o mnemônico P\_LRATINFO estiver como .T., **não importarão os Centros de Custos informados no lançamento** para o sistema, pois será respeitada apenas a configuração de rateio do funcionário;
3. Se o mnemônico P\_LRATINFO estiver como .F., o sistema funcionará como era anteriormente, ou seja, **não rateará a verba e respeitará exatamente o que foi informado**.
4. Conforme conceito do rateio, deverá haver **ao menos uma verba** configurada como Base para o rateio (campo **RV\_ENCARCC = B)** e as demais, que deverão ser rateadas com o campo **RV\_ENCARCC = S**.

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[1317775 DRHPAG-9124 DT Calculo Rateio Informada](https://tdn.totvs.com/display/PROT/1317775+DRHPAG-9124+DT+Calculo+Rateio+Informada)

[RH - Linha Protheus - GPE - Como realizar a programação de rateio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018658931-RH-Linha-Protheus-GPE-Como-realizar-a-programa%C3%A7%C3%A3o-de-rateio?source=search)
