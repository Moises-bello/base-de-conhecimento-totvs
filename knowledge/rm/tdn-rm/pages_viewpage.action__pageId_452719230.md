---
content_hash: f01ccb1addd2c2b535f82eaaa2e50d4da6433c4563d484874d939cae60d8bcdf
fetched_at: '2026-06-29T00:10:04.670416+00:00'
page_id: '452719230'
product: rm
source: tdn-rm
title: PPP – Perfil Profissiográfico Previdenciário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719230
version: 13
---

**PPP – Perfil Profissiográfico Previdenciário**

O Relatório Perfil Profissiográfico Previdenciário - PPP estará disponível no Menu SMT – Relatórios - PPP e possui um assistente para a sua geração

Passo 1 – Informar Funcionário e Representante Legal da empresa;

**Obs.: Dada a entrada do PPP eletrônico em**  **o limitará a exibição de funcionários admitidos até**  **.**

Passo 2 – Selecionar a profissiografia ( função, tarefas da função, quadro de lotação, tarefas do quadro de lotação, funções do posto de trabalho, tarefas das funções do posto de trabalho e tarefas do funcionário).

**Origem dos campos do Relatório PPP**

1-CNPJ do Domicílio Tributário/CEI/CAEPF/CNO

Sempre prevalecerá o registro que conter o CEI. Origem no banco de dados: PSECAO.CEI PSECAO.CGC.

Origem no sistema: RM Vitae – Cadastro de Seção.

Foi disponibilizado no Parametrizador o campo "Exibir o CNPJ do Domicilio Tributário/CEI da coligada do funcionário":

Se o campo "Exibir o CNPJ do Domicilio Tributário/CEI da coligada do funcionário" estiver desmarcado, na emissão do PPP será exibido o CNPJ da seção do funcionário.

Se o campo "Exibir o CNPJ do Domicilio Tributário/CEI da coligada do funcionário" estiver marcado, na emissão do PPP será exibido o CNPJ da coligada referente à filial (informada na seção) do funcionário.

Atenção: o parâmetro "Exibir o CNPJ do Domicilio Tributário/CEI da coligada do funcionário" está disponível a partir do patch 12.1.34.221.

2-Nome Empresarial

Origem no banco de dados: GCOLIGADA.NOME.

Origem no sistema: RM Vitae – Cadastro de Coligadas.

3-CNAE

Origem no banco de dados: PSECAO.ATIVECONOMICA.

Origem no sistema: RM Vitae – Cadastro de Seção.

4-Nome do Trabalhador

Origem no banco de dados: PFUNC.NOME.

Origem no sistema: RM Vitae – Cadastro de Funcionário.

5-BR/PDH

Origem no banco de dados: PPESSOA.BRPDH.

Origem no sistema: RM Labore.

6-CPF

Origem no banco de dados: PPESSOA.CPF.

Origem no sistema: RM Vitae – Cadastro de Pessoa.

7-Data do Nascimento

Origem no banco de dados: PPESSOA.DTNASCIMENTO.

Origem no sistema: RM Vitae – Cadastro de Pessoa.

8-Sexo (F/M)

Origem no banco de dados: PPESSOA.SEXO.

Origem no sistema: RM Vitae – Cadastro de Pessoa.

9-Matrícula do Trabalhador no eSocial:

Origem no banco de dados: PFUNC.MATRICULAESOCIAL.

Origem no sistema: RM Labore – Cadastro de Funcionário.

10-Data de Admissão

Origem no banco de dados: PFUNC.DATAADMISSAO.

Origem no sistema: RM Labore – Cadastro de Funcionário.

11-Regime Revezamento

Origem no banco de dados: PFUNC.REGIMEREVEZAMENTO.

Origem no sistema: RM Labore.

12-CAT Registrada

1- Data do Registro

Origem no banco de dados: VOCORRENCIA.DATAHORA.

Origem no sistema: RM Vitae SMT – Cadastro de Ocorrência de Acidente de Trabalho.

2- Número da CAT

Origem no banco de dados: VOCORRENCIA.REGISTROINSS.

Origem no sistema: RM Vitae SMT – Cadastro de Ocorrência de Acidente de Trabalho.

