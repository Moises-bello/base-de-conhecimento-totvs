---
article_id: 360007249591
category: Financeiro - Contas a Receber
content_hash: 071a095c56a466a59745ccdecb534006a0a57c3426cb69a48badd9125992a6b4
fetched_at: '2026-06-28T22:38:15.062097+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN - FINA460 - Desativar/controlar o tempo de inatividade  '
type: support-article
updated_at: '2021-04-28T15:17:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007249591-MP-SIGAFIN-FINA460-Desativar-controlar-o-tempo-de-inatividade
---

**Dúvida**Como **desativar/controlar** o tempo de inatividade nos processos supracitados?

**Ambiente**Microsiga Protheus – Financeiro – Versão 12

**Solução**Para a demanda/solicitação, é necessário:

Acesse: **SIGACFG** > **Base de Dados** > **Dicionário** > **Base de Dados** > **Parâmetros** > Pesquise o parâmetro respectivo:

**MV\_FATOUT** – Estabelece 15min para que o usuário selecione (15min (15\*60=900) – valor padrão 900)

**MV\_MSGTIME** – Estabelece 02min para exibir a mensagem para o usuário (2min (2\*60=120) valor padrão 120)

Sendo os mesmos informados o valor em segundos, devendo ser parametrizado conforme a necessidade. Não há limite máximo de tempo.

**Importante:**  
Rotinas envolvidas:

**FINA090** – Baixas Pagar Automática

**FINA091** – Baixa Automática de Multi-filiais

**FINA110** – Baixas Automáticas a Receber

**FINA290** – Faturas a Pagar

**FINA460** - Liquidação

**Saiba mais:**  
acesse:**<http://tdn.totvs.com/display/public/PROT/FIN0039_Controle_Inatividade>**
