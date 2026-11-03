---
article_id: 360018869451
category: RH - Folha de Pagamento
content_hash: acd50075a8fd7e1171a534c747ac3e3b55858ddea8431786d691b285ef36b60d
fetched_at: '2026-06-28T22:44:16.246331+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Quando funcionário é afastado no dia 31 por licença
  maternidade e o período está definido para efetuar cálculo por 30 dias, é gerado
  30 dias de salário e nenhum de auxilio maternidade
type: support-article
updated_at: '2025-06-16T18:24:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018869451-RH-Linha-Protheus-GPE-Quando-funcion%C3%A1rio-%C3%A9-afastado-no-dia-31-por-licen%C3%A7a-maternidade-e-o-per%C3%ADodo-est%C3%A1-definido-para-efetuar-c%C3%A1lculo-por-30-dias-%C3%A9-gerado-30-dias-de-sal%C3%A1rio-e-nenhum-de-auxilio-maternidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26159319686039) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo Gestão de Pessoal, quando funcionário é afastado no dia 31 por licença maternidade, e o período está definido para efetuar cálculo por 30 dias, é gerado 30 dias de salário e nenhum de auxilio maternidade.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12  
  
**Causa**Quando a ausência por licença maternidade da funcionária inicia no dia 31 e os dias de cálculo no cadastro de período estiver com 30 o cálculo da folha não apresenta esse dia calculado com a verba especifica, isso não altera o valor recebido pelo funcionário mas tem impacto nas informações enviadas para o governo pois não fará a dedução do salário maternidade.  
  
**Solução**Efetuado tratamento para que, ao contrário dos demais tipos de afastamentos, a prioridade seja os dias de auxilio maternidade no momento de efetuar a proporcionalização dos dias.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Realize o *backup* prévio;  
**2.** Aplique o pacote de atualização:  
**12.1.2210: [https://suporte.totvs.com/portal/p/10098/download?e=1080347 (Garantia Estendida)](https://suporte.totvs.com/portal/p/10098/download?e=1080347)**  
**12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1123885>****12.1.2410: <https://suporte.totvs.com/portal/p/10098/download?e=1170810>**

**3.** Refaça o teste.  
  
**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
