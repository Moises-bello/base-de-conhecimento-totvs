---
content_hash: 60174de38dd64112b81029f20bf9669bb40f0bb5540fdb931ea58018ac91bee7
fetched_at: '2026-06-29T00:05:47.318834+00:00'
page_id: '1010795528'
product: rm
source: tdn-rm
title: FOPTRP0022 - Ficha de Registro do Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1010795528
version: 6
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2602 e superiores.

## **02. V****ISÃO GERAL**

Relatório para emitir as informações do registro do funcionário. Nesse relatório temos os seguintes filtros disponíveis:

| Campo | Descrição do Campo | Campo na Tabela |
| --- | --- | --- |
| CPF | Filtra pelo CPF | PFUNC.CPF |
| Matrícula | Filtra pela matrícula do funcionário. | PFUNC.CHAPA |
| Seção | Filtra o código da seção de lotação do funcionário. | PFUNC.CODSECAO |
| Código Situação | Filtra pelo código de situação do funcionário. | PFUNC.CODSITUACAO |
| Filial | Filtra pela Filial | PFUNC.FILIAL |
| Tipo Funcionário | Filtra pelo tipo funcionário | PFUNC.CODTIPO |
| Data Admissão | Filtra pela data admissão | PFUNC.DATAADMISSAO |

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponível:

