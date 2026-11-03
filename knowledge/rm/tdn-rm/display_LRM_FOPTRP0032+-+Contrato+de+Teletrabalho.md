---
content_hash: b9ea332ed4032b5c5ebf72d6ac0a731b4012aab3674406097024233547504592
fetched_at: '2026-06-29T00:05:52.742803+00:00'
page_id: '1059322978'
product: rm
source: tdn-rm
title: FOPTRP0032 - Contrato de Teletrabalho
type: documentation
url: https://tdn.totvs.com/display/LRM/FOPTRP0032+-+Contrato+de+Teletrabalho
version: 10
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

**A partir dos patches:**

+ 12.1.2606 e Superiores
+ [DT- Smart View Contrato de Teletrabalho](https://tdn.totvs.com/display/LRM/DT-+Smart+view-+Contrato+de+Teletrabalho)

## **02. V****ISÃO GERAL**

Utilizando o objeto de negócio [Ficha de Registro do Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=1046819891), o relatório contrato de teletrabalho irá formalizar a prestação de serviços fora das dependências da empresa com uso de tecnologia, definindo regras sobre jornada, custos (internet, luz, equipamentos) e a responsabilidade de cada parte.

#### **Regras de Filtro (Importante)**

Para garantir a performance e a segurança dos dados, o objeto possui uma lógica de filtros obrigatórios:

**Importante - Regras de Preenchimento:** O objeto exige que todos os parâmetros declarados recebam um valor para processar a requisição. Para alternar entre os tipos de filtro, utilize a lógica abaixo:

* **Filtrar por CPF:** Informe o número do CPF  do funcionário ou -1 para todos.
* **Filtrar por Matrícula:** Preencha com a chapa do funcionário ou -1 para todos.
* **Coligada:** Este campo é mandatório e deve sempre receber um código de coligada válido.
* **Seção:** Selecione uma seção ou as seções desejadas.
* **Código Situação:** Selecione a situação do funcionário que deseja que o relatório retorne.
* **Filial :** Selecione a filial
* **Tipo Funcionário:** Selecione o tipo de funcionário que deseja que o relatório retorne.
* **Data Admissão:**Este campo retorna PFUNC.DATAADMISSAO >= a data informada.

|  |  |  |
| --- | --- | --- |
| Matrícula | PFUNC.CHAPA | Filtra pela chapa do funcionário. |
| CPF | PFUNC.CPF | Filtra pelo CPF. |
| Coligada | PFUNC.CODCOLIGADA | Filtra código de coligada. |
| Seção | PFUNC.SECAO | Filtra o código da seção de lotação do funcionário. |
| Código  Situação | PFUNC.CODSITUACAO | Filtra pelo código de situação do funcionário. |
| Filial | PFUNC.FILIAL | Filtra pela Filial. |
| Tipo Funcionário | PFUNC.CODTIPO | Filtra pelo tipo funcionário. |
| Data Admissão | PFUNC.DATAADMISSAO | Filtra utilizando a PFUNC.DATAADMISSAO >= a data informada. |

A visualização do relatório será baseada no filtro inserido pelo usuário na visão do Smart View. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

| Campo do Relatório | Campo da Tabela | Complemento |
| --- | --- | --- |
| DADOS EMPRESARIAIS | | |
| --- | --- | --- |
| Nome da empresa | GCOLIGADA.NOMEFANTASIA | Lista o nome da empresa |
| Endereço da empresa | GCOLIGADA.RUA | Lista o endereço da empresa |
| Código da empresa | GCOLIGADA.CODCOLIGADA | Lista o código da coligada |
| Cidade da empresa | GCOLIGADA.CIDADE | Lista a cidade da empresa |
| CNPJ | GCOLIGADA.CGC | Lista o CNPJ da empresa |
| Salário | PFUNC.SALARIO | Lista o Salário do funcionário |
| Nome | PFUNC.NOME | Lista o nome do funcionário |
| Horario | PFUNC.CODHORARIO | Lista o horario ded trabalho do funcionário |
| Data de adminissão | PFUNC.DATAADMISSÃO | Lista a data de admissão do funcionário |
| CPF | PFUNC.CPF | Lista o cpf do funcionário |
| Número da carteira de trabalho | PFUNC.CGC | Lista o número da carteira de trabalho do funcionário |
| Número do PIS | PFUNC.PISPASEP | Lista número do PIS do funcionário |

## **03.  EXEMPLO DE UTILIZAÇÃO**

1)Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Ações', e configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

3) Filtros selecionados para geração do relatório.

  Filtro:

**DICAS:**

* É necessário que todos os campos do filtro sejam preenchidos.  Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* A impressão da logo só ocorrerá caso uma coligada seja selecionada no filtro.
* Clicando no ícone  o relatório é apresentado em tela inteira.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GCOLIGADA
* PFUNC
