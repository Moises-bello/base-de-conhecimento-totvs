---
content_hash: 6316cda73c20994174b81c9e25a5de4ce2f9bb78e67ed63fcf9289dc345b4cfc
fetched_at: '2026-06-29T00:11:09.561310+00:00'
page_id: '640208931'
product: rm
source: tdn-rm
title: 03. Portal do Fornecedor | Principais Funcionalidades
type: documentation
url: https://tdn.totvs.com/display/LRM/03.+Portal+do+Fornecedor+%7C+Principais+Funcionalidades
version: 99
---

5%90%PaginageralAutenticacao\_usuarioAutenticação do usuário

O fornecedor deve ser convidado para participar de uma cotação, através do processo de [Comunicar Fornecedores](https://tdn.totvs.com/pages/viewpage.action?pageId=423938220) utilizando a opção "**Exportar Orçamento p/ Web**"

Um e-mail será enviado com o conteúdo estipulado pelo relatório selecionado no processo, junto com o usuário e senha.

O código de acesso e senha enviados para o fornecedor é único.

Caso o fornecedor tenha esquecido a senha, uma nova senha poderá ser enviada marcando a opção **Regerar Senha**

Não é necessário ter usuário no sistema para usar o portal, os usuários do portal são criados a cada comunicação e os já existente são mantidos para facilitar o gerenciamento por parte dos fornecedores.

Informação

Na tabela TCAUTHFORNECEDOR fica gravado o usuário e a senha, sendo esta criptografada.

Painel\_CotacoesPainel de Cotações

Esta tela é responsável por exibir todas as solicitações de cotação recebidas pelo fornecedor, as quais são agrupadas pela situação corrente do registro:

* **Pendentes:**Cotações exportadas para a Web, cuja data limite de resposta seja superior a data atual e que ainda não tenham sido respondidas pelo fornecedor.
* **Enviadas:**Cotações que foram enviadas para o comprador, cuja data limite de resposta seja superior a data atual e que ainda não tenham sido respondidas pelo fornecedor.
* **Finalizadas:**Cotações que foram canceladas, concluídas ou finalizadas (ordem de compra gerada).

PainelPendentesPendentes

Na aba responsável por exibir as cotações **Pendentes,** será possível verificar o status de conclusão, são eles:

* Não iniciada: Fornecedor não iniciou o preenchimento
* Andamento; Fornecedor iniciou o preenchimento da cotação e pode observar a quantidade de itens já preenchidos através da coluna **Nº Itens**, que mostra itens preenchidos/total de itens da cotação.

Em suas ações contamos com duas opções:

Editar acessa os detalhes da cotação, é possível visualizar este acesso observando a página "Detalhes da cotação".

Declinar sinaliza ao comprador que o fornecedor ficará de fora desta cotação, após realizar o declínio esta cotação sai da página "**Pendentes**" indo para a página "**Enviadas**".

Ao declinar, o fornecedor poderá informar o **motivo do declínio da cotação** e essa informação é opcional, o motivo informado é limitado a 100 caracteres e o comprador tem acesso a essa informação.

EnviadasEnviadas

Na aba responsável por exibir as cotações **Enviadas,** será possível realizar algumas ações.

Depois de enviado o orçamento inicial, o fornecedor poderá registrar os valores negociados para uma nova avalição do comprador.

Mesmo depois de enviado, caso a cotação ainda esteja dentro da data limite, o fornecedor poderá realizar alterações no orçamento enviado anteriormente, sem a necessidade de iniciar uma negociação.

Mesmo depois de enviado o orçamento, o fornecedor poderá declinar da cotação.

  Caso o fornecedor tenha declinado, mas gostaria de retornar ao processo de cotação, basta selecionar a ação **Participar** .

FinalizadasFinalizadas

Na aba responsável por exibir as cotações **Finalizadas,** será possível verificar o status de conclusão, são eles:

* Encerrada (Fornecedor não ganhou a cotação)
* Vencedor (Fornecedor foi o ganhador da cotação)
* Cancelada (Cotação cancelada pelo comprador)

OrcamentoOrçamento

Quando o fornecedor inicia o preenchimento do seu orçamento, será direcionado para o fluxo de preenchimento dos dados, até poder finalizar e enviar para o comprador.

OrçamentoDados\_GeraisDados Gerais

Nesta primeira tela é possível editar as informações de orçamento da cotação.

Os campos  despesa, desconto e condição de pagamento serão exibidos mediante parametrização do sistema.

Quando o fornecedor clica em **Salvar e continuar**é direcionado para a tela onde poderá visualizar os itens da cotação.

Itens de Orçamento (Visão)

Nesta tela temos acesso a lista de itens a serem cotados, é possível visualizar de forma rápida e prática as informações principais e até os detalhes de cada um.

Para iniciar o preenchimento da cotação, existem duas formas, sendo elas:

**1 - Edição do item:** clicar no ícone   do item desejado (vide aba Item de orçamento (Edição)).

**2- Edição na Visão:** clicar na linha do item e editar o campo desejado (**recurso disponível a partir da versão 12.1.2406**).

Ao clicar em **Salvar Itens**, as informações alteradas serão salvas e os itens cujo a coluna de preço for maior que 0 o status será alterado para Cotado.

Ao clicar em **Finalizar e Enviar**, será apresentado um totalizador e neste momento o sistema finalizará a cotação, redirecionando para o **Painel de Cotações,** filtrando as cotações **Enviadas**.

Clicando no ícone de **engrenagem** será exibido os campos que serão apresentados como colunas, na Grid de visualização/edição.

É possível também, por meio do botão: **Aplicar aos itens**, preencher condição de pagamento e informações de tributos. Ao clicar em **Aplicar**, essas informações serão aplicadas a todos os itens da cotação.

 

Item de orçamento (Edição)

Esta etapa da cotação, basicamente, tem por objetivo registrar o orçamento do produto selecionado.

No bloco **Solicitação** serão exibidos dados da solicitação do produto, tais como unidade solicitada e marca solicitada.

No bloco **Orçamento** será possível cotar o produto, neste momento, os campos serão exibidos mediante parametrização do sistema, garantindo o mesmo comportamento da MDI.

O Campo **Código do produto**é utilizado para realizar o de/para do código do produto no fornecedor e o código do produto no RM, para ser utilizado nas traduções de xml.

 

O produto pode ser marcado como **indisponível**, desta forma o comprador saberá que o fornecedor não possui o produto solicitado. Quando marcado como indisponível, apenas o campo **observações** pode ser preenchido.

No bloco **Solicitação,**é possível navegar entre os itens do orçamento (clicando no "**de**"), facilitando a localização e redirecionamento para um produto específico.

Quando alguma informação é editada neste formulário, caso o usuário tente **sair** da página atual, o sistema emitirá um alerta informando que os dados não salvos serão perdidos.

O formulário de edição possui três ações principais, as quais mudam de acordo com o índice do produto na relação de itens a serem orçados. A opção cancelar é fixa e será responsável por cancelar a edição do formulário e voltar a tela anterior. Caso o produto selecionado seja o primeiro da lista, exemplo: "**1** de 12", serão apresentados os botões **Salvar e Voltar**e **Salvar e Próximo**.

* **Salvar e Voltar**: Persiste os dados de orçamento do item corrente e volta para a tela anterior.
* **Salvar e Próximo**: Persiste os dados de orçamento do item corrente e redireciona para o próximo item.

Caso o produto selecionado seja o último da lista, exemplo: "**12** de 12", serão apresentados os botões **Salvar e Anterior**e **Finalizar e Enviar**.

* **Salvar e Anterior**: Persiste os dados de orçamento do item corrente e redireciona para o item anterior.
* **Finalizar e Enviar**: Persiste os dados de orçamento do item corrente e finaliza a cotação. Neste momento o sistema finalizará a cotação para este fornecedor, e redirecionará para o **Painel de Cotações** já filtrando as cotações **Enviadas**.

Durante a finalização e envio da cotação, caso algum produto **não** tenha sido Cotado, o fornecedor será alertado. Desta forma será possível corrigir a situação em casos de esquecimento. Caso o fornecedor opte por enviar nesta situação, os produtos serão exibidos ao comprador com o status **Não Cotado.**

Caso todas as informações obrigatórias sejam preenchidas, o sistema emitirá uma confirmação de envio. Assim como na situação onde existem produtos não cotados, o sistema exibirá o **Valor *Bruto* Atual** da cotação, ou seja, será calculado neste momento apenas o valor total considerando a quantidade x preço informado nos itens de orçamento, neste momento não serão realizados cálculos de descontos, despesas, frete, etc...

Caso o sistema esteja parametrizado para utilizar condição de pagamento por item de orçamento, será habilitada a opção [Composição de Preços](https://tdn.totvs.com/pages/viewpage.action?pageId=423938220).

Este recurso permite informar o preço de acordo com a condição de pagamento, auxiliando o comprador na tomada de decisão.

NegociacaoNegociação

Quando o fornecedor inicia o preenchimento da negociação terá uma experiência semelhante ao do preenchimento do orçamento.

NegociaçãoItem de Negociação (Visão)

A visão de itens a serem negociados funciona da mesma forma que a visão de itens a serem cotados, vide "**Itens de Orçamento (Visão)**".

No entanto, em relação a negociação, a funcionalidade "**Aplicar aos itens**" não estará disponível.

Item de Negociação (Edição)

Ao acessar a lista de cotações **enviadas** e clicar no botão **negociar**, será possível registar uma negociação para o produto, ou seja, diminuir o valor orçado.

O Campo **Código do produto**é utilizado para realizar o de/para do código do produto no fornecedor e o código do produto no RM, para ser utilizado nas traduções de xml.

 

Com o objetivo de facilitar o preenchimento da negociação, é possível visualizar os dados do orçamento realizado clicando no botão **Visualizar Orçamento.**

anexosAnexos da CotaçãoAnexos da Cotação

O recurso de anexos no portal está desabilitado por default.

Para disponibilizar, é necessário configurar a quantidade de arquivos que podem ser anexados nos parâmetros da cotação [Definições Gerais 6/6](https://tdn.totvs.com/pages/viewpage.action?pageId=423938121#Defini%C3%A7%C3%B5esGeraisDeck-1568666568).

É possível anexar arquivos na cotação a qualquer momento, desde que a cotação ainda não tenha sido finalizada.

Os arquivos podem ser anexados por meio das seguintes telas:

* Detalhes da Cotação (Orçamento)
* Visão dos Itens da Cotação
* Edição do Item da Cotação

Ao clicar no botão de anexos, o sistema exibirá uma tela lateral com os seguintes recursos?

* Visualizar arquivos já anexados
* Remover um arquivo anexado
* Anexar arquivos
* Fazer download do arquivo em anexo

Compatibilidade

Atualmente o portal do fornecedor está homologado para os seguintes **Navegadores:**

* Chrome versões mais recentes (latest)
* Firefox versões mais recentes (latest)
* Edge 2 últimas versões principais
* IE 11 \*deprecated, veja o guia de depreciação oficial do Angular
* Safari 2 últimas versões principais
* IOS 2 últimas versões principais
* Android Q (10.0), Pie (9.0), Oreo (8.0), Nougat (7.0)

O Portal do Fornecedor foi desenvolvido para ser responsivo até o nível de tablets para oferecer a melhor experiência ao fornecedor.

0solid

---

---

560px

 [Voltar para o Menu Principal](https://tdn.totvs.com/display/LRM/Portal+do+Fornecedor)

---

---

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
