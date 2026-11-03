---
article_id: 360017527812
category: Materiais - Compras (SIGACOM)
content_hash: 57957855dbb810c2d8ad3fa3277589199ee32b8d37342d654f9bd3243b19a5ef
fetched_at: '2026-06-28T22:41:08.783347+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Desabilitar Validação
  Item de Pedidos já utilizados no mesmo Documento de Entrada - MV_VLDITPC - Help
  A103ITEXCED
type: support-article
updated_at: '2023-08-29T19:15:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527812-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Desabilitar-Valida%C3%A7%C3%A3o-Item-de-Pedidos-j%C3%A1-utilizados-no-mesmo-Documento-de-Entrada-MV-VLDITPC-Help-A103ITEXCED
---

**Dúvida**

Desabilitar Validação Item de Pedidos já utilizados no mesmo Documento de Entrada - MV\_VLDITPC

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17125987900695)

**Ambiente**Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Qual a funcionalidade do parâmetro MV\_VLDITPC?

Permite desabilitar a validação dos itens de pedidos de compra já utilizados no mesmo documento de entrada.

No Configurador (SIGACFG) acesse Ambientes/Cadastros/Parâmetros **(CFGX017)**e configure conforme imagem abaixo:

![kcs1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360013115892)

Procedimento para utilização:

1. Em Compras (SIGACOM) acesse Atualizações/Pedidos/Pedidos de Compras **(MATA121**).  
2. Inclua um pedido de compra.  
3. Acesse Atualizações/Movimentos/Documento Entrada **(MATA103)**.  
4. Inclua um documento de entrada do tipo normal.  
5. Preencha o cabeçalho da nota e clique em Selecionar Pedido de Compra (por item) através [F6] ou tecle [F6].  
6. Selecione o item do pedido de compra criado anteriormente e confirme.

O parâmetro **MV\_VLDITPC** deve ser configurado com .T. para que seja desabilitada a validação do item no PC, caso esteja .F. não estará desabilitada a validação.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
