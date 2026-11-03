---
article_id: 360025672672
category: Gestão de Transportes (TMS)
content_hash: 95ea5e5f38bf4a4f5b686801e55089833dfe5e11daf68fbf3af61fa92d0cd5f5
fetched_at: '2026-06-28T22:45:33.372638+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Simples Nacional
type: support-article
updated_at: '2023-02-28T14:14:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025672672-Log%C3%ADstica-Linha-Protheus-TMS-Simples-Nacional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min****Dúvida**Quais parametrizações são necessárias para gerar **CT-e - Conhecimento de Transporte Eletrônico**, quando a empresa é enquadrada no **Regime do Simples Nacional**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para emitir **CT-e** quando a empresa é enquadrada no **Regime do Simples Nacional**, seguem parametrizações:

1. **SIGACFG** - Parâmetro **MV\_CODREG** igual a **1**
2. **MATA080 - Tipos de Entrada e Saída**, aba **Impostos,**campos:
   1. **Sit.Trib.ICM - F4\_SITTRIB =** informar**CST - Código Situação Tributária** igual a **90 - Outras**
   2. **Calcula ICMS - F4\_ICM = Sim**
   3. **L. Fiscal ICMS - F4\_LFICM = Outros**
   4. **ICMS Observ - F4\_OBSICM = Sim**
3. **MATA030** **- Cadastro de Clientes**, campo **Opt Simp Nac - A1\_SIMPNAC,**aba **Fiscais,** igual a **Sim**

Abaixo segue exemplo do arquivo **XML** com as respectivas *tag's* e impressão **DACTE - Documento Auxiliar do Conhecimento de Transporte Eletrônico**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024998671/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024988092/mceclip1.png)

 Informações extraídas do **Manual de Orientações do Contribuinte CTe\_v3.00**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025013491/mceclip0.png)
