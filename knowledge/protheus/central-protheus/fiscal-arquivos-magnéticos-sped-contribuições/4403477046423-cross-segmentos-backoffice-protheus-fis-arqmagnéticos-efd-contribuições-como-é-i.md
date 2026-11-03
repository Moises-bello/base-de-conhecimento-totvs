---
article_id: 4403477046423
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: df44a303733515714ff0403ea13e83981ea7d605ab460261729e5a0982891771
fetched_at: '2026-06-28T22:42:05.067372+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como é identificado a origem do tratamento para considerar uma operação no regime
  Cumulativo, não Cumulativo ou Ambos?
type: support-article
updated_at: '2023-08-16T18:15:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403477046423-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-%C3%A9-identificado-a-origem-do-tratamento-para-considerar-uma-opera%C3%A7%C3%A3o-no-regime-Cumulativo-n%C3%A3o-Cumulativo-ou-Ambos
---

**Dúvida**

Apuração **EFD Contribuições (FISA001)**: Como é identificado a origem do tratamento para **considerar uma operação no regime Cumulativo, não Cumulativo ou Ambos**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais- a partir da versão 12.1.17  
  
**Solução**

A origem do tratamento para considerar uma operação no **regime Cumulativo**, **não Cumulativo** ou **Ambos (Cumulativo** e **Não Cumulativo)**,  é baseado pela configuração informada no parâmetro **MV\_M996TPR** (**1=SF4, 2=SB1, 3=SA1**).

Para o caso da empresa optar pelo regime **Cumulativo** e **Não cumulativo**, a rotina se baseia neste parâmetro para fazer o tratamento dos valores corretamente.

Se o parâmetro estiver como **1**, a rotina verifica o Cadastro de **TES** campo **Tp. Reg (F4\_TPREG)**  
Se estiver como **2**, verifique no **Cadastro de Produto** no campo **Tp. Reg (B1\_TPREG)**  
Se estiver como **3**, verifique o **Cadastro de Cliente** no campo **Tp. Reg (A1\_TPREG)**

**Importante:**

O objetivo deste **parâmetro** é identificar se o valor em questão pertence ao **regime cumulativo** ou **não cumulativo**, e se caso for informado **1 (SF4)**, e no campo **Tp. Reg  (F4\_TPREG)** estiver como **3=Ambos**, não identifica qual regime o valor pertence, então para este caso, onde no **MV\_M996TPR** estiver com **1**, e no **Tp. Reg (F4\_TPREG)** igual a **3=Ambos**, a rotina verifica o cadastro de produtos, o campo **Tp. Reg (B1\_TPREG)**.
