---
content_hash: 7a7ddff770030e5ed75a90c3b4a71c38f67cdbd0b23fb12632519693ddf49f9f
fetched_at: '2026-06-29T00:09:58.358087+00:00'
page_id: '452690612'
product: rm
source: tdn-rm
title: Faturamento Direto
type: documentation
url: https://tdn.totvs.com/display/LRM/Faturamento+Direto
version: 87
---

## Objetivo

O Faturamento Direto tem como objetivo realizar um melhor controle, gerando maior confiabilidade e segurança no processo de inclusão de pedidos para Suprimento/Faturamento.

Essa funcionalidade está disponível também no formato web através do , podendo ser facilmente acessado de qualquer dispositivo conectado a internet.

Importante:

Se sua empresa utiliza o [BackOffice Protheus](https://tdn.totvs.com/display/INT/3+-+PROCESSOS), saiba que o recurso de Faturamento Direto está disponível apenas para contratos de pagamento relacionados a serviços, marco contratual ou insumo.

### Passos:

1 - Realizar parametrização para utilização do processo aba (Parâmetros);

2 - Criação de ao menos um cadastro de Tipo de Detalhamento da Retenção, Dedução e Adiantamento, onde o tipo definido é Faturamento Direto. O cadastro deve ser feito no menu Controle > Contrato > Tipo de Detalhamento da Retenção, Dedução e Adiantamento;

3 - Criação do Pedido de Faturamento Direto aba (Gerar Pedido de Faturamento Direto);

4 - Realizar dedução / medição e liberação do período.

### Procedimentos:

1Limite de Faturamento Direto

**Limite de Faturamento Direto**

Os limites de Faturamento Direto são incluídos no anexo do contrato. Para acessá-lo, selecione o Contrato | Anexos | Limite de Faturamento Direto.

Os limites são definidos pelo processo dentro do anexo e podem ser definidos por Valor e Por Percentual, podendo ser aplicado sobre o Contrato ou sobre os Itens do Contrato.

Quando o item ou contrato não podem ter faturamento direto?

O limite de faturamento direto cadastrado com o valor ou percentual igual a zero define que o item ou contrato não podem ter faturamento direto

**Validação Limite de Faturamento Direto:**

Se Contrato

* O valor ou percentual a grandeza do limite deve ser informada
* O valor do contrato tem que ser maior que zero
* Se valor, o valor do contrato tem que ser maior que o valor do limite
* Se percentual, o percentual não pode ser maior que 100%

Se Itens

* O valor ou percentual a grandeza do limite do item selecionado deve ser informada
* Se percentual, o percentual do item não pode ser maior que 100%
* Se valor, o valor contratado do item tem que ser maior que o valor do limite
* Se valor, o valor do limite não pode ser menor que o total de faturamento direto

**Associação de Itens/Aditivo**

* Valida apenas para itens alterados
* Se valor, o valor total contratado do item não pode ser menor que o valor do limite criado
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor total contratado do item não pode ser menor que o total de valor do faturamento direto existente para o item (tarefa).

**Cálculo do Contrato**

Se o limite for do tipo Contrato

* Se valor, o valor do contrato não pode ser menor que o valor do limite
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor do contrato não pode ser menor que o total de valor   
  do faturamento direto

**Liberação de Período/Liberação para Suprimentos/Faturamentos**

Se o limite for do tipo Contrato

* Se valor, o valor total de faturamento direto não pode ser maior que valor do limite
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor do contrato não pode ser menor que o total de valor do faturamento direto

Se o limite for do tipo Itens

* Se valor, o valor total de faturamento direto do item (tarefa) não pode ser maior que valor do limite  do item
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor contratado do item não pode ser menor que o total de valor do faturamento direto do item

**Associação de Dedução de Faturamento Direto**

* Se existir limite com valor ou percentual 0, não deve permitir a associação

**Cadastro de Pedido de Faturamento Direto**

* Se existir limite com valor ou percentual 0 tanto para o item quanto para o contrato, não deve permitir a inclusão/alteração do item

Se o limite for do tipo Contrato

* Se limite valor, o total de limite de faturamento direto + (quantidade pedida \* preço orçado) não pode ser maior que o valor do limite
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor do contrato não pode ser menor que o total de valor do faturamento direto + (quantidade pedida \* preço orçado)

Se o limite for do tipo Itens

* Se limite valor, o total de limite de faturamento direto + (quantidade pedida \* preço orçado) não pode ser maior que o valor do limite do item
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor contratado do item não pode ser menor que o total de valor do faturamento direto do item + (quantidade pedida \* preço orçado)

**Gerar Pedido de Faturamento Direto**

* Valida se os parâmetros Usa Dedução de Contrato e Editar Contrato no Item estão definidos para o tipo de movimento
* Se existir limite com valor ou percentual 0 tanto para o item quanto para o contrato, não deve permitir a geração do pedido

Se o limite for do tipo Contrato

* Se limite valor, o total de limite de faturamento direto considerando a tentativa de geração não pode ser maior que o valor do limite
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor do contrato não pode ser menor que o total de valor do faturamento direto considerando a tentativa de geração

Se o limite for do tipo Itens

* Se limite valor, o total de limite de faturamento direto do item considerando a tentativa de geração do item não pode ser maior que o valor do limite
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor contratado não pode ser menor que o total de valor do faturamento direto do item considerando a tentativa de geração do item

**Gerar movimento para o Sup/Fat do Pedido de Faturamento Direto**

* Caso o ambiente não seja integrado com o Protheus, valida se os parâmetros Usa Dedução de Contrato e Editar Contrato no Item estão definidos para o tipo de movimento.
* Se existir limite com valor ou percentual 0 tanto para o item quanto para o contrato, não deve permitir a geração do pedido

Se o limite for do tipo Contrato

* Se limite valor, o total de limite de faturamento direto considerando a tentativa de geração não pode ser maior que o valor do limite
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor do contrato não pode ser menor que o total de valor do faturamento direto considerando a tentativa de geração

Se o limite for do tipo Itens

* Se limite valor, o total de limite de faturamento direto do item considerando a tentativa de geração do item não pode ser maior que o valor do limite
* Se percentual, valor do limite calculado a partir do percentual em relação ao valor contratado não pode ser menor que o total de valor do faturamento direto do item considerando a tentativa de geração do item

Observação

Para que as rotinas de faturamento direto possam ser executadas, é necessário que exista ao menos um registo no cadastro de Tipo de Detalhamento da Retenção, Dedução e Adiantamento, onde o tipo definido é Faturamento Direto"

1Gerar Pedido de Material de Faturamento DiretoGerar Pedido de Material de Faturamento Direto

**Gerar de Pedido de Material Faturamento Direto**

Os pedidos de faturamento direto poderão ser incluir a partir do processo "Gerar Pedido de Material Faturamento Direto". Para acessá-lo, selecione o Contrato | Processos| Faturamento Direto | Pedido de Material Faturamento Direto.

Os pedidos de Faturamento Direto estão disponíveis para os contratos de finalidade: Serviços, Insumos e Extra-Histograma.

**Rateio por tarefas:** Através do botão "Inclui rateio de tarefa(s) para os item(ns) selecionado(s).", é possível informar várias tarefas para o mesmo produto, e após esta seleção, pode-se informar a quantidade/percentual do produto para cada tarefa.

**Observação.:** A partir do anexo | Faturamento Direto | Pedido de Material Faturamento Direto poderá ser consultado os pedidos gerados e também poderá ser incluído um pedido manualmente.

[Entendendo o Faturamento Direto](https://tdn.totvs.com/pages/viewpage.action?pageId=544705534)

3AnexosAnexos de Faturamento Direto

[Dedução de produto faturado](http://tdn.totvs.com/pages/viewpage.action?pageId=421385082)

2ParâmetrosParâmetros de Projeto

Para utilização do faturamento direto é necessário realizar a configuração do tipo de movimento que será utilizado nos contratos a Receber e a Pagar.

Para configurar os tipos de movimentos, acesse Projeto | Parâmetros | Construção e Projetos | Projetos (F6) | Integração | Suprimento/Faturamento | Tipos de Mov. de Contratos, nesta etapa deve informar nos campos "Tipo do movimento para contratos a pagar" e "Tipo do movimento para contratos a Receber" os movimentos utilizados no processo do Faturamento Direto.

Veja um exemplo aqui3AnexosAnexos de Faturamento Direto

**Cliente/Fornecedor para Faturamento Direto**

O anexo de Cliente/Fornecedores é utilizado para cadastrar os clientes/fornecedores que serão permitidos na geração de movimentos do Faturamento Direto.

Para acessar o anexo, selecione o contrato | Anexos | Faturamento Direto | Cliente/Fornecedor para Faturamento Direto.

Veja aqui um exemplo

Validação do anexo de Cliente/Fornecedor para Faturamento Direto:

* Não é possível realizar a inclusão de um Cliente para contratos do tipo a Pagar;

Mensagem apresentada ao tentar incluir um cliente para contrato à pagar

Causa:   
Não é permitido a inclusão de Cliente/Fornecedor com a Classificação igual a "Cliente" em contratos do Tipo "a Pagar".

Solução:   
- Favor selecionar um Cliente/Fornecedor com a Classificação igual a "Fornecedor" ou "Ambos" para o contrato do Tipo "a Pagar".

* Não é possível realizar a inclusão de um Fornecedor para contratos do tipo a Receber;

Mensagem apresentada ao tentar incluir um Fornecedor para contrato à receber

Causa:   
Não é permitido a inclusão de Cliente/Fornecedor com a Classificação igual a "Fornecedor" em contratos do Tipo "a Receber".

Solução:   
- Favor selecionar um Cliente/Fornecedor com a Classificação igual a "Cliente" ou "Ambos" para o contrato do Tipo "a Receber".

**Produtos para Faturamento Direto**

Assim como o anexo do Cliente/Fornecedor, temos o Produtos para Faturamento Direto, que possibilita a definição de produtos para serem usados no faturamento direto, restringindo a seleção de outros produtos pelo usuário. Para definir basta acessar no anexo de contratos a opção Faturamento Direto>Produtos para Faturamento Direto:

Será aberto o respectivo anexo para informar os produtos que deseja permitir ao usuário informar na criação do pedido de faturamento direto, e esse cadastro é por contrato:

**Pedido de Faturamento Direto**

Neste anexo é possível visualizar/editar e incluir Pedidos para o Faturamento Direto através do anexo "Faturamento Direto", disponível no módulo de Contratos:  Para acessá-lo, selecione o contrato | Anexos | Faturamento Direto | Pedido de Material Faturamento Direto.

Veja aqui um exemplo:

Com o anexo aberto, a criação do pedido é realizada através do botão "Incluir (Ctrl + Ins)" do anexo:

Ao clicar no botão para a criação de um Pedido de Material Faturamento Direto, vai ser apresentada a seguinte tela:

Código do pedido

Data da Requisição

Utiliza preço orçado

Tipo de Movimento

Este campo "Tipo de Movimento" traz o tipo de movimento informado nos parâmetros de projeto conforme descrito na aba Parâmetros deste documento. Mas pode ser alterado, caso seja necessário o envio do pedido utilizando um outro Tipo de Movimento diferente do parametrizado no projeto.

Caso não seja definido nos parâmetros de projeto o tipo de movimento , o sistema exibirá mensagem informando que é necessário a realização da configuração.

Cliente/Fornecedor

Será visível apenas os clientes/fornecedores associados no anexo de contrato de "Cliente/Fornecedor para Faturamento Direto".

Caso o contrato não possua cadastro de cliente/fornecedor no anexo "Cliente/Fornecedor para Faturamento Direto" o sistema exibirá todos os clientes/fornecedores existentes no sistema de acordo com a finalidade do contrato (Contrato a receber (Categoria: Cliente e Ambos) e Contrato a pagar (Categoria: Fornecedor e Ambos)).

Condição de Pagamento

Este campo permite informar a condição de pagamento, o mesmo é opcional.

Local de Estoque

Este campo permite informar o local de estoque, o mesmo é opcional.

Veja agora, um exemplo da tela sendo preenchida:

Após salvar o Pedido, é necessário informar os itens do Pedido, através do anexo Item Pedido Material Faturamento Direto:

Neste anexo, para incluir os itens, é necessário clicar no botão "Incluir Novo" e assim, preencher os campos:

Produto, Tarefa, Quantidade Pedida, Data de Entrega e Preço Orçado.

Veja o exemplo do item de um pedido sendo preenchido aqui:3RelatórioRelatorio de Faturamento Direto

Disponibilizamos o objeto gerencial TOPREL0070 para a funcionalidade Faturamento Direto, no Smart View;
