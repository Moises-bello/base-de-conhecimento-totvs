---
article_id: 4415224031255
category: RH - Soluções para error.log
content_hash: 2ce03cebb314b72ff722105ceed91847b9dadded55a6c872d790c77650044904
fetched_at: '2026-06-28T22:44:10.012340+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - MDT - Error log ao efetuar entrega de EPI em Funcionário
  X EPI - variable does not exist CTBLTRNS on MDTVLDRIS(MDTESOCIAL.PRW)
type: support-article
updated_at: '2021-12-07T18:07:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415224031255-RH-Linha-Protheus-MDT-Error-log-ao-efetuar-entrega-de-EPI-em-Funcion%C3%A1rio-X-EPI-variable-does-not-exist-CTBLTRNS-on-MDTVLDRIS-MDTESOCIAL-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao realizar uma **entrega de EPI** à um Funcionário, através da rotina em **Funcionário X EPI**, **MDTA695**, gera *error log*: "***variable does not exist* CTBLTRNS *on* MDTVLDRIS(MDTESOCIAL.PRW)**"  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**O erro ocorre em ambiente com o fonte **MDTESOCIAL** com data anterior a  **04/12/2021**  
  
**Solução**Para correção, será necessário aplicar o pacote baixo:  
12.1.17:<https://r.totvs.io/p/1053347> ;   
12.1.25:<https://r.totvs.io/p/1053348> ;   
12.1.27:<https://r.totvs.io/p/1053349> ;   
12.1.33:<https://r.totvs.io/p/1053350> ;  
  
**Informações complementares**  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>   
Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)
