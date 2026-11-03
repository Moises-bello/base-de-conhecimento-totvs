---
article_id: 20181026743831
category: Financeiro - Configurador
content_hash: ddb90795ddf58e0ac22db80d62e4c40f47199ca151826c15644591f504b38085
fetched_at: '2026-06-28T22:37:57.607032+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACFG - Como aumentar os campos
  de histórico
type: support-article
updated_at: '2023-12-29T11:56:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20181026743831-Cross-Segmento-Backoffice-Linha-Protheus-SIGACFG-Como-aumentar-os-campos-de-hist%C3%B3rico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20181070680215) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como aumentar o tamanho dos campos de histórico (E1\_HIST, E2\_HIST e E5\_HISTOR)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**

Foi criado um grupo de campos no configurador chamado **Histórico SE5.** Ao alterar este grupo de campos, o tamanho de todos os campos presentes no grupo serão alterados.   
  
Para entrar no grupo e alterar, realize os seguintes passos:

1. Acesse o **Configurador (SIGACFG)**;  
  
2. Acesse a aba **Banco de Dados** > **Dicionário de Dados** > **Grupo de Campos;**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20181026724247)  
  
3. Pesquise por: **115** - **Histórico SE5** e localize o grupo, clique em **Editar**;

4. Altere o tamanho do campo e **Confirme**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20181026727191)
