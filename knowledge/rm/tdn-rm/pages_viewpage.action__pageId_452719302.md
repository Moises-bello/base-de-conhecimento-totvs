---
content_hash: 06b58eddabeaea858a222e3a7d46dd4058cb58417f2756a548b475ed3d24389c
fetched_at: '2026-06-29T00:10:05.790878+00:00'
page_id: '452719302'
product: rm
source: tdn-rm
title: Layout Para Importação de Seções (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719302
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de Seções da base de origem:  
- GCALEND   
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo**Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.  
 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código identificador da seção** | **String** | **35** | **1** | **PSECAO.CODIGO** |
| **Descrição da seção** | **String** | **60** | **2** | **PSECAO.DESCRICAO** |
| CGC | String | 20 | 3 | PSECAO.CGC |
| CGC anterior | String | 20 | 4 | PSECAO.CGCANTERIOR |
| CEI (CGC provisório) | String | 20 | 5 | PSECAO.CEI |
| N. da atividade da empresa no INSS | String | 3 | 6 | PSECAO.FPAS |
| Seguro de acidentes de trabalho | String | 12 | 7 | PSECAO.SAT |
| Ramo de atividade econômica | String | 7 | 8 | PSECAO.ATIVECONOMICA |
| Inscrição estadual | String | 15 | 9 | PSECAO.INSCRESTADUAL |
| Inscrição municipal | String | 15 | 10 | PSECAO.INSCRMUNICIPAL |
| Rua | String | 100 | 11 | PSECAO.RUA |
| Número | String | 8 | 12 | PSECAO.NUMERO |
| Complemento |  | 60 | 13 | PSECAO.COMPLEMENTO |
| Bairro |  | 80 | 14 | PSECAO.BAIRRO |
| Unidade da federação | String | 2 | 15 | PSECAO.ESTADO |
| Cidade |  | 32 | 16 | PSECAO.CIDADE |
| CEP |  | 9 | 17 | PSECAO.CEP |
| Nome do país | String | 16 | 18 | PSECAO.PAIS |
| Telefone da seção | String | 15 | 19 | PSECAO.TELEFONE |
| Código da Caixa Econom. Federal | String | 14 | 20 | PSECAO.CODIGOCEF |
| Número de não empregados proprietários | Inteiro | 2 | 21 | PSECAO.NAOEMPREGPROPR |
| Prefixo de inscrição na RAIS | String | 2 | 22 | PSECAO.PREFIXORAIS |
| Código para Categoria (FGTS) | String | 2 | 23 | PSECAO.CATEGORIA |
| Integração contábil | String | 22 | 24 | PSECAO.INTEGRCONTABIL |
| Integração gerencial | String | 22 | 25 | PSECAO.INTEGRGERENCIAL |
| Número da filial | Inteiro | 4 | 26 | PSECAO.NROFILIALCONT |
| Número do centro de custo | String | 25 | 27 | PSECAO.NROCENCUSTOCONT |
| Código de terc. para guia INSS | String | 4 | 28 | PSECAO.CODTERCEIROSINSS |
| Percentual de terceiros | Real | 9 | 29 | PSECAO.PERCENTTERCEIROS |
| Percentual de acidente de trabalho | Real | 9 | 30 | PSECAO.PERCENTACIDTRAB |
| Faturamento bruto | Real | 9 | 31 | PSECAO.FATURAMENTOBRUTO |
| Valor do frete | Real | 9 | 32 | PSECAO.VALORFRETE |
| Informações para GRPS - 1 | String | 58 | 33 | PSECAO.COMPLEMENTOGRPS1 |
| Informações para GRPS - 2 | String | 58 | 34 | PSECAO.COMPLEMENTOGRPS2 |
| Informações para GRPS - 3 | String | 58 | 35 | PSECAO.COMPLEMENTOGRPS3 |
| Código de unidade de entrega | String | 6 | 36 | PSECAO.CODUNIDENTREGA |
| Pessoa para contato | String | 20 | 37 | PSECAO.CONTATO |
| Ramal | String | 4 | 38 | PSECAO.RAMAL |
| Cód. do departamento - VT Ticket | String | 6 | 39 | PSECAO.VTCODDEPTO |
| Início do 1. período de rec. próprio | Inteiro | 2 | 40 | PSECAO.INIPERRECPROPR1 |
| Fim 1. período de recolhimento próprio | Inteiro | 2 | 41 | PSECAO.FIMPERRECPROPR1 |
| Eventos pagos até 5. dia útil | Booleano | 2 | 42 | PSECAO.PROPRANTES5DIA1 |
| Início do 2. período de rec. próprio | Inteiro | 2 | 43 | PSECAO.INIPERRECPROPR2 |
| Fim 2. período de recolhimento próprio | Inteiro | 2 | 44 | PSECAO.FIMPERRECPROPR2 |
| Eventos pagos até 5. dia útil - 2 | Booleano | 2 | 45 | PSECAO.PROPRANTES5DIA2 |
| Início do 1. período de rec. centr. | Inteiro | 2 | 46 | PSECAO.INIPERRECCENTR1 |
| Fim 1. período de rec. centralizado | Inteiro | 2 | 47 | PSECAO.FIMPERRECCENTR1 |
| Rec. centr. de even. até 5. dia útil | Booleano | 2 | 48 | PSECAO.CENTRANTES5DIA1 |
| Início do 2. período de rec. centr. | Inteiro | 2 | 49 | PSECAO.INIPERRECCENTR2 |
| Fim 2. período de rec. centralizado | Inteiro | 2 | 50 | PSECAO.FIMPERRECCENTR2 |
| Rec. centr. de even. até 5. dia útil - 2 | Booleano | 2 | 51 | PSECAO.CENTRANTES5DIA2 |
| Nome da seção centralizadora | String | 35 | 52 | PSECAO.SECAOCENTRALIZ |
| Contribuição para SESI/SENAI | Booleano | 2 | 53 | PSECAO.CONTRIBSESIESENAI |
| Distribuidora petrolífera | Booleano | 2 | 54 | PSECAO.DISTRIBPETROLEO |
| Pessoa física | Booleano | 2 | 55 | PSECAO.PESSOAFISICA |
| Indicativo de seção desativada | Booleano | 2 | 56 | PSECAO.SECAODESATIVADA |
| Indicativo de identificação do CGC | Booleano | 2 | 57 | PSECAO.IDENTIFICACAOCGC |
| Indicativo de alteratpo de endereto | Booleano | 2 | 58 | PSECAO.ENDERECOALTEROU |
| End. para pagamento - VT Ticket | String | 48 | 59 | PSECAO.ENDERECOPAGTO |
| Identificação de pedido - VT Ticket | Inteiro | 2 | 60 | PSECAO.VTIDENTPEDIDO |
| Identificação personalizada - VT Ticket | Inteiro | 2 | 61 | PSECAO.VTIDENTPERSONAL |
| Cód. do cliente - VT Ticket | String | 6 | 62 | PSECAO.VTCODCLIENTE |
| Cód. do local - VT Ticket | String | 10 | 63 | PSECAO.VTCODLOCAL |
| Cód. da seção para fat. - VT Ticket | String | 35 | 64 | PSECAO.VTCODSECFATURAM |
| Cód. da seção para pedido - VT Ticket | String | 35 | 65 | PSECAO.VTCODSECPEDIDO |
| Cód. da seção para cobrança - VT Ticket | String | 35 | 66 | PSECAO.VTCODSECCOBRANCA |
| Cód. da seção para entrega - VT Ticket | String | 35 | 67 | PSECAO.VTCODSECENTREGA |
| Cód. do centro de custo - VT Ticket | String | 35 | 68 | PSECAO.VTCODCENTROCUSTO |
| Causa da mudança de CGC | Inteiro | 2 | 69 | PSECAO.CAUSAMUDANCACGC |
| Código do município | String | 7 | 70 | PSECAO.CODMUNICIPIO |
| Data base | Inteiro | 2 | 71 | PSECAO.MESDATABASE |
| Natureza jurídica | String | 4 | 72 | PSECAO.NATUREZAJURIDICA |
| Código de calendário | String | 16 | 73 | PSECAO.CODCALENDARIO |
| Prefixo de inscrição no FGTS | String | 2 | 74 | PSECAO.PREFIXOINSCRFGTS |
| Primeira Declaração de CAGED | Inteiro | 2 | 75 | PSECAO.PRIMEIRADECLCAGED |
| Alteração do CAGED | Inteiro | 2 | 76 | PSECAO.ALTERACAOCAGED |
| **Código identificador da filial** | **Inteiro** | **4** | **77** | **PSECAO.CODFILIAL** |
| **Código identificador do departamento** | **Inteiro** | **25** | **78** | **PSECAO.CODDEPTO** |
| Limite de Funcionários | Inteiro | 4 | 79 | PSECAO.LIMITEFUNC |
| Opta pelo SIMPLES | Inteiro | 2 | 80 | PSECAO.OPTASIMPLES |
| Alterou o CNAE | Booleano | 2 | 81 | PSECAO.MUDOUCNAE |
| Funcionário responsável pela seção |  | 16 | 82 | PSECAO.CHAPACHEFE |
| Percentual de aposentadoria 15 anos | Inteiro | 2 | 83 | PSECAO.PERCENT15ANOSGRPS |
| Percentual de aposentadoria 20 anos | Inteiro | 2 | 84 | PSECAO.PERCENT20ANOSGRPS |
| Percentual de aposentadoria 25 anos | Inteiro | 2 | 85 | PSECAO.PERCENT25ANOSGRPS |
| DDD da seção | String | 4 | 86 | PSECAO.DDD |
| Código de Pagamento GPS | String | 5 | 87 | PSECAO.CODPAGTOGPS |
| Porte da empresa | Inteiro | 2 | 88 | PSECAO.PORTEEMPRESA |
| Percentual de Isenção de Filantropia | Real | 9 | 89 | PSECAO.PERCISENCAOFILANTROPIA |
| Flag empresa participa PAT | Inteiro | 2 | 90 | PSECAO.PARTICIPAPAT |
| Código do departamento para contabilização | String | 25 | 91 | PSECAO.CODDEPTOCONT |
| Isenta de contribuição social | Booleano | 2 | 92 | PSECAO.ISENTOCONTRIBSOCIAL |
| Vínculos Particip PAT acima de 5 Sal.Min | Inteiro | 4 | 93 | PSECAO.VINCPATMAIOR5SAL |
| Vínculos Participantes PAT até 5 Sal.Min | Inteiro | 4 | 94 | PSECAO.VINCPAT5SAL |
| Porcentagem Administração Cozinha | Inteiro | 2 | 95 | PSECAO.PORCADMCOZINHA |
| Porcentagem Alimentação Convênio | Inteiro | 2 | 96 | PSECAO.PORCALIMCONVENIO |
| Porcentagem Cesta Alimento | Inteiro | 2 | 97 | PSECAO.PORCCESTAALIMENTO |
| Porcentagem Refeição Convênio | Inteiro | 2 | 98 | PSECAO.PORCREFEICAOCONV |
| Porcentagem Refeição Transportada | Inteiro | 2 | 99 | PSECAO.PORCREFEICAOTRANSP |
| Porcentagem serviços próprio | Inteiro | 2 | 100 | PSECAO.PORCSERVPROP |
| Data de Encerramento das Atividades | Data | 8 | 101 | PSECAO.DTENCERRATIV |
|  |  |  | 102 |  |
| Localidade | String | 40 | 103 | PSECAO.LOCALIDADE |
| Email | String | 45 | 104 | PSECAO.EMAIL |
| Capital Social do Estabelecimento | Real | 9 | 105 | PSECAO.CAPITALSOCESTAB |
| Capital Social da Empresa | Real | 9 | 106 | PSECAO.CAPITALSOCEMP |
| Código Pgto GPS Somente Terceiros | String | 5 | 107 | PSECAO.CODPAGTOGPSTERCEIROS |
| Encerramento | Inteiro | 2 | 108 | PSECAO.ENCERRAMENTO |
| Valor Verba Q.Vagas | Real | 9 | 109 | PSECAO.VERBAQUADROVAGAS |
| Percentual Verba Q.Vagas | Real | 9 | 110 | PSECAO.PERCQUADROVAGAS |
| Código da tabela | String | 10 | 111 | PSECAO.CODTABELA |
| Ramo de Ativ Econômica(para uso na RAIS) | String | 5 | 112 | PSECAO.CNAERAIS |
| INSS acumulado se tot.GPS < R$29,00 | Real | 9 | 113 | PSECAO.VALORINSSACUMULADO |
| Outras Ent.acumulado se tot.GPS<R$29,00 | Real | 9 | 114 | PSECAO.VALORENTIDADESACUMULADO |
| Código da seção pai | String | 35 | 115 | PSECAO.CODIGOPAI |
| Nro pontos disponíveis para a seção. | Inteiro | 4 | 116 | PSECAO.BENEFPONTOS |
| Tipo da Lotação | String | 2 | 117 | PSECAO.TPLOTACAO |
| Cadastro Nacional de Obra | String | 20 | 118 | PSECAO.CNO |
| Tipo de Logradouro | Inteiro | 2 | 119 | PSECAO.CODTIPORUA |
| Cadastro de Atividades da Pessoa Física | String | 20 | 120 | PSECAO.CAEPF |
| Tipo de controle de ponto | Inteiro | 2 | 121 | PSECAO.TIPOCONTROLEPONTO |
| Código da seção para alocação de autônomos (RPA) | String | 35 | 122 | PSECAO.SECAOAUTONOMOS |
| Tipo para tarefa agrária | Inteiro | 4 | 123 | PSECAO.TIPOTAREFA |
| Tipo do processo que justifica alteração de alíquota de rateio para Estabelecimentos e Obras | String | 1 | 124 | PSECAO.TPPROCESSORAT |
| Número do processo que justifica alteração de alíquota de rateio para Estabelecimentos e Obras | String | 30 | 125 | PSECAO.NRPROCESSORAT |
| Tipo de processo que justifica alteração na alíquota FAP para Estabelecimentos e Obras | String | 1 | 126 | PSECAO.TPPROCESSOFAP |
| Número do processo que justifica alteração na alíquota FAP para Estabelecimentos e Obras | String | 30 | 127 | PSECAO.NRPROCESSOFAP |
| Identificador do Item Contábil | Inteiro | 4 | 128 | PSECAO.IDITEMCONTABIL |
| Identificador da Classe de Valor | Inteiro | 4 | 129 | PSECAO.IDCLASSEVALOR |
| Área de Atuação | String | 1 | 130 | PSECAO.CODAREAATUACAO |
| Contratação de Aprendiz | Inteiro | 1 | 131 | PSECAO.CONTAPR |
| Número processo | String | 1 | 132 | PSECAO.NRPROCJUDAPR |
| Contrata aprendiz por intermédio de entidade educativa | Inteiro | 1 | 133 | PSECAO.CONTENTEDAPR |
| Contratação de pessoa com deficiência | Inteiro | 1 | 134 | PSECAO.CONTPCD |
| Número processo | String | 20 | 135 | PSECAO.NRPROCJUDPCD |
| Cód. Suspenão | String | 14 | 136 | PSECAO.CODSUSPPROCJUDRAT |
| Cód. Suspenão | String | 14 | 137 | PSECAO.CODSUSPPROCJUDFAP |
| Tipo de Processo | String | 1 | 138 | PSECAO.TPPROCJUDAPR |
| Código do Indicativo da Suspensão (APR) | String | 14 | 139 | PSECAO.CODSUSPPROCJUDAPR |
| Tipo de Processo | String | 1 | 140 | PSECAO.TPPROCJUDPCD |
| Código do Indicativo da Suspensão (APR) | String | 14 | 141 | PSECAO.CODSUSPPROCJUDPCD |
| Código Terceiros para os quais o recolhimento está suspenso | String | 4 | 142 | PSECAO.CODTERCSSUSP |
| Alíquota RAT para atividade (CNAE) preponderante | Real | 9 | 143 | PSECAO.ALIQRATISENTO |
| Tipo de CAEPF | Inteiro | 2 | 144 | PSECAO.TIPOCAEPF |
| CNAE Preponderante | String | 7 | 145 | PSECAO.CNAEPREPONDERANTE |
