---
content_hash: cff449761e7955c06f8b363c2a0ddb9ed857ade9fc075577bd9b6766c07d3c0e
fetched_at: '2026-06-29T00:09:27.299025+00:00'
page_id: '423938491'
product: rm
source: tdn-rm
title: Fórmula Visual (Contábil)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938491
version: 19
---

Fórmula Visual é uma ferramenta utilizada para facilitar a criação de procedimentos customizados. O TOTVS Gestão Contábil disponibiliza as seguintes atividades:

**Exemplo de utilização de Fórmulas Visuais na inclusão de Lançamento no Lote**

Ao receber uma parcela financeira de um aluno no sistema TOTVS Educacional, configurar a Inclusão de Lançamento no Lote, gerando integração do Lote automaticamente no sistema TOTVS Gestão Contábil.

falseInserir Lançamento Contábil

A inclusão de lançamentos pode ser realizada em um lote já existente ou em um novo lote criado automaticamente pela fórmula. A estrutura deve seguir o padrão visual da imagem abaixo para garantir a correta inserção dos dados:

##### Regras de Preenchimento

* **Lote Existente:** No campo **Valor**, informe `0` (zero). Neste cenário, não é necessário preencher o período de datas ou a descrição.
* **Novo Lote:** Para que o sistema gere um novo lote, todos os parâmetros devem ser obrigatoriamente preenchidos.

##### Sequenciamento de Atividades

Para operações com múltiplos registros, a fórmula deve ser estruturada de forma linear:

* **Múltiplas Partidas:** Insira atividades de "Inserir Partidas" sequencialmente para cada novo registro desejado.
* **Rateios:** Caso o lançamento possua rateio, a atividade correspondente deve ser incluída logo após a inserção da partida à qual ela pertence.

Exemplo

Detalhes sobre cada atividade acesse:

* [Inclusão de Lote de Lançamento](http://tdn.totvs.com/pages/viewpage.action?pageId=499111177)
* [Inclusão de Lançamento no Lote](http://tdn.totvs.com/pages/viewpage.action?pageId=499111289)
* [Inclusão de Partidas do Lançamento](http://tdn.totvs.com/pages/viewpage.action?pageId=499111381)
* [Inclusão de Rateio da Partida](https://tdn.totvs.com/pages/viewpage.action?pageId=679962138)
* [Salvar Inclusão de Lote](https://tdn.totvs.com/pages/viewpage.action?pageId=679962150)
falseBloqueio e Estorno de Lançamento Contábil

* [Estornar Lançamento Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=679962162)
* [Bloquear Lançamento Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=679962168)
* [Desbloquear Lançamento Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=679962173)
falseLotes

* [Bloquear Lote Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=679962178)
* [Desbloquear Lote Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=679962183)
* [Excluir Lote Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=679962185)
* [Fazer Integração de Lote Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=679962190)
