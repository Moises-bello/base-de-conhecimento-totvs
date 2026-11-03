---
article_id: 360020735492
category: Materiais - Compras (SIGACOM)
content_hash: 3d88e496dcfee337667dec4cd7c0331491bb28d6e4ac5ede8d6e460a06959399
fetched_at: '2026-06-28T22:41:07.553733+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar Controle
  de Alçadas utilizando Tipo de Compras ?
type: support-article
updated_at: '2026-02-06T12:53:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020735492-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-Controle-de-Al%C3%A7adas-utilizando-Tipo-de-Compras
---

**Dúvida**

Como configurar Controle de Alçadas utilizando Tipo de Compras ?

**Ambiente**

Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

A rotina de Tipo de Compra é um cadastro opcional que permite a definição de critérios de Políticas de compra mais avançadas que poderão ser aplicadas aos documentos de Solicitações de Compra e Pedidos de Compra

Links/Vídeos How-To/Webinar sobre a funcionalidade:

[- Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Diferença entre " Aprovador Especial " x " Aprovador Padrão " na rotina Tipo de Compras (COMA200)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001869541-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Diferen%C3%A7a-entre-Aprovador-Especial-x-Aprovador-Padr%C3%A3o-na-rotina-Tipo-de-Compras-COMA200-?source=search)

[- How To | SIGACOM  -  Tipo de Compras (COMA200): Aprovador Padrão](https://www.youtube.com/watch?v=WiTxsyeqUKE)

[- How To | SIGACOM  -  Tipo de Compras (COMA200): Aprovador Especial](https://www.youtube.com/watch?v=imQf541k9X8)

[- Assistam Nosso Evento/Webinar de Alçada Entidade Contábil x Tipo de compra](https://www.youtube.com/watch?v=otrgwaI2pRw)

Abaixo algumas informações sobre a funciondalide:

Informação do tipo de Aprovação rotina **COMA200**:

* **Aprov. Especial**  
  Quando marcado, o aporvador com este tipo de compras vinculado, aprovará os itens que obedecerem à regra deste Tipo de Compra vinculado.
* **Aprov. Padrão**  
  Será efetuada a alçada padrão do sistema considerando apenas os aprovadores que não possuem tipos de compras associados ou que não obedeceram à regra do Tipo de Compras vinculado.

Abaixo consta tela de cadastro do Tipo de Compras(COMA200)para verificar onde é possível criar as regras:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055619333)

Segue documentação da rotina Tipo de Compras com detalhes para análise:

[Tipos de Compras - Básico](http://tdn.totvs.com/pages/viewpage.action?pageId=267795014)

[Tipo de Compras - Alçada](https://tdn.totvs.com/display/public/PROT/8+-+Tipo+de+Compra)

***Obs:***

Para uso da funcionalidade de Tipo de Compras, primeiramente o Pedido de Compras ou Solicitação de Compras necessita entrar no processo de alçada normal, ou seja, precisa cumprir os requisitos para este Pedido ou SC entrar no processo de alçada configurado no Grupo de Aprovação fora da Aba de "Tp. Compra X Aprovador", para então estando na alçada, ele passar a verificar as regras cadastradas no Tipo de Compras vinculados na aba "Tp. Compra X Aprovador".

***Obs2:***

A funcionalidade Tipo de Compras funcionará corretamente por itens individualmente, quando o Controle de Alçadas por Entidade Contábil está ativo, ou seja, parâmetro MV\_APRSCEC = T e/ou MV\_APRPCEC = T, bem como Entidade Contábil preenchida no Grupo de Aprovação e Solicitação de Compras e/ou Pedido de Compras com Entidade Contábil preenchida (No mínimo Centro de Custo).

***Saiba Mais :***

[PCOM09006 - Tipos de Compra (COMA200)](https://tdn.totvs.com/pages/releaseview.action?pageId=267795014)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Diferença entre " Aprovador Especial " x " Aprovador Padrão " na rotina Tipo de Compras (COMA200)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001869541-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Diferen%C3%A7a-entre-Aprovador-Especial-x-Aprovador-Padr%C3%A3o-na-rotina-Tipo-de-Compras-COMA200-?source=search)

[How To | SIGACOM  -  Tipo de Compras (COMA200): Aprovador Padrão](https://www.youtube.com/watch?v=WiTxsyeqUKE)

[How To | SIGACOM  -  Tipo de Compras (COMA200): Aprovador Especial](https://www.youtube.com/watch?v=imQf541k9X8)

[MP - SIGACOM - Como utilizar o Tipo de Compra para alçada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011914111)

[PCOM09017 - Tipo de Compras - Campos que podem ser utilizados nas regras](https://tdn.totvs.com/x/hqnKMQ)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Uso de Filtro pela opção "Função" na rotina de Tipo de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25245405872407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Uso-de-Filtro-pela-op%C3%A7%C3%A3o-Fun%C3%A7%C3%A3o-na-rotina-de-Tipo-de-Compras)

[8 - Tipo de Compra](https://tdn.totvs.com/x/2bptHg)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
