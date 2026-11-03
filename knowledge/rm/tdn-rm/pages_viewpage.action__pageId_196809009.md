---
content_hash: f6f2a9854a36ba54b20435c934ecca68dddb6a114296d040464eda196547672c
fetched_at: '2026-06-29T00:06:00.480575+00:00'
page_id: '196809009'
product: rm
source: tdn-rm
title: Release Versão 12.1.6
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=196809009
version: 7
---

Topo

## 

1RH1

* TOTVS Automação de Ponto
1RH2

* TOTVS Folha de Pagamento
1RH3

* TOTVS Gestão de Pessoas
1RH4

* TOTVS Segurança e Medicina do Trabalho

## 

2BO1

* TOTVS Estoque, Compras e Faturamento
2BO2

* TOTVS Gestão Financeira
2BO3

* TOTVS Gestão Fiscal
2BO4

* TOTVS Gestão Patrimonial
2BO5

* TOTVS Gestão Contábil

## 

3EDU1

* TOTVS Educacional
3EDU2

* TOTVS Gestão Bibliotecária
3EDU4

* TOTVS Processo Seletivo
3EDU4

* TOTVS Avaliação e Pesquisa

## 

4CP1

* TOTVS Construção e Projetos
4CP2

* TOTVS Incorporação
4CP3

* ETO - Engenharia sob encomenda

## 

5CRM1

* TOTVS Gestão de Relacionamento com Cliente

---

# **RH**

# **RH**

