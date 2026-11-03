---
article_id: 360046551213
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 8f0d5d0f04ceed452fd76bbc90deeb28c405b2b04a3a9f1369f20d65e1d461cc
fetched_at: '2026-06-28T22:38:32.687761+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-type mismatch on +  on VLDLOCALIZ(SIGACUSB.PRX)
type: support-article
updated_at: '2021-04-28T15:53:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046551213-MP-FAT-type-mismatch-on-on-VLDLOCALIZ-SIGACUSB-PRX
---

**Ocorrência**

Ao selecionar um endereço na janela da consulta padrão, do campo **C6\_LOCALIZ** do pedido de venda (**MATA410**), é apresentado error.log:

**type mismatch on +  on VLDLOCALIZ(SIGACUSB.PRX) 03/01/2020 15:21:26 line : 3415**  
   
 **Ambiente**

Microsiga Protheus - todas as versões.  
   
 **Causa**

O erro ocorre por que o sistema está buscando o número de série do produto (**C6\_NUMSERI**) e não encontra, devido ao campo estar sem a marcação de usado.

**Solução**  
 Para solucionar essa ocorrência, via configurador , altere o campo **C6\_NUMSERI** e marque-o como usado, conforme a imagem abaixo, confirme a alteração do campo, salve a tabela e atualize o dicionário de dados.

![](https://totvssuporte.zendesk.com/attachments/token/VrkwnFvaFeROjzpGSae0Bm5JL/?name=inline-239889894.png)  
Obs: O campos **C6\_LOCALIZ**, **C6\_NUMLOTE** e **C6\_LOTECTL** também fazem parte da verificação, sempre mantê-los todos marcados como usado no configurador.
