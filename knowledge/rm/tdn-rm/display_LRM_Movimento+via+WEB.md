---
content_hash: 1d4a972640314813726654d8f5290499b25d6cbbbe89a71c630323520d336d66
fetched_at: '2026-06-29T00:09:24.111303+00:00'
page_id: '423937895'
product: rm
source: tdn-rm
title: Movimento via WEB
type: documentation
url: https://tdn.totvs.com/display/LRM/Movimento+via+WEB
version: 2
---

Para configurar os tipos de movimentos de solicitação de compras e pedido de venda para serem utilizados no Portal, basta habilitar o parâmetro "Pedido Integrado ao RM Nucleus.Net" na etapa Outros Dados do Movimento.   
Para que o tipo de movimento fique correto, a Filial Emitente deve estar parametrizada como "Edita" e a numeração do movimento deve estar como "Mostra", o local de saída não deve ser editado e o movimento deve ser parametrizado como solicitação de compras ou pedido de venda.

***Observações***:

* Através do Portal RM, não é possível utilizar alguns módulos como: contabilidade, estoque, financeiro, tributos, rateios. Ou seja, não há como emitir solicitações de compra ou venda com estes módulos parametrizados.
* Ao incluir movimentos pelo Portal RM nem todos os campos estarão disponíveis neste módulo. Os campos disponíveis para esses tipos de movimento são:

**Movimento Pasta Identificação**

* Identificador
* Status
* Tipo Movimento
* Código Filial
* Data Emissão
* Data Saída
* Série
* Número Movimento
* Local de Estoque
* Código Filial Local de Estoque
* Cliente \ Fornecedor
* Código da Filial de Destino
* Moeda
* Condição de Pagamento
* Vendedor 1
* Valor Líquido

**Pasta Cabeçalho**

* Número no Cliente
* 2º Número
* Data Extra 1
* Data Extra 2
* Data Retorno
* Data Entrega
* Prazo Entrega
* Percentual Frete
* Valor Frete
* Percentual Desconto
* Valor Desconto
* Percentual Despesa
* Valor Despesa
* Percentual Seguro
* Valor Seguro
* Percentual Extra 1
* Valor Extra 1
* Percentual Extra 2
* Valor Extra 2
* Pasta Tabelas
* Centro de Custo
* Departamento
* Tabela de Classificação 1
* Tabela de Classificação 2
* Tabela de Classificação 3
* Tabela de Classificação 4
* Tabela de Classificação 5
* Representante
* Comissão

**Pasta Transportadora**

* Transportadora
* Transportadora 2
* Peso Bruto
* Peso Líquido
* Frete CIF ou FOB

**Pasta Observações**

* Observação
* Campo Livre 1
* Campo Livre 2
* Campo Livre 3
* Histórico Curto
* Histórico Longo

**Pasta Campos Complementares**  
Todos os campos complementares existentes e parametrizados para o tipo de movimento Item de Movimento Pasta Identificação

* Número Sequencial
* Produto
* Centro de Custo
* Unidade
* Quantidade
* Seleção de Preço
* Preço Unitário
* Valor Total Item
* Percentual Desconto
* Valor Desconto
* Percentual Despesa
* Valor Despesa
* Data Orçamento
* Valor Unitário do Orçamento
* Natureza Orçamento
* Campo Livre
* Data Entrega
* Funcionário 2

**Pasta Tabelas**

* Departamento
* Tabela Classificação 1
* Tabela Classificação 2
* Tabela Classificação 3
* Tabela Classificação 4
* Tabela Classificação 5
* Tabela Classificação 1 (Tabelas do Faturamento)
* Tabela Classificação 2 (Tabelas do Faturamento)
* Tabela Classificação 3 (Tabelas do Faturamento)
* Tabela Classificação 4 (Tabelas do Faturamento)
* Tabela Classificação 5 (Tabelas do Faturamento)
* Representante
* Comissão
* Pasta Histórico
* Histórico Curto
* Histórico Longo

**Pasta Campos Complementares**  
Todos os campos complementares existentes e parametrizados para o tipo de movimento

* Integração
* Projetos
* Work FLow

Abaixo seguem as regras para exibição de cliente/fornecedor no Pedido de Venda Web.  
Se o usuário logado estiver associado a algum Representante serão exibidos somente os clientes/fornecedores que tem algum representante associado.  
Se na parametrização do tipo de movimento o emitente/destinatário for igual a fornecedor serão exibidos somente os registros do tipo fornecedor.  
Se na parametrização do tipo de movimento o emitente/destinatário for igual a empresa serão exibidos os somente os registros do tipo cliente.
