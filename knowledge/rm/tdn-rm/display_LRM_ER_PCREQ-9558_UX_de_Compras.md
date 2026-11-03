---
content_hash: d7a459418f72518d802927e462f9684345cd533e5d8ee65d62a5663de255e563
fetched_at: '2026-06-29T00:08:04.447103+00:00'
page_id: '235570935'
product: rm
source: tdn-rm
title: ER_PCREQ-9558_UX_de_Compras
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9558_UX_de_Compras
version: 146
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_CP\_MOV011 | **IRM1** | PCREQ-9556 |
| **Requisito1** | PCREQ-9558 | **Subtarefa1** | PDR\_CP\_MOV011-45 |
| **Chamado2** | Não se aplica. | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Não se aplica. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Revitalização do módulo de compras baseado nos levantamentos feitos através do projeto de UX, visando melhorar a usabilidade e experiência do usuário. 

## Definição da Regra de Negócio

Neste release, elencamos os seguintes itens para que possamos iniciar o processo de revitalização do módulo de compras. 

* ## Disponibilizar o campo CNPJ na visão de inclusão de fornecedores no processo de inclusão de cotação.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, no **Assistente de Cotação** existe um passo para **Escolha de Fornecedores** e **Escolha de Fornecedores - Qualificação**. Nessas duas telas ficará disponível para exibição a informação do **CNPJ/CPF** do fornecedor.

 Para que esta opção fique disponível na visão, deve-se **Configurar Colunas** e selecionar a coluna **CNPJ / CPF**ou clicar na opção **Restaurar configuração padrão** da janela **Selecionar colunas**:

Após escolher a coluna e definir a sua ordem de exibição, ela ficará disponível na visão de fornecedores conforme imagem abaixo:

**Escolha de Fornecedores**:

**Escolha de Fornecedores - Qualificação:**

* ## Ao compor a cotação, na fase de seleção do fornecedor, ao incluir um novo fornecedor aparece como primeira opção de filtro a cidade. Deveria ter como primeira opção o CNPJ ou nome fantasia ou razão social.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, no **Assistente de Cotação** existe um passo para **Escolha de Fornecedores** e **Escolha de Fornecedores - Qualificação**. Ao incluir um novo fornecedor, existe a possibilidade de filtrar os fornecedores por alguns campos. Nesse filtro, o campo que aparece como default é Cidade. Será alterado para **CNPJ/CPF.**Os campos **Nome Fantasia e Razão Social** tambémpoderão ser utilizados como filtros na busca de novos registros.

* ## Ter a possibilidade de enviar e-mail da ordem de compra somente para contato dos fornecedores, pois hoje só há como enviar com cópia para contato.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, quando o status de uma cotação está **Pedido de Compra**, há a possibilidade de enviar a Ordem de Compra por e-mail (opção: **Envio de Ordens de Compra via mail**). Na tela de **Seleção de Parâmetros do Cabeçalho do E-mail**, existe a opção **Cópia de E-mail para contatos Cliente/Fornecedor**, que faz o envio da Ordem de Compra para o contato principal do fornecedor e seus respectivos contatos cadastrados. Vamos disponibilizar uma opção para que seja feito o envio do e-mail apenas para os contatos do fornecedor, ignorando o e-mail principal. O e-mail principal será uma opção na tela de envio e será exibida marcada por padrão. Será permitido enviar e-mail individualmente para as demais opções e a única opção que será enviada como cópia será a opção Cópia de e-mail para Usuário Logado.

* ## Colocar status de envio da ordem de compra para que na visão o comprador identifique que a OC foi enviada.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Ordem de Compra,** haverá na visão um campo para identificar o status de envio de ordem de compra, visando facilitar a identificação do mesmo pelo usuário. Os status serão: **Enviado** e **Não Enviado**. Esse campo também será visualizado através da **Cotação** pelo anexo **Pedido Gerados.** 

**Observação:** na visão de Movimento este campo ficará disponível somente se o parâmetro Envia E-mail estiver habilitado para o tipo de movimento selecionado.

 

