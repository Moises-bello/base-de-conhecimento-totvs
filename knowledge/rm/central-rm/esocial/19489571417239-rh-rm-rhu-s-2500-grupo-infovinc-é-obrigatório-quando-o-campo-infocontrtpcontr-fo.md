---
article_id: 19489571417239
category: eSocial
content_hash: 80d970beba361cc0f5850476735565a8f6a60d19966f82fb92a39a92cac2826b
fetched_at: '2026-06-28T22:47:15.381979+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: RH - RM - RHU - S-2500 - Grupo infoVinc é obrigatório quando o campo 'infoContr/tpContr'
  for diferente de [6]
type: support-article
updated_at: '2024-09-30T11:19:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19489571417239-RH-RM-RHU-S-2500-Grupo-infoVinc-%C3%A9-obrigat%C3%B3rio-quando-o-campo-infoContr-tpContr-for-diferente-de-6
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19489555601815) Tempo aproximado para leitura: 00**:01:00 min**

**Dúvida**Ao gerar o XML do evento S-2500, é exibida a seguinte mensagem de erro: **Grupo infoVinc é obrigatório quando o campo 'infoContr/tpContr' for diferente de [6].**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155**e superiores.  
  
**Solução**

A mensagem de erro ocorre devido ao não preenchimento da Guia Informações de vínculo dentro do cadastro do Contrato de Trabalho quando o mesmo for diferente de 6 - Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício.  
   
   
![image.png](https://totvssuporte.zendesk.com/attachments/token/FrmPwQQFmRbeYvI2UaenHPZS4/?name=image.png&lotus_request=true)  
![image.png](https://totvssuporte.zendesk.com/attachments/token/B6WfIKHflSscrGGIZR1eQ3Z4j/?name=image.png&lotus_request=true)  
 

De acordo com o Leiaute do eSocial, quando o Tipo de Contrato for diferente de 6, é obrigatório informar a Guia Informações de Vínculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19489572157591)

Após realizar os ajustes no cadastro do contrato, salve as modificações feitas na visão e realize a geração do XML novamente para efetuar o envio.

**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
