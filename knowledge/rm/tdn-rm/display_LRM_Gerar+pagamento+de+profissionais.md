---
content_hash: c3b0b507b78bbffd789498f2e145aad02f3c554cc60a57fbdb4bf32c6a279e3f
fetched_at: '2026-06-29T00:09:34.465175+00:00'
page_id: '425459160'
product: rm
source: tdn-rm
title: Gerar pagamento de profissionais
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+pagamento+de+profissionais
version: 2
---

A função deste processo é gerenciar o pagamento de profissionais alocados para trabalhar no processo seletivo. Ele poderá ser executado várias vezes para um mesmo processo seletivo, permitindo que um pagamento gerado anteriormente tenha seu valor modificado ou zerado conforme a necessidade.

Profissionais provenientes do cadastro de "Clientes/Fornecedores" serão pagos por meio de lançamentos financeiros via integração com o RM Fluxus. Profissionais do tipo "Funcionário" serão pagos por meio de lançamentos em suas respectivas folhas de pagamento. Para interagir com a folha de pagamento, o processo utiliza o serviço de inclusão de códigos fixos do RM Labore.

Para que a integração com o RM Fluxus e como o RM Labore funcione, os parâmetros na guia "Informações Financeiras" no cadastro do processo seletivo devem ser configurados corretamente.

**Utilizando o processo:**   
 Do lado esquerdo da tela são exibidos todos os profissionais que foram alocados para trabalhar no processo seletivo. Mesmo os profissionais para os quais não constam presenças registradas são exibidos. Quando um profissional é selecionado na lista, são exibidas informações detalhadas sobre ele no painel no lado direito. Perceba que, para que o botão avançar seja habilitado, é necessário que ao menos um profissional seja marcado na lista. Isto quer dizer que somente os profissionais selecionados terão o pagamento processado durante a execução.

Quando a lista de profissionais é carregada, o valor do campo "Valor do pagamento" é inicialmente preenchido com valor devido ao profissional. O valor devido é obtido de acordo com o "Cálculo do pagamento por dias trabalhados" . O valor para cálculo provêm da tabela auxiliar "Tipo de profissionais" e sua remuneração.

O "Valor do pagamento" poderá ser alterado pelo usuário. Os profissionais sem registro de presenças são exibidos justamente porque é facultada à instituição a possibilidade inclusão de pagamentos para os mesmos. Dessa forma, o "Valor devido" ganha um caráter de sugestão a ser confirmada ou não pelo o operador do sistema. Clicando-se no botão "Valor Original" é possível retornar o "Valor do pagamento" ao "Valor devido" calculado inicialmente.

O sistema mantém o pagamentos desses profissionais e por meio desse controle é possível determinar se algum valor já foi pago para um profissional referente aquele processo seletivo. Essa informação, "Valor lançado anteriormente", é exibida no painel "Cálculo por dias trabalhados".  O processamento do pagamento poderá recair em 3 comandos possíveis na chamada ao serviço de integração:  
 Inclusão: o "Valor do pagamento" é maior que zero e "Valor lançado anteriormente" é zero, ou seja, primeira execução do processo.

Alteração: o "Valor do pagamento" é maior ou menor que o "Valor lançado anteriormente", ou seja, re-execução do processo alterando valores ou não.  
 Exclusão: o "Valor do pagamento" é zero e o "Valor lançado anteriormente" é maior que zero, ou seja, se você quiser excluir este pagamento, é necessário colocar um valor =0 no valor a pagar.

**Cuidados ao executar o processo para**:  
 Funcionário: (RM LABORE)   
Inclusão: ocorre à tentativa de inclusão de um código fixo para o funcionário no qual o valor passado será o "Valor do pagamento" e o parâmetro "Número de vezes" requerido pelo serviço de integração será sempre 1. Caso já exista um código fixo cadastrado anteriormente com o mesmo "Código de Evento" para o funcionário, o serviço de integração trata de somar o "Valor do pagamento" ao valor que já está cadastrado. Essa operação pode não ser bem sucedida, retornando um erro se já existir um código fixo com mesmo "Código de Evento" cadastrado para o funcionário e o "Número de Vezes" for maior que um.   
 Alteração: o serviço de integração disponibilizado pelo RM Labore não trabalha com o conceito de alteração de lançamentos. É feita a mesma chamada utilizada na operação de inclusão. Porém, o valor é passado para o serviço de integração de acordo com o efeito desejado. Se o pagamento estiver sendo alterado para um valor maior que o já lançado anteriormente, então é feita uma chamada de inclusão com o valor da diferença a maior. Se o pagamento estiver sendo alterado para um valor menor que o já lançado anteriormente, então é feita uma chamada de inclusão com o valor negativo correspondente a diferença a menor. O sucesso da operação também se restringe as condições citadas anteriormente.   
 Exclusão: o serviço de integração disponibilizado pelo RM Labore não trabalha com o conceito de exclusão de lançamentos. Para contemplar essa situação também é feita mesma chamada utilizada na operação de inclusão. Porém, o valor passado é o oposto (negativo) do valor que foi lançado anteriormente. Ou seja, ocorre a tentativa de se zerar o valor lançado anteriormente.

**Pré - requisitos do processo**:   
 **a)** O processo seletivo para o qual o processo será executado deverá ter encerrado o período de seleção.  
 **b)** As "Informações Financeiras" para pagamento de profissionais deverão ter sido preenchidas para o processo seletivo. O não preenchimento dessas informações não impedirá que o processo seja executado, mas chamadas aos serviços de integração não serão bem sucedidas.  
 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
 **Integração com o Protheus através do Totvs Business Connect - TBC**  
 Foi implementado a integração com o Protheus através de mensageria para que seja possível efetuar lançamentos na folha de um funcionário que está cadastrado no módulo de RH do Protheus.   
 Para que esta integração entre o Totvs Processo Seletivo e o Protheus ocorram é necessário efetuar a instalação do Totvs Business Connect e configurar o Web Service para troca de mensagens XML entre os sistemas.  
 A integração se dá nos dois sentidos:

* Protheus -> RM : será enviado do Protheus para o RM os cadastros de "Centro de Custo" , " Eventos" e os "Funcionários".
* RM -> Protheus: será enviado do RM para o Protheus o lançamento a ser lançado na folha do funcionário.

**Pré requisitos:**

Utilizar o Evento, Centro de Custo e Funcionário que foram importados ao RM através da integração ; Utilizar fórmula visual para envio do lançamento para a folha de pagamento do funcionário no Protheus.