1trueRH1Automação de Ponto

 [Help](http://wikihelp.totvs.com.br/WikiHelp/PTO/PTO.Chronus.aspx) e  do TOTVS Automação de Ponto.

Otimizado(a):

* + Cálculo do espelho quando utilizado linked server nos filtros.
  + Processo de Alteração por escala - Horário e Descanso.
  + Processo global de batidas.
  + Recálculo do espelho de ponto.
  + Lançamento de abonos considerando o limite de abono cadastrado.
  + Cadastro de Horário de Sobreaviso, passando a ser obrigatório o preenchimento do campo Hora Fim.
  + Lançamento de Dia Ponte, passando a ser obrigatório o preenchimento do período de compensação.
  + Cadastro de abonos através da versão em Delphi.
  + Tela de log do recálculo do ponto.
  + Alteração da jornada.
  + Aplicação de filtro por perfil na visão de visualização de cartão de ponto.
  + Impressão da justificativa de autorização de extra no relatório de espelho do cartão.
  + Aprovação de abonos quando a coligada for diferente de 1.
  + Geração do relatório de exceções com ordenação por seção.
  + Importação de batidas de visitante priorizando crachá.
  + Leitura do horário planejado para não gerar horas de falta em dias posteriores a demissão.
RH2Folha de Pagamento

 [Help](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.Labore.aspx) e  do TOTVS Folha de Pagamento.

Implementado o parâmetro para informação do termino do auxílio doença de responsabilidade da Empresa com duração de 30 dias (MP 664).

 Otimizado(a):

* Log da alteração global de campos do cadastro quando seleciona para alterar o campo Código da Seção. O sistema passa a exibir no log do processo o resultado da fórmula quando o campo não for preenchido ou existir algum retorno inválido.
* Processo de Diferença Salarial para permitir o cálculo da diferença do evento com código de cálculo 10 - Atrasos.
* Cálculo do salário hora para o funcionário que possue salário composto.
* Processo de alteração global de tomadores.
* Importação de Empréstimo Consignado Febraban. O sistema passa a ignorar o campo de data de pagamento quando não for informado no arquivo (posição 98 até 105) ou nos parâmetros de tela.
* Importação MIMS quando o parâmetro 'Gera Ficha de Registro sequencial pelo sistema' está desabilitado, possibilitando não informar a ficha de registro para casos de alteração de dados.
* Validação de página do wizard para execução de Contabilização Retroativa.
* Consideração da marcação do fato gerador no momento de geração dos Lançamentos Financeiros.
* Visualização do botão Executar Novamente no processo da RAIS.
* Importação de dados pessoais na importação MIMS.
* Lista de colunas a serem ignoradas na importação do SAP.
* Edição do cadastro de férias.
* Geração dos lançamentos financeiros pela GRRF.
* Visualização do saldo de dias do período aquisitivo ao aprovar férias no Portal.
RH3Gestão de Pessoas

 [Help](http://wikihelp.totvs.com.br/WikiHelp/RHU/RHU.Vitae.aspx) e  do TOTVS Gestão de Pessoas.

Otimizado(a):

* Envio de email para os avaliadores de uma avaliação de desempenho.
* Cadastro de novos Professores. Ao utilizar o recurso "Localizar pessoa", a unicidade do CPF não será validada quando não houver alteração no mesmo.
* Apresentação das Metas no Portal, passando a validar o flag "exige aceite dos avaliados".
* Validação de abonos.
* Chamada da validação de unicidade de pessoas.

Melhoria:

* Processo "Criar Atendente Agilis" passando a contemplar os campos Hierarquia e Localidade, que são obrigatórios para o cadastro de atendente.
* Ao salvar um candidato.
RH4Segurança e Medicina do Trabalho

 [Help](http://wikihelp.totvs.com.br/WikiHelp/SMT/SMT.VitaeSegurancaTrabalho.aspx) e  do TOTVS Segurança e Medicina do Trabalho.

* Adequações nos Atestados Médicos para atender solicitações do Labore.
* Disponibilizado novo relatório ASO. Passando a ser executado através do processo "Atestado de Saúde Ocupacional" , no cadastro da Consulta do anexo do Funcionário.
* Otimizado o lookup de Seção no Assistente de Agendamento Automático de exames, passando a listar somente as seções da coligada corrente.
* Otimizada a validação da geração de exames quando os exames são definidos como Mudança de Função ou Periódicos conforme definição da NR-7.
* Realizada uma otimização para acelerar a execução do processo.

 

# **BACKOFFICE**

## **BackOffice**

false2trueBO1Estoque, Compras e Faturamento

[Help](http://wikihelp.totvs.com.br/WikiHelp/EST/sEST.Nucleus.aspx) e  do TOTVS Gestão de Estoque, Compras e Faturamento.

* Inclusão de cadastro de veículos de terceiros.
* Totvs Colaboração: Inclusão Automática de Movimento CT-e.

Ajuste(s):

* Integração com o FLUIG em inclusão de movimentos.
* Impressão do DACTE (campos de endereços longos, unidade de medida, Logo da Filial).

Melhoria(s):

* Processo de inclusão de movimento com arquivo XML.
* Processo de aviso de cotação a fornecedor via WEB.
* Visualização dos últimos movimentos de cotação.
* Design da tela de inclusão de movimento com arquivo XML.
* Parametrizador de tabelas de classificação.
* Processo de Ressuprimento e Análise de para não permitir a Análise de itens com diferentes status.
* Processo de geração de Relatório para adequação ao novo modelo.
* Atualizar o status do orçamento de contrato ao excluir o faturamento do mesmo.
* Importar arquivos Totvs Colaboração.
BO2Gestão Financeira

[Help](http://wikihelp.totvs.com.br/WikiHelp/FIN/FIN.Fluxus.aspx) e  do TOTVS Gestão Financeira.

* Ajuste na geração do nosso número quando o processo é sequencial para que não se perca o sequencial gerando números de 2 em 2.
* Lei 13.137/2015 para a cumulatividade diária de retenção do PCC.

Melhoria(s):

* Tela do Fluxo de Caixa para que os campos do filtro fiquem do mesmo tamanho quando a resolução da tela é baixa.
* Processo de acordo para que o campo Valor Original do item de baixa fique com o valor atualizado quando durante o processo é inserido um acréscimo.
* Processo de baixa financeira onde existem parcelas do SGI a vencer.
* Processo de cancelamento da baixa limpando o campo FLAN.DATAPAG no caso de cancelamento da mesma.
* Processo de rateio de centro de custo na contabilização para que não despreze o ultimo rateio de pequeno valor.

Otimização:

* Processo da THREAD apenas no executável (Delphi) para calcular valor líquido.
* Processo de baixa de lançamento recebimento via cheque. Ao baixar o sistema não carregava o CODCOLIGADA do contexto.
* Processo de cancelamento de lançamento. Agora o processo de reabrir o financeiro é executado corretamente.
* Processo de cancelamento de baixa para clientes que utilizam base Oracle.
* Processo de cancelamento de baixa para mais de lançamento ao mesmo tempo.
* Visão de lançamentos quando a opção de filtrar dados do RM Classis estiver habilitada na preferência de usuário.
* Log do processo sobre geração de lançamento de adiantamento quando ocorre baixa a maior.
* Processo de importação de lançamentos via conceito.
BO3Gestão Fiscal

[Help](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.Liber.aspx) e  do TOTVS Gestão Fiscal.

* Evoluções no processo de simulação da apuração do IRPJ e CSLL
* Otimização do processo de geração da NF-e através do TOTVS Colaboração 2.0 para permitir a geração dos grupos de tributação outros para o PIS e para o COFINS informando os valores zerados
* Implementação da Rotina federal ECF – Escrituração Contábil Fiscal
* Foi uma modificação para que os Períodos de Apuração dos meses de Junho e Julho de 2015 dos Tributos com o tipo tributo "Retenção PIS, COFINS e CSLL" não consistam a validação de que exista lançamentos no período, na hora de excluir ou alterar um período, esta modificação e para atender a Legislação (lei 13.137).

Modificado:

* Processo de geração de NFS-e para ajustar automaticamente a máscara do item da lista de serviço para os municípios Novo Hamburgo - RS e São Leopoldo - RS
* Processo de geração do XML para a NF-e do TOTVS Colaboração 2.0 para não gerar as TAG’s de complemento em branco.
* Processo para considerar no XML da NF-e os casos em que o número sequencial do item foi alterado.
BO4Gestão Patrimonial

[Help](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.Bonum.aspx) e  do TOTVS Gestão Patrimonial.

Atualização:

* Rotina de Fechamento de Período relativo à atualização de período já fechado.
* Rotina de importação de patrimônio via conceito
* Método de validação da inclusão de patrimônio de terceiros.
* Parametrização de restrição de aquisição de patrimônio pelo valor mínimo.
* Método de baixa de patrimônio para SGDB Oracle

Ajuste:

* Máquina de cálculo para que só deprecie patrimônios não tenham depreciação acumulada maior que o valor base corrigido.
* Máquina de cálculos de depreciação para buscar a avaliação residual vigente dos patrimônios corretamente.
BO5Gestão Contábil

[Help](http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.Saldus.aspx) e  do TOTVS Gestão Contábil.

* Atualização do método de totalização dos fatos contábeis do SPED
* Correção na contabilização da baixa do lançamento financeiro quando utilizamos a classificação por centro de custo e aplicamos a classificação no item do evento, utilizando o centro de custo apenas no débito.
* Adequação na apuração virtual para atender a forma de tributação Lucro Real Mensal Estimado.

Otimizado:

* Otimizado a inconsistência na associação do plano de contas paralelo quando o cliente utiliza a conta gerencial para ser enviada no SPED Contábil e o código da conta possui mais de 25 caracteres.
* Otimizado no evento contábil a nova opção ==> "Não arredondar valor processado pela Fórmula".

Ajuste(s):

* Geração do razão auxiliar no SPED Contábil que não estava gerando o registro I500 e I510.
* Inversão de informações de Item Contábil e Classe de Valor nas partidas de estorno ao gerar lançamentos contábeis para integração por mensageria única.

Melhoria(s):

* Apuração virtual para apurar resultado considerando o centro custo, isto em função da ECF.
* Ferramenta de Demonstrações Contábeis que possibilita ao usuário identificar se que considerar o total de débito, total de crédito ou movimentação do filtro genérico.

Modificado:

* Cadastro de lotes de forma a permitir que o sistema TOTVS Gestão Fiscal, da mesma forma que o TOTVS Gestão Contábil, possa incluir lotes respeitando as regras para inclusão.
* Processo de Demonstração Contábil de forma a permitir que as informações sejam exibidas em ambiente 3 camadas.
* Processo de Demonstração Contábil de forma a permitir que as informações sejam exibidas em ambiente 3 camadas.
* Processo de desagrupamento de forma a validar as permissões do usuário que está executando o processo.
* Processo de desagrupamento de lançamentos para que sejam possíveis desagrupar lançamentos de outros sistemas.

EDUCACIONAL

## **Educacional**

3trueEDU1Educacional

[Help](http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.totvsEducacional.aspx) e  do TOTVS Educacional.

* Adequação da mensagem informativa para o usuário ao invés de exibir como um erro para o usuário.
* Ao utilizar um dispositivo configurado com o idioma inglês, o professor poderá utilizar o caractere "." como separador das casas decimais.
* Alterado o processo Mudança de Turma/Turno, para observar o parâmetro “Aproveitar contrato”. Regras de aproveitamento do contrato, somente para Ensino básico:
  1. Plano de pagamento das matrizes de origem e destino devem ser o mesmo.
  2. O status da matrícula de origem deve estar configurado para não cancelar o contrato e o status da matrícula de destino, deve estar configurado para exigir contrato.
  3. Centro de custo das matrizes de origem e destino devem ser o mesmo.
  4. Default contábil das matrizes de origem e destino devem ser o mesmo.

 Ajuste(s):

* Cadastro do aluno (necessidades e recursos especiais) para o ENADE 2015.
* Concessão de permissão de Edição do item Matrícula Isolada no perfil do usuário do Educacional.
* Digitação da nota da etapa e nota de avaliação no EducaMobile.
* Validação do botão "Avançar" no processo de mudança de turma/turno.
* Cadastro de Histórico do Ensino Básico, permitindo que letras ou caracteres especiais sejam informados no campo Carga Horária.
* Processo de geração de plano de aula permitindo que o processo seja executado selecionando várias turmas/disciplinas.
* Incluído filtro por período letivo no relatório EDUREL0012 do book de relatórios do Educacional.
* Melhoria para alterar o status de matrícula após uma alteração de informações de pagamento de professores no cadastro de Professores da Turma/Disciplina.
* No menu Currículo e Oferta | Professores | Anexo | Currículo Vitae | Anexos | Projetos de pesquisa, deverá permitir editar os campos “Nome do projeto em inglês” e “Descrição do projeto em inglês”.
* Verificação da existência de registros com dados inválidos referentes a necessidades/recursos especiais necessários ao ENADE.

Otimizado:

* Assistente de Repasse de Bolsa, para permitir a opção de “cancelar repasses” quando o valor do lançamento for igual ao valor do repasse. Nesta situação, somente a baixa do lançamento será cancelada.
* Cadastro de Professores, para aceitar somente caracteres numéricos nas telas do anexo “Currículo e ofertas” para os campos Ano e Mês.
* Portal, para permitir acessar o link Rematrícula quando o usuário logado é o responsável acadêmico.
* Processo de matricular aluno na disciplina para que seja vindo a situação atual de matrícula das disciplinas que o aluno está matriculado.
Edu2Gestão Bibliotecária

[Help](http://wikihelp.totvs.com.br/WikiHelp/BIB/BIB.Biblios.aspx) e do TOTVS Gestão Bibliotecária.

* Ajustes na integração Financeira/Contábil Educacional x Protheus para otimização e melhor tratamento das informações que são trafegas.
* Definido o valor default e obrigatoriedade para o campo Frequência de publicação.
* Inclusão de validação para permitir que sejam inseridos apenas valores numéricos nos campos volume, ano e quantidade da tabela Pedidos para a Biblioteca.
* O campo ano publicação passou a permitir apenas números.
* Otimizado processo de importação de arquivos texto para cadastro de publicação.
EDU3Processo Seletivo

[Help](http://wikihelp.totvs.com.br/WikiHelp/EDUPS/EDUPS.processoSeletivo.aspx) e  do TOTVS Processo Seletivo.

Otimizado:

* Consulta dos boletos do candidato.
* Inscrição de candidato com relação as informações de cotas.
* Log do processo de chamada de candidatos aprovados.
* Processo de cópia de processos seletivos.
EDU4Avaliação e Pesquisa

[Help](http://wikihelp.totvs.com.br/WikiHelp/TST/TST.testis.aspx) e  do TOTVS Avaliação e Pesquisa.

* Otimizado processo de execução de provas pelo TOTVS Executor, via webservice (online).

PROJETOS

## **Projetos**

4trueCP1Construção e Projetos

[Help](http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Solum.aspx) e  do TOTVS Obras e Projetos.

* Inclusão dos campos Nome e Descrição da tarefa nas visões.
* Criação de Filtro Implícito para todas as funcionalidades que contemplam tarefas afim de permitir associação de determinados usuários às respectivas disciplinas.
* Atualização realizada no processo Backup / Restore. Desta forma torna-se possível importar apenas recursos globais que são utilizados pelo projeto.
* Integração TOP x BackOffice Protheus - Ajuste na exclusão de movimento gerado a partir do período de contrato.
* Liberado acesso ao anexo de produtos faturados no contrato e permitida a inclusão de dedução de produtos faturados no processo de liberação de período quando integrado com o Protheus.

Reformulação:

* Aba de Custo Horário no cadastro de Insumos, unificando as abas de Planilhas e Campos Livres.
* Tela no processo de Alteração Geral de Insumos.
* Tela no processo de Alteração Geral de Composições.
* Tela de projetos incluindo uma anexo que permite visualização dos últimos projetos acessados pelos usuários.

Melhoria(s):

* TOP Mobile que incluem alterações no cadastro de ciclo de transporte e no processo de apontamento, assim como na geração de relatório do Ciclo, além de alterações no processo de Apropriação e Revaloração, geração de Arquivo para Manutenção de Ativos e na visão de apontamentos.
* Performance da execução da Curva S em ambiente Oracle, com a utilização de grande massa de insumos globais, com redução do tempo de cerca de cerca de 19 minutos para 20 segundos na execução da consulta.

Migração:

* Funcionalidades Projetos de Licitação, Equalização, Contrato e Negociação do módulo de Concorrência Eletrônica para plataforma .NET.
* Funcionalidade Definir Total para plataforma .NET.
* Funcionalidade Transformar Recursos Globais em Locais para Plataforma .NET.

Ajuste(s):

* Campos Produtivo e Improdutivo para recursos de composição.
* Realização de revisão de alteração de escopo em projetos com máscara de tarefa superior a máscara default em ambiente Oracle. Ajuste no carregamento dos parâmetros de projetos copiados para o projeto destino.
* Exportação de Planilha de Atividades para MS Excel.
* Geração de relatórios em que o título estoure 30 caracteres.
* Seleção da planilha no arquivo, na importação de composição e insumos do MS Excel. A mesma estava sendo recuperada conforme o nome, e caso não fosse encontrado não era selecionada a primeira planilha, isto em ambientes sem a instalação do MS Excel.
* Parâmetro BDI.
* Processo de rastrear movimentos de integração TOP x Protheus - Modelo antigo.
* Processo de salvamento de alterações no item de pedido de material em ambiente Oracle.
* Menu Server Fluig.
* Processo Backup/Restore.
* Processo de cópia de itens. Com este, torna-se possível a cópia de itens para composição tendo como base um projeto com máscara diferente da máscara do projeto origem.
* Cálculo da composição (cálculo de projeto), permitindo que os valores calculados para insumos e composições globais sejam salvos nos objetos.
* Permitir o envio da mensagem de exclusão de obra, etapa e tarefa para o BackOffice Protheus.
* Processo de realinhamento.
CP2Incorporação

[Help](http://wikihelp.totvs.com.br/WikiHelp/IMB/IMB.SGI.aspx) e  do TOTVS Incorporação.

* Criado parâmetro para configurar o Processo de Reajuste para considerar a variação por periodicidade ao detectar deflação para poder ignorá-la.

Aprimorado:

* Posicionamento dos componentes na tela de Aditivo.
* Processo de Reajuste para considerar corretamente a configuração de reajustar até a data de vencimento para periodicidade maior que 1 e com a data de vencimento sendo menor que a data base para o reajuste.
* Processo de Reajuste para os casos de venda que tiverem resíduo e o reajuste for no período do resíduo junto com a Correção Monetária e/ou do Juros de Contrato, com isso, o histórico de reajuste dos componentes também foi aprimorado para que não seja gerado em duplicidade.

Melhoria(s):

* Efetivação de aditivos de Garantia para Contratos de Locação.
* Geração do boleto por Antecipação de Parcelas via *Web*.
* Geração dos relatórios no Portal *Web*.
* Tela de Reajuste para pesquisar vendas distratadas utilizando os filtros de moeda.
* Contexto utilizado para pesquisar se existe valor de integração associado para o componente na coligada que se está tentando efetuar a baixa no Protheus. Ao preencher a coligada no contexto não estava sendo feito com a coligada corrente forçando sempre coligada Global.
* Cadastro de comissão.

CRM

## **CRM**

5trueCRM1Gestão do Relacionamento com o Cliente

[Help](http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.Agilis.aspx) e  do TOTVS Gestão do Relacionamento com o Cliente.

* Dados referentes ao educacional agora podem ser usados em um parâmetro baseado em sentença sql mesmo dentro do Agilis.
* Melhoria ao abrir atendimentos pelo cliente online quando um usuário tiver mais de um professor associado.

Ajuste(s):

* Ao selecionar um parâmetro baseado em sentença sql no portal que utilize fórmula ou campos do atendimento.
* Inconsistência ao salvar um registro de gráfico de gantt, realizar outra alteração sem fechar a tela e salvar novamente.
* Inconsistência ao enviar e-mail com relatório em anexo quando não existe relatório definido nos parâmetros.
