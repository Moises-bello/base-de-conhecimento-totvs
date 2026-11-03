---
article_id: 23768941623063
category: eSocial
content_hash: 59224613edad20e6d2b10385be34348bef97931a0139186f99fc65e95b365ef9
fetched_at: '2026-06-28T22:47:15.330996+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - eSocial - S-2500: O contrato de trabalho ja se encontra cadastrado
  na base de dados do Ambiente Nacional do eSocial'
type: support-article
updated_at: '2025-08-21T19:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23768941623063-RH-RM-RHU-eSocial-S-2500-O-contrato-de-trabalho-ja-se-encontra-cadastrado-na-base-de-dados-do-Ambiente-Nacional-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23768941599511) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao realizar o envio do evento S-2500 está sendo retornado o seguinte erro:   
  
*O contrato de trabalho ja se encontra cadastrado na base de dados do Ambiente Nacional do eSocial.Acao Sugerida: Verificar a matricula informada e, se ja utilizada em S-2190, S-2200, S-2300, S-2500 ou S-8200 de outro trabalhador, gerar uma nova matricula.*   
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2209.155 e superiores.**  
  
**Causa**Este erro ocorre quando já existe para o funcionário do Processo a ser enviado eventos anteriores ao eSocial, como os eventos admissionais(S-2190, S-2200, S-2300, etc), porém não foi informado no cadastro do Contrato de Trabalho no Processo Trabalhista.   
  
**Solução**Para correta geração, é necessário validar se o funcionário possui um dos eventos informados acima.   
Caso tenha, deve editar o Processo Trabalhista > Contrato de Trabalho > Campo '**Informações do evento**' e inserir a opção '**Sim**'.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34353727544599)  
  
Ainda assim, no campo '**Matricula**' deve informar a mesma matrícula enviada ao eSocial para os eventos admissionais deste funcionário.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34353727547543)  
  
**Saiba mais**  
- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
