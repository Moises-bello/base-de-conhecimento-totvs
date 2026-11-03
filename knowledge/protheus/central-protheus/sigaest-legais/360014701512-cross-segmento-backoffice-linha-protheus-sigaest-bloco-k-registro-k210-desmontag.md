---
article_id: 360014701512
category: SIGAEST - LEGAIS
content_hash: 6f3b73c843592cfbbdc7ad1e2d8e06a0f8f9a3693e12732ddc9b4aabc43d062d
fetched_at: '2026-06-28T22:38:51.461315+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Registro
  K210: Desmontagem de Mercadorias - Itens de Origem'
type: support-article
updated_at: '2022-08-24T19:33:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014701512-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Registro-K210-Desmontagem-de-Mercadorias-Itens-de-Origem
---

**Dúvida**O que é o Registro K210: Desmontagem de Mercadorias - Itens de Origem?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Este registro contém as informações dos movimentos de desmontagem de produtos, no que se refere à saída do estoque do item de origem.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K210" | C | 4 | - | O |
| 02 | DT\_INI\_OS | Data de início da ordem de serviço | N | 8 | - | OC |
| 03 | DT\_FIN\_OS | Data de conclusão da ordem de serviço | N | 8 | - | OC |
| 04 | COD\_DOC\_OS | Código de identificação da ordem de serviço | C | 30 | - | OC |
| 05 | COD\_ITEM\_ORI | Código do item de origem (campo 02 do Registro 0200) | C | 60 | - | O |
| 05 | QTD\_ORI | Quantidade de origem – saída do estoque | N | - | 3 | O |

São consideradas as desmontagens de produtos geradas através da rotina MATA242, dentro do período de apuração, sendo que neste registro serão considerados apenas os movimentos de origem com **D3\_CF = RE7.**

**Tipos de Produtos considerados**

00(ME), 01(MP), 02(EM), 03(PP), 04(PA), 05(SP) e 10(OI).

**Rotinas envolvidas**

MATA242 – Desmontagem de Produtos.

**Tabelas envolvidas**

SD3 – Movimentações Internas.

**Saiba mais:**

*[MP - SIGAEST - Bloco K - Registro K215: Desmontagem de Mercadorias - Itens de Destino](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014910951)*

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
