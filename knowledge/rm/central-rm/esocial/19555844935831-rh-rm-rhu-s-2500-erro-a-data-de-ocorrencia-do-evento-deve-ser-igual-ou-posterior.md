---
article_id: 19555844935831
category: eSocial
content_hash: 3d944ae8204663cc577a1ce4b5cadbf1905adf1755c589b1ad722a70309ada8f
fetched_at: '2026-06-28T22:47:15.363023+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500 - Erro: A data de ocorrencia do evento; deve ser igual
  ou posterior ao inicio da obrigatoriedade deste evento;01/10/2023'
type: support-article
updated_at: '2025-08-11T13:58:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19555844935831-RH-RM-RHU-S-2500-Erro-A-data-de-ocorrencia-do-evento-deve-ser-igual-ou-posterior-ao-inicio-da-obrigatoriedade-deste-evento-01-10-2023
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19555861126167) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Ao gerar o XML do evento S-2500 aparece a mensagem de erro: **Erro:A data de ocorrencia do evento; deve ser igual ou posterior ao inicio da obrigatoriedade deste evento;01/10/2023.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155**e superiores.  
  
**Solução**

De acordo com a mensagem de erro, a mesma ocorre devido a data informada no campo 'Data da sentença'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34093738237719)

De acordo com o Leiaute do eSocial, a data da sentença deverá ser informada de acordo com os critérios abaixo:

a) Trânsito em julgado da decisão líquida proferida no processo trabalhista;  
b) Homologação de acordo judicial; ou  
c) Trânsito em julgado da decisão homologatória dos cálculos de liquidação da sentença.

***Obs: Deve ser uma data igual ou anterior à data atual, e que obedeça a data de início de obrigatoriedade do envio dos eventos referentes aos Processos Trabalhistas, sendo 01/10/2023.***

**Saiba mais**  
Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543-RH-RM-RHU-eSocial-Processos-Trabalhistas-Perguntas-e-respostas-do-evento-webinar)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783-RH-RM-RHU-eSocial-S-2500-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2500)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
