---
article_id: 11960173670551
category: GPE - eSocial - Processo Trabalhista
content_hash: 9a04a063b5d816452137cc8bd1ef3dc3facb7c5bacd28a7cc210e9afe62c9395
fetched_at: '2026-06-28T22:45:00.442801+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Como funciona o De / Para dos
  campos entre GPE x TAF
type: support-article
updated_at: '2025-03-27T18:07:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11960173670551-RH-Linha-Protheus-GPE-eSocial-S-2500-Como-funciona-o-De-Para-dos-campos-entre-GPE-x-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446028755735) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Para o evento S-2500 como funciona o De / Para de campos Protheus com leiaute eSocial S-1.2, entre GPExTAF?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Consulte na tabela a seguir detalhadamente a estrutura de campos entre GPE e TAF para o evento S-2500:

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **eSocial** | **Protheus Recursos Humanos** | | | | **Protheus TAF** | | | | **Descrição / Validação** | **Leiautes:** |
| **S-1.1/S-1.2** |
| **tag xml** | **Rotina** | **Tabela** | **Campo** | **Nome** | **Rotina** | **Tabela** | **Campo** | **Nome** | **\* Ambas versões** |
| tpInsc | APTA100 | RE0 | RE0\_TPINSC | Tipo de Inscrição | TAFA608 | V9U | V9U\_TPINSC | Tp.Inscrição | Tipo de Inscrição | \* |
| nrInsc | APTA100 | RE0 | RE0\_NINSC | Número de Inscrição | TAFA608 | V9U | V9U\_NRINSC | Nr.Ins.Empr. | Informações de identificação do contribuinte (responsável direto), caso tenha havido imposição de responsabilidade indireta | \* |
| origem | APTA100 | RE0 | RE0\_ORIGEM | Origem | TAFA608 | V9U | V9U\_ORIGEM | Origem Proc. | Informe a origem do processo. | \* |
| nrProcTrab | APTA100 | RE0 | RE0\_PROJUD | Número do Processo | TAFA608 | V9U | V9U\_NRPROC | Número Proc. | Preencher com a identificação do processo judicial ou administrativo. | \* |
| obsProcTrab | APTA100 | RE0 | RE0\_COBS | Observacoes | TAFA608 | V9U | V9U\_OBSERV | Observação | Campo Memo destinado ao cadastramento das Observações do Processo Trabalhista. | \* |
| dtSent | APTA100 | RE0 | RE0\_DTDECI | Data de Decisão | TAFA608 | V9U | V9U\_DTSENT | Dt. Sentença | Data da Sentença | \* |
| ufVara | APTA060 | RE1 | RE1\_UF | Unid. Federacao | TAFA608 | V9U | V9U\_UFVARA | Id. UF | Unidade de Federação da Vara. | \* |
| codMunic | APTA060 | RE1 | RE1\_CODMUN | Código Município eSocial | TAFA608 | V9U | V9U\_CODMUN | Id.Cod.Mun. | Preencher com o código do município, conforme tabela do IBGE. | \* |
| idVara | APTA060 | RE1 | RE1\_IDVARA | Id.Vara eSocial | TAFA608 | V9U | V9U\_IDVARA | Id. da Vara | Preencher com o código de Identificação da Vara | \* |
| dtCCP | APTA100 | RE0 | RE0\_DTCCP | Data da Conciliação | TAFA608 | V9U | V9U\_DTCCP | Dt.Concili. | Informar a Data da Conciliação | \* |
| tpCCP | APTA100 | RE0 | RE0\_TPCCP | Âmbito CCP | TAFA608 | V9U | V9U\_TPCCP | Cel.do Acor. | Indicar o âmbito de celebração do acordo. | \* |
| cnpjCCP | APTA100 | RE0 | RE0\_CNPJCC | CNPJ CCP | TAFA608 | V9U | V9U\_CNPJCP | CNPJ CCP | Identificar o CNPJ do sindicato representativo do trabalhador, no âmbito da CCP ou NINTER. | \* |
| cpfTrab | APDA020 | RD0 | RD0\_CIC | CPF | TAFA608 | V9U | V9U\_CPFTRA | CPF | CPF do Reclamante | \* |
| nmTrab | APDA020 | RD0 | RD0\_NOME | Nome Participante | TAFA608 | V9U | V9U\_NMTRAB | Nome do Trab | Nome do Reclamante | \* |
| dtNascto | APDA020 | RD0 | RD0\_DTNASC | Data de Nascimento | TAFA608 | V9U | V9U\_DTNASC | Dt.de Nasc. | Data de nascimento do reclamante | \* |
| cpfDep | GPEA020 | SRB | RB\_CIC | CPF | TAFA608 | V9V | V9V\_CPFDEP | CPF Depend | CPF do dependente | S-1.1 |
| tpDep | GPEA020 | SRB | RB\_TPDEP | Tipo Dependente eSocial | TAFA608 | V9V | V9V\_TPDEP | Tipo Depende | Tipo de dependente conforme tabela 07. | S-1.1 |
| descDep | GPEA020 | SRB | RB\_NOME | Nome do Dependente | TAFA608 | V9V | V9V\_DSCDEP | Desc Dep | Nome do dependente | S-1.1 |
| tpContr | TAFA552D | E0B | E0B\_TPCONT | Tipo de Contrato | TAFA608 | V9W | V9W\_TPCONT | Tipo Contrat | Tipo de contrato a que se refere o processo judicial ou a demanda submetida à CCP ou ao NINTER. | \* |
| indContr | TAFA552D | E0B | E0B\_INDCON | Indicativo de Contrato | TAFA608 | V9W | V9W\_INDCON | Ind. Contrat | Informe se o reclamente possui informação no evento S-2190, S-2200 ou S-2300 no declarante. | \* |
| dtAdmOrig | TAFA552D | E0B | E0B\_DTADMO | Dt. Admissao Original | TAFA608 | V9W | V9W\_DTADMO | Dt Adm Orig | Preencher com a data de admissão original do vínculo (data de admissão antes da alteração). | \* |
| indReint | TAFA552D | E0B | E0B\_INDREI | Indicativo Reintegração | TAFA608 | V9W | V9W\_INDREI | Indicativo Reintegração | Informe se existir evento de reintegração (S-2298) | \* |
| indCateg | TAFA552D | E0B | E0B\_INDCAT | Reconhecimento Categoria | TAFA608 | V9W | V9W\_INDCAT | Indicativo de Categoria | Indicativo se houve reconhecimento de categoria do trabalhador diferente da cadastrada (no eSocial ou na GFIP) pelo declarante. | \* |
| indNatAtiv | TAFA552D | E0B | E0B\_INDNAT | Reconhecimento Atividade | TAFA608 | V9W | V9W\_INDNAT | Indicativo da Natureza | Indicativo se houve reconhecimento de natureza da atividade diferente da cadastrada pelo declarante. | \* |
| indMotDeslig | TAFA552D | E0B | E0B\_INDMDE | Reconhecimento Desligamen | TAFA608 | V9W | V9W\_INDMDE | Indicativo Mot Deslig | Indicativo se houve reconhecimento de motivo de desligamento diferente do informado pelo declarante. | \* |
| indUnic | TAFA552D | E0B | E0B\_INDUNI | Reconhecimento Contrato | TAFA608 | V9W | V9W\_INDUNI | Indicativo Unicidade Cont | Indicativo se houve reconhecimento de unicidade contratual (declaração da continuidade do contrato de trabalho, considerando como único dois ou mais vínculos sucessivos informados no eSocial). | S-1.1 |
| matricula | TAFA552D | E0B | E0B\_CODUNI | Matrícula eSocial | TAFA608 | V9W | V9W\_MATRIC | Matricula | Matricula eSocial | \* |
| codCateg | TAFA552D | E0B | E0B\_CATEFD | Categoria eSocial | TAFA608 | V9W | V9W\_CODCAT | Código Categoria | Categoria eSocial | \* |
| dtInicio | TAFA552D | E0B | E0B\_DTITSV | Dt. Inicio TSV | TAFA608 | V9W | V9W\_DTINIC | Data de Inicio | Data de início do trabalhador sem vínculo no eSocial. | \* |
| codCBO | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_CODCBO | Código de CBO | Código de CBO | \* |
| natAtividade | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_NATATV | Natureza da atividade | Natureza da atividade | \* |
| dtRemun | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9Y | V9Y\_DTREMU | Data de Remuneração | Data de Remuneração | \* |
| vrSalFx | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9Y | V9Y\_VRSAL | Valor da remuneração | Valor da remuneração | \* |
| undSalFixo | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9Y | V9Y\_UNDSAL | Unidade de salário | Unidade de salário | \* |
| dscSalVar | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9Y | V9Y\_DSCSAL | Descrição do Salario | Descrição do Salario | \* |
| tpRegTrab | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_TPREGT | Tipo de regime trabalhista | Tipo de regime trabalhista | \* |
| tpRegPrev | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_TPREGP | Tipo Reg. Previdenciario | Tipo Reg. Previdenciario | \* |
| dtAdm | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_DTADM | Data de Admissão | Data de Admissão | \* |
| tmpParc | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_TMPPAR | Tipo de contrato | Data de Admissão | \* |
| tpContr | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_TPCDUR | Tipo de contrato de trab | Tipo de contrato de trabalho | \* |
| dtTerm | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_DTTERM | Dt Term Contrato | Data Termino do Contrato | \* |
| clauAssec | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_CLAASS | Clausula Assecuratória | Clausula Assecuratória | \* |
| objDet | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_OBJDET | Objeto determinante | Objeto determinante | \* |
| observacao | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9Z | V9Z\_OBS | Observação Relacionada | Observação Relacionada | \* |
| tpInsc | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_TPINSC | Tipo de Inscrição | Tipo de Inscrição | \* |
| nrInsc | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_NRINSC | Numero de inscrição | Numero de inscrição | \* |
| matricAnt | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_MATANT | Matricula Anterior | Matricula Anterior | \* |
| dtTransf | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_DTTRAN | Data Transferência | Data Transferência | \* |
| dtDeslig | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_DTDESL | Data de desligamento | Data de desligamento | \* |
| mtvDeslig | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_MTVDES | Motivo de desligamento | Motivo de desligamento | \* |
| dtProjFimAPI | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_DTFPRO | Data Projetada Term | Data Projetada | \* |
| pensAlim | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_PENSAL | Pens Alim | Indicativo de pensão alimentícia para fins de retenção de FGTS. | S-1.2 |
| percAliment | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_PERCAL | Perc Pens Al | Percentual a ser destinado a pensão alimentícia. | S-1.2 |
| vrAlim | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_VRALIM | Vl Pens Ali | Valor da pensão alimentícia. | S-1.2 |
| dtTerm | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_DTFIM | Data do Término | Data de Término | \* |
| mtvDesligTSV | TAFA552D | E0G | E0G\_MEM | (Memo) | TAFA608 | V9X | V9X\_MTDTSV | Motivo Término do Diretor | Motivo Término | \* |
| codCateg | TAFA552D | E0A | E0A\_NCAT | Nova Cat. eSocial | TAFA608 | V7A | V7A\_NEWCAT | Novo Cód. Categoria | Novo código de Categoria Trab. eSocial, no caso de reconhecimento judicial nesse sentido. | \* |
| natAtividade | TAFA552D | E0A | E0A\_NATUR | Natureza Atividade | TAFA608 | V7A | V7A\_NATATV | Natureza da Atividade | Natureza da Atividade. | \* |
| dtMudCategAtiv | TAFA552D | E0A | E0A\_DTALT | Data Mudança Categoria | TAFA608 | V7A | V7A\_DTMUDC | Data Nova Categoria | Data a partir da qual foi reconhecida a nova Categoria Trab. eSocial. | \* |
| matUnic | TAFA552D | E0B | E0B\_CODUNI | Mat. eSocial | TAFA608 | V7B | V7B\_MATUNI | Matricula de Unicidade | Matricula eSocial | \* |
| codCateg | TAFA552D | E0B | E0B\_CATEFD | Cat. eSocial | TAFA608 | V7B | V7B\_NEWCAT | Novo Cód. Categoria | Novo código Categoria eSocial | \* |
| dtInicio | TAFA552D | E0B | E0B\_DTITSV | Dt. Inicio TSV | TAFA608 | V7B | V7B\_DTTSV | Data Inicio do TSVE | Data de Inicio do TSVE | \* |
| tpInsc | TAFA552D | E0C | E0C\_TPINSC | Tipo de Inscrição | TAFA608 | V7H | V7H\_TPINSC | Tipo de inscrição | Tipo de Inscrição | \* |
| nrInsc | TAFA552D | E0C | E0C\_NINSC | Número de Inscrição | TAFA608 | V7H | V7H\_NRINSC | Número de inscrição | Numero de Inscrição | \* |
| compIni | TAFA552D | E0C | E0C\_COMPIN | Competencia Inicial | TAFA608 | V7H | V7H\_COMPIN | Competencia Inicial | Competência Inicial | \* |
| compFim | TAFA552D | E0C | E0C\_COMFIM | Competencia Final | TAFA608 | V7H | V7H\_COMPFI | Competencia Final | Competência Final | \* |
| repercProc | TAFA552D | E0C | E0C\_REPPRO | Repercussão do Processo | TAFA608 | V7H | V7H\_REPPRO | Reperc Proce | Informe a Repercussão do processo trabalhista | S-1.1 |
| indReperc | TAFA552D | E0C | E0C\_REPPRO | Repercussão do Processo | TAFA608 | V7H | V7H\_INDREP | Ind. Reperc. | Indicativo de repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER. | S-1.2 |
| vrRemun | TAFA552D | E0C | E0C\_VREMUN | Total Verb Remuneratorias | TAFA608 | V7H | V7H\_VLVERB | Valor total das verbas | valor total das verbas remuneratórias a serem pagas | S-1.1 |
| vrAPI | TAFA552D | E0C | E0C\_VRAPI | Valor Aviso Previo | TAFA608 | V7H | V7H\_VLAVSP | Valor do aviso prévio | Valor do aviso prévio indenizado | S-1.1 |
| vr13API | TAFA552D | E0C | E0C\_V13API | Proj Aviso Prev Ind 13 Sl | TAFA608 | V7H | V7H\_VRAPI | Valor da projeção | valor da projeção do aviso prévio indenizado sobre o 13º salário | S-1.1 |
| vrInden | TAFA552D | E0C | E0C\_VINDEN | Tot demais Verbas Indeniz | TAFA608 | V7H | V7H\_VLINDE | Valor total das Verb Inde | valor total das demais verbas indenizatórias a serem pagas | S-1.1 |
| vrBaseIndenFGTS | TAFA552D | E0C | E0C\_BCFGTS | B.C. FGTS sobre Multa | TAFA608 | V7H | V7H\_VLBASE | Valor Base de Cálculo | Valor da base de cálculo para recolhimento da indenização compensatória (multa rescisória) do FGTS | S-1.1 |
| pagDiretoResc | TAFA552D | E0C | E0C\_PGRESC | Ind Compensatória FGTS | TAFA608 | V7H | V7H\_PAGDIR | Indenização Compensatória | Informar se a indenização compensatória (multa rescisória) do FGTS transacionada foi paga diretamente ao trabalhador mediante decisão/autorização judicial | S-1.1 |
| indenSD | TAFA552D | E0C | E0C\_INDENS | Inden. Substitutiva? | TAFA608 | V7H | V7H\_INDESD | Ind Subst SD | Indicativo se houve decisão para pagamento da indenização substitutiva do seguro-desemprego | S-1.2 |
| indenAbono | TAFA552D | E0C | E0C\_ABONO | Inden. Abono? | TAFA608 | V7H | V7H\_INDABO | Pag Ind Abon | Indicativo se houve decisão para pagamento da indenização substitutiva de abono salarial | S-1.2 |
| anoBase | TAFA552D | E0C | E0C\_MEMO | (Memo) | TAFA608 | V7Q | V7Q\_ANOBAS | Ano Abono | Ano-base em que houve indenização substitutiva do abono salarial. | S-1.2 |
| perRef | TAFA552D | E0D | E0D\_COMPET | Competencia | TAFA608 | V7I | V7I\_PERREF | Período Referência | Informar o mês/ano (formato AAAAMM) de referência das informações | \* |
| vrBcCpMensal | TAFA552D | E0D | E0D\_BCINSS | Base de Cálculo INSS | TAFA608 | V7I | V7I\_VRMEN | Valor Base Mensal | Valor da base de cálculo da contribuição previdenciária sobre a remuneração mensal do trabalhador. | \* |
| vrBcCp13 | TAFA552D | E0D | E0D\_BCCP13 | Base de Cálculo INSS 13 | TAFA608 | V7I | V7I\_VRCP | Valor Base Calculo 13° | Valor da base de cálculo da contribuição previdenciária sobre a remuneração do trabalhador referente ao 13º salário. | \* |
| vrBcFgts | TAFA552D | E0D | E0D\_BCFGTS | Base de Cálculo FGTS | TAFA608 | V7I | V7I\_VRFGTS | Valor Base FGTS | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador (sem 13° salário). | S-1.1 |
| vrBcFgts13 | TAFA552D | E0D | E0D\_FGTS13 | Base de Cálculo FGTS 13 | TAFA608 | V7I | V7I\_BCFGTS | Base Cal. FGTS 13° | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador sobre o 13º salário. | S-1.1 |
| grauExp | TAFA552D | E0D | E0D\_GRAUEX | Grau de Exposição | TAFA608 | V7I | V7I\_GRAUEX | Grau de exposição | Preencher com o código que representa o grau de exposição a agentes nocivos: | \* |
| vrBcFgtsGuia | TAFA552D | E0D | E0D\_FGTSDE | BC FGTS ja Declarado | TAFA608 | V7I | V7I\_VRFGUI | Vr. Base FGTS Guia | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador, anteriormente declarado | S-1.1 |
| vrBcFgts13Guia | TAFA552D | E0D | E0D\_FG13AN | BC FGTS 13 Decl Anter. | TAFA608 | V7I | V7I\_FGTSGU | Vr. Base FGTS 13° Guia | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador sobre o 13º salário, anteriormente declarado | S-1.1 |
| pagDireto | TAFA552D | E0D | E0D\_FGTSPG | FGTS Declarado Anterior. | TAFA608 | V7I | V7I\_PAGDIR | Pago diretamente? | O FGTS transacionado referente a perRef foi pago diretamente ao trabalhador mediante decisão/autorização judicial? | S-1.1 |
| vrBcFGTSProcTrab | TAFA552D | E0D | E0D\_FGTSPR | FGTS Processo | TAFA608 | V7I | V7I\_BCPROT | Vl FGTS PT | Valor da base de cálculo de FGTS ainda não declarada em SEFIP ou no eSocial, inclusive de verba reconhecida no processo trabalhista. | S-1.2 |
| vrBcFGTSSefip | TAFA552D | E0D | E0D\_FGTSSE | FGTS SEFIP | TAFA608 | V7I | V7I\_BCSEFI | Vl BC SEFIP | Valor da base de cálculo de FGTS declarada apenas em SEFIP (não informada no eSocial) e ainda não recolhida. | S-1.2 |
| vrBcFGTSDecAnt | TAFA552D | E0D | E0D\_FGTSAN | FGTS Anterior | TAFA608 | V7I | V7I\_BCDECA | Vl BC Dec An | Valor da base de cálculo de FGTS declarada anteriormente no eSocial e ainda não recolhida. | S-1.2 |
| codCateg | TAFA552D | E0D | E0D\_CODCAT | Categoria Trabalhador | TAFA608 | V7I | V7I\_CATMUD | Cod Categoria Mud | Preencher com o código da categoria do trabalhador declarado no período de referência, no caso de reconhecimento de mudança de código de categoria. | \* |
| vrBcCPrev | TAFA552D | E0D | E0D\_BCCPRE | Remuneração | TAFA608 | V7I | V7I\_VRPREV | Valor Previdenciário | Valor da remuneração do trabalhador a ser considerada para fins previdenciários declarada em GFIP ou em S-1200 de trabalhador sem cadastro no S-2300, no caso de reconhecimento de mudança de código de categoria. | \* |

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - Como se adequar ao eSocial leiaute S-1.2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8658568031127)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
