---
article_id: 4414767580439
category: MDT - PPRA
content_hash: 4876abbf5a1468bb747c5fcf1867a7f19887fdbb11d47cf9a135e84f7eefd963
fetched_at: '2026-06-28T22:44:27.358819+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - O botão EPCs Bens ou EPCs M. C. não aparece na
  tela da rotina Risco x EPC (MDTA265) no modulo SIGAMDT
type: support-article
updated_at: '2025-09-05T16:43:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414767580439-RH-Linha-Protheus-MDT-O-bot%C3%A3o-EPCs-Bens-ou-EPCs-M-C-n%C3%A3o-aparece-na-tela-da-rotina-Risco-x-EPC-MDTA265-no-modulo-SIGAMDT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372546593175) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**O botão **EPCs Bens** ou **EPCs M. C.** não aparece na tela da rotina **Risco x EPC** (MDTA265) no modulo medicina e segurança do trabalho.  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Quando um dos botões **EPCs Bens** ou **EPCs M. C** não é demonstrado na rotina **Risco x EPC** (MDTA265) é devido a configuração do parâmetro **MV\_NG2UEPC.****Solução**Para ajuste acesse o Configurador (SIGACFG) no caminho: ambiente > cadastro > parâmetros. E busque pelo parâmetro **MV\_NG2UEPC**.  
  
Com a tela de parâmetros aberta defina uma das seguintes opções:  
1 = Bens;   
2 = Medidas de Controle;   
3 = Ambos.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414784359191)  
  
Caso tenha definido o parâmetro com 3 o sistema vai apresentar os dois botões na tela.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414784453015)  
  
**Observação**

* As informações do botão **EPCs Bens** vem do cadastro de Bens no SIGAMDT no caminho: **EPC > EPC (bem)** (MNTA080).
* As informações do botão **EPCs M. C.** vem do cadastro de medidas de controle no SIGAMDT no caminho: **PPRA > Medidas Controle** (MDTA135).
* Apenas Medidas de Controle do tipo proteção coletiva são demonstradas no botão **EPCs M. C.**

**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[MDT - PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
