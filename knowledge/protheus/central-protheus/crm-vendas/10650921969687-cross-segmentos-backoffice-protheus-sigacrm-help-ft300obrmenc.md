---
article_id: 10650921969687
category: CRM - Vendas
content_hash: 4110de24aeac0c72888946ea6bc352885a719df799f25a053f75a862cb497c75
fetched_at: '2026-06-28T22:40:25.827354+00:00'
product: protheus
section_id: 1500001549102
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Help FT300OBRMENC
type: support-article
updated_at: '2024-03-25T20:27:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10650921969687-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Help-FT300OBRMENC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22327247462679) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao tentar salvar uma oportunidade apresenta o "Help: FT300OBRMENC Por favor, informe um tipo de encerramento"  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da versão 12.1.17  
  
**Causa**Para o sistema apresentar esta mensagem significa que quando preenche o **Status** = **Perdido** ou **Suspenso** é necessário preencher o **tipo de encerramento** e o **motivo**.   
  
**Solução**

Para cadastrar o tipo de encerramento é necessário acessar a rotina: **TMKA220  
![tipo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10650881277335)**  
  
Preencha os campos abaixo para encerrar a oportunidade:

* Fator Critico de Insucesso: F.C.I - **AD1\_FCI**;
* Status: **AD1\_STATUS**;
* Encerramento: **AD1\_ENCERR;**
* Motivo: **AD1\_COMUNI.**

**![perdido.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10650901186455)**
