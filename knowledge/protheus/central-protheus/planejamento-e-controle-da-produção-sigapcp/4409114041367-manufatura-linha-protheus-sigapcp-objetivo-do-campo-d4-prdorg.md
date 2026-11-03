---
article_id: 4409114041367
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fc26dbc7390b46794cbced669cebf1334b4315097cc80fe28fdd7b68cfd2b570
fetched_at: '2026-06-28T22:42:44.660541+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Objetivo do campo D4_PRDORG
type: support-article
updated_at: '2021-09-21T13:32:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409114041367-Manufatura-Linha-Protheus-SIGAPCP-Objetivo-do-campo-D4-PRDORG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o objetivo do campo **D4\_PRDORG - Produto Original**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O campo **D4\_PRDORG** tem por objetivo sinalizar qual componente da estrutura foi substituído por um alternativo.   
Como no registro **0210 - Consumo Específico Padronizado**, existe a listagem de componentes necessárias para produção de um terminado item, quando ocorre a substituição de um desses componentes por outro na produção de uma **OP - Ordem de Produção**, é necessário indicador no registro **K235 - Insumos Consumidos** através do campo **COD\_INS\_SUBST - Código do Insumo que foi Substituído** qual foi o componente substituído e essa informação é obtida através do campo **D4\_PRDORG**.  
  
**Saiba mais**Para saber como o campo **D4\_PRDORG** é preenchido, acesse a documentação do *link:* [Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo D4\_PRDORG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409113675543-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-D4-PRDORG?source=search)
