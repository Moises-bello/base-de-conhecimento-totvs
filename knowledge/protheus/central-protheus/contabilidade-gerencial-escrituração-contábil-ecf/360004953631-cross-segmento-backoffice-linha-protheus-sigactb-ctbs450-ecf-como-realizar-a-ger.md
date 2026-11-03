---
article_id: 360004953631
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 788f2ca3a28e4b0743d73673e54590112658e2470684090a3ac78faa07654fc5
fetched_at: '2026-06-28T22:40:47.296959+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS450 - ECF-  Como
  realizar a geração do bloco V - DEREX?
type: support-article
updated_at: '2021-06-29T23:50:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004953631-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS450-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-do-bloco-V-DEREX
---

**Duvida:**

Como realizar a geração do Bloco V - DEREX?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus -Contabilidade Gerencial - todas as versões

**Solução:**

Passo 1 - Importar modelo da visão gerencial (CTBA161): <http://tdn.totvs.com/pages/viewpage.action?pageId=189314312>

Passo 2 - Incluir e amarrar a configuração do livro com a visão gerencial (CTBA130)

Passo 3 - Cadastrar o bloco V (CTBS450): V010, V020, V030

Passo 4 - Ao gerar a revisão através da rotina CTBS001, gerar a revisão da escrituração informando as perguntas:

* DEREX = Selecione SIM
* Cod. Identif. Bloco V - DEREX = Selecione o código do cadastro criado na rotina CTBS450

Passo 5 - Através do Módulo TAF acesse a rotina TAFA507(DEREX) verifique se o sistema alimentou

Veja documentação : [Criação do bloco V - DEREX - Campos e Rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=354470450)

Para maiores informações, acessar o link: <http://tdn.totvs.com/display/public/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF>

Página Centralizadora: <http://tdn.totvs.com/display/PROT/ECF>

Para criar campo e tabelas do Derex execute :[Atualização do SPED ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211)

<https://tdn.totvs.com/display/public/PROT/ECF_SPED_CONTABIL_FISCAL_Alteracoes_para_Leiaute_4_00>

[Bloco V - Declaração DEREX](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512)

* Tabela -  V1Q (Cadastro de Instituição Financeira)
* abela -  V1S

#
