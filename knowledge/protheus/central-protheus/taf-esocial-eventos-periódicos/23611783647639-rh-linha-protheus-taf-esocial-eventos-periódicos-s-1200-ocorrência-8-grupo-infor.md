---
article_id: 23611783647639
category: TAF - eSocial - Eventos Periódicos
content_hash: 88634de8e582261d56c45fcdcf3f997c80b927a4e0ac844904f9ee3daa942878
fetched_at: '2026-06-28T22:45:19.012375+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1200 - ocorrência
  8, Grupo 'Informacoes complementares de identificacao do trabalhador' deve ser preenchido.
  Verifique as condicoes de preenchimento no leiaute.
type: support-article
updated_at: '2026-06-24T21:54:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23611783647639-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1200-ocorr%C3%AAncia-8-Grupo-Informacoes-complementares-de-identificacao-do-trabalhador-deve-ser-preenchido-Verifique-as-condicoes-de-preenchimento-no-leiaute
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23611813977623) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Ao tentar transmitir o evento do eSocial S-1200 (TAFA250), Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social, ocorre a inconsistência:

*Codigo da ocorrência: 8*

*Localização:/eSocial/evtRemun/ideTrabalhador*

*Descrição: Grupo 'Informacoes complementares de identificacao do trabalhador' deve ser preenchido. Verifique as condicoes de preenchimento no leiaute.*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23611813981079)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Periódicos - S-1200 - Todas as versões  
  
**Solução**Para solucionar a inconsistência, retornada pelo governo (eSocial):

1. Verifique se o sistema está com atualização do mês 04/2024 ou posterior.

Acesse a tela de diagnostico do TAF para confirmar a última atualização:

[Automação Fiscal - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23611783610135)

2. Se o sistema estiver com atualização anterior á 04/2024:

A) aplique a patch pontual disponibilizada abaixo, conforme versão do Protheus (enquanto a mesma permanecer disponível no nosso Portal TOTVS)

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1143596> ; 12.1.2310:<https://suporte.totvs.com/portal/p/10098/download?e=1143597> ; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1143598> ;  
  
B) Ou aplique a última expedição continua do TAF, onde a correção já está contemplada, conforme versão do Protheus:

12.1.2210

<https://suporte.totvs.com/portal/p/10098/download?e=1084563>

12.1.2310

<https://suporte.totvs.com/portal/p/10098/download#detail/1126399>

12.1.33

<https://suporte.totvs.com/portal/p/10098/download?e=1043538>  
  
3. Após atualizar ou aplicar a patch, teste a transmissão novamente.  
  
**Saiba Mais**

[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)
