---
article_id: 34953074585367
category: Rental by ItUp Business
content_hash: ba26b161a2479aab2539d92044ad68baf26ee205229537f99b9f39613a062c66
fetched_at: '2026-06-28T22:36:20.486643+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Ao gerar a Nota Fiscal de
  Remessa, é exibida a mensagem de HELP informando que o valor está zerado.
type: support-article
updated_at: '2025-09-15T17:44:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34953074585367-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Ao-gerar-a-Nota-Fiscal-de-Remessa-%C3%A9-exibida-a-mensagem-de-HELP-informando-que-o-valor-est%C3%A1-zerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34953074559639) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao gerar a Nota Fiscal de Remessa, o sistema apresenta um aviso informando que o item "X" está com o valor zerado.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Causa**  
Ao gerar a Nota Fiscal de Remessa de um contrato de locação na rotina **LOCA001** – **Orçamento**, o sistema exibe o seguinte aviso:

> **"O item 'X' está com o valor zerado.**  
> **Favor verificar o cadastro do produto 'PREÇO VENDA' (B1\_PRV1), ou o cadastro do bem 'VALOR COMPRA' (T9\_VALCPA), se for o caso."**

Esse aviso ocorre quando o sistema não encontra o valor do item informado, seja no cadastro do produto ou do bem, impedindo a correta geração do contrato.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o produto selecionado no campo **"PRODUTO (FPA\_PRODUT)"** possui o campo **"PREÇO VENDA (B1\_PRV1)"** preenchido no seu cadastro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34953074560919)  
  
2. Caso o campo **"PREÇO VENDA (B1\_PRV1)"** não seja utilizado no processo, é necessário informar o valor diretamente no **CADASTRO DO BEM**, no campo **"VALOR COMPRA (T9\_VALCPA)"**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34953074562455)  
  
Após o preenchimento correto de um dos campos mencionados, o aviso deixará de ser exibido e o processo de geração do contrato poderá ser concluído com sucesso.
