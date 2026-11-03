---
article_id: 1500009863821
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1b8e6c01ae9dc6c532987219a415d6317a96faca2ba3f5c9898ed2cbd1d41d43
fetched_at: '2026-06-28T22:42:42.191542+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Desdobramento no cadastro da operação
type: support-article
updated_at: '2021-05-11T10:48:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009863821-Manufatura-Linha-Protheus-SIGAPCP-Desdobramento-no-cadastro-da-opera%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Qual a funcionalidade do**desdobramento** no cadastro da **operação**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Se utilizado a opção **desdobramento** no cadastro da **operação** na rotina **MATA632 - Operações**, no **MATA690- Carga Máquina** irá alocar a **operação** de modo a produzir no menor tempo possível, dividindo a produção com todos os **recursos** cadastrados como **alternativos**, para o **recurso** dessa **operação**.  
O tipo de **desdobramento** é cadastrada através do campo **G2\_TPDESD - Tipo de Desdobramento**, onde pode ser definido como **tempo** ou **quantidade** e no campo **G2\_TEMPDES - Tempo de Desdobramento**, é definido o **tempo** de **desdobramento**.  
  
Exemplo de uso:  
**Desdobramento por tempo**: 6h de produção, tenho 3 recursos cadastrados, cada recurso vai trabalhar 2h da produção, em simultâneo.   
  
**Desdobramento** **por quantidade:** 60 peças para produzir, tenho 3 recursos cadastrados, cada recurso vai produzir 20 peças ao mesmo tempo.
