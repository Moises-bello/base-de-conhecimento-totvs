---
article_id: 33719695145367
category: Rental by ItUp Business
content_hash: 57091ad576199b6afca2762e220893d487c8b3f525f75dab24cc91a921ec1b19
fetched_at: '2026-06-28T22:36:20.703593+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGALOC - RENTAL: LOCA00196 A quantidade
  não pode ser superior a 1.'
type: support-article
updated_at: '2025-07-25T17:41:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33719695145367-Cross-Segmentos-Backoffice-Protheus-SIGALOC-RENTAL-LOCA00196-A-quantidade-n%C3%A3o-pode-ser-superior-a-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33719695118871) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Quando altero a quantidade no campo **FPA\_QUANT** (**QUANTIDADE**) o sistema apresenta um **HELP**  
  
**HELP**: RENTAL: LOCA00196   
**Problema**: Inconsistência nos dados.  
**Solução**: A quantidade não pode ser superior a 1.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC -A partir da release P12.1.2410.  
  
**Causa**  
Estou utilizando um produto cujo campo **B1\_GRUPO** (**Grupo**) está devidamente preenchido, e este grupo está informado no parâmetro **MV\_LOCX014**.

No entanto, ao tentar utilizar esse produto na rotina **LOCA001** – **Orçamento**, o sistema exibe a seguinte mensagem de ajuda: **RENTAL: LOCA00196**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **MATA035 Grupo de Produtos**;  
2. Selecione o Grupo que está sendo utilizado e faça uma alteração;  
3. Localize o campo **BM\_XACESS (Tp. Rental)** e coloque o valor de "1- Acessórios".
