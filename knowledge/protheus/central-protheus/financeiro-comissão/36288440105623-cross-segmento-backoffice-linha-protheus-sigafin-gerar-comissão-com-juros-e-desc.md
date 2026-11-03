---
article_id: 36288440105623
category: Financeiro - Comissão
content_hash: bed7b36f8c6010ea30617e6e6c7c6f0ffe23c8ea45b3c215d83707acd2236a37
fetched_at: '2026-06-28T22:37:50.722920+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Gerar comissão com juros
  e descontos
type: support-article
updated_at: '2026-02-06T12:28:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36288440105623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Gerar-comiss%C3%A3o-com-juros-e-descontos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36288440090519) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como compor juros e desconto à comissão?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Baixa variação cambial - Todas as versões.  
  
**Solução**  
Parâmetros de Cálculo de Comissão nas Rotinas de Baixa e Recálculo.

As rotinas **Baixa a Receber (FINA070)**, **Baixa a Receber Automática (FINA110)** e **Retorno de Cobrança (FINA200)** possuem parametrizações controladas pelas perguntas do **F12**, conforme descrito a seguir:

* **Cons. Jur/Acres comissão?**  
  Define se os **juros** devem ser considerados na base de cálculo da comissão.

  + **Sim:** os juros serão somados à base de cálculo.
  + **Não:** os juros não serão somados à base de cálculo.
* **Abate Desc. Comiss.?**  
  Define se os **descontos** devem ser abatidos da base de cálculo da comissão.

  + **Sim:** o desconto será abatido da base.
  + **Não:** o desconto não será abatido da base.

Na rotina **Recalculo de Comissões (FINA440)**, utilizam-se as perguntas: **Considera Juros?** E **Considera Desconto?**, que possuem o mesmo comportamento das perguntas **Cons. Jur/Acres comissão?** E **Abate Desc. Comiss.?**, respectivamente.

#### Exemplo Prático

Em uma baixa de **R$ 70,00** com **R$ 30,00 de desconto**:

* Se a pergunta **Abate Desc. Comiss.? / Considera desconto?** Estiver configurada como **“Não”**, o valor considerado na base de cálculo da comissão será **R$ 100,00**.
* Se estiver configurada como **“Sim”**, o valor considerado na base será **R$ 70,00**.

**Importante**

Os campos de **Acréscimo** e **Decréscimo** apresentam o mesmo comportamento referente aos **juros** e **multa**, sendo considerados os parâmetros de configuração do sistema para definir se esses valores irão ou não compor a base de cálculo da comissão.

**Saiba mais**

[Financeiro - Comissão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/26655771327895-Financeiro-Comiss%C3%A3o)
