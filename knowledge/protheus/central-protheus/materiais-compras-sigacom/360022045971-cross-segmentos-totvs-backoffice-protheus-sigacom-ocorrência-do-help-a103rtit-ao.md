---
article_id: 360022045971
category: Materiais - Compras (SIGACOM)
content_hash: 9e24c767e557b8718d1994e5a2f06e727c9f0b6ca60156e0ce9bf9a8ffe63de1
fetched_at: '2026-06-28T22:41:10.128402+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ocorrência do Help
  A103RTIT ao tentar excluir Documento de Entrada
type: support-article
updated_at: '2023-06-19T19:45:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022045971-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncia-do-Help-A103RTIT-ao-tentar-excluir-Documento-de-Entrada
---

**Dúvida**Ocorrência do Help A103RTIT ao tentar excluir Documento de Entrada  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
  
**Solução**O Help em questão (A103RTIT), somente será apresentado quando tentamos Excluir o documento de Entrada e os títulos deste está sendo utilizado em outra operação.

Pois dentro da função, existe uma validação, que verifica o registro da tabela SE2 - Contas a Pagar, se registro não esta preso no banco por algum motivo.

![Help_A103RTIT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018790871/Help_A103RTIT.png)

Para que sistema permita a conclusão do processo, caso não esteja identificando o registro preso, deve-se reiniciar o serviço do TOP e efetuar novamente o processo.
