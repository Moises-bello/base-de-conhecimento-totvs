---
article_id: 29275581416983
category: Evento S-2240
content_hash: 52b8a400838eb0d5e8c1dfb9914fa88540b5d96a8c11a60e7f2c33f930d82e3a
fetched_at: '2026-06-28T22:45:23.501835+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - Entity 'Colon' not defined [xmlParseMemory] Failed
  Parse XML
type: support-article
updated_at: '2025-01-17T13:08:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29275581416983-RH-Linha-Protheus-MDT-Entity-Colon-not-defined-xmlParseMemory-Failed-Parse-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29275597121687) **Tempo aproximado para leitura: 00:02:00 min****Ocorrência**Ao realizar transferências ou utilizar rotinas que geram os eventos S-2210, S-2220 e S-2240, o sistema apresenta o erro: Entity 'Colon' not defined [xmlParseMemory] Failed Parse XML

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29275581406999)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29275581407767)

**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões

**Causa**Este erro ocorre em geral devido alguns cadastros que compõem os eventos de SST possuírem textos com caracteres especiais (&></:; etc).  
  
**Solução**  
Para correção, faça a aplicação do pacote abaixo na ordem indicada e de acordo com sua release:

* Acumulado **[MDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773-RH-Linha-Protheus-MDT-Como-fazer-o-download-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-para-atualizar-o-modulo-medicina-e-seguran%C3%A7a-do-trabalho)**  
  [12.1.2310](https://suporte.totvs.com/portal/p/10098/download#detail/1125634)  
  [12.1.2410](https://suporte.totvs.com/portal/p/10098/download#detail/1174364)
* Pacote pontual - **[DNGRHUMDT-512](https://tdn.totvs.com/pages/releaseview.action?pageId=901950397)**  
  [12.1.2310](https://suporte.totvs.com/portal/p/10098/download?e=1179884)  
  [12.1.2410](https://suporte.totvs.com/portal/p/10098/download?e=1179886)

**Saiba Mais**[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
