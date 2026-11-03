---
article_id: 37676372047511
category: Financeiro
content_hash: c4e3f833b7da853bc8315815e594e11f9edfd5ce9f2778747268348f3b51a2a0
fetched_at: '2026-06-28T22:38:00.879793+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - IRRF - Tabela Progressiva de
  Cálculo de Imposto de Renda Pessoa Física 2026
type: support-article
updated_at: '2026-02-12T18:09:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37676372047511-Cross-Segmentos-Backoffice-Linha-Protheus-IRRF-Tabela-Progressiva-de-C%C3%A1lculo-de-Imposto-de-Renda-Pessoa-F%C3%ADsica-2026
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37676342225175) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como configurar tabela progressiva para pessoa física?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
**Acesso:** no módulo **Configurador (SIGACFG)**, acesse **Ambiente** > **Cadastros** > **Tabela IRRF**.

**Preenchimento:** Preencha a tabela progressiva com os seguintes limites, alíquotas e parcelas a deduzir **referentes ao ano de 2026**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38362351602711)

**Importante**

Para o configurador de tributos, a configuração deve ser realizada diretamente pela rotina

**Configurador de tributos → Regras financeiras → Regras de tabelas progressivas**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Regra Tabela Progressiva](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34976665133079-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regra-Tabela-Progressiva)

**Parâmetros responsáveis pela validação e geração do IRRF**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37676372026135)

**Cadastro de Natureza - Legado**

Atualizações → Cadastros → Cadastro de Natureza → Aba Impostos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37676342228247)

**Cadastro de Clientes - Legado**

**Aba admin → Campo Aliq. IRRF → Percentual de cálculo de IRRF (conforme necessidade)**

Aba Fiscais **→**

* **Campo** Recolhe IRRF (SIM)
* Campo Modo abat imp (1 - Calculo do sistema)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37676342235031)

**Cadastro de Fornecedor - Legado**

**Aba Fiscais →**

* **Cálculo IRRF (1 -** Normal 2 - IRRF Baixa) preencher conforme a necessidade.
* **IRRF Prog (SIM)**
* Vlr. Min. IR **1 – Sim** - O Sistema não considera o parâmetro **MV\_VLRETIR/ 2 – Não** - O sistema considera esse parâmetro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37676372036759)

**Importante**  
Ao utilizar o **Configurador de Tributos**, os cadastros de **cliente** e **fornecedor** não devem possuir impostos configurados. Nesses cadastros, devem ser **preenchidos exclusivamente os campos mencionados nas tabelas acima**, conforme orientação apresentada.

Saiba mais

[IRRF - Tabela Progressiva](https://tdn.totvs.com/pages/releaseview.action?pageId=695202577)

[Lei 15.270/2025 - Reforma do Imposto de Renda 2026](https://tdn.totvs.com/pages/releaseview.action?pageId=1027817283)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o IRRF para notas de entrada e saída?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025517971-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-IRRF-para-notas-de-entrada-e-sa%C3%ADda)
