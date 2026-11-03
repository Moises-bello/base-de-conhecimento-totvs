---
article_id: 360026551513
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: fcddac81e9960dba8ba62f86147ecb06f990e91a3ada903dd933fb62547573e8
fetched_at: '2026-06-28T22:38:41.304213+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT-Não é possível habilitar o campo C6_CODROM - Código de romaneio no pedido
  de venda(MATA410).
type: support-article
updated_at: '2021-04-28T15:50:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026551513-MP-FAT-N%C3%A3o-%C3%A9-poss%C3%ADvel-habilitar-o-campo-C6-CODROM-C%C3%B3digo-de-romaneio-no-pedido-de-venda-MATA410
---

**Dúvida**

Não é possível habilitar o campo **C6\_CODROM - Código de romaneio**no pedido de venda**(MATA410).**

**Ambiente**

Microsiga Protheus - todas as versões.

**Solução**

O campo **C6\_CODROM**é um campo interno de sistema (campo vermelho),  de uso exclusivo do sistema, somente utilizado para tratar as operações internas relacionadas a integração do módulo de Agronegócios com o módulo Faturamento, validando as informações existentes na tabela **NPR** para o seu preenchimento:

![](https://totvssuporte.zendesk.com/attachments/token/HzCXl8sOQZPKnqzYrh54rRck0/?name=inline-1065952920.png)​  
O campo não possui nenhum uso isolado por parte do módulo Faturamento.

Além da tabela **NPR**, o campo também é validado por outras três tabelas dentro das operações do módulo 67 - Agronegócios:

**N8H**, **N8I** e **NJM**.

Por se tratar de campo de uso interno do sistema, não são passíveis de marcação , somente será utilizado para o fim para o qual foi criado.
