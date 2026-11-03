---
content_hash: 2c446cfac8016910fea3ab583e8165a44b2fdd1a5e129f6354184d3850a0bc96
fetched_at: '2026-06-29T00:06:20.282632+00:00'
page_id: '221551222'
product: rm
source: tdn-rm
title: ER_Importar_Cotacoes_via_Planilha_Excel
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Importar_Cotacoes_via_Planilha_Excel
version: 175
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_CP\_MOV009 | **IRM1** | PCREQ-8866 |
| **Requisito1** | PCREQ-8867 | **Subtarefa1** | PDR\_CP\_MOV009-34 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.11 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Não se aplica. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Criar planilha de Pedido de Orçamento que será enviada para os fornecedores escolhidos na cotação para preenchimento das informações de orçamento ou negociação. Após preenchida e devolvida pelos fornecedores, a planilha será importada no módulo de cotação para registro dos orçamentos ou negociações e continuidade do processo.

Definição da Regra de Negócio

* **Envio da Planilha de Pedido do Orçamento**

No **TOTVS Gestão de Estoque, Compras e Faturamento | Compras | Cotação**ao utilizar o processo **Comunicar Fornecedores**, na tela de  **Seleção dos Principais Parâmetros**, deverá ser utilizado o **Tipo de Comunicação | Enviar orçamento via e-mail** (protótipo 01).

Ao selecionar este tipo de envio, o usuário poderá informar qual relatório ele deseja utilizar para o envio do e-mail. Sendo obrigatório ele selecionar algum relatório ou planilha. Haverá uma validação para que ele escolha ao menos um, podendo escolher os dois.

Haverá um campo **Planilha de Orçamento**, que poderá ser informado ou não. Caso o usuário informe um modelo de planilha neste campo, ele também deverá informar qual o tipo de exportação deverá ser feito (orçamento ou negociação). Sendo assim o sistema irá realizar a exportação dos pedidos de orçamento ou negociação e enviará uma planilha com essas informações no anexo do e-mail.

A exportação obedecerá a regra existente no momento da comunicação com fornecedores.

Haverá uma validação que não permitirá o envio de negociação sem antes haver um registro de orçamento.

Um modelo de planilha com as configurações padrões, será disponibilizado através do **Planilha Net**. Os clientes poderão, a partir da planilha modelo padrão, customizar a planilha da forma que desejar, desde que sigam as orientações contidas no .

Os campos exibidos na planilha sofrerão alteração conforme a parametrização do sistema. Sendo assim, campos serão ocultos e/ou exibidos em diferentes abas.

No momento em que o processo for executado, o sistema irá preencher a planilha com os dados relacionados a orçamento ou negociação e fazer o envio da mesma no anexo do e-mail para cada fornecedor.

---

## Planilha de Pedido de Orçamento/Negociação

Será utilizado o **Planilha Net** para criar a planilha de pedido de orçamento. De acordo com a consulta associada, os campos poderão ser de orçamento ou de negociação (protótipo 02) e deverão constar os seguintes dados:

* **Dados do Pedido**

 Todos os campos referentes aos dados do pedido serão bloqueados, não sendo possível sua alteração pelo fornecedor.

- Nome da Empresa

- CNPJ da Empresa

- Endereço da Empresa

- Código da Cotação

- Data do Pedido

- Data Limite de Resposta

- Comprador

* **Dados do Fornecedor**

 Todos os campos referentes aos dados do fornecedor serão bloqueados, não sendo possível sua alteração pelo fornecedor.

- Fornecedor: concatenar o código do fornecedor e o nome

- CNPJ do Fornecedor

- Contato do Fornecedor

- Telefone do Contato do Fornecedor

- E-mail do Contato do Fornecedor

**Planilha de Orçamento**

* **Dados do Orçamento**

- ICMS/ISS (%): será exibido conforme parâmetro. Esse dado pode ser omitido pelo fornecedor.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usa Tributo no Orçamento (ICMS/ISS)**

- ICMSST (%): esse dado pode ser omitido pelo fornecedor.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usa Tributo no Orçamento (ICMS/ISS)**

- Número Doc. Fornecedor: esse dado pode ser omitido pelo fornecedor.

