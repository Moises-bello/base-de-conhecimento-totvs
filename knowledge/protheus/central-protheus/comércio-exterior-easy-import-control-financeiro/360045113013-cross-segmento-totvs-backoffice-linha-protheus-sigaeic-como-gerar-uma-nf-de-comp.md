---
article_id: 360045113013
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 671924e292cf27d947490a9591dc69bef4e8ce1c0d092a816db49275359c0fff
fetched_at: '2026-06-28T22:39:44.454550+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAEIC - Como gerar uma
  NF de Complementar Despesa base de Custo
type: support-article
updated_at: '2021-12-22T18:42:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045113013-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-gerar-uma-NF-de-Complementar-Despesa-base-de-Custo
---

**Dúvida**Como gerar uma NF de Complementar para uma Despesa base de custo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

Quando a despesa for complementar o custo, cadastrar da seguinte forma, no Módulo 17- SIGAEIC em:  
Atualizações \ Financeiro \ Cadastro de Despesas(EICA110):

- Base de custo = SIM

- Base de imposto = NÃO

- Base de ICMS = NÃO

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001330441/mceclip0.png)

Para gerar a nota complementar, realizar o seguinte procedimento:

1. Acessar a rotina desembaraço\Manutenção (EICDI502), posicionar no processo a ser gerada a nota complementar, selecione em outras ações\Despesa, informar a despesa base de custo e confirmar.  
2. Acessar a rotina de Desembaraço\Recebimento de Importação(EICDI154), posicionar no processo, selecione Complementar.
