---
article_id: 4414648139543
category: NFe - Nota Fiscal Eletrônica
content_hash: b3c00647bc5d55e1b29a154f5eefffd0753cca976b8022f96ce1b2c209c22b39
fetched_at: '2026-06-28T22:40:07.028212+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2021.004
type: support-article
updated_at: '2025-06-30T21:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414648139543-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-t%C3%A9cnica-2021-004
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2021.004 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

* **Importante:**

**Nota Técnica 2021.004\_V\_1.35**

949 / 950 Implementação futura das ***regras de Validações - Apenas para NFC-e***

**O prazo previsto para a Nota Técnica 2021.004\_V\_1.34:**

* Ambiente de Homologação (ambiente de teste das empresas):  **23****/****09/2022**
* **Ambiente de Produção: 27/09/2022**

    1. **Para a criação dos novos campos :**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Campos do Faturamento para uso da NT 2021.004](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5717173840791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Campos-do-Faturamento-par-uso-da-NT-2021-004)

[Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Campos Compras para uso da NT 2021.004](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6502168930327-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Campos-Compras-para-uso-da-NT-2021-004)

De acordo com a Nota Técnica **2021.004** do Projeto Nota Fiscal Eletrônica, será necessário a criação dos campos de observação para o **Fisco**no cabeçalho do**Pedido de Venda**,devido novas regras de validações do arquivo da NF-e/NFC-e.

Criados os campos **Obs. T.Fisco**(**C5\_OBSFCMP**) e **Obs. Fisco** (**C5\_OBSFISC**) na tabela do**Cabeçalho do** **Pedidos de Venda** (**SC5**) da rotina de **Pedidos de Venda** (**MATA410**) para atender as novas exigências da **NT 2021.004** do Projeto Nota Fiscal Eletrônica.

Caso ainda não tenha os campos, veja a documentação abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=837424185>
