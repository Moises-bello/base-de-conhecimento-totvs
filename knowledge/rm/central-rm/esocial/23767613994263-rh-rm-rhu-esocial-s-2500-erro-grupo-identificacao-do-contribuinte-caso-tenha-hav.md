---
article_id: 23767613994263
category: eSocial
content_hash: 02dab217e15ca0720f11a340032d0fb266add91a5180f9b4fa39b0d52e67060b
fetched_at: '2026-06-28T22:47:15.334865+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - eSocial - S-2500: Erro: Grupo Identificacao do contribuinte,
  caso tenha havido imposicao de responsabilidade indireta nao deve ser preenchido'
type: support-article
updated_at: '2025-08-21T19:19:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23767613994263-RH-RM-RHU-eSocial-S-2500-Erro-Grupo-Identificacao-do-contribuinte-caso-tenha-havido-imposicao-de-responsabilidade-indireta-nao-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23767604418583) Tempo aproximado para leitura: **00:01:33 min****Ocorrência**Ao gerar o XML do evento S-2500, a seguinte mensagem de erro é exibida:

***Grupo #39;Identificacao do contribuinte, caso tenha havido imposicao de responsabilidade indireta#39; nao deve ser preenchido. Verifique as condicoes de preenchimento no leiaute.***   
***- Localização : /eSocial/evtProcTrab/ideEmpregador***   
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2209.155 e superiores.**  
  
**Causa**A mensagem de erro ocorre quando os campos **'Tipo Inscrição'** e **'Numero Inscrição'** presentes na guia **'Identificação do Processo'** estão preenchidos, porém não trata-se de uma ação com responsabilidade indireta.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34353554636567)  
  
  
**Solução**Para correção do erro no XML do evento os campos devem estar em branco, pois só precisam ser preenchidos caso haja responsabilidade indireta, no qual deve ser informados os dados de identificação do responsável direto.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23767613960727)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23767613968151)  
  
Após ajustes, salve as alterações e gere o XML novamente.   
  
**Saiba mais**- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)  
- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)  
- [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
