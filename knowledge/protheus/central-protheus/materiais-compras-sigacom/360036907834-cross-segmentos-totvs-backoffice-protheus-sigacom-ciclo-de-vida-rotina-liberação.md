---
article_id: 360036907834
category: Materiais - Compras (SIGACOM)
content_hash: 65c55fcf5793901f6a502cc3c1e8afa9b999c807241cd8a4d87821c51141425a
fetched_at: '2026-06-28T22:41:07.488713+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - CICLO DE VIDA - Rotina
  Liberação de Documentos (MATA097)
type: support-article
updated_at: '2022-05-16T22:11:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036907834-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-CICLO-DE-VIDA-Rotina-Libera%C3%A7%C3%A3o-de-Documentos-MATA097
---

**Dúvida**

CICLO DE VIDA - Rotina Liberação de Documentos (MATA097)  
  
**Ambiente**

Protheus – Compras – A partir da 12.1.17  
  
**Solução**

Ao acessar a rotina de Liberação de Documentos do Compras (**MATA097**) o sistema retorna os Helps abaixo sobre Ciclo de Vida e substituição da rotina.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048235414/mceclip0.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048236214/mceclip0.png)

A rotina de Liberação de Documentos foi substituída por uma nova rotina com mesma finalidade que já está disponível no repositório de objetos. A substituição da rotina visa a evolução do produto.

Somente a nova rotina possibilitará a liberação dos documentos a partir de Julho/2019.

*Rotina anterior:* **MATA097** - Liberação de Documentos

*Rotina atual:* **MATA094** - Liberação de Documentos

***Vantagens:***

- Possibilita a liberação de documentos de vários tipos, e não apenas do tipo pedido de compras.  
- Possibilita utilizar o controle de alçadas por entidade contábil.

***Procedimentos para utilização:***

Não há a necessidade de realizar nenhuma configuração para utilização da nova rotina. É necessário somente alterar no Configurador a chamada do programa no menu do Protheus de "MATA097" para "MATA094" caso não esteja com o menu atualizado do [Portal do Cliente](https://totvscst.zendesk.com/hc/pt-br/#home)

***Customizações**:*

Caso possua customizações na rotina antiga, será necessário revisá-las pois a estrutura e a tecnologia da rotina nova é diferente.

***Estrutura de Dados:***

- **SCR** - Documentos com Alçada permanece gravando os dados referente aos documentos bloqueados, bem como a gravação das liberações.

- **DBM** - Itens do Documento com Alçada que irá apresentar os itens que fazem parte do documento a ser liberado.

***Documentos Relacionados:***

[MATA097: Liberação de Documentos](https://tdn.totvs.com/pages/viewpage.action?pageId=372558515)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