- Moeda: será exibido conforme parâmetro. O campo terá o valor da moeda padrão do sistema, sendo possível a alteração dessa pelo fornecedor.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Moeda**

- Condição de Pagamento: será exibido conforme parâmetro.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Condição de Pagamento**

- Frete: se o parâmetro estiver marcado, será por valor, caso não esteja, será por %. Esse dado pode ser omitido pelo fornecedor.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar Valor do Frete**

- Tipo de Frete: esse dado pode ser omitido pelo fornecedor.

- Transportadora: esse dado pode ser omitido pelo fornecedor.

- Desconto: pode ser valor ou porcentagem, de acordo com a parametrização. Esse dado pode ser omitido pelo fornecedor.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa desconto no orçamento**

- Despesa: por valor. Esse dado pode ser omitido pelo fornecedor

- Prazo Validade (dias): esse dado pode ser omitido pelo fornecedor.

- Prazo de Entrega (dias): exibirá a quantidade de dias entre a Data Limite de Entrega definida na cotação e a data de criação da cotação, sendo possível a alteração dessa pelo fornecedor.

* **Dados do(s) Item(ns)**

- Id. Solicitação: campo bloqueado e não editável.

- Coligada Movimento: campo bloqueado e não editável.

- Sequencial do Item: campo bloqueado e não editável.

- Produto: campo bloqueado e não editável.

- Descrição do Produto: campo bloqueado e não editável.

- Unidade Solicitada: campo bloqueado e não editável.

- Unidade Orçada: esse campo será exibido caso o parâmetro esteja marcado. Será permitido informar somente unidades cadastradas no sistema e que sejam compatíveis com a unidade que foi solicitada.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | **Definições Gerais 2/4** | Permite alterar unidade de cotação.**

- Quantidade Solicitada: campo bloqueado e não editável. Caso o fornecedor altere a Unidade Orçada, no momento da importação, a conversão de unidade será realizada e a quantidade será atualizada.

- Condição de Pagamento: se a parametrização estiver por item, será possível informar mais de uma condição de pagamento para o item. Para isso, haverá uma aba para que estes dados sejam informados. Nesta aba haverá uma lista suspensa na coluna Identificador do Produto, para que o usuário selecione o produto que deseja informar a condição de pagamento. Ele poderá repetir essa operação até esgotar as condições de pagamento. Na coluna de Condição de Pagamento, também haverá uma lista suspensa contendo as condições de pagamento disponíveis. Protótipo abaixo:

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Condição de Pagamento**

- Preço Unitário: esse dado pode ser omitido pelo fornecedor desde que seja preenchido o Valor Total.

- Valor Total: esse dado pode ser omitido pelo fornecedor desde que seja preenchido o Preço Unitário. Se o parâmetro estiver desmarcado, ele não será exibido. Quando o parâmetro citado no item "Unidade Orçada" estiver habilitado, este campo será ocultado, pois a planilha Excel não consegue realizar a conversão e alterar o valor total do item. Essa conversão será realizada no momento da importação da planilha.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 |****Usar preço total no item**

- Moeda: será exibido conforme parâmetro. O campo terá o valor da moeda padrão do sistema, sendo possível a alteração da mesma pelo fornecedor.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Moeda**

- IPI (%): esse dado pode ser omitido pelo fornecedor. Se o parâmetro estiver desmarcado, ele não será exibido. Este campo será preenchido com a informação que está na base de dados.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar Tributo no Item de Orçamento (IPI)**

- ICMS (%): esse dado pode ser omitido pelo fornecedor. Se o parâmetro estiver desmarcado, ele não será exibido. Este campo será preenchido com a informação que está na base de dados.

Parâmetro: ****Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar ICMS no Item de Orçamento****

- ICMSST (%): esse dado pode ser omitido pelo fornecedor. Se o parâmetro estiver desmarcado, ele não será exibido. 

Parâmetro: ****Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar ICMS no Item de Orçamento****

- Margem de Lucro ICMSST: esse dado pode ser omitido pelo fornecedor. Se o parâmetro estiver desmarcado, ele não será exibido. 

Parâmetro: ****Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar ICMS no Item de Orçamento****

- Desconto: Pode ser valor ou porcentagem, de acordo com a parametrização.  Esse dado pode ser omitido pelo fornecedor

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa desconto no item de orçamento**

