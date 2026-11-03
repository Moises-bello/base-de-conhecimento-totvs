---
article_id: 360025960231
category: Manutenção de Ativos (SIGAMNT)
content_hash: c7490398cc4e98f891e0574a5e9f6e66f7dc14d2032c192dae650e3566d3d0b8
fetched_at: '2026-06-28T22:42:34.354982+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Procedimento para gerar O.S automaticamente
  para os componentes da estrutura do bem pai
type: support-article
updated_at: '2021-06-09T17:53:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025960231-Manufatura-Linha-Protheus-MNT-Procedimento-para-gerar-O-S-automaticamente-para-os-componentes-da-estrutura-do-bem-pai
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Qual é o procedimento para gerar a **OS** automaticamente para os componentes da estrutura do bem pai?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Para que sejam geradas **O.S's** automaticamente, também para os componentes da estrutura do bem pai, é necessário verificar os parâmetros abaixo, e configurá-los da seguinte maneira:   
  
**MV\_NGNOVOS** **= 1**  
**MV\_NGPREVE = S**  
**MV\_NGVEROS** **= S**  
**MV\_NGGERPR** **= S**  
**MV\_NGOSAUT = S**   
**MV\_NGOSAES = S**  
  
**Glossário  
OS** - Ordem de serviço.  
**SS** - Solicitação de serviço.  
**MV\_NGNOVOS -** Quando gerar nova **OS**? 1=Gerar apenas quando não existir **OS** aberta para o mesmo bem, serviço e sequencia; 2=Gera mesmo se existir **OS** aberta.  
**MV\_NGPREVE -** Exibir alerta de manutenção preventiva atrasada 1=Abertura de **OS** Corretiva; 2=Abertura de **SS**; 3=**OS** Corretiva ou **SS**; 4=Não exibir).   
**MV\_NGVEROS -** Indica se deve verificar/gerar **OS** automática para contador com **OS** aberta. V=Consulta uma única vez; S=Consulta cada manutenção; N=Desabilitado.; C=Não consulta verifica/Não gera.  
**MV\_NGGERPR -** Indica se o Sistema deve gerar automaticamente **OS** preventiva, se após o reporte do contador, for identificado que a manutenção está vencida.   
**MV\_NGOSAUT -** Indica se deve gerar **OS** automaticamente sempre que uma **OS** por tempo for finalizada.   
**MV\_NGOSAES -** Indica se deve verificar e gerar **OS** automática por contador para os componentes da estrutura. S=Gera sem consultar, N=Não gera, C=Consulta usuário
