---
article_id: 26762659061911
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1e21cc47e60d82334cd5d99310017c8409a78c9a28689b1f13efd9850b089a41
fetched_at: '2026-06-28T22:39:12.560680+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como encerrar uma
  OP parcial ?
type: support-article
updated_at: '2025-03-12T12:45:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26762659061911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-encerrar-uma-OP-parcial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26762691943447) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao tentar encerrar uma OP na rotina Apontamento de Produção, ocorre a mensagem de erro

**"Produto XPTO possui saldo empenhado para a OP"**. Como resolver?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

A respeito do Help apresentado **"Produto XPTO possui saldo empenhado para a OP"**, para o mesmo não ser mais exibido é necessário desativar o parâmetro [MV\_CBPE004](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302467-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Par%C3%A2metros-SX6-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados) (Validação do Encerramento da OP - Mata250)pois o parâmetro realiza a validação direto no encerramento da OP e também valida o fonte **ACDA250ENOK.PRW**.

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
