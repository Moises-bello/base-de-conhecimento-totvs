---
content_hash: 1fd0b9c3022c99209f6ce7ad1408003e08443bae6fd8fdef3e5b6dccc364fdf7
fetched_at: '2026-06-29T00:05:58.235353+00:00'
page_id: '185744050'
product: rm
source: tdn-rm
title: Como Fazer - Movimentação via Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185744050
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Totvs Gestão de Estoque, Compras e Faturamento                       **Versão:***a partir 11.40* |
| **Processo** | **:** | Compras |
| **Subprocesso** | **:** | Parametrizar o tipo de movimento para inclusão via portal |
| **Data da publicação** | **:** | 16/03/2015 |

A finalidade deste documento é auxiliar na parametrização de tipos de movimentos para utilizarem o Portal.

***Parametrizações Necessárias***

Para configurar os tipos de movimentos de Solicitação de Compras e Pedido de Venda para serem utilizados no Portal, terá quer ser feito as seguintes parametrizações abaixo:

* Acessar a etapa Mov- Identificação no campo “Edita Numeração” deverá selecionar a opção “Mostra”
* Acessar a etapa Mov- Emitente/ Destinatário 1/2 o campo “Edição da Filial de Emissão” deverá selecionar a opção “Edita”
* Acessar a etapa Mov- Emitente/ Destinatário 2/2 o campo “Edição do Local de Saída” deverá selecionar a opção “Não Edita”
* Acessar a etapa Mov- Outros Dados e marcar o Flag “Pedido Integrado ao RMNucleus.Net”

Para utilização de movimentos que utilizam o portal é necessário que os Tipos de Movimentos sejam parametrizados como “Solicitação de Compra” ou “Pedido de Venda” esta configuração deverá ser realizada na etapa Compra/Venda – Outros Dados no campo “Tipo de Movimento de Compra” Deverá selecionar (“Pedido de Compra” para tipos de movimento 2.1.xx e “Solicitação de Compra” para tipos de movimento 1.1.xx).  
*Observações:*  
- Ao marcar o parâmetro “Pedido Integrado ao RMNucleus.Net”, o sistema irá fazer uma consistência dos campos que não poderão ser utilizados no portal.

Através do Portal RM, não é possível utilizar alguns módulos como: Contabilidade, Estoque, Financeiro, Tributos, Rateios. Ou seja, não há como emitir solicitações de compra ou venda com estes módulos parametrizados.  
- Ao incluir movimentos pelo Portal RM nem todos os campos estarão disponíveis neste módulo. Os campos disponíveis para esses tipos de movimento são:

**Movimento**  
*Pasta Identificação*  
- Identificador  
- Status  
- Tipo Movimento  
- Código Filial  
- Data Emissão  
- Data Saída  
- Série  
- Número Movimento  
- Local de Estoque  
- Código Filial Local de Estoque  
- Cliente \ Fornecedor  
- Código da Filial de Destino  
- Moeda  
- Condição de Pagamento  
- Vendedor 1  
- Valor Líquido  
*Pasta Cabeçalho*  
- Número no Cliente  
- 2º Número  
- Data Extra 1  
- Data Extra 2  
- Data Retorno  
- Data Entrega  
- Prazo Entrega  
- Percentual Frete  
- Valor Frete  
- Percentual Desconto  
- Valor Desconto  
- Percentual Despesa  
- Valor Despesa  
- Percentual Seguro  
- Valor Seguro  
- Percentual Extra 1  
- Valor Extra 1  
- Percentual Extra 2  
- Valor Extra 2  
- Pasta Tabelas  
- Centro de Custo  
- Departamento  
- Tabela de Classificação 1  
- Tabela de Classificação 2  
- Tabela de Classificação 3  
- Tabela de Classificação 4  
- Tabela de Classificação 5  
- Representante  
- Comissão  
*Pasta Transportadora*  
- Transportadora  
- Transportadora 2  
- Peso Bruto   
- Peso Líquido  
- Frete CIF ou FOB  
- Pasta Observações  
- Observação  
- Campo Livre 1  
- Campo Livre 2  
- Campo Livre 3  
- Histórico Curto  
- Histórico Longo  
*Pasta Campos Complementares*  
- Todos os campos complementares existentes e parametrizados para o tipo de movimento  
**Item de Movimento***Pasta Identificação*  
- Número Seqüencial  
- Produto  
- Centro de Custo  
- Unidade  
- Quantidade  
- Seleção de Preço  
- Preço Unitário   
- Valor Total Item  
- Percentual Desconto  
- Valor Desconto  
- Percentual Despesa  
- Valor Despesa  
- Data Orçamento  
- Valor Unitário do Orçamento  
- Natureza Orçamento  
- Campo Livre  
- Data Entrega  
- Funcionário 2  
*Pasta Tabelas*  
- Departamento  
- Tabela Classificação 1  
- Tabela Classificação 2  
- Tabela Classificação 3  
- Tabela Classificação 4  
- Tabela Classificação 5  
- Tabela Classificação 1 (Tabelas do Faturamento)  
- Tabela Classificação 2 (Tabelas do Faturamento)  
- Tabela Classificação 3 (Tabelas do Faturamento)  
- Tabela Classificação 4 (Tabelas do Faturamento)  
- Tabela Classificação 5 (Tabelas do Faturamento)  
- Representante  
- Comissão

*Pasta Histórico*

- Histórico Curto  
- Histórico Longo  
*Pasta Campos Complementares*  
- Todos os campos complementares existentes e parametrizados para o tipo de movimento  
**Integração**  
- Projetos  
- Work FLow

***Descrição do Processo***

**Dados da Inclusão**

Acessar o link do portal e preencher os campos “Login” e “Senha” do usuário e “Alias” de conexão a Base de Dados que esta configurada, conforme tela abaixo:

Posteriormente será apresentada a seguinte tela abaixo onde possui as opções relativas ao modo “Administrativo”:

Para inclusão de movimento entrada deverá escolher a opção “Solicitação de Compra”, para inclusão de movimento de saída deverá escolher a opção “Pedido de Venda”, escolher a Filial e Tipo de Movimento que deseja fazer a inclusão e clicar em “OK”

Será apresentada a tela abaixo onde deverá clicar em “Novo”

Será aberta uma nova tela para que sejam preenchidos os dados do movimento:

Depois de Preenchido os dados do movimento, do lado esquerdo clicar na opção “Item de Movimento” posteriormente clicar em “Novo” para que seja incluso os itens do movimento.

Será aberta a seguinte tela abaixo, após preencher todos os dados de todos os itens deverá clicar na opção “Salvar e Fechar” o sistema retornar para a tela principal onde deverá ser feito o mesmo.:

***Informações Adicionais***

- Após salvar o movimento no portal o mesmo será incluso diretamente na base de dados sem a necessidade de realizar nenhum outro procedimento.

- Caso envolva integração com outros aplicativos é necessário que seja descrito informação de ambos.