* ## Na negociação o campo de preço cotado vir com aspecto de campo bloqueado. Atualmente ele parece estar desbloqueado para edição, mas não permite a edição.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e editar uma cotação para registrar negociação os campos Preço Cotado, Unidade Solicitada e Orçada, Prazo Entrega, Coligada Movimento, Código e Descrição do Produto e Quantidade Solicitada, Orçada e Negociada, % ICMS Orçado, %ICMSST e Margem de Lucro ICMS ST, que não são permitidos a edição irão apresentar o aspecto acinzentado. Os campos de Percentual e Valor de Desconto e Despesa que são habilitados por parâmetro da Cotação terão o mesmo comportamento quando não se permitir a edição. Para o registro de orçamento os campos  Unidade Solicitada, Coligada Movimento, Código e Descrição do Produto e Quantidade Solicitada e Orçada e os campos Percentual e Valor de Desconto e Despesa que são habilitados por parâmetro da Cotação terão o mesmo comportamento quando não se permitir a edição. Vide figura abaixo do campo Preço Cotado para a negociação.

* ## Na tela de cotação ser possível abrir a tela de edição do movimento de solicitação de compra, assim como pode ser feito com o movimento de ordem de compra gerado.

 Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e editar uma cotação para visualizar a aba de Itens de Movimento no clique duplo na Grid no Item de Movimento será exibido o Movimento associado ao mesmo, tanto para Solicitação de Compra quanto para Ordem de Compra. No anexo de Itens de Movimento será possível visualizar o movimento associado, portanto, não sendo necessário editar a cotação.

* ## Possibilidade de visualizar a tela de edição da cotação através do rastreamento de movimentos, ao clicar no registro de cotação.

 Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Solicitação de Compras** e visualizar a rastreabilidade do movimento que originou a cotação no clique duplo da Grid será exibida a Cotação.

* ## No campo Motivo, seja na exclusão de item, na interferência ou no cancelamento de cotação, ter a opção "Outros", que ao ser selecionada, exibirá um campo "Descrição" onde o cliente poderá informar o real motivo, tornando mais flexível.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** nos processos de Cancelamento de Cotação e Exclusão de Item de Movimento atualmente não é apresentado o campo Descrição, portanto, será disponibilizado o mesmo para que seja possível informar através de texto o motivo do Cancelamento da Cotação ou Exclusão de Itens de Movimento. Será disponibilizado os campos Código e Descrição de Motivo da Exclusão na aba de Itens de Movimento.

* ## Permitir que o processo de incrementar valor cotado/negociado permita informar valores negativos. O nome desse processo é incoerente, pois normalmente diminuímos o valor cotado/negociado e não aumentamos.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e editar uma cotação para registrar negociação na aba Produtos o Processo "Incrementar Preço Negociado" na Grid acessado através do menu terá o seu nome alterado para "Alterar Preço Negociado" e portanto, terá o seu comportamento alterado para diminuir o valor negociado informando valor ou percentual negativo. 

Ao realizar a edição de uma cotação para registrar Orçamento na aba Produtos o Processo "Incrementar Preço Cotado" na Grid acessado através do menu terá o seu nome alterado para "Alterar Preço Cotado" e portanto, terá o seu comportamento alterado para diminuir o valor cotado informando valor ou percentual negativo.

 

* ## Possibilidade de interferência em todos os itens.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e editar uma cotação para visualizar e/ou Calcular o Quadro Comparativo será alterada a interferência por Produto para que seja possível ser aplicada a todos os produtos. A entrada de menu do processo será realizada no menu existente separando os Processos Por Fornecedor e Por Produto, conforme imagem abaixo.

Será utilizada o processo, conforme figura abaixo,  para a interferência por Produto e Fornecedor, entretanto, a entrada de dados será realizada de acordo com a intenção do Comprador.

### **Interferência por Produto via Quadro Comparativo:**

Para a interferência realizada através de um duplo clique no Quadro comparativo o Fornecedor virá preenchido e não será permitido a edição e a Grid de produtos terá o filtro de acordo com o produto selecionado e não permitira alteração dos campos Código e Descrição do Produto, Unidade Solicitada, Quantidade Solicitada e Preço, exceto pelo campo Qtde a ser Gerada  ou Qtde Efetivada, de acordo com a parametrização, que poderá ser o seu valor preenchido e por fim informar o Motivo e se necessário o Detalhe do Motivo.