| Campo relatório | Tabela e campo | Complemento |
| --- | --- | --- |
| **DADOS EMPRESARIAIS** | | |
| Empresa | GCOLIGADA.NOMEFANTASIA |  |
| CNPJ | GCOLIGADA.CGC |  |
| Endereço | GCOLIGADA.RUA |  |
| Número | GCOLIGADA.NUMERO |  |
| Complemento | GCOLIGADA.COMPLEMENTO |  |
| Bairro | GCOLIGADA.BAIRRO |  |
| Cidade | GCOLIGADA.CIDADE |  |
| Estado | GCOLIGADA.ESTADO |  |
| CEP | GCOLIGADA.CEP |  |
| **DADOS CADASTRAIS** | | |
| Foto | GIMAGEM ON PPESSOA.IDIMAGEM = GIMAGEM.ID |  |
| No. Ficha Registro | PFUNC.NROFICHAREG |  |
| Matrícula | PFUNC.CHAPA |  |
| Nome Social | PPESSOA.NOMESOCIAL |  |
| Matricula eSocial | PFUNC.MATRICULAESOCIAL |  |
| Nome | PFUNC.NOME |  |
| Apelido | PPESSOA.APELIDO |  |
| Naturalidade | PPESSOA.NATURALIDADE |  |
| Mãe | PFDEPEND.NOME | PFDEPEND.GRAUPARENTESCO = 6 |
| Pai | PFDEPEND.NOME | PFDEPEND.GRAUPARENTESCO = 7 |
| Nacionalidade | PPESSOA.NACIONALIDADE |  |
| Estado Civil | PPESSOA.ESTADOCIVIL | Descrição |
| Sexo | PPESSOA.SEXO | Descrição |
| Raça | PCORRACA.DESCRICAO | Descrição |
| Tipo Deficiência | PPESSOA.DEFICIENTEFISICO | Descrição |
| Grau Instrução | PPESSOA.GRAUINSTRUCAO | Descrição |
| Data Nascimento | PPESSOA.DTNASCIMENTO |  |
| Entrada Brasil | PPESSOA.DATACHEGADA |  |
| Tipo Visto | PPESSOA.TIPOVISTO |  |
| Data Naturalização | PPESSOA.DATANATURALIZACAO |  |
| Endereço | PPESSOA.RUA |  |
| Número | PPESSOA.NUMERO |  |
| Complemento | PPESSOA.COMPLEMENTO |  |
| Bairro | PPESSOA.BAIRRO |  |
| Cidade | PPESSOA.CIDADE |  |
| Estado | PPESSOA.ESTADO |  |
| CEP | PPESSOA.CEP |  |
| **DADOS CONTRATUAIS** | | |
| Filial | GFILIAL.NOMEFANTASIA |  |
| CNPJ Filial | GFILIAL.CNPJ |  |
| Endereço | GFILIAL.RUA |  |
| Número | GFILIAL.NUMERO |  |
| Bairro | GFILIAL.BAIRRO |  |
| Complemento | GFILIAL.COMPLEMENTO |  |
| Cidade | GFILIAL.CIDADE |  |
| Estado | GFILIAL.ESTADO |  |
| CEP | GFILIAL.CEP |  |
| Tipo Admissão | PFUNC.TIPOADMISSAO, PTPADMISSAO.DESCRICAO | Descrição |
| Data Admissão | PFUNC.DATAADMISSAO |  |
| Recebimento | PFUNC.CODRECEBIMENTO, PCODRECEB.DESCRICAO | Descrição |
| Função | PFUNC.CODFUNCAO, PFUNCAO.DESCRICAO | Descrição |
| Tipo Funcionário | PFUNC.CODTIPO | Descrição |
| Salário | PFUNC.SALARIO |  |
| Tipo Contrato | PFUNC.TIPOCONTRATOPAZO | Descrição |
| Regime Previdenciário | PFUNC.TPREGIMEPREV | Descrição |
| Jornada Mensal | PFUNC.JORNADA\_MENSAL |  |
| Salário Hora | PFUNC.SALARIO / PFUNC.JORNADA\_MENSAL |  |
| Data Fim Contrato | PFUNC.FIMPRAZOCONTR |  |
| Sindicato | PFUNC.CODSINDICATO, PSINDIC.NOME | Descrição |
| Departamento | PFUNC.CODSECAO, PSECAO.DESCRICAO | Descrição |
| Categoria eSocial | PFUNC.CODCATEGORIAESOCIAL | Descrição |
| **DOCUMENTOS** | | |
| CPF | PPESSOA.CPF |  |
| Identidade | PPESSOA.CARTIDENTIDADE |  |
| Órgão | PPESSOA.ORGEMISSORIDENT |  |
| UF | PPESSOA.UFCARTIDENT |  |
| Data emissão | PPESSOA.DTEMISSAOIDENT |  |
| Certificado Reservista | PPESSOA.CERTIFRESERV |  |
| Categoria | PPESSOA.CATEGMILITAR |  |
| Carteira Habilitação | PPESSOA.CARTMOTORISTA |  |
| Categoria | PPESSOA.TIPOCARTHABILIT |  |
| Titulo Eleitor | PPESSOA.TITULOELEITOR |  |
| Zona | PPESSOA.ZONATITELEITOR |  |
| Seção | PPESSOA.SECAOTITELEITOR |  |
| RNM | PPESSOA.NROREGGERAL |  |
| Passaporte | PPESSOA.NPASSAPORTE |  |
| Emissão Passaporte | PPESSOA.DTEMISSPASSAPORTE |  |
| Validade Passporte | PPESSOA.DTVALPASSAPORTE |  |
| Decreto Imigração | PPESSOA.NRODECRETO |  |
| UF | PPESSOA.ORGEMISSORRNE |  |
| **DADOS BANCÁRIOS** | | |
| Banco | PFUNC.CODBANCOPAGTO |  |
| Agência | PFUNC.CODAGENCIAPAGTO |  |
| No. Conta | PFUNC.CONTAPAGAMENTO |  |
| Operação Conta | PFUNC.OPBANCARIA |  |
| Tipo Conta | PFUNC.TPCONTABANCARIA | Descrição |
| **CONTATO** | | |
| E-mail | PPESSOA.EMAIL |  |
| E-mail Pessoal | PPESSOA.EMAILPESSOAL |  |
| Telefone | PPESSOA.TELEFONE1 |  |
| **HISTORICO DE ENDEREÇO** | | |
| Data de Mudança | PFHSTEND.DTMUDANCA |  |
| Rua | PFHSTEND.RUA |  |
| Número | PFHSTEND.NUMERO |  |
| Complemento | PFHSTEND.COMPLEMENTO |  |
| Bairro | PFHSTEND.BAIRRO |  |
| Cidade | PFHSTEND.CIDADE |  |
| Estado | PFHSTEND.ESTADO |  |
| CEP | PFHSTEND.CEP |  |
| **DEPENDENTES** | | |
| Nome | PFDEPEND.NOME | exceto PFDEPEND.GRAUPARENTESCO = 6 e 7 |
| Parentesco | PFDEPEND.GRAUPARENDESCO | Descrição |
| Nascimento | PFDEPEND.DTNASCIMENTO |  |
| CPF | PFDEPEND.CPF |  |
| Sexo | PFDEPEND.SEXO | Descrição |
| Estado Civil | PFDEPEND.ESTADOCIVIL | Descrição |
| CPF | PFDEPEND.CPF |  |
| **CONTRIBUIÇÃO SINDICAL** | | |
| Data | PFHSTCSD.DTCONTRIBUICAO |  |
| Sindicato | PFHSTCSD.CODSINDICATO | Descrição |
| Valor | PFHSTCSD.VALOR |  |
| **ANOTAÇÕES GERAIS** | | |
| Data | PANOTAC.DTANOTACAO |  |
| Texto | PANOTAC.TEXTO |  |
| **AFASTAMENTOS** | | |
| Data | PHSTAFT.DTINICIO, PHSTAFT.DTFIM |  |
| Afastamento | PHSTAFT.TIPO | Descrição |
| Motivo | PHSTAFT.MOTIVO | Descrição |
| **ALTERAÇÃO DE FUNÇÃO** | | |
| Data | PFHSTFCO.DTMUDANCA |  |
| Função | PFHSTFCO.CODFUNCAO | Descrição |
| Motivo | PFHSTFCO.MOTIVO | Descrição |
| **ALTERAÇÃO DE SEÇÃO** | | |
| Data | PFHSTSEC.DTMUDANCA |  |
| Departamento | PFHSTSEC.CODSECAO | Descrição |
| Motivo | PFHSTSEC.MOTIVO | Descrição |
| **ALTERAÇÃO DE HORÁRIO** | | |
| Data | PFHSTHOR.DTMUDANCA |  |
| Horário | PFHSTHOR.CODHORARIO | Descrição |
| Motivo | PFHSTHOR.MOTIVO | Descrição |
| **ALTERAÇÃO DE SALÁRIO** | | |
| Data | PFHSTSAL.DTMUDANCA |  |
| Salário | PFHSTSAL.SALARIO |  |
| Motivo | PFHSTSAL.MOTIVO |  |
| **DELISGAMENTO** | | |
| Data | PFUNC.DATADEMISSAO |  |
| Tipo | PFUNC.TIPODEMISSAO | Descrição |

## **03. EXEMPLO DE UTILIZAÇÃO**

**1)** Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Mais Ações' depois em 'Anexos da Execução de Recurso do Smart View'. Configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

DICA

* É necessário que todos os campos do filtro sejam preenchidos. Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GCOLIGADA
* GFILIAL
* PSECAO
* PFUNC
* PPESSOA
* PFHSTEND
* PFHSTCSD
* PANOTAC
* PFUFERIAS
* PFHSTFCO
* PFHSTSEC
* PFHSTHOR
* PFHSTSAL
* PHSTAFT
* PFDEPEND
* PFUFERIASPER
* PFUFERIAS
* PTPADMISSAO
* PSINDIC
* PCODRECEB
