---
article_id: 360061780773
category: Financeiro - Consultas a Pagar
content_hash: 2b99934ed9fd0ea08ed0fdd361d8e8ba2ac3c308b9c5643547110fa07c2733b5
fetched_at: '2026-06-28T22:37:29.584103+00:00'
product: protheus
section_id: 35057716924311
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR150 - Finalidade
  parâmetro Compõe Saldo Retroativo
type: support-article
updated_at: '2026-04-15T13:33:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061780773-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR150-Finalidade-par%C3%A2metro-Comp%C3%B5e-Saldo-Retroativo
---

Informamos que o relatório **FINR150 foi descontinuado a partir de 2024.** Devido a essa atualização, não estão previstas novas manutenções ou correções para este fonte. Caso ainda haja interesse em utilizá-lo, o código-fonte mais recente permanece disponível para download no Portal TOTVS.

Ressaltamos que o suporte padrão não realiza mais validações sobre este arquivo.

**Dúvida**

Qual a finalidade do parâmetro **Compõe Saldo Retroativo** no relatório de **Títulos a Pagar - FINR150**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA210 - Todas as versões  
  
**Solução**  
Ao utilizar parâmetro **Compõe Saldo Retroativo = SIM** , relatório valida e retorna títulos que estavam em aberto até **data base** informada para compor relatório, considerando baixas totais e parciais.  
  
**Exemplo**: Título com **Baixa** em **01/01/2021** retornará ao relatório quando utilizada **data base** anterior a **data da baixa** compondo saldo até o momento.

**Saiba Mais**  
<https://tdn.totvs.com/display/public/PROT/FIN0078_CPAG_FINR150_COMPOE_SALDO_RETROATIVO_FIN15021>  
[Títulos a Pagar - FINR150 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=510498025)