**Interferência por Produto via Menu:**

Para a interferência realizada através do menu, conforme imagem acima, o usuário poderá selecionar o Fornecedor e todos os produtos que terão o campo Qtde a ser Gerada ou Qtde Efetivada alterada e por fim informar o Motivo e se necessário o Detalhe do Motivo. Serão alterados os valores dos produtos que estão exibidos na Grid de acordo com o Fornecedor selecionado, portanto, não será possível editar múltiplos produtos para múltiplos fornecedores.

**Interferência por Fornecedor via Menu:**

Para a interferência realizada através do menu, conforme imagem acima, o usuário poderá selecionar o Fornecedor e todos os produtos estarão disponíveis apenas para a visualização e por fim informar o Motivo e se necessário o Detalhe do Motivo.

* ## Permitir incluir uma cotação sem informar condição de pagamento, para que o fornecedor não seja induzido.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação,** no **Assistente de Cotação** existe o passo **Informações** **Gerais** onde são informados os itens que serão impostos aos fornecedores no momento de envio do Pedido de Orçamento. Até a versão 12.1.11 a informação de **Condição de Pagamento** é obrigatório e por padrão vem preenchida com a condição de pagamento utilizada pela última Cotação da coligada logada.

Será criado um parâmetro na Cotação "**Condição de Pagamento obrigatório na Inclusão de Cotação**" que terá como valor default: marcado. Este parâmetro será considerado no Assistente de Inclusão de Cotação e também no serviço de inclusão de cotação ao preencher os valores defaults do Orçamento para manter o comportamento que existe atualmente.

Quando parâmetro **Condição de Pagamento obrigatório na Inclusão de Cotação** estiver desmarcado, será permitido:

* **Assistente de Inclusão de Cotação**: incluir Cotação sem informar condição de pagamento.
* **Incluir Fornecedor na Cotação** sem informar a condição de pagamento.
* **Alteração de Cotação:** a consistência será aplicada quando o parâmetro estiver marcado ou é permitido registrar orçamento e registrar negociação.

A Condição de Pagamento será obrigatório nas rotinas: **Registrar Orçamento** e **Registrar Negociação**.

Outro ponto que será alterado é o momento de carregar os valores defaults da Cotação. Antes estes valores eram carregados no evento Load do Assistente de Inclusão de Cotação e agora serão carregados ao avançar para o passo Informações Gerais. Foi criado um novo método para Carregar os defaults da cotação por Filial.

Na rotina de **Imprimir Quadro Comparativo de Preço**, o Prazo Equalizado sempre foi calculado considerando a Condição de Pagamento do Orçamento. Com esta implementação de ser permitido incluir Cotação sem informar Condição de Pagamento, quando a Condição de Pagamento for Por Item, o Prazo Equalizado será sempre 1. A condição de pagamento sendo por Fornecedor, o Prazo Equalizado será calculado somente se a condição de pagamento estiver preenchida no orçamento.

**Condição de Pagamento Default**

Quando o parâmetro da Cotação **Buscar Cond. Pagto do Cli/For** estiver marcado, será considerado a Condição de Pagamento de Compra definida no cadastro Condições de Pagamento Defaults para Cliente/Fornecedor (anexo do cadastro de Cliente/Fornecedor). Caso não seja encontrado a condição de pagamento default e a condição de pagamento da cotação for vazia/nula, o sistema irá considerar como valor default para condição de pagamento do Orçamento a Condição de Pagamento utilizada para a última cotação com condição de pagamento informada.

Na alteração da Cotação caso a condição de pagamento esteja vazia/nula, será considerado como valor default a condição de pagamento informada no primeiro registro de Orçamento.

Quando a Cotação utilizar Condição de Pagamento por Item, caso a condição de pagamento esteja vazia/nula, será considerado como valor default a condição de pagamento do Item de Orçamento. Se não encontrar nos Itens de Orçamento será carregado como default a primeira condição de pagamento do Item de Orçamento.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
