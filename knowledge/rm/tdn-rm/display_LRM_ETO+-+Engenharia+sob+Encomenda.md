---
content_hash: 9317b2d7fce5671aa39e4a56f7f6ea0f74c16f2e42afddbeeba6faa4340b1ee3
fetched_at: '2026-06-29T00:09:12.954078+00:00'
page_id: '419530101'
product: rm
source: tdn-rm
title: ETO - Engenharia sob Encomenda
type: documentation
url: https://tdn.totvs.com/display/LRM/ETO+-+Engenharia+sob+Encomenda
version: 4
---

O processo de ETO (Engenharia sob Demanda) é um processo onde o produto é especificado, projetado e fabricado mediante encomenda (pedidos).

Está disponível através do o menu principal TOTVS – Linha RM | PROJETOS | ETO ENGENHARIA SOB ENCOMENDA.

Utilizando a solução do RMFactor, especializada em planejamento e controle da produção é possível realizar todo o controle para produção de produtos como:

* **Alocação:** Divisão ou distribuição de produto, atividades, capacidade e custo para as unidades organizacionais como clientes, fornecedores.
* **Demanda:** Necessidade de um produto ou componente especifico
* **Explosão:** Analise de uma lista de materiais no total de cada um dos componentes necessários para a fabricação de determinado produto.
* **Lead time:** Tempo computado entre o início da primeira atividade até a conclusão da última, em uma série de atividades
* **Lote:** Quantidade definida de um produto ou componente que é tratada e identificada como uma entidade no que diz respeito a certas operações, como por exemplo, movimentações, processamento, aquisição, produção, transporte
* **Matéria Prima:** Componente utilizado para fabricar um produto.
* **Necessidade Bruta:** Necessidade total de material para o processo de produção.
* **Necessidade Liquida:** Necessidade Bruta menos o estoque disponível e recebimento s programados.
* **Planejamento:** Processo de planejar e coordenar com base no tempo e também nos recursos disponíveis.
* **Rastreabilidade:** Registro e rastreamento de peças, processo e materiais usados na produção.

Para utilizar o processo de ETO no TOTVS Obras e projetos, é necessário primeiramente, realizar o cadastro dos produtos acabados (termo utilizado pelo Módulo de Suprimentos e Faturamentos) e toda a sua estrutura, componentes e atividades.

Antes de iniciar o cadastro de estrutura, é importante entender que todo produto que se deseja controlar, além da matéria prima ou componentes, deve ser previamente cadastrado no Módulo de Suprimentos e Faturamentos, pois só é possível cadastrar uma estrutura de um produto no RMFactor se já existir um cadastro correspondente no Módulo de Suprimentos e Faturamentos (Menu Cadastro->Produtos).

A estrutura contém a informação do produto que possui itens como componentes e atividades produtivas com o intuito de obter o produto final ou produto acabado.

O produto acabado é o produto que se deseja produção, mas para que esse produto seja produzido são necessários vários outros componentes, chamados de matéria-prima e produto semiacabado.

Os produtos semiacabados são pequenos produtos que também possuem fabricação, e depois de fabricados viram componentes do produto acabado.

A matéria prima será toda a matéria necessária para a fabricação do produto.  
   
**Associação do Produto**

Após o cadastro de toda a estrutura do produto, é necessário associar o insumo do TOTVS Obras e Projetos ao produto manufaturado cadastrado.  
   
**ATENÇÃO!**

É aconselhável que na associação de um produto produzido, seja feita apenas de produtos acabados (termo utilizado pelo RMFactor), para não haver duplicidade de produtos semiacabados na ordem de produção.  
   
Na tela de associação poderão ser cadastrados produtos normais e produtos produzidos a diferença entre eles ocorrerá apenas na solicitação de compra ou produção e será tratada no pedido.
