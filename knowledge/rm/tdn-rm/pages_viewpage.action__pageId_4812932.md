---
content_hash: 78753336b444cf2aa6d0e72ff229f229e7b0377be4fbaa666b7c8d1b00ec6d0a
fetched_at: '2026-06-29T00:10:18.981324+00:00'
page_id: '4812932'
product: rm
source: tdn-rm
title: PPP - Conferência dos dados impressos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812932
version: 11
---

BLOCK

PPP - Conferência dos dados impressos

FAQ: **PPP - Conferência dos dados impressos**

Avaliação

Esse roteiro tem o objetivo de auxiliar na conferência das informações que são geradas no relatório do PPP (Perfil Profissiográfico Previdenciário).

Solução

**Procedimento:**

1) É necessário importar o relatório PPP do RM Reports.

2) Conheça os campos do relatório e de onde são buscadas as informações no sistema:

2.1) Acesse: Cadastros / Coligadas:

PPP – Campo 1 – CNPJ do Domicilio Tributário/CEI - Será buscado da seção do Funcionário.

**Origem no banco de dados:   
GCOLIGADA.CGC**

PPP – Campo 2 – Nome Empresarial.

  

**Origem no banco de dados:**

**GCOLIGADA.NOME**

2.2) Acesse: Cadastros / Seções, edite a seção.

PPP – Campo 3 – CNAE .

**Origem no banco de dados:**

**PSECAO.ATIVECONOMICA**

2.3) Acesse: Cadastros / Funcionários – Edite o cadastro do funcionário

à Acesse a guia “Informações Pessoais / Identificação”.

PPP – Campo 4 - Nome do Trabalhador.

PPP – Campo 7 - Data do Nascimento

PPP – Campo 8 - Sexo

  

**Origem no banco de dados:**

**PPESSOA.NOME**

**PPESSOA.DTNASCIMENTO**

**PSECAO.SEXO**

à Acesse a guia “Informações Pessoais / Documentação”.

PPP – Campo 6 - NIT

PPP – Campo 9 - CTPS (Nº, Série e UF).

**Origem no banco de dados:**

**PPESSOA.PISPASEP**

**Composição entre os campos PPESSOA.CARTEIRATRAB,**

**PPESSOA.SERIECARTTRAB**

**PPESSOA.UFCARTTRAB**

Acesse a guia “Registro”.

PPP – Campo 10 - Data de Admissão.

  

**Origem no banco de dados:**

**PFUNC.DATAADMISSAO**

2.4) Ainda no cadastro do funcionário acesse:

à Anexos / Segurança e Medicina / Informações PPP.

PPP – Campo 5 - BR/PDH.

  

**Origem no banco de dados:**

**PPESSOA.BRPDH**

* BR/PDH – Beneficiário Reabilitado / Portador de Deficiência Habilitado;

PPP – Campo 11 - Regime de Revezamento.

**Origem no banco de dados:**

**PFUNC.REGIMEREVEZAMENTO**

à Anexos / Segurança e Medicina / Acidente de Trabalho.

PPP – Campo 12 - CAT Registrada.

PPP – Campos 12.1 e 12.2 – Data do Registro e Número da CAT.

Acesse o módulo SMT / Seg e Med do Trab / CAT|Incidentes /  Ocorrências Acidente Trabalho.

**Origem no banco de dados:**

**VOCORRENCIA.DATAHORA,**

**VOCORRENCIA. REGISTROINSS**

**Descrição do Processo**

* + Para visualizar as informações citadas acima, inclua uma CAT no módulo SMT em Seg. e Med do Trab / Ocorrências Acidente Trabalho;
  + **Somente serão impressas informações no campo 12, funcionários com CAT cadastrada.**

  2.5) Lotação e Atribuição.

  Caso o funcionário esteja alocado em um tomador de serviço, as informações provenientes deste tomador prevalecerão sobre as informações diretas do funcionário.

  PPP – Campo 13.1 – Período

  Este campo é uma composição das datas de entrada na seção e função, para isso devemos:

  Comparar os históricos de ambos:

