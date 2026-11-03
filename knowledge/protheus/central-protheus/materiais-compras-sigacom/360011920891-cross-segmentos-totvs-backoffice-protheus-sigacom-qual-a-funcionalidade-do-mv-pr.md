---
article_id: 360011920891
category: Materiais - Compras (SIGACOM)
content_hash: 6c95a566dac2b581c65dd94415a41d976c8755f7424986417ec6f2fd8df6e5e1
fetched_at: '2026-06-28T22:41:10.382325+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a Funcionalidade
  do MV_PRODCTB no Pedido de Compras ( Gatilho Entidades Contábeis no Pedido de Compras
  )?
type: support-article
updated_at: '2024-10-22T19:35:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011920891-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-Funcionalidade-do-MV-PRODCTB-no-Pedido-de-Compras-Gatilho-Entidades-Cont%C3%A1beis-no-Pedido-de-Compras
---

**Dúvida**Qual a Funcionalidade do MV\_PRODCTB no Pedido de Compras ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
  
**Solução**

Na rotina Pedido de Compras (MATA120) com a criação do parâmetro MV\_PRODCTB, que tem a finalidade de relacionar as Entidades Contábeis nos itens do Pedido de Compras (MATA120), conforme cadastradas na tabela SB1 (Cadastro de Produtos).

* Se conteúdo do parâmetro estiver configurado como .T. (True / Verdadeiro), ao digitar o produto no Pedido de Compras (MATA120), o conteúdo das Entidades Contábeis são substituídos conforme cadastrados na tabela SB1 (Cadastro de Produtos).
* Se conteúdo do parâmetro estiver configurado como .F. (False / Falso)(default), será conforme já definido no padrão do processo.

**Observação:**  
As Entidades Contábeis envolvem os campos: Centro Custo (B1\_CC), Item da Conta Contábil (B1\_ITEMCC), Classe Valor Contábil (B1\_CLVL) ou Cta Contábil (B1\_CONTA), definidos no Cadastro de Produtos (MATA010).

**MV\_PRODCTB** : Indica o campo Contábil da tabela SB1 (Cadastro de Produtos) utilizado no Pedido de Compras.

***Saiba Mais :***

***[MV\_PRODCTB](https://tdn.totvs.com/pages/releaseview.action?pageId=271181501)***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
