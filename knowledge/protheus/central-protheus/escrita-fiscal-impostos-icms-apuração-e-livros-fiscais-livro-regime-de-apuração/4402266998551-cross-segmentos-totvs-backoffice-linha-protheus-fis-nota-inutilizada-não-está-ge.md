---
article_id: 4402266998551
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: e5ab4c0e7fa26ea356d1837e06b341a192afcab1a55816f34ec9efaad68d9e60
fetched_at: '2026-06-28T22:39:22.175619+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice linha Protheus - FIS - Nota inutilizada
  não está gerando livro fiscal (SFT e SF3).
type: support-article
updated_at: '2024-10-08T21:34:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402266998551-Cross-Segmentos-TOTVS-Backoffice-linha-Protheus-FIS-Nota-inutilizada-n%C3%A3o-est%C3%A1-gerando-livro-fiscal-SFT-e-SF3
---

**Ocorrência:**Notas inutilizadas que não estão constando nas tabelas de livros fiscais SFT e SF3.  
**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Escrituração e Relatórios Fiscais - Compras ou Faturamento - Todas as versões.  
  
**Causa:**Esse incidente ocorre, pois a configuração da nota escriturada não foi gerada corretamente entre as tabelas SB1 e SF4.  
  
**Solução:**  
Para solucionar essa ocorrência, faça a seguinte validação:

*1) Configurar a TES:*

Calcula ICMS = Sim ou Não // L. Fiscal ICMS = Outros / Isento

2) Parâmetro:

MV\_INUTTES - Informar Tes que gera Livro Fiscal Calcula ICMS = Não/ L. Fiscal ICMS = Outros/ Isento

3) Excluir o documento de saída/ Entrada com Formulário próprio = SIM

Segue documentação:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017458472-MP-NFE-Como-realizar-Inutiliza%C3%A7%C3%A3o-de-uma-nota-fiscal-eletr%C3%B4nica->
