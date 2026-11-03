---
article_id: 360025501133
category: MDT - PCMSO
content_hash: fb3c0511d593acad36b7f7d3f8ce3b4bd147b937915cc89755c1f4564f774876
fetched_at: '2026-06-28T22:44:28.465140+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Não foi possível visualizar os exames pendentes,
  pois o CNAE não está informado ou está incorreto nos dados cadastrais da empresa
type: support-article
updated_at: '2021-04-27T21:51:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025501133-RH-Linha-Protheus-MDT-N%C3%A3o-foi-poss%C3%ADvel-visualizar-os-exames-pendentes-pois-o-CNAE-n%C3%A3o-est%C3%A1-informado-ou-est%C3%A1-incorreto-nos-dados-cadastrais-da-empresa
---

**Dúvida**Ao acessar: **Atualizações > PCMSO > Exames para Demissão (MDTA280)**  Selecionar o **Funcionário >Outras Ações > Exames**,  o sistema apresenta a seguinte mensagem de inconsistência: “Não foi possível visualizar os exames pendentes, pois o CNAE não está informado ou está incorreto nos dados cadastrais da empresa”.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040131613/mceclip0.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Para a correção, faça os seguintes procedimentos:  
  
1. Verifique os registros da Empresa nas rotinas **MDTA082** (Intervalo CID X CNAE), **MDTA880** (CNES) e **MDTA281** (Atividades Econômicas), todas essas rotinas estão no menu do SIGAMDT no caminho: atualizações > cadastros básicos. Caso não possua os registros, efetue os cadastros;  
  
2. O Código do CNAE na rotina **MDTA281** (Atividades Econômicas), deve estar idêntico ao do SIGACFG (Configurador) **Ambiente > Empresas >Filial.**

**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho)
