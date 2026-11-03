---
article_id: 1500011759042
category: Evento S-2240
content_hash: 2210c19d88ef68c0e702c83801f01d787e8f5d40273955c8bc4a657b90440de6
fetched_at: '2026-06-28T22:45:23.694696+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - O campo Cod. eSocial (TN5_ESOC)
  está bloqueado na rotina Tarefa por Func. (MDTA090) no SIGAMDT
type: support-article
updated_at: '2025-03-03T17:59:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011759042-RH-Linha-Protheus-MDT-eSocial-S-2240-O-campo-Cod-eSocial-TN5-ESOC-est%C3%A1-bloqueado-na-rotina-Tarefa-por-Func-MDTA090-no-SIGAMDT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372178675351)**Tempo aproximado para leitura: **00:02:00 min****Ocorrência**O campo **Cod.eSocial** (TN5\_ESOC) está bloqueado na rotina **Tarefa por Func.** (MDTA090) no modulo Medicina de Segurança do Trabalho (SIGAMDT)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**O campo **Cod.eSocial** (TN5\_ESOC) era responsável por gerar a tag **codAtiv**, porem essa tag não é mais utilizada no layout simplificado do **eSocial**. Por isso no sistema ele foi bloqueado para digitação.  
  
**Solução**Devido a informação do campo **Cod.eSocial** (TN5\_ESOC)  não ser mais necessária no layout ele pode aparecer bloqueado em branco, ou bloqueado com o código que já estava informando anteriormente. Nesse caso não é necessario fazer nada, o sistema já está preparado para não enviar a tag **codAtiv** mesmo que tenha dados no campo.  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
