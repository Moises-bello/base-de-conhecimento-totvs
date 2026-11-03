---
content_hash: 4da2c133c00d27e9cc31e56aa8ec436740119dd8135cd5bd6917bb531e5c8d67
fetched_at: '2026-06-29T00:11:32.879631+00:00'
page_id: '750395820'
product: rm
source: tdn-rm
title: Etapa de Cadastros
type: documentation
url: https://tdn.totvs.com/display/LRM/Etapa+de+Cadastros
version: 15
---

Para o correto funcionamento da rotina de *"Inclusão de Movimento Através do XML - NF-e"* devemos ficar atentos ao preenchimento de alguns cadastros. São eles:

---

CadastrosIdCadastrosProdutos

Para efetuar a inclusão de um movimento através do XML é necessário que seja feita a correlação entre os produtos constantes dos XML e os produtos constantes da sua base de dados, ou seja, dos produtos do fornecedor com os produtos do seu estoque.

Este vínculo poderá ser realizado no momento da *"Inclusão de Movimento através de XML - NF-e",* através da Tradução de Itens.

Caso seja a primeira vez que esteja efetuando o processo, ou caso seja a primeira compra do produto para o fornecedor, ao importar o xml será exigido que seja feita a tradução durante a inclusão do movimento. A partir do momento que a primeira tradução for realizada, não será mais necessário refazer este vinculo nas próximas importações de xml (para o mesmo fornecedor/produto). Mais detalhes sobre a Tradução de Itens durante a inclusão do Movimento estará descrita no tópico Inclusão de Movimento Através de XML/Aba Tradução de Itens.

Ou seja, não é obrigatório que a tradução de itens seja  feita previamente.

Mas, caso já possua estas informações, a tradução dos produtos contidos no XML, também poderá ser feita através da tabela *Produtos para Importação de XML*.

O usuário poderá definir um relacionamento de 1 x N, conforme exemplificamos abaixo:

Note que para o produto 100524 podemos ter N produtos vinculados, como por exemplo, os produtos Caneta Esferográfica Azul e Caneta Esferográfica Preta do fornecedor, correspondem a um só produto no estoque, Caneta Esferográfica.

Para incluir produtos na tabela acesse *“Cadastros > Produtos > Anexos > Produtos para Importação de XML”.*

Como todos os demais Anexos do sistema, você poderá acessá-lo a partir da visão de Produtos ou a partir da tela de edição de determinado Produto.

Acesso a partir da visão de Produtos:

Acesso a partir da tela de edição do produto:

Informe o 'Código do Fornecedor', o 'Código do Produto no Fornecedor' e se este for o único produto correspondente para este fornecedor, clique em*"Salvar"* ou *"OK"* para efetuar a gravação do registro ou no ícone *"Incluir"* caso queira gravar o registro e em seguida informar um novo fornecedor e código de produto correspondente para este produto.

Caso o produto possua mais de um produto correspondente no mesmo fornecedor, informe um deles no 'Cód. do Produto no Fornecedor' e clique em "Inserir Múltiplos" para utilizar esse recurso facilitador que permitirá que você inclua vários registros na mesma tela e grave-os de uma só vez.

No campo 'Código do Produto' informe o código do produto no fornecedor e em seguida clique em "Inserir", e assim sucessivamente até que todos os códigos no fornecedor tenham sido informados.

Após informar os códigos de todos os produtos correspondentes nesse fornecedor clique em *"Salvar"* ou *"OK"* para efetuar a gravação do registro ou no botão *"Incluir"* caso queira gravar o registro e em seguida informar um novo fornecedor e produto correspondente para este produto.

Após finalizar a inserção dos Registros Múltiplos, caso opte por "Salvar" o sistema lhe apresentará em tela a mensagem informando os registros que foram gravados.

Para encerrar a informação dos fornecedores e produtos correspondentes a este produto tecle "OK" e o sistema automaticamente sairá da tela de cadastro e exibirá a visão dos Produtos para Importação de XML cadastrados para o seu produto. Vale salientar que caso tenha(m) havido inclusão(ões) a partir da inserção de múltiplos registros será necessário clicar no botão "Atualizar Informações" para que os mesmos sejam apresentados.

O cadastro também pode ser realizado a partir da Cotação, na aba: Produto para Tradução. Ao realizar o orçamento ou negociação

**Importante:** Para que a aba Produto Tradução seja apresentada na cotação, é necessário que o perfil associado ao usuário logado, tenha permissão para acesso a menus em: [01.01.01.04] Editar Produtos.

Unidades do Produto no Fornecedor

Ao cadastrar a unidade de tradução no produto, será possível traduzir itens com unidades de tradução diferente da unidade cadastrada para importação de XML.

