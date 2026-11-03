---
article_id: 360021216391
category: Faturamento - Cadastros
content_hash: 7cf5a84d0407170a715110d51e3bac38760b2f3d863cd9177492d9f45e687fe6
fetched_at: '2026-06-28T22:38:35.425009+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como bloquear um cadastro?
type: support-article
updated_at: '2024-12-05T12:27:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021216391-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-bloquear-um-cadastro
---

**Ocorrência**

Como bloquear um cadastro?  
  
**Ambiente**  
Ambiente: Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12

**Solução**O bloqueio de registros, cadastros no Protheus, é realizado pelo campo **MSBLQL**. Quando ele não existe na tabela, basta criá-lo conforme instrução abaixo.

No Módulo Faturamento este bloqueio impede de selecionar este cadastro em novos registros do Protheus. Como por exemplo, a inclusão de um cliente ou do vendedor, transportadora, produto, etc. em novos Pedidos de Venda.

Porém, as definições, o status, o histórico já gerado para este registro não são invalidados ou desconsiderados. Os registros que já foram gerados para este cliente permanecem na base e podem ser manipulados normalmente como, por exemplo, faturar um Pedido em que já contenha o cliente relacionado.

O bloqueio será válido apenas para os novos registros em que tentar selecionar este cadastro - a partir do momento em que bloqueou.

Estou deixando o manual com configurações para auxiliar.

**Saiba Mais:**

**[Bloqueio de Registro / Cadastro](https://tdn.totvs.com/x/p4WFDg)**
