---
content_hash: 909527abf5289ae5d778e6969c245c3e7a69a67848046d364a0002947654738c
fetched_at: '2026-06-29T00:08:26.323779+00:00'
page_id: '271174307'
product: rm
source: tdn-rm
title: DT_Calculo_do_Digito_Verificador_do_Debito_Automático_do_Cliente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271174307
version: 125
---

# Cálculo do Dígito Verificador do Débito Automático do Cliente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Função:** | *Cálculo do Dígito Verificador do Débito Automático do Cliente**.* |
| **Situação/Requisito:** | *Não se aplica.* |
| **Requisito (**ISSUE**):** | *EDUCTB002-436* |

## Descrição

Conforme orientação do manual de retorno de débito automático do CNAB 150 da Febraban se fez necessário a realização da implementação da função *Cálculo do Dígito Verificador do Débito Automático do Cliente**.*

Então esta implementação tem como objetivo:

* Criar um campo para armazenação do dígito verificador de débito automático do cliente;
* Processamento de arquivos de retorno de débito automático contendo linhas do tipo B.
* Atualizar as informações bancárias dos clientes que optarem por pagamento através de débito automático de acordo com os dados enviados pelo banco no para esse tipo de retorno.

O motivo da implementação é facilitar o tratamento de débito automático, sem a necessidade do cadastramento manual dos dados bancários de cada um dos clientes optantes por essa forma de pagamento.

## Procedimento para Configuração

Necessário execução do Atualizador de Base de Dados TOTVS RM na versão 12.1.16 ou superior.

## Procedimento para Utilização

1- Conversão para preenchimento do Dígito verificador:

A execução do Atualizador de Base de Dados TOTVS RM realiza:

* Acréscimo do campo DIGVERIFICDEBAUTOMATICO na tabela FCFO para representar o dígito verificador de débito automático do cliente.
* Cálculo para preenchimento do dígito verificador de todos clientes existentes na base. O campo será preenchido a partir de um cálculo realizado sobre o campo IDCFO (utilizado por ser um campo sequencial e único na tabela conforme orientação do manual do CNAB 150 da Febraban).
* Detalhamento do Cálculo do Dígito Verificador do débito automático do cliente:

Para o cálculo é utilizado a rotina CalculoDV da FinBancoCalculoUtils. Ele é realizado seguindo sempre como base os seguintes dados:

IDCFO: Criado no momento da inclusão do registro (AutoInc);

Módulo: 11;

Pesos: 2,3,4,5;

O dígito verificador para débito automático não pode ser uma dezena, então quando o cálculo retornado for uma dezena, ou seja, for maior que 9, será realizado a soma dos dígitos para transforma-lo em unidade.

Na rotina CalculoDV para o cálculo do dígito verificador com "Modulo 11" as únicas dezenas retornadas serão 10 e 11, então nessa situação a nova rotina para geração do dígito verificador para Débito Automático do cliente fará o seguinte calculo:

Ex.:

**10** = 1+0 = 1;

**11** = 1+1 = 2;

Observação

A ordem dos pesos para o cálculo será 5,4,3,2 e caso o IdCfo contenha mais de 4 dígitos, o peso será repetido sempre acrescentando a esquerda "...**4,3,2**,5,4,3,2".

Exemplos:

**IDCFO**:  2 6 5  
**PESOS**: 4,3,2

**IDCFO**:  5 2 6 5

**PESOS**: 5,4,3,2

**IDCFO**:  2  1  5  2  6  5  
**PESOS**: 3, 2, 5, 4, 3, 2

Cálculo:

* Multiplicação do IDCFO pela inversão do peso:

Ex.:**IDCFO: 346159**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IDCFO | 3 | 4 | 6 | 1 | 5 | 9 | X    = |
| Pesos | 3 | 2 | 5 | 4 | 3 | 2 |
| Resultado | 9 | 8 | 30 | 4 | 15 | 18 |

* Os resultados maiores que 9 deverão ser subtraídos por 9:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 9 | 8 | 30-9 | 4 | 15-9 | 18-9 | = |
| 9 | 8 | 21 | 4 | 6 | 9 |

* Soma dos resultados:   
  9 + 8 + 21 + 4 + 6 + 9 = **57**

* Calcular o mod (% - resto da divisão) da somatória pelo módulo:   
  [Soma] % [Módulo] = 57 % 11 =**2**
* Subtrair o módulo pelo resultado do mod (resto da divisão) do passo anterior:  
  11 - 2 = **9**

Conforme exemplo acima, o dígito verificador do IDCFO: 346159 é **9**

2- Preenchimento do dígito verificador no cadastro de Cliente/Fornecedor:

1. Acessar o Cadastro de Cliente/Fornecedor no TOTVS Gestão Financeira: *BackOffice | Gestão Financeira |**Cadastros | Clientes Fornecedores* .
2. No processo de inclusão de novo registro ao salvar o mesmo será realizado o cálculo do dígito verificador a partir do IDCFO gerado conforme detalhado no item anterior (*Detalhamento do Cálculo do Dígito Verificador do débito automático do cliente*).

O campo dígito verificador não será visível na tela de cadastro de cliente/fornecedor.

3- Arquivo de remessa de débito automático para CNAB 150:

O layout CNAB 150 – padrão Febraban existente no book de relatórios foi evoluído para que no campo identificador do registro E seja enviado o campo ID do Cliente/Fornecedor (FCFO.IDCFO) concatenado com o Dígito verificador do identificador de débito automático (FCFO.DIGVERIFICDEBAUTOMATICO).

1. Acessar o TOTVS Gestão Financeira: *BackOffice | Gestão Financeira.*
2. No menu*Contas a Pagar/Receber | Boleto | Processos | Remessa Débito Automático*realizará a geração do arquivo de remessa.

Layout CNAB150: arquivo FINLAY0005 - Débito Automático CNAB150.TotvsGen

4- Retorno de débito automático (linha do tipo B):

Para o retorno de débito automático já existente no sistema foi implementado uma tratativa para linhas identificadas com registro do tipo B. Para essas linhas o sistema se comporta da seguinte forma:

* Procura o registro referente ao cliente referido no arquivo de retorno na base. Ele será identificado pelo identificador (IDCFO) e o dígito verificador. Caso não seja encontrado nenhum registro, um erro será retornado no log do processo de retorno, informando que o cliente não foi encontrado.
* Se o código do movimento enviado no arquivo de retorno for 2 (inclusão do optante pelo débito automático):
  + Será cadastrado um novo registro de dados bancários para o cliente (FDADOSPGTO) com a forma de pagamento “Débito Automático”. Os campos banco, agência e conta corrente serão preenchidos com as informações retornadas no arquivo.
  + O dado bancário cadastrado é definido como default para o respectivo cliente.

* Se o código do movimento enviado no arquivo de retorno for 1 (exclusão de optante pelo débito automático):
  + Verificado se o cliente possui um registro de dados bancários do tipo "Débito Automático" que seja compatível com as informações enviadas pelo banco. Caso não seja encontrado será emitida mensagem indicando a ausência do registro de dado bancário para ser inativado. Caso exista, o registro de dados bancários de “Débito Automático” será desativado.
  + Após desativação do dado bancário, o mesmo é retirado do default para o cliente.

divs
