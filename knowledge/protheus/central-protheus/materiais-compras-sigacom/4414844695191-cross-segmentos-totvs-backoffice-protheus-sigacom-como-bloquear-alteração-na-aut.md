---
article_id: 4414844695191
category: Materiais - Compras (SIGACOM)
content_hash: 2382a0cc5fca6aa18aaf2a0ccea5da9882edb4aa499d74f4148abc9bed006623
fetched_at: '2026-06-28T22:41:14.484735+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como bloquear alteração
  na Autorização de Entrega vinda do Contrato de Parceria?
type: support-article
updated_at: '2022-05-16T22:28:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414844695191-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-bloquear-altera%C3%A7%C3%A3o-na-Autoriza%C3%A7%C3%A3o-de-Entrega-vinda-do-Contrato-de-Parceria
---

**Dúvida**É possível bloquear a alteração de quantidade/valor na Autorização de Entrega vinda do Contrato de Parceria?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**Para que a não seja possível alterar a Autorização de Entrega gerada a partir de um Contrato de Parceria deve-se ativar/configurar dois parâmetros:

**MV\_ALTPRCC:** É utilizado para validar se o preço unitário da AE deve ser igual ao CP, para isso, utilizar as opções abaixo:   **4  5 / 6**

* 0 - Desabilitado: o preço unitário do produto pode ser alterado em qualquer situação.
* 1 – Valida o preço informado no pedido de compras, ou seja, no registro da entrada da nota fiscal (rotina Documento de Entrada) ou na Classificação da Pré-Nota. Não permite alteração no preço unitário do produto quando relacionado a um pedido de compras.
* 2 – Valida o preço informado na autorização de entrega, ou seja, no registro da entrada da nota fiscal (rotina Documento de Entrada) ou na classificação da Pré-nota. Não permite alteração no preço unitário do produto quando relacionado a uma autorização de entrega.
* 3 – Valida o preço informado no pedido de compras e na autorização de entrega (ambos), no registro da entrada da nota fiscal (rotina Documento de Entrada)ou na classificação da Pré-nota. Não permite alteração no preço unitário do produto quando relacionado a um pedido de compras ou a uma autorização de entrega.
* 4 – Valida o preço informado no contrato de parceria, ou seja, na inclusão da autorização de entrega. Não permite alteração no preço unitário do produto relacionado ao contrato.
* 5 – Valida o preço informado no contrato de parceria e na autorização de entrega.
* 6 - Valida o preço informado no pedido de compras, na autorização de entrega e no contrato de parceria.

**MV\_CONTQTD -** Restringe a quantidade do item na autorização de entrega para que não ultrapasse a quantidade original do contrato de parceria vinculado: **1**

1 - Restringe a QTD da AE ao MAXIMO da QTD que consta no contrato de parceria original.  
2 - Desativa a Restrição (DEFAULT)

Após essas configurações ao gerar uma autorização de entrega e tentar alterar seja quantidade ou preço o sistema gera os alertas:

Alterando preço unitário na AE:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414858274199/mceclip0.png)

Alterando quantidade na AE:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414844657815/mceclip1.png)

***Saiba Mais :***

[MV\_CONTQTD - Restringe a quantidade do item na autorização de entrega](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034453954-MP-SIGACOM-Restringir-Quantidade-da-Autoriza%C3%A7%C3%A3o-de-Entrega-maior-que-Contrato-de-Parceria-MV-CONTQTD)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)

[MV\_ALTPRCC- Permitir ou Bloquear alteração do preço unitário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024815131-MP-SIGACOM-Permitir-ou-Bloquear-altera%C3%A7%C3%A3o-do-pre%C3%A7o-unit%C3%A1rio-informado-no-Pedido-de-Compras-MV-ALTPRCC)