**Origem no banco de dados:   
PFHSTFCO.DTMUDANCA  
PFHSTSEC.DTMUDANCA  
PHSTOCORRENCIA.DTMUDANCA  
PSUBSTCHEFE.DATAINICIO  
PSUBSTCHEFE.DATAFIM  
VTOMADORSERVICOVINC.DATAINICIAL  
VTOMADORSERVICOVINC.DATAFINAL**

PPP – Campo 13.2 - CNPJ / CEI

Essa informação está diretamente vinculada com as seções nas quais o funcionário passou.

**Sempre prevalecerá o registro que conter o CEI.  
Origem no banco de dados:  
PSECAO.CGC  
PSECAO.CEI  
FCFO.CEI  
FCFO.CGCCFO**

PPP – Campo 13.3 – Setor

Acesse Cadastros / Funcionários, selecione ou edite o cadastro do mesmo.

Acesse Anexos / Históricos / Histórico de Seção:

**Origem no banco de dados:**

**PSECAO.DESCRICAO**

PPP – Campo 13.4 – Cargo

Segundo Legislação do PPP o cargo é a função que o funcionário desempenha.

Verificar as funções no histórico de funções do funcionário (Anexos / Históricos / Histórico

de Função).

**Origem no banco de dados:**

**PFUNCAO.CODIGO**

PPP – Campo 13.5 – Função

Caso o trabalhador ocupe um cargo de Chefia ou Supervisão (no sistema em Cadastro | Tabelas

Auxiliares | Chefes/Supervisores) esse campo será alimentado, quando não ocupar algum

desses cargos o campo será preenchido com NA – Não Aplicável.

PPP – Campo 13.6 – CBO

* As informações desse campo obedecem ao histórico:
  1. Funções – Observadas as funções as quais o funcionário executou, acessar o cadastro das mesmas e verificar se o número do CBO confere com o que está sendo impresso no relatório.

**Origem no banco de dados:**

**PFUNCAO.NOME**

**PFUNCAO.CBO2002**

PPP – Campo 13.7 – Cód. GFIP

Acesse: Cadastros / Funcionários – Edite o cadastro do funcionário, guia “Rotinas Mensais |

FGTS / SEFIP”.

  

**Origem no banco de dados:   
PHSTOCORRENCIA.CODOCORRENCIA  
VTOMADORSERVICOVINC.CODGFIP**

2.6) Profissiografia.

Pode ser exibida por:

* As informações desse campo podem originar-se de:
  1. Funções
  2. Tarefas
  3. Quadro de Lotação

E estas se vinculam a Quadros de lotação ou Postos de Trabalho.

PPP – Campo 14.1 – Período

Acesse Cadastro/ Funcionários – Edite o cadastro do funcionário, em Anexos / Históricos /

Histórico de Função:

**Origem no banco de dados:   
PFHSTFCO.DTMUDANCA  
VPPRAHISTTAREFASFUNCAO.DATA  
VPPRAHISTTAREFASFUNCAO.DATASAIDA  
PFHSTSEC.DTMUDANCA  
VPPRAHISTTAREFALOTACAO.DATA  
VPPRAHISTTAREFALOTACAO.DATASAIDA  
VHISTPOSTOPFUNC.DATA  
VHISTPOSTOPFUNC.DATASAIDA  
VPPRAHISTAREFAFUNCAOPOSTO.DATA  
VPPRAHISTAREFAFUNCAOPOSTO.DATASAIDA  
VPPRAHISTTAREFAPESSOAL.DATA  
VPPRAHISTTAREFAPESSOAL.DATASAIDA**

PPP – Campo 14.2 – Descrição

Para verificar se a descrição está na função acesse Cadastros / Funções.