Exemplo:

| **Produto** | **Unidade no XML** | **Unidade do Produto no sistema** |
| --- | --- | --- |
| 01.01 | UN | PC |
| 01.02 | UN | UN |
| 01.03 | UN | PC |

O sistema realiza tradução da unidade do produto através da tabela **TUNDPRDCFOCOLAB** e o campo que corresponde a unidade do produto no fornecedor é o **CODUNDCFO**.

Se existir tradução para o produto com unidade cadastrada, ao executar o processo de inclusão de movimento através de XML, a unidade que será preenchida na tradução será a unidade do produto, caso contrário buscamos a unidade de tradução do fornecedor.

É possível cadastrar a unidade do produto manualmente no cadastro de **Produtos para Importação de XML,**em *“Cadastros > Produtos >  Anexos > Produtos para Importação de XML”*

Clique na aba "*Unidade do Produto no Fornecedor"*e preencha as informações da unidade do produto e a unidade do produto no Fornecedor.

Unidades

Da mesma forma que ocorre com os produtos, para efetuar a inclusão via XML é necessário que seja feita a correlação entre as unidades de medida dos produtos constantes dos XML, ou seja das unidades do fornecedor com as unidades utilizadas na sua empresa.

Assim como ocorre com os produtos, este vínculo poderá ser realizado no momento da *"Inclusão de Movimento através de XML - NF-e",* também através da Tradução de Itens. Ou seja, não é obrigatório que tenha uma tradução das unidades de medida cadastrada previamente. 

O sistema realizará a tradução do campo Unidade de Medida ‘CODUND’ através da tabela ‘TUNDCFOCOLAB’, onde será possível cadastrar o código da unidade no fornecedor, e informar a unidade correspondente no sistema, podendo assim evitar a intervenção manual do usuário durante o processo de recebimento.

Para informar a correlação entre as unidades vá em *“Cadastros > Tabelas Auxiliares > Unidade > Anexos > Unidades para Importação de XML”**.*

Você poderá acessar este Anexo exclusivamente da visão de Unidades.

O sistema abrirá o Anexo do lado direito da tela de visão das Unidades.

Clique no botão "Incluir" para inserir as Unidades dos Fornecedores que correspondem à sua Unidade selecionada. Informe ou selecione o 'Fornecedor' (código ou nome), informe o  'Código da Unidade no Fornecedor' e se esta for a única correspondência para esta unidade, clique em *"Salvar"* ou *"OK"* para efetuar a gravação do registro. Caso existam outros fornecedores para o qual essa unidade será utilizada clique no ícone *"Incluir"* para gravar o registro e em seguida informar um novo fornecedor e código de unidade correspondente para esta unidade.

Para encerrar a informação dos fornecedores e unidades correspondentes a esta unidade clique em *"OK"* e o sistema automaticamente sairá da tela de cadastro e exibirá a visão  das Unidades para Importação de XML cadastradas.

É importante salientar que caso o sistema não localize a unidade correspondente você poderá informá-la na tradução do XML que é executada no processo *"Inclusão de Movimento através de XML - NF-e"*.

Natureza de Operação

Quando uma nota fiscal eletrônica é enviada por um fornecedor, ela contém, para cada um dos seus itens, uma natureza fiscal (CFOP) de saída, que caracteriza a operação desse fornecedor. Para a empresa que recebe esse documento, entretanto, devemos encontrar a natureza (CFOP) de entrada correspondente. Essa ‘Natureza Inversa’ é indispensável para a criação de um movimento de NF-e.

No TOTVS Gestão de Estoque, Compras e Faturamento, o cadastro das naturezas inversas***,***está disponível em *“Cadastros > Fiscais > Natureza Fiscal > Anexos > Natureza Inversa para Importação de XML”*.

O sistema irá verificar a Natureza Inversa do CFOP constante da NF-e, ou seja as Naturezas Inversas devem estar cadastradas nas naturezas sintéticas de Saída. Assim, selecione o CFOP sintético para o qual você irá cadastrar as Naturezas Inversas e clique em *"Anexos > Natureza Inversa para Importação de XML"*.

Será apresentada a tela onde você poderá cadastrar as Naturezas Inversas a serem vinculadas à natureza sintética selecionada.

Informe a Natureza Inversa correspondente, marque o campo caso a mesma vá ser uma natureza 'Default' para esta natureza sintética e clique em 'Inserir'.

O sistema apresentará na tela a correspondência entre as naturezas inseridas, permitindo que as demais Naturezas Inversas dessa Sintética sejam incluídas, caso existam.

Informe todas as naturezas inversas de cada natureza sintética de saída e clique em*"OK"* ou *"Salvar"* .
