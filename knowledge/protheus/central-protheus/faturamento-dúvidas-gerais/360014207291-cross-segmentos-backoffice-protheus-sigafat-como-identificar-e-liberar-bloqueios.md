---
article_id: 360014207291
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 0ff67d14531d1b2e83fce149da2fe3885d204b8816f27d995f032febbe2cca49
fetched_at: '2026-06-28T22:38:29.771343+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como identificar e liberar
  bloqueios do Pedido de Vendas
type: support-article
updated_at: '2026-03-20T19:57:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014207291-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-identificar-e-liberar-bloqueios-do-Pedido-de-Vendas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38929229437975) Tempo aproximado para leitura: 00:03:30 min**

**Dúvida**  
Como identificar a causa de bloqueios do Pedidos de Vendas e liberar para Faturamento?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**  
 O que determina que um Pedido está apto a Faturar são as liberações do Pedido. Estando com algum bloqueio identifica que o Pedido não está em condições de ser faturado. É necessário primeiramente identificar a causa do bloqueio, sanar a causa e reprocessar a análise para que ocorra a liberação.

O Pedido passa por um fluxo de análises para validação de que está liberado por todos os fatores:

**1ª Análise: Liberação de Regras de Negócio / Verbas de Venda**

* Esta etapa avalia se o Pedido incluído está de acordo com as [Regras de Negócio (FATA100)](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/fata100_regras_de_negocio.htm) da Organização. E caso a análise indique que o Pedido ultrapassou o desconto máximo concedido na Regra de Negócio, é avaliado também se há [Verbas de Vendas](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/fata190_verbas_de_vendas.htm) que compensam a diferença e permitem a liberação
* Após liberar o Pedido nesta etapa, é criado um registro deste Pedido na Tabela SC9 (Tabela de Liberações do sistema) o que indica que o Pedido está apto a ser analisado por **Crédito de Cliente** e **Saldo de Estoque**. O que nos leva à próxima análise.

**2ª Análise: Liberação de Crédito de Cliente**

* Esta etapa avalia se o Cliente possui Saldo de Crédito Disponível. Veja aqui as [configurações e parametrizações para análise automática de crédito](http://tdn.totvs.com/pages/viewpage.action?pageId=225950030) ou, se não desejar utilizar Análise de crédito no Protheus, é opcional (neste caso configure MV\_BLOQUEI como .F.)
  + Caso o Pedido seja avaliado com Bloqueio de Crédito (C9\_BLCRED preenchido) então indica que não há limite de crédito disponível para este Cliente. Para identificar o que o sistema está validando para chegar a essa conclusão, consulte (e ajuste de acordo com sua necessidade) a FAQ: [Bloqueio de Crédito](http://tdn.totvs.com/pages/viewpage.action?pageId=239036879)
* Após liberar o Pedido nesta etapa de análise de Crédito indica que o mesmo está apto a ter os itens analisados por Saldo de Estoque. O que nos leva à próxima análise.

**3ª Análise: Liberação de Estoque de Produto**

* Esta etapa avalia se os itens inseridos no Pedido de Vendas possuem Saldo de estoque Disponível. Obs: Diferente da Análise de crédito no Protheus, a Análise de Estoque já não é opcional, ou seja, não havendo saldo disponível o item/pedido realmente ficará com bloqueio de Estoque pela análise automática
  + Caso o Pedido seja avaliado com Bloqueio de Estoque (C9\_BLEST preenchido) então indica que não há saldo de estoque disponível para estes itens/para este Pedido / para o lote selecionado (caso exista). Para identificar o que o sistema está validando para chegar a essa conclusão, consulte (e ajuste de acordo com sua necessidade) a FAQ: [Bloqueio de Estoque](http://tdn.totvs.com/display/PROT/FAT0083_Bloqueio_de_Estoque)
* Após liberar o Pedido nesta etapa de análise de Estoque indica que o mesmo está apto a ser faturado

**Observação:**

As rotinas de liberação, como a MATA450 (crédito) e MATA455 (estoque), foram concebidas para execução mediante ação do usuário e não possuem execução automática nativa (schedule/ExecAuto).

Isso ocorre porque o bloqueio registrado representa uma validação de regras de negócio. Dessa forma, a intervenção do usuário garante rastreabilidade e aderência às políticas da empresa.

**Saiba Mais:**

* [FAT0242 Liberações /](https://tdn.totvs.com/pages/releaseview.action?pageId=330839110) [Bloqueios](https://tdn.totvs.com/x/RjS4Ew) [do Pedido de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=330839110)
* Assista nosso vídeo [How To | MP - SIGAFAT - Pedidos de venda aptos a faturar](https://www.youtube.com/watch?v=5E08tiWORdA)
