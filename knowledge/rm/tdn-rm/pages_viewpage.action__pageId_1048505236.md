---
content_hash: e5cf4b8bb02490881ad5195c40cbda5c6b6d0552d9718599f5cccd8b42749c9e
fetched_at: '2026-06-29T00:05:51.193672+00:00'
page_id: '1048505236'
product: rm
source: tdn-rm
title: FOPTRP0026 - Termo de Responsabilidade para Concessão de Salário Família
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1048505236
version: 10
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2602 e Superiores
* [DT - Smart View - Termo Responsabilidade (Concessão Salário Família)](https://tdn.totvs.com/pages/viewpage.action?pageId=1048480083)

## **02. V****ISÃO GERAL**

O objeto de negócio tem como finalidade principal fornecer dados para a geração do **Termo de Responsabilidade de Salário Família**. Ele recupera informações detalhadas do funcionário (dados pessoais, endereço, CTPS e unidade organizacional) e de seus respectivos dependentes que possuam incidência de salario familia.

O processo funciona em duas etapas principais:

1. **ListaFuncionarios**: Busca os dados cadastrais da coligada e do funcionário, permitindo filtrar apenas aqueles que possuem dependentes (via cláusula `HAVING`).
2. **ListaDependentes**: Busca a relação de dependentes para os funcionários selecionados, vinculando-os através da Chapa e Código da Coligada.
3. **Logotipo**: Recupera dinamicamente a imagem da empresa para exibição no cabeçalho do termo.

|  |  |  |
| --- | --- | --- |
| Coligada | PFUNC.CODCOLIGADA | Filtra código de coligada |
| Matricula | PFUNC.CHAPA | Filtra pela matricula do funcionário |
| Seção | PFUNC.CODSECAO | Filtra código da seção |
| Situação | PFUNC.CODSITUACAO | Filtra pelo código da situação |
| Data de admissão (data inicio) | PFUNC.DATAADMISSÃO | Filtra pela data de admissão ou dentro de uma período de admissão  >= e <= |
| Data de admissão (data fim) | PFUNC.DATAADMISSÃO | Filtra pela data de admissão ou dentro de uma período de admissão  >= e <= |
| Funcionário sem dependente | (0-Não / 1-Sim) | Exibe funcionário sem dependente |

A visualização do relatório será conforme o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

| Campo do Relatório | Campo da Tabela | Complemento |
| --- | --- | --- |
| DADOS EMPRESARIAIS | | |
| Nome da empresa | GCOLIGADA.NOMEFANTASIA | Lista o nome da empresa |
| Endereço | GCOLIGADA.RUA | Lista o endereço da empresa |
| Número | GCOLIGADA.NUMERO | Lista o número da empresa |
| Bairro | GCOLIGADA.BAIRRO | Lista o bairro da empresa |
| CEP | GCOLIGADA.CEP | Lista o cep da empresa |
| Cidade | GCOLIGADA.CIDADE | Lista a cidade da empresa |
| UF | GCOLIGADA.ESTADO | Lista o estado da empresa |
| CNPJ | GCOLIGADA.CGC | Lista o CNPJ da empresa |
| DADOS DO EMPREGADO | | |
| Nome | PFUNC.NOME | Lista o nome do funcionário |
| Matricula | PFUNC.CHAPA | Lista a matricula do funcionário |
| Departamento | PPESSOA.EMPRESA | Lista o departamento do funcionário |
| CTPS | PPESSOA.CARTEIRATRAB | Lista o número da carteira de trabalho do funcionário |
| Série | PPESSOA.SERIECARTTRAB | Lista a série da carteira de trabalho do funcionário |
| Endereço | PPESSOA.RUA | Lista o endereço do funcionário |
| Numero | PPESSOA.NUMERO | Lista o número do endereço do funcionário |
| Bairro | PPESSOA.BAIRRO | Lista o bairro do funcionário |
| CEP | PPESSOA.CEP | Lista o CEP do funcionário |
| Estado Civil | PPESSOA.ESTADOCIVIL | Lista o estado civil do funcionário |
| CPF | PPESSOA.CPF | Lista o CPF do funcionário |
| RG | PPESSOA.CARTIDENTIDADE | Lista o RG do funcionário |
| DEPENDENTES | | |
| Numero do dependente | PFDEPEND.NRODEPEND | Lista o número do dependente |
| Nome do dependente | PFDEPEND.NOME | Lista o nome do dependente |
| Cpf do dependente | PFDEPEND.CPF | Lista o CPF do dependente |
| Relação do dependente | PFDEPEND.GRAUPARENTESCO | Lista a relação do dependente |
| Data de nascimento do dependente | PFDEPEND.DTNASCIMENTO | Lista a data de nascimento do dependente |

## **03.  EXEMPLO DE UTILIZAÇÃO**

1)Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Ações', e configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

3) Filtros selecionados para geração do relatório.

DICA

* É necessário que todos os campos do filtro sejam preenchidos.  Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* A impressão da logo só ocorrerá caso uma coligada seja selecionada no filtro.
* Clicando no ícone  o relatório é apresentado em tela inteira.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GFILIAL
* GDEPTO
* PSECAO
* PFUNC