**Origem no banco de dados:   
PFUNCAO.DESCRICAO  
VTAREFA.DESCRICAO  
VMEMO.VALMEMO (Referenciando VLOTACAO.IDOBSERVACAO)  
VMEMO.VALMEMO (Referenciando VPOSTOFUNCAO.CODMEMOOBS)**

Para verificar se a descrição está nas tarefas acesse  Gestão de Pessoas / Gestão Organizacional / Tarefas

Para verificar qual é o vínculo devemos acessar Gestão de Pessoas / Gestão Organizacional  / Administração de Tarefas

No wizard de Administração de Tarefas, clique em avançar.

Na próxima tela selecione a opção desejada, como por exemplo Funcionário e avance.

Nessa próxima tela é possível ver quais tarefas estão vinculadas.

Ou então, ao editar o cadastro desejado (Funcionário por exemplo) e verificar “Histórico de

Tarefas” é possível ver se há alguma tarefa vinculada.

2.7) Exposição a Fatores de Risco.

**ATENÇÃO!**

**A partir da versão 10.80, no campo 15 do relatório sairão todas as medições existentes que de alguma forma vincule-se ao funcionário:**

Exemplo: Se existir uma medição por função, outra por seção e outra por lotação, sendo que, todas se enquadram nas funções que o funcionário desempenhou na empresa, nas seções ou lotações por onde passou, no campo 15 serão impressas todas elas.

**A alteração de qualquer um dos campos 15.2 a 15.8 implica, obrigatoriamente, na criação de uma nova linha, com discriminação do período, repetindo as informações que não foram alteradas.**

Acesse SMT / Seg e Med do Trab / PPRA|PGR  / Reconhecimento e Avaliação de Risco.

PPP – Campo 15.1 – Períodos

* Para identificarmos se os períodos impressos estão corretos, temos que verificar nas medições os campos “Data Início” e “Data Fim”.

**Origem no banco de dados:   
VPPRAMEDICOES.DATA  
VPPRAMEDICOES.DATATERMINOMEDICAO**

PPP – Campo 15.2 – Tipo

* Estes podem ser Físicos, Químicos, Biológicos, Ergonômicos ou de Acidentes.

Acesse SMT / Seg e Med do Trab / PPRA|PGR / Riscos.

Verifique dentro do risco que está especificado na medição qual o tipo definido.

**Origem no banco de dados:**

**VAGENTE.NOME**

PPP – Campo 15.3 – Fator de Risco

Acesse SMT / Seg e Med do Trab / PPRA / Medições de Risco.

**Origem no banco de dados:**

**VPPRARISCOS.NOMEITEMRISCO**

PPP – Campo 15.4 – Intensidade / Concentração

**Origem no banco de dados:   
Quando quantitativo composto por: VPPRAMEDICOES.OPERADOR, PPRAMEDICOES.VALORQUANTITATIVO e VPPRAMEDICOES.CODUND  
Quando Qualitativo composto por: VTPMEDQUALIITEMRISCO.DESCRICAO e PPRAMEDICOES.CODUND**

PPP – Campo 15.5 – Técnica Utilizada

**Origem no banco de dados:**

**VPPRATECNICASMEDICAO.DESCRICAO**

PPP – Campo 15.6 – EPC Eficaz (S/N)

* Para que o sistema considere um EPI como EPC, este deve ter seu empréstimo realizado através do “Assistente de Empréstimo Automático de EPI”, sendo esse realizado para um “Local de Trabalho”.

**Importante !**

Para a correta impressão do EPC no relatório PPP, assim como o fornecimento, a Avaliação de Riscos também deverá ser realizada utilizando o "Local de Trabalho".

Acesse SMT / Seg e Med do Trab / Empréstimo Automático de EPI.

* Para que o EPC seja impresso como Eficaz (SIM) é necessário marcar a opção “Eficaz” no empréstimo, o EPC não pode estar em estado “Inválido” ou “Processo de Higienização”, e deve estar dentro da validade.

