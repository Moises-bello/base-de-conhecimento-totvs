---
article_id: 9138402927639
category: RH - Funcionários
content_hash: d0a3dea3760bdee4657c3b82cbad00708c86f74c2576984a8d71526abd89ec5c
fetched_at: '2026-06-28T22:43:28.662748+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o cadastro
  de funcionários
type: support-article
updated_at: '2025-08-18T19:09:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9138402927639-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-utilizados-para-o-cadastro-de-funcion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31481205296151) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Quais os parâmetros utilizados para o cadastro de funcionários?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Os parâmetros que envolvem o cadastro de funcionários são:

**MV\_ACCATPR** - Quais categorias de funcionários devem ser usadas para filtrar professores.   
**MV\_ALTSAL** - Altera C.B.O. e Salario quando alterar a função   
**MV\_APICLO0** - Utiliza integração com Carol Clockin?   
**MV\_AUDESP** - Utiliza AUDESP   
**MV\_CARGSQ3** - Informe se ao enviar o evento S-1030 - Cargos ao eSocial, serão utilizados os dados da tabela SQ3 no lugar da SRJ, preenchimento .T.=SQ3, .F.=SRJ   
**MV\_CCTFUNC** - Valida se função esta associada a CCT do sindicato no cadastro de funcionários?   
**MV\_CLASSIS** - Parametro de integração Protheus x ClassisNet .T. = Ativo, .F. = Desativado   
**MV\_CTRVAGA** - Indica se controla ou não o número de vaga aberta.   
**MV\_EFDAVIS** - Na ocorrência de inconsistência na eSocial 0-Emite aviso; 1-Avisa e impede processo; 2-Não emite aviso.   
**MV\_EFDMSG** - Apresenta aviso informando que o evento foi enviado com sucesso para o TAF. Valido apenas para eventos não periódicos.   
**MV\_ERPLOGI** - Indica se há integração com o ERP LOGIX   
**MV\_FASESOC** - Responsável por gerenciar o faseamento do eSocial. (Vazio) - 1a Fase / 1 - 1a Fase + 2a Fase 2 - 1a Fase + 2a Fase + 3a Fase   
**MV\_FUNCARG** - C - Atualiza o campo salario baseado na Faixa Sala rial ou F - Atualiza o campo salario baseado no salario da função   
**MV\_GPCFUPR** - Quais categorias de funcionário que podem ser também considerado professor eventualmente.   
**MV\_HSTSAL** - Verifica se deve gravar histórico salarial  
**MV\_INTTAF** - Habilita a Integração Nativa do Protheus para o modulo SIGATAF. Valores validos (S - Habilita, N - Desabilita)   
**MV\_IORGRSP** - Define se haverá integração entre os módulos de Arquitetura Organizacional e Recrutamento seleção (0-Integracao não ativada e 1-Integracao ativada)   
**MV\_ITMCLVL** - Informe 1 para utilização do Item contábil e Clas- se de valor, 2 para não utilizar, ou 3 para utilizar item/classe sem obrigatoriedade de ambos.   
**MV\_MATRICU** - Indica como será o controle de numeração da Matric (0=Usuário informará; 1=Automática por Filial; 2=Autom. por Empresa; 3=Autom. por Grp Empresa;)   
**MV\_MODFOL** - Determina qual a versão que está sendo utilizada (1=padrão e 2=Modelo 2)   
**MV\_NG2ESOC** - Indica se o sistema de Medicina e Segurança do Trabalho irá gerar registros no SIGATAF ou Middleware. 1 = Sim, 2 = Não.   
**MV\_NGMNTRH** - integração manutenção (MNT) com Recursos Humanos (RH). Informar S=Tem integração, N=não tem integração ou X=Tem integração e permite terceiros   
**MV\_NGSALHO** - Define se calcula o Salário Hora do Funcionário ou apenas traz do GPE (RA\_SALARIO). Informar S=Sim ou N=não.   
**MV\_NTSV** - Informe as categorias de TSV que não são obrigados a terem o evento S-2300   
**MV\_OPESOC** - Utiliza o Controle de Beneficiário - Órgão Público .T. = Sim e .F. = Não   
**MV\_ORGCFG** - Configura o modo de uso do modulo Arquitetura Organizacional. 0=Não utiliza;1=Utiliza com controle de postos;2=Utiliza sem controle de Postos;   
**MV\_PIMSINT** - Habilita integração Protheus x PimsGraos   
**MV\_RESCAD** - Define as exportações habilitadas do Protheus para o Reserve (0=Não/1=Sim). Ex. 010 (0=C.Custo/1=Clientes/0=Participantes).   
**MV\_RESEXP** - Forma de exportação dos cadastros para o Sistema Reserve. 0=Desativado,1=Online,2=Scheduler, 3=Online e Scheduler   
**MV\_RETSOC** - Parâmetro de definição do evento retificador S2200   
**MV\_RHNG** - Habilita integração de dados entre GPE e NG   
**MV\_RHTAF** - Habilita a integração de dados do eSocial com TAF Se .T., passa a integrar dados de eventos não periódicos do SIGAGPE com o SIGATAF   
**MV\_TAFVLES** - Versão do Layout e-Social. Utilizado para a criação do nameSpace dos eventos e validações de estrutura no modulo SIGATAF.   
**MV\_TECXRH** - Define se o gestão de serviço esta integrado com Rh do Microsiga Protheus.   
**MV\_TRMINTG** - Habilita a integração do modulo de treinamento com o EPM Datasul.   
**MV\_TSREP** - Define se haverá integração entre o módulo Sigapon e o aplicativo TSA (Totvs Controle de Acesso)   
**MV\_USESPJ** - Determina se o calendário será elaborado utilizando a tabela SPJ. 0 - não (padrão); 1 - sim.   
**MV\_VLDCTR** - SIGAGPE - Indica se o campo Data Término de Contrato deve ser preenchido quando Tipo de Contrato for igual a 2 - Determinado.   
**MV\_QGINT** - Indica se os módulos Quality estão integrados com Modulo SIGAGPE e não habilita a opção de "INCLUIR"   
  
**Saiba mais:**Para adquirir mais conhecimento acesse o(s) *link**(s)* abaixo:

[RH - Linha Protheus - GPE - Como cadastrar um funcionário celetista mensalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058682774-MP-GPE-Como-cadastrar-um-funcion%C3%A1rio-celetista-mensalista?source=search)

[RH - Linha Protheus - GPE - Onde alterar os dados cadastrais do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016407931-RH-Linha-Protheus-GPE-Onde-alterar-os-dados-cadastrais-do-funcion%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Como realizar a cópia do cadastro do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412275775895-RH-Linha-Protheus-GPE-Como-realizar-a-c%C3%B3pia-do-cadastro-do-funcion%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Como cadastrar um Autônomo MEI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035241534-RH-Linha-Protheus-GPE-Como-cadastrar-um-Aut%C3%B4nomo-MEI?source=search)

[RH - Linha Protheus - GPE - Como cadastrar um Autônomo ou Pró-labore](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052067393-RH-Linha-Protheus-GPE-Como-cadastrar-um-Aut%C3%B4nomo-ou-Pr%C3%B3-labore?source=search)
