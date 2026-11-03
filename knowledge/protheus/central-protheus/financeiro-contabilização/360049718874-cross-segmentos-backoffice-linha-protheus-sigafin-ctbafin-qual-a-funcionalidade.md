---
article_id: 360049718874
category: Financeiro - Contabilização
content_hash: 206418aa0cc963b850ee1b7d70888e65e1f36f0f59634c651f1f74e6d5b44633
fetched_at: '2026-06-28T22:38:05.358152+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Qual a funcionalidade
  do parâmetro MV_CTCHQBX
type: support-article
updated_at: '2023-01-25T21:47:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049718874-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Qual-a-funcionalidade-do-par%C3%A2metro-MV-CTCHQBX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **05:00 min  
  
Dúvida**Qual finalidade é utilizado o parâmetro **MV\_CTCHQBX**?  
  
**Ambiente**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Todas as versões

**Solução**

O parâmetro **MV\_CTCHQBX**permite definir em que momento será realizada a contabilização do**LP-590.**

* Caso o parâmetro esteja definido como **1 (Geração)**: Não é necessário que o cheque esteja liberado para que ocorra a Contabilização *Off-line* (**EF\_LIBER** = "N"). A contabilização online ocorrerá durante a geração do cheque sem a necessidade do mesmo estar liberado.

**Obs.** Não ocorrerá a contabilização durante a liberação do cheque.

* Caso o parâmetro esteja definido como**2 (Liberação)**: A contabilização do LP ocorrerá somente na liberação do cheque, ou através da rotina **CTBAFIN** caso o cheque já esteja liberado **EF\_LIBER** = "S".

**Obs.**  Caso o parâmetro **MV\_LIBCHEQ** esteja configurado com "S", o cheque será contabilizado no momento de sua geração, visto que já estará liberado.
