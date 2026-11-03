---
article_id: 360022903671
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 68c0474c4dc78267ba8019290d9b6ce733d96fc2bc8fa58d4560c147334df758
fetched_at: '2026-06-28T22:39:22.244744+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: MP - FIS - Notas com ICMS ST Não São Apresentadas Na Apuração do ICMS ST
type: support-article
updated_at: '2024-10-08T21:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022903671-MP-FIS-Notas-com-ICMS-ST-N%C3%A3o-S%C3%A3o-Apresentadas-Na-Apura%C3%A7%C3%A3o-do-ICMS-ST
---

**Dúvida**  
O movimento de ICMS ST não está sendo demonstrado no resumo do ICMS-ST - MATA953

**Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80  
  
  
**Solução**

**Apuração do ICMS ST**

Segue abaixo a configuração padrão para que seja considerado a informação no resumo ST

MV\_ESTADO = preenchido.  
P9AUTOTEXT = De acordo com o estado.  
MV\_USASPED = .T.  
MV\_P9SPED = .T.  
MV\_P9AUTO = T  
MV\_STUF = preenchido com todos os estados  
MV\_STUFS = preenchido com todos os estados  
MV\_SUBTRIB = preenchido com seu  estado + inscrição estadual (todos os estados que possuírem inscrição estadual para recolhimento do ICMS ST).

**Importante:**

Quando os parâmetros:  
MV\_USASPED = .T. os parâmetros MV\_P9AUTO/MV\_P9SPED devem estar preenchidos = T  
MV\_USASPED = .F. os parâmetros MV\_P9AUTO/MV\_P9SPED = devem estar preenchidos = F

**Configuração de TES:**

Cred ICMS ST (F4\_CREDST) = 2 = Retido ST

Importante:

Ao preencher o campo Cred ICMS ST (F4\_CREDST) = 4 Subst.Ttrib., as informações não serão levadas para o livro de ICMS, pois será gravado o campo F3\_credt = 4
