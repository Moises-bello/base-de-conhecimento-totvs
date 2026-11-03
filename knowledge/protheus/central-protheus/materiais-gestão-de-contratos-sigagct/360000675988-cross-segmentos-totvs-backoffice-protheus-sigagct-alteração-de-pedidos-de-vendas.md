---
article_id: 360000675988
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 51005933b041f7ae294cab7460dcf0553078b3ce7c176ac85065f958f2f75f6c
fetched_at: '2026-06-28T22:37:19.753090+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alteração de Pedidos
  de Vendas / Compras gerados pela Medição do Gestão de Contratos
type: support-article
updated_at: '2026-02-16T19:10:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000675988-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Altera%C3%A7%C3%A3o-de-Pedidos-de-Vendas-Compras-gerados-pela-Medi%C3%A7%C3%A3o-do-Gest%C3%A3o-de-Contratos
---

**Dúvida**  
Alteração de Pedidos de Vendas / Compras gerados pela Medição do Gestão de Contratos  
  
**Ambiente**  
Microsiga Protheus - A partir da versão 12.  
  
**Solução**

A alteração do **Pedido de Vendas** gerados a partir do Processo de encerramento da Medição, por padrão e conceito do sistema, é permitida apenas para alguns campos. E para isso o ambiente deve estar atualizado com as últimas atualização do Portal do Cliente.

Abaixo artigo que contém a informação dos campos que são permitidos no padrão do sistema:

[GCT0048\_Alteração Pedido de Vendas/Compras gerado pelo produto Gestão de Contratos](http://tdn.totvs.com/pages/releaseview.action?pageId=259557631)

Para campos que não são liberados para edição no padrão, existe um ponto de entrada disponível: GCTPEDCPO para Pedido de Vendas.

Para mais informações sobre o mesmo favor acessar o Portal TDN, através do link:

[GCTPEDCPO - Liberar campos para alteração de pedidos de venda oriundos do SIGAGCT](https://tdn.totvs.com/pages/viewpage.action?pageId=658231372)

Quanto ao **Pedido de Compras**, a alteração não é permitida, pois trata-se do conceito do sistema.

Caso deseja-se proceder com alguma customização, existe um Ponto de Entrada MT120PED abaixo disponível pra que possa verificar se atenda alguma necessidade existente:

[MT120PED - Altera campos de usuário onde houve processo externo](https://tdn.totvs.com/x/UNxc)

Caso se deseje, pode-se também avaliar, através de customização, a possibilidade de preenchimento de outros campos no Pedido de Compras ou de Vendas no momento de sua geração no Encerramento da Medição através do ponto de entrada CN121PED do artigo abaixo:

[CN121PED - Tratamento especifico antes da geração do pedido de compra ou venda](https://tdn.totvs.com/x/3QMtE)

**Obs1:**

Os Pedidos de Compras gerados através da rotina de medição também não têm permissão para serem excluídos pela rotina de Pedido de Compras (MATA121), sendo que para serem excluídos deve ser estornado o processo de Encerramento da Medição que gerou este pedido pela rotina de Medição (CNTA121).

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como excluir ou estornar uma medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6845020127767-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-excluir-ou-estornar-uma-medi%C3%A7%C3%A3o?source=search)

***Obs2:***

Caso se deseje alterar o campo de Previsão de Entrega de um Pedido de Vendas gerado por uma medição a possibilidade existente seria apenas através de customização do ponto de entrada reportado acima pra liberar alteração de outros campos:

[*GCTPEDCPO - Liberar campos para alteração de pedidos de venda oriundos do SIGAGCT"*](https://tdn.totvs.com/pages/viewpage.action?pageId=658231372)

***Obs3:***

No pedido de vendas, não estou conseguindo alterar o campo **C5\_VEICULO** quando o mesmo é gerado pelo Gestão de contratos GCT, o que fazer?

**R:**A possibilidade existente seria apenas através de customização do ponto de entrada reportado acima pra liberar alteração de outros campos:

[*GCTPEDCPO - Liberar campos para alteração de pedidos de venda oriundos do SIGAGCT"*](https://tdn.totvs.com/pages/viewpage.action?pageId=658231372)

Abaixo no artigo em "***Saiba Mais***" seguem mais informações.

***Saiba Mais:***

[GCT0048\_Alteração Pedido de Vendas/Compras gerado pelo produto Gestão de Contratos](http://tdn.totvs.com/pages/releaseview.action?pageId=259557631)

[GCTPEDCPO - Liberar campos para alteração de pedidos de venda oriundos do SIGAGCT](https://tdn.totvs.com/pages/viewpage.action?pageId=658231372)

[MT120PED - Altera campos de usuário onde houve processo externo](https://tdn.totvs.com/x/UNxc)

[CN121PED - Tratamento especifico antes da geração do pedido de compra ou venda](https://tdn.totvs.com/x/3QMtE)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como excluir ou estornar uma medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6845020127767-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-excluir-ou-estornar-uma-medi%C3%A7%C3%A3o?source=search)

[Pacotes de Atualização - Gestão de Contratos](https://tdn.totvs.com/pages/viewpage.action?pageId=522013125)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
