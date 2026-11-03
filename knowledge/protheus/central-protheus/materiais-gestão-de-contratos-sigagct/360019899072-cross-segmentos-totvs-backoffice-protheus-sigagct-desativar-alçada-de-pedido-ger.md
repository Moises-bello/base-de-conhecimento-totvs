---
article_id: 360019899072
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d1379fb37c2fe3ff342e289d8d56c232d9f123fb6089d2adfb14a3ee52fd278b
fetched_at: '2026-06-28T22:37:20.031733+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Desativar Alçada de
  Pedido gerado na Medição - Relação entre MV_CNDPCAL e Alçada Pedido de Compras (MV_PCAPROV/Alçada
  por Ent. Contabeis)
type: support-article
updated_at: '2025-12-18T11:56:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019899072-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Desativar-Al%C3%A7ada-de-Pedido-gerado-na-Medi%C3%A7%C3%A3o-Rela%C3%A7%C3%A3o-entre-MV-CNDPCAL-e-Al%C3%A7ada-Pedido-de-Compras-MV-PCAPROV-Al%C3%A7ada-por-Ent-Contabeis
---

**Dúvida**

Desativar Alçada de Pedido gerado nas Medições - Relação entre MV\_CNDPCAL e MV\_PCAPROV

**Ambiente**

Protheus – Gestão de Contratos – A partir da versão 12.1.17

**Solução**

A maioria das empresas tem necessidades de controlar os direitos e limites de compras/medição de contratos de seus funcionários. Para que isso seja feito de forma prática e segura é que disponibilizamos o controle de Alçadas para o módulo GCT.

O objetivo deste é reduzir os custos operacionais, visto que ele impede que seja feita uma solicitação de produto/grupo de produtos, que esteja fora da alçada do solicitante, ou ainda, que seja efetuado um pedido de compras por um comprador/grupo de compradores que não possua direitos para tal.

E, no caso de contratos, impedir que seja feita uma medição de contrato fora da alçada do solicitante ou que o solicitante não possua direitos para efetuar tal procedimento.

Para tanto existe o parâmetro abaixo que possibilita tratamento no Pedido ou conforme a alçada da medição.

**MV\_CNDPCAL** - Desativa o controle de alçada para o Pedido de Compras gerado pelas medições de contrato.

**Opções de Conteúdo:**

* 1 (Ativado) - Ativa aprovação conforme MV\_PCAPROV/Alçada por Ent. Contabeis do pedido gerado a partir da medição
* 2 (Desativado) - Desativa aprovação conforme MV\_PCAPROV/Alçada por Ent. Contabeis do pedido gerado a partir da medição
* 3 (Conforme alçada da medição) - Caso a medição tenha alçada, desativa alçada do MV\_PCAPROV/Alçada por Ent. Contabeis.

Abaixo conceito das possibilidades de uso do parâmetro abaixo:

**MV\_CNDPCAL = 1** - Ativa alçada do pedido de compras  independente se a medição for gerada bloqueada ou liberada , a alçada do Pedido será gerada com base na alçada do compras ou parâmetro MV\_PCAPROV preenchido ou Cadastro do comprador na rotina do compras com Grupo vinculado e no Grupo de aprovação Aba Tipo de documentos flegado a opção Pedido de compras.

Como gerar os pedidos de compras gerados pelo módulo gestão de contrato através do encerramento da medição de contrato como liberado ao invés de bloqueado ?

Existem as 2 opções abaixo poderá analisar qual se adequa melhor a sua necessidade.

**MV\_CNDPCAL  = 2**  - Desativa alçada do Pedido de compras quando o Pedido for gerado pelo encerramento da medição.  
   
**MV\_CNDPCAL = 3** - Se na Medição tiver alçada, ao encerrar a medição e gerar o Pedido de compra , o pedido é gerado sem bloqueio.  
Se a medição não tiver alçada e o campo CND\_APROV em branco, o pedido é gerado bloqueado no encerramento da medição de acordo com a alçada do compras.

Para mais informações referente o Controle de Alçada nas Medições de Contrato no GCT, acessar o link:

[Alçada nas medições de contrato](http://tdn.totvs.com.br/pages/releaseview.action?pageId=268579126)

***Saiba Mais:***

[GCT0044\_MV\_CNDPCAL\_Qual\_a\_Relação\_com\_o\_MV\_PCAPROV - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=244940338)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
