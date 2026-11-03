---
content_hash: 9852366b41c74be5f0343f298ec88ce088694fc3a21fa6f01255500d8d81f399
fetched_at: '2026-06-29T00:11:33.861762+00:00'
page_id: '761017178'
product: rm
source: tdn-rm
title: Integração Financeira|Aba Tributos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=761017178
version: 10
---

Regras

**Regras para preenchimento do campo Natureza de Rendimento do Movimento para o Lançamento Financeiro**

Na geração dos lançamentos financeiros a partir de um movimento inserido no TOTVS Gestão de Estoque, Compras e Faturamento, o campo Natureza de Rendimento será levado para o lançamento financeiro (aba Valores |Tributos), conforme as regras abaixo:

| **Tributos** | **Seleção** |
| --- | --- |
| IRRF | Para as situações onde o lançamento financeiro tem o tipo de documento **Gerar IRRF** a natureza de rendimento preenchida em  Movimento | Tributos e Valores | Tributos será enviado para o lançamento | Tributos | Valor do IRRF.  Para mais informações de Geração de IRRF Automático para o Totvs Gestão Financeira acesse  Para preenchimento automático (Default) é seguido a seguinte hierarquia:       1. Cadastro do Produto em: Anexos | Dados Fiscais do Produto | Código da Natureza de Rendimento;       2. Cadastro do Cliente Fornecedor em:  Outros | Tributos | Código da Receita;  **Importante:** Caso o campo Natureza de Rendimento  (Tributos e Valores | Tributos ) no movimento esteja preenchido, o valor default não serão aplicados. |
| PISRF, COFINSRF, CSLLRF e CSRF | A Natureza padrão definida nos tributos do item de movimento ou no movimento será copiada para o lançamento financeiro |

Para conhecer as regras do preenchimento automático do campo "natureza de rendimento" no movimento, acesse a documentação:

Para mais informações acesse também os documentos abaixo:
