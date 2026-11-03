---
content_hash: 825fb720d896f424255162309901cf1cb2c638f26019621f2e214432b074fde3
fetched_at: '2026-06-29T00:12:01.251707+00:00'
page_id: '890542986'
product: rm
source: tdn-rm
title: Acordo Corporativo
type: documentation
url: https://tdn.totvs.com/display/LRM/Acordo+Corporativo
version: 59
---

O "Acordo Corporativo" é uma funcionalidade criada para facilitar a gestão de negociações entre a empresa e seus fornecedores. Com ela, será possível cadastrar os acordos estabelecidos, definindo condições de preço, prazo e quantidade para os itens negociados e garantir que os pedidos sigam o combinado. Com base nas informações a seguir, o usuário poderá utilizar a funcionalidade de forma eficiente, maximizando os benefícios para a gestão de compras da sua empresa.

**Benefícios do Acordo Corporativo:**

* Centralização de informações de negociação;
* Garantia de que os pedidos sigam os preços e condições acordados;
* Maior controle sobre os fornecedores e condições comerciais;
* Flexibilidade para lidar com acordos globais e locais.

# Configurações

Clique no link a seguir para mais informações de

Após as configurações iniciais, defina nos parâmetros dos projetos, a forma que deseja trabalhar o Acordo Corporativo, através da opção Suprimentos/Faturamento>Geral]]>:

O tipo de movimento que será usado para acordo corporativo deverá ser informado no respectivo parâmetro de :

# Perfil de usuário

Para acessar o Acordo Corporativo, o usuário deverá ter a funcionalidade liberada no perfil conforme destacado:

# Navegando pelo sistema

**Acessando o módulo:**

Navegue até "Acordo Corporativo" no menu Controle do TOTVS Construção, Obras e Projetos ou através da URL de acesso WEB:

Ao acessar, o usuário poderá registrar os acordos preenchendo um formulário que será demonstrado na sequência,

**Cadastrando um Acordo:**

Clique no botão "Incluir" na tela de visão do Acordo demonstrada na imagem abaixo:

1. **Cadastro de um Acordo**

Na tela do formulário, serão detalhados cada um dos campos e as regras aplicáveis ao Acordo:

**Campos e regras para inclusão de um Acordo**

1. **Status do Acordo:** Status em que se encontra um acordo. Ao realizar a configuração de um Acordo, ele será automaticamente criado com o status inicial **"Em Negociação"**;

   Importante!

   No momento, este status não poderá ser alterado. A funcionalidade completa para o gerenciamento e a alteração de status dos Acordos será implementada em versões futuras do sistema.
2. **Número do Acordo:** Deve ser preenchido sem máscara (apenas números ou texto simples, limitado a 20 caracteres);
3. **Prioridade:**Campo opcional que permite priorizar um acordo em relação a outro;
4. **Data de Início e Fim do Acordo:** Representam o período de validade do acordo;
5. **Valor mínimo para Faturamento:**Valor mínimo do pedido para o fornecedor;
6. **Moeda:** Moeda na qual o acordo será registrado (ex.: Real, Dólar);
7. **Multicoligadas:** Se sim, significa que os **fornecedores e produtos usados no acordo serão globais e apenas as coligadas que já tiveram a conversão de produto para global poderão ser selecionadas** na respectiva aba do acordo. Se não, deverá informar a coligada do acordo e apenas serão visualizados os produtos e vínculos da coligada em questão. Fornecedores globais são visualizados em todas as coligadas.
8. **Coligada:**
   * Quando o acordo for **multicoligada** (abrangendo coligadas convertidas para produto global), este campo ficará **bloqueado na tela do acordo** e poderá ser informado **no anexo de Coligada,** o que será explicado mais adiante.
   * Quando o acordo **não** for multicoligada, ou sejalocal, será **obrigatório** informar a coligada do acordo e os dados usados  no acordo (Produto, Filial, Projeto), serão apenas da coligada informada.
9. **Fornecedor:**
   * Se o acordo for **multicoligada**, apenas **Fornecedores Globais** serão exibidos;
   * Se o acordo for **local**, o sistema exibirá **Fornecedores Globais** (que conceitualmente são visíveis a todas as coligadas) e os **Fornecedores vinculados à coligada selecionada**.
   * O sistema aplicará os filtros para garantir que apenas fornecedores válidos sejam exibidos;
10. **Contato:** Esse campo possibilita selecionar um contato associado ao fornecedor.
11. **Descrição:** Texto descritivo daquilo que foi acordado entre empresa e o fornecedor em questão;
12. **Observação:** Campo opcional caso seja necessário incluir comentários ou informações adicionais sobre o acordo.

**Salvando o acordo:** Após preencher todos os campos necessários, salve o acordo.

Ao concluir o preenchimento dos detalhes, serão habilitados alguns anexos que também deverão ser cadastrados:

**Item:** Aba onde serão informados os itens (produtos) que irão compor o acordo;

**Coligada:**Onde serão cadastrados as coligadas vinculadas ao acordo.

**Filial:** Nessa aba, temos a possibilidade de vincular o acordo a filiais específicas.

**Projeto:** Os projetos cadastrados nesse anexo, utilizarão os dados definidos no acordo para a criação de seus pedidos.

**Adicionando itens:**

Após salvar o acordo, acesse a aba **Item.** Nessa visão, serão incluídos todos os itens que irão compor o Acordo:

Ao clicar em "Incluir" na visão de **Item** acima, um novo formulário será aberto para que sejam informados os campos referentes ao novo item que será associado:

**Cadastro de Itens no Acordo**

O usuário deverá incluir os itens negociados no mesmo. Veja as regras aplicáveis:

* **Produtos:**Serão listados produtos e serviços de acordo com a coligada informada e de último nível, caso o backoffice utilizado controle níveis de máscara;
  + Para **Acordos Globais**: Apenas produtos globais serão exibidos (código de coligada do produto = 0);
  + Para **Acordos Locais**: Apenas produtos da coligada do acordo serão exibidos (filtrados pelo código da coligada);
* **Preço:** Campo para informar o valor negociado do item quem questão;
  + Possui 4 casas decimais fixas, pois o acordo pode ser multcoligada, e não seria possível utilizar a parametrização de uma coligada especifica.
* **Tipo de Prazo:** Define como será calculado o prazo de entrega, influenciando diretamente a determinação da data final de entrega.
  + **Dias Corridos** (padrão): O cálculo considera todos os dias do calendário, sem exceções.
  + **Dias Úteis**: O cálculo desconsidera dias não úteis, como feriados, sábados e domingos.
* **Prazo de Entrega (em Dias):** Deverá preencher o prazo estimado de entrega considerando os dias que o fornecedor estabelece.
* **Quantidade Mínima:** Define a quantidade mínima permitida no acordo. Por ser um campo obrigatório, o valor padrão será 1. Se o campo "Múltiplo de Quantidade" estiver preenchido, a quantidade mínima deve seguir essa regra..
* **Múltiplo de Quantidade:** Deve ser informado quando as compras tiverem que respeitar múltiplos específicos de quantidade. Por exemplo: se o múltiplo for 5, as compras deverão ser feitas em lotes de 5, 10, 15, etc.
* **Tipo de Frete:** Baseado no cadastro já existente no Gestão de Estoque, Compras e Faturamento;.
* **Observação:** Campo opcional para adicionar comentários sobre o item.

Dicas importantes

**Inclua cada produto negociado, configurando suas condições específicas (preço, prazo, quantidade mínima, etc.).**

* **Verifique os filtros:** Certifique-se de que os fornecedores e produtos exibidos estão corretos para o tipo de acordo (global ou local).
* **Mantenha os prazos atualizados:** Acompanhe a validade dos acordos para evitar expiração sem renovação.
* **Revise os dados:** Sempre revise os campos antes de salvar para evitar inconsistências.

**Vínculo de Coligadas (apenas para Acordos Multicoligada):**

* + A opção para vincular coligadas aparecerá apenas para acordos multicoligadas.
  + O sistema exibirá somente coligadas configuradas para usar produtos globais, com base no **Parâmetro Global do Totvs Gestão de Estoque, Compras e Faturamento**.

**Vínculo de Filiais:**

* + Se o acordo for multicoligadas, apenas filiais das coligadas que utilizam produtos globais aparecerão para seleção.
  + Se o acordo for local (uma coligada específica), somente as filiais da coligada selecionada estarão disponíveis para seleção.

**Vínculo de Projetos:**

* + Se o acordo for local (uma coligada específica), somente as projetos da coligada selecionada estarão disponíveis para seleção.
  + Se o acordo for multicoligadas, projetos de outras coligadas estarão disponíveis para seleção.

O Acordo Corporativo permite apenas um tipo de vínculo por vez. Ou seja, se estiver associado a uma coligada, não poderá ser vinculado simultaneamente a uma filial ou a um projeto. Da mesma forma, caso o acordo esteja vinculado a uma filial ou a um projeto, não será possível vinculá-lo a uma coligada.

**Exportar Itens do Acordo via Excel**

É possível exportar do Acordo Corporativo os itens para o Excel através do processo **Exportar Excel**.

Ao executar o processo, um arquivo do tipo .XLSX será baixado contendo as informações e itens do acordo corporativo.

**Importar itens do Acordo via Excel**

O processo de importação visa agilizar e otimizar a inclusão de diversos itens em um acordo corporativo, eliminando a necessidade de cadastro manual de cada item individualmente.

Para que o processo de importação via Excel funcione, você terá que fazer o download do template pelo processo de **Exportar Excel**, preenchê-lo para depois realizar a importação.

1. Download do template:

   * Clique no botão "**Exportar Excel**" para baixar o modelo de planilha Excel.
2. Preenchimento do template:

   * Abra o template baixado no Excel.
   * Preencha as colunas do template com os dados dos itens a serem importados, seguindo o formato e as instruções especificadas no próprio template.
3. Importação dos dados:

   * Na tela de importação, clique no botão "Selecionar arquivo".
   * Localize e selecione o arquivo Excel preenchido.
   * Clique no botão "Avançar" para iniciar o processo de importação.
4. Confirmação da importação:

   * O sistema exibirá uma mensagem de confirmação ao término do processo de importação.
   * Verifique se todos os itens foram importados corretamente.

**5. Considerações importantes**

* Formato dos arquivos: O sistema aceita arquivos nos formatos XLS, XLSX e CSV.
* Tamanho máximo do arquivo: O tamanho máximo permitido para cada arquivo é de 80MB.
* Estrutura do template: É fundamental seguir a estrutura do template fornecido pelo sistema, incluindo os nomes das colunas e os tipos de dados.

# Geração de Pedidos e Pedidos Extra

Ao incluir um pedido de um fornecedor que possua acordo cadastrado, o usuário terá a opção de informar se o mesmo estará ou não vinculado a um acordo, assim como já acontece com o contrato, no cadastro dos  como também no de item de :
