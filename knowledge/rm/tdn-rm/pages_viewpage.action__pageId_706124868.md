---
content_hash: 0fb69ee3f2c86aa642f47cd10916ee9a3dc8335f4a72a4ba9d59cad3312d017b
fetched_at: '2026-06-29T00:11:22.592897+00:00'
page_id: '706124868'
product: rm
source: tdn-rm
title: Contagem do estoque utilizando o app "Minha Contagem de Estoque"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706124868
version: 39
---

Ao acessar o APP "Minha Contagem de Estoque" pela primeira vez ou se estiver vazio (sem inventários) vai ser feito automaticamente o sincronismo com o TOTVS Gestão de Estoque, Compras e Faturamento - BackOffice (RM), usando o menu no topo lateral à esquerda também é possível selecionar a opção "Sincronizar" que vai enviar e receber dados dos inventários.

Após ter sincronizado os inventários, estes estarão disponíveis no "PAINEL DE INVENTÁRIOS"

Painel de inventários

Clique sobre o inventário  que se deseja realizar a contagem do estoque para seleciona-lo e entrar no modo de edição do inventário

Na tela de edição do inventário iniciamos o processo de contagem de estoque do inventário, a tela de edição traz informações e ações que podem ser realizadas pelo usuário.

Edição de inventários

Veja detalhamento dos campos e ações:

1) Código do inventário

2) Tipo do inventário

3) Indicador de que nesse inventário foi realizado contagem de estoque, mas essa contagem está pendente de sincronismo com o ERP. Para mais informações acesse

4) Esse campo busca itens no inventário, se o produto fizer parte inventário ele vai ser retornado com indicativo se já foi contato ou está pendente de contagem.

5) A opção "Endereços a Inventariar" lista os endereços que fazem parte do inventário, endereçamentos vinculados aos produtos, mostra apenas os que faltam a ser contados.

6) Locais de estoque relacionados ao inventário.

Na tela abaixo a lista de "Endereçamentos a Inventariar" foi apresentada

Na tela abaixo o produto pesquisado foi encontrado, esse produto ainda não teve contagem.

No final da tela temos a opção "Ler endereçamento", clique nesse botão e leia o endereçamento que será realizado a contagem do estoque.

Registro de Contagem

Após ler o endereçamento na tela "Registro de Contagem"  apresentará o endereçamento lido.

Nesse momento deverá ser lido o código de barra do produto, a tela de "Registro de Contagem" vai seguir para contagem de estoque do produto.

No momento de realizar a contagem, é possível modificar a unidade de contagem (1), na quantidade contada é possível incrementar/decrementar a quantidade de 1 em 1 utilizando os botões +/- ou selecionar diretamente o campo e informar a quantidade contada.

Clique em "Salvar" (3) para registrar a quantidade contada e voltar na tela anterior, onde temos o inventário posicionando no endereço.

Clique em "Próximo" para registrar a quantidade contada e abrir novamente a tela do leitor de código de barras para ler em sequencia o próximo produto deste endereçamento.

É possível consultar os produtos que ainda não foram contados, basta clicar no botão  
“Produtos a inventariar” consultado os produtos que a serem contados basta clicar no botão "Produtos a Inventariar".

Leitura do código de barra

Ao clicar no ícone representado por um código de barras do produto ou endereçamento vai ser aberto a tela de leitura do código de barras, aponte a câmera do celular para o código de barras.

Caso seja necessário, pode-se clicar no botão  para ligar a lanterna do dispositivo de forma a facilitar a leitura do código de barras.

Ao realizar a leitura do código de barra, se o produto ou endereçamento não existir vai receber o aviso abaixo, para produto e endereçamento respectivamente.

Clicar em "Digitar código de barras" permite inserir o código de barras manualmente através do teclado, terceira tela, se o valor for válido um produto/endereçamento vai ser selecionado.

Registrar produtos não encontrados durante a contagem

É possível solicitar ao App que registre Produtos a partir da leitura códigos de barras dos produtos que não foram encontrados durante o processo de Contagem.

Para isso é necessário marcar o campo 'Ativar/Desativar Log' no app:

Durante a leitura do código de barras para um Produto, se o mesmo não existir o app irá exibir o aviso abaixo:

Após esse aviso o app irá registrar, no dispositivo, que o código de barras informado não foi localizado para aquele Endereço/inventário.  
Assim, qualquer produto não encontrado será registrado.

Para transmitir esses dados é necessário acessar a opção 'Enviar Logs'.

Ao clicar nessa opção, o sistema irá enviar um arquivo .csv para o e-mail de cadastro do usuário criador do Inventário.

O nome do arquivo terá o seguinte formato: o nome **ProdNaoEncontrados** + data do envio desse e-mail.

Esse e-mail terá o o assunto **Relatório de Produtos não encontrados durante o Inventário.**

O remetente do e-mail esta configurado em **Ambiente/****Parâmetros/Parâmetros Globais** na aba **Envio de E-mails**.

O arquivo enviado conterá os seguintes campos:

* Código da Coligada;
* Código do Inventário;
* Código do Endereço; (registrado a partir da leitura no App)
* Código do Produto;
* Nome do Produto;
* Código de Barras do Produto encontrado no app;
* Usuário da Contagem

Abaixo, um exemplo de como o arquivo se parecerá

Parâmetro da descrição do produto

É possível parametrizar qual o campo do produto será apresentado na "Descrição do Produto".   
  
Este campo é visível tanto para a tela de "Edição de Inventários" quanto para a tela "Registro de Contagem".  
  
  
Segue caminho onde o App realiza a leitura do parâmetro de Parâmetros > Gestão de Estoque, Compras e Faturamento > Parâmetros Gerais > Tabelas > Produto > Definições de Produto 1/3 > Descrição de produto. conforme tela abaixo:

Após parametrização, será necessário necessário Sincronizar o aplicativo para carregar o dado do campo selecionado.

IMPORTANTE

* Para o bom funcionamento da leitura dos códigos de barras a resolução das etiquetas utilizadas devem ser de boa qualidade.
* Os códigos de barras compatíveis a serem utilizados no cadastro de produtos são: EAN 13, EAN 128 e Data Matrix.
* Alguns aparelhos de leitura de código de barras podem apresentar incompatibilidade com o leitor nativo do app, para estes cenários é recomendado que a permissão de acesso à câmera do dispositivo seja removida, e seja utilizado o botão "digitar código de barras", de forma que o leitor do aparelho em questão preencha o texto do código de barras em vez de tentar acessar a câmera do dispositivo.