- Despesa: Pode ser valor ou porcentagem, de acordo com a parametrização. Se o parâmetro estiver desmarcado, ele não será exibido. Esse dado pode ser omitido pelo fornecedor

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 2/2 | Usa despesa no item de orçamento**

- Data Entrega: este campo exibirá a data de entrega do item de acordo com a Data de Entrega informada na solicitação de compras, sendo permitida a alteração pelo fornecedor.

- Observação: Será carregada as informações que estão no item da cotação. Campo para preenchimento de dados adicionais sobre o orçamento do item.

**Planilha de Negociação**

* **Dados do Orçamento**

Além dos dados já exibidos na planilha de orçamento, será exibido o seguinte dado:

- Desconto Negociado: Pode ser valor ou porcentagem, de acordo com a parametrização.  Esse dado pode ser omitido pelo fornecedor

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa desconto no orçamento**

* **Dados do(s) Item(ns)**

Além dos dados já exibidos na planilha de orçamento, serão exibidos os seguintes dados:

- Unidade Negociada: esse dado pode ser omitido pelo fornecedor. Este campo será exibido caso o parâmetro esteja marcado. Será permitido informar somente unidades cadastradas no sistema e que sejam compatíveis com a unidade que foi solicitada.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | **Definições Gerais 2/4** | Permite alterar unidade de cotação.**

- Quantidade Orçada: campo bloqueado e não editável.

- Quantidade Negociada: campo bloqueado e não editável. Caso o fornecedor altere a Unidade Negociada, no momento da importação, a conversão de unidade será realizada e o valor da quantidade atualizado

- Condição de Pagamento Negociada: esse dado pode ser omitido pelo fornecedor. A aba de Condições de Pagamento por Item não é exibida, pois não é permitido informar mais que uma condição de pagamento, este comportamento já existe atualmente no sistema.

- Preço Unitário Negociado: esse dado pode ser omitido pelo fornecedor.

- Valor Total Negociado: esse dado pode ser omitido pelo fornecedor. Se o parâmetro estiver desmarcado, ele não será exibido. Quando o parâmetro citado no item "Unidade Negociada" estiver habilitado, este campo será ocultado, pois a planilha Excel não consegue realizar a conversão e alterar o valor total do item. Essa conversão será realizada no momento da importação da planilha.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar preço total no item**

- Desconto Negociado: pode ser valor ou porcentagem, de acordo com a parametrização. Esse dado pode ser omitido pelo fornecedor.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa desconto no item de orçamento**

- Despesa Negociada: pode ser valor ou porcentagem, de acordo com a parametrização. Se o parâmetro estiver desmarcado, ele não será exibido. Esse dado pode ser omitido pelo fornecedor.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa despesa no item de orçamento**

- Observação: campo para preenchimento de dados adicionais sobre a negociação do item. Estará preenchido com a observação inserida na cotação.

**Observações Gerais**

- Os dados sublinhados sempre devem existir na planilha pois são campos chaves para o processo de importação de preços orçados.

- Os demais campos são opcionais e podem ser estruturados conforme a necessidade do cliente.

- O cliente poderá incluir outros campos conforme a sua necessidade.

- O sistema irá obedecer a parametrização de item agrupado.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Movimentos 1/2 | Não agrupar itens iguais na cotação**

- Quando o sistema estiver parametrizado para cotar apenas produtos fornecidos pelos fornecedores e/ou utilizar qualificação de fornecedores, os produtos da cotação serão filtrados para cada cliente, obedecendo as regras que hoje já existem no sistema.

Parâmetro: **Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Somente Cotar Produtos Fornecidos**

Parâmetro:****Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 3/4 | Utiliza Fornecedores Qualificados****

- Todos os campos da planilha de orçamento ou negociação terão valores defaults de acordo com que existe hoje no sistema.

* **Lista Suspensa**

Os seguintes dados serão exibidos como lista suspensa, visando facilitar a inclusão da informação e evitando possíveis erros.

- Transportadora

- Moeda

- Tipo de Frete

- Condição de Pagamento

- Unidade de Medida

---

* **Importação da Planilha de Pedido de Orçamento**

- Será adicionado um novo processo para **Importar Planilha de Orçamento/Negociação** na tela de visão das cotações.

