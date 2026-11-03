---
content_hash: c24d3243c78780ebea695212c8653c5b30ebd0c2dbd8ce409cfb5c414d16d310
fetched_at: '2026-06-29T00:12:15.386494+00:00'
page_id: '977835958'
product: rm
source: tdn-rm
title: FOPTRP0021 - Relatório de Admitidos e Desligados - Turnover
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=977835958
version: 9
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2510 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir listagem de admitidos e demitidos - Tournover.  Nesse relatório temos os seguintes filtros disponíveis:

| Campo | Descrição do Campo | Campo na Tabela |
| --- | --- | --- |
| Matrícula | Filtra pela matrícula do funcionário. | PFUNC.CHAPA |
| Seção | Filtra o código da seção de lotação do funcionário. | PFUNC.CODSECAO |
| Data de referência de | Filtra início do período | PFUNC.DATAADMISSAO, PFUNC.DATADEMISSAO |
| Data de referência até | Filtra  fim do período | PFUNC.DATAADMISSAO, PFUNC.DATADEMISSAO |
| Filial | Filtra Filial | PFUNC.FILIAL |

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponível:

| **Campo** | **Campo na Tabela** |
| --- | --- |
| Nome da Empresa | GCOLIGADA.NOMEFANTASIA |
| CNPJ/CPF | GCOLIGADA.CGC |
| Estabelecimento/Filial | GFILIAL.NOMEFANTASIA |
| Matrícula | PFUNC.CHAPA |
| Data de Admissão | PFUNC.DATAADMISSAO |
| Nome da Pessoa Colaboradora | PFUNC.NOME |
| Cargo/Função | PFUNCAO.NOME |
| Tipo Contratação | PFUNC.TIPOADMISSAO |
| Salário Contratual | PFUNC.SALARIO |
| Transferência | PFUNC.TIPOADMISSAO |
| Data Desligamento | PFUNC.DATADEMISSAO |
| Aviso Prévio | PFUNC.TEMAVISOPREVIO, PFUNC.DESCONTAAVISOPREVIO, PFUNC.DTAVISOPREVIOTRAB |
| Código/Motivo do Desligamento | PFUNC.MOTIVODEMISSAO |
| PCD | PPESSOA.DEFICIENTEAUDITIVO,  PPESSOA.DEFICIENTEFISICO, PPESSOA.DEFICIENTEINTELECTUAL, PPESSOA.BRPDH, PPESSOA.DEFICIENTEFALA, PPESSOA.DEFICIENTEVISUAL, PPESSOA.DEFICIENTEMENTAL |
| Feminino, Masculino | PPESSOA.SEXO |
| Branco, Pardo, Amarelo, Preto e Indígena | PPESSOA.CORRACA |
| Aprendiz | PFUNC.CODTIPO |
| Estágio | PFUNC.CODTIPO |

## **03. EXEMPLO DE UTILIZAÇÃO**

**1)** Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Anexos da Execução de Recurso do Smart View'. Configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

* É necessário que todos os campos do filtro sejam preenchidos. Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* A impressão da logo só ocorrerá caso uma coligada seja selecionada no filtro.
* Clicando no ícone  o relatório é apresentado em tela inteira.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GCOLIGADA
* GFILIAL
* PPESSOA
* PFUNC
