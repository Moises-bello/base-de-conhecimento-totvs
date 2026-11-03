---
article_id: 360038813773
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 88d62a2a594158a487ebdaecfb7ebfb91e184c46689acc99bae0ced34dbb64d8
fetched_at: '2026-06-28T22:39:36.838498+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Qual a configuração
  necessária para gerar nota fiscal com cálculo de PIS e COFINS apuração?
type: support-article
updated_at: '2021-10-01T22:05:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038813773-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-necess%C3%A1ria-para-gerar-nota-fiscal-com-c%C3%A1lculo-de-PIS-e-COFINS-apura%C3%A7%C3%A3o
---

**Dúvida**  
Qual a Configuração Necessária Para Gerar Nota Fiscal Com Cálculo de PIS E COFINS Via Apuração?  
 **Ambiente**  
Microsiga Protheus– Livros Fiscais – A partir da versão 11.80  
  
**Solução**

# **TES - Notas de Entrada**

**PIS/ COFINS** (F4\_PISCOF) =**Ambos**

**Cred.PIS/COF** (F4\_PISCRED) = **Credita**

**Tp Reg** (F4\_TPREG) = **Cumulativo ou Não Cumulativo**

**Sit. Trib. PIS** (F4\_CSTPIS) = **50 a 66**

**Sit. Trib. COF** (F4\_CSTCOF) = **50 a 66**

**L. Fisc. ICMS**(F4\_LFICM) ; **L. Fiscal IPI** (F4\_LFIPI) ou **L. Fiscal ISS** (F4\_LFISS) = **Preenchimento diferente de NÃO**- Deve ser configurado o campo de um dos livros fiscais com opção diferente de NÃO, para geração dos valores de PIS COFINS nas tabelas SF3 e SFT.

# **TES - Notas de Saída**

**PIS/ COFINS** (F4\_PISCOF) =**Ambos**

**Cred.PIS/COF** (F4\_PISCRED) = **Debita**

**Tp Reg** (F4\_TPREG) = **Cumulativo ou Não Cumulativo**

**Sit. Trib. PIS** (F4\_CSTPIS) = **01 a 49**

**Sit. Trib. COF** (F4\_CSTCOF) = **01 a 49**

**L. Fisc. ICMS**(F4\_LFICM) ;**L. Fiscal IPI** (F4\_LFIPI) ou**L. Fiscal ISS** (F4\_LFISS) = **Preenchimento diferente de NÃO** - Deve ser configurado o campo de um dos livros fiscais com opção diferente de NÃO, para geração dos valores de PIS COFINS nas tabelas SF3 e SFT.

# **PRODUTO**

**Perc. PIS** (B1\_PPIS) = **Informe a alíquota**

**Perc. COFINS** (B1\_PCOFINS) =  **Informe a alíquota**

Para o cálculo do PIS COFINS apuração o sistema verifica primeiro as alíquotas informadas na exceção fiscal, após produto, caso não tenha alíquota, serão verificados os parâmetros **MV\_TXPIS** e **MV\_TXCOFIN.**

# **FORNECEDOR**

**Rec. PIS** (A2\_RECPIS) = **Não**

**Rec. COFINS** (A2\_RECCOFI) = **Não**

# **CLIENTE**

**Rec. PIS** (A1\_RECPIS) = **Não**

**Rec. COFINS** (A1\_RECCOFI) = **Não**

# **Parâmetros referentes à apuração de PIS COFINS**

**MV\_TXPIS:**Taxa para cálculo do PIS =**1.65 ou 0.65 (separado por ponto)**                     

**MV\_TXCOFIN:** Taxa para cálculo do COFINS = **7.60 ou 3.00** **(separado por ponto)**

**Informações Adicionais:**

**Retenção de PIS COFINS e CSLL**

**<https://tdn.totvs.com/pages/viewpage.action?pageId=6076816>**
