---
article_id: 14178815918487
category: TAF - REINF
content_hash: 8b225845e531b52b1480e8d10ec1829921097863867f156a02819f390ac2f734
fetched_at: '2026-06-28T22:41:33.727021+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como informar despesas
  e processos judiciais  diretamente no TAF
type: support-article
updated_at: '2023-04-27T18:24:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14178815918487-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-informar-despesas-e-processos-judiciais-diretamente-no-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como informar despesas e processos judiciais diretamente no TAF ?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - a partir da versão 12.  
  
**Solução**

Caso o título a pagar seja decorrente de uma decisão judicial ou RRA, nos eventos R-4010 e R-4020 são solicitadas informações sobre o processo judicial e suas despesas (registros "infoProcJud" e "infoRRA").

Como nos módulos do Backoffice Protheus não há esse tipo de detalhamento, essas informações deverão ser inseridas diretamente no TAF.

**Passo 1.**

Faça a integração com o TAF através do Extrator Fiscal (EXTFISXTAF). Certifique  se os layouts T154  e T158  foram gerados:

![tela_c.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14176346780695)

**Passo 2.**

Cadastre no TAF os dados das despesas processuais através da rotina  **TAFA541** ( Despesas Processuais)  e   advogados no  (cadastro  advogados ) **TAFA537**

Este cadastro pode ser preenchido de forma manual por meio da rotina **TAFA541:**

**Despesas Processuais**

![tre.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14176779990423)

**Cadastro Advogados**

Este cadastro pode ser preenchido de forma manual através da rotina **TAFA537**

O numero de Inscrição do advogado (CPF ou CNPJ) e os valores com advogados vinculados ao processo judicial e/ou RRA serão apresentados nos eventos R-4010 e R-4020 quando o rendimento possuir um código de Despesas Processuais que possui um advogado listado como despesa do processo.

![t34.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14176979101591)

**Passo 4.**

Faça o vinculo do processo judicial no programa **TAFA448** (Faturas) e **TAFA535** (Pagamentos);

**Pagamento**

![t44.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14177305566231)

**Fatura**

![t55.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14178115295255)
