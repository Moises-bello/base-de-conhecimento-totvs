---
article_id: 360028507631
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 1b3508ea135d54cc981656d72ffdd7c77fa380e91fc084c11a2474f1eafd7477
fetched_at: '2026-06-28T22:38:31.128403+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT -Integração mata030 x GFE - Nofuncw - Opção não disponível no Protheus  Função-
  GFEXIEMITM Called by OMSEMITMP
type: support-article
updated_at: '2021-04-28T15:54:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028507631-MP-FAT-Integra%C3%A7%C3%A3o-mata030-x-GFE-Nofuncw-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-GFEXIEMITM-Called-by-OMSEMITMP
---

**Ocorrência**

Ao alterar um registro no cadastro de cliente (**MATA030**) com integração GFE, está gerando o help:

**Nofuncw - Problema: Opção não disponível no Protheus**

**Função: GFEXIEMITM Called by OMSEMITMP**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028620551/mceclip0.png)  
 **Ambiente**

Microsiga Protheus -  a partir da versão 12.

**Causa**

A falta de função (**NOFUNCW**), indica que o fonte onde a função foi criada deve estar desatualizado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **GFEXINTA:**

**<https://suporte.totvs.com/portal/p/10098/download?e=728490>**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
