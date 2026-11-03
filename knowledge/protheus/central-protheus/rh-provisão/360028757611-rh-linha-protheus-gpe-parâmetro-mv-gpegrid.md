---
article_id: 360028757611
category: RH - Provisão
content_hash: 4e7d133e75ef40c5d913286e88fb997e0322024f214272f541cd2a4b926f8a2d
fetched_at: '2026-06-28T22:43:55.968613+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Parâmetro MV_GPEGRID
type: support-article
updated_at: '2025-10-24T12:38:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028757611-RH-Linha-Protheus-GPE-Par%C3%A2metro-MV-GPEGRID
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998214946583)** Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**Como funciona o parâmetro MV\_GPEGRID?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Implementada melhoria no módulo Gestão de Pessoal (SIGAGPE), com a criação do novo parâmetro MV\_GPEGRID, com o objetivo de habilitar o modo de execução GRID para apenas uma ou ambas as rotinas: Provisão mensal de Férias e 13º Salário e Cálculo Folha, 13º.

Para que seja habilitado o modo GRID apenas para Provisão, configure o parâmetro MV\_GPEGRID com conteúdo 1, ou para habilitar apenas as rotinas de Cálculo Folha, 13º.,Adiantam., configure-o com conteúdo 2.

Para habilitar todas as rotinas citadas, deixe-o em branco.  
  
**Importante!**O parâmetro MV\_GPEGRID somente será considerado se, previamente, for habilitado o parâmetro MV\_GRID (.T.).  
  
Procedimento para utilização:  
1. No Configurador (SIGACFG) acesse Ambientes/ Cadastro/Parâmetros (CFGX018), configure o parâmetro MV\_GPEGRID.

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
