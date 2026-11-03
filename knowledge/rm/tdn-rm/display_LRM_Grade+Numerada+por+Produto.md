---
content_hash: fcc2d753a91ffe260f0d8a0493946e95f9803e7e8aac378a120cb7c0ec4a2555
fetched_at: '2026-06-29T00:09:25.375480+00:00'
page_id: '423938134'
product: rm
source: tdn-rm
title: Grade Numerada por Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Grade+Numerada+por+Produto
version: 5
---

A Grade Numerada por Produto é utilizada para se fazer um controle detalhado do estoque físico. A utilização da grade numerada por produto facilita o cadastro e controle de estoque para produtos com especificações similares. Exemplo de Produto com Grade Numerada:

|  |  |  |
| --- | --- | --- |
| **Produto Base da Grade:** Camisa | | |
| **Tamanho** | **Cor** | **Item da Grade** |
| P | Azul | Camisa, P, Azul |
| M | Azul | Camisa, M, Azul |
| G | Azul | Camisa, G, Azul |
| P | Amarelo | Camisa, P, Amarelo |
| M | Amarelo | Camisa, M, Amarelo |
| G | Amarelo | Camisa, G, Amarelo |

Com a grade numerada por produto cada item de grade numerada será um produto independente, de último nível e poderá ser referenciado diretamente na inclusão do movimento, a gestão do estoque é muito mais efetiva pois todo o custo é por produto.  
   
**Identificação**

A grade numerada por produto será criada à partir de um produto base. Cada grade numerada (produto base) estará então associada a um cadastro de linhas e colunas. A combinação de cada linha com cada coluna de uma grade numerada será então representada por um novo produto de último nível no cadastro de produtos.

Código da Grade: Definição dó código que que armazenará a grade.

Produto Base: produto que será vinculado a grade. O produto base deverá ser de nível analítico e ter o parâmetro "Base para Grade Numerada" marcado no cadastro do produto.

Nome da Linha:  descrição que será apresentada na aba da linha da grade.

Nome da Coluna: descrição que será apresentada na aba da coluna da grade.

**Linha**

Nesta aba é possível incluir/editar/excluir as linhas da grade numerada. Exemplo:

|  |  |
| --- | --- |
| **Linha de Grade:** Tamanho | |
| **Código** | **Descrição** |
| P | Pequeno |
| M | Médio |
| G | Grande |

Para inserir uma nova linha pressione INSERT, para inutilizar uma linha marque a opção inativo.

**Coluna**

Nesta aba é possível incluir/editar/excluir as colunas da grade numerada. Exemplo:

|  |  |
| --- | --- |
| **Coluna de Grade:** Cores |  |
| **Código** | **Descrição** |
| AM | Amarelo |
| AZ | Azul |
| BR | Branco |
| PR | Preto |
| VE | Vermelho |

 Para inserir uma nova coluna de grade pressione INSERT, para inutilizar uma coluna de grade marque a opção inativo.

**Produtos da Grade**

Nesta pasta serão visualizados todos os produtos de grade numerada gerados pelo processo de Assistente de grade numerada. Os produtos gerados serão de último nível da mascará do produto, vale ressaltar a importância de verificar a máscara do cadastro dos produtos se contemplará a necessidade da empresa em termos de crescimento.

**Processos de Assistente Grade Numerada:**

* **Criar novo produto base para grade numerada:**Através desta opção será criado um novo produto base a partir de um pré-existente.
* **Criar nova grade numerada com base em outra existente:**Através desta opção será criada uma nova grade numerada com a estrutura de outra grade, as linha e colunas serão copiadas para a nova grade.
* **Criar novos produtos de grade numerada:**Através desta opção poderão ser criados novos produtos de grade numerada. Os produtos serão criados de acordo com a combinação Linha x Coluna escolhida.
* **Copiar dados do produto base para os produtos de grade numerada:**Através desta opção serão copiados dados do cadastro do produto base para os produtos de grade numerada originados deste.
