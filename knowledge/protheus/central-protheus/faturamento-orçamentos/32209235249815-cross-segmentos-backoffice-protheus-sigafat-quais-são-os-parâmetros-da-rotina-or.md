---
article_id: 32209235249815
category: Faturamento - Orçamentos
content_hash: 163c2b35a15e614bbe751348d64b528077a3af77a4422a2671d1785dede4270f
fetched_at: '2026-06-28T22:38:25.041825+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Quais são os parâmetros da
  rotina Orçamento de Vendas (MATA415)?
type: support-article
updated_at: '2025-05-21T17:15:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32209235249815-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Quais-s%C3%A3o-os-par%C3%A2metros-da-rotina-Or%C3%A7amento-de-Vendas-MATA415
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32209213606679) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Quais são os parâmetros da rotina Orçamento de Vendas (MATA415) ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

|  |  |
| --- | --- |
| **Parâmetro** | **Descrição** |
| **MV\_IFATDPR** | Define se a integração entre Faturamento (SIGAFAT) e Desenvolvimento de Produtos (SIGADPR) está ativa (`.T.`) ou inativa (`.F.`). |
| **MV\_NDESCTP** | Indica se a diferença entre o preço de lista (DK\_PRUNIT) e o valor unitário (CK\_PRCVEN) será considerada como desconto. Se `.T.`, a diferença **não** será gravada em C6\_DESCON. |
| **MV\_ORCIMPR** | Nome do RDMAKE utilizado para impressão dos orçamentos. [Saiba mais](https://tdn.totvs.com/x/A95gDQ) |
| **MV\_ORCLIPD** | Código do Cliente + Loja padrão para orçamentos. Preenche automaticamente os campos CJ\_CLIENTE e CJ\_LOJA.     **Atenção:** Caso não exista no ambiente um cliente com código '000001' e loja '01', o sistema irá criar este cliente com a descrição "Cliente padrão p/ Orçamento".  Caso exista um cliente com este código e loja, o sistema utilizará ele como cliente padrão, porém o parâmetro pode ser alterado indicando outro código/loja. |
| **MV\_ORCPGPD** | Código da condição de pagamento **padrão** para Orçamentos. |
| **MV\_PRCORC** | Define se o preço considerado será dos Componentes (`.T.`) ou do Produto Pai (`.F.`). [Saiba mais](https://tdn.totvs.com/x/dUWbEg) |
| **MV\_VEBLQRG** | Libera a consulta de motivo de bloqueio de regra/verba em outras rotinas além da Liberação de Regras. [Saiba mais](https://tdn.totvs.com/x/OekpE) |
| **MV\_ORCVLD** | Ativa o cancelamento automático de orçamentos vencidos (baseado no campo CJ\_VALIDA). [Saiba mais](https://tdn.totvs.com/x/CAmjIQ) |
| **MV\_ORCUVLD** | Registra a data do último processamento de cancelamento automático de orçamentos vencidos. |
| **MV\_TESSAI** | Define o Tipo de Saída padrão para orçamentos, caso o produto não tenha um TES informado no campo **B1\_TS** (**Cadastro de Produtos – MATA010**). |

**Saiba mais:**

**[FAT0172 Orçamento de Vendas (MATA415)](https://tdn.totvs.com/x/rLIpE)**