**Origem no banco de dados: Se houve empréstimo de EPI ao local de trabalho em que o funcionário esteve alocado e se for ligado ao risco em que houve a medição, é informada a string "S". As tabelas envolvidas são: VEMPRESTIMOEPI, VHISTEPISEGURANCA**

PPP – Campo 15.7 – EPI Eficaz (S/N)

Para que o EPI seja impresso como Eficaz (SIM) é necessário marcar a opção “Eficaz” no empréstimo, o EPI não pode estar em estado “Inválido” ou “Processo de Higienização”, e deve estar dentro da validade.

**Origem no banco de dados: Se houve empréstimo de EPI ao funcionário; Se for ligado ao risco em que houve a medição; Se o EPI não estiver marcado como inválido ou em estado de higienização; Será informada a string "S". As tabelas envolvidas são: VHISTEPISEGURANCA, VEMPRESTIMOEPI, VEPI**

PPP – Campo 15.8 – CA EPI

Acesse SMT / Seg e Med do Trab / Catálogo de EPI’s

à Verifique dentro do EPI na Guia Identificação.

PPP – Campo 15.9 – Atendimento aos requisitos das NR-06 e NR-09 do MTE pelos EPI’s

informados (S/N).

à Essas informações do campo 15.9 deverão ser informadas no ato da geração do PPP quando a tela abaixo aparecer.

2.8) Responsável Pelos Registros Ambientais.

Acesse SMT / Seg e Med do Trab / PPRA|PGR  / Responsável pelos Registros Ambientais.

Edite o cadastro do Responsável.

PPP – Campo 16.1 – Período

**Origem no banco de dados:   
VRESPREGAMBIENTAL.DATAINICIAL  
VRESPREGAMBIENTAL.DATAFINAL**

PPP – Campo 16.2 – NIT

**Origem no banco de dados:**

**VRESPREGAMBIENTAL.NIT**

PPP – Campo 16.3 – Registro de Conselho de Classe

**Origem no banco de dados:**

**VRESPREGAMBIENTAL.REGCONSELHOCLASSE**

PPP – Campo 16.4 – Nome do Profissional Legalmente Habilitado

**Origem no banco de dados:**

**PPESSOA.NOME**

2.9) Exames Médicos Clínicos e Complementares (Quadros I e II, da NR-07)

PPP – Campo 17 - Exames Médicos Clínicos e Complementares (Quadros I e II, da NR-07)

**OBS: Segundo definição do conselho nacional de medicina, este campo não deverá ser apresentado no PPP.**

<http://www81.dataprev.gov.br/sislex/paginas/38/INSS-DC/2003/99.htm>

2.10) Responsáveis pela Monitoração Biológica

PPP – Campo 18 – Responsáveis pela Monitoração Biológica.

Acesse SMT / Seg e Med do Trab / PCMSO /Responsáveis pelas Monitorações Biológicas.

PPP – Campo 18.1 – Período

**Origem no banco de dados:   
VRESPMONBIOLOGICA.DATAINICIAL  
VRESPMONBIOLOGICA.DATAFINAL**

PPP – Campo 18.2 – NIT

**Origem no banco de dados:**

**VRESPMONBIOLOGICA.NIT**

PPP – Campo 18.3 – Registro Conselho de Classe

**Origem no banco de dados:**

**VRESPMONBIOLOGICA.REGCONSELHOCLASSE**

PPP – Campo 18.4 – Nome do Profissional Legalmente Habilitado

**Origem no banco de dados:**

**PPESSOA.NOME**

2.11) Responsáveis pelas informações

PPP – Campo 19 – Data Emissão PPP

à Data do dia da geração (Data do Servidor)

2.12) Representante Legal da Empresa

PPP – Campo 20.1 – NIT

PPP – Campo 20.2 – Nome

à Nessa tela é informado quem é o representante legal da empresa.

Acesse Cadastros / Funcionários – Edite o cadastro do funcionário

à Acesse a guia “Informações Pessoais / Identificação”.

**Origem no banco de dados:**

**PPESSOA.NOME**
