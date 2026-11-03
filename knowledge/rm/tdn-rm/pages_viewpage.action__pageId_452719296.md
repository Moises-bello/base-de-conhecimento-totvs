---
content_hash: 02aedc75e538cd2f7b2d5284dc57e61fbd5bbeefd513940d1ca1c2ca2ee7b23a
fetched_at: '2026-06-29T00:10:05.710577+00:00'
page_id: '452719296'
product: rm
source: tdn-rm
title: Layout Para Importação de Funcionários (Dados Cadastrais - Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719296
version: 82
---

**Importante:**

**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: **";"**  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são exemplos de premissas para a importação, caso a mesma esteja vinculada a tabela de Dados Cadastrais do Funcionário da base de origem:  
 

* PSECAO
* PFUNCAO
* PSINDIC
* AHORARIO
* PMOTADMISSAO
* PMOTDEMISSAO
* GBANCO
* GAGENCIA
* FCFO
* PCCUSTO
* DTIPORUA
* DTIPOBAIRRO

**Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:

- 0 (zero) ou 1(um) em campos do tipo **Booleano**;  
- Nº s (00) em campos do tipo**Inteiro**;  
- Nº s com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
- F - campos cuja alteração ligam os flags de FGTS  
- H - campos cuja alteração geram histórico  
- Q - campos que podem ser alterados via RM Portal  
- O sistema leva em consideração as informações agrupadas da seguinte maneira:

* + - CPF e Data de Nascimento
    - Carteira de identidade
    - Carteira de Trabalho e Série da Carteira de Trabalho
    - Nome e Data de Nascimento

**Atenção!** O encode do arquivo deve estar em UTF-8 ou ANSI. UTF-8 (sem BOM) pode ocasionar erro nos caracteres especiais. Além disso, o arquivo deve obrigatoriamente ter a **extensão .TXT**.

   
Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.  
   
 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **ORIGEM:** Arquivo informado no campo "Dados Cadastrais" | | | | | | |
| **DESTINO:** Tabelas  PPESSOA, PFUNC e demais tabelas de históricos conforme regra em validações e procedimentos antes de efetuar a gravação dos dados do funcionário | | | | | | |
| **LAYOUT** | | | | | | |
| **Flg** | **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **POSIÇÃO** | **TABELA E NOME DO CAMPO** | **OBSERVAÇÃOOOOOOOOOOOOO** |
| **F** | **Chapa** | **String** | **16** | 1 | **PFUNC.CHAPA** |  |
| **F** | **Nome** | **String** | **120** | 2 | **PPESSOA.NOME** |  |
|  | Apelido | String | 40 | 3 | PPESSOA.APELIDO |  |
| **F** | **Data de Nascimento** | **Data** | **8** | 4 | **PESSOA.DTNASCIMENTO** |  |
|  | **Estado Civil** | **Char** | **1** | 5 | **PPESSOA.ESTADOCIVIL** |  |
|  | **Sexo (M/F)** | **Char** | **1** | 6 | **PPESSOA.SEXO** |  |
|  | Nacionalidade | String | 3 | 7 | PPESSOA.NACIONALIDADE |  |
|  | **Grau de Instrução** | **String** | **1** | 8 | **PPESSOA.GRAUINSTRUCAO** |  |
| FHQ | Rua | String | 30 | 9 | PESSOA.RUA |  |
| FHQ | Nº | String | 8 | 10 | PPESSOA.NUMERO |  |
| FHQ | Complemento | String | 16 | 11 | PPESSOA.COMPLEMENTO |  |
| FHQ | Bairro | String | 20 | 12 | PPESSOA.BAIRRO |  |
| FHQ | Estado (Unidade da Federação) | String | 2 | 13 | PPESSOA.ESTADO |  |
| FHQ | Cidade | String | 32 | 14 | PPESSOA.CIDADE |  |
| FHQ | CEP | String | 9 | 15 | PPESSOA.CEP |  |
| FHQ | Nome do País | String | 16 | 16 | PPESSOA.PAIS |  |
|  | Registro Profissional | String | 15 | 17 | PPESSOA.REGPROFISSIONAL |  |
|  | **CPF** | **String** | **12** | 18 | **PPESSOA.CPF** |  |
| FQ | Telefone 1 | String | 15 | 19 | PPESSOA.TELEFONE1 |  |
| FQ | Telefone 2 | String | 15 | 20 | PPESSOA.TELEFONE2 |  |
|  | Nº da Carteira de Identidade | String | 15 | 21 | PPESSOA.CARTIDENTIDADE |  |
|  | UF - Carteira de Identidade | String | 2 | 22 | PPESSOA.UFCARTIDENT |  |
|  | Órgão Emissor - Carteira de Identidade | String | 15 | 23 | PPESSOA.ORGEMISSORIDENT |  |
|  | Data de Emissão - Carteira de Identidade | Data | 8 | 24 | PPESSOA.DTEMISSAOIDENT |  |
|  | Data de Vencimento- Carteira de Identidade | Data | 8 | 25 | PPESSOA.DTVENCIDENT |  |
|  | Título de Eleitor | String | 14 | 26 | PPESSOA.TITULOELEITOR |  |
|  | Zona de Votação | String | 6 | 27 | PPESSOA.ZONATITELEITOR |  |
|  | Seção de Votacão | String | 6 | 28 | PPESSOA.SECAOTITELEITOR |  |
| F | Nº da Carteira de Trabalho | String | 10 | 29 | PPESSOA.CARTEIRATRAB |  |
| F | Série - Carteira de Trabalho | String | 5 | 30 | PPESSOA.SERIECARTTRAB |  |
|  | UF - Carteira de Trabalho | String | 2 | 31 | PPESSOA.UFCARTTRAB |  |
|  | Data da emissão - Carteira de Trabalho | Data | 8 | 32 | PPESSOA.DTCARTTRAB |  |
|  | Data de Vencimento - Carteira de Trabalho | Data | 8 | 33 | PPESSOA.DTVENCCARTTRAB |  |
|  | NIT - Tipo de Carteira de Trabalho | Inteiro | 1 | 34 | PPESSOA.NIT | 0-Não ou 1-Sim |
|  | Nº da Carteira de Motorista | String | 15 | 35 | PPESSOA.CARTMOTORISTA |  |
|  | Tipo da Carteira de Habilitação | String | 5 | 36 | PPESSOA.TIPOCARTHABILIT |  |
|  | Data de Venc. Da Habilitação | Data | 8 | 37 | PPESSOA.DTVENCHABILIT |  |
|  | Nº do Certificado Reservista | String | 40 | 38 | PPESSOA.CERTIFRESERV |  |
|  | Categoria Militar | String | 10 | 39 | PPESSOA.CATEGMILITAR |  |
|  | **Naturalidade** | **String** | **32** | 40 | **PPESSOA.NATURALIDADE** |  |
|  | **Estado Natal** | **String** | **2** | 41 | **PPESSOA.ESTADONATAL** |  |
|  | Data da Chegada ao Brasil | Data | 8 | 42 | PPESSOA.DATACHEGADA |  |
|  | Carta Modelo 19 | String | 15 | 43 | PPESSOA.CARTMODELO19 |  |
|  | Cônjuge Brasil | Inteiro | 1 | 44 | PPESSOA.CONJUGEBRASIL | 0-Não ou 1-Sim |
|  | Naturalizado | Inteiro | 1 | 45 | PPESSOA.NATURALIZADO | 0-Não ou 1-Sim |
|  | Filhos no Brasil | Inteiro | 1 | 46 | PPESSOA.FILHOSBRASIL | 0-Não ou 1-Sim |
|  | Nº de Filhos no Brasil | Inteiro | 2 | 47 | PPESSOA.NROFILHOSBRASIL |  |
|  | Nº do Registro Geral | String | 15 | 48 | PPESSOA.NROREGGERAL |  |
|  | Nº do Decreto | String | 15 | 49 | PPESSOA.NRODECRETO |  |
|  | Tipo de Visto | String | 10 | 50 | PPESSOA.TIPOVISTO |  |
|  | E-Mail | String | 60 | 51 | PPESSOA.EMAIL |  |
| Q | Senha | String | 8 | 52 | ? |  |
|  | **Nº da Ficha de Registro** | **Inteiro** | **10** | **53** | **PFUNC.NROFICHAREG** |  |
|  | **Código de Recebimento** | **Char** | **1** | **54** | **PFUNC.CODRECEBIMENTO** |  |
| **H** | **Código de Situação** | **Char** | **1** | **55** | **PFUNC.CODSITUACAO** |  |
| **F** | **Código do Tipo do Funcionário** | **Char** | **1** | **56** | **PFUNC.CODTIPO** |  |
| **F H** | **Código da Seção** | **String** | **35** | **57** | **PFUNC.CODSECAO** |  |
| **H** | **Código da Função** | **String** | **10** | **58** | **PFUNC.CODFUNCAO** |  |
|  | **Código do Sindicato** | **String** | **10** | **59** | **PFUNC.CODSINDICATO** |  |
| **H** | **Jornada (Formato HHH:MM)** | **String** | **6** | **60** | **PFUNC.JORNADAMENSAL** |  |
| **H** | **Código do Horário** | **String** | **10** | **61** | **PFUNC.CODHORARIO** |  |
| H | Nº  de Dependentes de IRRF | Inteiro | 2 | 62 | PFUNC.NRODEPIRRF |  |
|  | Nº  de Dependentes de Salário Família | Inteiro | 2 | 63 | PFUNC.NRODEPSALFAM |  |
|  | Data Base | Data | 8 | 64 | PFUNC.DTBASE |  |
| **H** | **Salário** | **Real** | **15** | **65** | **PFUNC.SALARIO** | **Formato 999999999999,99** |
|  | **Situação de FGTS** | **Char** | **1** | **66** | **PFUNC.SITUACAOFGTS** | **1-Optante ou 2-Não Optante** |
| **F** | **Data de Opção de FGTS** | **Data** | **8** | **67** | **PFUNC.DTOPCAOFGTS** | **Obrigatório quando o campo 66 for preenchido com 1** |
|  | Nº  da Conta de FGTS | String | 11 | 68 | PFUNC.CONTAFGTS |  |
|  | Saldo do FGTS no Banco | Real | 15 | 69 | PFUNC.SALDOFGTS | **Formato 999999999999,99** |
|  | Data do Saldo do FGTS | Data | 8 | 70 | PFUNC.DTSALDOFGTS |  |
| F | PIS/PASEP | String | 11 | 71 | PFUNC.PISPASEP |  |
|  | Data de Cadastro do PIS | Data | 8 | 72 | PFUNC.DTCADASTROPIS |  |
|  | Cód. Banco do PIS | String | 3 | 73 | PFUNC.CODBANCOPIS |  |
|  | **Contribuição Sindical** | **Char** | **1** | 74 | **PFUNC.CONTRIBSINDICAL** | **J-Já Descontou ou L-Liberal ou N-Não Descontou** |
|  | Aposentado | Inteiro | 1 | 75 | PFUNC.APOSENTADO | 0-Não ou 1-Sim |
|  | Tem Mais de 65 Anos | Inteiro | 1 | 76 | PFUNC.TEMMAIS65ANOS |  |
|  | Ajuda de Custo | Real | 15 | 77 | PFUNC.AJUDACUSTO | 0-Não ou 1-Sim |
|  | Percentual de Adiantamento | Real | 6 | 78 | PFUNC.PERCENTADIANT | Formato 999,99 |
|  | Arredondamento | Real | 8 | 79 | PFUNC.ARREDONDAMENTO | Formato 99999,99 |
| F | **Data de Admissão** | **Data** | **8** | **80** | **PFUNC.DATAADMISSAO** |  |
| **F** | **Tipo de Admissão** | **Char** | **1** | **81** | **PFUNC.TIPOADMISSAO** |  |
|  | Data da Transferência | Data | 8 | 82 | PFUNC.DTTRANSFERENCIA |  |
|  | **Motivo da Admissão** | **String** | **2** | **83** | **PFUNC.MOTIVOADMISSAO** |  |
|  | Contrato tem Prazo Determinado | Inteiro | 1 | 84 | PFUNC.TEMPRAZOCONTR | 0-Não ou 1-Sim |
|  | Fim do Prazo do Contrato | Data | 8 | 85 | PFUNC.FIMPRAZOCONTR |  |
|  | Data de Demissão | Data | 8 | 86 | PFUNC.DATADEMISSAO |  |
|  | Tipo de Demissão | Char | 1 | 87 | PFUNC.TIPODEMISSAO |  |
|  | Motivo de Demissão | String | 2 | 88 | PFUNC.MOTIVODEMISSAO |  |
|  | Data de Desligamento | Data | 8 | 89 | PFUNC.DTDESLIGAMENTO |  |
|  | Data da Última Movimentação | Data | 8 | 90 | PFUNC.DTULTIMOMOVIM |  |
|  | Data de Pagamento da Rescisão | Data | 8 | 91 | PFUNC.DTPAGTORESCISAO |  |
|  | Código de Saque de FGTS | String | 2 | 92 | PFUNC.CODSAQUEFGTS |  |
|  | **Tem Aviso Prévio** | **Integer** | **1** | **93** | **PFUNC.TEMAVISOPREVIO** | **0- Não ou 1-Sim**  **Obrigatório quando o  campo 86 for preenchido.** |
|  | **Data do Aviso Prévio** | **Data** | **8** | **94** | **PFUNC.DTAVISOPREVIO** | **Obrigatório quando o  campo 93 for preenchido com 1-Sim.** |
|  | **Nº  de Dias de Aviso** | **Inteiro** | **3** | **95** | **PFUNC.NRODIASAVISO** | **Obrigatório quando o  campo 93 for preenchido com 1-Sim.** |
|  | Data de Venc. De Férias | Data | 8 | 96 | PFUNC.DTVENCFERIAS |  |
| Q | Início de Programação de Férias 1 | Data | 8 | 97 | PFUNC.INICPROGFERIAS1 |  |
| Q | Fim de Programação de Férias 1 | Data | 8 | 98 | PFUNC.FIMPROGFERIAS1 |  |
|  | Quer Abono | Inteiro | 1 | 99 | PFUNC.QUERABONO | 0- Não ou 1-Sim |
|  | Quer 1ª Parcela de 13º Salário | Inteiro | 1 | 100 | PFUNC.QUER1APARC13O | 0- Não ou 1-Sim |
|  | Nº de dias de Adiantamento de Férias | Inteiro | 3 | 101 | PFUNC.NRODIASADIANTFER |  |
|  | Evento de Adiantamento de Férias | String | 4 | 102 | PFUNC.EVTADIANTFERIAS |  |
|  | Férias Coletivas / Globais | Inteiro | 1 | 103 | PFUNC.FERIASCOLETIVAS | 0-Não ou 1-Sim |
| Q | Nº de dias de Férias | Real | 7 | 104 | PFUNC.NRODIASFERIAS | Formato 9999,99. O 1º representa o sinal. 0-Positivo ou -Negativo. |
|  | Nº de dias de Abono | Real | 6 | 105 | PFUNC.NRODIASABONO | Formato 999,99 |
|  | Saldo de Férias | Real | 6 | 106 | PFUNC.SALDOFERIAS | Formato 999,99 |
|  | Saldo de Férias Anterior | Real | 6 | 107 | PFUNC.SALDOFERIASANT | Formato 999,99 |
|  | Saldo de Férias Auxiliar | Real | 6 | 108 | PFUNC.SALDOFERANTAUX | Formato 999,99 |
|  | Observação de Férias | String | 80 | 109 | PFUNC.OBSFERIAS |  |
|  | Data de Pagamento de Férias | Data | 8 | 110 | PFUNC.DTPAGTOFERIAS |  |
|  | Data de Aviso de Férias | Data | 8 | 111 | PFUNC.DTAVISOFERIAS |  |
|  | Nº de Dias Licença Remunerada 1 | Real | 6 | 112 | PFUNC.NDIASLICREM1 | Formato 999,99 |
|  | Nº de Dias Licença Remunerada 2 | Real | 6 | 113 | PFUNC.NDIASLICREM2 | Formato 999,99 |
|  | Data de Início da Licença | Data | 8 | 114 | PFUNC.DTINICIOLICENCA |  |
|  | Média Salário Maternidade | Real | 15 | 115 | PFUNC.MEDIASALMATERN | Formato 999999999999,99 |
|  | **Situação RAIS** | **Char** | **1** | **116** | **PFUNC.SITUACAORAIS** |  |
| Q | Cód. Banco de Pagamento | String | 3 | 117 | PFUNC.CODBANCOPAGTO |  |
| Q | Cód. Agência Pagamento | String | 6 | 118 | PFUNC.CODAGENCIAPAGTO |  |
| Q | Conta de Pagamento | String | 15 | 119 | PFUNC.CONTAPAGAMENTO |  |
|  | Membro Sindical | Inteiro | 1 | 120 | PFUNC.MEMBROSINDICAL | 0-Não ou 1-Sim |
| F | Vínculo RAIS | Char | 1 | 121 | PFUNC.VINCULORAIS |  |
|  | Usa Vale Transporte | Inteiro | 1 | 122 | PFUNC.USAVALETRANSP | 0-Não ou 1-Sim |
|  | Dias Úteis no Mês | Inteiro | 2 | 123 | PFUNC.DIASUTEISMES |  |
|  | Dias Úteis Meio Expediente | Inteiro | 2 | 124 | PFUNC.DIASUTMEIOEXP |  |
|  | Dias Úteis Próximo Mês | Inteiro | 2 | 125 | PFUNC.DIASUTPROXMES |  |
|  | Dias Úteis Próximo Mês Meio Expediente | Inteiro | 2 | 126 | PFUNC.DIASUTPROXMEIO |  |
|  | Dias Úteis Restantes | Inteiro | 2 | 127 | PFUNC.DIASUTRESTANTES |  |
|  | Dias Úteis Restantes Meio | Inteiro | 2 | 128 | PFUNC.DIASUTRESTMEIO |  |
|  | Mudou Endereço | Inteiro | 1 | 129 | PFUNC.MUDOUENDERECO | 0-Não ou 1-Sim |
|  | Mudou Carteira de Trabalho | Inteiro | 1 | 130 | PFUNC.MUDOUCARTTRAB | 0-Não ou 1-Sim |
|  | Antiga Carteira de Trabalho | String | 10 | 131 | PFUNC.ANTIGACARTTRAB |  |
|  | Antiga Série - Carteira de Trabalho | String | 5 | 132 | PFUNC.ANTIGASERIECART |  |
|  | Mudou Nome | Inteiro | 1 | 133 | PFUNC.MUDOUNOME | 0-Não ou 1-Sim |
|  | Antigo Nome | String | 45 | 134 | PFUNC.ANTIGONOME |  |
|  | Mudou PIS | Inteiro | 1 | 135 | PFUNC.MUDOUPIS | 0-Não ou 1-Sim |
|  | Antigo PIS | String | 11 | 136 | PFUNC.ANTIGOPIS |  |
|  | Mudou Chapa | Inteiro | 1 | 137 | PFUNC.MUDOUCHAPA | 0-Não ou 1-Sim |
|  | Antiga Chapa | String | 16 | 138 | PFUNC.ANTIGACHAPA |  |
|  | Mudou Data de Admissão | Inteiro | 1 | 139 | PFUNC.MUDOUADMISSAO | 0-Não ou 1-Sim |
|  | Antiga Data de Admissão | Data | 8 | 140 | PFUNC.ANTIGADTADM |  |
|  | Antigo Vínculo | Char | 1 | 141 | PFUNC.ANTIGOVINCULO |  |
|  | Antigo Tipo do Funcionário | Char | 1 | 142 | PFUNC.ANTIGOTIPOFUNC |  |
|  | Antigo Tipo de Admissão | Char | 1 | 143 | PFUNC.ANTIGOTIPOADM |  |
|  | Mudou Data de Opção | Inteiro | 1 | 144 | PFUNC.MUDOUDTOPCAO | 0-Não ou 1-Sim |
|  | Antiga Data de Opção | Data | 8 | 145 | PFUNC.ANTIGADTOPCAO |  |
|  | Mudou Seção | Inteiro | 1 | 146 | PFUNC.MUDOUSECAO | 0-Não ou 1-Sim |
|  | Antiga Seção | String | 35 | 147 | PFUNC.ANTIGASECAO |  |
|  | Mudou Data de Nascimento | Inteiro | 1 | 148 | PFUNC.MUDOUDTNASCIM | 0-Não ou 1-Sim |
|  | Antiga Data de Nascimento | Data | 8 | 149 | PFUNC.ANTIGADTNASCIM |  |
|  | Falta Alterar FGTS | Inteiro | 1 | 150 | PFUNC.FALTAALTERFGTS | 0-Não ou 1-Sim |
|  | Deduzir IRRF Mais 65 | Inteiro | 1 | 151 | PFUNC.DEDUZIRRF65 | 0-Não ou 1-Sim |
|  | PIS para FGTS | String | 11 | 152 | PFUNC.PISPARAFGTS |  |
|  | Cód. Banco de FGTS | String | 3 | 153 | PFUNC.CODBANCOFGTS |  |
|  | Desconta Aviso Prévio | Inteiro | 1 | 154 | PFUNC.DESCONTAAVISOPREVIO | 0-Não ou 1-Sim |
|  | Código identificador da filial | Inteiro | 4 | 155 | PSECAO.CODFILIAL |  |
| **H** | **Índice de Início de Horário** | **Inteiro** | **5** | **156** | **PFUNC.INDINICIOHOR** |  |
|  | Usa Salário Composto | Inteiro | 1 | 157 | PFUNC.USASALCOMPOSTO | 0-Não ou 1-Sim |
|  | Funcionário é membro da CIPA | Inteiro | 1 | 158 | PFUNC.MEMBROCIPA | 0-Não ou 1-Sim |
|  | Operação bancária | String | 5 | 159 | PFUNC.OPBANCARIA |  |
|  | Nro vezes para desconto do empréstimo de férias | Inteiro | 2 | 160 | PFUNC.NUMVEZESDESCEMPRESTIMO |  |
|  | Data de início para desconto do empréstimo de férias | Data | 8 | 161 | PFUNC.DATAINICIODESCEMPRESTIMO |  |
|  | Grupo Salarial | String | 10 | 162 | PFUNC.GRUPOSALARIAL |  |
|  | Funcionário é o atual | Inteiro | 1 | 163 | PFUNC.REGATUAL | 0-Não ou 1-Sim  O campo deverá conter o valor "1", mesmo quando houver mais de um registro (múltiplos vínculos) para o mesmo funcionário dentro da mesma coligada.  Exceção: Nos casos de transferência, o registro referente à demissão deve ser preenchido com o valor "0", enquanto o novo registro ativo (após a transferência) deve ser preenchido com o valor "1". |
|  | Previsão de disponibilidade | Data | 8 | 164 | PFUNC.PREVDISP | Este campo deverá ficar em branco, devido não ser  mais utilizado. |
|  | Código da Ocorrência | Inteiro | 2 | 165 | PFUNC.CODOCORRENCIA |  |
|  | Código da Categoria | Inteiro | 2 | 166 | PFUNC.CODCATEGORIA |  |
|  | Classe de contribuição para o INSS | Inteiro | 8 | 167 | PFUNC.CLASSECONTRIB |  |
|  | Código da equipe do funcionário | String | 20 | 168 | PFUNC.CODEQUIPE |  |
|  | Funcionário tem status de supervisor | Inteiro | 1 | 169 | PFUNC.ESUPERVISOR | 0-Não ou 1-Sim |
|  | Integração Contábil | String | 22 | 170 | PFUNC.INTEGRCONTABIL |  |
|  | Integração Gerencial | String | 22 | 171 | PFUNC.INTEGRGERENCIAL |  |
|  | Usa Controle de Saldo de Verbas | Inteiro | 1 | 172 | PFUNC.USACONTROLEDESALDO | 0-Não ou 1-Sim |
|  | Código Contribuinte Individual | String | 11 | 173 | PFUNC.CI |  |
|  | Mudou Código Contribuinte Individual | Inteiro | 1 | 174 | PFUNC.MUDOUCI | 0-Não ou 1-Sim |
|  | Antigo Código Contribuinte Individual | Inteiro | 11 | 175 | PFUNC.ANTIGOCI |  |
|  | Período de Rescisão | Inteiro | 2 | 176 | PFUNC.PERIODORESCISAO |  |
|  | Cor / Raça | Inteiro | 1 | 177 | PPESSOA.CORRACA | 0-Indígena | 2-Branca | 4-Preta | 6-Amarela | 8-Parda |
|  | Flag Deficiente físico? | Inteiro | 1 | 178 | PPESSOA.DEFICIENTEFISICO |  |
|  | FGTS mês anterior será recolhido na GRFC | Inteiro | 1 | 179 | PFUNC.FGTSMESANTRECOLGRFP | 0-Não ou 1-Sim |
|  | Código do Nível da Tabela Salarial | String | 10 | 180 | PFUNC.CODNIVELSAL |  |
|  | Nº  de Dias de Férias para a Jornada Reduzida | Inteiro | 2 | 181 | PFUNC.NRODIASFERIASJORNRED |  |
|  | Tem alvará judicial para funcionário menor de 16 anos | String | 1 | 182 | PFUNC.POSSUIALVARAMENOR16 | 0-Não ou 1-Sim |
|  | Situação do INSS | Inteiro | 1 | 183 | PFUNC.SITUACAOINSS |  |
|  | Data de aposentadoria | Data | 8 | 184 | PFUNC.DTAPOSENTADORIA |  |
|  | Quer adiantamento nas férias | Inteiro | 1 | 185 | PFUNC.QUERADIANTAMENTO | 0-Não ou 1-Sim |
|  | Data próximo período aquisitivo de férias | Data | 8 | 186 | PFUNC.DTPROXAQUISFERIAS |  |
|  | Coligada do fornecedor | Inteiro | 5 | 187 | PFUNC.CODCOLFORNEC |  |
|  | Código do fornecedor | String | 25 | 188 | PFUNC.CODFORNECEDOR |  |
|  | Deficiente Auditivo | Inteiro | 1 | 189 | PPESSOA.DEFICIENTEAUDITIVO |  |
|  | Deficiente Fala | Inteiro | 1 | 190 | PPESSOA.DEFICIENTEFALA |  |
|  | Deficiente Mental | Inteiro | 1 | 191 | PPESSOA.DEFICIENTEMENTAL |  |
|  | Deficiente Visual | Inteiro | 1 | 192 | PPESSOA.DEFICIENTEVISUAL |  |
|  | Código Município | String | 20 | 193 | PPESSOA.CODMUNICIPIO |  |
|  | Localidade | String | 40 | 194 | PPESSOA.LOCALIDADE |  |
|  | Posição Abono | Inteiro | 2 | 195 | PFUNC.POSICAOABONO | 0-Não ou 1-Sim |
|  | Nº de Dias de Férias Corridos | Inteiro | 2 | 196 | PFUNC.NRODIASFERIASCORRIDOS |  |
|  | País de Origem | String | 20 | 197 | PPESSOA.PAISORIGEM |  |
|  | Fumante | Inteiro | 2 | 198 | PPESSOA.FUMANTE | 0-Não ou 1-Sim |
|  | Nº  Passaporte | String | 15 | 199 | PPESSOA.NPASSAPORTE |  |
|  | Telefone 3 | String | 15 | 200 | PPESSOA.TELEFONE3 |  |
|  | Data de Emissão do Passaporte | Data | 8 | 201 | PPESSOA.DTEMISSPASSAPORTE |  |
|  | Data validade do Passaporte | Data | 8 | 202 | PPESSOA.DTVALPASSAPORTE |  |
|  | Tipo de Aposentadoria | Inteiro | 1 | 203 | PFUNC.TIPOAPOSENTADORIA | 1-Tempo Serviço | 2-Idade | 3-Especial |
|  | Reposição de Vaga | String | 1 | 204 | PFUNC.REPOEVAGA | N-Não ou S-Sim |
|  | Saldo de FGTS Real | Real | 15 | 205 | PFUNC.SALDOFGTSREAL |  |
|  | BR-PDH | Inteiro | 5 | 206 | PPESSOA.BRPDH | 0-Não Aplicável | 1-BR | 2-PDH |
|  | Carregou Dados do Aviso Prévio | Inteiro | 2 | 207 | PFUNC.CARREGOUAVISOPREVIO |  |
|  | Situação IRRF | Inteiro | 1 | 208 | PFUNC.SITUACAOIRRF | 0-Não Calcula ou 1-Calcula |
|  | Código da coligada origem | String | 2 | 209 | PFUNC.CODCOLIGADAORIGEM |  |
|  | Chapa Origem | String | 16 | 210 | PFUNC.CHAPAORIGEM |  |
|  | Férias finalizadas para o próximo mês | Booleano | 2 | 211 | PFUNC.FERIASFINALIZADASPROXMES |  |
|  | Nº  do Cartão SUS | String | 100 | 212 | PFUNC.NUMEROCARTAOSUS |  |
|  | Tipo de redução do aviso: dias ou jornada | Inteiro | 2 | 213 | PFUNC.TIPOREDUCAOAVISO |  |
|  | Forma de redução do aviso: inicio ou fim | Inteiro | 2 | 214 | PFUNC.FORMAREDUCAOAVISO |  |
|  | Indicador de Contribuição Substituída | Inteiro | 2 | 215 | PFUNC.INDSIMPLES |  |
|  | Tipo de conta bancária | String | 1 | 216 | PFUNC.TPCONTABANCARIA |  |
|  | Preencher com o Nº  do processo judicial | String | 20 | 217 | PFUNC.NRPROCJUD |  |
|  | Indicar se a residência pertence ao trabalhador | Inteiro | 2 | 218 | PFUNC.RESIDENCIAPROPRIA |  |
|  | Indicar se foi adquirido o imóvel próprio foi adquirido com recursos do FGTS | Inteiro | 2 | 219 | PFUNC.RESIDENCIARECURSOSFGTS |  |
|  | Tipo de regime previdenciário | String | 1 | 220 | PFUNC.TPREGIMEPREV |  |
|  | Indicativo de Admissão | Inteiro | 2 | 221 | PFUNC.INDADMISSAO |  |
|  | Tipo da Reintegração | Inteiro | 2 | 222 | PFUNC.TIPOREINTEGRACAO |  |
|  | Data da Reintegração | Data | 8 | 223 | PFUNC.DATAREINTEGRACAO |  |
|  | Data do Efetivo Retorno ao Trabalho | Data | 8 | 224 | PFUNC.DATARETORNOEFETIVO |  |
|  | Nº  da Lei de Anistia | String | 20 | 225 | PFUNC.NROLEIANISTIA |  |
|  | Nº  do Processo Judicial | String | 20 | 226 | PFUNC.NROPROCESSOJUDICIAL |  |
|  | Natureza do Estágio | String | 1 | 227 | PFUNC.NATUREZAESTAGIO |  |
|  | Nível do Estágio | String | 1 | 228 | PFUNC.CODNIVELESTAGIO |  |
|  | Área de Atuação do Estagiário | String | 50 | 229 | PFUNC.AREAATUACAOESTAGIO |  |
|  | Nº  Apólice de Seguro | String | 30 | 230 | PFUNC.NUMEROAPOLICEESTAGIO |  |
|  | Data Prevista para o Término do Estágio | Data | 8 | 231 | PFUNC.DTPREVTERMINOESTAGIO |  |
|  | Código da Instituição de Ensino | String | 16 | 232 | PFUNC.CODINSTITUICAOENSINOESTAGIO |  |
|  | Código do Agente de Integração | String | 16 | 233 | PFUNC.CODAGENTEINTEGRACAOESTAGIO |  |
|  | CPF do Coordenador do Estágio | String | 11 | 234 | PFUNC.CPFCOORDENADORESTAGIO |  |
|  | Nome do Coordenador do Estágio | String | 80 | 235 | PFUNC.NOMECOORDENADORESTAGIO |  |
|  | CNPJ empresa anterior | String | 20 | 236 | PFUNC.CNPJEMPRESAANTERIOR |  |
|  | Data de Admissão do Dirigente Sindical na Empresa de Origem | Data | 8 | 237 | PFUNC.DTADMISSAOEMPRESAORIGEM |  |
|  | Matrícula do Trabalhador na Empresa de Origem | String | 30 | 238 | PFUNC.MATRICULAEMPRESAORIGEM |  |
|  | Código Correspondente à Categoria de Origem do Dirigente Sindical | Inteiro | 2 | 239 | PFUNC.CODCATEGORIAEMPRESAORIGEM |  |
|  | Motivo de Contratação do Trabalhador Temporário | Inteiro | 2 | 240 | PFUNC.MOTIVOTRABTEMP |  |
|  | Chapa do ex-funcionário que o trabalhador temporário esta substituindo | String | 16 | 241 | PFUNC.CHAPASUBSTRABTEMP |  |
|  | Motivo cancelamento do Aviso Prévio | Inteiro | 2 | 242 | PFUNC.MOTIVOCANCELAMENTOAVISO |  |
|  | Data do cancelamento do aviso prévio visando | Data | 8 | 243 | PFUNC.DTCANCELAMENTOAVISO |  |
|  | Nº  que identifica o registro do Atestado de Óbito | String | 30 | 244 | PFUNC.NROATESTADOOBITO |  |
|  | Nº  que identifica o processo trabalhista | String | 20 | 245 | PFUNC.NROPROCESSOTRAB |  |
|  | Observação sobre o desligamento do trabalhador | String | 255 | 246 | PFUNC.OBSERVACAORESCISAO |  |
|  | Observação do aviso prévio | String | 255 | 247 | PFUNC.OBSERVACAOAVISOPREVIO |  |
|  | Descrição do Salário Variável | String | 90 | 248 | PFUNC.DESCRICAOSALVARIAVEL |  |
|  | Observação cancelamento Aviso Prévio | String | 255 | 249 | PFUNC.OBSCANCELAMENTOAVISO |  |
|  | Indicativo sucessão de vínculo | Inteiro | 2 | 250 | PFUNC.SUCESSAOVINCULO |  |
|  | CNPJ da Empresa de Origem do Dirigente Sindical | String | 14 | 251 | PFUNC.CNPJEMPRESAORIGEM |  |
|  | Matrícula anterior | String | 30 | 252 | PFUNC.MATRICULAANTERIOR |  |
|  | Data início do vínculo | Data | 8 | 253 | PFUNC.DTINICIOVINCULO |  |
|  | Observação da sucessão | String | 255 | 254 | PFUNC.OBSERVACAOSUCESSAO |  |
|  | Transferência por sucessão | Inteiro | 2 | 255 | PFUNC.TRANSFERENCIASUCESSAO |  |
|  | Data do aviso trabalhado quando aviso misto | Data | 8 | 256 | PFUNC.APMISTO\_DTAVTRAB |  |
|  | Indicativo de aviso misto | Inteiro | 2 | 257 | PFUNC.APMISTO |  |
|  | Considera período de férias com dias úteis | Booleano | 2 | 258 | PFUNC.FERIASDIASUTEIS |  |
|  | Saldo de férias para o período com dias úteis | Real | 9 | 259 | PFUNC.FERIASSALDODIASUTEIS |  |
|  | ID dados do residente | Inteiro | 2 | 260 | PFUNC.IDDADOSRESID |  |
|  | Estava Recebendo Seguro Desemprego na Admissão | Inteiro | 2 | 261 | PFUNC.RECEBSEGDESEMP | 0-Não ou 1-Sim |
|  | Nº  sequencial para transferências | Inteiro | 2 | 262 | PFUNC.SEQUENCIATRANSF |  |
|  | Banco de Pagamento | String | 3 | 263 | PFUNC.CODBANCOPAGTO2 |  |
|  | Agência Banco Pagamento | String | 6 | 264 | PFUNC.CODAGENCIAPAGTO2 |  |
|  | Conta Pagamento | String | 15 | 265 | PFUNC.CONTAPAGAMENTO2 |  |
|  | Operação bancária | String | 5 | 266 | PFUNC.OPBANCARIA2 |  |
|  | Tipo de conta bancária | String | 1 | 267 | PFUNC.TPCONTABANCARIA2 |  |
|  | Indicativo de Pagamento em Juízo | Inteiro | 2 | 268 | PFUNC.INDPAGTOJUIZO |  |
|  | DIRF - Informar remuneração no Código da Receita 3533 | Inteiro | 2 | 269 | PFUNC.CODIGORECEITA3533 |  |
|  | Data do desligamento feito antes da reintegração | Data | 8 | 270 | PFUNC.DTDESLIGAMENTOREINT |  |
|  | Matrícula do trabalhador no eSocial | String | 30 | 271 | PFUNC.MATRICULAESOCIAL |  |
|  | Motivo da transferência | Inteiro | 2 | 272 | PFUNC.MOTIVOTRANSFERENCIA |  |
|  | Código do Centro de Custo | String | 25 | 273 | PFUNC.CODCCUSTO |  |
|  | Identificador do Item Contábil | Inteiro | 4 | 274 | PFUNC.IDITEMCONTABIL |  |
|  | Identificador da Classe de Valor | Inteiro | 4 | 275 | PFUNC.IDCLASSEVALOR |  |
|  | Anos de Contribuição para INSS PPE | Inteiro | 4 | 276 | PFUNC.ANOSCONTRIBINSS |  |
|  | Órgão Origem / Destino | Inteiro | 10 | 277 | PFUNC.CODORGORIDES |  |
|  | Código Tipo Regime Jurídico | String | 2 | 278 | PFUNC.CODREGJURI |  |
|  | Tipo de Regime da Jornada | Inteiro | 2 | 279 | PFUNC.TIPOREGIMEJORNADA |  |
|  | Desconta Aviso Prévio | Inteiro | 1 | 280 | PFUNC.DESCONTAAVISOPREVIO | 0-Não ou 1-Sim |
|  | Identificador da Pessoa | Inteiro | 10 | 281 | PFUNC.CODPESSOA |  |
|  | Flag Rescisão Calculada | Booleano | 2 | 282 | PFUNC.RESCISAOCALCULADA |  |
|  | Previsão de disponibilidade | Data | 8 | 283 | PFUNC.PREVDISP | Este campo deverá ficar em branco devido não ser mais utilizado. |
|  | Código do Grupo de Quiosque | String | 15 | 284 | PFUNC.CODGRPQUIOSQUE |  |
|  | Data de Vencimento do Documento de Identidade | Data | 8 | 285 | PPESSOA.DTVENCIDENTPT |  |
|  | Tipo da Rua | Inteiro | 2 | 286 | PPESSOA.CODTIPORUA |  |
|  | Tipo do Bairro | Inteiro | 2 | 287 | PPESSOA.CODTIPOBAIRRO |  |
|  | Código do Município Naturalidade | String | 20 | 288 | PPESSOA.CODNATURALIDADE |  |
|  | Nº  do registro único de cadastro | String | 20 | 289 | PPESSOA.NUMERORIC |  |
|  | Órgão emissor do registro único de cadastro | String | 20 | 290 | PPESSOA.ORGEMISSORRIC |  |
|  | Data de emissão do registro único de cadastro | Data | 8 | 291 | PPESSOA.DTEMISSAORIC |  |
|  | Data de emissão do registro único de cadastro | Data | 8 | 292 | PPESSOA.DTEMISSAOCNH |  |
|  | Órgão emissor da carteira habilitação | String | 20 | 293 | PPESSOA.ORGEMISSORCNH |  |
|  | Data de naturalização do estrangeiro no brasil | Data | 8 | 294 | PPESSOA.DATANATURALIZACAO |  |
|  | Órgão emissor do registro nacional de estrangeiros | String | 20 | 295 | PPESSOA.ORGEMISSORRNE |  |
|  | Data de emissão do registro nacional de estrangeiros | Data | 8 | 296 | PPESSOA.DTEMISSAORNE |  |
|  | Nome Social | String | 120 | 297 | PPESSOA.NOMESOCIAL |  |
|  | Código do País de Endereço | Inteiro | 2 | 298 | PPESSOA.IDPAIS |  |
|  | Deficiente intelectual | Inteiro | 2 | 299 | PPESSOA.DEFICIENTEINTELECTUAL |  |
|  | Observação deficiência | String | 255 | 300 | PPESSOA.DEFICIENTEOBSERVACAO |  |
|  | Data do Óbito | Data | 8 | 301 | PPESSOA.DATAOBITO |  |
|  | Matrícula da Certidão de Óbito | String | 50 | 302 | PPESSOA.MATRICULAOBITO |  |
|  | Falecido | Inteiro | 4 | 303 | PPESSOA.FALECIDO |  |
|  | Portaria de Naturalização | String | 50 | 304 | PPESSOA.PORTARIANATURALIZACAO |  |
|  | Classificação do Trabalhador Estrangeiro | String | 20 | 305 | PPESSOA.CODCLASSIFTRABESTRANG |  |
|  | UF de Emissão da Carteira de Motorista | String | 2 | 306 | PPESSOA.UFCNH |  |
|  | Data da Primeira Carteira de Motorista | Data | 8 | 307 | PPESSOA.DATAPRIMEIRACNH |  |
|  | Ano do Primeiro Emprego PPE | Inteiro | 4 | 308 | PPESSOA.ANO1EMPREGO |  |
|  | E-Mail pessoal | String | 60 | 309 | PPESSOA.EMAILPESSOAL |  |
|  | Identificador da Imagem | Inteiro | 4 | 310 | PPESSOA.IDIMAGEM |  |
|  | Investimento em Treinamentos Anteriores | Real | 9 | 311 | PPESSOA.INVESTTREINANT |  |
|  | FAX | String | 15 | 312 | PPESSOA.FAX |  |
|  | Código da Profissão | Inteiro | 4 | 313 | PPESSOA.CODPROFISSAO |  |
|  | Código da Ocupação | String | 3 | 314 | PPESSOA.CODOCUPACAO |  |
|  | Observações da pessoa | Memo | 16 | 315 | PPESSOA.OBSPESSOA |  |
|  | Circunscrição do Serviço Militar | String | 10 | 316 | PPESSOA.CSM |  |
|  | Data de Emissão do Certificado Militar | Data | 8 | 317 | PPESSOA.DTEXPCML |  |
|  | Órgão Expedidor do Certificado Militar | String | 10 | 318 | PPESSOA.EXPED |  |
|  | Região Militar | String | 10 | 319 | PPESSOA.RM |  |
|  | Situação Militar | String | 10 | 320 | PPESSOA.SITMILITAR |  |
|  | Data de emissão do Título de Eleitoral | Data | 8 | 321 | PPESSOA.DTTITELEITOR |  |
|  | Uf do Título Eleitoral | String | 2 | 322 | PPESSOA.ESTELEIT |  |
|  | Tipo Sanguíneo | String | 10 | 323 | PPESSOA.TIPOSANG |  |
|  | Fiador no TOTVS Incorporação | Booleano | 2 | 324 | PPESSOA.FIADOR\_SGI |  |
|  | Fiador no TOTVS Incorporação | Booleano | 2 | 325 | PPESSOA.CONJUGE\_SGI |  |
|  | Deficiente Mobilidade Reduzida | Inteiro | 1 | 326 | PPESSOA.DEFICIENTEMOBREDUZIDA |  |
|  | Contrato trabalho em regime tempo Parcial | Inteiro | 2 | 327 | PFUNC.TEMPOPARCIAL |  |
|  | Preenche Cota de PCD | Inteiro | 2 | 328 | PFUNC.COTAPCD |  |
|  | Coligada Tomador Temporário | Inteiro | 2 | 329 | PFUNC.COLTOMADORTEMP |  |
|  | Código tomador temporário | String | 25 | 330 | PFUNC.CODIGOTOMADORTEMP |  |
|  | Justificativa contrato temporário | String | 999 | 331 | PFUNC.JUSTIFICATIVATRABTEMP |  |
|  | Tipo inclusão contrato | Inteiro | 2 | 332 | PFUNC.TPINCLUSAOCONTRATO |  |
|  | CNPJ empresa sucessora | String | 20 | 333 | PFUNC.CNPJEMPRESASUCESSORA |  |
|  | Justificativa prorrogação contrato temporário | String | 999 | 334 | PFUNC.JUSTIFICATIVAPRORROGTEMP |  |
|  | Data demissão Prevista | Data | 8 | 335 | PFUNC.DTDEMISSAOPREVISTA |  |
|  | Data Aviso prévio Trabalhado | Data | 8 | 336 | PFUNC.DTAVISOPREVIOTRAB |  |
|  | Contém cláusula Asseguratória | Inteiro | 1 | 337 | PFUNC.TEMCLAUASSEG |  |
|  | CPF do Trabalhador Substituído | String | 11 | 338 | PFUNC.CPFSUBSTRABTEMP |  |
|  | Tipo Inscrição Trabalhador Substituído | Inteiro | 1 | 339 | PFUNC.TPINSCRICAOTEMP |  |
|  | Nº  Inscrição Trabalhador Substituído | String | 20 | 340 | PFUNC.NROINSCRITEMP |  |
|  | Tipo de Aviso Prévio | Inteiro | 1 | 341 | PFUNC.TIPOAVISOPREVIO |  |
|  | **Código Categoria eSocial** | **Inteiro** | **5** | **342** | **PFUNC.CODCATEGORIAESOCIAL** |  |
|  | Código do Tipo de Contrato | Inteiro | 1 | 343 | PFUNC.CODTIPOCONTRATO |  |
|  | **Data da Mudança de Salário** | **Data** | **8** | **344** | **PFHSTSAL.DTMUDANCA** |  |
|  | **Motivo da Mudança de Salário** | **String** | **2** | **345** | **PFHSTSAL.MOTIVO** |  |
|  | **Data da Mudança de Função** | **Data** | **8** | **346** | **PFHSTFCO.DTMUDANCA** |  |
|  | **Motivo da Mudança de Função** | **String** | **2** | **347** | **PFHSTFCO.MOTIVO** |  |
|  | **Data da Mudança de Situação** | **Data** | **8** | **348** | **PFHSTSIT.DATAMUDANCA** |  |
|  | **Motivo da Mudança de Situação** | **String** | **10** | **349** | **PFHSTSIT.MOTIVO** |  |
|  | **Data da Mudança de Seção** | **Data** | **8** | **350** | **PFHSTSEC.DTMUDANCA** |  |
|  | **Motivo da Mudança de Seção** | **String** | **2** | **351** | **PFHSTSEC.MOTIVO** |  |
|  | **Data da Mudança de Horário** | **Data** | **8** | **352** | **PFHSTHOR.DTMUDANCA** |  |
|  | Data da Mudança das Informações SEFIP | Data | 8 | 353 | PHSTOCORRENCIA.DTMUDANCA |  |
|  | **Data da Mudança da Contribuição Sindical** | **Data** | **8** | **354** | **PFHSTCSD.DTCONTRIBUICAO** |  |
|  | Data da Mudança dos Dados Bancários | Data | 8 | 355 | PFHSTCPGTO.DTMUDANCA |  |
|  | Data da Mudança dos Dados Bancários Alternativo | Data | 8 | 356 | PFHSTCPGTO.DTMUDANCA |  |
|  | Indicativo de função de confiança/cargo em comissão | Inteiro | 2 | 357 | PFUNC.ESOCIALFUNCAOCONF |  |
|  | Código da função de confiança/cargo em comissão | String | 10 | 358 | PFUNC.CODFUNCAOCONF |  |
|  | **Natureza da Atividade eSocial** | **Inteiro** | **1** | **359** | **PFUNC.ESOCIALNATATIVIDADE** |  |
|  | **Data Mudança do Indicador de Contribuição Substituída** | **Data** | **8** | **360** | **PFUNC.DTMUDANCAINDSIMPLES** |  |
|  | Demissão por Desempenho Insuficiente ou Inadaptação | Inteiro | 1 | 361 | PFUNC.DEMISSAODESEMPISULFINAD |  |
|  | Prefixo Período para o eSocial | String | 30 | 362 | PFUNC.PREFIXOPERIODOESOCIAL |  |
|  | Data final da quarentena | Data | 8 | 363 | PFUNC.DTFIMQUARENTENA |  |
|  | Tipo de contrato do prazo determinado | Inteiro | 1 | 364 | PFUNC.TIPOCONTPRAZODETERMINADO |  |
|  | Motivo da contratação por prazo determinado | String | 255 | 365 | PFUNC.MOTIVOCONTPRAZODETERMINADO |  |
|  | Tipo do Contrato com prazo | String | 1 | 366 | PFUNC.TIPOCONTRATOPRAZO |  |
|  | Tipo Adesão do B.E.M | String | 1 | 367 | PFUNC.TIPOADESAOBEM |  |
|  | Data da Mudança do B.E.M | Data | 8 | 368 | PFUNC.DTMUDANCABEM |  |
|  | Data do Acordo do B.E.M | Data | 8 | 369 | PFUNC.DTACORDOBEM |  |
|  | Percentual do B.E.M | Real | 6 | 370 | PFUNC.PERCENTUALREDUCAOBEM |  |
|  | Duração do Acordo do B.E.M | Inteiro | 2 | 371 | PFUNC.DURACAOBEM |  |
|  | Valor Reduzido do B.E.M | Real | 6 | 372 | PFUNC.VALORREDUZIDOBEM |  |
|  | Data de Cancelamento do BEM | Data | 8 | 373 | PFUNC.DTCANCELAMENTOBEM |  |
|  | Data de Antecipação do BEM | Data | 8 | 374 | PFUNC.DTANTECIPACAOBEM |  |
|  | Dias de prorrogação do BEM | Inteiro | 2 | 375 | PFUNC.DIASPRORROGACAOBEM |  |
|  | Não calcula recibo de férias | Inteiro | 2 | 376 | PFUNC.NAOCALCULARECIBOFERIAS |  |
|  | Data Prorrogação BEM | Data | 8 | 377 | PFUNC.DTPRORROGACAOBEM |  |
|  | CNPJ Empresa contratante Aprendiz | String | 20 | 378 | PFUNC.CNPJEMPRESACONTRATANTEAPRENDIZ |  |
|  | NRO Processo Trabalhista | string | 20 | 379 | PFUNC.NROPROCESSOTRABADMISSAO |  |
|  | Tipo de Regime Previdenciário | inteiro | 1 | 380 | PFUNC.TIPOREGPREVDIRIGENTESINDICAL |  |
|  | Tipo de Registro Trabalhista | inteiro | 1 | 381 | PFUNC.TIPOREGTRABDIRIGENTESINDICAL |  |
|  | Prazo de Residência Indeterminado | string | 1 | 382 | PPESSOA.TIPOPRAZORESIDENCIA |  |
|  | Categoria de origem do trabalhador | inteiro | 5 | 383 | PFUNC.CODCATEGORIATRABCEDIDO |  |
|  | CNPJ da empresa cedente | string | 18 | 384 | PFUNC.CNPJCEDENTE |  |
|  | Data admissão do trabalhador no empregador de origem (Cedente) | data | 8 | 385 | PFUNC.DATAADMISSAOCEDENTE |  |
|  | Ônus da cessão/requisição | string | 1 | 386 | PFUNC.INFOONUSCESSAO |  |
|  | Matricula do Trabalhador no Empregador de Origem (Cedente) | string | 30 | 387 | PFUNC.MATRICULACEDENTE |  |
|  | Tipo de regime previdenciário  do trabalhador cedido | string | 1 | 388 | PFUNC.TIPOREGIMEPREVIDENCIARIOCEDIDO |  |
|  | Tipo de regime trabalhista  do trabalhador cedido | string | 1 | 389 | PFUNC.TIPOREGIMETRABALHISTACEDIDO |  |
|  | Beneficiário | Inteiro | 1 | 390 | PFUNC.BENEFICIARIO |  |
|  | Informa se o beneficiário é pessoa com doença incapacitante | Inteiro | 1 | 391 | PFUNC.BENEFICIARIOINCAPAZ |  |
|  | CNPJ do responsável pela matrícula do servidor/militar | string | 20 | 392 | PFUNC.CNPJRESPONSAVELMATRICULA |  |
|  | Data do reconhecimento da incapacidade | Data | 8 | 393 | PFUNC.DATAINCAPACIDADE |  |
|  | Data de inicio do cadastro do beneficiário | Data | 8 | 394 | PFUNC.DATAINICIOBENEFICIARIO |  |
|  | Matrícula do beneficiário | string | 30 | 395 | PFUNC.MATRICULABENEFICIARIO |  |
|  | Função/Emprego/Cargo Acumulável | inteiro | 1 | 396 | PFUNC.FUNCAOACUMULAVEL |  |
|  | Tipo de provimento estatutário | Inteiro | 1 | 397 | PFUNC.TIPOPROVIMENTO |  |
|  | Data em exercício estatutário | Data | 8 | 398 | PFUNC.DTEXERCICIO |  |
|  | Tipo de plano de segregação da massa do estatutário | Inteiro | 1 | 399 | PFUNC.TIPOPLANOSEGREGACAOMASSA |  |
|  | Sujeito ao teto do RGPS estatutário | Inteiro | 1 | 400 | PFUNC.TETORGPS |  |
|  | Recebe abono permanência estatutário | Inteiro | 1 | 401 | PFUNC.ABONOPERMANENCIA |  |
|  | Data de início do abono permanência estatutário | Data | 8 | 402 | PFUNC.DTINICIOABONO |  |
|  | Indicar se o servidor optou pela remuneração do cargo efetivo | Inteiro | 1 | 403 | PFUNC.INDICATIVOREMUNERACAOCARGO |  |
|  | Tipo de regime trabalhista para servidor público com mandato eletivo | Inteiro | 1 | 404 | PFUNC.TIPOREGTRABMANDATOELETIVO |  |
|  | Tipo de regime previdenciário para servidor público com mandato eletivo | Inteiro | 1 | 405 | PFUNC.TIPOREGPREVMANDATOELETIVO |  |
|  | Data mudança do estatutário | Data | 8 | 406 | PFHSTESTATUTARIO.DTMUDANCA |  |
|  | CNPJ do orgão público de origem com mandato eletivo | String | 20 | 407 | PFUNC.CNPJMANDATOELETIVO |  |
|  | Código  da categoria de origem do servidor público com mandato eletivo | Inteiro | 3 | 408 | PFUNC.CODCATEGORIAMANDATOELETIVO |  |
|  | Data de exercício do servidor no órgão público de origem com mandato eletivo | Data | 8 | 409 | PFUNC.DTEXERCICIOMANDATOELETIVO |  |
|  | Matrícula do servidor no órgão público de origem com mandato eletivo | String | 30 | 410 | PFUNC.MATRICULAMANDATOELETIVO |  |
|  | Tipo de regime trabalhista do funcionário | Inteiro | 1 | 411 | PFUNC.TIPOREGIMETRABALHISTA |  |
|  | Indicativo de Situação de Remuneração Após o Desligamento | Inteiro | 1 | 412 | PFUNC.INDSITREMUNAPOSDESLIG |  |
|  | Desconsiderar Desconto Simplificado do IRRF | Inteiro | 1 | 413 | PFUNC.DESCONSIDERARIRRFSIMPLIFICADO |  |
|  | Data de Desligamento Judicial | Data | 8 | 414 | PFUNC.DTDESLIGAMENTOJUDICIAL |  |
|  | Indica adesão ao Programa de Demissão Voluntária (PDV) | Inteiro | 1 | 415 | PFUNC.ADESAOPDV |  |
|  | Modalidade de Contratação | Inteiro | 1 | 416 | PFUNC.MODALIDADECONTRATACAO |  |
|  | Inscrição Estabelecimento Atividades Práticas | String | 20 | 417 | PFUNC.INSCESTABELECIMENTOATIVPRATICA |  |
|  | Funcionário Utiliza Ponto Web (Ahgora) | Inteiro | 1 | 418 | PFUNC.UTILIZAPONTOAHGORA | 0-Não ou 1-Sim |

## **OBSERVAÇÃO:**

* ## Na versão 2306 será considerado até o campo 413
* ## Na versão 2310 será considerado até o campo 417
* ## Na versão 2402 e superiores será considerado até o campo 418

|  |  |
| --- | --- |
|  | Informações Complementares |

* [Opções sobrescrever na importação de Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=553900870)
