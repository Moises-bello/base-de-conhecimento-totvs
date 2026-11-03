---
article_id: 4415306824343
category: RH - Soluções para error.log
content_hash: 8406f9c30453038086b003cefc6e193c8789ccf6c4180d5439384c98eac6ffc3
fetched_at: '2026-06-28T22:44:09.043118+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Ao tentar imprimir CAT gera error log - array out
  of bounds ( 2 of 0 ) on { |CERR| AADD( _ALOGEXECROT[ 2 , 2 ] , CERR ) }(GPEXFORM.PRX)
type: support-article
updated_at: '2025-09-12T11:39:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415306824343-RH-Linha-Protheus-GPE-Ao-tentar-imprimir-CAT-gera-error-log-array-out-of-bounds-2-of-0-on-CERR-AADD-ALOGEXECROT-2-2-CERR-GPEXFORM-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34890102136855) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar imprimir a CAT (Comunicação de Acidente de Trabalho), através da rotina MDTR830 gera *error log*: "*array out of bounds* ( 2 *of* 0 ) *on* { |CERR| AADD( \_ALOGEXECROT[ 2 , 2 ] , CERR ) }(GPEXFORM.PRX)"  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**O erro ocorre por se tratar de problemas na **estrutura** da tabela de **RC3** (Fórmulas)  
  
**Solução**Para solucionar o problema, será necessário:  
**1.** Efetuar backup da tabela RC3;  
**2.** Recriar a tabela;  
**3.** Efetuar os procedimentos da documentação abaixo:  
[RH - Linha Protheus - GPE - Como recriar apenas roteiros e fórmulas do módulo 07 Gestão de Pessoal (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044572434-RH-Linha-Protheus-GPE-Como-recriar-apenas-roteiros-e-f%C3%B3rmulas-do-m%C3%B3dulo-07-Gest%C3%A3o-de-Pessoal-SIGAGPE-?source=search)

**Saiba Mais:**

[RH - Soluções para Error Log](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115003853987-RH-Solu%C3%A7%C3%B5es-para-error-log)   
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>   
Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)
