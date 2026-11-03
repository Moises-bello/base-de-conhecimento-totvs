---
article_id: 4412694930711
category: RH - Soluções para error.log
content_hash: ea4c87e8217fdb5cb14d6728ba43815d9dc22fe9ae12f50e61003617070b2b65
fetched_at: '2026-06-28T22:44:09.000251+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - PON - Relatório de divergências gera error log: "argument
  #0 error, expected N->C, function __min2hrs on PN040IMP"'
type: support-article
updated_at: '2025-09-26T13:58:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412694930711-RH-Linha-Protheus-PON-Relat%C3%B3rio-de-diverg%C3%AAncias-gera-error-log-argument-0-error-expected-N-C-function-min2hrs-on-PN040IMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35218612614167) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar entrar na rotina de **Relatório de Divergências**, **PONR040** gera *error log* "***argument* #0 *error,**expected* N->C, *function* \_\_min2hrs *on* PN040IMP(PONR040.PRX)**"  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**O erro ocorre por inconsistência no **tipo** e/ou **conteúdo** do parâmetro **MV\_DIVTINT**.   
  
**Solução**Para que o erro não ocorra o parâmetro **MV\_DIVTINT** deve estar como **TIPO= NÚMERICO** e **CONTEÚDO= 0** (zero), ou maior:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412694811031)  
  
**Informações complementares:**Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>  
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)