**Obs.: Conforme orientação da Consultoria de Segmentos ([eSocial - PPP Eletrônico](https://tdn.totvs.com/pages/viewpage.action?pageId=727939942)) os campos que tratam "período" no relatório PPP estarão limitados a extração de dados até 31/12/2022.**

13-Lotação e Atribuição

Quando não houver uma data de fim clara para o registro, poderá ser adotado conforme o caso, a data de início do próximo registro - 1 dia ou a data de demissão.  
Caso o funcionário esteja alocado em um tomador de serviço, as informações provenientes deste tomador prevalecerão sobre as informações diretas do funcionário.

Observação:  
Caso a parametrização do tipo de gestão de hierarquia do sistema tenha sofrido alguma alteração os registros ficarão salvos na tabela VHHISTORICOHIERARQUIAUTILIZADA. Ao gerar o PPP o sistema irá  se basear nas datas de inicio e fim dessa tabela de cada tipo de hierarquia (Chefe/supervisor ou Posições) para o preenchimento dos campos de Cargo e Função do funcionário selecionado.

13.1-Período

Origem no banco de dados: PFHSTFCO.DTMUDANCA PFHSTSEC.DTMUDANCA PHSTOCORRENCIA.DTMUDANCA PSUBSTCHEFE.DATAINICIO PSUBSTCHEFE.DATAFIM VTOMADORSERVICOVINC.DATAINICIAL VTOMADORSERVICOVINC.DATAFINAL.

Origem no sistema: RM Labore RM Vitae – Histórico de Função RM Vitae – Histórico de Seção RM Labore.

**Obs.: Conforme orientação da Consultoria de Segmentos () os campos que tratam "período" no relatório PPP estarão limitados a extração de dados até 31/12/2022.**

13.2-CNPJ/CEI/CAEPF/CNO

Sempre prevalecerá o registro que conter o CEI.

Origem no banco de dados: PSECAO.CGC PSECAO.CEI FCFO.CEI FCFO.CGCCFO.  
Origem no sistema: RM Labore RM Vitae – Cadastro de Seção RM Labore.

13.3-Setor

Origem no banco de dados: PSECAO.DESCRICAO.

Origem no sistema: RM Vitae – Cadastro de Seção.

13.4-Cargo

Origem no banco de dados: PFUNCAO.NOME.

Origem no sistema: RM Vitae – Cadastro de Função.

13.5-Função

Origem no banco de dados: Se houver registro na tabela PSUBSTCHEFE será informada a string "Chefe" Se houver registro na tabela PSUBSTSUP será informada a string "Supervisor".

Origem no sistema: RM Labore.

13.6-CBO

Após o ano de 2002 foi reformulada a tabela de CBO, portanto quando um funcionário esteve atuante durante esta transição, estará sujeito a dois códigos de CBO um para antes de 2002 e outro para depois.

Origem no banco de dados: PFUNCAO.CBO PFUNCAO.CBO2002.

Origem no sistema: RM Vitae – Cadastro de Função.

13.7-Cód. GFIP/eSocial

Origem no banco de dados: PHSTOCORRENCIA.CODOCORRENCIA VTOMADORSERVICOVINC.CODGFIP.

Origem no sistema: RM Labore.

14-PROFISSIOGRAFIA

Quando não houver uma data de fim clara para o registro, poderá ser adotado conforme o caso, a data de início do próximo registro - 1 dia ou a data de demissão.  
A origem das informações de profissiografia deverá ser selecionada pelo usuário na tela de parâmetros que precede a emissão do relatório.

14.1-Período

Origem no banco de dados: PFHSTFCO.DTMUDANCA VPPRAHISTTAREFASFUNCAO.DATA VPPRAHISTTAREFASFUNCAO.DATASAIDA PFHSTSEC.DTMUDANCA VPPRAHISTTAREFALOTACAO.DATA VPPRAHISTTAREFALOTACAO.DATASAIDA VHISTPOSTOPFUNC.DATA VHISTPOSTOPFUNC.DATASAIDA VPPRAHISTAREFAFUNCAOPOSTO.DATA VPPRAHISTAREFAFUNCAOPOSTO.DATASAIDA VPPRAHISTTAREFAPESSOAL.DATA VPPRAHISTTAREFAPESSOAL.DATASAIDA.

Origem no sistema: RM Labore.

**Obs.: Conforme orientação da Consultoria de Segmentos () os campos que tratam "período" no relatório PPP estarão limitados a extração de dados até 31/12/2022.**

14.2-Descrição das Atividades

Origem no banco de dados: PFUNCAO.DESCRICAO VTAREFA.DESCRICAO VMEMO.VALMEMO (Referenciando VLOTACAO.IDOBSERVACAO) VMEMO.VALMEMO (Referenciando VPOSTOFUNCAO.CODMEMOOBS).

Origem no sistema: RM Vitae – Histórico de Função RM Vitae – Histórico de Seção RM Vitae – Histórico de Tarefas RM Vitae SMT – Histórico de Posto de Trabalho.

15 - EXPOSIÇÃO A FATORES DE RISCO

15.1 - Período

Origem no banco de dados: VPPRAMEDICOES.DATA VPPRAMEDICOES.DATATERMINOMEDICAO.

Origem no sistema: RM Vitae – Avaliação / Medição de Risco.

**Obs.: Conforme orientação da Consultoria de Segmentos () os campos que tratam "período" no relatório PPP estarão limitados a extração de dados até 31/12/2022.**

15.2-Tipo

Origem no banco de dados: VAGENTE.NOME

Origem no sistema: RM Vitae – Cadastro de Agente.

15.3-Fator de Risco

Origem no banco de dados: VPPRARISCOS.NOMEITEMRISCO Origem no sistema: RM Vitae – Cadastro de Riscos.

15.4-Itens/Conc

Origem no banco de dados: Quando quantitativo composto por: VPPRAMEDICOES.OPERADOR, PPRAMEDICOES.VALORQUANTITATIVO e VPPRAMEDICOES.CODUND Quando Qualitativo composto por: VTPMEDQUALIITEMRISCO.DESCRICAO e PPRAMEDICOES.CODUND.

Origem no sistema: RM Vitae – Cadastro de Riscos.

15.5 - Técnica Utilizada

Origem no banco de dados: VPPRATECNICASMEDICAO.DESCRICAO Origem no sistema: RM Vitae – Cadastro de Técnicas de Medição.

15.6-EPC Eficaz(S/N)

Origem no banco de dados: Se houve empréstimo de EPI ao local de trabalho em que o funcionário esteve alocado e se for ligado ao risco em que houve a medição, é informada a string "S". As tabelas envolvidas são: VEMPRESTIMOEPI, VHISTEPISEGURANCA.

Origem no sistema: RM Vitae – Catálogo de EPI.

15.7-EPI Eficaz (S/N)

Origem no banco de dados: Se houve empréstimo de EPI ao funcionário; Se for ligado ao risco em que houve a medição; Se o EPI não estiver marcado como inválido ou em estado de higienização; Será informada a string "S". As tabelas envolvidas são: VHISTEPISEGURANCA, VEMPRESTIMOEPI, VEPI.

Origem no sistema: RM Vitae – Catálogo de EPI.

15.8-CA EPI

Origem no banco de dados: VCUSTOEPI.CA, porém somente será exibido o CA do EPI quando os campos VEPI.AQUISICAO e VCUSTOEPI.DTAQUISICAO coincidirem. Origem no sistema: RM Vitae – Catálogo de EPI.

15.9 - Atendimento aos requisitos das NR-06 e NR-01 do MTP pelos EPI informados (\*)

A origem dos dados deste campo deverá ser informada pelo usuário na tela de parâmetros que precede a emissão do relatório.

16-RESPONSÁVEL PELOS REGISTROS AMBIENTAIS

16.1-Período

Origem no banco de dados: VRESPREGAMBIENTAL.DATAINICIAL VRESPREGAMBIENTAL.DATAFINAL.

Origem no sistema: RM Vitae SMT – Cadastro de Responsável pelos Registros Ambientais.

**Obs.: Conforme orientação da Consultoria de Segmentos () os campos que tratam "período" no relatório PPP estarão limitados a extração de dados até 31/12/2022.**

16.2-CPF

CPF da pessoa pessoa informada nos Responsáveis pelos Registros Ambientais.

Origem no banco de dados: PPESSOA.CPF.

Origem no sistema: RM Vitae SMT – Cadastro de Responsável pelos Registros Ambientais.

16.3-Registro Conselho de Classe

Origem no banco de dados: VRESPREGAMBIENTAL.REGCONSELHOCLASSE.

Origem no sistema: RM Vitae SMT – Cadastro de Responsável pelos Registros Ambientais.

16.4-Nome do Profissional Legalmente Habilitado

Origem no banco de dados: PPESSOA.NOME.

Origem no sistema: RM Vitae – Cadastro de Pessoa.

17-Data Emissão PPP

Data atual.

18-REPRESENTANTE LEGAL DA EMPRESA

Este campo deverá ser informado na tela de parâmetros que precede a emissão do relatório.

18.1-NIT do Representante Legal

Origem no banco de dados: PFUNC.PISPASEP.

Origem no sistema: RM Labore - Cadastro de Funcionário.

18.2-Nome do Representante Legal

Origem no banco de dados: PFUNC.NOME.

Origem no sistema: RM Labore - Cadastro de Funcionário.

**Observações**

- De acordo com a Resolução 1715, de 08/01/2004, do Conselho Federal de Medicina que proibiu os médicos do trabalho de prestarem informações relativas aos exames médicos realizados nos trabalhadores para preenchimento do Perfil Profissiográfico Previdenciário por parte do empregador, o campo 17 não será preenchido.

- O campo "Descrição para o PPP" aparecerá no relatório do PPP (campo 14) se a profissiografia for por função.

**Importante !**

Para a correta impressão do EPC no relatório PPP, assim como o fornecimento, a Avaliação de Riscos também deverá ser realizada utilizando o "Local de Trabalho".
