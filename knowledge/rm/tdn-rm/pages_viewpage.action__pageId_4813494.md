---
content_hash: d5f1376ae03ab3b72b1ba0e26c9b8b208eb7f597548a0a8be10648eb9fc4ca6e
fetched_at: '2026-06-29T00:10:19.361055+00:00'
page_id: '4813494'
product: rm
source: tdn-rm
title: Utilização da Data de Entrega como Default da Data do Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813494
version: 5
---

BLOCK

Utilização da Data de Entrega como Default da Data do Orçamento

FAQ: **Utilização da Data de Entrega como Default da Data do Orçamento**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

***Como Fazer***

Se os itens de um movimento serão recebidos em uma outra Data, de acordo com o cronograma de entregas do Fornecedor, como fazer para que o Controle Orçamentário apresente informações de efeito somente quando estes itens estiverem realmente no meu Estoque?

***Definição do Processo***

Este processo tem por finalidade a parametrização da Data de Entrega dos Itens como Data Default do Orçamento, armazenando informações consistentes em relação ao processo de Compras do sistema.

Solução

***Parametrizações Necessárias***

- Parametrização do novo modelo do Controle Orçamentário

- Parametrização da Data de Entrega no Tipo de Movimento

- Parametrização da Data de Entrega como Data Default do Orçamento

***Descrição do Processo***

Primeiramente, deverá ser feita a parametrização do tipo de movimento, para que, posteriormente, a movimentação possa ser criada e, assim, atualizar as informações do Controle Orçamentário no Item de Movimento.

***Parametrização do Tipo de Movimento***

Acessar os parâmetros do Tipo de Movimento que se deseja utilizar para o Controle Orçamentário, navegar até a etapa Item – Identificação 1/2, alterando o parâmetro ‘Data Entrega’ para ‘Edita’. Com isto, a Data de Entrega dos Itens poderá ser definida pelo Usuário.

Em seguida, navegar até a etapa Orçamento e parametrizar conforme a necessidade do processo na empresa. Na imagem abaixo, segue um exemplo de parametrização:

[![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TROQOHd9JpI/AAAAAAAAFDw/SGweU2eyzJA/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TROQNtkOc9I/AAAAAAAAFDs/kIFxfKsU4wA/s1600-h/clip_image002%5B1%5D.jpg)

Explicando as parametrizações feitas nesta tela:

- De acordo com as parametrizações feitas, o sistema irá aumentar o valor ‘Realizado’ no Orçamento, bloqueando os movimentos caso os valores ultrapassem o valor orçado definido. Além disso, utilizará a Data de Entrega do Item como Data Default.

Nota: A fórmula criada com o código ‘KPU’ utiliza uma variável de fórmula para tratar somente o Valor Unitário do Item de Movimento. Esta fórmula pode ser adaptada para QUALQUER cálculo desejado pelo Cliente.

***Testando a inclusão do Movimento***

Ao incluir um novo Movimento, informe os dados obrigatórios e inclua um novo Item. Neste ponto, será possível identificar o campo de ‘Data de Entrega’, conforme segue:

[![clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TROQPS2UBXI/AAAAAAAAFEA/qjbuuSpvDoE/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh4.ggpht.com/_G7KXZLoZDsY/TROQOtGG6-I/AAAAAAAAFD0/2sat7Or7Hdo/s1600-h/clip_image004%5B1%5D.jpg)

Porém, neste momento, a Data do Orçamento ainda não conterá a informação, pois o sistema depende da gravação do movimento para a aplicação destas informações.

Após salvar o movimento, o Item conterá a informação no campo ‘Data do Orçamento’ na aba ‘Tributos e Valores | Valores’, conforme segue:

[![clip_image006](http://lh5.ggpht.com/_G7KXZLoZDsY/TROQRhtH_ZI/AAAAAAAAFEM/vxiTJnl-kNk/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh4.ggpht.com/_G7KXZLoZDsY/TROQQ2plFII/AAAAAAAAFEI/N4G7vBnlMYc/s1600-h/clip_image006%5B1%5D.jpg)

Importante:

- As informações relativas a este movimento não estarão disponíveis nos relatórios de Consulta de Valores do Orçamento do sistema, devendo ser desenvolvido um relatório específico que buscará as informações deste recurso. Porém, se trata de um recurso muito poderoso na tomada de decisões, já que poderá ser aplicada em uma quantidade rica de cenários: tempo de entrega do Produto, movimentações do Orçamento por Data, GAP entre Data de Entrega e Data de Inclusão do Movimento (funcionando como SCM – Supply Chain Management), entre outros possíveis.