- O sistema utilizará o Conceito para leitura da planilha. O conceito padrão disponibilizado já estará com as ligações padrões prontas e caso o usuário customize sua planilha, ele terá que editar o conceito e realizar a ligação dos novos campos.

- Na execução do processo de importação, o usuário deverá informar o conceito de importação e o caminho do arquivo ou da pasta em que se encontram as planilhas das cotações ou negociações dos fornecedores.

- O processo filtrará os conceitos pelo nome do sistema, apresentando apenas os conceitos com o nome RM NUCLEUS e TODOS.

- O processo irá carregar como default, o ultimo caminho informado na tela do processo.

- Durante a execução do processo o sistema irá percorrer todas as planilhas, importando as cotações uma a uma.

- Será possível também agendar jobs para executar o processo de importação de cotação e/ou negociação de forma automatizada.

- No final do processo, será exibido um log referente às planilhas que foram importadas com sucesso e quais tiveram erro(s), caso haja. Além disso as planilhas processadas serão renomeadas com o Id do Job executado visando a identificação do job que processou a(s) planilha(s) e também impedindo que na próxima execução do processo esse arquivo seja processado novamente.

- A correta edição das informações sobre o orçamento são de responsabilidade do Fornecedor e caso informações desnecessárias ou desencontradas sejam preenchidas, poderá ocasionar erros na importação da planilha.

- Data Recebimento (TCORCAMENTO.DATAENTREGA)

- Este campo será preenchido com a data atual do servidor no momento da execução do processo de importação.

- Data Entrega (TCORCAMENTO.VALPRAZOENTREGA)

- Este campo será preenchido com a informação da planilha (PRAZO ENTREGA (DIAS)), e o sistema faz o calculo da data de entrega a partir da data da cotação(TCCOTACAO.DATENTREGA) somada ao prazo de entrega.

- Alteração da Unidade Orçada/Negociada: 

- Caso a empresa permita a alteração da unidade dos produtos orçados / negociados, não será possível que o fornecedor altere a quantidade Orçada/Negociada na planilha. O recalculo da quantidade é realizado pelo processo de importação de acordo com a unidade Orçada/Negociada informado na planilha.

- Status do Item Cotado:

O processo de importação irá alterar o status da cotação para cotado durante a impotação da planilha caso o campo Valor Cotado tenha sido preenchido.

- Agrupamento de itens iguais:

- Caso a empresa utilize o agrupamento de itens iguais na cotação o processo de importação irá identificar os itens agrupados e replicar os valores de orçamento/Negociação para todos os itens. O mesmo acontece para as condições de pagamento por item informados na aba COND\_PAGTO\_ITENS.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Gestão de Estoque, Compras e Faturamento | [Alteração] | [BackOffice -> Gestão de Estoque, Compras e Faturamento -> Ambiente -> Parâmetros -> Gestão de Estoque, Compras e Faturamento -> Gestão Compras -> Cotação] | - |

***Tabelas Utilizadas***

* TCCOTACAO
* TCITMORCAMENTO
* TCITMORCAMENTOGRP
* TCORCAMENTO

Na importação, os campos de preço unitário e valor total do item deverão respeitar a parametrização da cotação, pois se o valor total não estiver sendo utilizado, deverá ser preenchido o preço unitário, caso contrário deverá ser preenchido o valor total.

VALPRAZOENTREGA

## Protótipo de Tela

**Protótipo 01**

Na área do **Tipo de Comunicação**, ao selecionar **Imprimir orçamento ou Exportar orçamento para web,**a área **Planilha de Orçamento** deverá ser ocultada, sendo exibida apenas na seleção da opção **Enviar orçamento via e-mail****.**

Nessa opção, se o usuário selecionar alguma **Planilha de Orçamento**, essa será criada, por fornecedor, e enviada no anexo do e-mail. Haverá uma validação para que um relatório ou planilha seja informado.

**Protótipo 02**

Dados da Cotação

Orçamento

Itens de Orçamento/Negociação

A estrutura será a mesma para ambos os casos. O que mudará são os cabeçalhos das colunas.

**Protótipo 03**

Na tela de Cotação será criado um Processo para realizar a importação de Orçamentos

Na execução do processo o conceito de importação será selecionado e o diretório onde a planilha está será informado.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
