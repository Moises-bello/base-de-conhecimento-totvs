---
article_id: 360027787051
category: Escrita Fiscal - Impostos - ICMS
content_hash: 483aef1e2822791c87c3387ccbbe0cff8621aaaa6ac00486a0a89c26b4d37daf
fetched_at: '2026-06-28T22:39:25.597082+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configuração padrão
  do ICMS-ST
type: support-article
updated_at: '2024-01-29T12:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027787051-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-padr%C3%A3o-do-ICMS-ST
---

**Dúvida**

Configuração padrão do ICMS ST

**Ambiente**

Protheus – Livros Fiscais – Todas as versões  
  
**Solução**

Para calcular o ICMS ST configure conforme abaixo:

**Produto:**

Para Saídas:

Na exceção fiscal no campo Margem de Lucro (F7\_MARGEM) - informe o MVA do produto para saída; ou no cadastro de produto pelo campo Solid. Saída (B1\_PICMRET) ou caso utilize indicador de produto "Tabela SBZ" no campo Solid. Saída (BZ\_PICMRET)

Para entradas:

Na exceção fiscal no campo Margem de Lucro (F7\_MARGEM) - informe o MVA do produto para saída; ou no cadastro de produto pelo campo Solid. Entr. (B1\_PICMENT) ou caso utilize indicador de produto "Tabela SBZ" no campo Solid. Entr. (BZ\_PICMENT)

**TES**:

Mkp ICM Comp. (F4\_MKPCMP) = 2-Não;

Marg. Solid. (F4\_MKPSOL) = 2-Configuração;

Ded.ICM.ST (F4\_ICMSTMT) = 1-SIM ou 2-NÃO

Se deixar Ded.ICM.ST (F4\_ICMSTMT) = 1-SIM, ele subtrai o valor do ICMS próprio do valor do Retido

Se deixar Ded.ICM.ST (F4\_ICMSTMT) = 2-Não, ele Não subtrai o valor do ICMS próprio do valor do Retido

**Cliente**:

Tipo (A1\_TIPO) = Este campo têm relação com o parâmetro MV\_TPSOLCF, onde são informados os tipos de cliente/fornecedores que possuem cálculo de ICMS Solidário.

**Parâmetro:**

MV\_TPSOLCF – Indica quais os tipos de cliente devem ser considerados para cálculo do ICMS-ST. Lembrando que é realizado o vínculo com o campo Tipo (A1\_TIPO).

MV\_MKPICPT - Indica se há margem de lucro nas operações de venda para o consumidor final.

Segue abaixo exemplo "Didático"  com 1 Produto no valor unitário e total em 1.000,00, com Margem de Lucro de 60% e operação interna a 18%

* Com  **Ded.ICM.ST (F4\_ICMSTMT)** = **1-SIM**, ele subtrai o valor do ICMS próprio do valor do Retido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20939848678935)

* Com **Ded.ICM.ST (F4\_ICMSTMT)** = **2-Não**, ele Não subtrai o valor do ICMS próprio do valor do Retido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20939859406359)
