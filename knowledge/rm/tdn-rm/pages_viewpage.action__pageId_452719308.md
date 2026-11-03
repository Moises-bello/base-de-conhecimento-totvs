---
content_hash: f62792dd82e45bc7bf3eca987cd56425ec9dbb9d841876599a4aaf64cb8c1f14
fetched_at: '2026-06-29T00:10:06.044316+00:00'
page_id: '452719308'
product: rm
source: tdn-rm
title: Layout Para Importação de Eventos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719308
version: 24
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Funções da base de origem:  
- PCODTOTALIZ  
- CHISTP  
**Observação**; Alguns campos podem ser zerados dependendo da Regra de Negocio.  
   
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
| **Código Identificador do Evento** | **String** | **4** | **1** | **PEVENTO.CODIGO** |
| **Descrição do Evento** | **String** | **80** | **2** | **PEVENTO.DESCRICAO** |
| Totalizador do Evento | String | 2 | 3 | PEVENTO.TOTALIZADOR |
| Indicador de Estado do Evento | String | 1 | 4 | PEVENTO.CHAVE |
| Indicativo de Composição de Comissão | Inteiro | 2 | 5 | PEVENTO.COMPOECOMISSAO |
| **Provento/Desconto** | **String** | **1** | **6** | **PEVENTO.PROVDESCBASE** |
| **Valor/Hora/Dia/Referência** | **String** | **1** | **7** | **PEVENTO.VALHORDIAREF** |
| Porcentagem de Incidência | Real | 9 | 8 | PEVENTO.PORCINCID |
| **Código de Cálculo** | **Inteiro** | **2** | **9** | **PEVENTO.CODIGOCALCULO** |
| Prioridade do Evento | Inteiro | 2 | 10 | PEVENTO.PRIORIDADE |
| Código da Fórmula de Valor | String | 8 | 11 | PEVENTO.FORMULAVALOR |
| Código da Fórmula de Hora | String | 8 | 12 | PEVENTO.FORMULAHORA |
| Código da Fórmula de Referência | String | 8 | 13 | PEVENTO.FORMULAREF |
| Código da Fórmula de Crédito | String | 8 | 14 | PEVENTO.FORMULACRITICA |
| Incidência de Inss | Booleano | 2 | 15 | PEVENTO.INCINSS |
| Incidência de Irrf | Booleano | 2 | 16 | PEVENTO.INCIRRF |
| Incidência de Fgts | Booleano | 2 | 17 | PEVENTO.INCFGTS |
| Incidência de Rais | Booleano | 2 | 18 | PEVENTO.INCRAIS |
| Incidência no Informe de Rendimentos | Booleano | 2 | 19 | PEVENTO.INCINFREND |
| Incidência do Dsr | Booleano | 2 | 20 | PEVENTO.INCDSR |
| Incidência em Vale-Transporte | Booleano | 2 | 21 | PEVENTO.INCVALETRANSP |
| Incidência de Irrf nas Férias | Booleano | 2 | 22 | PEVENTO.INCIRRFFERIAS |
| Incidência no Terço de Férias | Booleano | 2 | 23 | PEVENTO.INCTERCOFERIAS |
| Incidência em Salário-Família | Booleano | 2 | 24 | PEVENTO.INCSALFAMILIA |
| Incidência de Inss no 13. Salário | Booleano | 2 | 25 | PEVENTO.INCINSS13 |
| Incidência de Irrf no 13. Salário | Booleano | 2 | 26 | PEVENTO.INCIRRF13 |
| Incremento de Acumuladores | String | 100 | 27 | PEVENTO.INCACUMULADOR |
| Incidência de Salário | Booleano | 2 | 28 | PEVENTO.INCSALARIO |
| Prop. de Acordo com a Admissão | Booleano | 2 | 29 | PEVENTO.PROPORCADMISSAO |
| Proporcionalizar de Acordo com a Licença | Booleano | 2 | 30 | PEVENTO.PROPORCLICENCA |
| Proporcionalizar de Acordo com as Férias | Booleano | 2 | 31 | PEVENTO.PROPORCFERIAS |
| Dedutível de Irrf | Booleano | 2 | 32 | PEVENTO.DEDUTIVELIRRF |
| Estorna Somente em Irrf de Férias | Booleano | 2 | 33 | PEVENTO.ESTIRRFFERIAS |
| Indicativo de Est. de Base de Sal. Fam. | Booleano | 2 | 34 | PEVENTO.ESTCALCSALFAM |
| Indicativo de Est da Base de Vale-Transp | Booleano | 2 | 35 | PEVENTO.ESTCALCVALETR |
| Indicativo de Est.De Inss no 13. Sal. | Booleano | 2 | 36 | PEVENTO.ESTINSS13 |
| Grupo Aas | Inteiro | 2 | 37 | PEVENTO.GRUPOAAS |
| Indicativo de Evento a Lançar | String | 4 | 38 | PEVENTO.EVTALANCAR |
| Número da Conta para Crédito | String | 22 | 39 | PEVENTO.CONTACREDITO |
| Número da Conta para Débito | String | 22 | 40 | PEVENTO.CONTADEBITO |
| Número do Histórico Padrão | String | 10 | 41 | PEVENTO.NROHISTPADRAO |
| Complemento do Histórico | String | 60 | 42 | PEVENTO.COMPLHISTORICO |
| No Conta Gerencial para Crédito | String | 22 | 43 | PEVENTO.CGCREDITO |
| No Conta Gerencial para Débito | String | 22 | 44 | PEVENTO.CGDEBITO |
| Evento de Diferença de Salário | String | 4 | 45 | PEVENTO.CODEVENTODIF |
| Código do Rateio que o Evento Segue | String | 8 | 46 | PEVENTO.CODRATEIO |
| Sal.Composto Base de Calc. do Evento | String | 16 | 47 | PEVENTO.BASESALCOMPOSTO |
| Se o Evento Será Descont.No Mês Seguinte | Booleano | 2 | 48 | PEVENTO.DESCONTOPERDOADO |
| Segue Rateio de Tomador de Serviço | Booleano | 2 | 49 | PEVENTO.PROPPORTOMADOR |
| Indic. de Evento para Pag. Obrigatório | Booleano | 2 | 50 | PEVENTO.PAGOBRIGATORIO |
| Existe Intgr Contábil Conta Crédito | Booleano | 2 | 51 | PEVENTO.TEMINTCONTCC |
| Existe Intgr Contábil Conta Dédito | Booleano | 2 | 52 | PEVENTO.TEMINTCONTCD |
| Existe Intgr Contábil Conta Ger Crédito | Booleano | 2 | 53 | PEVENTO.TEMINTCONTGC |
| Existe Intgr Contábil Conta Ger Dédito | Booleano | 2 | 54 | PEVENTO.TEMINTCONTGD |
| Existe Intgr Func Contab Conta Crédito | Booleano | 2 | 55 | PEVENTO.TEMINTFUNCCC |
| Existe Intgr Func Contab Conta Dédito | Booleano | 2 | 56 | PEVENTO.TEMINTFUNCCD |
| Existe Intgr Func Ger Conta Crédito | Booleano | 2 | 57 | PEVENTO.TEMINTFUNCGC |
| Existe Intgr Func Ger Conta Débito | Booleano | 2 | 58 | PEVENTO.TEMINTFUNCGD |
| Indicativo para Contab. Parcial | Booleano | 2 | 59 | PEVENTO.CONTPARCIAL |
| Evento Incide em Adic. Substituição | Booleano | 2 | 60 | PEVENTO.INCSUBSTITUICAO |
| Indicativo de Est. da Base de Fgts 13O. | Booleano | 2 | 61 | PEVENTO.ESTFGTS13 |
| Indicativo de Est. da Base de Irrf 13O. | Booleano | 2 | 62 | PEVENTO.ESTIRRF13 |
| Evento de Insuficiência de Saldos | String | 4 | 63 | PEVENTO.CODEVENTOINSUF |
| Evento incide em pensão | Inteiro | 2 | 64 | PEVENTO.INCPENSAO |
| Evento incide em pensão de férias | Inteiro | 2 | 65 | PEVENTO.INCPENSAOFERIAS |
| Evento incide em pensão de 13º salário | Inteiro | 2 | 66 | PEVENTO.INCPENSAO13SAL |
| Evento incide em pensão de part. Lucros | Inteiro | 2 | 67 | PEVENTO.INCPENSAOPARTICIP |
| Fórmula para compor Compl. Histórico | String | 8 | 68 | PEVENTO.FORMCOMPLHIST |
| Período de cálculo do rateio de eventos | Inteiro | 2 | 69 | PEVENTO.PERCALCRATEIO |
| Estorna FGTS | Inteiro | 2 | 70 | PEVENTO.ESTFGTS |
| Estorna INSS | Inteiro | 2 | 71 | PEVENTO.ESTINSS |
| Estorna IRRF | Inteiro | 2 | 72 | PEVENTO.ESTIRRF |
| Incide FGTS 13 | Inteiro | 2 | 73 | PEVENTO.INCFGTS13 |
| Proporcionalizar de acordo com demissão. | Booleano | 2 | 74 | PEVENTO.PROPORCDEMISSAO |
| **Exibir Evento na Entrada de Mov. via Web** | **Booleano** | **2** | **75** | **PEVENTO.EVENTOEXIBIDOENTRADADADOSWEB** |
| Código do centro de custo do evento | String | 25 | 76 | PEVENTO.CCUSTO |
| Codigo de rubrica | String | 3 | 77 | PEVENTO.CODRUBRICA |
| Conteúdo do memo (começa com /@ e termina com @/) | Memo | 16 | 78 | PMEMO.VALMEMO |
| Indicativo de Evento Inativo | Inteiro | 2 | 79 | PEVENTO.INATIVO |
| Indicativo de Estorno da Base de Cálculo | Booleano | 2 | 80 | PEVENTO.ESTCALCULO |
| Indicativo de Estorno da Base de Férias | Booleano | 2 | 81 | PEVENTO.ESTCALCFERIAS |
| Identificador do memo | Inteiro | 4 | 82 | PEVENTO.IDANOTACAO |
| Segue rateio de salário composto | Booleano | 2 | 83 | PEVENTO.SEGUERATEIOSALCMP |
| Conta Reversão | String | 20 | 84 | PEVENTO.CONTAREVERSAO |
| Fórmula para evento relacionado. | String | 8 | 85 | PEVENTO.FORMULAEVTRELAC |
| Remunerações Quadro de Pessoal | String | 1 | 86 | PEVENTO.QUADROREM |
| Ordem cálculo dentro de uma prioridade | Inteiro | 4 | 87 | PEVENTO.ORDEMCALCULO |
| Evento dedutível em IRRF de 13o | Booleano | 2 | 88 | PEVENTO.DEDUTIVELIRRF13 |
| Evento dedutível em IRRF de férias | Booleano | 2 | 89 | PEVENTO.DEDUTIVELIRRFFERIAS |
| Segue rateio do movimento de ensino | Booleano | 2 | 90 | PEVENTO.SEGUERATEIOMOVENSINO |
| Natureza da rubrica | String | 4 | 91 | PEVENTO.NATRUBRICA |
| Incidência de INSS suspensa em decorrência de decisão judicial (campo descontinuado e substituido para o campo 136 INCINSSSUSPENSAO) | Inteiro | 2 | 92 | PEVENTO.INCINSSSUSPENSA |
| Incidência de IRRF suspensa em decorrência de decisão judicial (campo descontinuado e substituido para o campo 137 INCIRRFSUSPENSAO) | Inteiro | 2 | 93 | PEVENTO.INCIRRFSUSPENSA |
| Incidência de FGTS suspensa em decorrência de decisão judicial  (Valores válidos : 1, 2, 3) | Inteiro | 2 | 94 | PEVENTO.INCFGTSSUSPENSA |
| Número do Processo Administrativo/Judicial | String | 20 | 95 | PEVENTO.NRPROCESSOINSS |
| Código Correspondente ao Tipo de Processo (A - Administrativo, J - Judicial) | String | 1 | 96 | PEVENTO.TPPROCESSOINSS |
| Extensão da Decisão/Sentença | Inteiro | 2 | 97 | PEVENTO.EXTDECISAOINSS |
| Número do Processo Administrativo/Judicial | String | 20 | 98 | PEVENTO.NRPROCESSOIRRF |
| Código Correspondente ao Tipo de Processo (A - Administrativo, J - Judicial) | String | 1 | 99 | PEVENTO.TPPROCESSOIRRF |
| Número do Processo Administrativo/Judicial | String | 20 | 100 | PEVENTO.NRPROCESSOFGTS |
| Código Correspondente ao Tipo de Processo (A - Administrativo, J - Judicial) | String | 1 | 101 | PEVENTO.TPPROCESSOFGTS |
| Incidência de Contribuição Sindical Suspensa | Inteiro | 2 | 102 | PEVENTO.INCSINDSUSPENSA |
| Número do Processo Administrativo/Judicial | String | 20 | 103 | PEVENTO.NRPROCESSOSIND |
| Código Correspondente ao Tipo de Processo (A - Administrativo, J - Judicial) | String | 1 | 104 | PEVENTO.TPPROCESSOSIND |
| Incidência de Salário Maternidade Suspensa | Inteiro | 2 | 105 | PEVENTO.INCSALMATERNSUSPENSA |
| Número do Processo Administrativo/Judicial | String | 20 | 106 | PEVENTO.NRPROCESSOSALMATERN |
| Código Correspondente ao Tipo de Processo (A - Administrativo, J - Judicial) | String | 1 | 107 | PEVENTO.TPPROCESSOSALMATERN |
| Incide no Custo do funcionário | Inteiro | 2 | 108 | PEVENTO.INCIDECUSTOFUNCIONARIO |
| Identificador do Item Contábil | Inteiro | 4 | 109 | PEVENTO.IDITEMCONTABIL |
| Identificador da Classe de Valor | Inteiro | 4 | 110 | PEVENTO.IDCLASSEVALOR |
| Tipo de Benefício PPE | String | 1 | 111 | PEVENTO.CODTPBENEFICIO |
| Tipo de Desconto PPE | String | 2 | 112 | PEVENTO.CODTPDESCONTO |
| Incidência de PIS | Booleano | 2 | 113 | PEVENTO.INCPIS |
| Estorna PIS | Booleano | 2 | 114 | PEVENTO.ESTPIS |
| Compõe Remuneração Base de Professor | Booleano | 2 | 115 | PEVENTO.COMPOEREMBASE |
| Rendimento não tributável em função de acordos internacionais de bitributação | Booleano | 2 | 116 | PEVENTO.RENDNAOTRIBACORDOINTERNAC |
| Não é base de cálculo em função de acordos internacionais de previdência social | Booleano | 2 | 117 | PEVENTO.NAOEBASECALCACORDOINTERNAC |
| Incidência de INSS 13º suspensa em decorrência de decisão judicial (campo descontinuado e substituido para o campo 136 INCINSSSUSPENSAO) | Inteiro | 2 | 118 | PEVENTO.INCINSS13SUSPENSA |
| Incidência de IRRF 13º suspensa em decorrência de decisão judicial (campo descontinuado e substituido para o campo 137 INCIRRFSUSPENSAO) | Inteiro | 2 | 119 | PEVENTO. INCIRRF13SUSPENSA |
| Incidência de FGTS 13º suspensa em decorrência de decisão judicial | Inteiro | 2 | 120 | INCFGTS13SUSPENSA |
| Incidência de IRRF Férias suspensa em decorrência de decisão judicial (campo descontinuado e substituido para o campo 137 INCIRRFSUSPENSAO) | Inteiro | 2 | 121 | INCIRRFFERIASSUSPENSA |
| Incidência de IRRF PLR suspensa em decorrência de decisão judicial (campo descontinuado e substituido para o campo 137 INCIRRFSUSPENSAO) | Inteiro | 2 | 122 | INCIRRFPLRSUSPENSA |
| Incidência de INSS Sal.Matern. suspensa em decorrência de decisão judicial (campo descontinuado e substituido para o campo 136 INCINSSSUSPENSAO) | Inteiro | 2 | 123 | INCINSSSALMATSUSPENSA |
| Incidência de INSS Sal.Mater.13º suspensa em decorrência de decisão judicial (campo descontinuado e substituido para o campo 136 INCINSSSUSPENSAO) | Inteiro | 2 | 124 | INCINSSSALMAT13SUSPENSA |
| Incidência de Contribuição Sindical | Boleano | 2 | 125 | INCCONTRIBSINDICAL |
| Forçar incidência  de IRRF | Inteiro | 2 | 126 | FORCARINCIRRF |
| Incidência de IRRF Forçada | String | 2 | 127 | INCIRRFFORCADA |
| Isento de IRRF | Inteiro | 2 | 128 | ISENTOIRRF |
| Incidência IRRF Isenção | String | 4 | 129 | INCIRRFISENCAO |
| Não calcula diferença para este evento | Boleano | 2 | 130 | NAOCALCDIFERENCA |
| Incidência de Suspensão para Contribuição Previdenciária (Aba Proventos) | Inteiro | 2 | 131 | INCCPSUSPENSAO |
| Evento de Diferença de Salário Negativa | String | 4 | 132 | CODEVENTODIFNEGATIVA |
| Incidência de INSS exclusiva do empregador (Aba Proventos) | Inteiro | 2 | 133 | INCINSSEXCLUSIVAEMPREGADOR |
| Incidência de INSS exclusiva do segurado - 13º salário | Inteiro | 2 | 134 | INCINSSEXCLUSIVASEGURADO13 |
| Incidência de INSS exclusiva do empregador (Aba Descontos) | Inteiro | 2 | 135 | INCINSSEXCLUSIVAEMPREGADORDESC |
| Incidência de INSS suspensa em decorrência de decisão judicial  (Valores válidos: 91, 92, 93, 94) | Inteiro | 2 | 136 | INCINSSSUSPENSAO |
| Incidência de IRRF suspensa em decorrência de decisão judicial (Valores válidos: Conforme tabela 21 do eSocial independente do layout do eSocial) | Inteiro | 4 | 137 | INCIRRFSUSPENSAO |
| Compõe o teto remuneratório específico (art. 37, XI, da CF/1988) | Boleano | 2 | 138 | COMPOETETOREMUNERATORIO |
| Incidência de Suspensão para Contribuição Previvenciária (Aba Descontos) | Inteiro | 2 | 139 | INCCPSUSPENSAODESC |
| Incidência de INSS décimo terceiro exclusiva do empregador (Aba Proventos) | Inteiro | 2 | 140 | INCINSSEXCLUSIVAEMPREGADOR13 |
| Incidência de INSS décimo terceiro exclusiva do empregador (Aba Descontos) | Inteiro | 2 | 141 | INCINSSEXCLUSIVAEMPREGADOR13DS |
| Incidência para as contribuições do Regime Próprio de Previdência Social - RPPS/regime militar (Aba Proventos) | string | 2 | 142 | INCREGIMEPROPRIOPREVIDENCIA |
| Incidência para as contribuições do Regime Próprio de Previdência Social - RPPS/regime militar (Aba Descontos) | string | 2 | 143 | INCREGIMEPROPRIOPREVIDENCIADSC |
| Tipo de Previdência Complementar | Boleano | 2 | 144 | TIPOPREVIDENCIACOMPLEMENTAR |
| Incidência PIS/PASEP | Boleano | 2 | 145 | INCPISPASEP |
| Antecipação de Férias (Provento/Desconto) | Texto | 4 | 146 | CODEVENTODEPARARECIBOFERIAS |
| Envelope de Pagamento (Provento) | Texto | 4 | 147 | CODEVENTODEPARAPROVENTOFERIAS |
| Envelope de Pagamento (Desconto) | Texto | 4 | 148 | CODEVENTODEPARADESCONTOFERIAS |
| Forçar codIncCP eSocial | Texto | 2 | 149 | FORCARINCINSS |
| Código de incidência tributária do eSocial | Texto | 2 | 150 | INCINSSFORCADA |

**Fique atento!** A partir do campo 136 só serão habilitados após a sua criação pelo RM.Atualizador.exe
