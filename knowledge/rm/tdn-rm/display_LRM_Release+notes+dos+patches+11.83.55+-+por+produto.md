---
content_hash: 7758edf3c54c9ac51402264dfb0d125a50fe144aa1271c2e4fb2db92f0198415
fetched_at: '2026-06-29T00:09:03.216728+00:00'
page_id: '381039656'
product: rm
source: tdn-rm
title: Release notes dos patches 11.83.55 - por produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Release+notes+dos+patches+11.83.55+-+por+produto
version: 9
---

|  |
| --- |
| Esses são todos os patches gerados, porém nem todos estão disponíveis para todos os clientes. |

---

  
  

1square

---

  
  

# Engenharia de Software

## 11.83.55.188

* **[Ticket: Alterações Gerais]**

Arquivos: RM.Eng.StressClient.exe, RM.Eng.Library.Server.dll, RM.Eng.StressAgent.exe, RM.Eng.AutomationTest.exe, RM.Eng.CommonControlsPlugin.dll, RM.Eng.RemoteTest.Service.dll, RM.Eng.AutomationFramework.dll, RM.Eng.Library.Winforms.dll, RM.Eng.RemoteTest.exe, RM.Eng.TestFlowData.dll, RM.Eng.Library.WinControls.dll, RM.Eng.Library.Intf.dll, RM.Eng.TestFlow.exe

## 11.83.55.226

* **[Ticket: Alterações Gerais]**

Arquivos: RM.Eng.Library.Server.dll, RM.Eng.Library.WinControls.dll, RM.Eng.Library.Intf.dll, RM.Lib.Server.dll, RM.Eng.Library.Winforms.dll

# Outros

## 11.83.55.108

* **[Ticket: Alterações Gerais]** Inclusão da funcionalidade de importação de scripts.

Arquivo: RM.Script.Executor.exe

## 11.83.55.164

* **[Ticket: 07\TSOQBS]** Após o retorno da customização de uma dll pela equipe TOTVS TEC de são paulo, foi realizado o checkin do ShelveSet MelhoriasLS\_1183 enviado pelo Diogo Ferreira com a solução do cliente.

Arquivos: license\_client\_x64.dll, license\_client\_x86.dll

## 11.83.55.188

* **[Ticket: Alterações Gerais]**

Arquivo: GOLD Engine.dll

## 11.83.55.206

* **[Ticket: 07\TTWHYO]** Ajustes no parametrizador TOTVS Business Analytics

Arquivo: RM.Lib.Params.Wizard.xml

## 11.83.55.305

* **[Ticket: Alterações Gerais]**

Arquivos: RM.Script.Executor.Server.dll, RM.Script.Executor.Intf.dll, RM.Script.Executor.exe

# TOTVS Automação de Ponto

## 11.83.55.100

* **[Ticket: 07\TQZBV2]** Implementação CCT SINDADOS BH:- Controle do escopo das faixas de extra (diário/período/semanal)- Evolução do limite do banco de horas para permitir escolher entre alterar atitude ou alterar faixa para o banco de horas

Arquivos: RM.Pto.Common.Server.dll, RM.Pto.Ocorrencia.Intf.dll, RM.Pto.Common.Intf.dll, RM.Pto.Calculo.Intf.dll, RM.Pto.Parametros.Form.dll, RM.Pto.Parametros.Data.dll, RM.Pto.Movimento.Intf.dll, RM.Pto.Calculo.Service.dll, RM.Pto.Parametros.Intf.dll

* **[Ticket: 07\TQXRDX]** - Ajuste na exibição dos campos na customização do intervalo planejado - Ajuste na seleção do CheckBox de customição da intervalo planejado

Arquivos: RM.Pto.Horario.Data.dll, RM.Pto.Horario.Form.dll, RM.Pto.Horario.Intf.dll

* **[Ticket: 07\TPXFRO]** Ajuste na permissão de alteração e inclusão dos registros da tela

Arquivo: RM.Pto.Funcionario.Form.dll

* **[Ticket: 07\TPYNWH]** Correção no lançando abono futuro através do processo de lançamento de abono global.

Arquivos: RM.Pto.Ocorrencia.Data.dll, RM.Pto.Abono.Form.dll, RM.Pto.Common.Intf.dll, RM.Pto.Abono.Data.dll

* **[Ticket: 07\TQVPJ1]** Realizada otimização no cálculo do arredondamento referente as horas que serão gravadas no movimento do período dos funcionários.

Arquivo: RM.Pto.Calculo.Service.dll

* **[Ticket: 07\TQZBV2]** Implementação CCT SINDADOS BH:- Ajuste para considerar o evento do banco de horas ao lançar para o movimento do período

Arquivo: RM.Pto.Calculo.Service.dll

## 11.83.55.102

* **[Ticket: 07\TRAR15]** Foi implementado uma atualização do campo de código de cálculos no momento do carregamento deste.

Arquivo: RM.Pto.BancoDeHoras.Form.dll

* **[Ticket: 07\TQWHC7]** Foi ajustado o campo de seleção da ordem por código de cálculo onde os primeiros campos, quando criado um novo perfil, era apresentado em branco, sem opções de seleção.

Arquivo: RM.Pto.BancoDeHoras.Form.dll

## 11.83.55.115

* **[Ticket: 07\TRHUIK]** Ajuste no cálculo dos eventos do Labore, para quando considerar o evento do banco de horas, incrementar o ID da AMOVFUN para não ocorrer o problema de chave duplicada

Arquivo: RM.Pto.Calculo.Service.dll

## 11.83.55.116

* **[Ticket: 07\TQYWJV]**  Melhoria no sistema para trabalhar de forma diferente a atualização de saldo do banco de horas. Agora, após a compensação, quando o usuário voltar um período anterior como ativo e em seguida, retornar ao período atual o sistema vai continuar gerando o saldo do banco de horas da época ao invés de zerar as horas.

Arquivo: RM.Pto.BancoDeHoras.Data.dll

* **[Ticket: 07\TRMGNB]** Ajuste no limite semanal, onde não estava considerando as ocorrências calculadas do período anterior, quando a semana começa no período anterior.

Arquivo: RM.Pto.Calculo.Service.dll

## 11.83.55.117

* **[Ticket: 07\TQWWX3]** Ajustes na integração e envio do relatório do espelho de ponto para o Fluig.

Arquivos: RM.Pto.Relatorio.Data.dll, RM.Pto.AprovacaoPonto.Data.dll, RM.Pto.Facade.dll, Menu.xml

## 11.83.55.120

* **[Ticket: 07\TRMCBH]** Refeita a rotina de cálculo de DSR perdido, onde o sistema passa a considerar somente quando o parâmetro estiver marcado na parametrização do sindicato.

Arquivos: RM.Pto.Calculo.Service.dll, RM.Pto.Parametros.Intf.dll

* **[Ticket: 07\TRIAM7]** Ajustes na exclusão da movimentação ao alterar o período.

Arquivo: RM.Pto.Periodo.Intf.dll

* **[Ticket: 07\TQVSNE]** Foi melhorado o processo de abono de funcionário onde o registro do abono passará por uma verificação se o registro estará fora do limite (considerando a quantidade de ocorrências de abonos no dia ou o total de horas). Caso o limite seja superado será apresentado uma mensagem para cada data apresentando a opção, ao usuário, de cancelar o lançamento do abono ou lança-lo além do limite.

Arquivos: RM.Pto.Abono.Intf.dll, RM.Pto.Abono.Data.dll, RM.Pto.Abono.Form.dll, RM.Pto.Ocorrencia.Data.dll

* **[Ticket: 07\TRNYSE]** Ajustes no recálculo do espelho de ponto.

Arquivos: RM.Pto.Periodo.Data.dll, RM.Pto.Periodo.Intf.dll

* **[Ticket: 07\TRNTP1]** Foi melhorado o processo de lançamento de abono para o funcionário de modo que no lançamento de abono para um período que não haja ocorrências abonáveis, será apresentado uma mensagem:Não há ocorrências a serem abonadas no período informado.

Arquivo: RM.Pto.Ocorrencia.Data.dll

## 11.83.55.121

* **[Ticket: 07\TRLZX3]** Foi realizado ajuste para que o sistema obedeça a permissão cadastrada através do perfil no menu referente a edição de períodos, caso o usuário não tenha permissão neste item não será possível realizar alteração das informações na tela de período.

Arquivo: RM.Pto.Periodo.Form.dll

* **[Ticket: 07\TROTT3]** Foi ajustado o lançamento de abono de funcionário de modo que ao efetuar um lançamento tendo a data de início do limite de abono em branco não corra o erro: 'Conversão especificada não é válida."

Arquivo: RM.Pto.Abono.Data.dll

## 11.83.55.123

* **[Ticket: 07\TRPUS5]** Ajuste na exibição de totais de período relacionados a atrasos no portal.

Arquivo: RM.Pto.Batida.Data.dll

## 11.83.55.125

* **[Ticket: 07\TRNSO1]** Evolução na visualização do espelho de ponto, na aba Totais do dia, para que seja apresentado os valores das colunas Extra Banco, Atraso Banco e Falta Banco caso o sindicaco utilize banco de horas diário.

Arquivo: RM.Pto.Ocorrencia.Data.dll

* **[Ticket: 07\TRPNO8]** Ajustes na integração e envio do relatório do espelho de ponto para o Fluig.

Arquivos: RM.Pto.AprovacaoPonto.Form.dll, RM.Pto.AprovacaoPonto.Data.dll, RM.Pto.Relatorio.Form.dll

* **[Ticket: 07\TRPBG3]** Ajustada a geração do espelho do cartão para funcionários que não utilizam banco de horas.

Arquivo: RM.Pto.BancoDeHoras.Data.dll

## 11.83.55.126

* **[Ticket: 07\TQVSNE]** Foi ajustado o lançamento de abonos para funcionário de modo que o processo passe a considerar o limite de abono e o seu período de validade deste. Ao lançar um abono e este exceder o limite de registros ou de horas será apresentado uma mensagem dando a opção do usuário de lançar o abono além do limite ou cancela-lo.

Arquivos: RM.Pto.Abono.Data.dll, RM.Pto.Abono.Form.dll, RM.Pto.Abono.Intf.dll

* **[Ticket: 07\TRPBOH]** Foi ajustado a tela de visualização de horário onde os intervalos de tolerância no sindicato não modificarão os períodos de compensação ou descanso.

Arquivo: RM.Pto.Horario.Data.dll

## 11.83.55.131

* **[Ticket: 07\TRQQZG]** Aprimorada a associação da action de "Alteração de atitude de ocorrências" (PtoAlterarAtitudeOcorrenciaActionWeb) a um gatinho da Fórmula Visual.

Arquivo: RM.Pto.AlterarAtitudeOcorrencia.WebForm.dll

## 11.83.55.132

* **[Ticket: 07\TPTAGX]** Ajuste na tela de processo de lançamento global de escala de horário/descanso para correta exibição dos botões.

Arquivo: RM.Pto.Horario.Form.dll

## 11.83.55.134

* **[Ticket: 07\TPTBAX]** Ajuste no processo de alterações globais de escalas de horários e descanso.

Arquivo: RM.Pto.Horario.Form.dll

## 11.83.55.138

* **[Ticket: 07\TRXTLY]** Feita uma nova validação onde na exibição do espelho sistema verifica a data em que o funcionário deixou de usar ponto.

Arquivos: RM.Pto.Batida.Data.dll, RM.Pto.Contexto.Server.dll

## 11.83.55.142

* **[Ticket: 07\TSALRF]** Feita uma nova validação onde na exibição do espelho sistema verifica a data em que o funcionário deixou de usar ponto.

Arquivo: RM.Pto.Batida.Data.dll

## 11.83.55.143

* **[Ticket: 07\TRWI89]** Trata-se de melhoria. Foi implementado a validação do limite de abonos parametrizado por hora onde será exibido uma mensagem de confirmação para que o usuário confirme o registro dos abonos além do limite. Também foi implementado a validação do limite no lançamento de abonos sintéticos.

Arquivos: RM.Pto.Abono.Intf.dll, RM.Pto.Abono.Form.dll, RM.Pto.Abono.Data.dll

## 11.83.55.144

* **[Ticket: 07\TSBJBN]** Foi ajustado o processo de lançamento de abono de modo que não ocorre erros no lançamento do abono quando este não tiver limite de abono parametrizado.

Arquivo: RM.Pto.Abono.Data.dll

## 11.83.55.150

* **[Ticket: 07\TSEAU3]** Alterada a data de início do Acerto de Inconsistência da Portaria 1510/2009 de 01/01/2010 para 01/11/2009, data de início da vigência da Portaria do menu Configurações - Período - Processos - Acerto de Inconsistência.

Arquivo: RM.Pto.Periodo.Data.dll

## 11.83.55.160

* **[Ticket: 07\TSOIN2]** Foi realizado ajuste para que o sistema inclua com sucesso mais de um intervalo de compensado na mesma jornada.

Arquivo: RM.Pto.Horario.Form.dll

## 11.83.55.167

* **[Ticket: 07\TSU040]** Ajuste realizado para permitir a inclusão de ausência planejada em jornadas dos tipos compensado e descanso.

Arquivo: RM.Pto.Horario.Form.dll

## 11.83.55.182

* **[Ticket: 07\TTGZ08]** Foi ajustado o cálculo da função de formula HORASAFAST de forma que ela se comporte da mesma forma no teste e no durante o cálculo. Também foi ajustado para que as horas de afastamentos sejam contabilizadas a partir do primeiro dia após o afastamento ao invés de 15 dias após o início.

Arquivo: RM.Pto.Formula.dll

## 11.83.55.188

* **[Ticket: 07\TTPVJT]** Ajuste na transferência de períodos para evitar erro de violação de chave estrangeira.

Arquivo: RM.Pto.Periodo.Data.dll

## 11.83.55.196

* **[Ticket: 07\TTWOPR]** Aperfeiçoamento do sistema para permitir que a action possa ser adicionada entre as triggers da Fórmula Visual.

Arquivo: RM.Pto.AlterarHorarioLetra.WebForm.dll

## 11.83.55.197

* **[Ticket: Alterações Gerais]** Ajuste na geração do XML do evento s1050 para horário flexível

Arquivo: RM.Pto.Horario.Intf.dll

* **[Ticket: 07\TTWHYO]** Ajuste projeto GoodData referente ao campo de COLIGADA

Arquivo: RM.Pto.BancoDeHoras.Data.dll

## 11.83.55.224

* **[Ticket: 07\TUNNBN]** Implementada a importação de batidas de acordo com a Portaria 388 de 25 de agosto de 2014 do INMETRO.

Arquivos: RM.Pto.ImportacaoExportacao.Data.dll, RM.Pto.Layout.Intf.dll

## 11.83.55.230

* **[Ticket: 07\TUKIOV]** Otimizada a mensagem apresentada ao alterar a natureza de uma batida, apresentando que é necessário desbloquear o recálculo do usuário.

Arquivo: RM.Pto.Batida.Data.dll

## 11.83.55.244

* **[Ticket: 07\TUUSKN]** Otimizado o processo de período de forma que a possibilidade de erro referente a violação de chave estrangeira seja minimizado.

Arquivo: RM.Pto.Periodo.Data.dll

## 11.83.55.251

* **[Ticket: 07\TVRUGB]** Foi realizado o ajuste para que chefes externos possam abonar atrasos e faltas através do Portal Web.

Arquivo: App\_Web\_ptocodabono.ascx.7d151a08.dll

# TOTVS Avaliação e Pesquisa

## 11.83.55.154

* **[Ticket: 07\TSITTZ]** Otimizado processo de correção de questões abertas.

Arquivo: RM.Tst.Provas.Form.dll

## 11.83.55.157

* **[Ticket: 07\TSMSJK]** Otimizado processo de cadastro de questões.

Arquivo: RM.Tst.Provas.Form.dll

## 11.83.55.160

* **[Ticket: 07\TSPDQE]** Otimizado processo de recuperação de resultados do Testis pelo Painel de Seleção do TOTVS Gestão de Pessoas

Arquivo: RM.Tst.Provas.Server.dll

## 11.83.55.241

* **[Ticket: 07\TVGS44]** Ajuste na entrada de notas de candidatos por prova.

Arquivo: RM.Tst.Provas.Intf.dll

## 11.83.55.276

### Rotina: AVALIACAO INSTITUCIONAL EDU 50 064

* **[Ticket: 719123 / EDUCACIONAL01-73]** Ajuste no processo de adicionar questões as provas quando as mesmas já existam, para que não ocorra o erro ao fechar o processo após finalizado.

Arquivo: RM.Tst.Provas.Form.dll

## 11.83.55.286

### Rotina: Project-898694 Erro executor Project-898694

* **[Ticket: 920651 / EDUCACIONAL01-983]** Foi alterada a codificação de caracteres para UTF7 na geração da prova offline e importação de prova no Totvs.Executor. O erro ocorria porque no texto da questão existia o caracter unicode (0x8230) que fazia com que o xml gerado fosse inválido.

Arquivos: RM.TstExec.Executor.exe, RM.Tst.Processos.Form.dll

## 11.83.55.311

### Rotina: Project-1625212 avaliação descritiva Project-1625212

* **[Ticket: 1625299 / EDUCACIONAL01-3046]** Otimização no Totvs Avaliação e Pesquisa: no cadastro de candidato da prova, NÃO será permitido excluir o registro do candidato nas seguintes situações:- Status diferente de Pendente.- Caso o candidato pertença à uma Avaliação Descritiva do Totvs Educacional.- Caso o candidato pertença à uma Avaliação Institucional do Totvs Educacional.

Arquivos: RM.Tst.Provas.Server.dll, RM.Tst.Lib.Intf.dll, RM.Tst.Provas.Data.dll

# TOTVS Banco de Dados

## 11.83.55.123

* **[Ticket: Alterações Gerais]** Correções na versão das dlls e executáveis do Executor de Scripts RM.

Arquivos: RM.Script.Executor.exe, RM.Script.Executor.Intf.dll, RM.Script.Executor.Server.dll

## 11.83.55.128

* **[Ticket: Alterações Gerais]** Melhorias na execução de scripts Oracle.

Arquivo: RM.Script.Executor.Server.dll

# TOTVS Business Connect

## 11.83.55.106

* **[Ticket: 07\TRCJOT]** Ajuste no configurador da integração TOP x BackOffice Protheus

Arquivo: RM.Con.ConfiguraIntegracao.TotvsFolhaPagtoMobilidade.dll

## 11.83.55.109

* **[Ticket: 07\TRASN7]** Melhoria na integração contábil ao definir o período contábil para a integração entre o Educacional e o BackOffice do Protheus.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.111

* **[Ticket: 07\TRFLLY]** A utilização de xsd baseado em dataserver na ferramenta de conceito foi otimizada.

Arquivo: RM.Con.MetaConcept.dll

* **[Ticket: 07\TRFYQ8]** Unificação de códigos das mensagens de unidade de medida e Grupo de estoque para globalização de serviços.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.116

* **[Ticket: 07\TRIYWD]** Alterações feitas no GED conforme solicitação da equipe do Chronus.

Arquivo: RM.Con.GED.Server.dll

## 11.83.55.118

* **[Ticket: 07\TRHFNE]** Melhoria na mensagem de log de execução de conceito.

Arquivo: RM.Con.MetaConcept.dll

## 11.83.55.125

* **[Ticket: 07\TRQPYA]** Otimizado processo de exclusão de arquivos na integração RM x GED (ECM e Fluig)

Arquivo: RM.Con.GED.Server.dll

## 11.83.55.126

* **[Ticket: 07\TRPWAM]** Otimização do processo de Gerenciamento GED

Arquivo: RM.Con.GED.Form.dll

## 11.83.55.127

* **[Ticket: 07\TRPWAM]** Otimização do processo de Gerenciamento GED

Arquivo: RM.Con.GED.Form.dll

## 11.83.55.129

* **[Ticket: 07\TRUDFI]** Estava faltando aspas no script de instalação da integração Protheus X backoffice

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.132

* **[Ticket: Alterações Gerais]** Ajustando script ORACLE para a mensagem ACCOUNTINGENTRY3.000

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.134

* **[Ticket: 07\TRG335]** Melhoria ao visualizar documentos da integração com GED.

Arquivo: RM.Con.GED.Server.dll

## 11.83.55.138

* **[Ticket: Alterações Gerais]** Ajuste no apontamento avulso de mão d eobra

Arquivo: RM.Con.ConfiguraIntegracao.TotvsObrasProjetosMobilidade.dll

* **[Ticket: Alterações Gerais]** Ajuste no apontamento avulso de mão de obra

Arquivo: RM.Con.ConfiguraIntegracao.TotvsObrasProjetosMobilidade.dll

## 11.83.55.139

* **[Ticket: 07\TRZFQ0]** Melhoria na instalação das integrações Financeira e Contábil entre o Educacional e o Protheus através do Configurador de Integração.

Arquivos: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll, RM.Edu.ConfiguraIntegracao.TotvsEducacionalSigaCTB.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.144

* **[Ticket: Alterações Gerais]** Atualização da Mensagem

Arquivo: RM.Con.ConfiguraIntegracao.TotvsObrasProjetosMobilidade.dll

## 11.83.55.156

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Ajuste na mensagem de baixa de lançamentos a receber para tratamento na conversão de valores para adequação ao uso de '.' como padrão de separação de casas decimais.

Arquivos: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.157

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Melhoria no tratamento das informações de cliente/fornecedor cadastradas por sistemas da integração por mensageria única.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.158

* **[Ticket: Alterações Gerais]** Melhoria na exclusão de apontamento de equipamento quando temos integração com Manuntenção de ativos

Arquivos: RM.Con.ConfiguraIntegracao.TotvsObrasProjetosMobilidade.dll, RM.Con.ConfiguraIntegracao.TotvsObrasProjetosManutencaoAtivos.dll

## 11.83.55.159

* **[Ticket: Alterações Gerais]** Ajuste no tratamento das informações de país enviadas na mensagem de cliente/fornecedor para utilização da tabela de codificação do módulo fiscal.

Arquivos: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll, RM.Fin.CliFor.Service.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.164

* **[Ticket: 07\TSGEKX]** Melhoria da mensagem quando não é possível fazer a integração com o GED devido à visão ter sido aberta a partir de outra visão.

Arquivos: RM.Con.GED.Form.dll, RM.Con.Localizacao.dll

## 11.83.55.169

* **[Ticket: 07\TSXWNL]** Ajuste para padronizar comportamento de processo de agendamento de execução de mensagens genericas e de mensagem de status de funcionario. No processo de agendamento de execução de mensagem de status de funcionario sera validado a existencia de agendamento realizado, evitar conflitos de agendamentos repetidos principalmente com recorrencia.

Arquivos: RM.Con.TotvsMessage.Intf.dll, RM.Con.Indicadores.Mov.IService.dll, RM.Con.Indicadores.Ctb.IService.dll, RM.Con.Indicadores.Mov.Data.dll, RM.Con.Indicadores.Ctb.Data.dll, RM.Con.TotvsMessage.Data.dll, RM.Con.Indicadores.Ctb.Service.dll, RM.Con.Indicadores.Utils.dll, RM.Con.Indicadores.Mov.Service.dll, RM.Con.MetaConcept.dll

* **[Ticket: 07\TSXNOG]** Ajuste no script de instalação da integração Backoffice X Protheus.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

* **[Ticket: 07\TSXNOG]** Ajuste no script de instalação de integração de Protheus com Backoffice.

Arquivos: RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## 11.83.55.171

* **[Ticket: 07\TSXFG8]** Incluído namespace de classe utilizada pelo Script para evitar erro de execução da mensagem.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.177

* **[Ticket: 07\TSIWJZ]** Melhoria no processo de edição de itens.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.180

* **[Ticket: 07\TTIEXM]** As funções RealizarConsultaSQLDataTable() e RealizarConsultaSQLDataTableAUTH() foram adicionadas e as funções RealizarConsultaSQL() e RealizarConsultaSQLAUTH() continuaram, porém com outro tipo de retorno.

Arquivo: RM.Con.Conector.WebService.dll

## 11.83.55.182

* **[Ticket: 07\TSYBKE]** Melhoria na execução de conceito com conexão de origem arquivo txt.

Arquivo: RM.Con.MetaConcept.dll

## 11.83.55.184

* **[Ticket: 07\TTLHD0]** Melhoria na integração possibilitando excluir um título no Protheus

Arquivos: RM.Con.TotvsMessage.Intf.dll, RM.Con.TotvsMessage.Services.dll

## 11.83.55.190

* **[Ticket: Alterações Gerais]** Incluindo classes TotvsBA do Concept

Arquivos: RM.Con.Concept.Form.dll, RM.Con.Concept.dll, RM.Con.Concept.Server.dll

## 11.83.55.191

* **[Ticket: Alterações Gerais]** Ajuste na Engine do Concept

Arquivos: RM.Con.Indicadores.Utils.dll, RM.Con.Concept.Server.dll, RM.Con.Concept.dll, RM.Lib.dll, RM.Con.Concept.Form.dll, RM.Lib.Server.dll

* **[Ticket: Alterações Gerais]** Ajuste no Con-Concept

Arquivos: RM.Con.Concept.dll, RM.Con.Concept.Server.dll

## 11.83.55.197

* **[Ticket: Alterações Gerais]** Merge de Con-Cenector - Requisitos x 11.83

Arquivos: RM.Fop.Facade.dll, RM.Con.Conector.Data.dll, RM.Con.EducacionalWebEnsino.Data.dll, RM.Con.Conector.Interface.dll, RM.Con.Conector.Server.dll, RM.Con.Utils.dll, RM.Con.Workflow.Intf.dll, RM.Con.Concept.dll, RM.Rhu.Facade.dll, RM.Con.Conector.Form.dll, RM.Con.Workflow.dll, RM.Con.Conector.Service.dll, RM.Con.Conector.Intf.dll, RM.Con.Concept.Server.dll

* **[Ticket: 07\TTWHYO]** Ajustes projeto GoodData

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TTUFEP]** Melhoria no processo de Extração de dados dos Conceitos - GoodData

Arquivos: RM.Con.Indicadores.Fin.Service.dll, RM.Con.Indicadores.Utils.dll, RM.Con.Indicadores.Mov.IService.dll, RM.Con.Indicadores.RH.IService.dll, RM.Con.Indicadores.RH.Service.dll, RM.Con.Indicadores.Ctb.Service.dll, RM.Con.Indicadores.Mov.Service.dll, RM.Con.Indicadores.Fin.Data.dll, RM.Con.Indicadores.RH.Data.dll, RM.Con.Indicadores.Mov.Data.dll, RM.Con.Indicadores.Edu.Service.dll, RM.Con.Indicadores.Ctb.IService.dll, RM.Con.Indicadores.Fin.IService.dll, RM.Con.Indicadores.Ctb.Data.dll

* **[Ticket: 07\TTUW72]** Script para acerto de Auto incremento da PItemPartidaLC

Arquivo: RM.Con.Indicadores.Ctb.Service.dll

* **[Ticket: 07\TTWHYO]** Otimização Parametrização TOTVS BA

Arquivos: RM.Con.Parametrizador.Data.dll, RM.Con.Parametrizador.Form.dll, RM.Con.Indicadores.Ctb.Service.dll, RM.Con.Parametrizador.Intf.dll

* **[Ticket: 07\TTWHYO]** Ajustes parametrizador TOTVS BA

Arquivo: RM.Lib.Params.Wizard.xml

## 11.83.55.198

* **[Ticket: 07\TTWHYO]** Ajustes projeto GoodData

Arquivos: RM.Con.Indicadores.RH.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

## 11.83.55.199

* **[Ticket: 07\TTWHYO]** Ajustes GoodData na versão 11.83

Arquivos: RM.Con.Indicadores.RH.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TTUFEP]** Melhoria no processo de extratores do GoodData

Arquivos: RM.Con.Indicadores.Ctb.IService.dll, RM.Con.Indicadores.Ctb.Service.dll, RM.Con.Indicadores.Ctb.Data.dll

* **[Ticket: Alterações Gerais]** Projeto Downgrade GoodData

Arquivo: RM.Con.Parametrizador.Data.dll

## 11.83.55.205

* **[Ticket: 07\TUBUZJ]** -No conector da versão 11.83 o schema deve ser considerado ao transformar um DataSet em XmlString

Arquivo: RM.Con.Utils.dll

* **[Ticket: Alterações Gerais]** Melhoria no processo de geração de acordo financeiro pela integração por Mensageria única

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.206

* **[Ticket: 07\TUAPUQ]** Otimização do Parametrizador do TOTVS BA

Arquivo: RM.Con.Parametrizador.Form.dll

### Rotina: EDU-Pesquisa e Extensão

* **[Ticket: PCREQ-5444]** Ajuste na validação utilizada na instalação da transformação do adapter de acordo financeiro, FINANCINGTRADING, na versão 1.002.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.209

* **[Ticket: 07\TUAPUQ]** Ajuste no Extrator para considerar diferença de saldo entre filiais.

Arquivo: RM.Con.Indicadores.Ctb.Service.dll

* **[Ticket: 07\TUAPUQ]** Projeto GoodData - Modificação na regra de extração das Fatos do Financeiro

Arquivo: RM.Con.Indicadores.Fin.Service.dll

## 11.83.55.211

* **[Ticket: 07\TUGWVE]** Ajustes GoodData Versão 11.83.55

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUGQXH]** Criando possibilidade de manipular o retorno da exec de conceito

Arquivo: RM.Con.Workflow.dll

* **[Ticket: Alterações Gerais]** Melhoria no processo dos extratores do GoodData

Arquivos: RM.Con.TotvsBA.Workflow.Server.dll, RM.Con.TotvsBA.Workflow.Intf.dll, RM.Con.TotvsBA.Workflow.dll

* **[Ticket: Alterações Gerais]** Melhoria nos processo de extratores gooddata

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: Alterações Gerais]** Melhoria no processo de extratores do GoodData

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: Alterações Gerais]** Melhoria no extratores do gooddata

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: Alterações Gerais]** Melhorias no Projeto GoodData

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

## 11.83.55.214

* **[Ticket: 07\TUAPUQ]** Melhoria no processamento dos extratores do gooddata

Arquivos: RM.Con.Parametrizador.Form.dll, RM.Con.Parametrizador.Data.dll, RM.Con.Indicadores.Fin.IService.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll, RM.Con.Indicadores.Ctb.Service.dll

* **[Ticket: 07\TUJTBM]** Ajustes GoodData Versão 11.83.55: Melhorias no DataServer Reclamações Trabalhistas

Arquivos: RM.Con.Indicadores.RH.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUJTBM]** Ajustes GoodData Versão 11.83.55: Melhorias no DataServer Recrutamento

Arquivo: RM.Con.Indicadores.RH.Service.dll

* **[Ticket: 07\TUAPUQ]** Melhoria no processo de geração dos extratores gooddata

Arquivos: RM.Con.Indicadores.Ctb.Service.dll, RM.Con.Indicadores.Fin.IService.dll

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivos: RM.Con.Indicadores.Mov.Service.dll, RM.Con.Indicadores.Utils.dll, RM.Con.Indicadores.Mov.Data.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUAPUQ]** Otimização do processamento das Fatos Financeiro

Arquivos: RM.Con.Indicadores.Fin.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUJTBM]** Ajustes GoodData Versão 11.83.55: Melhorias no DataServer Banco de Horas

Arquivo: RM.Con.Indicadores.RH.Service.dll

## 11.83.55.215

* **[Ticket: 07\TUJTBM]** Ajustes GoodData Versão 11.83.55: Ajustes Fato Banco de Horas

Arquivo: RM.Con.Indicadores.RH.Service.dll

* **[Ticket: 07\TUAPUQ]** Projeto GoodData - Otimização da Extração das Fatos Financeiro.

Arquivos: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll, RM.Con.Indicadores.Fin.Service.dll

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivos: RM.Con.Indicadores.Mov.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll, RM.Con.Indicadores.Mov.Data.dll

* **[Ticket: 07\TUJTBM]** Ajustes GoodData Versão 11.83.55

Arquivos: RM.Con.Indicadores.RH.Data.dll, RM.Con.Indicadores.RH.Service.dll, RM.Con.Indicadores.RH.IService.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUAPUQ]** Melhoria no extrator de contabilidade

Arquivo: RM.Con.Indicadores.Ctb.Service.dll

* **[Ticket: 07\TUAPUQ]** Melhoria no processo de extração do dados - GoodData

Arquivos: RM.Con.Indicadores.Ctb.Service.dll, RM.Con.Indicadores.Ctb.Data.dll, RM.Con.ConfiguraIntegracao.Server.dll

## 11.83.55.216

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUAPUQ]** Melhoria de filtros para a extração dos dados do Gooddata

Arquivo: RM.Con.Parametrizador.Form.dll

* **[Ticket: 07\TUJTBM]** Ajustes GoodData Versão 11.83.55

Arquivo: RM.Con.Indicadores.RH.Service.dll

## 11.83.55.217

* **[Ticket: Alterações Gerais]** Melhorias nos artefatos do gooddata

Arquivos: RM.Con.Indicadores.Fin.IService.dll, RM.Con.Indicadores.Fin.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUJTBM]** Ajustes no projeto GoodData 11.83.55

Arquivo: RM.Con.Indicadores.RH.Service.dll

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivos: RM.Con.Indicadores.Mov.Data.dll, RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.218

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivos: RM.Con.Indicadores.Mov.Data.dll, RM.Con.Indicadores.Mov.IService.dll, RM.Con.Indicadores.Mov.Service.dll

* **[Ticket: 07\TUMXL5]** Ajustes projeto GoodData

Arquivo: RM.Con.Indicadores.RH.Service.dll

* **[Ticket: 07\TUAPUQ]** Melhorias no processo de extração dos dados GoodData

Arquivos: RM.Con.Indicadores.Fin.Service.dll, RM.Con.Indicadores.Fin.IService.dll

* **[Ticket: Alterações Gerais]** Melhoria no extrator de portardor do gooddata

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUJTBM]** Ajustes GoodData Versão 11.83.55

Arquivo: RM.Con.Indicadores.RH.Service.dll

## 11.83.55.219

* **[Ticket: 07\TUAPUQ]** Melhoria nos extratores do financeiro

Arquivos: RM.Con.Indicadores.Ctb.Service.dll, RM.Con.Indicadores.Fin.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUMXL5]** Ajuste projeto GoodData 11.83.55

Arquivo: RM.Con.Indicadores.RH.Service.dll

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivo: RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.220

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivos: RM.Con.Parametrizador.Form.dll, RM.Con.Indicadores.Mov.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll, RM.Con.Indicadores.Mov.IService.dll

* **[Ticket: 07\TUAPUQ]** Melhoria no extratores de controladoria para quebra de valores

Arquivo: RM.Con.Indicadores.Ctb.Service.dll

* **[Ticket: 07\TUAPUQ]** Melhoria nos filtros dos extratores de fatos de finanças para evolução de performace

Arquivo: RM.Con.Indicadores.Fin.Service.dll

* **[Ticket: 07\TUAPUQ]** Melhoria nos extratores do financeiro quanto ao tempo de preenchimento da StageArea.

Arquivos: RM.Con.Indicadores.Fin.Service.dll, RM.Con.Indicadores.Ctb.Service.dll

* **[Ticket: 07\TUMNVU]** Melhoria ao realizar integração de produto entre RM e Protheus.

Arquivo: RM.Con.Workflow.dll

## 11.83.55.221

* **[Ticket: 07\TUMXL5]** Ajustes extratores dos conceitos - GoodData

Arquivo: RM.Con.Indicadores.RH.Service.dll

* **[Ticket: 07\TUAPUQ]** Melhoria no processo de extração dos fatos por segmento.

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivos: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll, RM.Con.Indicadores.Mov.IService.dll, RM.Con.Indicadores.Mov.Service.dll

* **[Ticket: 07\TUAPUQ]** Melhoria na extração do saldo anterior do fato de contabilidade para gerar o saldo anterior mesmo sem registro de movimentação no período.

Arquivo: RM.Con.Indicadores.Ctb.Service.dll

* **[Ticket: 07\TUAPUQ]** Melhoria na limpeza dos dados da stage Area. A limpeza agora é separada por dimensões e fatos.

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUAPUQ]** Melhoria nos extratores de controladoria.

Arquivo: RM.Con.Indicadores.Ctb.Service.dll

* **[Ticket: 07\TUMXL5]** Ajustes Projeto GoodData

Arquivos: RM.Con.Indicadores.RH.Service.dll, RM.Con.Indicadores.RH.IService.dll

* **[Ticket: 07\TUAPUQ]** Melhoria no processo de criação de stage para obtermos um melhor desempenho na extração dos dados.

Arquivo: RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

* **[Ticket: 07\TUAPUQ]** Melhoria na extração do saldo anterior do fato de contabilidade para selecionar apenas quando o saldo anterior for diferente de zero.

Arquivo: RM.Con.Indicadores.Ctb.Service.dll

## 11.83.55.222

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivo: RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.223

* **[Ticket: 07\TUAPUQ]** Melhoria na extração dos dados para stage Area.1-Implementação do fato de orçamento-HLC.2-Adicionada validação do fato de orçamento, para bloquear a extração diária.

Arquivos: RM.Con.Indicadores.Ctb.IService.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll, RM.Con.Parametrizador.Form.dll, RM.Con.Indicadores.Ctb.Data.dll, RM.Con.Parametrizador.Data.dll, RM.Con.Indicadores.Ctb.Service.dll

## 11.83.55.224

* **[Ticket: 07\TUAPUQ]** Melhoria na extração dos dados para stage Area.1-Implementação do fato de orçamento-HLC.2-Adicionada validação do fato de orçamento, para bloquear a extração diária.

Arquivo: RM.Con.Parametrizador.Form.dll

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivo: RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.225

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivo: RM.Con.Indicadores.Mov.Service.dll

* **[Ticket: 07\TUSY30]** Ajuste na função RetornaDataExtração para validar a opção do Parâmetro Variavel.

Arquivo: RM.Con.Indicadores.Utils.dll

* **[Ticket: 07\TUMXL5]** Ajustes GoodData 11.83

Arquivo: RM.Con.Indicadores.RH.Service.dll

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivo: RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.226

* **[Ticket: 07\TUKFCQ]** Melhoria no processamento dos extratores do gooddata

Arquivo: RM.Con.Indicadores.Mov.Data.dll

* **[Ticket: 07\TUAPUQ]** Melhoria no processo de extração dos dados GoodData-RM. Implementado o fato de orçamento da area de controladoria.

Arquivos: RM.Con.Indicadores.Ctb.Service.dll, RM.Con.Indicadores.Fin.Service.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

## 11.83.55.227

* **[Ticket: 07\TUKFCQ]** Melhorias no processamento dos extratores do GoodData

Arquivo: RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.234

* **[Ticket: 07\TUKFCQ]** Melhorias no processamento dos extratores do GoodData

Arquivo: RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.235

* **[Ticket: 07\TVCKEQ]** Adaptação do adapter de integração para geração do código de Nosso Número e código de barras para considerar a tag de contrato como o identificador de convênio.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

* **[Ticket: 07\TUKFCQ]** Melhorias no processamento dos extratores do GoodData

Arquivo: RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.236

* **[Ticket: 07\TUKFCQ]** Melhorias no processamento dos extratores do GoodData

Arquivo: RM.Con.Indicadores.Mov.Service.dll

## 11.83.55.237

* **[Ticket: 07\TVDNG7]** Melhoria na validação do código de convênio utilizado para a geração do código de Nosso Número no adapter da mensagem "OurNumberBanking".

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.241

* **[Ticket: 07\TVHQ18]** Criação de novas funcionalidades para extração dos dados para a stage área. (GoodData)

Arquivo: RM.Lib.Params.Wizard.xml

## 11.83.55.246

* **[Ticket: 07\TVNGPM]** Melhoria no adapter de Bancos para utilização de tratamento de autoincremento para os cadastros de conta caixa e convênio, quando a origem do cadastro é um sistema externo.

Arquivos: RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## 11.83.55.257

### Rotina: [PROJETO CNI] - FIEAM - INTEGRAÇÃO PROTHEUS - CADASTRO CLIENTE: CODIGO IGUAL E LOJA DIFERENTE

* **[Ticket: 182873 / MEDU-1136]** Melhoria na integração para permitir a utilização de código sequencial no cadastro de cliente/fornecedor na integração do Educacional com o BackOffice Protheus, para o adapter CustomerVendor na versão 2002.

Arquivos: RM.Fin.Parametros.Data.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## 11.83.55.307

### Rotina: Project-1486739 GED Project-1486739

* **[Ticket: 1496275 / DFRWFOUNDATION-877]** Ao enviar um arquivo para o ECM é verificado se o usuário possui permissão para postar na pasta.

Arquivo: RM.Con.GED.Server.dll

* **[Ticket: 1496275 / DFRWFOUNDATION-877]** A mensagem foi tratada para que exiba o nome correto do GED utilizado

Arquivo: RM.Con.GED.Server.dll

# TOTVS Construção e Projetos

## 11.83.55.100

* **[Ticket: 07\TQZINT]** Ajuste realizado na máscara de insumos no processo de "Importar Insumos via Excel" desta forma independentemente da forma como seja informadoo código de insumo se possuir letras elas serão convertidas para maiúsculo.

Arquivos: RM.Prj.Importacao.Form.dll, RM.Prj.Insumo.Data.dll, RM.Prj.Insumo.Form.dll, RM.Prj.Insumo.Intf.dll

* **[Ticket: 07\TQZIOI]** Validação do campo "Ativo" para edição de "Cenários" em se tratando do cenário principal. Caso o mesmo tenha o campo "Ativo"

Arquivo: RM.Prj.Cadastros.Data.dll

## 11.83.55.101

* **[Ticket: 07\TQXLZ9]** Durante o cálculo do Total Teórico na equalização de insumo, os recursos de composição que continham os grupos DNIT iguais a: Nenhum, Material, e Transporte. Estavam sendo dívidas pela produção por Hora da composição por Produção.Recursos que possuem tal grupo não devem ter a quantidade afetada pela produção por hora.

Arquivos: RM.Prj.Insumo.Data.dll, RM.Prj.Cronograma.Server.dll

## 11.83.55.102

* **[Ticket: 07\TQZUQD]** Realizada melhorias de performance no cálculo do projeto.. Otimização no cálculo do projeto, que em testes internos, passou de 52 minutos para 12 minutos.

Arquivos: RM.Prj.CalculoFormula.Intf.dll, RM.Prj.Calculo.Server.dll

* **[Ticket: Alterações Gerais]** Corrigindo problemas de discrepância da solution.

Arquivos: RM.Prj.Parametros.Form.dll, RM.Prj.BackupRestore.Form.dll, RM.Prj.GrupoCusto.Data.dll, RM.Prj.GrupoCusto.Intf.dll, RM.Prj.Projeto.Form.dll, RM.Prj.BackupRestore.Intf.dll, RM.Prj.Composicao.Intf.dll

* **[Ticket: 07\TQVZKW]** Colocando o Rateio de Item por Produto em um processo desaclopado da Associação de Item de Contrato.Foi necessário devido a Utilização do Status no Contrato onde estava sendo possível associar um rateio quando o contrato esta em andamento.

Arquivos: RM.Prj.Contrato.Intf.dll, RM.Prj.Contrato.Form.dll

## 11.83.55.103

* **[Ticket: 07\TRBDC0]** Ajuste no Quadro de Permanência

Arquivo: RM.Prj.Insumo.Data.dll

## 11.83.55.105

* **[Ticket: 07\TQZILL]** Ajuste para permitir edição do código de projeto quando a integração TOP x BackOffice Protheus estiver ativa e não houver filial informada no Projeto

Arquivo: RM.Prj.Projeto.Form.dll

## 11.83.55.106

* **[Ticket: 07\TQW155]** Realizado ajuste no calculo do valor total contratado do item de contrato, emcasos da existencia de periodo de estorno.

Arquivo: RM.Prj.Contrato.Data.dll

## 11.83.55.108

* **[Ticket: 07\TQVJII]** Verifica tipos de Dados nos Apontamentos realizados em ambientes com base Oracle.

Arquivo: RM.Prj.Mobilidade.Data.dll

* **[Ticket: 07\TRD795]** Ajuste realizado para que ao utilizar na aba orçamento, em Composições no processo Alteração Geral no painel Substituir Recurso e sendo este recurso uma composição que é utilizada na equipe mecânica apareça uma mensagem informando "Este recurso é utilizado na equipe mecânica e não pode ser alterado."

Arquivo: RM.Prj.Composicao.Data.dll

* **[Ticket: 07\TRDLJY]** Verificado as coluna parametrizadas durante o processo de importação.

Arquivo: RM.Prj.Utils.Intf.dll

* **[Ticket: 07\TRDIB5]** Ajuste nos relatórios produzir melhor

Arquivos: RM.Prj.Mobilidade.Data.dll, RM.Prj.Mobilidade.Intf.dll, RM.Prj.Mobilidade.Form.dll, RM.Prj.Cronograma.Form.dll

* **[Ticket: 07\TRDFXM]** Ajuste realizado ao cancelar a Geração de Pedidos que está sendo cadastrado. Não será mais exibido a mensagem de excessão.

Arquivo: RM.Prj.PedidoMaterial.Form.dll

* **[Ticket: 07\TRDENV]** Conforme acordado com cliente ao finalizar o processo de geração de pedido de material a tela de log será exibida, após o fechamento do log o novo pedido gerado será aberto

Arquivos: RM.Prj.PedidoMaterial.Server.dll, RM.Prj.PedidoMaterial.Form.dll, RM.Prj.PedidoMaterial.Intf.dll

* **[Ticket: 07\TRDMD1]** Ao executar o processo que Exporta o Pert para o Cronograma, será verificado a quantidade de registros selecionando.Caso seja igual a quantidade de registros de tarefas enviadas o processo realizar a exportação de todas as tarefas listadas no Pert.

Arquivo: RM.Prj.Tarefa.Form.dll

* **[Ticket: 07\TRCZVV]** Planilha de Serviços - Ajuste do incidente que ocorria ao tentar inserir uma composição através da visão.

Arquivo: RM.Prj.Planilhas.Form.dll

* **[Ticket: 07\TRCZVQ]** Ajustado para que o BDI do projeto seja levado na geração do relatório de modelo fixo de composição

Arquivo: RM.Prj.Composicao.Data.dll

* **[Ticket: 07\TRDLRV]** Agrupando a necessidade dos insumos nas tarefas na requisição de material.

Arquivo: RM.Prj.Insumo.Server.dll

## 11.83.55.109

* **[Ticket: 07\TRCZXC]** Ajuste na integração TOP x BackOffice Protheus. Preenchimento automático do campo FILIAL, na aba DEFAULT do Contrato

Arquivos: RM.Prj.Contrato.Form.dll, RM.Prj.Utils.Server.dll, RM.Prj.Utils.Intf.dll

* **[Ticket: 07\TRCW43]** O processo de Acerto de Inconsistência, estava adicionando a tela os recursos de composição por produção e das composições utilizadas no projeto, quando não era necessário realizar nenhum ajuste. Foi Adicionado ao processo uma mensagem que alerta ao usuário que não existem insumos ou recursos com inconsistência no projeto. Após confirmar a leitura o processo será fechado.

Arquivos: RM.Prj.Projeto.Form.dll, RM.Prj.Projeto.Data.dll

* **[Ticket: 07\TRDMGD]** Ajuste na integração TOP x BackOffice Protheus: Movimento padrão e de estorno são preenchidos com o tipo default ao acessar a tela de integração com suprimento/faturamento

Arquivos: RM.Prj.Contrato.Data.dll, RM.Prj.Contrato.Form.dll, RM.Prj.Contrato.Intf.dll, RM.Prj.Contrato.Server.dll, RM.Prj.Contrato.IServer.dll

* **[Ticket: 07\TRDM81]** Durante o processo é disparado um JOB executor, foi adicionado ao processo a opção de cancelar a execução do JOB que sendo executado ou que será executado.O processo será disparado quando o usuário solicitar o cancelamento via o botão cancelar disponível na tela do processo.

Arquivo: RM.Prj.Tarefa.Data.dll

## 11.83.55.110

* **[Ticket: 07\TRF057]** Ajustes no mobilidade

Arquivos: RM.Prj.Parametros.Form.dll, RM.Prj.dll, RM.Prj.Mobilidade.Form.dll, RM.Prj.Projeto.Form.dll

* **[Ticket: 07\TREAHF]** O processo ‘Lançar Cronograma Automaticamente’ sofre melhorias, onde será possível realizar o lançamento restante quando existir lançamentos em períodos que estão bloqueados para à edição.

Arquivos: RM.Prj.Cronograma.Server.dll, RM.Prj.AlocacaoRecurso.Form.dll

* **[Ticket: 07\TRF057]** Ajustes Mobilidade- Layout dos parametros de projeto

Arquivo: RM.Prj.Parametros.Form.dll

* **[Ticket: 07\TRDE15]** Insumos derivados não eram adicionados à composição após a cópia.

Arquivos: RM.Prj.Projeto.Data.dll, RM.Prj.Utils.Intf.dll

* **[Ticket: 07\TRF057]** Ajuste na copia de itens para o mobilidade

Arquivo: RM.Prj.Projeto.Form.dll

* **[Ticket: 07\TRF057]** Ajuste na Edição de Apontamento de avanço fisico no mobilidade

Arquivo: RM.Prj.Mobilidade.Form.dll

## 11.83.55.114

* **[Ticket: 07\TREMAH]** Máscara de insumo não contempla insumo especializado

Arquivos: RM.Prj.Composicao.Form.dll, RM.Prj.Parametros.Intf.dll, RM.Prj.Planilhas.Form.dll, RM.Prj.Parametros.Data.dll, RM.Prj.Planilhas.Data.dll, RM.Prj.Insumo.Form.dll, RM.Prj.Tarefa.Form.dll

* **[Ticket: 07\TRHIZN]** Máscara de insumo não contempla insumo especializado

Arquivo: RM.Prj.Parametros.Intf.dll

## 11.83.55.115

* **[Ticket: 07\TRHCB6]** Criação de resource para a tradução das telas apontadas no chamado.

Arquivos: RM.Prj.Importacao.Form.dll, RM.Prj.Relatorios.Form.dll, RM.Prj.Cronograma.Intf.dll, RM.Prj.Planilhas.Data.dll, RM.Prj.Tarefa.Data.dll, RM.Prj.Cronograma.Form.dll, RM.Prj.Planilhas.Intf.dll

* **[Ticket: 07\TRHUOQ]** Durante o processo que replaneja o Cronograma planejado os períodos com valores zerados ou com quantidade inferiores a zeros serão apagados;

Arquivos: RM.Prj.Tarefa.Data.dll, RM.Prj.Cronograma.Server.dll

* **[Ticket: 07\TRIBQB]** Ajustado log do processo de exportar pert para o cronograma com botão de "Recalcular Cronograma"

Arquivo: RM.Prj.Tarefa.Data.dll

## 11.83.55.118

* **[Ticket: 07\TRMFZ6]** Ajuste em motagem de log ao exportar Pert para Cronograma quando o mesmo contêm tarefas com parametro de Alterar Quantidade pelo Cornograma marcado

Arquivo: RM.Prj.Tarefa.Data.dll

* **[Ticket: 07\TRMBAL]** Realizado o bloqueio dos campos referentes tipos de movimento de transferencia de estoque, quando ativo a integração com Protheus.

Arquivo: RM.Prj.Parametros.Form.dll

## 11.83.55.121

* **[Ticket: 07\TRIBQ5]** Validação não permite a exclusão do projeto.

Arquivos: RM.Prj.Log.Data.dll, RM.Prj.Projeto.Form.dll

## 11.83.55.123

* **[Ticket: 07\TRHVQ8]** dicionando processo na tela de Insumo que permite ao usuário adicionar uma ou varias regras de derivação para os insumos derivados selecionados

Arquivo: RM.Prj.Insumo.Form.dll

* **[Ticket: 07\TRHVPH]** Adicionando processo na tela de Insumo que permite ao usuário adicionar uma ou varias regras de derivação para os insumos derivados selecionados (MELHORIA).

Arquivos: RM.Prj.Insumo.Intf.dll, RM.Prj.GrupoCusto.Intf.dll, RM.Prj.Insumo.Data.dll, RM.Prj.Composicao.Intf.dll

* **[Ticket: 07\TIAKKJ]** Melhoria na copia de itens de projeto, para possibilitar a remoção da copia de insumos derivados, pois o mesmo possui regras de derivação que em alguns o usuário não utilizara no projeto de destino ou precisara recriar.

Arquivos: RM.Prj.Projeto.Intf.dll, RM.Prj.Projeto.Data.dll, RM.Prj.Projeto.Form.dll

* **[Ticket: 07\TRNRGP]** Ajuste realizado no processo de Histograma de Insumos por Tarefas para tratar as especificidades inerentes a cada Sistema Gerenciador de Banco de Dados. Após, não será necessário a interação através de mensagens.

Arquivo: RM.Prj.Relatorios.Server.dll

## 11.83.55.124

* **[Ticket: 07\TRPUM0]** Replanejamento de tarefas ao Exportar Pert para Cronograma

Arquivo: RM.Prj.Tarefa.Data.dll

## 11.83.55.125

* **[Ticket: 07\TFOBS4]** Validar no cálculo do projeto, inserindo os insumos derivados necessários.

Arquivo: RM.Prj.Calculo.Server.dll

* **[Ticket: 07\TRMFZ6]** Exportação de Pert para Cronograma em cenários

Arquivo: RM.Prj.Calculo.Server.dll

## 11.83.55.127

* **[Ticket: 07\TRQSCA]** Melhoria nas mensagens de alerta do processo "Associar Regra de Derivação" para auxiliar o usuário na identificação do registro que causou o incidente.

Arquivos: RM.Prj.Insumo.Server.dll, RM.Prj.Insumo.Data.dll

## 11.83.55.128

* **[Ticket: 07\TRSXSH]** Ajuste na tela de Associação de Objetos ao Aditivo de Contrato

Arquivo: RM.Prj.Contrato.Form.dll

## 11.83.55.129

* **[Ticket: 07\TRUCOW]** Atualização do processo de exclusão de Projetos.

Arquivo: RM.Prj.Projeto.Data.dll

## 11.83.55.130

* **[Ticket: 07\TRTP21]** Atualização realizada No processo de “Alterar quantidade do item” em Aditivos Contratuais para o campo Quantidade Alterada passando a exibir a formatação com casas decimais.

Arquivo: RM.Prj.Contrato.Form.dll

## 11.83.55.131

* **[Ticket: 07\TRSMW6]** Ao excluir o cronograma pela Obra ou Etapa é validado se suas atividades possuem lançamentos caso haja o mesmo será excluido

Arquivos: RM.Prj.Cronograma.Form.dll, RM.Prj.Cronograma.Server.dll, RM.Prj.Cronograma.Intf.dll

* **[Ticket: 07\TRTOWD]** Atualização realizada no processo Alterar quantidade do item em Aditivos Contratuais com status “Em Andamento” deixando de exibir a tela de Alterar quantidade de Item.

Arquivo: RM.Prj.Contrato.Form.dll

## 11.83.55.133

* **[Ticket: 07\TRUYUI]** Campo Local de Estoque sendo exibido na tela de Solicitação de Compra. Este campo não deve ser exibido nesta tela, pois ele é obtido do SubProjeto.

Arquivo: RM.Prj.PedidoMaterial.Form.dll

* **[Ticket: 07\TRVHIM]** Ajuste no processo de alteração de percentual na tela de Insumo Derivado

Arquivo: RM.Prj.Insumo.Form.dll

## 11.83.55.134

* **[Ticket: 07\TRVIBJ]** Atualização realizada no processo de Importar Insumos Via Excel que passa a exibir a barra de rolagem para Grupo de Custos

Arquivo: RM.Prj.Importacao.Form.dll

## 11.83.55.135

* **[Ticket: 07\TRVI38]** Será importado no processo ‘Importar Cronograma via Excel’ apenas os registros contidos na planilha principal (ativa).

Arquivo: RM.Prj.Cronograma.Form.dll

## 11.83.55.136

* **[Ticket: 07\TRVZM7]** Ajuste no filtro de usuário do anexo de Preço do Insumo

Arquivo: RM.Prj.Insumo.Data.dll

* **[Ticket: 07\TRVZMN]** Ajuste na tela de Associação de Objetos ao Contrato

Arquivo: RM.Prj.Contrato.Form.dll

* **[Ticket: 07\TRVZM1]** Aplicar curva de distribuição com alguns períodos travados permitia o planejamento em mais de 100%

Arquivo: RM.Prj.Cadastros.Server.dll

* **[Ticket: 07\TRVICE]** Atualização realizada no processo de Cotação de Insumos para a funcionalidade de maximizar e minimizar a tela. Desta forma será possível redimensionar a tela entre os dois estados.

Arquivo: RM.Prj.Insumo.Form.dll

## 11.83.55.137

* **[Ticket: 07\TRXO78]** Durante o processo que exportar o Pert para o Cronograma o replanejamento do cronograma planejado quando o percentual concluído for zero (0) ou igual ao lançando em um período fechado.

Arquivo: RM.Prj.Tarefa.Data.dll

* **[Ticket: 07\TRWCJD]** Importação de composição nao atualizava o campo DNIT

Arquivo: RM.Prj.Composicao.Data.dll

## 11.83.55.138

* **[Ticket: 07\TRYH75]** Realizado ajuste no processo de copia de tarefas associadas a insumos derivados.

Arquivos: RM.Prj.Projeto.Data.dll, RM.Prj.Projeto.Form.dll, RM.Prj.Projeto.Intf.dll

* **[Ticket: 07\TRYADM]** Durante a edição do apontamento será verificado qual é o status original do apontamento.Assim as colunas que devem ser bloqueadas quando o status for igual à validado, serão bloqueadas após a confirmação do registro.

Arquivo: RM.Prj.Mobilidade.Form.dll

* **[Ticket: 07\TRYADE]** Adicionando a permissão de acesso ao projeto do usuário conectado (contexto).O Usuário somente poderá associar o coletor em projetos que o mesmo possua permissão de acesso.

Arquivos: RM.Prj.Mobilidade.Form.dll, RM.Prj.Mobilidade.Data.dll

## 11.83.55.140

* **[Ticket: 07\TGIQDR]** Atualização das regras de validação para exclusão dos Projetos. Serão considerados para exclusão dos Projetos as permissões de segurança.

Arquivo: RM.Prj.Projeto.Form.dll

* **[Ticket: 07\TRXWOX]** Inclusão de recurso da composição através do anexo não está incluindo a máscara de insumo no lookup.

Arquivo: RM.Prj.Composicao.Form.dll

## 11.83.55.141

* **[Ticket: 07\TRZXRJ]** Melhoria em mensagem ao importar Tarefas via MSProject utilizando código EDT

Arquivos: RM.Prj.Classes.Server.dll, RM.Prj.Tarefa.Data.dll, RM.Prj.Planilhas.Data.dll

* **[Ticket: 07\TIANCV]** Inclusão do campo unidade da composição e dos recursos no relatório de modelo fixo excel de composição analítica de preço unitário por produção

Arquivo: RM.Prj.Composicao.Data.dll

* **[Ticket: 07\TIANCV]** Inclusão da unidade da composição e dos recursos no relatório de modelo fixo excel de composição analítica de preço unitário por produção

Arquivo: RM.Prj.Composicao.Data.dll

## 11.83.55.143

* **[Ticket: Alterações Gerais]** Melhorias TOP Mobile

Arquivos: RM.Prj.Insumo.Data.dll, RM.Prj.Utils.Intf.dll, RM.Prj.EquipeProjeto.Intf.dll, RM.Prj.EquipeProjeto.Data.dll, RM.Prj.Formula.dll, RM.Prj.Utils.Form.dll, RM.Prj.Insumo.Intf.dll, RM.Prj.Utils.Server.dll, RM.Prj.Mobilidade.Form.dll, RM.Prj.Parametros.Form.dll, RM.Prj.Mobilidade.Intf.dll, RM.Prj.Planilhas.Form.dll, RM.Prj.IntegracaoNexus.Intf.dll, RM.Prj.Mobilidade.Server.dll, RM.Prj.Parametros.Intf.dll, RM.Prj.Mobilidade.Data.dll, RM.Prj.EquipeProjeto.Form.dll, RM.Prj.Parametros.Data.dll

* **[Ticket: 07\TRQWDT]** Tratamentos para o cancelamento do processo

Arquivo: RM.Prj.Tarefa.Data.dll

## 11.83.55.144

* **[Ticket: 07\TSBGAU]** Ao Editar a valor da quantidade da Etapa na visão.Durante à alteração da quantidade da obra estava sendo impresso uma mensagem que valida altrerações em etapas. O evento foi verificado e a mensagem será impressa apenas nas alterações das etapas.

Arquivo: RM.Prj.Planilhas.Form.dll

* **[Ticket: Alterações Gerais]** Criação de filtro padrão na planilha para buscar por data programada da tarefa

Arquivo: RM.Prj.Utils.Form.dll

* **[Ticket: Alterações Gerais]** Inclusão de filtro "Por Período"

Arquivo: RM.Prj.Utils.Form.dll

## 11.83.55.146

* **[Ticket: 07\TSCN57]** cancelar processo de exportação do PERT para o cronograma

Arquivos: RM.Prj.Tarefa.Form.dll, RM.Prj.Tarefa.Intf.dll, RM.Prj.Cronograma.Server.dll, RM.Prj.Tarefa.Data.dll

* **[Ticket: 07\TSBXKM]** Ajuste ao finalizar o processo de espacilizar insumo

Arquivo: RM.Prj.Insumo.Form.dll

## 11.83.55.147

* **[Ticket: Alterações Gerais]** Ajuste no filtro de visão de apontamento de equipamento

Arquivo: RM.Prj.Mobilidade.Data.dll

* **[Ticket: Alterações Gerais]** Ajuste no apontamento de equipamento

Arquivo: RM.Prj.Insumo.Data.dll

## 11.83.55.148

* **[Ticket: 07\TSDYBH]** Ajuste no Filtro da planilha de Atividade

Arquivo: RM.Prj.Utils.Form.dll

* **[Ticket: 07\TSEKRQ]** Atualização realizada no processo de Importar Tarefas via MS-Project. Os componentes referentes ao Nome, Descrição, Unidade, Valor Cotado, Nome Recurso, Tipo Recurso e BDI Diferenciado foram atualizados.

Arquivos: RM.Prj.Planilhas.Form.dll, RM.Prj.Planilhas.Intf.dll

* **[Ticket: Alterações Gerais]** Ajuste no cadastro de Equipe

Arquivo: RM.Prj.EquipeProjeto.Form.dll

## 11.83.55.149

* **[Ticket: 07\TRIPPP]** Melhoria em Curva ABC de composição, inclusão de coluna Valor Unitário e Valor Unitário (Médio)

Arquivo: RM.Prj.Composicao.Data.dll

* **[Ticket: 07\TRQWDT]** Cronograma planejado por quantidade gerava diferença nos relatórios de histograma

Arquivo: RM.Prj.Calculo.Server.dll

## 11.83.55.150

* **[Ticket: 07\TSFCYS]** Ajuste no processo 'Planejar Resposta' do módulo 'Gestão de Riscos'.

Arquivo: RM.Prj.GestaoRiscos.Form.dll

* **[Ticket: 07\TSF492]** Ajuste na tela de cancelamento de apontamento

Arquivo: RM.Prj.Mobilidade.Form.dll

* **[Ticket: 07\TSF492]** Ajuste na função de Formula da folha tarefa. Ajuste no processo de Inclusão de Membro

Arquivos: RM.Prj.Mobilidade.Server.dll, RM.Prj.EquipeProjeto.Form.dll, RM.Prj.Mobilidade.Form.dll

## 11.83.55.151

* **[Ticket: 07\TSFYMD]** Ajuste no calculo do valor de composições com vigencia, e existencia de planilha de serviço com cronograma diferente da planilha de atividades.

Arquivo: RM.Prj.Calculo.Server.dll

* **[Ticket: 07\TSFCYK]** Ajuste na mensagem de atualização do Pert e Validação do apontamento de avanço fisico

Arquivo: RM.Prj.Mobilidade.Form.dll

* **[Ticket: Alterações Gerais]** Correção dos arquivos do TFS que perderam o checkin em virtude da restauração do backup.

Arquivo: RM.Prj.PedidoMaterial.Form.dll

## 11.83.55.157

* **[Ticket: 07\TSLQXJ]** O Processo deverá fazer a distribuição proporcional, respeitando os períodos fechados.

Arquivo: RM.Prj.Cadastros.Server.dll

## 11.83.55.158

* **[Ticket: 07\TSOQMQ]** Melhoria na exclusão de apontamento da NG

Arquivos: RM.Prj.Mobilidade.Data.dll, RM.Projetos.exe, RM.Prj.Mobilidade.Intf.dll, RM.Prj.Mobilidade.Server.dll, RM.Prj.Mobilidade.Form.dll

## 11.83.55.166

* **[Ticket: 07\TSQKMG]** Ajuste em tela de recurso de composição ao inserir uma Composição auxiliar do tipo Equipamento

Arquivos: RM.Prj.Composicao.Form.dll, RM.Prj.Composicao.Data.dll

* **[Ticket: 07\TSQEM4]** Ajuste na liberação de período em contratos do tipo insumo

Arquivos: RM.Prj.Contrato.Server.dll, RM.Prj.Contrato.Form.dll

## 11.83.55.167

* **[Ticket: 07\TSVAZX]** Atualização realizada no processo de geração de pedidos para materiais. Desta forma serão exibidos todos os insumos.

Arquivos: RM.Prj.Insumo.Server.dll, RM.Prj.PedidoMaterial.Form.dll

## 11.83.55.169

* **[Ticket: 07\TSUNW5]** Ajustado exclusão de folha tarefa cancelada, caso a folha tarefa não tenha apontamentos de mão de obra "Apropriado" ou percentual "Executado" de avanço físico a folha ooderá ser excluída

Arquivo: RM.Prj.Mobilidade.Data.dll

* **[Ticket: 07\TSXWNL]** Ajuste para padronizar comportamento de processo de agendamento de execução de mensagens genericas e de mensagem de status de funcionario. No processo de agendamento de execução de mensagem de status de funcionario sera validado a existencia de agendamento realizado, evitar conflitos de agendamentos repetidos principalmente com recorrencia.

Arquivo: RM.Prj.Mobilidade.Form.dll

* **[Ticket: 07\TSWYAJ]** Ajustes em Descrição de componentes em parâmetros de projeto / "Mobilidade"

Arquivo: RM.Prj.Parametros.Form.dll

## 11.83.55.170

* **[Ticket: 07\TSYPNX]** Ajuste no status do log após executar o processo "Ativar Coletores Móveis" e apresentar ressalvas no final.

Arquivos: RM.Projetos.exe, RM.Prj.Mobilidade.Data.dll

## 11.83.55.171

* **[Ticket: 07\TSZLNC]** Ajuste na funcionalidade da Planilha de Atividades ao realizar a funcionalidade "Copiar Tarefas / Etapas".

Arquivo: RM.Prj.Planilhas.Intf.dll

## 11.83.55.172

* **[Ticket: 07\TSZJQ6]** Ao executar o processo de Importação de Insumos via Excel o processo irá logar os insumos inconsistente e continuar o processo importando o restante dos insumos

Arquivos: RM.Prj.Importacao.Data.dll, RM.Prj.Importacao.Form.dll

## 11.83.55.174

* **[Ticket: 07\TTCMWV]** Rateio de contrato de tarefas permite associação de centros de custo bloqueados.

Arquivos: RM.Prj.Projeto.Form.dll, RM.Prj.Planilhas.Form.dll

## 11.83.55.178

* **[Ticket: 07\TTEZKP]** No processo Gerar Apropriação de Mão de obra, serão listados os apontamentos avulsos. Que estão vinculados em folhas tarefa que permitem tais apontamento (tipo apontamento avulso).

Arquivo: RM.Prj.Mobilidade.Server.dll

* **[Ticket: 07\TTFSKW]** Ao copiar um insumo derivado e especializado que possui produto associado, que provoque a cópia de uma composição que possui o próprio insumo, o mesmo está sendo copiado 2 vezes.

Arquivo: RM.Prj.Projeto.Data.dll

## 11.83.55.180

* **[Ticket: 07\TTH475]** A mensagem era impressa devido a verificação de atividades associadas a serviços.Foram adicionados novas validações, que garantem a execução do processo.

Arquivo: RM.Prj.Projeto.Data.dll

* **[Ticket: 07\TTE947]** Verificado as alterações não confirmadas, realizadas em anexos dependentes.

Arquivo: RM.Prj.Composicao.Form.dll

## 11.83.55.251

* **[Ticket: 07\TVVKQ3]** Correção em função de alteração na lib.

Arquivo: RM.Prj.Mobilidade.Server.dll

## 11.83.55.263

* **[Ticket: Alterações Gerais]**

Arquivos: RM.Prj.Composicao.Intf.dll, RM.Prj.GrupoCusto.Intf.dll, RM.Prj.Parametros.Form.dll, RM.Prj.Mobilidade.Server.dll, RM.Prj.BackupRestore.Intf.dll, RM.Prj.BackupRestore.Form.dll, RM.Prj.GrupoCusto.Data.dll, RM.Prj.Projeto.Form.dll

# TOTVS Educacional

## 11.83.55.100

* **[Ticket: 07\TR8502]** Melhoria no tratamento da integração financeira com o Protheus.

Arquivos: RM.Edu.Parametros.Form.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Financeiro.Server.dll

## 11.83.55.102

* **[Ticket: 07\TRAJSR]** Melhoria no tratamento das informações bancárias ao enviar informações de lançamentos a receber e adequação do sistema para registrar na tabela De-Para o código da baixa gerada de baixa automática.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.Financeiro.Server.dll, RM.Edu.Integracoes.Server.dll, RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## 11.83.55.105

* **[Ticket: Alterações Gerais]** Disponibilizada a funcionalidade de importação dos dados do Scientia para o TOTVS Educacional de acordo com as regras do Modelo 2.

Arquivos: RM.Edu.Integracoes.Data.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Parametros.Data.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Integracoes.Server.dll, RM.Edu.Integracoes.Form.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Consts.dll, RM.Edu.dll, RM.Edu.Integracoes.Intf.dll

* **[Ticket: Alterações Gerais]** Implementação de funcionalidade de importação dos professores do horário a partir do Scientia.

Arquivo: RM.Edu.Integracoes.Form.dll

## 11.83.55.106

* **[Ticket: 07\TQICPN]** Possível identificar o Campus para o curso/habilitação do aluno no ato da matricula dos aprovados no processo seletivo.Criado o vínculo "de-para" entre a forma de inscrição (Processo Seletivo) e o tipo de ingresso (Educacional).

Arquivos: RM.Edu.ProcSel.Data.dll, RM.Edu.Interfaces.Intf.dll, RM.EduPS.Inscricoes.Form.dll, RM.Edu.ProcSel.Form.dll, RM.Edu.ProcSel.Intf.dll, RM.Edu.ProcSel.Server.dll, RM.Edu.Facade.dll, RM.Edu.dll

* **[Ticket: 07\TQQOWR]** - Foi retirado o campo de tipo de oferta da tela de Dados do Curso para o Censo Escolar e SISTEC da Habilitação.- Foi incluído o campo de tipo de oferta integrada no cadastro de curso.- Foi incluído também o tipo de curso na tela de dados do censo escolar para o curso/habilitação do aluno com as opções: Integrada, Concomitante e Subsequente. Se for marcado a opção tipo de oferta integrada no curso, o cadastro receberá o valor padrão como integrada.

Arquivos: RM.Edu.Matricula.Form.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.MatrizCurricular.Form.dll, RM.Edu.Matricula.Data.dll, RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.Matricula.Intf.dll

## 11.83.55.108

* **[Ticket: 07\TRCM97]** Melhoria no cadastro de Cursos / Habilitações - o botão de Análise Curricular ficará ativo apenas se for edição de registro.

Arquivo: RM.Edu.Matricula.Form.dll

* **[Ticket: 07\TQSZC9]** Ajuste no processo de "Copiar de Avalações para outras Turmas/Disciplinas".

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

## 11.83.55.109

* **[Ticket: 07\TRASN7]** Melhoria na integração contábil ao definir o período contábil para a integração entre o Educacional e o BackOffice do Protheus.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEducacionalSigaCTB.dll

## 11.83.55.111

* **[Ticket: 07\TRFYQ8]** Inclusão das mensagem de unidade de medida e grupo de estoque na integração Educacional x Protheus devido a melhoria na mensagem de Produto para adaptação da mensagem para cadastro de produtos globais.

Arquivos: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll, RM.Edu.Integracoes.Server.dll

## 11.83.55.112

* **[Ticket: 07\TRGJV0]** Adaptação da geração de responsável financeiro para inclusão dos campos de código do município, tipo de bairro e tipo de rua no cadastro de cliente/fornecedor.

Arquivos: RM.Edu.Facade.dll, RM.Edu.Aluno.Data.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Cadastros.Server.dll

## 11.83.55.113

* **[Ticket: 07\TRGXE2]** Melhoria da validação para identificação dos valores de bolsas disponíveis quando a solicitação é realizada pela mensagem única UpdateContractParcel para a integração.

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: 07\TQTLJW]** Foi realizada otimização do processo de cancelamento de contratos, no que tange a contabilização por competência, para que as apropriações mensais efetuadas sejam mantidas e a contabilização do contrato seja estornada para que seja feita nova contabilização com base nas apropriações já efetuadas.

Arquivo: RM.Edu.Contabil.Server.dll

## 11.83.55.115

* **[Ticket: 07\TRHSFL]** Melhoria no cancelamento de lançamento quando houver uma solicitação da integração com o Protheus por mensageria única.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

* **[Ticket: 07\TRFOCW]** Ajuste na digitação de frequência no portal do professor impedindo que alunos com resultado final tenham sua frequência atualizada.

Arquivo: App\_Web\_edufrequenciadiariawebform.ascx.497dfae.dll

## 11.83.55.116

* **[Ticket: 07\TRMC26]** Melhoria no teste de conexão a base de dados Protheus nos parâmetros do Educacional.

Arquivo: RM.Edu.Parametros.Data.dll

* **[Ticket: 07\TRHASI]** A rotina de transferência interna foi alterada para suportar código de situação de matrícula com até 10 caracteres.

Arquivo: RM.Edu.Matricula.Intf.dll

## 11.83.55.117

* **[Ticket: 07\TRGWZ2]** Otimização de geração de acordo

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.120

* **[Ticket: Alterações Gerais]** Implementação do Código da Turma, na matrícula do processo seletivo terceirizado.

Arquivos: RM.Edu.ProcSel.Form.dll, RM.Edu.ProcSel.Intf.dll, RM.Edu.ProcSel.Data.dll

* **[Ticket: Alterações Gerais]** Implementação para permitir o cliente cadastrar contratos do tipo "Serviço" no educacional, onde o mesmo possuir vínculo com os itens dos contratos do Nucleus.

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Edu.Processos.Data.dll

## 11.83.55.121

* **[Ticket: 07\TRORE5]** Melhoria na consulta de valores de bolsas e descontos na mensagem de requisição UPDATECONTRACTPARCEL

Arquivos: RM.Edu.dll, RM.Edu.Integracoes.Server.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Parametros.Form.dll

* **[Ticket: 07\TRNMVS]** Foi realizada otimização do cadastro de contrato do tipo plano de forma que seja possível incluir contratos dessa modalidade em bases de dados Oracle.

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.122

* **[Ticket: 07\TRDOM9]** O processo de inscrição de candidatos a uma vaga foi alterado para que o campo turma seja filtrado pelas informações selecionadas anteriormente na tela.

Arquivo: RM.Edu.MatrizCurricular.Form.dll

## 11.83.55.123

* **[Ticket: 07\TROUYM]** Melhoria na integração contábil para envio das informações de Item Contábil e Classe de Valor em integrações por mensageria única com o Protheus.

Arquivos: RM.Edu.Integracoes.Server.dll, RM.Edu.Parametros.Intf.dll, RM.Edu.Financeiro.Data.dll, RM.Edu.Facade.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Financeiro.Intf.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Contabil.Server.dll

* **[Ticket: Alterações Gerais]** Disponibilizado o servico GetInfoClasseValorItemContabil na dll RM.Financeiro.Server

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Interfaces.Intf.dll

* **[Ticket: Alterações Gerais]** Adicionando summary

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Financeiro.Server.dll

* **[Ticket: 07\TROUYM]** Otimização de consultas no processo de contabilização por competência.

Arquivo: RM.Edu.Contabil.Server.dll

## 11.83.55.125

* **[Ticket: Alterações Gerais]** Integração Modelo 2 do TOTVS Educacional X Scientia

Arquivos: RM.Edu.Consts.dll, RM.Edu.Integracoes.Form.dll, RM.Edu.Matricula.Server.dll, RM.Edu.Lib.Intf.dll, RM.Edu.PeriodoLetivo.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.dll, RM.Edu.Integracoes.Data.dll, RM.Edu.Lib.Server.dll, RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.Lib.WinForms.dll, RM.Edu.Facade.dll, RM.Edu.Services.Server.dll, RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.Academico.Server.dll, RM.Edu.Integracoes.Intf.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Integracoes.Server.dll

* **[Ticket: Alterações Gerais]** Modelo 2 de integração TOTVS Educacional com o Scientia

Arquivos: RM.Edu.dll, RM.Edu.Integracoes.Form.dll

* **[Ticket: Alterações Gerais]** Integração do TOTVS Educacional com o Scientia

Arquivo: RM.Edu.Lib.WinForms.dll

## 11.83.55.126

* **[Ticket: Alterações Gerais]** Carga de valores no evento contábil para contabilização integrada ao Protheus.

Arquivo: RM.Edu.Contabil.Server.dll

## 11.83.55.127

* **[Ticket: Alterações Gerais]** Adequação da consulta no serviço GetInfoClasseValorItemContabil

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: Alterações Gerais]** Disponibilizado no serviço GetInfoClassevalorItemcontabil informação referente a mais de uma matriz aplicada.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Financeiro.Server.dll

* **[Ticket: Alterações Gerais]** Ajuste na integração com Protheus dados contábeis

Arquivo: RM.Edu.Lib.Intf.dll

## 11.83.55.128

* **[Ticket: 07\TRRS22]** Bloqueio na utilização do parâmetro "Manter o contrato original e alterar a matriz aplicada para matriz do aluno", quando a transferência interna for realizada para períodos letivos diferentes. O contrato só é atualizado quando a matriz de destino está no mesmo período letivo da matriz de origem.

Arquivo: RM.Edu.Matricula.Form.dll

## 11.83.55.129

* **[Ticket: 07\TRRX40]** Ajuste na seleção dos Tipos de Sala durante a reserva de instalação, permitindo que todos os registros sejam carregados durante a exibição da página.

Arquivos: Portal Corpore.Net

## 11.83.55.130

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia: Modelo 2

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.Integracoes.Server.dll

## 11.83.55.131

* **[Ticket: 07\TRUIB2]** Otimizações no processo de Gerar Contabilização do contrato em lote:- Na visão de contratos, ao selecionar vários registros para contabilizar, não deverá executar o processo para contratos cancelados.- Tratamento para não apresentar a mensagem “Violação de chave estrangeira”.

Arquivo: RM.Edu.Contabil.Server.dll

## 11.83.55.134

* **[Ticket: Alterações Gerais]** Otimização da validação de choque de horário na criação da oferta pela integração com o Scientia.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.136

* **[Ticket: 07\TRUOJ0]** Foi realizada uma otimização na validação de turmas disciplinas gerenciais, quando esta possuir turmas gerenciadas que contenha alunos matriculados.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## 11.83.55.137

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia: Modelo 2

Arquivo: RM.Edu.Integracoes.Data.dll

## 11.83.55.140

* **[Ticket: 07\TRNNIE]** Melhoria no processo de exclusão de Recurso - sistema realiza validação dos registros de Recursos e/ou Campos Complementares do Recurso.

Arquivos: RM.Edu.Cadastros.Intf.dll, RM.Edu.Cadastros.Data.dll

## 11.83.55.141

* **[Ticket: Alterações Gerais]** Ajustes na integração TOTVS Educacional X Scientia: Modelo 2

Arquivos: RM.Edu.Integracoes.Form.dll, RM.Edu.Integracoes.Server.dll, RM.Edu.PeriodoLetivo.Server.dll

* **[Ticket: 07\TRYXMQ]** Alteração do Censo do Ensino Superior conforme leiaute de 2014.

Arquivos: RM.Edu.Matricula.Form.dll, RM.Edu.Academico.Server.dll, RM.Edu.Matricula.Data.dll, RM.Edu.Academico.Form.dll, RM.Edu.Matricula.Intf.dll, RM.Edu.Lib.Intf.dll

## 11.83.55.142

* **[Ticket: 07\TRVCJK]** Alteração no método de criação de lançamento financeiro no processo de solicitação de Atendimento. As parcelas devem ser criadas antes da criação do lançamento no financeiro.

Arquivo: RM.Edu.Aluno.Server.dll

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia: Modelo 2 - Turmas/Disciplinas gerencial e gerenciadas

Arquivo: RM.Edu.Integracoes.Server.dll

## 11.83.55.143

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia: Modelo 2 - Ajustes da importaçao dos dados do Scientia

Arquivos: RM.Edu.Integracoes.Server.dll, RM.Edu.Integracoes.Form.dll, RM.Edu.Parametros.Form.dll

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia: Modelo 2 - ajuste na definição do número máximo de alunos da turma/disciplina gerencial

Arquivo: RM.Edu.Integracoes.Server.dll

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia - verificação de professor autorizado a lecionar uma disciplina

Arquivo: RM.Edu.Integracoes.Server.dll

* **[Ticket: 07\TSAZOO]** Alteração nos campos de mobilidade acadêmica para se adequarem às seguintes regras do INEP:\* Tipo de mobilidade acadêmica: Campo de preenchimento obrigatório quando informada a opção “1 - Sim” no campo Mobilidade acadêmica e a IES é Federal ou Universidade Estadual.\* IES destino: Campo de preenchimento obrigatório quando informada a opção “1 - Nacional” no campo Tipo de mobilidade acadêmica.\* Tipo de mobilidade acadêmica internacional: Campo de preenchimento obrigatório em duas situações:1) IES Federal ou Universidade estadual: se informada a opção “2 - Internacional” no campo Tipo de mobilidade acadêmica. 2) Demais IES: se informada a opção “1 – SIM” no campo Mobilidade Acadêmica.\* País destino: Campo de preenchimento obrigatório quando informada qualquer opção no campo Tipo de mobilidade acadêmica internacional.

Arquivos: RM.Edu.Matricula.Form.dll, RM.Edu.Matricula.Data.dll

## 11.83.55.145

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia - ajustes na geração de plano de aula

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Integracoes.Server.dll

## 11.83.55.146

* **[Ticket: 07\TSCRUV]** Ajuste no processo de matrícula em lote, executando a matrícula dos alunos apenas nas turmas disciplinas selecionadas no grid.

Arquivo: RM.Edu.Matricula.Form.dll

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia: Modelo 2 - otimizando a exportação de dados para o Scientia.

Arquivo: RM.Edu.Integracoes.Server.dll

## 11.83.55.148

* **[Ticket: 07\TSDTFG]** Ajuste no processo de matrícula de alunos nas disciplinas em lote, possibilitando a execução do mesmo em ambientes 3 camadas.

Arquivo: RM.Edu.Matricula.Form.dll

## 11.83.55.149

### Rotina: IRM de Controle de Defeitos do HIS

* **[Ticket: PCREQ-1160]** Melhoria no cadastro de Bancos, Agências, Contas Correntes, Contas Caixas e Convênios atravês da integração utilizando mensageria única.

Arquivos: RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.Edu.ConfiguraIntegracao.TotvsEducacionalSigaCTB.dll, RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## 11.83.55.151

* **[Ticket: Alterações Gerais]** Foram feitos ajustes nos fontes para realização de mesclagem entre o backup do TFS e os fontes recuperados pelo time de engenharia, referentes ao dia 15/05/2015.

Arquivos: Portal Corpore.Net

## 11.83.55.152

* **[Ticket: 07\TSGWV1]** Alterações nos tratamentos das informações geradas para a integração por mensageria única dos sistemas Educacionais

Arquivos: RM.Bib.Parametros.Intf.dll, RM.Fin.Lan.Service.dll, RM.EduPS.Facade.Server.dll, RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll, RM.Bib.Importacao.Server.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Integracoes.Server.dll, RM.Ctb.Lan.Service.dll, RM.Bib.Parametros.Data.dll, RM.Bib.Facade.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.EduPS.Cadastros.Form.dll, RM.EduPS.Processos.Data.dll, RM.Bib.Lib.Intf.dll, RM.Edu.Integracoes.Intf.dll, RM.Edu.Financeiro.Server.dll, RM.Fin.Lan.Form.dll

* **[Ticket: 07\TSGY12]** - Melhoria no tratamento da mensagem utilizada no envio de informações de lançamentos contábeis para a mensageria única.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEducacionalSigaCTB.dll

## 11.83.55.154

* **[Ticket: 07\TSISLO]** Otimizado processo de matrícula de candidatos em processos seletivos terceirizados onde o próprio candidato é o responsável financeiro quando há integração com o Protheus.

Arquivos: RM.Edu.ProcSel.Data.dll, RM.Edu.Facade.dll

* **[Ticket: Alterações Gerais]** Integração TOTVS Educacional X Scientia: Modelo 2 - ajuste na exportação de staff

Arquivos: RM.Edu.Integracoes.Intf.dll, RM.Edu.Integracoes.Form.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.dll, RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.Parametros.Intf.dll, RM.Edu.Integracoes.Data.dll, RM.Edu.Integracoes.Server.dll, RM.Edu.MatrizCurricular.Server.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Consts.dll

* **[Ticket: 07\TQVVBI]** Ajuste na validação ao cancelar um contrato quando se altera a situação de matrícula de um aluno e a nova situação de matrícula exige o cancelamento do contrato.

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Form.dll

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Melhoria na geração da mensagem de lançamentos a receber a partir do Educacional para a integração por mensageria única.

Arquivo: RM.Edu.Integracoes.Server.dll

## 11.83.55.155

* **[Ticket: 07\TQXZIO]** Alteração do Educacenso conforme leiaute de 2015.

Arquivos: RM.Edu.Cadastros.Form.dll, RM.Edu.Consts.dll, RM.Edu.Cadastros.Intf.dll, RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.Classes.Server.dll, RM.Edu.Academico.Form.dll, RM.Edu.PeriodoLetivo.Form.dll, RM.Edu.PeriodoLetivo.Intf.dll, RM.Edu.Cadastros.Data.dll

* **[Ticket: 07\TSKKXJ]** Alterado no cadastro de Habilitação, no campo Tipo de Habilitação permitirá preencher códigos com até 3 dígitos.

Arquivo: RM.Edu.MatrizCurricular.Intf.dll

* **[Ticket: 07\TSKKEU]** Retirada do campo CODINEP, pois o script dele não foi liberado ainda e ele não é utilizado na funcionalidade.

Arquivo: RM.Edu.MatrizCurricular.Data.dll

* **[Ticket: 07\TSKV15]** Alterada a data de estorno das apropriações para buscar a data atual do sistema

Arquivo: RM.Edu.Contabil.Server.dll

## 11.83.55.156

* **[Ticket: 07\TSKGME]** Melhoria da validação de choque de horário de Salas no cadastro de Turma/Disciplina.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.157

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Ajuste no recebimento do retorno da mensagem de baixa de lançamentos financeiros para um melhor tratamento em cenário onde houver uma mensagem de erro.

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## 11.83.55.158

* **[Ticket: 07\TQXZIO]** Inclusão do parâmetro para escola com proposta pedagógica de formação por alternância.Inclusão do parâmetro para função que o professor exerce na escola.

Arquivos: RM.Edu.PeriodoLetivo.Form.dll, RM.Edu.Academico.Form.dll, RM.Edu.Consts.dll, RM.Edu.PeriodoLetivo.Intf.dll, RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.Cadastros.Data.dll, RM.Edu.Cadastros.Intf.dll, RM.Edu.Cadastros.Form.dll

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Ajuste na mensagem de baixa de lançamentos financeiros e nas rotinas de geração da mensagem para enviar a informação da chave da conta-caixa cadastrada no De-Para ao cadastrar o banco quando baixa automática para lançamentos zerados.

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: PCREQ-3488]** Ajuste na mensagem de baixa de lançamentos financeiros e nas rotinas de geração da mensagem para enviar a informação da chave da conta-caixa cadastrada no De-Para ao cadastrar o banco.

Arquivos: RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.Edu.Financeiro.Server.dll

* **[Ticket: PCREQ-3488]** Ajuste interno no serviço de retorno de parâmetros para validação de informações do Educacional em integrações com o Protheus.

Arquivo: RM.Edu.Parametros.Data.dll

## 11.83.55.159

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Ajuste na regra de cálculo do desconto condicional na mensagem UPDATECONTRACTPARCEL para abater do total de desconto o que já foi concedido em baixas parciais.

Arquivo: RM.Edu.Integracoes.Server.dll

## 11.83.55.161

* **[Ticket: 07\TSLGR8]** Tratamento na rotina que insere um novo recurso.

Arquivo: RM.Edu.Cadastros.Data.dll

## 11.83.55.162

* **[Ticket: 07\TSCOAG]** Tratamento nos campos Status, Linha de Pesquisa e Tipo de TCC no cadastro de TCC pelo TOTVS Educacional para considerar o nível de ensino selecionado no contexto.

Arquivo: RM.Edu.MatrizCurricular.Form.dll

* **[Ticket: 07\TSPUFZ]** Alterado assistente de Repasse de Bolsa, para permitir a opção de “Cancelar repasses” quando o valor do lançamento for igual ao valor do repasse. Nesta situação, somente a baixa do lançamento será cancelada.

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.163

* **[Ticket: 07\TSIUEA]** Tratamento na validação dos pontos distribuídos na etapa com os pontos do modelo de avaliação por curso, quando o parâmetro "Permitir que os pontos das avaliações sejam superiores aos pontos distribuídos nas etapas" esteja marcado nas configurações.

Arquivos: RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.Services.Server.dll

## 11.83.55.164

* **[Ticket: 07\TSKL51]** Tratamento na rotina que traz os professores autorizados nas disciplinas ao executar o processo de Cadastro de Turmas e Turmas/Disciplinas, quando o parâmetro "Considerar somente disciplinas autorizadas" esteja marcado nas configurações da secretaria.

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

* **[Ticket: 07\TSQYKT]** Ajuste na exibição das notas conceituais na tela de Digitação de Notas de Avaliações

Arquivo: RM.Edu.NotaFalta.Data.dll

## 11.83.55.167

* **[Ticket: 07\TSCPNB]** Alterado Sistema para excluir os dados do Censo e Sistec antes de excluir uma matrícula no período letivo.

Arquivo: RM.Edu.Matricula.Server.dll

* **[Ticket: 07\TRDA71]** Alteração no cadastro de autorização/reconhecimento da IES para que possa ser cadastrado mais de um registro para a mesma filial, conforme legislação.

Arquivos: RM.Edu.Utils.Server.dll, RM.Edu.Cadastros.Intf.dll, RM.Edu.dll, RM.Edu.Cadastros.Form.dll, RM.Edu.Cadastros.Data.dll, RM.Edu.Consts.dll

## 11.83.55.169

* **[Ticket: 07\TSQORI]** A nomenclatura do parâmetro para a busca do centro de custo da turma estava errada. O parâmetro deve ser "Da Turma" e não "Da Turma/Disciplina", uma vez que o sistema utiliza o centro de custo da turma cadastrada na matrícula do aluno e não da turma/disciplina. Sendo assim, a nomenclatura do parâmetro foi alterada para "Da Turma".

Arquivo: RM.Edu.Consts.dll

* **[Ticket: 07\TSWG06]** Ajuste na consulta que traz os participantes da banca considerando a coligada, pois a mesma não estava efetuando esta consideração ao trazer os participantes.

Arquivo: RM.Edu.MatrizCurricular.Data.dll

* **[Ticket: 07\TSIUEA]** Tratamento na validação dos pontos distribuídos na etapa das disciplinas com o somatório dos pontos das avaliações, para que seja permitido que os pontos distribuídos sejam menores que a soma dos pontos das avaliações, quando o parâmetro "Permitir que os pontos das avaliações sejam superiores aos pontos distribuídos nas etapas" esteja marcado nas configurações da secretaria.

Arquivo: RM.Edu.Services.Server.dll

## 11.83.55.170

* **[Ticket: Alterações Gerais]** Disponibilização dos valores de bolsa permanente e bolsa até o vencimento no serviço para requisição de valores de bolsa e desconto condicional.

Arquivo: RM.Edu.Integracoes.Server.dll

* **[Ticket: 07\TSYAZ4]** Ajustes no processo de cadastro de turmas/disciplinas

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

## 11.83.55.171

* **[Ticket: 07\TSZR99]** Melhoria na validação das informações sobre certidão de nascimento/casamento.

Arquivo: RM.Edu.Lib.Intf.dll

* **[Ticket: 07\TSEC17]** Criado menu de permissões Gerador Web dentro do módulo Educacional para permitir a visualização de relatórios do gerador antigo pelo Portal.

Arquivo: RM.Edu.dll

## 11.83.55.173

* **[Ticket: 07\TTAHTM]** Ajuste no processo para descartar disciplinas ministradas exclusivamente em cursos não recenseados

Arquivo: RM.Edu.Academico.Server.dll

* **[Ticket: 07\TSEC17]** criado menu de permissões Gerador de Relatórios dentro do módulo Educacional para permitir a visualização de relatórios pelo Portal.

Arquivo: RM.Edu.dll

## 11.83.55.174

* **[Ticket: 07\TSZWFP]** A tela de Dados dos Censo Escolar do Aluno foi alterada para que nenhum campo desapareça ao editar e salvar alguma informação.

Arquivo: RM.Edu.Aluno.Form.dll

* **[Ticket: 07\TT4835]** Foi criado um novo parâmetro no sistema, para permitir que no processo de Cancelar Contrato, os estornos da contabilização tenham a data de cancelamento do contrato informado durante o processo:Parâmetros > Integração > Financeiro > "Fin - Geral 3/3" > "Considera a data de cancelamento do contrato para a data do estorno contábil no processo de cancelamento de contrato"Somente se este parâmetro estiver marcado, os estornos da contabilização receberão a mesma data informada no processo de "Cancelar contrato". Com o parâmetro desmarcado, o comportamento do sistema se manteve o mesmo.

Arquivos: RM.Edu.Parametros.Intf.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Contabil.Server.dll, RM.Edu.Parametros.Form.dll

* **[Ticket: 07\TTASBZ]** Tratamento no processo de geração de plano de aula sequencial para que o contador de dias úteis não seja zerado a cada disciplina na geração do plano.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## 11.83.55.178

* **[Ticket: 07\TTDHXH]** Ajuste no comportamento das 3 opções de permissão educacional referentes a alteração de notas e faltas na digitação de frequência diária pelo executável.

Arquivos: RM.Edu.Parametros.Form.dll, RM.Edu.NotaFalta.Data.dll, RM.Edu.NotaFalta.Form.dll

* **[Ticket: 07\TTFGLE]** Ajuste na contabilização do contrato quando o contexto de execução de fórmulas é a bolsa

Arquivo: RM.Edu.Contabil.Server.dll

## 11.83.55.179

* **[Ticket: 07\TTGQQJ]** Alterado no Contrato Educacional, ao gerar lançamento cujo valor liquido seja zero e esteja marcado o parâmetro Educacional “Baixar automaticamente lançamentos com valor líquido igual a zero”, a data da baixa deverá obedecer a parametrização do Finacneiro “Data default da baixa a receber”.

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.182

* **[Ticket: 07\TSCBN6]** Ajustes na edição do TCC, via portal.

Arquivo: App\_Web\_edutccalunowebform.ascx.1d4ca059.dll

* **[Ticket: 07\TSCDDC]** Ajustes ao anexar o arquivo no email a ser enviado no arquivo final do TCC.

Arquivos: Portal Corpore.Net

## 11.83.55.190

* **[Ticket: 07\TTSANJ]** Ajuste na carga de dados do lançamento financeiro quando integração com Backoffice Protheus ativa.

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: 07\TTS321]** No cadastro do aluno ou na atualização de endereço de pai, mãe, responsável financeiro e responsável acadêmico, após salvar com o campo CEP preenchido, o mesmo fica em branco na aba Endereço Principal da tela de Pessoas. Isto ocorre devido máscara do campo no Educacional conflitar com a máscara do mesmo no Gestão de Pessoas. Como solução, foi removida a formatação do campo no educacional, mantendo somente a do Gestão de Pessoas.

Arquivo: RM.Edu.Aluno.Intf.dll

### Rotina: REUNIÃO EDUCACIONAL 12.1.2

* **[Ticket: PCREQ-2241]** Adequação do código do método de pagamento na mensagem AccountReceivableDocumentDischarge na versão 2.001, para a mensageria única, de acordo com o padrão definido a integração.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## 11.83.55.196

* **[Ticket: 07\TQQORD]** Alteração no cadastro do Aluno para inclusão de novos tipos de deficiência.

Arquivos: RM.Edu.Lib.WinForms.dll, RM.Edu.Aluno.Form.dll, RM.Edu.Aluno.Intf.dll, RM.Edu.Aluno.Data.dll, RM.Edu.Aluno.Server.dll, RM.Edu.Interfaces.Intf.dll

## 11.83.55.201

* **[Ticket: Alterações Gerais]** Melhoria na mensagem de Acordo Financeiro para retorno das informações de ID de origem e destino dos lançamentos gerados, juntamente com os códigos de barra e nosso número.

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.Fin.Lan.Data.dll, RM.Edu.Integracoes.Server.dll, RM.Fin.Lan.Service.dll

* **[Ticket: 07\TTVD40]** Ajuste no método que gera RA de forma automática, para exiba o erro informando que é necessário o preenchimento do período letivo corrente na parametrização, somente se na máscara do RA existir um "&". A mensagem informativa para o usuário será "Foi configurado uma máscara para geração automática do RA que necessita do preenchimento do período letivo corrente na parametrização (Configuração | Parâmetros | Secretaria | Período Letivo).". Caso contrário não será feita nenhuma validação ao cadastrar o aluno.

Arquivo: RM.Edu.Aluno.Server.dll

* **[Ticket: 07\TU1252]** Melhoria no tratamento de valores das mensagem de baixa de lançamentos a receber, na versão 2.001, para tratamento de valores de acréscimos.

Arquivos: RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

* **[Ticket: 07\TTZDTK]** Ajuste no processo de matrícula em disciplinas(Ensino básico), evitando que seja gerada uma mensagem de erro em registros que não contém a informação do período.

Arquivo: RM.Edu.Matricula.Form.dll

## 11.83.55.202

* **[Ticket: 07\TTPJV9]** Adequação ao Censo da Educação Superior 2015

Arquivos: RM.Edu.Academico.Server.dll, RM.Edu.Academico.Form.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Lib.Intf.dll, RM.Edu.MatrizCurricular.Form.dll, RM.Edu.Academico.Data.dll

## 11.83.55.203

* **[Ticket: 07\TTZTZW]** Ajuste no retorno dos registros de Certificados/Diplomas, quando a base de dados utilizada é Oracle.

Arquivo: RM.Edu.Academico.Data.dll

## 11.83.55.204

* **[Ticket: 07\TTZ169]** Otimizado processo "Gerar contabilização" para não gravar parcelas contábeis do contrato quando não existe valor para a partida.

Arquivo: RM.Edu.Contabil.Server.dll

## 11.83.55.205

* **[Ticket: Alterações Gerais]** Melhoria na integração de acordos financeiros por mensageria única com a inclusão dos valores de acréscimo e decréscimo ao gerar uma Fatura/Liquidação pelo sistema Protheus.

Arquivos: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll, RM.Fin.Lan.Data.dll, RM.Fin.Lan.Service.dll

## 11.83.55.207

### Rotina: EDU-Pesquisa e Extensão

* **[Ticket: PCREQ-5444]** Melhoria na mensagem de Item Contábil, Department V. 1.000, para adequação a estrutura padrão de retorno de IDs, na integração por mensageria única, de forma a utilizar uma lista de internalIds.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## 11.83.55.208

* **[Ticket: 07\TTRXGT]** Remoção da crase da expressão "A Distância" do campo Tipo de Turma.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Matricula.Form.dll, RM.Edu.Integracoes.Form.dll, RM.Edu.Academico.Server.dll

* **[Ticket: 07\TUAJNG]** Ajuste efetuado na consulta SQL para trazer os dados dos estágio ao utilizar o sistema em base Oracle.

Arquivo: RM.Edu.MatrizCurricular.Server.dll

* **[Ticket: 07\TTZUL9]** Foi incluída a opção "Ensino Básico" no campo Modalidade do cadastro de autorização da filial.

Arquivos: RM.Edu.Cadastros.Form.dll, RM.Edu.Consts.dll

* **[Ticket: 07\TTZJHD]** Ajustado consulta que preenchia o campo "Selecionar novo orientador(a)"

Arquivos: App\_Web\_edutccalunowebform.ascx.1d4ca059.dll, RM.Edu.Professor.Data.dll

## 11.83.55.210

* **[Ticket: 07\TUCNDM]** Ajustes nos campos relativos a deficiências no cadastro de alunos.

Arquivos: RM.Edu.Aluno.Intf.dll, RM.Edu.Aluno.Data.dll, RM.Edu.Lib.WinForms.dll, RM.Edu.Aluno.Form.dll

## 11.83.55.212

* **[Ticket: 07\TQQORD]** Ajustes nos campos relativos a deficiências no cadastro de alunos.

Arquivo: RM.Edu.Lib.WinForms.dll

* **[Ticket: 07\TUHWK0]** Alteração na rotina do Censo para buscar disciplinas e grades sem carga horária apenas do Ensino Superior

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.213

* **[Ticket: 07\TUIEEW]** Ajuste na verificação do ano entre duas datas.O ano de 2016 é bissexto, portanto foi encontrado uma não-conformidade pelos nosos Testes Unitários nesta validação.

Arquivo: RM.Edu.Utils.Intf.dll

## 11.83.55.217

* **[Ticket: 07\TUKGRP]** Ajuste na mensagem informativa exibida quando existe choque de horários para o aluno e o parâmetro "Aluno poderá concorrer a uma vaga em caso de choque de horário" está desmarcado.

Arquivo: RM.Edu.MatrizCurricular.Server.dll

## 11.83.55.220

* **[Ticket: 07\TUNSHO]** Alteração da rotina do censo para melhorar performance

Arquivos: RM.Edu.Academico.Form.dll, RM.Edu.Academico.Server.dll

* **[Ticket: 07\TULHQR]** Ajuste na forma de carregamento dos dados da página de estágio no portal.

Arquivo: App\_Web\_eduvagasacompanhamentoalunowebform.ascx.1d4ca059.dll

## 11.83.55.221

* **[Ticket: 07\TUMCFW]** ajuste diversos nos campos de deficiências do cadastro de alunos para que fiquem coerentes com o processo do Censo.

Arquivos: RM.Edu.Aluno.Form.dll, RM.Edu.Lib.WinForms.dll

* **[Ticket: 07\TULGLR]** Ajuste na mudança de turma para que quando esteja parametrizado para aproveitar o contrato e utilize contabilização por competência por data contábil do contrato e plano de pagamento não efetue a criação de um contrato um novo contrato (onde é validado a data de competência) e sim que efetue a sua atualização e execute o processo.

Arquivos: RM.Edu.Matricula.Form.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Server.dll

* **[Ticket: 07\TUMCFW]** Ajuste diversos nos campos de deficiências do cadastro de alunos para que fiquem coerentes com o processo do Censo

Arquivos: RM.Edu.Aluno.Form.dll, RM.Edu.Lib.WinForms.dll, RM.Edu.Aluno.Server.dll, RM.Edu.Aluno.Data.dll

### Rotina: Correção de erro na execução de teste unitário de desconto condicional

* **[Ticket: EDU1210-82]** Adaptação da regra de aplicação de desconto condicional para a integração com a mensageria única de forma a aplicar descontos, somente, em pagamentos no dia limite ou antes e em um mês anterior ao vencimento ou ano anterior. As datas de pagamento posteriores não terão retorno de desconto.

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.222

* **[Ticket: 07\TUOSM6]** Melhoria na validação que habilita campos que não devem ser informados no momento do cadastro de Certificado/Diplomação, quando a tela é aberta através do anexo de Aluno ou Professor.

Arquivo: RM.Edu.Academico.Form.dll

* **[Ticket: 07\TUOVVB]** Ajustado valor máximo permitido para os parâmetros "Número de alunos que cada professor pode orientar" e "Número de alunos que podem ser supervisionados por uma mesma pessoa"

Arquivo: RM.Edu.Parametros.Form.dll

## 11.83.55.223

* **[Ticket: 07\TUQHDJ]** Ajuste no quadro de horários do Aluno para exibir o nome das disciplinas corretamente e sem repetição.

Arquivo: App\_Web\_eduquadrohorarioalunowebform.ascx.f55b27f4.dll

## 11.83.55.224

* **[Ticket: 07\TUOYRL]** Alteração no Censo Superior para sincronia com os campos de deficiência do RHU.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.227

* **[Ticket: 07\TUWAMB]** Educacenso - Censo da Educação Básica 2016

Arquivo: RM.Edu.Academico.Server.dll

* **[Ticket: 07\TULCIR]** Otimização na tela de curso/habilitação para que não haja sobreposição de campos ao salvar um registro.

Arquivo: RM.Edu.Matricula.Form.dll

## 11.83.55.228

* **[Ticket: 07\TUUDCS]** Ajuste no processo de matrícula no período letivo do aluno no ensino superior quando a matriz curricular estiver com controle de vagas por turma, para que seja verificado se o aluno já está matriculado na turma ao tentar inserir as disciplinas para o aluno.

Arquivos: RM.Edu.Matricula.Server.dll, RM.Edu.Services.Server.dll

* **[Ticket: 07\TUVSR0]** alterada consulta que busca os lançamentos vencidos do aluno para melhorar sua performance.

Arquivo: RM.Edu.Services.Server.dll

* **[Ticket: 07\TUUVER]** Ajuste na montagem das turmas do professor quando se acessa pelo coordenador para que seja exibidas todas as turmas correspondentes.

Arquivo: App\_Web\_eduturmasprofwebform.ascx.497dfae.dll

* **[Ticket: 07\TUKGLV]** Ao gerar lançamento em lote, o campo Turno deverá listar somente os turnos do curso escolhido e da coligada corrente.

Arquivo: RM.Edu.Financeiro.Form.dll

## 11.83.55.234

* **[Ticket: 07\TVANLI]** Ajuste no cadastro do professor para que ao salvar a alteração do professor não apague o pai e mãe do aluno.

Arquivos: RM.Edu.Cadastros.Server.dll, RM.Edu.Professor.Data.dll, RM.Edu.Aluno.Data.dll, RM.Edu.Aluno.Server.dll

* **[Ticket: 07\TV9254]** Melhoria na tela de aprovação de frequência no RM.exe, adicionado no filtro a etapa da turma/disciplina.

Arquivos: RM.Edu.NotaFalta.Data.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.NotaFalta.Form.dll

## 11.83.55.236

* **[Ticket: 07\TVCWDV]** Adaptação do adapter da mensagem de Plano de Conta (AccountantAccount) para interpretar a informação de empresa/filial enviado da integração para a correta validação com o De-Para.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEducacionalSigaCTB.dll

## 11.83.55.237

* **[Ticket: 07\TUZY24]** Ajuste na seleção de turmas/disciplinas para emissão de relatórios no portal do professor.

Arquivo: App\_Web\_eduturmasprofradiobuttonwebform.ascx.497dfae.dll

* **[Ticket: 07\TVCQRD]** Foi realizada otimização do processo de estorno da contabilização por competência de forma que o sistema passe a suportar o estorno de contratos que já tenham sido estornados anteriormente.

Arquivo: RM.Edu.Contabil.Server.dll

## 11.83.55.238

* **[Ticket: 07\TUZKAE]** Implementação da Legislação Nome Social nas listagens de alunos visualizadas pelo professor no Portal, exe e Mobile. Estas alterações só estarão visíveis para o usuário após execução do script ExecORA\_TUKJJU ou ExecSQL\_TUKJJU.

Arquivos: Portal Corpore.Net

* **[Ticket: 07\TVDES8]** Ajuste na montagem das turmas do professor quando se acessa pelo coordenador para que seja exibidas todas as turmas correspondentes no diário de classe.

Arquivo: App\_Web\_eduturmasprofradiobuttonwebform.ascx.497dfae.dll

* **[Ticket: 07\TVDKL6]** Ajustes para que, ao exibir a mensagem alertando sobre o choque de horário e a quantidade de choques for muito grande, o alerta seja exibido com a barra de rolagem para permitir a finalização da alteração.

Arquivos: RM.Edu.Utils.Client.dll, RM.Edu.AtvCurricular.Form.dll, RM.Edu.Professor.Form.dll, RM.Edu.PeriodoLetivo.Form.dll

* **[Ticket: 07\TVDHMW]** Ajuste na cópia de conteúdo realizado para a próxima aula para que a data efetiva também seja gravada.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## 11.83.55.239

* **[Ticket: 07\TVEKWV]** Censo da Educação Básica (Educacenso)Recursos necessários para a participação do aluno em avaliações do Inep (prova Brasil, SAEB, Outros)

Arquivos: RM.Edu.Aluno.Intf.dll, RM.Edu.Aluno.Data.dll, RM.Edu.Aluno.Server.dll, RM.Edu.Aluno.Form.dll

* **[Ticket: 07\TVEYUA]** Implementação da legislação sobre o nome social do aluno que poderá ser exibido no lugar do seu nome civil em algumas funcionalidades do Sistema.

Arquivo: RM.Edu.NotaFalta.Form.dll

## 11.83.55.240

* **[Ticket: 07\TVGKK8]** Educacenso - Censo da Educação Básica 2016

Arquivo: RM.Edu.Professor.Intf.dll

* **[Ticket: 07\TVAQV0]** Ajuste na visão da Banca do TCC(Portal do professor) para que não ocorra erro ao utilizar base de dados Oracle.

Arquivo: RM.Edu.MatrizCurricular.Data.dll

## 11.83.55.241

* **[Ticket: 07\TVGCIS]** Ajuste na consulta SQL que retorna os arquivos da visão de Estágio, disponível no portal do professor.

Arquivo: App\_Web\_eduestagioplanoatividadeprofessorwebform.ascx.497dfae.dll

* **[Ticket: 07\TVHOW7]** Ajuste no portal para que quando o parâmetro "Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, freqüência diária..." da secretaria estivesse marcado, as turmas/disciplinas em que o professor está incluído não apareçam na aprovação de frequência no portal caso ele não seja coordenador delas.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

* **[Ticket: 07\TVGXN1]** Ajuste na consulta SQL que retorna as informações do Encerramento do TCC, no portal do professor.

Arquivo: RM.Edu.MatrizCurricular.Data.dll

## 11.83.55.242

* **[Ticket: 07\TVIEE2]** Inclusão da opção de informar filiação para o docente, pois, ela é obrigatória quando está declarada na Receita Federal.

Arquivos: RM.Edu.Academico.Data.dll, RM.Edu.Academico.Form.dll

## 11.83.55.243

* **[Ticket: 07\TVFCJC]** Reformulação na digitação de frequência diária pelo Portal para permitir que as frequências sejam processadas corretamente, independente do período selecionado para a pesquisa das aulas e da quantidade de horários em cada turma/disciplina

Arquivos: Portal Corpore.Net

## 11.83.55.244

* **[Ticket: 07\TVJIGE]** Correção no processo de geração de plano de aula. Após alteração, os planos de aulas serão gerados para todas as turmas/disciplinas selecionadas. As informações sobre a geração e o motivo da não geração do plano de aula será listado no log do processo.

Arquivo: RM.Edu.PeriodoLetivo.Data.dll

## 11.83.55.245

* **[Ticket: 07\TVMDD8]** Ajuste no cadastro de necessidades educacionais especiais para que funcione corretamente na plataforma Go Global.

Arquivos: RM.Edu.Lib.WinForms.dll, RM.Edu.Aluno.Intf.dll

## 11.83.55.246

* **[Ticket: 07\TVOLX4]** Correção do botão Limpar das pesquisas lookup da tela de preparação para o Censo Escolar, para excluir o item selecionado anteriormente.

Arquivo: RM.Edu.Academico.Form.dll

* **[Ticket: 07\TVNN63]** Melhoria de performance quando o aluno vai candidatar à vaga de estágio.

Arquivos: RM.Edu.MatrizCurricular.Form.dll, RM.Edu.MatrizCurricular.Server.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.Interfaces.Intf.dll

## 11.83.55.247

* **[Ticket: 07\TVOPYV]** Alteração na visualização dos campos de recursos necessários do aluno. Quando os campos forem nulos, os checkbox deverão vir sem nenhuma marcação.

Arquivo: RM.Edu.Aluno.Form.dll

* **[Ticket: 07\TVOUID]** Correção na geração de dados do Censo para não ocorrer violação de chave primária.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.250

* **[Ticket: 07\TVMEFP]** Melhoria de performance ao selecionar o candidato a vaga de estágio.

Arquivos: RM.Edu.MatrizCurricular.Data.dll, RM.Edu.MatrizCurricular.Server.dll

## 11.83.55.251

* **[Ticket: 07\TVTJG8]** Ajuste de visibilidade dos campos de data de competência inicial e data de competência final para contrato, período letivo e parametrização por curso que passaram a verificar os parâmetros de utilização de contabilização por competência e o tipo de data contábil.

Arquivos: RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.PeriodoLetivo.Intf.dll, RM.Edu.Financeiro.Data.dll

* **[Ticket: 07\TVUKCF]** Foi realizada otimização do cadastro de serviços, de forma a impedir que um serviço que esteja sendo utilizado na parametrização de tesouraria do sistema seja excluído.

Arquivo: RM.Edu.Financeiro.Data.dll

* **[Ticket: 07\TVPVCB]** Ajuste no componente de seleção da matriz aplicada no cadastro de turma para que seja gravado a matriz curricular correta e não sempre a matriz atual.

Arquivo: RM.Edu.Lib.WinForms.dll

## 11.83.55.252

* **[Ticket: 07\TVXOZ5]** O campo Livro de Registro foi alterado para permitir a inserção de até 20 caracteres.

Arquivos: RM.Edu.Matricula.Intf.dll, RM.Edu.Matricula.Form.dll, RM.Edu.Historico.Intf.dll

* **[Ticket: 07\TVYTVF]** Otimizado menu Parcelas do contrato para permitir utilizar nome do responsável financeiro contendo o tamanho limite do banco de dados que é 100 caracteres.

Arquivo: RM.Edu.Financeiro.Intf.dll

* **[Ticket: 07\TVYCL0]** Ajuste na seleção de alunos matriculados na subturma na visão de frequência diária, trazendo apenas os alunos e horários da subturma selecionada.

Arquivo: RM.Edu.NotaFalta.Data.dll

* **[Ticket: 07\TVUK06]** Acerto na página de cursos da instituição no portal com a remoção dos campos de decretos e descrições de Cursos e Habilitações, devido a uma mudança para atender a uma legislação que mudou os campos para a Matriz Aplicada.

Arquivos: Portal Corpore.Net

## 11.83.55.253

* **[Ticket: 07\TVZKNZ]** Ajuste da consulta para que a mesma recupere as notas e as faltas de disciplinas de outras filiais em que o aluno esteja matriculado.

Arquivo: RM.Edu.NotaFalta.Server.dll

* **[Ticket: 07\TVY419]** Ajuste no formulário de Curso/Habilitação, possibilitando ser cadastrado como um anexo obrigatório do cadastro de aluno.

Arquivo: RM.Edu.Matricula.Form.dll

* **[Ticket: 07\TVZB32]** Ajuste para possibilitar a geração de certificado para cada Atividade Ofertada de uma determinada pessoa.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.254

* **[Ticket: 07\TVXCL8]** Foi realizada otimização do processo de simulação de parcelas financeiras, de forma que quando a simulação tiver como origem a integração com o Protheus.

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: 07\TVTIF5]** Ajuste na edição do plano de aula via portal do Professor, quando o acesso é realizado via navegado Firefox em uma versão igual ou superior a 44.0.2.

Arquivos: Portal Corpore.Net

## 11.83.55.255

* **[Ticket: 07\TWAW44]** Melhoria de performance na seleção de alunos disponíveis para a vaga de estágio.

Arquivo: RM.Edu.MatrizCurricular.Server.dll

## 11.83.55.256

* **[Ticket: 07\TVYAL9]** Ajuste na validação de mãe/pai na matrícula do processo seletivo terceirizado.

Arquivo: RM.Edu.ProcSel.Data.dll

### Rotina: #SalaNaoDisponivel Esta permitindo reservar sal

* **[Ticket: MEDU-668]** Ajuste no processo de efetuar reserva de instalação no portal para que seja respeitado o cadastro do tipo de sala e sala se permite ou não reserva, caso permitir, então deve se aparecer para seleção, caso contrário não deverão ser exibidos.

Arquivo: App\_Web\_edureservainstalacaowebform.ascx.497dfae.dll

### Rotina: Erro Aba Financeiro - Cadastrar Contrato Project-169664

* **[Ticket: MEDU-930]** Ao realizar uma matricula via processo seletivo (Matrícula e Avaliação -> Matrícula -> Processo Seletivo RM) realizamos uma melhoria para que o botão avançar não fique habilitadoindevidamente caso a competência contábil não esteja preenchida (isto se o sistema estiver parametrizado para utilizar a data da competência do contrato como data de contabilização).

Arquivo: RM.Edu.ProcSel.Form.dll

## 11.83.55.258

### Rotina: Erro ao executar Fórmula Visual (após Matricula no Período Letivo)

* **[Ticket: 220124 / MEDU-1249]** Ajuste na passagem dos parâmetros para que a fórmula visual atribuída na execução após a matrícula do aluno em período letivo seja executada.Além disso foi ajustado também antes da execução da matrícula do aluno em período letivo.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: Participantes Banca TCC - puxa professores do SESI no ambiente SENAI

* **[Ticket: 226696 / MEDU-1256]** Ajuste no filtro para trazer apenas o professor que foi inserido na banca do TCC no portal, quando o mesmo possuir o mesmo código porém em outra coligada.Além disso, foi feito o ajuste para que seja exibido no lookup de seleção do professor no RM apenas professores ainda não inseridos na banca.

Arquivos: RM.Edu.MatrizCurricular.Data.dll, RM.Edu.MatrizCurricular.Form.dll

## 11.83.55.259

### Rotina: Emissão de certificado.

* **[Ticket: 296467 / MEDU-1682]** Ajuste no processo de geração de diploma, em um caso específico dava problema para descobrir o próximo registro do diploma.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.261

### Rotina: Erro ao executar testes unitários

* **[Ticket: MEDU-1879]** Foi realizado ajuste na rotina e no teste unitário para que o resultado esperado da diferença entre dois anos subseqüentes seja sempre 1 e não zero

Arquivo: RM.Edu.Utils.Intf.dll

### Rotina: Permissão em Actions associadas aos Cubos Project-213623

* **[Ticket: 239912 / MEDU-1413]** Ajustes para verificar a permissão do usuário ao acessar a tela.

Arquivo: RM.Edu.Matricula.Data.dll

## 11.83.55.262

### Rotina: Project-355651 Quadro de horário Portal Project-355651

* **[Ticket: 357460 / MEDU-1979]** Ajustes para que seja exibido o código concatenado com a descrição (melhoria realizada) para prédio, bloco e sala. Além de incluir a coluna bloco na grid.

Arquivos: Portal Corpore.Net

## 11.83.55.263

### Rotina: Campo Obrigatório no cadastro de Aluno

* **[Ticket: 372326 / MEDU-2015]** Ajustes para permitir que sejam retiradas as obrigatoriedades dos campos.

Arquivo: RM.Edu.Aluno.Form.dll

## 11.83.55.264

### Rotina: Adequação do Censo Ensino Superior ao novo Layout

* **[Ticket: MEDU-2215]** Adequação de leiaute novo do Censo da Educação Superior 2016

Arquivos: RM.Edu.Academico.Form.dll, RM.Edu.Academico.Server.dll, RM.Edu.Lib.Intf.dll

### Rotina: Boleto Portal

* **[Ticket: 404468 / MEDU-2146]** Foi realizada otimização do extrato financeiro do aluno no portal de forma que somente os boletos do contexto atual do aluno sejam exibidos no portal.

Arquivos: RM.Edu.Financeiro.WebForm.dll, RM.Edu.Financeiro.Data.dll

### Rotina: Project-324647 RES: Solicitação pendente: Geração de certificado Project-324647

* **[Ticket: 324854 / MEDU-1848]** Implementação de legislação possibilitando que seja gerado mais de um certificado para o aluno na mesma habilitação filial.

Arquivos: RM.Edu.Parametros.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.Academico.Form.dll, RM.Edu.Academico.Data.dll, RM.Edu.Academico.Intf.dll, RM.Edu.Parametros.Form.dll

## 11.83.55.265

### Rotina: Project-429909 Tela consulta de matrícula em disciplina Project-429909

* **[Ticket: 434813 / MEDU-2331]** Alterado cadastro de “Matrícula na disciplina” para não habilitar o botão salvar quando editamos uma disciplina que tenha nota final lançada e não foi realizado nenhuma alteração no registro.

Arquivo: RM.Edu.Services.Server.dll

## 11.83.55.266

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 445479 / MEDU-2558]** Otimização no processo de baixa integrada ao Protheus. A alteração fopi alterar o fonte ACCOUNTRECEIVABLEDOCUMENTDISCHARGE da integração TOTVS Educacional x BackOffice Protheus com a funcionalidade de que quando realizar a baixa via Protheus e o mesmo não possui a informação do banco, é então informado o dado do banco a partir do próprio lançamento.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## 11.83.55.267

### Rotina: Disciplina equivalente não disponível para cadastro do TCC

* **[Ticket: 400534 / MEDU-2139]** Alterado o comportamento do sistema para permitir que disciplina por equivalência seja listada no anexo “Matrículas vinculadas ao TCC” do TCC do aluno. Para listar disciplinas equivalentes, o status da disciplina deverá estar “Em Curso” e na matriz curricular do aluno, a disciplina que utiliza equivalência deverá estar marcado o parâmetro “Indica se a disciplina é de TCC” (vide cadastro de “Disciplinas da Matriz Curricular”).A disciplina matriculada deverá pertencer à uma turma/disciplina.Esta alteração também afetará o processo de “Análise Curricular”, onde o item TCC também listará as disciplinas equivalentes que foram vinculadas ao TCC do aluno.Informações sobre como configurar ambiente para uso do TCC encontra-se em http://fwrm-wiki:9999/WikiHelp/EDU/EDU.tcc.aspx

Arquivos: RM.Edu.Matricula.Server.dll, RM.Edu.MatrizCurricular.Server.dll

## 11.83.55.270

### Rotina: Erro ao excluir certificado de aluno.

* **[Ticket: 551460 / MEDU-2821]** Alterado comportamento do sistema para permitir excluir Certificado que esteja vinculado à um livro de registro. Caso tenha participantes incluído neste certificado, deverá ser excluído primeiro os participantes.

Arquivo: RM.Edu.Academico.Intf.dll

### Rotina: MATRICULA EM DISCIPLINAS EDU 50 295

* **[Ticket: 577869 / MEDU-2909]** Otimizado a análise curricular do aluno, para demonstrar a nota quando o aluno foi transferido de turma.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: PORTAL PROFESSOR MENSAGENS EDU 50 495

* **[Ticket: 573799 / MEDU-2895]** Melhoria na funcionalidade de envio de mensagem no portal, possibilitando o funcionamento quando o aluno está matriculado em turma/disciplina de outra filial.

Arquivo: RM.Edu.Mensagens.Data.dll

## 11.83.55.271

### Rotina: BOLETOS EDU 50 069

* **[Ticket: 621293 / MEDU-3079]** Foi realizada otimização do processo de contabilização por competência, permitindo ao sistema, contabilizar, mediante parametrização, parcelas do tipo extra e adicional.

Arquivos: RM.Edu.Parametros.Form.dll, RM.Edu.Contabil.Server.dll, RM.Edu.Parametros.Intf.dll

### Rotina: Project-580499 Tela Sugestão de Disciplinas - opções com inconsistências Project-580499

* **[Ticket: 584563 / MEDU-2937]** Ajuste na busca de vagas na SDD, para que seja buscado o número de vagas na turma quando o controle de vagas é por turma e feito a busca na turma/disciplina quando o controle de vagas for por turma/disciplina.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Server.dll

### Rotina: Project-606171 Erro ao Matricula e Rematricular nível superior Project-606171

* **[Ticket: 622448 / MEDU-3087]** Ajuste na matrícula e rematrícula.

Arquivo: RM.Edu.Services.Server.dll

### Rotina: TURMAS DISCIPLINAS EDU 50 454

* **[Ticket: 402796 / MEDU-2151]** Ajuste na geração do plano de aula quando se considera para não gerar plano de aula para o tipo de feriado municipal, para o mesmo seja gerado de forma correta.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## 11.83.55.273

### Rotina: FREQUENCIA DIARIA EDU 50 219

* **[Ticket: 674194 / MEDU-3326]** Ajuste na montagem da frequência diária para que não ocorra queda do host.

Arquivo: RM.Edu.NotaFalta.Data.dll

### Rotina: PERFIS SEGURANCA CAMPOS FRW 00056

* **[Ticket: 643131 / MEDU-3282]** Ajuste na frequência diária para que passe a respeitar a restrição de campos da tabela SFREQUENCIA no exe.

Arquivos: RM.Edu.NotaFalta.Data.dll, RM.Edu.NotaFalta.Form.dll, RM.Edu.Interfaces.Intf.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: EDUCACIONAL01-26]** O sistema será alterado para considerar o campo complementar Licenciatura com o valor "S" ou "1". Antes considerava apenas "S", mas existe uma mensagem no sistema pedindo para que esse campo seja cadastrado como inteiro.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: Project-641560 Não aproveitamento do Contrato para transferência entre turmas Project-641560

* **[Ticket: 652154 / MEDU-3223]** Foi realizada otimização do processo de mudança de turma, de forma que o sistema consiga concluir o processo, mesmo que o sistema não seja capaz de determinar o período contábil para a nova turma com base no plano de pagamento padrão do curso.

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.274

### Rotina: Project-676468 Sistema "contabiliza a maior" (contrato 6618)determinado contrato quando executamos a rotina de contabili

* **[Ticket: 680361 / MEDU-3352]** Foi realizada otimização do processo de contabilização por competência, para que a o processo de arredondamento final considere apenas o contrato atual que está sendo processado.

Arquivo: RM.Edu.Contabil.Server.dll

### Rotina: Project-684676 Data do Contrato - Erro Project-684676

* **[Ticket: 706364 / EDUCACIONAL01-19]** Melhoria no cadastro do contrato para que não seja apresentada nenhuma não conformidade quando a data final da competência do contábil do contrato for 06/AAAA e a data do contrato 31/MM/AAAA.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: Project-692075 Erro ao salvar grau de instrução Project-692075

* **[Ticket: 692809 / EDUCACIONAL01-27]** Ajuste no cadastro do aluno para que seja feita a validação da certidão de nascimento/casamento apenas no modelo novo e não no modelo antigo como estava sendo feito.Além disso, foi ajustado a validação do modelo novo que estava considerando o campo 14º do número da certidão e não o 15º na validação do tipo de certidão.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Aluno.Data.dll

## 11.83.55.275

### Rotina: Project-680064 Permissão para gerar usuários para alunos Project-680064

* **[Ticket: 683404 / EDUCACIONAL01-46]** Otimizado processo de geração de usuário ao preencher o campo “Perfil” não será possível acessar o cadastro de perfil de usuário através deste link.

Arquivo: RM.Edu.Processos.Form.dll

### Rotina: Project-711071 Turma Gerencial Project-711071

* **[Ticket: 717640 / PORTALMOBILE01-110]** Realizado ajuste na exibição das turmas no menu "Minhas turmas" do Portal Educacional do Professor.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## 11.83.55.277

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: EDUCACIONAL01-92]** Correção na verificação de grade sem carga horária para não trazer grades de outras filiais.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.278

### Rotina: CONTRATOS CONTABILIZACAO EDU 50 141

* **[Ticket: 750396 / EDUCACIONAL01-173]** Foi realizada otimização do processo de cancelamento de contrato, permitindo ao sistema, cancelar contratos contabilizados.

Arquivo: RM.Edu.Contabil.Server.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: EDUCACIONAL01-246]** Correção no Censo para que a nacionalidade do aluno saia corretamente quando ele é alterado para estrangeiro.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: Project-742296 Lançamento de Nota da Turma Gerencial Project-742296

* **[Ticket: 744337 / EDUCACIONAL01-163]** Otimizado menu “Matricula e Avaliação | Notas de Avaliação” para permitir a digitação de notas em disciplinas de turma gerenciais. Esta opção somente será possível se marcado o parâmetro Educacional | Secretaria | “Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária, plano de aula”.

Arquivo: RM.Edu.PeriodoLetivo.Data.dll

### Rotina: Project-765846 Geração errada de planos de aulas Project-765846

* **[Ticket: 767135 / EDUCACIONAL01-289]** Ajuste na geração do plano de aula para que quando não marcar a opção de "Não gerar plano de aula para os feriados" seja gerado aula para todos os dias, independente se é feriado ou não.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## 11.83.55.279

### Rotina: INTEGRACAO FINANCEIRO

* **[Ticket: EDUCACIONAL01-636]** Adequação de parâmetros do Educacional

Arquivo: RM.Edu.Parametros.Data.dll

### Rotina: Usuario sem permissão de acesso ao Financeiro, ao acessar educacional tem acesso a todos os parametros > Integração > Fi

* **[Ticket: 733387 / EDUCACIONAL01-122]** Não deve ser permitir o acesso aos parâmetros do Financeiro dentro do módulo Educacional aos usuários que não possuem permissão no seu perfil.

Arquivo: RM.Edu.Parametros.Data.dll

## 11.83.55.280

### Rotina: Project-816582 Calendário aluno Project-816582

* **[Ticket: 819249 / PORTALMOBILE01-421]** Alunos que possuem disciplinas em filiais diferentes, serão carregadas os horários de aula no calendário independente da filial de matrícula.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.282

### Rotina: CONFIGURACAO FWB 00002

* **[Ticket: 833968 / PORTALMOBILE01-467]** Ajuste para tratamento de nomes de alunos ou professores que possuem apóstrofo em seu nome, na tela de envio de mensagens do Portal Educacional Corpore.Net.

Arquivos: App\_Web\_edumensagensfiltroprofessorwebform.ascx.cd7a3888.dll, App\_Web\_edumensagensfiltroalunowebform.ascx.cd7a3888.dll

### Rotina: Project-844003 Agendamento data para disponibilizar boleto do aluno no portal Project-844003

* **[Ticket: 847954 / PORTALMOBILE01-498]** Criação de um parâmetro para definir se um boleto pode ser impresso no portal antes de ser registrado.

Arquivos: RM.Fin.Lan.Data.dll, App\_Web\_eduboletowebform.ascx.dc12fd66.dll, RM.Fin.Lan.Intf.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Parametros.Intf.dll

### Rotina: Project-867096 Exclusão de disciplinas na matriz curricular Project-867096

* **[Ticket: 869045 / EDUCACIONAL01-885]** Ajuste na exclusão de disciplinas na matriz curricular para que não seja possível excluir uma disciplina cadastrada na matriz que já esteja ofertada em alguma turma.

Arquivo: RM.Edu.MatrizCurricular.Data.dll

## 11.83.55.284

### Rotina: ALTERAÇÃO DE DATA FINAL DE COMPETENCIA DE CONTABILIZAÇÃO DO CONTRATO

* **[Ticket: 894516 / EDUCACIONAL01-941]** Melhoria no cadastro de contrato para permitir alterar a competência contábil caso as contabilizações do contrato estejam estornadas.

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.285

### Rotina: Project-873021 Calendário aluno Project-873021

* **[Ticket: 873895 / PORTALMOBILE01-553]** Ajuste no calendário do aluno para abrir com a data atual em foco.

Arquivo: App\_Web\_educalendarioalunowebform.ascx.1d4ca059.dll

## 11.83.55.287

### Rotina: Cadastro de aluno com necessidades educacionais especiais

* **[Ticket: 967014 / EDUCACIONAL01-1188]** Sistema passou a verificar se existe um registro de origem para validação de dados anteriores de deficiência. Verificamos o registro de origem se o mesmo existir, ou seja, na inclusão de um aluno, não será verificado se a pessoa desse aluno possui dados de deficiências.

Arquivo: RM.Edu.Lib.WinForms.dll

## 11.83.55.289

### Rotina: MATRICULA EM DISCIPLINAS EDU 50 295

* **[Ticket: 1058027 / EDUCACIONAL01-1537]** Ajuste na exclusão de matrícula em disciplina do aluno, para ocorrer a exclusão corretamente.

Arquivo: RM.Edu.Matricula.Server.dll

## 11.83.55.291

### Rotina: Project-1070918 Configuração envio de arquivo pelo Portal no módulo TCC Project-1070918

* **[Ticket: 1094804 / PORTALMOBILE01-1015]** Evolução no processo de upload de TCC para respeitar o parâmetro configurado em TCC.

Arquivo: RM.Edu.Cadastros.Server.dll

## 11.83.55.292

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 1068659 / EDUCACIONAL01-1573]** Alteração no Censo para verificar se a data de início e término da turma do professor está de acordo com a data de referência do censo.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.293

### Rotina: PORTAL ALUNO HISTORICO EDU 50 355

* **[Ticket: 865476 / PORTALMOBILE01-540]** Evolução na leitura do histórico do aluno, para que os registros sejam carregados da tabela de forma consistente.

Arquivo: RM.Edu.Historico.Data.dll

### Rotina: Project-1144738 Choque de Horário Project-1144738

* **[Ticket: 1145001 / EDUCACIONAL01-1857]** Ajuste na rotina que checa choque de horário de sala, para que não mais ocorra choque de sala da turma/disciplina com ela mesma ao se alterar a data final.

Arquivo: RM.Edu.Academico.Server.dll

## 11.83.55.295

### Rotina: PORTAL ALUNO ARQUIVO POR DISCIPLINA EDU 50 343

* **[Ticket: 1185492 / PORTALMOBILE01-1240]** Ajuste na tela de Arquivos por disciplina no portal do aluno para exibir disciplinas que o aluno esteja em curso em outra filial.

Arquivos: RM.Edu.Materiais.Data.dll, RM.Edu.Materiais.WebForm.dll

### Rotina: Project-1148367 Analise Curricular - Erro Project-1148367

* **[Ticket: 1159271 / EDUCACIONAL01-1899]** Ajuste na visão de aproveitamento de estudos dentro do anexo do curso/habilitação do aluno para que seja respeitada as casas decimais parametrizada no cadastro da disciplina.Foi ajustado também no cadastro da disciplina (contexto ensino superior) e no cadastro da disciplina da matriz (contexto ensino básico) para que não seja possível cadastrar um valor maior que 4 no campo de casas decimais, pois este valor é definido na base de dados. Caso informe um valor maior que 4 o sistema ecoará a seguinte mensagem: "O número máximo de casas decimais definida na base de dados é 4.".

Arquivos: RM.Edu.Services.Server.dll, RM.Edu.MatrizCurricular.Form.dll, RM.Edu.Historico.Data.dll

### Rotina: Project-1152785 Disciplinas extras Project-1152785

* **[Ticket: 1172603 / EDUCACIONAL01-1939]** Ajuste na análise curricular para que seja exibido as disciplinas extras, ou seja, as disciplinas que não pertence a grade do aluno bem como disciplinas de outras filiais.

Arquivo: RM.Edu.Matricula.Server.dll

## 11.83.55.297

### Rotina: Project-1222548 Ocorrência aluno Project-1222548

* **[Ticket: 1225320 / EDUCACIONAL01-2075]** A pesquisa de turma/disciplina do cadastro de ocorrência foi alterada para permitir selecionar as turmas/disciplinas que o aluno está cursando em filiais diferentes da dele, mesmo com o sistema logado na filial do aluno.

Arquivos: RM.Edu.PeriodoLetivo.Intf.dll, RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.Aluno.Form.dll

## 11.83.55.302

### Rotina: Project-1332504 Data Contrato Educacional Project-1332504

* **[Ticket: 1376808 / DEDUINTEGRACOES-434]** Ajuste no cadastro de um contrato para que não seja apresentada mensagem de não conformidade na validação do período da competência contábil quando a data do contrato é igual a 31/08/2017.

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.304

### Rotina: PORTAL PROFESSOR MENSAGENS EDU 50 495

* **[Ticket: 1353616 / PORTALMOBILE01-1621]** Ajuste na seleção de alunos disponíveis para envio de mensagens via portal do professor. Somente serão listados alunos que tenham uma situação de matrícula parametrizada para "Disponível nas listagens de consulta do professor".

Arquivo: RM.Edu.Mensagens.Data.dll

## 11.83.55.306

### Rotina: Project-1390605 Visualização plano de aula aluno Project-1390605

* **[Ticket: 1391852 / PORTALMOBILE01-1758]** Alteração realizada na visualização de Planos de Aulas das disciplinas matriculadas pelo aluno.Quando o aluno de uma filial estava matriculado em disciplinas de outras filiais, os planos de aulas não eram exibidos no Portal antigo.

Arquivo: App\_Web\_educonsultaplanoaulawebform.ascx.1d4ca059.dll

## 11.83.55.311

### Rotina: CERTIFICADOS DIPLOMAS DISCIPLINAS EDU 50 119

* **[Ticket: 1577278 / EDUCACIONAL01-2994]** Ajuste na ordenação da geração de certificados e diplomas.

Arquivo: RM.Edu.Academico.Data.dll

### Rotina: CERTIFICADOS DIPLOMAS PARTICIPANTE EDU 50 120

* **[Ticket: 1580331 / EDUCACIONAL01-2996]** Ajuste na pesquisa avançada na geração de certificados e diplomas.

Arquivos: RM.Edu.Lib.WinForms.dll, RM.Edu.Academico.Data.dll

### Rotina: Project-1625212 avaliação descritiva Project-1625212

* **[Ticket: 1625299 / EDUCACIONAL01-3046]** Ao alterar o cadastro de avaliação da etapa da turma/disciplina, será realizado a validação do campo “Código da prova (Avaliação e Pesquisa)” somente se os candidatos da prova pertencerem à turma/disciplina da etapa. Não será permitido alterar o código da prova caso exista candidatos cadastrados nesta prova e que pertençam à turma/disciplina.

Arquivos: RM.Edu.Facade.dll, RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.Services.Server.dll, RM.Edu.AvaliacaoInstitucional.Server.dll

## 11.83.55.312

### Rotina: Project-1625212 avaliação descritiva Project-1625212

* **[Ticket: 1625299 / EDUCACIONAL01-3046]** Correção da seleção de provas do candidato para a avalição instrucional que estava trazendo as avaliações descritivas.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.AvaliacaoInstitucional.Form.dll, RM.Edu.Academico.Server.dll, RM.Edu.AvaliacaoInstitucional.Server.dll, RM.Edu.AvaliacaoInstitucional.Data.dll

* **[Ticket: 1625299 / EDUCACIONAL01-3046]** No processo “Avaliação descritiva” foi implementado opção para excluir o candidato da prova já cadastrada anteriormente. Ao escolher esta opção, o candidato será excluído tanto no Educacional (avaliação descritiva) quanto no Avaliação e Pesquisa (cadastro de candidato da prova)

Arquivos: RM.Edu.AvaliacaoInstitucional.Server.dll, RM.Edu.Academico.Server.dll, RM.Edu.AvaliacaoInstitucional.Form.dll, RM.Edu.AvaliacaoInstitucional.Data.dll, RM.Edu.Interfaces.Intf.dll

* **[Ticket: 1625299 / EDUCACIONAL01-3046]** Ao alterar o cadastro de avaliação da etapa da turma/disciplina, será realizado a validação do campo “Código da prova (Avaliação e Pesquisa)” e caso o candidato já tenha executado esta prova, não será permitido alterar o código da avaliação.

Arquivos: RM.Edu.Facade.dll, RM.Edu.Services.Server.dll, RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.AvaliacaoInstitucional.Server.dll

## 11.83.55.313

### Rotina: PORTAL ALUNO NOTAS DE AVALIACAO EDU 50 360

* **[Ticket: 1664288 / PORTALMOBILE01-2477]** Ajuste na tela de notas de avaliação no portal do aluno para o perfeito funcionamento em base oracle tanto no contexto de ensino básico quanto superior.

Arquivo: RM.Edu.NotaFalta.Data.dll

## 11.83.55.314

### Rotina: Project-1678646 PORTAL DO DOCENTE >> Nota de Provas gravando NULL Project-1678646

* **[Ticket: 1685023 / PORTALMOBILE01-2495]** Ajustes na digitação de notas de avaliações evitando que seja salvo na base registros com nota vazia.

Arquivo: App\_Web\_edudigitacaoprovaswebform.ascx.497dfae.dll

## 11.83.55.315

### Rotina: PORTAL PROFESSOR EMITIR RELATORIOS EDU 50 481

* **[Ticket: 1387986 / PORTALMOBILE01-2244]** Alterado a propriedade CheckListType do componente RMSCheckedListBox, possibilitando que o componente trabalhe de forma coerente. Ao selecionar um item da lista, ele seja realmente marcado, sem afetar as outras opções marcadas ou desmarcadas.

Arquivo: RM.Edu.Parametros.Form.dll

## 11.83.55.316

### Rotina: ALTERAR SITUACAO DE MATRICULA CURSO EDU 50 010

* **[Ticket: 1887526 / EDUCACIONAL01-3563]** Melhoria no sistema para permitir a exclusão de matrículas que atendam ao público alvo de uma vaga.

Arquivos: RM.Edu.MatrizCurricular.Data.dll, RM.Edu.dll, RM.Edu.MatrizCurricular.Form.dll

## 11.83.55.319

### Rotina: PORTAL PROFESSOR DISPONIBILIDADE DE HORARIOS EDU 50 375

* **[Ticket: 2043055 / PORTALMOBILE01-3170]** Ajuste no webservice para que seja exibido uma mensagem de erro ao tentar incluir turno com hora inválida.

Arquivo: RM.Edu.Academico.Data.dll

## 11.83.55.320

### Rotina: Portal Educacional - alteração dados pessoais

* **[Ticket: 2059518 / PORTALMOBILE01-3217]** Ajuste para tratar corretamente a máscara do cep e telefone

Arquivo: App\_Web\_edualunowebform.ascx.1d4ca059.dll

## 11.83.55.321

### Rotina: TRANSFERENCIA INTERNA EDU 50 451

* **[Ticket: 2183919 / EDUCACIONAL01-3966]** Ajuste na transferência interna para que ao transferir alunos com disciplina em curso e o mesmo possuir código da turma preenchido no período letivo de origem ocorra a transferência de forma correta.

Arquivo: RM.Edu.Matricula.Server.dll

## 11.83.55.322

### Rotina: ANÁLISE CURRICULAR (EDU.50.016)

* **[Ticket: 2555898 / EDUCACIONAL01-4487]** Ajuste no campo "Ano/Semestre" na tela de disciplina de origem no aproveitamento de estudo, para que suporte no máximo 10 caracteres

Arquivos: RM.Edu.Historico.Form.dll, RM.Edu.Historico.Intf.dll

### Rotina: BOLETOS (EDU.50.069)

* **[Ticket: 2228098 / DEDUINTEGRACOES-1765]** Foi alterado o anexo da visão de boleto para carregar a action FinLanBoletoAction por causa da chave só existir apenas FLANBOLETO para boletos cancelados

Arquivo: RM.Edu.Financeiro.Form.dll

* **[Ticket: 2228098 / DEDUINTEGRACOES-1765]** Alteração da leitura (ReadRecord) para a tela de boleto para que o vinculo entre o boleto e o lançamento seja feito pela tabela FLANBOLETO por causa de boletos cancelados que não contem o numero do lançamento na tabela de FBOLETO.

Arquivos: RM.Edu.Facade.dll, RM.Edu.Interfaces.Intf.dll

* **[Ticket: 2228098 / DEDUINTEGRACOES-1765]** Foi corrigido a consulta de boletos do educacional para que boletos cancelados sejam retornados.

Arquivo: RM.Edu.Facade.dll

### Rotina: Project-2301715 Parametrização por curso - copiar modelo de etapa para outro período letivo Project-2301715

* **[Ticket: 2305802 / EDUCACIONAL01-4120]** Ajuste no processo de cópia de modelo de etapa para outro período letivo para que copie as datas de início e término das etapas do período letivo de origem para o de destino, considerando o tipo da etapa (falta e/ou nota).

Arquivo: RM.Edu.Services.Server.dll

## 11.83.55.323

### Rotina: Portal Educacional - alteração dados pessoais

* **[Ticket: 2059518 / PORTALMOBILE01-3567]** Alteração dos campos de telefone e CEP para respeitarem corretamente a máscara.

Arquivos: Portal Corpore.Net

## 11.83.55.324

### Rotina: FREQUÊNCIA DIÁRIA (EDU.50.219)

* **[Ticket: 2610550 / EDUCACIONAL01-4595]** Nas telas de digitação de falta por dia e digitação de frequência diária não era validada se a data da falta era futura.

Arquivo: RM.Edu.NotaFalta.Data.dll

* **[Ticket: 2610550 / EDUCACIONAL01-4595]** Foi ajustado nas telas de digitação de falta por dia e digitação de frequência diária para que não seja possível digitar faltas em datas futuras, ou seja, que sejam maiores que o dia de hoje.

Arquivo: RM.Edu.NotaFalta.Data.dll

## 11.83.55.325

### Rotina: PORTAL - PROFESSOR - AVALIAÇÕES (EDU.50.371)

* **[Ticket: 2606787 / EDUCACIONAL01-4653]** Ajuste no processo de avaliação descritiva para que seja possível criar avaliações descritivas por etapa independente se é a mesma prova do módulo de Avaliação e Pesquisa.

Arquivos: RM.Edu.AvaliacaoInstitucional.Form.dll, RM.Edu.AvaliacaoInstitucional.Intf.dll, RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.AvaliacaoInstitucional.Data.dll, RM.Edu.AvaliacaoInstitucional.Server.dll

* **[Ticket: 2606787 / EDUCACIONAL01-4653]** Remoção de método não utilizado

Arquivo: RM.Edu.AvaliacaoInstitucional.Server.dll

## 11.83.55.326

### Rotina: HISTÓRICO - ALUNO (EDU.50.250)

* **[Ticket: 2783393 / EDUCACIONAL01-4860]** Acerto na geração de histórico quando o aluno já possui um gerado em outra filial em um ano anterior.

Arquivo: RM.Edu.Historico.Server.dll

## 11.83.55.327

### Rotina: MATRICULAR ALUNO (EDU.50.300)

* **[Ticket: 2815490 / EDUCACIONAL01-4906]** Otimização na chamada do processo de matricula em disciplinas.

Arquivos: RM.Edu.Classes.Server.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.Matricula.Form.dll, RM.Edu.Matricula.Data.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Utils.Server.dll, RM.Edu.Lib.WinForms.dll

## 11.83.55.328

### Rotina: AVALIAÇÃO INSTITUCIONAL (EDU.50.064)

* **[Ticket: 2942105 / EDUCACIONAL01-5115]** Na Avaliação Descritiva, para melhor entendimento, foi alterado o grid de exclusão de candidatos para demonstrar o código do professor.

Arquivos: RM.Edu.AvaliacaoInstitucional.Intf.dll, RM.Edu.AvaliacaoInstitucional.Form.dll, RM.Edu.AvaliacaoInstitucional.Server.dll

* **[Ticket: 2942105 / EDUCACIONAL01-5115]** Na Avaliação Descritiva, para melhor identificação das informações, foram incluídas colunas demonstrando a Etapa e a Prova do respectivo registro.

Arquivos: RM.Edu.AvaliacaoInstitucional.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.AvaliacaoInstitucional.Data.dll, RM.Edu.AvaliacaoInstitucional.Server.dll, RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.AvaliacaoInstitucional.Form.dll

* **[Ticket: 2942105 / EDUCACIONAL01-5115]** Ajuste no filtro em Oracle

Arquivo: RM.Edu.AvaliacaoInstitucional.Form.dll

## 11.83.55.330

### Rotina: ATENDIMENTO ESPECÍFICO - CUSTOMIZAÇÃO

* **[Ticket: 3007603 / EDUCACIONAL01-5249]** Ajuste no processo de mudança de turma para que seja gravado histórico da matrícula do período letivo do aluno de forma correta quando o mesmo sai da turma A (manhã) para B (tarde) e volta de B (tarde) para A (manhã).

Arquivos: RM.Edu.Matricula.Server.dll, RM.Edu.Services.Server.dll, RM.Edu.Lib.Intf.dll

## 11.83.55.331

### Rotina: DIGITAÇÃO POR ALUNO - NOTAS DE AVALIAÇÕES (EDU.50.176)

* **[Ticket: 3141979 / EDUCACIONAL01-5407]** Acerto na definição de cores ao editar uma nota no lançamento de notas de prova.

Arquivos: RM.Edu.NotaFalta.Form.dll, RM.Edu.Interfaces.Intf.dll

## 11.83.55.332

### Rotina: AVALIAÇÃO INSTITUCIONAL (EDU.50.064)

* **[Ticket: 3233799 / EDUCACIONAL01-5562]** Otimização no cadastro de Avaliação da Turma/Disciplina, para melhor entendimento foi acrescentado na mensagem de validação da avaliação descritiva o código da pessoa.Por exemplo:Não será possível alterar o “Código da prova do Avaliação e Pesquisa”, pois existe(m) candidatos que executaram esta prova (vide Histórico da prova).Código de Pessoas que executaram a Prova no Testis (tabela BHISTORICO): 3021;3022

Arquivos: RM.Edu.Facade.dll, RM.Edu.Services.Server.dll, RM.Edu.PeriodoLetivo.Intf.dll, RM.Edu.PeriodoLetivo.Data.dll

## 11.83.55.333

### Rotina: PARAMETRIZAÇÕES POR CURSO (EDU.50.329)

* **[Ticket: 3251025 / EDUCACIONAL01-5611]** Acerto na validação entre as datas de colação de grau e emissão do diploma e a conclusão de curso e a emissão do diploma. Quando havia validação desses campos, o sistema estava considerando a parte horária da data.

Arquivo: RM.Edu.Matricula.Data.dll

## 11.83.55.334

### Rotina: CANCELAR CONTRATO (EDU.50.115)

* **[Ticket: 3294700 / DEDUINTEGRACOES-2754]** Otimização do processo de cancelamento de contratos para que durante o cancelamento de um contrato o responsável financeiro do contrato não seja excluído.

Arquivo: RM.Edu.Financeiro.Server.dll

## 11.83.55.335

### Rotina: DADOS DO CURSO PARA O CENSO ESCOLAR (EDU.50.172)

* **[Ticket: 3247247 / EDUCACIONAL01-5615]** Alteração no processo de preparação de dados para o Educacenso com a correção dos códigos dos cursos que são classificados como profissionalizantes.

Arquivo: RM.Edu.Academico.Form.dll

### Rotina: NOTAS DE AVALIAÇÕES (EDU.50.317)

* **[Ticket: 3503060 / EDUCACIONAL01-5982]** Foi retirado o texto "label9" da tela, pois ele não serve para nada e não deveria existir.

Arquivo: RM.Edu.NotaFalta.Form.dll

## 11.83.55.336

### Rotina: PROCESSO SELETIVO TERCEIRIZADO (EDU.50.394)

* **[Ticket: 2839233 / EDUCACIONAL01-5800]** Inclusão dos campos: Tipo de rua, Tipo de bairro, Cor/Raça, Grau/Escolaridade, País e Data de emissão da identidade no layout do arquivo do processo de seleção terceirizado.

Arquivos: RM.Edu.Utils.Server.dll, RM.Edu.ProcSel.Form.dll, RM.Edu.ProcSel.Intf.dll, RM.Edu.ProcSel.Data.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Consts.dll

## 11.83.55.337

### Rotina: APURAÇÃO DE RESULTADOS (EDU.50.021)

* **[Ticket: 3825549 / EDUCACIONAL01-6389]** A função de fórmula “BuscaCampoCursoAluno” foi alterada para retornar o nível de ensino do curso e não do aluno.

Arquivo: RM.Edu.Formula.dll

## 11.83.55.338

### Rotina: AVALIAÇÃO INSTITUCIONAL (EDU.50.064)

* **[Ticket: 4029849 / EDUCACIONAL01-6657]** Alteração na avaliação descritiva para aceitar registros que possuam a descrição da prova com tamanho maior que 60 caracteres e não aparecer a mensagem de erro: "Failed to enable constraints. One or more rows contain values violating non-null, unique, or foreign-key constraints."

Arquivo: RM.Edu.AvaliacaoInstitucional.Intf.dll

### Rotina: PORTAL - ALUNO - MATRÍCULA ONLINE (EDU.50.356)

* **[Ticket: 4025964 / PORTALMOBILE01-5884]** Ajuste na assinatura do contrato e comprovante de matrícula, filtrando a filial da assinatura.

Arquivos: RM.Edu.Matricula.Data.dll, RM.Edu.Interfaces.Intf.dll, App\_Web\_edumatriculaonlinecomprovantematricula.aspx.f55b27f4.dll

# TOTVS Folha de Pagamento

## 11.83.55.100

* **[Ticket: 07\TRA163]** Ajustado na geração do histórico de provisões para não retornar o erro de data.

Arquivo: RM.Fop.Calc.CalculosBase.dll

* **[Ticket: 07\TQZ447]** Tratado no lançamento do Grupo de Eventos para permitir o recálculo do envelope de funcionários demitidos no mês, quando ocorre lançamento de novos eventos.

Arquivo: RM.Fop.Calc.Calculos.dll

* **[Ticket: 07\TQUQVK]** Tratado na diferença de 13o. Salário para não somar valores do tipo desconto ou base de cálculo no CC 66.

Arquivo: RM.Fop.Calc.Calculos.dll

* **[Ticket: 07\TQZZ12]** Ajuste na Liberação da Competência para não consistir quando existem funcionários com férias coletivas terminando no mês, acrescentada de licença remunerada, terminando no mês seguinte.

Arquivo: RM.Fop.Data.Server.dll

## 11.83.55.105

* **[Ticket: 07\TQZP50]** Ao fazer o lançamento de um evento programado utilizando o gerenciador de movimento, o sistema não obedecia o Centro de Custo do Evento Programado.

Arquivo: RM.Fop.CalcularFolha.Data.dll

## 11.83.55.106

* **[Ticket: 07\TQZNQD]** Ao aprovar férias de funcionário pelo portal, o sistema estava validando a consideração de dias úteis com base do parâmetro do gestor, e não do funcionário em questão.

Arquivo: RM.Fop.FuFerias.Data.dll

## 11.83.55.108

* **[Ticket: 07\TRDLGG]** Otimizada a mensagem de aviso durante a geração de lançamentos contábeis.

Arquivo: RM.Fop.Rotinas.Form.dll

* **[Ticket: 07\TQVRA5]** Otimizado geração da DIRF.

Arquivos: Portal Corpore.Net

## 11.83.55.111

* **[Ticket: 07\TRFLM0]** Otimizado geração da DIRF em Arquivo quando utiliza a opção TODOS.

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

## 11.83.55.114

* **[Ticket: 07\TQRFRS]** Altera comportamento dos novos parâmetros nas provisões calculadas no segundo mês das férias partidas.

Arquivos: RM.Fop.Calc.Calculos.dll, RM.Fop.Calc.CalculosBase.dll

* **[Ticket: 07\TRHOBP]** Otimizado geração da DIRF.

Arquivos: RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Intf.dll

## 11.83.55.115

* **[Ticket: 07\TRHZEN]** Sistema passa a considerar apenas números dos dados digitados no Registro ANS.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TRHTHE]** Não permitir o cálculo da contribuição sindical em janeiro, mesmo que tenha sido lançado manualmente pelo usuário.

Arquivo: RM.Fop.Calc.Calculos.dll

* **[Ticket: 07\TRGICG]** Foi adicionada a coluna "Descrição da Função" nos campos de seleção de funcionário quando o parâmetro apropriado estiver marcado no parametrizador

Arquivo: RM.Fop.Funcionario.Server.dll

* **[Ticket: 07\TRFNR6]** Ajuste na Provisão de Férias da competência dezembro, para funcionários admitidos no mês e que tenham eventos no envelope que incidem em média de férias.

Arquivo: RM.Fop.Calc.Calculos.dll

* **[Ticket: 07\TRGKAU]** Não calcular diferença do evento de CC 145, quando o aumento salarial é no mês seguinte á demissão, durante a projeção do aviso prévio indenizado.

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

## 11.83.55.116

* **[Ticket: 07\TRIHF5]** Ajuste no processo de cancelamento global de férias, que não estava realizando os cancelamentos.

Arquivo: RM.Fop.FuFerias.Data.dll

* **[Ticket: 07\TRMAAK]** Na parametrização da DIRF o sistema passa a incluir a máscara de CNPJ automaticamente ao atualizar os eventos da operadora de saúde, a fim de manter compatibilidade entre os eventos e as operadoras de saúde relacionadas.

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TRMLHL]** Alteração na nomenclatura da faixa "rendimentos acima de R$6.000,00 ou assalariado com rendimentos acima de R$25.661,70".

Arquivo: RM.Fop.Relatorios.Intf.dll

## 11.83.55.117

* **[Ticket: 07\TRMBRM]** Ajuste no CC 329, quando o parâmetro "Soma avos ref. aviso após o cálculo" está confirmado, e houve antecipação de férias.

Arquivo: RM.Fop.Calc.CalculosBase.dll

* **[Ticket: 07\TRGZV8]** Otimizado a exibição do remetente do envio de e-mail para funcionário.

Arquivo: RM.Fop.Facade.dll

## 11.83.55.118

* **[Ticket: 07\TREP82]** Implementação da nova regra de afastamento por motivo de doença ou acidente de trabalho, conforme publicado na MP 664, que à partir de 1º/03/2015, as empresas serão responsáveis pelo salário do empregado nos primeiros 30 dias de afastamento.

Arquivo: RM.Fop.Calc.CalculosBase.dll

## 11.83.55.120

* **[Ticket: 07\TRHNO6]** Implementação da nova regra de afastamento por motivo de doença ou acidente de trabalho, conforme publicado na MP 664, que à partir de 1º/03/2015, as empresas serão responsáveis pelo salário do empregado nos primeiros 30 dias de afastamento.

Arquivo: RM.Fop.Calc.CalculosBase.dll

## 11.83.55.122

* **[Ticket: 07\TREVOM]** Ajuste na rescisão complementar para não calcular diferença de 1a. parcela de 13o. (CC 9), mesmo que esteja com data de pagamento posterior à demissão.

Arquivos: RM.Fop.Calc.Formulas.dll, RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

* **[Ticket: 07\TRPLNZ]** Ajuste na consistência de mês caixa no cadastro de movimento de pensão, para permitir realizar alteração no movimento de férias, com caixa no mês anterior ao mês competência.

Arquivo: RM.Fop.Funcionario.Data.dll

## 11.83.55.123

* **[Ticket: 07\TRPWD1]** \* Ao gerar arquivo, caracteres especiais não são mais retirados do nome da empresa e chapa do funcionário\* Ajuste no preenchimento automático de quebra de seção

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Dominio.dll

* **[Ticket: 07\TRPAX1]** Otimizado preenchimento do informe de rendimentos referente a movimentação de pensão.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Paramquiosque.Data.dll, RM.Fop.Informe.Data.dll

* **[Ticket: 07\TRQALH]** Ajuste para realização da média do salário contratual para funcionários tipo O – Comissionistas que passou a filtrar a partir da data de transferencia (para tipo de admissão "E" ou "T"), caso contrário, a partir da data de admissão

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 07\TRPVFM]** Otimizado o uso do campo que informa o caminho do arquivo salvo dentro do assistente de geração da RAIS.

Arquivos: RM.Fop.Dominio.dll, RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TRPWGN]** Otimizada tela da RAIS, de forma que o botão “Executar novamente” não fique subscrito na tela.

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TRQSFR]** Otimizada tela da RAIS, validações no campo telefone.

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TRPVV1]** Melhoria no tratamento do campo "Tipo de Admissão" para considerar registro que estão gravados com o código em letra minúscula.

Arquivo: RM.Fop.Infraestrutura.Repositorios.dll

## 11.83.55.126

* **[Ticket: 07\TRRLBY]** Otimizado cálculo do décimo terceiro quando tem base negativa em um caixa no informe de rendimentos.

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Intf.dll

* **[Ticket: 07\TRRU42]** Tratamento no Cadastro de Funcionários, para gerar o registro de estabilidade somente após 30 dias de atestado, para afastamentos após 01/03/2015, devido a MP 664.

Arquivo: RM.Fop.Lib.Server.dll

## 11.83.55.127

* **[Ticket: 07\TRMAAY]** Parametro para visualização de Função na Visão de Funcionário agora também exibe a descrição da função no lookup de funcionários.

Arquivo: RM.Fop.Funcionario.Server.dll

## 11.83.55.128

* **[Ticket: 07\TRQYEH]** Otimizada a visualização do envelope de pagamento de subordinados através do Portal.

Arquivo: RM.Fop.Envelope.Data.dll

## 11.83.55.129

* **[Ticket: 07\TRSOMA]** Ajuste na diferença de férias, quando é considerado somente dias úteis, e o aumento salarial ocorre no segundo mês das férias partidas.

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Data.Server.dll, RM.Fop.Dominio.dll, RM.Fop.Sefip.Data.dll

* **[Ticket: 07\TRUG70]** Reestruturação em exclusão de dependentes.

Arquivo: RM.Fop.Funcionario.Data.dll

## 11.83.55.130

* **[Ticket: 07\TRPTWQ]** Não bloquear alteração no movimento de pensão, com caixa no mês anterior ao mês competência.

Arquivo: RM.Fop.Funcionario.Data.dll

## 11.83.55.131

* **[Ticket: 07\TRTYOS]** Ajuste na informação de nacionalidade no arquivo. Realizado "De/Para" para que o relatório imprima o código correto para nacionalidade

Arquivo: RM.Fop.Dominio.dll

## 11.83.55.132

* **[Ticket: 07\TRRLY0]** Ajuste na geração da RAIS para tratar os casos de demissão com projeção dos dias de aviso prévio indenizado no campo “Data de Desligamento”.

Arquivos: RM.Fop.Dominio.dll, RM.Fop.Calc.Interfaces.dll, RM.Fop.Relatorios.Form.dll

## 11.83.55.134

* **[Ticket: 07\TRSTKC]** Ajuste na RAIS, quando o funcionário foi transferido e recebeu diferença por dissídio antes da transferência, o sistema não estava levando a informação correta para o campo "Mês de pagamento do 13º Salário Final".

Arquivo: RM.Fop.Dominio.dll

## 11.83.55.136

* **[Ticket: 07\TRVPXH]** Otimizada processo de eleger presidente da CIPA.

Arquivo: RM.Fop.Funcionario.Server.dll

## 11.83.55.137

* **[Ticket: 07\TRNUU3]** Ajuste na listagem de colunas de tabelas para importaçãoAjuste em mensagem de erro para colunas obrigatórias para importação

Arquivo: RM.Fop.Importacao.Data.dll

## 11.83.55.138

* **[Ticket: 07\TRXKCL]** Otimizada a gravação do endereço do funcionário através de alteração no Portal.

Arquivo: RM.Fop.Funcionario.Data.dll

## 11.83.55.140

* **[Ticket: 07\TRYFXT]** Otimizado o processo de aprovação de alterações cadastrais.

Arquivo: RM.Fop.Rotinas.Data.dll

## 11.83.55.141

* **[Ticket: 07\TRZW42]** Otimizado cadastro de sindicatos, homolognet, TRCT e GRCSU com inclusão de uma nova opção de tipo de entidade sindical e novo formato do código da entidade sindical

Arquivos: RM.Fop.Processos.Data.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Sindicato.Form.dll, RM.Fop.Relatorios.Form.dll

## 11.83.55.143

* **[Ticket: 07\TSB642]** Ajuste na geração do MANAD, quando o evento está vinculado ao código de cálculo 46 - "Autônomos", o sistema não estava preparado para gerar o arquivo caso o usuário parametrizasse este evento como "Desconto". Fazendo com que o arquivo não validasse no programa SVA.

Arquivo: RM.Fop.Manad.Data.dll

## 11.83.55.146

* **[Ticket: 07\TRXJB5]** Ajuste em campos Hora (valor Hora) e Jornada Mensal para restrição de visualização de campo em perfilO campo Hora (valor Hora) passa a herdar restrição do campo Salário

Arquivo: RM.Fop.Funcionario.Form.dll

* **[Ticket: 07\TRZXJF]** Otimizado processo Geração de Encargos ao utilizar encargos por fórmula e fgts.

Arquivos: RM.Fop.Calc.Integracao.dll, RM.Fop.Calc.Calculos.dll

## 11.83.55.150

* **[Ticket: 07\TSDKBH]** - Nova legislação referente ao código da entidade sindical

Arquivo: RM.Fop.Sindicato.Form.dll

## 11.83.55.151

* **[Ticket: 07\TSGWND]** No envio de relatório por email para o funcionário, foi adicionada uma opção para que o relatório seja enviado como HTML no corpo do email.

Arquivos: RM.Prj.Planilhas.Data.dll, RM.Fop.Lib.Data.dll, RM.Fop.Lib.WinForms.dll, RM.Fop.Lib.Intf.dll, RM.Prj.PedidoMaterial.Server.dll, RM.Prj.Planilhas.Form.dll

## 11.83.55.152

* **[Ticket: 07\TSIEHG]** Quando integrado com o vitae/SSO ao demitir um funcionário que não tenha realizado exame demissional é emitida a mensagem de aviso "Chapa {0}: Este funcionário tem exame médico demissional pendente" permitindo que a rescisão seja gravada e calculada. O sistema irã incluir automaticamente os exames do tipo demissional.

Arquivos: RM.Fop.Rescisao.Form.dll, RM.Fop.Rescisao.Intf.dll, RM.Fop.Facade.dll, RM.Fop.Rescisao.Data.dll

## 11.83.55.154

* **[Ticket: 07\TSFNGT]** Na liberação de competência foi criado o parâmetro "Atualiza Uso de Vale Transporte" que quando marcado irá atualizar o campo PFUNC.USAVALETRANSP para 1 se na nova competência alguma linha de transporte tenha vigência no primeiro ou último dia da nova competência. O funcionário em que a nova competência não tenha vigências nas linhas de transporte a ele associada ou sem linhas associadas o campo PFUNC.USAVALETRANSP será 0.

Arquivos: RM.Fop.Rotinas.Data.dll, RM.Fop.Data.Server.dll, RM.Fop.Rotinas.Form.dll, RM.Fop.Data.Intf.dll, RM.Fop.Rotinas.Intf.dll

* **[Ticket: 07\TSGISN]** Ajuste na geração do MANAD, quando se tratar de um evento que não tem incidência de INSS e de IRRF, e também sem código de cálculo, a rotina irá exportar este evento no registro K300 com o campo IND\_RUBR preenchido com a informação ‘O’ – Outros.

Arquivo: RM.Fop.Manad.Data.dll

* **[Ticket: 07\TSFMJ6]** Sistema não gerava seguro desemprego para demitidos tipo TIncluído parâmetro em tela para considerar demitidos tipo T em arquivo seguro desemprego.

Arquivos: RM.Fop.Lib.Intf.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Server.dll, RM.Fop.Calc.Interfaces.dll

## 11.83.55.155

* **[Ticket: 07\TSDHYR]** Criação de novo parâmetro na função CALCMEDJOR, para permitir a comparação dos valores de média, considerando as 3 colunas de nro. meses parametrizadas no Sindicato.

Arquivos: RM.Fop.Calc.Formulas.dll, RM.Fop.Calc.CalculosBase.dll

## 11.83.55.157

* **[Ticket: 07\TSN899]** Otimizado log na aprovação de férias do RM Portal.

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.FuFerias.Data.dll

## 11.83.55.158

* **[Ticket: 07\TSJFW9]** Corrigido problema na alteração de endereço via Portal

Arquivos: RM.Fop.Funcionario.Data.dll, RM.Fop.Rotinas.Data.dll

## 11.83.55.160

* **[Ticket: 07\TSOCY9]** Criação de parâmetro para definir o final do periodo em que o auxílio doença de responsabilidade da Empresa teve duração de 30 dias (MP 664).

Arquivos: RM.Fop.Parametros.Intf.dll, RM.Fop.Lib.Server.dll, RM.Fop.Parametros.Form.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Sefip.Data.dll, RM.Fop.Calc.CalculosBase.dll, RM.Fop.Dominio.dll, RM.Fop.Data.Server.dll

## 11.83.55.166

### Rotina: eSocial

* **[Ticket: PCREQ-3579]** Adequação minuta 2.0 esocial 4ª Entrega

Arquivos: RM.Fop.Cadastros.Intf.dll, RM.Fop.Funcionario.Server.dll, RM.Fop.Funcionario.Intf.dll, RM.Fop.Importacao.Data.dll, RM.Fop.Cadastros.Form.dll, RM.Fop.Lib.Extensions.dll, RM.Fop.Funcionario.Form.dll, RM.Fop.Cadastros.Data.dll, RM.Fop.Funcionario.Data.dll

## 11.83.55.167

### Rotina: eSocial

* **[Ticket: PCREQ-3579]** Adequação minuta 2.0 esocial 4ª Entrega

Arquivo: RM.Fop.Funcionario.Intf.dll

## 11.83.55.168

* **[Ticket: 07\TSMMQH]** Implementado a geração do SEFIP com tomadores sem valor de renteção.

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Sefip.Intf.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Sefip.Form.dll, RM.Fop.Calc.Interfaces.dll, RM.Fop.Lib.Extensions.dll, RM.Fop.Utils.Server.dll, RM.Fop.Calc.CalculosBase.dll

* **[Ticket: 07\TSTVOT]** Alteração de situação do funcionário para "Contrato de Trabalho Suspenso" deve gerar histórico de afastamento corretamente.

Arquivo: RM.Fop.Funcionario.Server.dll

## 11.83.55.169

* **[Ticket: 07\TSRZWT]** Verificamos que a inconsistência na duplicidade de registros no arquivo deve-se ao fato existir mais de uma ocorrência do mesmo município (tabela GMUNICIPIO) para o mesmo Estado.Foi realizado ajuste na consulta SQL para evitar problema de duplicidade de registros quando existirem dois municípios cadastrados com o mesmo nome e para o mesmo Estado. Ex: Rio de Janeiro

Arquivos: RM.Fop.Calc.Interfaces.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Intf.dll

* **[Ticket: 07\TSQX78]** Atualização da Barra de progresso para funcionários que não possuem registros para processamento ou que estão fora do período informado nos parâmetros de tela.Inclusão de log de processamento de funcionários

Arquivo: RM.Fop.Manad.Data.dll

## 11.83.55.170

* **[Ticket: 07\TSYWM6]** Ajuste na rescisão coletiva para gravar os dados do aviso prévio misto no cadastro do funcionário.

Arquivos: RM.Fop.Calc.Interfaces.dll, RM.Fop.Calc.CalculosBase.dll, RM.Fop.Rescisao.Form.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Rescisao.Intf.dll, RM.Fop.Rescisao.Data.dll

## 11.83.55.172

* **[Ticket: 07\TTAXOL]** Ajuste no cálculo das médias na geração do histórico de provisões, quando o funcionário está afastado pelo tipo C - "Contrato de Trabalho Suspenso", sem data de retorno.

Arquivo: RM.Fop.Calc.CalculosBase.dll

## 11.83.55.174

* **[Ticket: 07\TTCHLV]** Correção no processo de Rescisão Coletiva relacionado à erro de Aviso Prévio Misto

Arquivo: RM.Fop.Calc.Calculos.dll

* **[Ticket: 07\TSFRBX]** Foi ajustado serviço utilizado para envio de e-mail anônimo ao aprovar sugestão de férias no Portal.

Arquivo: RM.Fop.FuFerias.Data.dll

## 11.83.55.176

* **[Ticket: 07\TSYANK]** Realizado o tratamento para o tamanho dos campos de Informações na geração da GPS..

Arquivo: RM.Fop.Relatorios.Data.dll

## 11.83.55.178

* **[Ticket: 07\TTCWX5]** No  comparativo SEFIP x FA foi otimizado o tratamento quanto a obtenção dos campos vindo do Layout da Folha Analítica, quando este arquivo encontra-se corrompido, por não ter todas as informações necessárias no registro 30 a ser importado no comparador.

Arquivo: RM.Fop.Relatorios.Data.dll

## 11.83.55.180

* **[Ticket: 07\TTFOMQ]** Funcionário possui dois eventos de horas extra, utilizando a mesma rubrica, ao gerar arquivo Homolognet para o mesmo o sistema não está considerando apenas um evento de hora extra

Arquivo: RM.Fop.Processos.Data.dll

## 11.83.55.190

* **[Ticket: 07\TTBJX1]** O sistema passa a validar os caminhos para o comparativo SEFIP x Folha Analítica e SEFIP x SEFIP somente se for informado algum dado. Caso o campo fique em branco não será validado no momento da digitação.

Arquivo: RM.Fop.Relatorios.Form.dll

## 11.83.55.191

* **[Ticket: 07\TTIDF1]** Legislação para FAP.

Arquivo: RM.Fop.Secao.Intf.dll

## 11.83.55.192

### Rotina: eSocial

* **[Ticket: PCREQ-3579]** Geração dos Eventos da Carga Inicial e Validador de Base do eSocial

Arquivo: RM.Lib.Params.Wizard.xml

## 11.83.55.194

* **[Ticket: 07\TTIDF1]** De acordo com resolução CNPS nº 1.327 de 24/09/2015 publicada no Diário Oficial de 25/09/2015, o FAP (Fator Acidentário de Prevenção), o qual estabelece que o cálculo da GPS em 2016 deverá ser determinado por estabelecimento, ou seja, poderemos ter casos de FAP diferentes entre Matriz e Filiais de uma mesma Coligada.Para atender a resolução CNPS nº 1.327 foi criado o anexo "FAP por estabelecimento empresarial" no cadastro de seção. Deve ser informado a vigência em que o estabelecimento terá o FAP diferenciado. Após efetuar este cadastro deve relacionar a vigência para Alíquota com o seu valor.Conforme descrito acima, para o controle do FAP por estabelecimento, a duas vigências: Uma para definir o período em que o estabelecimento usará FAP diferenciado do Valor fixo, e outra para definir uma ou mais alíquota dentro da vigência principal.Com estas duas vigências informada o sistema poderá identificar se utilizará o FAP do valor fixo ou do anexo da seção.Nos módulos que utilizam o FAP como Folha Analítica, GUIA de INSS o sistema irá identificar a seção centralizadora de CNPJ do funcionário está sendo processado e verificará se no primeiro dia da competência informada a vigência para o FAP por estabelecimento, caso haja irá buscar a alíquota, caso não haja irá buscar a alíquota no valor fixo. Porém caso haja vigência para o FAP por estabelecimento, mas não tendo vigência para alíquota. O sistema não processará o funcionário ou seção, informando no log as seções e ou funcionários que não foram processadas. O sistema irá consistir o cadastro para o FAP por estabelecimento empresarial, a saber:• O FAP deverá ser informado nas seções centralizadoras de CNPJ de acordo com o informado no parâmetro "Código de Quebra para CNPJ". Será emitida uma mensagem de alerta caso a seção não seja centralizadora de CNPJ;• As datas de início e fim de vigências são obrigatórias;• A data final deverá ser maior ou igual a data inicial;• Não será permitido informar vigências em que o intervalo de datas tenha interseção com vigência já cadastradas;• A vigência do FAP deverá englobar todas as vigências de suas respectivas alíquotas;• O valor da alíquota dever ser maior que zero.• Ao Excluir uma vigência para o FAP por estabelecimento todas as suas alíquotas também serão excluídas.Na Folha Analítica os campos que utilizam o FAP são: "INSSTotalEmpSatJustTerc" e "INSS (Emp+SATAju+Terc)". Quando a seção centralizadora de CNPJ possui vigência cadastrada para FAP por Estabelecimento no primeiro dia da competência, mas não possui vigência para alíquota o sistema não processa a seção e informa no Log a mensagem: "Seção {1} Não foi processado. Seção centralizadora de CNPJ Não possui Alíquota para FAP por Estabelecimento".Na Guia de INSS o campo "Acidente Trabalho" e consequentemente os que são impactado por ele utilizaram o FAP por estabelecimento ou pelo valor fixo seguindo as mesmas regras citadas para Folha Analítica.  Quando a seção centralizadora de CNPJ possui vigência cadastrada para FAP por Estabelecimento no primeiro dia da competência, mas não possui vigência para alíquota o sistema não processa a seção e informa no Log a mensagem: "Coligada {0} Seção {1} Não foi processada. Seção centralizadora de CNPJ Não possui Alíquota para FAP por Estabelecimento em dd/mm/aaaa".O SEFIP o FAP é informado no aplicativo do governo e por isso não foi necessários ajustes quanto ao FAP.A Liberação de Competência irá estender a vigência do FAP por estabelecimento assim como é feito para o valor fixo, desde de que o campo "Atualiza final de vigência na liberação de competência" tenha sido marcado. No  Log do debug é informado "Atualizando vigência para FAP por Estabelecimento".Os novos cadastros foram contemplados no processo de "Troca código de seção".Foi criado a formula "FAPCHAPADATA" que recebe como parâmetros a data e a chapa do funcionário, a seção centralizadora é obtida pela histórico de seção do funcionário. A formula retora 0 (Zero) se a seção centralizadora de CNPJ não tem cadastrado vigência de FAP por estabelecimento, -1 quando possui vigência para o FAP mas não possui alíquota na data informada, ou o valor da alíquota referente ao FAP.

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Lib.Extensions.dll, RM.Fop.Processos.Data.dll, RM.Fop.Data.Server.dll, RM.Fop.Rotinas.Data.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Secao.Form.dll, RM.Fop.Secao.Data.dll, RM.Fop.Secao.Intf.dll, RM.Fop.Dominio.dll, RM.Fop.Calc.Formulas.dll, RM.Fop.Data.Intf.dll, RM.Fop.Utils.Server.dll

## 11.83.55.197

* **[Ticket: 07\TTXEX4]** Realizado downgrade da rotina Rais para conferência

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Utils.Intf.dll, RM.Fop.Lib.Extensions.dll, RM.Fop.Utils.Server.dll, RM.Fop.Relatorios.Server.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Calc.Interfaces.dll

* **[Ticket: Alterações Gerais]** Merge de Con-Cenector - Requisitos x 11.83

Arquivos: RM.Fop.Facade.dll, RM.Rhu.Facade.dll

## 11.83.55.198

* **[Ticket: 07\TTXEX4]** Realizado downgrade Rais para conferência

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Form.dll

## 11.83.55.199

* **[Ticket: 07\TTXOEL]** Foi adicionado uma checkbox na tela de cadastro de encargo para informar se será ou não acrescentado o percentual FAP por estabelecimento no momento da geração do encargo. Caso esteja marcado, no momento da geração do encargo é buscada a alíquota FAP vigente para a filial em questão no período informado.

Arquivos: RM.Fop.Rotinas.Server.dll, RM.Fop.Cadastros.Form.dll, RM.Fop.Cadastros.Data.dll, RM.Fop.Dominio.dll, RM.Fop.Rotinas.Data.dll, RM.Fop.Cadastros.Intf.dll, RM.Fop.Utils.Server.dll, RM.Fop.Infraestrutura.Repositorios.dll, RM.Fop.Secao.Services.dll

* **[Ticket: 07\TTD137]** - Ajuste na rotina da Rais para considerar valor correto para Seção Sindicalizada, respeitando o valor informado.- Ajuste na rotina de Rais para trazer registro de funcionário quando identificado por CEI. Arquivo trazia somente registros das seções.

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Server.dll, RM.Fop.Calc.Interfaces.dll

* **[Ticket: 07\TTMO78]** Ajuste no cadastro de periodo aquisitivo de férias, quando é acionado o recurso para visualizar o nome dos campos, para informar "Campo calculado pelo sistema" no campo "Saldo do período(vencido)".

Arquivo: RM.Fop.FuFerias.Data.dll

* **[Ticket: 07\TTYM77]** Campo Prefixo Rais no arquivo com valor errado.Gerar arquivo contendo varios registros de seções, onde algumas contenham prefixo diferente. O sistema atribui a todas um valor de prefixo errado no arquivo (.DEC) registro 1 posições 021 a 022.

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TTZIJF]** - Ajuste na rotina da Rais para considerar valor correto do campo CNPJ Centralizadora, respeitando o valor informado.

Arquivos: RM.Fop.Calc.Interfaces.dll, RM.Fop.Relatorios.Form.dll

## 11.83.55.200

* **[Ticket: 07\TTYHKU]** Alterações DIRF 2016.

Arquivos: RM.Fop.Lib.Intf.dll, RM.Fop.Dominio.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Infraestrutura.Repositorios.dll, RM.Fop.Const.Intf.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Lib.WinForms.dll

* **[Ticket: 07\TTXXDJ]** Tratamento de valores de perfis antigos que acessavam campos com valores nulos

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TTZDUR]** Ajuste na rotina Rais para validar linhas excluídas e não tentar acessá-las

Arquivo: RM.Fop.Dominio.dll

## 11.83.55.201

* **[Ticket: 07\TU3383]** Caso 1: Ajuste na rotina da Rais para considerar valor de aviso previo indenizado quando demissão ocorrer anterior ao ano base e a data de projeção for no ano base. Exemplo: Ano base 2015 - Data desligamento em dezembro de 2014 e data de projeção em janeiro de 2015Caso 2: Ajuste na rotina da Rais para considerar valor de aviso previo indenizado quando demissão ocorrer no ano base e a data de projeção também for no ano base. Exemplo: Ano base 2015 - Data desligamento em novembro de 2015 e data de projeção em dezembro de 2015

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 07\TTZUVS]** Alteração DIRF 2016.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 07\TTZYYF]** Alterações DIRF 2016: Atualizado Instrução Normativa do Informe de Rendimento no Portal .

Arquivos: RM.Fop.Informe.Data.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: 07\TU4467]** Verificação de parâmetro gravado antes de carregar, evitando acesso à objeto nulo (não preenchido)

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TTZSAD]** Ajuste na rotina Rais para gravar parametros especificos de coligadas na aba de seções

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TTXOEL]** Geração de Encargos com alíquota FAP por filial não estava levando em consideração do valor SAT da seção.

Arquivo: RM.Fop.Dominio.dll

## 11.83.55.202

* **[Ticket: 07\TTXOEL]** Geração de Encargos com FAP por Filial

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 07\TTZTLF]** Ajuste para carregar parâmetros específicos de coligada quando salva perfil antes de carregar aba de multicoligadas.

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Dominio.dll

* **[Ticket: 07\TUAQAB]** Ajustada geração da DIRF para que seja sempre levado o funcionário que tenha rendimentos isentos.

Arquivo: RM.Fop.Relatorios.Data.dll

## 11.83.55.203

* **[Ticket: 07\TUBBR1]** Ajuste na rotina Rais para considerar primeiramente o valor de Tipo de Sistema de Controle de Ponto informado nos parametros específicos, caso não tenha informado, considerar cadastro de seções

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 07\TUB661]** Ajuste na rotina Rais para arredondar valores de horas extras conforme era arredondado no Delphi.Ajuste em campo de Série de CTPS para retirar alfabéticos e espaços em branco conforme validador, preenchendo com zeros à esquerda

Arquivos: RM.Fop.Dominio.dll, RM.Fop.Relatorios.Server.dll

## 11.83.55.204

* **[Ticket: 07\TUAYZE]** Alterado a idade obrigatória para o CPF do dependente de 16 para 14 anos, ao informar os dados de assistência médica na DIRF 2016.

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: 07\TUBBSO]** Os proventos de aposentadoria, reserva ou reforma e de pensão civil ou militar pagos por previdência da União, estados, DF ou municípios (regime geral ou do servidor público) deverão ser informados no código 3533.Para atender essa demanda no produto foi feito as seguintes alterações: - Criado no cadastro do funcionário o campo DIRF - Informar remuneração no Cód. da Receita 3533. Caso esse parâmetro esteja marcado o sistema irá informar toda a movimentação desse funcionário no código 3533. - Caso o usuário deseja informa muitos funcionários com o código da receita 3533 pode utilizar o processo alteração global de campos do cadastro, alterando o campo CODIGORECEITA3533 para 1; - Ao gerar o arquivo o sistema passa a gerar também o registro IDREC 3533, respeitando a ordenação dos outros IDREC no arquivo: ? IDREC|3533|

Arquivos: RM.Fop.Funcionario.Form.dll, RM.Fop.Funcionario.Server.dll, RM.Fop.Funcionario.Intf.dll, RM.Fop.Funcionario.Data.dll, RM.Fop.Infraestrutura.Repositorios.dll

* **[Ticket: 07\TTZWNE]** Ajuste no arquivo gerado da RAIS para considerar valores de casas decimais e zeros à esquerda nos campos: Natureza Jurídica, Atividade Econômica, Código do Município, Valor contribuição confederativa, Valor contribuição assistencial, Valor contribuição sindical, Valor contribuição associativa

Arquivos: RM.Fop.Dominio.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Intf.dll

* **[Ticket: 07\TUBPIM]** 1 - Ajustado validação se tem base de irrf quando o funcionário tem RRA;2 - Ajustado validação da base de irrf de 13º para considerar se deve informar a dedução de dependente ou não;3 - Tratado as situações que impediam o sistema de lançar os valores para o gerador de relatórios quando utilizava o informe de rendimentos em txt;4 - Criado opção para o usuário lançar apenas os valores para o gerador de relatório fazendo com que a geração seja mais rápida. Antes o sistema sempre gerava o informe de rendimentos, mesmo quando o usuário não ia utilizar.

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Intf.dll

* **[Ticket: 07\TU3278]** Ajuste em rotina da RAIS para levar verbas rescisórias relativa ap ano anterior ao ano base quando existe projeção de aviso prévio indenizado para o ano seguinte (ano base)

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 07\TUBQCK]** Ajuste em rotina RAIS para considerar valor de código de estado (IBGE) concatenado com código de município quando não preenchido no cadastro de seções

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Dominio.dll

## 11.83.55.205

* **[Ticket: 07\TSLCO8]** Foi realizado a adaptação da RAIS genérica referente ao layout 1976-2014 Data 21/01/2016-11:56Baixado de: http://www.rais.gov.br/sitio/download.jsf#gdPrazo.Registro 1:Campo Informação de Uso Exclusivo da Empresa: Para RAIS Genérica passa a informar cinco espaços em branco estava saindo a informação "REG. TIPO 1".Para RAIS Genérica foi incluído o campo Natureza Jurídica do estabelecimento que não estava sendo contempladoRegistro 2:Campo Reservado para informação de uso exclusivo da empresa: Para RAIS genérica passa a informar cinco espaços embranco estava saindo 12 espaços e o conteúdo era a chapa do funcionário.Campo entre o CPF e número da CTPS para RAIS genérica passa a sair (0) zero antes saia um espaço em brancoPara RAIS Genérica foi incluído o campo CBO que não estava sendo contemplado.

Arquivo: RM.Fop.Dominio.dll

## 11.83.55.206

* **[Ticket: 07\TUCGX2]** Ajuste na rotina RAIS para verificação de existência de coluna TIPOCONTROLEPONTO da tabela PSECAO ao utilizar perfis mais antigos

Arquivo: RM.Fop.Relatorios.Server.dll

* **[Ticket: 07\TTXL17]** Criação do parâmetro "Não lança avo 13o.indenizado quando a projeção do aviso não chega a 15 dias do mês seguinte".

Arquivos: RM.Fop.Parametros.Form.dll, RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Parametros.Intf.dll

* **[Ticket: 07\TUBWT5]** Ajustado a validação do Registro ANS ao preencher os dados da Assistência à Saúde na DIRF.

Arquivo: RM.Fop.Relatorios.Form.dll

## 11.83.55.207

* **[Ticket: 07\TUCBGW]** Ajuste na rotina Rais para copiar parâmetros específicos da coligada ao ser copiado de perfil existente

Arquivo: RM.Fop.Relatorios.Form.dll

## 11.83.55.208

* **[Ticket: 07\TUEELD]** Ajuste em rotina RAIS para evitar inclusão de linhas vazias no grid de seções

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TTZUGT]** Equivalência para a função FAPCHAPADATA em delphi como em .Net

Arquivo: RM.Fop.Calc.Formulas.dll

* **[Ticket: 07\TUCBGW]** Ajuste na rotina Rais para copiar parâmetros específicos da coligada ao ser copiado de perfil existente

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TTZSAD]** Ajuste na rotina de geração de RAIS para manter alterações no perfil na aba de seções para casos de perfil convertido do Delphi qeu ainda não foram salvos

Arquivo: RM.Fop.Relatorios.Form.dll

## 11.83.55.209

* **[Ticket: 07\TTWWNO]** Ajuste em rotina RAIS para evitar inclusão de linhas vazias no grid de seções

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 07\TUEMBZ]** Correção da atulização de vigência de alíquota FAP na liberação de competência

Arquivo: RM.Fop.Data.Server.dll

## 11.83.55.210

* **[Ticket: 07\TUGFBT]** Ajuste na rotina de Seguro Desemprego adicionando parâmetro para considerar nono dígito para o telefone no Registro 01, utilizando esse dígito dos campos reservados (Filler)

Arquivos: RM.Fop.Dominio.dll, RM.Fop.Calc.Interfaces.dll, RM.Fop.Lib.Intf.dll, RM.Fop.Relatorios.Form.dll

## 11.83.55.211

* **[Ticket: 07\TUFSPT]** Ajuste na rotina da Rais para não considerar verbas de rescisão na validação para funcionários com transferência sem ônus já que esses não possuem tais.

Arquivo: RM.Fop.Dominio.dll

## 11.83.55.212

* **[Ticket: 07\TUHG40]** Ajustado erros encontrados na DIRF 2016.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Data.dll

## 11.83.55.215

* **[Ticket: 07\TUKPHX]** Ajuste na rotina da Rais para considerar demitidos com tipo 5 - Transferidos sem onus cedente. Foi tratada condição para campo TEMAVISOPREVIO na tabela PFUNC nulo.

Arquivo: RM.Fop.Relatorios.Server.dll

## 11.83.55.224

* **[Ticket: 07\TUMNVP]** Ajuste na rotina de aviso automático para envio de mensagem por tela.

Arquivo: RM.Fop.Cadastros.Data.dll

## 11.83.55.235

* **[Ticket: 07\TVBLVH]** Ajuste no cálculo da 1a.parcela de 13o.salário para que o lançamento o evento de CC 314, Arredondamento Base, iniba o cálculo do CC 21, Arredondamento Desconto.

Arquivos: RM.Fop.Calc.Calculos.dll, RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Formulas.dll

### Rotina: eSocial - Gatilhos Monitoramento

* **[Ticket: RHFOP001-16]** Liberação do módulo de Qualificação Cadastral em lote para o eSocial

Arquivos: RM.Fop.Esocial.Form.dll, RM.Fop.Dominio.dll, RM.FopFolha.dll, RM.Fop.Lib.WinForms.dll, RM.Fop.Lib.Intf.dll, RM.Fop.Esocial.Data.dll, RM.Fop.Lib.Data.dll

## 11.83.55.244

* **[Ticket: 07\TVJWKK]** Ajuste no Acerta Período Aquisitivo, que estava cadastrando um dia a menos na data fim, quando o período aquisitivo é estendido devido a afastamento tipo L.

Arquivo: RM.Fop.Calc.Calculos.dll

## 11.83.55.266

### Rotina: GRUPO DE EVENTOS LAB 01 116

* **[Ticket: 464050 / MRH-6351]** Ajuste no cálculo da Contribuição Sindical para efetuar o desconto dos funcionários admitidos em dezembro, na competência janeiro do ano seguinte.

Arquivo: RM.Fop.Calc.Calculos.dll

# TOTVS Framework

## 11.83.55.103

* **[Ticket: Alterações Gerais]** Não consumir licenças ao abrir os Parâmetros Globais.

Arquivo: RM.Glb.Cadastros.Form.dll

## 11.83.55.104

* **[Ticket: Alterações Gerais]** Melhoria o consumo de licença correto pelos sistemas Delphi quando o licenciamento for corporativo.

Arquivo: RM.Lib.Interop.dll

* **[Ticket: 07\TQZMSF]** A seleção do tipo de código fixo / atividades complementares foi otimizada.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.105

* **[Ticket: 07\TQZMSF]** A seleção do tipo de código fixo / atividades complementares foi otimizada.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.106

* **[Ticket: 07\TRCTFB]** A seleção do código do trabalho foi otimizada.

Arquivo: RM.Lib.WinForms.dll

* **[Ticket: Alterações Gerais]** Retirando exibição de mensagem "Erro do License Server desconhecido" quando a licença do cliente está próximo de expirar.

Arquivos: Totvs.Licence.Client.dll, RM.Lib.dll

## 11.83.55.108

* **[Ticket: 07\TQLBNB]** A tradução do sistema foi otimizada e ampliada para traduzir alguns controles (RMSTextBox e RMSLookup) que antes não eram traduzidos.

Arquivos: RM.Lib.WinForms.dll, RM.Lib.Server.dll

* **[Ticket: 07\TQZOIF]** A importação de fórmulas visuais que contenham fórmulas foi otimizada.

Arquivo: RM.Glb.ImpExp.Server.dll

* **[Ticket: 07\TRDQEC]** Otimização do Acesso TS

Arquivo: RM.Lib.dll

* **[Ticket: 07\TRDIFY]** Otimização da abertura de planilha.Net

Arquivo: RM.Glb.PlanilhaNet.Intf.dll

## 11.83.55.110

* **[Ticket: Alterações Gerais]** Inserindo stacktrace ao ero de criação do broker.dat

Arquivo: RM.Lib.Server.dll

## 11.83.55.111

* **[Ticket: 07\TRFGI0]** Otimização no envio de email assicrono.

Arquivo: RM.Lib.dll

## 11.83.55.115

* **[Ticket: 07\TRHXC7]** Otimizado componente de máscara para Windows Forms

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.118

* **[Ticket: 07\TRHJKE]** A cópia de feriados entre calendários foi otimizada.

Arquivo: RM.Glb.Processos.Form.dll

## 11.83.55.121

* **[Ticket: 07\TRP524]** O merge das correções na versão 11.83.55 foram feitas.

Arquivos: Portal Corpore.Net

* **[Ticket: 07\TRJAXF]** Otimização na atualização nos dados da Planilha.

Arquivo: RM.Glb.PlanilhaNet.API.dll

* **[Ticket: 07\TROPAF]** Otimização do RMSClientUpdate

Arquivo: RM.Lib.dll

* **[Ticket: 07\TRMFR2]** A associação do departamento na unidade bibliotecária foi otimizada.

Arquivo: RM.Glb.Cadastros.Intf.dll

## 11.83.55.128

* **[Ticket: 07\TPNQMN]** Otimizações da inicialização do host.

Arquivo: RM.Lib.Server.dll

## 11.83.55.133

* **[Ticket: 07\TRSUWZ]** A utilização de valores defaul em campos complementares foi otimizada.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.136

* **[Ticket: 07\TRPUVW]** Otimizações da importação e exportação de objetos

Arquivo: RM.Lib.dll

* **[Ticket: Alterações Gerais]** Otimizado processo de geração de DANFE Provider em PDF para ser enviada por email

Arquivos: RM.Lib.dll, RM.Lib.Jobs.Server.dll, RM.Lib.WinForms.dll, RM.Rpt.Reports.Form.dll

## 11.83.55.137

* **[Ticket: 07\TRVZM1]** A utilização de campos complementares foi otimizada.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.143

* **[Ticket: 07\TRHDW6]** Melhoria na exibição do resultado da execução de processos.

Arquivos: RM.Lib.Jobs.Common.dll, RM.Lib.WinForms.dll

## 11.83.55.149

* **[Ticket: 07\TSBTDC]** Possibilitar a função planilha tipo Excel, salvar como, ou seja, sem a barra lateral que vincula o Excel ao ERP.

Arquivo: RM.Glb.PlanilhaNet.API.dll

## 11.83.55.151

* **[Ticket: Alterações Gerais]** Acerto do erro ao iniciar host

Arquivo: RM.Lib.Server.dll

* **[Ticket: Alterações Gerais]** Acerto do erro ao gerar o broker quando há concorrência.

Arquivo: RM.Lib.Server.dll

* **[Ticket: 07\TSBQSV]** Otimizado processo de enviar e-mail com conteúdo do relatório destinado ao corpo do e-mail

Arquivo: HtmlAgilityPack.dll

* **[Ticket: 07\TSEN26]** Otimizações da fórmula visual.

Arquivo: RM.Lib.Workflow.Activities.dll

## 11.83.55.152

* **[Ticket: 07\TRVHL5]** Otimização na exibição de aba Campos Complementares

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.153

* **[Ticket: Alterações Gerais]** Remove todo o conteúdo da tag <script> do HTML somente se a Tag Script existir no documento

Arquivo: RM.Lib.Server.dll

## 11.83.55.155

* **[Ticket: 07\TSHG40]** A seleção das datas no formulário de filtros da visão foi normalizada.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.158

* **[Ticket: 07\TSDHFC]** Otimizado processo que associa uma Action de Processo Web em um gatilho na Fórmula Visual

Arquivos: RM.Lib.dll, RM.Lib.WebForms.dll, RM.Glb.Workflow.Form.dll

## 11.83.55.164

* **[Ticket: 07\TSOQBS]** Após o retorno da customização de uma dll pela equipe TOTVS TEC de são paulo, foi realizado o checkin do ShelveSet MelhoriasLS\_1183 enviado pelo Diogo Ferreira com a solução do cliente.

Arquivos: license\_client\_x64.dll, license\_client\_x86.dll

## 11.83.55.167

* **[Ticket: 07\TSQGJP]** Melhoria para permitir a utilização de processos web em fórmulas visuais.

Arquivos: RM.Lib.Workflow.Activities.dll, RM.Lib.WebForms.dll, ProcessControl.js, ProcessControlList.js, App\_Web\_viewcontrol.ascx.bb2461a3.dll

## 11.83.55.168

* **[Ticket: 07\TSVSL5]** Melhorias internas para impedir queda do host causada pela concorrência na liberação de licenças.

Arquivo: RM.Lib.dll

## 11.83.55.169

* **[Ticket: Alterações Gerais]** Montar corretamente as URIs dos Endpoints WCF.

Arquivo: RM.Lib.Server.dll

## 11.83.55.174

* **[Ticket: Alterações Gerais]** -Publicação de propriedades do RMSMail

Arquivo: RM.Lib.Server.dll

* **[Ticket: Alterações Gerais]** -Otimizações do envio de e-mail

Arquivo: RM.Lib.Server.dll

## 11.83.55.182

* **[Ticket: 07\TTKPM0]** Ajustes e melhorias no jobserver referentes ao processamento de fila

Arquivos: RM.Lib.Jobs.Server.dll, RM.Host.JobRunner.exe, RM.Lib.Data.dll, RM.Lib.Server.dll, RM.Lib.dll

## 11.83.55.183

* **[Ticket: 07\TSYCOA]** Melhoria ao vincular mapa em anexo as visões do RM.

Arquivos: RM.Lib.WinForms.dll, App\_Web\_gmaps.aspx.83896cb1.dll, GoogleMaps.js, GRouteMaps.aspx, GMaps.aspx

## 11.83.55.184

* **[Ticket: 07\TSHHCM]** Melhoria na integração entre Protheus e RM.

Arquivos: RM.Lib.dll, RM.Con.Conector.Service.dll, RM.Lib.Server.dll

## 11.83.55.188

* **[Ticket: Alterações Gerais]**

Arquivos: RM.Lib.Server.dll, WeifenLuo.WinFormsUI.Docking.dll, WindowsInput.dll, RM.Lib.WinForms.dll, CommandLine.dll, Dapper.dll, RM.Lib.dll

## 11.83.55.191

* **[Ticket: 07\TTRT60]** Melhoria ao executar processos com um sistema ou coligada selecionados na visão de consultas SQL.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.192

* **[Ticket: Alterações Gerais]** Vazamento de memória no host e na mdi provocava a queda dos mesmos.

Arquivos: RM.Glb.Workflow.Server.dll, RM.Lib.Workflow.Runtime.dll

## 11.83.55.203

* **[Ticket: 07\TUAWVV]** Melhoria ao acessar a visão de integrações.

Arquivo: RM.Lib.dll

## 11.83.55.211

* **[Ticket: 07\TUFNHP]** Melhoria para o correto funcionamento no .NET Framework 4.6

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.213

* **[Ticket: 07\TTXIV3]** Melhoria na tela inicial da nova MDI de forma que não sejam exibidas mensagens de erro no consumo do serviço que disponibiliza as novidades do sistema.

Arquivo: RM.Glb.dll

## 11.83.55.219

* **[Ticket: 07\TUNKCD]** Ajuste para tratar a fonte de dados do formulário ao fechar a janela.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.222

* **[Ticket: 07\TUPVPI]** Alterações globais para a impressão de relatórios em 3 camadas

Arquivos: RM.Lib.Report.Server.dll, RM.Lib.Report.dll

## 11.83.55.223

* **[Ticket: 07\TUNKCD]** Ajuste para tratar a fonte de dados do formulário ao fechar a janela.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.224

* **[Ticket: 07\TUSCEU]** Ajuste na lib solicitada pela equipe do Agilis

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.225

* **[Ticket: 07\TUQPQL]** Melhoria no processo de troca de senha

Arquivo: RM.Lib.Server.dll

## 11.83.55.226

* **[Ticket: 07\TUSMH5]** Melhoria na exibição e fechamento de formulários

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.230

* **[Ticket: 07\TUUY59]** Implementação de entrypoint para equipe da customização

Arquivo: RM.Glb.Seguranca.Server.dll

## 11.83.55.231

* **[Ticket: 07\TUXPPT]** Ao configurar um usuário para trocar a senha no próximo Login a exceção não mais aparece e o fluxo de acesso ao sistema funciona corretamente.

Arquivo: RM.Lib.Server.dll

## 11.83.55.232

* **[Ticket: Alterações Gerais]** Implementação de Entrypoint para a customização

Arquivo: RM.Glb.Seguranca.Intf.dll

## 11.83.55.233

* **[Ticket: Alterações Gerais]** Implementação de Entrypoint para a customização

Arquivo: RM.Glb.Seguranca.Server.dll

## 11.83.55.239

### Rotina: Mudar informação ProcessorModel no RMSHardwareInfo

* **[Ticket: R\_FRW\_INOVBH-64]** Melhoria no consumo de licenças

Arquivo: RM.Lib.dll

## 11.83.55.242

* **[Ticket: 07\TVCOIH]** 07Ajuste na action painel de metas para que a mesma possa ser utilizada na inicialização automática do sistema.

Arquivos: RM.Glb.BalancedScorecard.Data.dll, RM.Lib.WinForms.dll, RM.Glb.BalancedScorecard.Form.dll

## 11.83.55.244

* **[Ticket: 07\TVEKOS]** Foi incluido um cache de dados no momento de salvar o relatório que diminui o número de requisições ao banco e consequentemente impede o esgotamento do pool de conexões.

Arquivos: RM.Rpt.Lib.dll, RM.Lib.Data.dll

## 11.83.55.246

* **[Ticket: 07\TVKLNF]** Melhoria na exportação de pacotes de tradução.

Arquivo: RM.Lib.Server.dll

* **[Ticket: 07\TVNKHI]** -Assim como as versões mais recentes da aplicação, ao importar uma fórmula não deve ficar disponível a opção "Todas Coligadas"

Arquivos: RM.Lib.WinForms.dll, RM.Glb.ImpExp.Form.dll

## 11.83.55.251

* **[Ticket: 07\TVUKLS]** Downgrade das ultimas correções relacionadas ao License Server

Arquivos: Totvs.Licence.Client.dll, RM.Lib.Server.dll, RM.Lib.Interop.dll, RM.Lib.dll, RM.Lib.WinForms.dll

* **[Ticket: 07\TVVCOK]** Downgrade das ultimas correções relacionadas ao License Server

Arquivo: RM.Lib.dll

## 11.83.55.252

* **[Ticket: 07\TVKLJE]** Melhoria em lookups quando a tag do host EnableDynamicLocalization está ativada.

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.253

* **[Ticket: 07\TVY419]** Melhoria no anexos obrigatórios do cadastro

Arquivos: RM.Lib.WinForms.dll, RM.Lib.Server.dll

## 11.83.55.264

### Rotina: Ao ativar o JobRunner os plugins customizados em processos param de funcionar.

* **[Ticket: 206167 / MFRWBH-1016]** Melhoria no JobRunner para que execute customizações de processos.

Arquivo: RM.Lib.Server.dll

## 11.83.55.270

### Rotina: Project-580520 Importação de Consulta SQL Project-580520

* **[Ticket: 583374 / MFRWBH-1314]** Melhoria na exportação/importação de consulta SQL contendo Stored Procedure na sua configuração

Arquivo: RM.Glb.ImpExp.Server.dll

## 11.83.55.273

### Rotina: PERFIL

* **[Ticket: MFRWBH-1481]** Melhoria na restrição de campos do RM.

Arquivo: RM.Lib.Server.dll

### Rotina: Project-581969 Planilha .NET Project-581969

* **[Ticket: 596114 / MFRWBH-1331]** -Otimização das planilhas para que seja possível abri-las em versões mais antigas do Office como a versão 2007.

Arquivo: RM.Glb.PlanilhaNet.Intf.dll

## 11.83.55.279

### Rotina: TROCAR SENHA FRW 00070

* **[Ticket: 794485 / MFRWBH-1673]** A integração com LDAP foi otimizada

Arquivo: RM.Lib.Server.dll

## 11.83.55.282

### Rotina: PERMISSÕES DE ACESSO FRW00058

* **[Ticket: MFRWBH-1780]** Alteração dos métodos de TotvsLicense no Interop

Arquivo: RM.Lib.Interop.dll

## 11.83.55.299

### Rotina: GERACAO DE RELATORIO RPT 00005

* **[Ticket: 1259202 / DFRWBI-212]** Melhoria para que as permissões de exibição de relatórios também sejam aplicadas no menu do TOTVS Reports na aba Gestão da nova MDI.

Arquivos: RM.Lib.dll, RM.MDI.Server.dll, RM.exe

## 11.83.55.300

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 1140369 / DFRWFOUNDATION-408]** Mascara para telefone com 9 digitos foi implementado corretamente

Arquivo: RM.Lib.WinForms.dll

## 11.83.55.302

### Rotina: FORMULAS EXECUCAO FRW 00033

* **[Ticket: 1361862 / DFRWBI-453]** Otimização da edição de consultas SQL em bases distintas.

Arquivo: RM.Lib.Server.dll

# TOTVS Framework Web

## 11.83.55.128

* **[Ticket: 07\TRRDCG]** A utilização do portal do RH foi otimizada.

Arquivo: RM.Lib.WebForms.dll

* **[Ticket: 07\TRRDCG]** Melhorias internas no consumo de licenças

Arquivos: App\_Web\_rmwjsresource.js.aspx.630e773b.dll, RM.Lib.WebForms.dll

* **[Ticket: Alterações Gerais]** A utilização do portal do RH foi otimizada.

Arquivo: RM.Lib.WebForms.dll

## 11.83.55.175

* **[Ticket: 07\TSYLB0]** Correção para que a mensagem "Value cannot be null. Parameter name: value" não seja exibida ao acessar o espelho do funcionário no portal.

Arquivo: RM.Lib.WebForms.dll

## 11.83.55.178

* **[Ticket: 07\TTCI74]** -Converter uma base para base teste e tentar acessar o portal.

Arquivo: RM.Lib.WebForms.dll

## 11.83.55.296

### Rotina: FRW 00023

* **[Ticket: MFRWBH-2270]** Melhoria na segurança do RM Portal

Arquivo: RM.Lib.Web.dll

## 11.83.55.307

### Rotina: PORTAL ALUNO DADOS PESSOAIS EDU 50 349

* **[Ticket: 1498120 / DFRWFOUNDATION-937]** Os campos com mascara de telefone aparecem corretamente mesmo com a mascara de nono digito.

Arquivos: RM.Lib.Web.dll, RM.Lib.WebForms.dll, MaskedTextBox.js

## 11.83.55.321

### Rotina: Componente RMWCEPTextBox deve respeitar a máscara setada

* **[Ticket: DFRWFOUNDATION-2475]** O Componente RMWCEPTextBox foi ajustado para que ao carregar ele respeite a mascara.

Arquivo: RM.Lib.WebForms.dll

# TOTVS Gerador de Relatórios

## 11.83.55.102

* **[Ticket: 07\TRBHFZ]** Otimizações para NF-e

Arquivos: RM.Rpt.Lib.Server.dll, RM.Rpt.Lib.dll

## 11.83.55.105

* **[Ticket: 07\TRCGLD]** Otimização na execução de relatórios do tipo Dados da minha equipe.

Arquivos: RM.Rpt.Reports.Server.dll, RM.Rpt.Reports.Intf.dll, RM.Rpt.Reports.Data.dll, RM.Rpt.Lib.dll

## 11.83.55.114

* **[Ticket: 07\TRFR76]** Otimizaçõa de execução dos relatórios do tipo Dados da Minha Equipe.

Arquivo: RM.Rpt.Reports.Data.dll

## 11.83.55.115

* **[Ticket: 07\TQYZGZ]** A árvore de relatórios, ao clicar no link Relatórios .Net - Gestão de RH, agora é aberto de acordo com o filtro passado pela action.

Arquivos: App\_Web\_rptreportswebmainform.ascx.ffa54ff2.dll, RM.Rpt.Reports.Data.dll, RM.Rpt.Reports.Intf.dll

## 11.83.55.138

* **[Ticket: 07\TRPUVW]** A importação e exportação de relatórios foi otimizada.

Arquivo: RM.Rpt.Lib.dll

## 11.83.55.169

* **[Ticket: 07\TSKDPK]** Melhoria ao utilizar texto rico no TOTVS Reports.

Arquivo: RM.Rpt.Lib.dll

## 11.83.55.190

* **[Ticket: 07\TTHAGC]** Ao importar um relatório net, o sistema agora indica corretamente se a consulta existe ou não na coligada corrente (a ser importado o relatório).

Arquivos: RM.Rpt.Lib.Server.dll, RM.Rpt.Lib.dll, RM.Rpt.Reports.Form.dll

## 11.83.55.290

### Rotina: Project-1045805 Erro ao importar relatório Project-1045805

* **[Ticket: 1047504 / MFRWBH-2073]** Melhoria na importação de relatórios que seja alterado o código da sentença SQL vinculada

Arquivo: RM.Rpt.Reports.Server.dll

# TOTVS Gerador de saídas

## 11.83.55.161

* **[Ticket: Alterações Gerais]** Ajuste solicitado pelo Paulo Andre da Rocha da equipe Educacional.

Arquivo: RM.Gen.Engine.dll

## 11.83.55.166

* **[Ticket: Alterações Gerais]** Alterações solicitadas pelo Paulo Andre.

Arquivo: RM.Gen.Engine.dll

## 11.83.55.174

* **[Ticket: 07\TTCIFP]** Otimização do gerador de saídas para contendo valores decimais negativos.

Arquivo: RM.Gen.Engine.dll

## 11.83.55.254

* **[Ticket: 07\TVZRNP]** Melhoria na utilização de stored procedures em contexto do gerador de saídas com base oracle.

Arquivo: RM.Gen.Engine.Server.dll

# TOTVS Gestão Bibliotecária

## 11.83.55.100

* **[Ticket: 07\TR8502]** Adaptação do sistema na exibição de anexo para informações de integração com o Protheus na unidade bibliotecária.

Arquivo: RM.Bib.Cadastros.Form.dll

## 11.83.55.154

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Melhoria no envio das informações bancárias, na mensagem de lançamentos a receber, ao se utilizar bases Oracle, para a integração por mensageria única. As informações de banco, agência e conta corrente não eram enviados.

Arquivos: RM.Bib.Cadastros.Intf.dll, RM.Bib.Financeiro.Server.dll, RM.Bib.Cadastros.Server.dll, RM.EduPS.Cadastros.Intf.dll, RM.EduPS.Cadastros.Data.dll, RM.Bib.Cadastros.Form.dll, RM.EduPS.Facade.Intf.dll, RM.EduPS.Facade.Server.dll, RM.Bib.Cadastros.Data.dll, RM.Bib.Facade.dll, RM.Fin.Lan.IService.dll, RM.EduPS.ProcessoSeletivo.Server.dll, RM.EduPS.Cadastros.Form.dll, RM.Bib.Lib.Intf.dll, RM.EduPS.Lib.Intf.dll

## 11.83.55.158

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Ajuste no envio da informação de Centro de Custo da unidade bibliotecária para a integração financeira por mensageria única.

Arquivo: RM.Bib.Cadastros.Server.dll

* **[Ticket: PCREQ-3488]** Ajuste na geração da mensagem de lançamentos a receber no TOTVS Gestão Bibliotecária para enviar sempre o Centro de Custo associado com a unidade bibliotecária.

Arquivo: RM.Bib.Facade.dll

## 11.83.55.167

* **[Ticket: 07\TRZ568]** Otimizado processo de pesquisa no acervo.

Arquivo: RM.Bib.Pesquisa.Server.dll

## 11.83.55.213

* **[Ticket: 07\TUGFLB]** Ajusta nos filtros de unidades bibliotecárias na pesquisa ao acervo.

Arquivo: RM.Bib.Lib.Intf.dll

## 11.83.55.248

* **[Ticket: 07\TVNURA]** Ajuste nos campos de classificação e subclassificação no cadastro de publicação.

Arquivo: RM.Bib.Publicacao.Form.dll

## 11.83.55.251

* **[Ticket: 07\TVNURA]** Ajuste na geração do código da área do conhecimento.

Arquivos: RM.Bib.Cadastros.Data.dll, RM.Bib.Cadastros.Intf.dll

# TOTVS Gestão Contábil

## 11.83.55.123

* **[Ticket: Alterações Gerais]** Melhoria na integração com a mensageria única para envio das informações de Classe de Valor e Item Contábil junto da mensagem de lançamentos contábeis.

Arquivos: RM.Ctb.Lan.Service.dll, RM.Ctb.Lan.IService.dll

## 11.83.55.125

* **[Ticket: Alterações Gerais]** Evolução da integração do Educacional com Protheus tratando os campos Item Contábil e Classe de Valor na Contabilização.

Arquivos: RM.Ctb.Lib.Server.dll, RM.Ctb.Lib.dll, RM.Ctb.EventosContabeis.Data.dll, RM.Ctb.EventosContabeis.Intf.dll, RM.Ctb.EventosContabeis.Form.dll, RM.Ctb.Parametros.Intf.dll

## 11.83.55.126

* **[Ticket: Alterações Gerais]** Parametrização do Evento Contábil para integração com Protheus.

Arquivo: RM.Ctb.EventosContabeis.Data.dll

## 11.83.55.127

* **[Ticket: Alterações Gerais]** Ajuste na carga de dados de integração com Protheus na contabilização via Evento Contábil

Arquivo: RM.Ctb.Lib.Server.dll

## 11.83.55.137

* **[Ticket: 07\TRXCQH]** Não se Aplica Não se Aplica

Arquivos: RM.Ctb.ECF.IService.dll, RM.Ctb.DemonstracaoContabil.IService.dll

## 11.83.55.148

* **[Ticket: 07\TSDRWF]** Modificado o cadastro de evento contábil de forma a permitir que seja incluído em base de dados do tipo ORACLE.

Arquivo: RM.Ctb.EventosContabeis.Data.dll

## 11.83.55.149

* **[Ticket: Alterações Gerais]** Ajuste no cadastro de evento contábil para campo de Integração com Protheus.

Arquivo: RM.Ctb.EventosContabeis.Data.dll

* **[Ticket: Alterações Gerais]** Ajustes na implementação da integração da Contabilidade com Protheus.

Arquivos: RM.Ctb.Lan.IService.dll, RM.Ctb.Lan.Service.dll

## 11.83.55.150

* **[Ticket: Alterações Gerais]** Ajuste no cadastro de evento contábil quando há integração com Protheus.

Arquivo: RM.Ctb.EventosContabeis.Data.dll

## 11.83.55.154

* **[Ticket: Alterações Gerais]** Melhorias nos processos e adapters envolvidos na integração do Educacional com o BackOffice Protheus.

Arquivos: RM.Edu.Facade.Intf.dll, RM.Ctb.Lan.IService.dll, RM.Edu.Contabil.Server.dll, RM.Ctb.Lan.Service.dll, RM.Fin.Lan.Service.dll

## 11.83.55.156

* **[Ticket: 07\TSKYSA]** Modificado o SPED FCONT de forma a permitir que o arquivo seja de acordo com as informações parametrizadas.

Arquivos: RM.Ctb.Sped.Service.dll, RM.Ctb.Sped.Data.dll

## 11.83.55.157

* **[Ticket: 07\TSMUGV]** Evoluções do SPED Contábil e DMPL, DLPA

Arquivos: RM.Ctb.Sped.Data.dll, RM.Ctb.DemonstracaoContabil.Service.dll, RM.Ctb.Parametros.Intf.dll, RM.Ctb.Sped.Service.dll, RM.Ctb.DemonstracaoContabil.IService.dll, RM.Ctb.Sped.Form.dll, RM.Ctb.DemonstracaoContabil.Form.dll, RM.Ctb.Lib.Server.dll, RM.Ctb.DemonstracaoContabil.Data.dll

## 11.83.55.164

* **[Ticket: ]** Evoluções para atender a ECF

Arquivos: RM.Ctb.ECF.Form.dll, RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Ajuste na inversão de informações de Item Contábil e Classe de Valor nas partidas de estorno ao gerar lançamentos contábeis para integração por mensageria única.

Arquivo: RM.Ctb.Lan.Service.dll

## 11.83.55.165

* **[Ticket: 07\TSPSVZ]** Evolução na ECF para que o registro M312/M362 seja gerado quando o valore processado no registro M310/M360 seja diferente dos valores processados no registro K15/K355.

Arquivos: RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.Sped.Service.dll

## 11.83.55.166

* **[Ticket: 07\TSFLBY]** Evolução no recurso de apuração virtual para que seja possível identificar uma conta para Lucro e outra para Prejuízo.Para habilitar o recurso deverá ser solicitado ao suporte script.

Arquivos: RM.Ctb.ECF.Intf.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.Data.dll, RM.Ctb.ECF.Form.dll, RM.Ctb.Parametros.Intf.dll

* **[Ticket: 07\TSNNSD]** Evolução na geração do registro J051 para permitir identificar o código da tabela do PVA a ser utilizado no TAF.

Arquivos: RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll

## 11.83.55.167

* **[Ticket: 07\TSQPYT]** Melhoria no processamento das informações contábeis para ECF com objetivo de permitir ao usuário informar dados de mais de uma transferência de grupos contábeis.

Arquivos: RM.Ctb.ECF.Form.dll, RM.Ctb.DemonstracaoContabil.Form.dll, RM.Ctb.ECF.Data.dll, RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Intf.dll, RM.Ctb.DemonstracaoContabil.Service.dll, RM.Ctb.ECF.Service.dll

## 11.83.55.168

* **[Ticket: 07\TSMT89]** Evolução na ECF para contemplar a geração do registro J053

Arquivos: RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.Contas.Form.dll

* **[Ticket: 07\TSUV33]** Ajuste no filtro do cadastro de SubContas para não apresenta não conformidade quando é utilizado o campo código da conta | Ajuste para não enviar as contas com data de inclusão superior a data da ECF.

Arquivo: RM.Ctb.Contas.Form.dll

* **[Ticket: 07\TSJPMG]** Ajuste referente a seguinte situação: Na geração da ECF quando temos levantamento de balanço o valor do total de débito e crédito gerado no registro K155 esta ficando diferente do valor apresentado no relatório balancete.

Arquivo: RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TSJPMG]** Tratamento na geração do registro J050 e J100, pois a data de alteração pode não estar preenchida no cadastro.

Arquivo: RM.Ctb.ECF.Service.dll

## 11.83.55.169

* **[Ticket: 07\TSWMVG]** Identificamos uma não conformidade na Apuração Virtual, quando o saldo apurado para uma determinada conta/c. custo esta invertido em relação a natureza da conta.

Arquivos: RM.Ctb.Lan.Data.dll, RM.Ctb.ECF.Intf.dll, RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.Form.dll

* **[Ticket: 07\TSXFBC]** ECF - Implementação Contábil do Bloco Y Registro Y540

Arquivos: RM.Ctb.ECF.Form.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.IService.dll

## 11.83.55.171

* **[Ticket: 07\TSZGTB]** Disponibilizado nas opções de parametrização do registro L210 a opção "8 - Não há".

Arquivos: RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TSYQW6]** Ajuste na geração da ECF para que o sistema não barre a geração durante o processamento da apuração virtual quando for identificado lançamento manual na conta de lucro ou prejuízo.

Arquivos: RM.Ctb.Sped.Data.dll, RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TSZPW0]** Foi realizada uma analise nos itens do registro L210 para identificar quais itens deveriam mostrar o saldo inicial, quais o saldo final e quais a movimentação.Ajustamos a geração do L210 para que de forma implícita o sistema calcule estes valores .

Arquivos: RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.IService.dll

## 11.83.55.172

* **[Ticket: 07\TTAZQS]** Ao gerar o arquivo da ECF, o sistema gerou dois registros L200 para o período anual e para o período de dezembro:

Arquivo: RM.Ctb.ECF.Service.dll

## 11.83.55.174

* **[Ticket: Alterações Gerais]** Inclusão dos campos Item Contábil e Classe de valor na tabela de partidas para tratar o estorno quando da integração do Educacional com Módulo Contábil do Protheus.

Arquivo: RM.Ctb.Lan.Service.dll

## 11.83.55.176

* **[Ticket: 07\TTCK82]** Com objetivo de auxiliar nesta solução disponibilizamos nos parâmetros do sistema (Rotinas Legais/SPED Contábil) uma opção que identifica o C. Custo que o sistema preencherá nas movimentações das Contas Contábeis que estiver no cenário relatado acima.

Arquivos: RM.Ctb.Sped.Service.dll, RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.Parametros.Form.dll, RM.Ctb.Parametros.Intf.dll

## 11.83.55.178

* **[Ticket: 07\TTEMPC]** Com objetivo de auxiliar nesta solução disponibilizamos nos parâmetros do sistema (Rotinas Legais/SPED Contábil) uma opção que identifica o C. Custo que o sistema preencherá nas movimentações das Contas Contábeis que estiver no cenário relatado acima.

Arquivos: RM.Ctb.Sped.Service.dll, RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TTGAPH]** Na geração do Y540, quando a Qualificação da PJ for “PJ Componente do Sistema Financeiro” E a Forma de Tributação for “Lucro Real” E a Forma de Apuração for “Anual”, o sistema não esta identificando conta referencial “3.1.7.1.0.00.00”.

Arquivos: RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TTGAPH]** Ajuste no processamento do registro M310/M360 da ECF para que as informações não sejam agrupadas no módulo contábil, pois serão tratadas pelo módulo fiscal.

Arquivo: RM.Ctb.ECF.Service.dll

## 11.83.55.179

* **[Ticket: 07\TTDKH3]** Tratamento no processamento da ECF para contemplar cisão

Arquivos: RM.Ctb.Sped.Data.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.IService.dll

## 11.83.55.180

* **[Ticket: 07\TTERU4]** Evolução na ECF para que o registro nK355 seja gerado mesmo quando não for identificado movimentação para nenhuma conta de resultado.

Arquivos: RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.IService.dll

## 11.83.55.182

* **[Ticket: 07\TTFXXF]** Ao gerar os Lançamentos classificados como SPEDFCONT não estavam sendo desconsiderados

Arquivo: RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TTFXXF]** Adequação do processamento da ECF para desconsiderar os lançamentos do FCONT.

Arquivo: RM.Ctb.ECF.Service.dll

## 11.83.55.185

* **[Ticket: 07\TTMKVO]** Alteração no serviço disponibilizado pelo contábil onde o vínculo com a tabela DLAFCTB será realizado na mesma transação da inserção da contabilização.

Arquivos: RM.Ctb.Lan.Intf.dll, RM.Ctb.Lan.Data.dll, RM.Ctb.Lan.Service.dll, RM.Ctb.Lan.IService.dll, RM.Ctb.Lan.Form.dll

## 11.83.55.220

* **[Ticket: 07\TUMDMX]** Ajustado o módulo de integração de lote em uma nova coligada para que crie a referência do lançamento na tabela GAUTOINC quando não existir.

Arquivo: RM.Ctb.Lan.Service.dll

## 11.83.55.222

* **[Ticket: 07\TUOUH9]** Implementação do layout 4.0 do SPED Contábil

Arquivos: RM.Ctb.Lib.dll, RM.Ctb.Lan.Intf.dll, RM.Ctb.DemonstracaoContabil.Intf.dll, RM.Ctb.Lan.Form.dll, RM.Ctb.DemonstracaoContabil.Service.dll, RM.Ctb.Utils.Intf.dll, RM.Ctb.Parametros.Intf.dll, RM.Ctb.DemonstracaoContabil.Data.dll, RM.Ctb.Sped.Data.dll, RM.Ctb.Contas.Data.dll, RM.Ctb.Lan.Service.dll, RM.Ctb.DemonstracaoContabil.Form.dll, RM.Ctb.Contas.Form.dll, RM.Ctb.Contas.Intf.dll, RM.Ctb.dll, RM.Contabilidade.exe, RM.Ctb.Sped.Form.dll, RM.Ctb.Lan.Data.dll, RM.Ctb.Sped.Intf.dll, RM.Ctb.Lan.IService.dll, RM.Ctb.Sped.Service.dll, RM.Ctb.DemonstracaoContabil.IService.dll

* **[Ticket: 07\TUPFJQ]** Implementação SPED Contábil layout 4.0

Arquivos: RM.Ctb.Sped.Data.dll, RM.Ctb.Sped.Intf.dll, RM.Ctb.Sped.Form.dll, RM.Ctb.DemonstracaoContabil.Form.dll

* **[Ticket: 07\TUPFJQ]** Implementação do processo de importação Razão Auxiliar de Subcontas.

Arquivos: RM.Ctb.Sped.Form.dll, RM.Ctb.Sped.Intf.dll, RM.Ctb.Lan.IService.dll, RM.Ctb.Sped.Data.dll, RM.Ctb.dll

## 11.83.55.226

* **[Ticket: 07\TUUKEN]** Ajuste no cadastro de estrutura do LALUR para que seja possível cadastrar uma capa de parametrização que não obrigue o preenchimento de máscara.

Arquivos: RM.Ctb.Lib.Server.dll, RM.Ctb.Lib.WinForms.dll, RM.Ctb.Contas.Data.dll, RM.Ctb.Contas.Form.dll

## 11.83.55.227

* **[Ticket: 07\TURF22]** Identificamos um cenário em que o campo “nível” do registro J150 para fatos contábeis do tipo analítico totalizador tem que ser inferior quando para este fato contábil não existi nenhum fato contábil sintético no mesmo nível. Se não é apresentado o seguinte erro no PVA “Na DRE, a soma das parcelas deverá ser igual aos totais e subtotais.”

Arquivo: RM.Ctb.Sped.Service.dll

* **[Ticket: 07\TUSTV1]** Melhoria na tela do sped contábil para que os campos complementares comuns ao layout 3.0 e 4.0 não apresente a versão 3.0 no topo da tela e desta forma não gere dúvidas no usuário.

Arquivo: RM.Ctb.Sped.Form.dll

## 11.83.55.228

* **[Ticket: 07\TUUZ12]** Ajuste no processo de importação do controle do plano de contas anterior através do arquivo do SPED Contábil, pois podem existir informações ao final do arquivo do SPED Contábil que não esteja no padrão dos registros e sistema não está tratando.

Arquivo: RM.Ctb.Sped.Data.dll

* **[Ticket: 07\TUSUGF]** Ajuste no processamento do registro J150 do SPED Contábil em função do saldo do período anterior que estava sendo gerado inconsistente.

Arquivo: RM.Ctb.Sped.Service.dll

## 11.83.55.229

* **[Ticket: 07\TUYOF6]** Ajuste no processamento do registro J100 do SPED contábil quando é apuração trimestral, pois o saldo inicial não estava acumulando corretamente.

Arquivos: RM.Ctb.Sped.Form.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.Sped.Data.dll, RM.Ctb.Sped.Service.dll, RM.Ctb.Sped.Intf.dll

## 11.83.55.231

* **[Ticket: 07\TUXIU0]** Evlução na ECF para gerar o registro K156 e K356 para atender a ECF no TAF

Arquivos: RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TUXIU0]** Replicando implementação registro Y671, Y672 e X390 para versão 11.83.55

Arquivos: RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.Intf.dll, RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Form.dll, RM.Ctb.Parametros.Intf.dll, RM.Ctb.ECF.Data.dll, RM.Ctb.DemonstracaoContabil.Intf.dll, RM.Ctb.DemonstracaoContabil.Service.dll, RM.Ctb.DemonstracaoContabil.Form.dll, RM.Ctb.DemonstracaoContabil.Data.dll, RM.Ctb.DemonstracaoContabil.IService.dll

* **[Ticket: 07\TUXIU0]** Implementação do registro Y665 da ECF

Arquivos: RM.Ctb.Sped.Data.dll, RM.Ctb.Contas.Form.dll, RM.Ctb.ECF.Data.dll, RM.Ctb.Contas.Data.dll, RM.Ctb.ECF.Intf.dll, RM.Ctb.Contas.Intf.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.IService.dll, RM.Ctb.Sped.Service.dll, RM.Ctb.ECF.Form.dll, RM.Ctb.Parametros.Intf.dll, RM.Ctb.Sped.Intf.dll

* **[Ticket: 07\TUXIU0]** Evolução no processamento do registro M310/M360 para identificar no registro o código da natureza da conta conforme a emissão do SPED (registro J050), pois esta informação será utilizada pelo TOTVS Gestão Fiscal para aplicar regras especificas.

Arquivos: RM.Ctb.ECF.Intf.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.Data.dll, RM.Ctb.ECF.IService.dll

* **[Ticket: 07\TUXIU0]** Ao gerar a ECF durante o processamento do registro K355 o sistema não esta considerando os encerramentos provenientes do histórico padrão informados manualmente nas parametrizações da ECF do nódulo contábil.

Arquivos: RM.Ctb.ECF.IService.dll, RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TUXIU0]** Ajustes ECF registr K155

Arquivos: RM.Ctb.ECF.Service.dll, RM.Ctb.ECF.IService.dll

## 11.83.55.233

* **[Ticket: 07\TVAGW1]** Implementação do processo de preenchimento do centro de custo nas movimentações em função da regra do SPED/ECF.

Arquivos: RM.Ctb.dll, RM.Ctb.ConsisteLancamento.Intf.dll, RM.Ctb.ECF.IService.dll, RM.Ctb.ConsisteLancamento.Form.dll, RM.Ctb.Parametros.Form.dll, RM.Ctb.Contas.Data.dll, RM.Ctb.ConsisteLancamento.Service.dll, RM.Ctb.Contas.Intf.dll, RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TVAXQE]** Implementação do processo de preenchimento do centro de custo nas movimentações em função da regra do SPED/ECF.

Arquivos: RM.Ctb.ConsisteLancamento.Service.dll, RM.Ctb.ECF.Service.dll

## 11.83.55.234

* **[Ticket: 07\TVAXQE]** Implementação do processo de preenchimento do centro de custo nas movimentações em função da regra do SPED/ECF.

Arquivos: RM.Ctb.ConsisteLancamento.Form.dll, RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TUXFNH]** Implementação do registro Y665

Arquivo: RM.Ctb.ECF.Service.dll

* **[Ticket: 07\TUVTD9]** Implementação do registro T124 para a ECF no TAF

Arquivo: RM.Ctb.ECF.Service.dll

## 11.83.55.235

* **[Ticket: 07\TUUOF8]** Evolução no SPED Contábil / ECF para atender ao decreto nº 8.683/2016, determina que o plano de contas transmitido para o Sped junto com os Livros Diários e Auxiliares, e com os documentos da Escrituração Contábil Digital, contenha apenas contas que tenham saldo ou sido movimentadas no período.

Arquivos: RM.Ctb.Sped.Service.dll, RM.Ctb.Sped.Data.dll, RM.Ctb.ECF.Service.dll, RM.Ctb.Sped.Form.dll, RM.Ctb.Parametros.Form.dll, RM.Ctb.ConsisteLancamento.Intf.dll, RM.Ctb.ECF.IService.dll, RM.Ctb.Parametros.Intf.dll

## 11.83.55.243

* **[Ticket: 07\TVHTQ3]** \* Atualização do Evento Contábil referente seleção ao item contábil e classe de valor relativo à integração Protheus

Arquivo: RM.Ctb.Lib.dll

# TOTVS Gestão de Estoques, Compras e Faturamento

## 11.83.55.100

* **[Ticket: 07\TRANXR]** Melhorias no processo responsável por corrigir movimentos com status = "Em faturamento"

Arquivo: RM.Mov.Processos.Form.dll

* **[Ticket: 07\TQYEE4]** Ajuste ao abrir o QCP, não era maximizado.

Arquivo: RM.Mov.Orcamento.Data.dll

## 11.83.55.104

* **[Ticket: 07\TQZYK3]** Legislação - Lei da Transparência

Arquivos: RM.Mov.Movimento.Form.dll, RM.Mov.Movimento.IService.dll, RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Movimento.Intf.dll

## 11.83.55.110

* **[Ticket: 07\TREZFG]** Ajuste no cálculo do Valor Total do Tributos - Tabela IBPTax.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.111

* **[Ticket: 07\TRFSOX]** Melhorias no processo de cálculo dos tributos.

Arquivo: RM.Mov.Movimento.Form.dll

## 11.83.55.115

* **[Ticket: 07\TREHRI]** Melhorias na regeração de saldos e custos

Arquivos: RM.Est.Estoque.Service.dll, RM.Est.Processos.Data.dll

## 11.83.55.116

* **[Ticket: 07\TRFDBY]** Melhoria no cadastro de produtos

Arquivo: RM.Est.Produto.Service.dll

## 11.83.55.118

* **[Ticket: 07\TRIYJY]** Ajuste nos valores de rateio de centro de custo no faturamento de contrato quando parametrizado por valor.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.119

* **[Ticket: 07\TRHCB6]** Melhoria no processo de tradução de idiomas.

Arquivos: RM.Est.Cadastros.Form.dll, RM.Mov.Cadastros.Form.dll

* **[Ticket: 07\TQZSPX]** Resolvida inconsistência na exclusão de produtos.. Ao excluir um produto com vínculo com SigaMNT, o sistema gerava a seguinte mensagem:"Fórmula Visual: '05.Mensagem Única - Item (Produto)'.Erro na execução da Atividade: 'movProdutoIntegradoProtheus1'Erro: Informações sobre a linha excluída não podem ser acessadas através da linha."

Arquivo: RM.Mov.FormulaVisual.Activities.dll

* **[Ticket: 07\TRMGFJ]** ajuste na mascara parametrizada para o lookup de produto

Arquivos: RM.Est.Produto.Data.dll, RM.Est.Processos.Form.dll

## 11.83.55.120

* **[Ticket: 07\TRGAFW]** Melhoria no processo de integração de Ordens de Serviço e Movimentação.

Arquivos: RM.Mov.CopiaMovimento.Service.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Movimento.Data.dll

## 11.83.55.121

* **[Ticket: 07\TRHUFH]** Ajuste na Conversão de unidade ao gerar Sugestão de Compra.

Arquivos: RM.Est.Parametros.Intf.dll, RM.Est.Ressuprimento.Service.dll

* **[Ticket: 07\TRIVTU]** Inclusão do campo codigoNBS no cadastro de produtos

Arquivos: RM.Est.Produto.IService.dll, RM.Est.Exportacao.Service.dll, RM.Est.Produto.Data.dll, RM.Est.Produto.Intf.dll, RM.Est.Produto.Service.dll, RM.Est.Produto.Form.dll

## 11.83.55.123

* **[Ticket: 07\TRPPE6]** Ajuste no parametrizador tabela de classificação de itens.

Arquivo: RM.Mov.Parametros.Data.dll

## 11.83.55.126

* **[Ticket: 07\TRHUKU]** Melhoria no processo de Análise de Ressuprimento para não mostrar informações de outras coligadas.

Arquivo: RM.Est.Ressuprimento.Data.dll

## 11.83.55.127

* **[Ticket: Alterações Gerais]** Alteração no Evento Contábil Educacional x Protheus (CNI)

Arquivos: RM.Mov.Facade.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Movimento.IService.dll

## 11.83.55.128

* **[Ticket: 07\TRSIB0]** Melhorias nas consistências do movimento.

Arquivo: RM.Mov.Parametros.Data.dll

## 11.83.55.131

* **[Ticket: 07\TRUDUX]** Melhorias no processo de cálculo dos tributos.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.136

* **[Ticket: 07\TRWZZX]** Melhorias na integração entre RMNucleus x RMLiber.

Arquivos: RM.Est.Estoque.Service.dll, RM.Est.Estoque.IService.dll, RM.Est.Consts.dll

## 11.83.55.137

* **[Ticket: 07\TRRTFC]** Foi modificado o processo de emissão da NF-e para atender a legislção da NF-e 3.10

Arquivos: RM.Mov.Movimento.IService.dll, RM.Mov.Movimento.Intf.dll, RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Movimento.Form.dll

* **[Ticket: 07\TRWNYT]** Melhoria no processo de baixa de pedido de pagamento.

Arquivo: RM.Mov.FormulaVisual.Activities.dll

## 11.83.55.138

* **[Ticket: 07\TRXSUN]** Melhoria no processo de cadastro de movimento utilizando via de transporte.

Arquivos: RM.Mov.Movimento.Form.dll, RM.Mov.Consts.dll

* **[Ticket: 07\TRVNXW]** Melhoria no faturamento parcial por valor.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.151

* **[Ticket: 07\TSCEF3]** Inclusão de Gatilho para Fórmula Visual

Arquivos: RM.Mov.FormulaVisual.Activities.dll, RM.Mov.Movimento.Service.dll

* **[Ticket: 07\TSEWW9]** Melhoria na parametrização de produtos.

Arquivo: RM.Est.Parametros.Data.dll

## 11.83.55.154

* **[Ticket: 07\TSCOJ3]** Ajuste no campo chave de acesso ao salvar o movimento.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.155

* **[Ticket: 07\TSKYHD]** Melhorias no parametrizador do tipo de movimento.

Arquivo: RM.Mov.Parametros.Form.dll

* **[Ticket: 07\TSKX53]** Melhorias na integração Educacional x Nucleus x Protheus

Arquivos: RM.Mov.Movimento.Service.dll, RM.Mov.Facade.dll, RM.Mov.Consts.dll

## 11.83.55.160

* **[Ticket: 07\TSPHN9]** Melhorias na integração Protheus x Educacional x Nucleus.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.161

* **[Ticket: 07\TSQFHH]** Melhorias na integração Educacional x Nucleus x Protheus

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.162

* **[Ticket: 07\TSPTMF]** Melhorias ao incluir movimento via XML no faturamento.

Arquivo: RM.Mov.Movimento.Form.dll

## 11.83.55.164

* **[Ticket: 07\TSQNGQ]** Melhorias no processo de inclusão da Cotação.

Arquivos: RM.Cmp.Cotacao.Service.dll, RM.Cmp.Cotacao.Data.dll

## 11.83.55.167

* **[Ticket: 07\TSGUDF]** Melhoria relacionada a salvar movimento de transferência entre locais de estoque.

Arquivos: RM.Mov.Movimento.Service.dll, RM.Mov.Movimento.IService.dll, RM.Mov.Facade.dll, RM.Est.Cadastros.Service.dll, RM.Est.Cadastros.IService.dll

## 11.83.55.169

* **[Ticket: 07\TSY984]** Melhorias de performance no processo responsável pelo faturamento do movimento.

Arquivo: RM.Mov.Faturamento.Form.dll

* **[Ticket: 07\TSIAXB]** Melhorias ao regerar saldos e custos

Arquivo: RM.Est.Estoque.Service.dll

* **[Ticket: 07\TSSZQ5]** Modificado verificação do tipo de documento associado ao movimento e sendo esse movimento do tipo NFC-e passa a ser exibido a página "NFC-e (Consumidor)" entre as integrações, nessa página é informado "Chave de acesso do NFC-e".

Arquivos: RM.Mov.Movimento.Form.dll, RM.Mov.Movimento.Service.dll

## 11.83.55.173

* **[Ticket: 07\TSVWI9]** Melhorias no processo responsável por sincronisar documentos do MD-e.

Arquivos: RM.Mov.Integracoes.Data.dll, RM.Mov.Integracoes.Intf.dll, RM.Mov.Integracoes.Service.dll, RM.Fis.TSS.Service.dll

## 11.83.55.177

* **[Ticket: 07\TTEDZ2]** Melhoria no processo de importação de xml

Arquivos: RM.Mov.Utils.Intf.dll, RM.Mov.Integracoes.Service.dll

## 11.83.55.182

* **[Ticket: 07\TTFRQ1]** Disponibilizado serviço entre os módulos para consultar movimentos de origem através do relacionamento gerado por Cópia por Referência ou Faturamento vinculados a devolução ou retorno de devolução.

Arquivos: RM.Mov.Movimento.IService.dll, RM.Mov.Movimento.Service.dll

## 11.83.55.183

* **[Ticket: 07\TTJEHF]** Melhorias ao incluir XML de Cte

Arquivo: RM.Mov.Utils.Intf.dll

* **[Ticket: 07\TSNR99]** Ajuste no serviço entre os módulos para consultar movimentos de origem através do relacionamento gerado por Cópia por Referência de ESTORNO.

Arquivo: RM.Mov.Movimento.Service.dll

* **[Ticket: 07\TTJEHF]** Melhorias ao cadastrar XML Totvs Colaboração

Arquivos: RM.Mov.Integracoes.Form.dll, RM.Mov.Utils.Intf.dll

## 11.83.55.184

* **[Ticket: 07\TTMERF]** Inclusão de campo para informação do Código Enquadramento IPI para tributo do Item de Movimento.

Arquivos: RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Form.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Movimento.Intf.dll, RM.Mov.Movimento.IService.dll

* **[Ticket: 07\TTJXR3]** Melhorias ao excluir fornecedor da cotação.

Arquivo: RM.Cmp.Cotacao.Data.dll

## 11.83.55.186

* **[Ticket: 07\TTOCEK]** Ajuste no serviço para consulta de movimento origem pelo relacionamento gerado por Cópia por Referência (NF Complementar).

Arquivo: RM.Mov.Movimento.Service.dll

* **[Ticket: 07\TTMEHX]** Ajuste para que o sistema considere corretamente o formato do relatório definido no Tipo de Movimento etapa “Fis – Conhecimento de Transporte” (1: Retrato; 2: Paisagem).

Arquivo: RM.Mov.CTe.Service.dll

## 11.83.55.187

* **[Ticket: 07\TTMAUL]** Inclusão de campo para informar percentual de perda no cadastro de Componentes da Estrutura.

Arquivos: RM.Est.Cadastros.Form.dll, RM.Est.Estoque.Service.dll, RM.Est.Estoque.IService.dll, RM.Est.Cadastros.Data.dll, RM.Est.Cadastros.Intf.dll

## 11.83.55.188

* **[Ticket: 07\TTLEWW]** Foram acrescentadas as permissões de aprovação por workflow e alterar movimentos em aprovação por workflow para requisição de serviços de gestão de compras.

Arquivos: RM.Est.dll, RM.Mov.Movimento.Service.dll

* **[Ticket: 07\TTJSC5]** Melhorias ao incluir movimento via XML

Arquivos: RM.Mov.Integracoes.Form.dll, RM.Mov.Integracoes.Data.dll, RM.Mov.Movimento.Form.dll, RM.Mov.Integracoes.Intf.dll, RM.Mov.Integracoes.Service.dll

* **[Ticket: 07\TTKXOX]** Consistência no faturamento de movimento de Ordem de Produção (Produção Simples) com apenas um item para permitir a edição de itens no movimento de Baixa de Matéria Prima (Produção Simples).

Arquivos: RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Service.dll

* **[Ticket: 07\TTQNOX]** Inclusão da Baixa de Lançamento ao incluir movimento via Web Service.

Arquivo: RM.Mov.Movimento.Data.dll

* **[Ticket: Alterações Gerais]** Inclusão da Baixa de Lançamento ao incluir movimento via Web Service.

Arquivo: RM.Mov.Movimento.Data.dll

## 11.83.55.190

* **[Ticket: 07\TTPLHX]** Melhorias ao importar movimento via XML.

Arquivos: RM.Mov.Integracoes.Intf.dll, RM.Mov.Integracoes.Form.dll, RM.Mov.Integracoes.Service.dll

* **[Ticket: 07\TTJYU9]** Melhoria no processo de aprovação de movimentos por WorkFlow

Arquivo: RM.Mov.Movimento.Service.dll

* **[Ticket: 07\TTS982]** Foi realizado downgrade do metódo 'HaMovimentacoesFechamentoEstoque' da versão 11.82.41 para atender uma demanda da Comau.

Arquivos: RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Intf.dll

## 11.83.55.191

* **[Ticket: 07\TTSXK6]** Foi realizado uma melhoria ao concluir o movimento para preencher o Valor Concluído.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.194

* **[Ticket: 07\TTW011]** Melhoria no serviço "ListaMovimentosRelacionados" utilizado pelo RMLiber.

Arquivos: RM.Mov.Movimento.IService.dll, RM.Mov.Movimento.Service.dll

* **[Ticket: 07\TUBEV4]** Melhorias ao faturar contrato

Arquivo: RM.Ctr.Faturamento.Form.dll

## 11.83.55.197

* **[Ticket: 07\TTCZ75]** Melhorias na inclusão de movimento.

Arquivo: RM.Est.Baixa.Service.dll

## 11.83.55.199

* **[Ticket: 07\TTVNA1]** Melhorias na regeração de saldos e custos

Arquivo: RM.Est.Estoque.Service.dll

## 11.83.55.204

* **[Ticket: 07\TUBIH9]** Removida validação de integração com Bonum ao reabrir financeiro de um movimento.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.208

* **[Ticket: 07\TTZXAR]** Realizada melhorias de legislação do produto.. Implementação de parâmetro fórmula para a lei de transparência fiscal.

Arquivos: RM.Mov.Parametros.Intf.dll, RM.Mov.Parametros.Form.dll, RM.Mov.Formula.dll, RM.Mov.Parametros.Data.dll, RM.Mov.Movimento.Service.dll

## 11.83.55.211

* **[Ticket: 07\TUGUAW]** Melhorias ao incluir movimento.

Arquivo: RM.Est.Baixa.Service.dll

## 11.83.55.212

* **[Ticket: 07\TUHO36]** Melhoria no processo "Gerar financeiro" para movimentos agrupados calculando corretamente o valor da base de cálculo do tributo do item do movimento.

Arquivo: RM.Mov.Movimento.Service.dll

## 11.83.55.217

* **[Ticket: 07\TRSGEY]** Legislação - Habilitar campo Procedência no Item de Movimento quando for Movimento de Entrada e Cliente Optante pelo Simples.

Arquivo: RM.Mov.Movimento.Form.dll

## 11.83.55.220

* **[Ticket: 07\TULI91]** Legislação - Inclusão do cálculo da Base de Cálculo do ICMS Diferencial de alíquota que afeta Movimento, NF-e, Escrituração e Lançamento Fiscal

Arquivos: RM.Mov.Facade.dll, RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Service.dll

## 11.83.55.221

* **[Ticket: 07\TUNIDL]** Melhoria para agrupamento de Município + UF para dados de Carga.

Arquivo: RM.Mov.CTe.Service.dll

## 11.83.55.224

* **[Ticket: 07\TUPQVH]** Agora, o acionar o processo faturar/receber pelo atalho "Receber", as regras do fluxo de atendimento genérico serão levadas em consideração normalmente.

Arquivos: RM.Mov.Processos.Data.dll, RM.Mov.Integracoes.Data.dll, RM.Mov.Faturamento.Data.dll

## 11.83.55.225

* **[Ticket: 07\TUKJ91]** Melhoria para atualizar diferimento de ICMS ao se alterar a natureza do mMovimento

Arquivos: RM.Mov.Movimento.Intf.dll, RM.Mov.Facade.dll, RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Form.dll

* **[Ticket: 07\TUSO71]** Melhoria no parametrizador do ressuprimento para um local de estoque recém cadastro que poderia falhar ao carregar parametrizador para esse local.

Arquivos: RM.Est.Parametros.Data.dll, RM.Est.Ressuprimento.Service.dll

## 11.83.55.229

* **[Ticket: 07\TUGSZB]** Melhoria para permitir que a fórmula do histórico afete os campos de Informações Adicionais do Fisco e Informações do Contribuinte.

Arquivos: RM.Mov.Movimento.Service.dll, RM.Mov.Consts.dll, RM.Mov.Parametros.Data.dll, RM.Mov.Parametros.Intf.dll, RM.Mov.Parametros.Form.dll

## 11.83.55.233

* **[Ticket: 07\TUUFBQ]** Legislação - Implementação do veiculo de reboque no MDF-e

Arquivo: RM.Mov.CTe.Service.dll

## 11.83.55.238

* **[Ticket: 07\TVDZV4]** Foi realizado uma alteração na leitura dos parâmetros devido a base de dados Oracle tratar os valores de forma diferente do SQLServer.

Arquivo: RM.Ctr.Parametros.Data.dll

## 11.83.55.239

* **[Ticket: 07\TUZMVX]** Melhoria para atualizar o código de enquadramento do IPI aautomaticamente ao se alterar a Natureza(desde que o mesmo esteja parametrizado)

Arquivos: RM.Mov.Movimento.Form.dll, RM.Mov.Movimento.Data.dll, RM.Mov.Facade.dll, RM.Mov.Movimento.Intf.dll

## 11.83.55.249

* **[Ticket: 07\TVM505]** Melhorias no processo de inclusão de movimento através de XML.

Arquivo: RM.Mov.Movimento.Form.dll

# TOTVS Gestão de Pessoas

## 11.83.55.122

* **[Ticket: 07\TRDLSI]** Otimização nos dados de Óbito do cadastro de Pessoas. Sistema salva o registro após a data de óbito ser preenchida e desabilita o botão salvar logo após o salvamento.

Arquivo: RM.Rhu.Lib.WinForms.dll

## 11.83.55.123

* **[Ticket: 07\TRPDGR]** Reestruturação em visão de requisição de Substituição.

Arquivo: RM.Rhu.Requisicao.Server.dll

## 11.83.55.125

* **[Ticket: 07\TRQUQ1]** Reestruturação em aprovação de requisição de Alteração de Dados Funcionais.

Arquivos: Portal Corpore.Net

## 11.83.55.127

* **[Ticket: 07\TRSIO9]** Reestruturação em validação do controle de lotação.

Arquivo: RM.Rhu.Funcionario.Data.dll

## 11.83.55.129

* **[Ticket: 07\TRSO15]** Reestruturação em exclusão de Histórico de Benefícios Lançados aos Dependentes.

Arquivos: RM.Rhu.Beneficios.Data.dll, RM.Rhu.Beneficios.Intf.dll

## 11.83.55.130

* **[Ticket: 07\TRUJVG]** Aprimorada a apresentação das requisições de substituição no Portal.

Arquivo: RM.Rhu.Requisicao.Server.dll

## 11.83.55.134

* **[Ticket: 07\TRVCP5]** Otimização no anexo Avaliação de Qualidade, no cadastro de Turmas. O campo "Prova do RM Testis" passa a trazer somente provas da coligada corrente.

Arquivo: RM.Rhu.Turmas.Form.dll

## 11.83.55.150

* **[Ticket: 07\TRYBUW]** Realizado ajuste em Cursos Pessoais para que o mesmo fique concluído quando a turma cadastrada for encerrada e estiver com data de início e data de fim preenchidas.

Arquivo: RM.Rhu.Turmas.Server.dll

## 11.83.55.152

* **[Ticket: 07\TSHLNQ]** Melhoria ao iniciar o processo de seleção

Arquivo: RM.Rhu.Captacao.Data.dll

## 11.83.55.153

* **[Ticket: 07\TSHLNQ]** Melhoria ao iniciar o processo de seleção

Arquivo: RM.Rhu.Captacao.Data.dll

## 11.83.55.158

* **[Ticket: 07\TSMWKF]** Melhoria nas labels da grid de Candidatos por Etapa de Etapas da Seleção

Arquivo: RM.Rhu.Captacao.Data.dll

## 11.83.55.159

* **[Ticket: 07\TSMWGJ]** Ajuste no Início de um Processo de Seleção. A Triagem não estava sendo considerada e todos os candidatos estavam sendo trazidos.

Arquivo: RM.Rhu.Captacao.Data.dll

## 11.83.55.160

* **[Ticket: 07\TSMWYR]** Otimização no processo "Iniciar Processo de Seleção". Quando um processo de seleção é reiniciado, o usuário tem as opções de substituir todos os candidatos já incluídos na seleção por novos candidatos encontrados na nova triagem ou reiniciar o processo sem nenhum candidato.

Arquivos: RM.Rhu.Captacao.Form.dll, RM.Rhu.Captacao.Data.dll

## 11.83.55.161

* **[Ticket: 07\TSMWR5]** Adequação aplicada para que não seja passado valor o valor do código da seleção para o campo código da etapa no painel de seleção.

Arquivo: RM.Rhu.Captacao.Form.dll

* **[Ticket: 07\TSPNRZ]** Otimização no processo "Recuperar Resultados do Testis", do anexo "Candidatos da Etapa", no Painel de Seleção. O processo é executado corretamente.

Arquivo: RM.Rhu.Captacao.Data.dll

## 11.83.55.162

* **[Ticket: 07\TSNUOZ]** Realizada melhoria no cadastro de questionários para que o usuário possa informar a ordem em que as perguntas serão exibidas no Currículo Web. As perguntas no currículo web serão ordenadas primeiramente pelo novo campo "Ordem", caso o mesmo não esteja preenchido será ordenado então pelo código da pergunta.

Arquivos: RM.Rhu.Captacao.Data.dll, RM.Rhu.Captacao.Form.dll, RM.Rhu.Captacao.Intf.dll, RM.Rhu.Curriculo.Server.dll

## 11.83.55.163

* **[Ticket: 07\TSLPGQ]** Ajustes nos processos de mudança de status para concluído e reiniciado, de forma que ao concluir a data de fechamento seja preenchida com a data do processamento e ao reiniciar uma etapa caso a data de fechamento esteja preenchida a mesma seja removida.

Arquivo: RM.Rhu.Captacao.Data.dll

## 11.83.55.166

### Rotina: eSocial

* **[Ticket: PCREQ-3579]** Adequação minuta 2.0 esocial 4ª Entrega

Arquivos: RM.Rhu.ProcessosJuridicos.Form.dll, RM.Rhu.Lib.WinForms.dll, RM.Rhu.ProcessosJuridicos.Data.dll, RM.Rhu.Pessoa.Intf.dll, RM.Rhu.Pessoa.Data.dll, RM.Rhu.ProcessosJuridicos.Intf.dll

## 11.83.55.168

* **[Ticket: 07\TSPWMM]** Foram realizadas adequações na busca de dados da integração com o Agilis para as Requisições.

Arquivo: RM.Rhu.Requisicao.Server.dll

## 11.83.55.171

* **[Ticket: 07\TSZLBO]** Ajuste em geração de relatório de dados pessoais do candidato da etapa para coligada global.

Arquivo: RM.Rhu.Lib.WinForms.dll

* **[Ticket: 07\TSZKHN]** Melhoria no cadastro de Triagem ao salvar palavras-chave

Arquivo: RM.Rhu.Captacao.Data.dll

## 11.83.55.174

* **[Ticket: 07\TTBEOB]** Alteração de obrigatoriedade do campo Requisições do perfil de vaga

Arquivo: RM.Rhu.Captacao.Intf.dll

## 11.83.55.184

* **[Ticket: 07\TTCVHX]** Ajuste em processo "Criar Atendentes do Agilis" para que o usuário possa informar a "Localidade" e a "Hierarquia".

Arquivos: RM.Rhu.AtendenteAgilis.Intf.dll, RM.Rhu.AtendenteAgilis.Data.dll, RM.Rhu.AtendenteAgilis.Form.dll

* **[Ticket: 07\TTAPUJ]** Otimizada a carga de solicitações de requisitos.

Arquivo: RM.Rhu.Competencia.Data.dll

## 11.83.55.192

* **[Ticket: 07\TQQORD]** Ajuste para o educacional.

Arquivo: RM.Rhu.Lib.WinForms.dll

## 11.83.55.224

* **[Ticket: 07\TUCEL2]** Ajuste no Portal, ao anexar um novo Currículo no Banco de Talentos. Ao clicar no link, a tela de seleção do arquivo é aberta.

Arquivos: Portal Corpore.Net

## 11.83.55.230

* **[Ticket: 07\TURUBQ]** Ajuste no processo de unificar pessoas quando existe vínculo com Alunos.

Arquivos: RM.Rhu.Pessoa.Data.dll, RM.Rhu.Utils.Server.dll

## 11.83.55.233

* **[Ticket: 07\TUUIEO]** Ajuste no acesso à requisições de treinamento no portal.

Arquivos: Portal Corpore.Net

## 11.83.55.238

* **[Ticket: 07\TVAITS]** Realizada tratativa na carga do dos dados da pessoa para que sejam removidos os caracteres não numéricos.

Arquivos: RM.Rhu.Cadastros.Data.dll, RM.Rhu.Pessoa.Intf.dll, RM.Rhu.Pessoa.Data.dll

## 11.83.55.241

* **[Ticket: 07\TURUBQ]** Realizado ajuste no processo de Unificação de Pessoas, afim de que mesmo tendo registros no Educacional, seja possível unificar as pessoas mantendo a integridade dos dados.

Arquivos: RM.Rhu.Pessoa.Data.dll, RM.Rhu.Utils.Server.dll

## 11.83.55.248

* **[Ticket: 07\TVMJLA]** Realizado ajuste para visualizar a hierarquia na criação de atendentes do Agilis.

Arquivos: RM.Rhu.Lib.Server.dll, RM.Rhu.AtendenteAgilis.Form.dll

## 11.83.55.251

* **[Ticket: 07\TVMYBL]** Acertada a mascara do campo CEP.

Arquivo: RM.Rhu.Lib.WinForms.dll

## 11.83.55.281

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 584574 / FOPROTINAS01-370]** Ajuste no acesso do aluno ao portal para não visualizar menu de Recursos Humanos

Arquivo: RM.Rhu.Beneficios.WebForm.dll

## 11.83.55.305

### Rotina: ATENDIMENTO ESPECIFICO CUSTOMIZACAO

* **[Ticket: 1458003 / RHU01-1614]** Corrigido dropdown de País para endereço principal. Agora na criação ao preencher um dropdown com o nome do País o código do país é preenchindo corretamente.

Arquivo: RM.Rhu.Lib.WinForms.dll

# TOTVS Gestão do Relacionamento com o Cliente

## 11.83.55.127

* **[Ticket: 07\TRNGCO]** Ajuste para que não haja inconscistência ao usar um parâmetro do tipo de atendimento baseado em uma sentença sql que use um campo do atendimento como parâmetro no cliente online

Arquivo: App\_Web\_crmclienteonlineedicao.ascx.72e19a66.dll

## 11.83.55.145

* **[Ticket: 07\TSCBK5]** Agora o botão para alterar o arquivo anexo a um atendimento, está se submetendo a regra de acesso a campos pelo perfil

Arquivo: RM.CRM.Atendimento.Form.dll

## 11.83.55.158

* **[Ticket: 07\TSHFTD]** Melhoria de performance ao executar algum processo com vários registros que usem o fluxo de atendimento genêrico do agilis

Arquivo: RM.CRM.TipoAtendimento.Data.dll

* **[Ticket: Alterações Gerais]** Ajuste de layout de tela de processo

Arquivos: RM.CRM.TipoAtendimento.Form.dll, RM.CRM.TipoAtendimento.Data.dll

## 11.83.55.178

* **[Ticket: 07\TTFPZG]** O campo do tipo data deve ser formatado adequadamente para que possa ser executado sem inconsistência.

Arquivo: RM.CRM.TipoAtendimento.Data.dll

## 11.83.55.249

* **[Ticket: 07\TVOWI9]** Ao adicionar vário registros em um parâmetro do tipo tabela, usando o botão "Seleção de registro", todos serão salvos normalmente.

Arquivo: RM.CRM.Lib.Form.dll

## 11.83.55.282

### Rotina: Project-806712 Itens de Permissão de Menu - AGILIS Project-806712

* **[Ticket: 810655 / MATFATCMPCRM01-349]** Tag de segurança do grupo de pesquisa de satisfação, estava igual a do grupo de atendente, isso fazia com que os itens desse grupo no gerenciador de acesso a menus do perfil, fossem exibidos em posições inadequadas.

Arquivo: RM.CRM.dll

## 11.83.55.306

### Rotina: CRM - Project-1332405 Erro no Portal CRM Project-1332405

* **[Ticket: 1341932 / TOPEXECONTROL01-1048]** Agora, quando o usuário do cliente online inclui um atendimento em uma coligada diferente do atendente definidos nos parâmetros do cliente online, o sistema inclui o atendimento normalmente.

Arquivo: RM.CRM.ClienteOnline.Data.dll

# TOTVS Gestão Estratégica

## 11.83.55.301

### Rotina: Project-1303198 Erro ao gerar Cubo (#1209650) Project-1303198

* **[Ticket: 1315408 / DFRWBI-322]** Melhoria na exibição de mensagem sobre o tamanho do cubo para que seja exibida como um alerta.

Arquivo: RM.Bis.Cubo.Form.dll

# TOTVS Gestão Financeira

## 11.83.55.108

* **[Ticket: 07\TRCRP7]** Na inclusão de boleto bancário se o convênio do lançamento estiver parametrizado para usar a referência do boleto como tipo de nosso número, o sistema apresenta mensagem indevida.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.109

* **[Ticket: 07\TQZBP6]** Correção do processo de envio de e-mail. O sistema ao perceber que iria enviar um e-mail para um destinatario como "teste@teste.com.br;" com o ';' no final, ele entendia que tinha outro e-mail para ser enviado depois do "teste@teste.com.br" por causa do ';' (ponto e virgula). Agora o sistema valida se depois do ';' possui um e-mail para depois poder ser enviado.

Arquivo: RM.Fin.Lan.Data.dll

## 11.83.55.110

* **[Ticket: 07\TRES77]** Ajuste na baixa de lançamento do Educacional quando integração com Protheus.

Arquivos: RM.Fin.Lan.IService.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lan.Data.dll

## 11.83.55.112

* **[Ticket: 07\TRGJV0]** Melhoria na formatação das informações de Cliente/Fornecedor enviadas para integração com Mensageria Única.

Arquivo: RM.Fin.CliFor.Service.dll

## 11.83.55.115

* **[Ticket: 07\TRHSFL]** Melhoria no processo de cancelamento de lançamentos para a integração utilizando mensageria única.

Arquivos: RM.Fin.Lan.Intf.dll, RM.Fin.CliFor.Service.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lan.Data.dll

## 11.83.55.116

* **[Ticket: 07\TRAHSF]** Ajustes no conversor, no caso onde um lançamento faz referência a varios movimentos.

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 07\TRMC26]** Melhoria na geração de mensagens únicas de lançamentos a receber quando as mesmas foram geradas de faturamentos de contratos para a integração com o Educacional.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.127

* **[Ticket: 07\TRTCMI]** Melhoria no processo de envio de anexo de relatório delphi no envio de email da visão de cliente/fornecedor

Arquivo: RM.Fin.Lan.Data.dll

## 11.83.55.128

* **[Ticket: 07\TRFJHW]** Otimizado processo de baixa para retirada do código que bloqueava a tela ao recalcular o valor

Arquivo: RM.Fin.Lan.Form.dll

## 11.83.55.136

* **[Ticket: 07\TRTVYS]** Otimizado processo de baixa para que caso exista um workflow do Agilis a baixa de lançamento seja bloqueada

Arquivo: RM.Fin.Lan.Form.dll

## 11.83.55.146

* **[Ticket: 07\TSBGT5]** Alteração no processo de validação da execução do processo de cancelamento de baixa, para desconsiderar a origem da baixa "Cancelamento de Borderô".

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 07\TRZSAY]** Melhoria no processo de Retorno Bancário Cobrança. Agora o sistema registra a data de Retorno no lançamento na aba de Campos Complementares.

Arquivos: RM.Fin.Banco.Data.dll, RM.Fin.Lan.IService.dll, RM.Fin.Lan.Service.dll

* **[Ticket: Alterações Gerais]** Atualização de fluxo de caixa - integração com o Office

Arquivo: RM.Fin.FluxoCaixa.API.dll

## 11.83.55.148

* **[Ticket: 07\TSEPLO]** Melhoria na geração da mensagem de Cliente/Fornecedor para a correta interpretação da informação de CEP pelo Protheus.

Arquivo: RM.Fin.CliFor.Service.dll

## 11.83.55.152

* **[Ticket: 07\TSGG41]** Otimização sobre a geração do extrato com o extorno. Agora o sistema utiliza a Data informada no Arquivo e não pela data do sistema.

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 07\TSIKV1]** Alteração sobre a geração do extrato com o extorno. Agora o sistema utiliza a Data informada no Arquivo e não pela data do sistema.

Arquivo: RM.Fin.Banco.Data.dll

## 11.83.55.154

* **[Ticket: 07\TSIPLK]** Desabilitado a visualização das funcionalidades de Gestão de Financiamento.

Arquivo: RM.Fin.dll

* **[Ticket: 07\TSICBN]** Otimização do processo de Alteração da data de vencimendo do boleto/lançamento. Agora o sistema deixa realizar a alteração da data de vencimento se nos paramêtros do Fluxus estiver marcado a opção onde o sistema aceita inserir a data de vencimento menor que a data de emissão. Caso o paramêtro não estiver marcado, o sistema irá valida se a data de vencimento é menor que a data de emissão. Se for menor então o sistema não deixará realizar o processo de alteração e exibirá uma mensagem de erro.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.157

* **[Ticket: 07\TSLOPI]** Otimizado processo de geração de código de barras para emitir mensagem caso o layout bancário não esteja associado ao banco

Arquivo: RM.Fin.Banco.Service.dll

## 11.83.55.159

* **[Ticket: 07\TSGXYX]** Melhoria na integração para envio de item contabil, classe de valor e natureza financeira.

Arquivos: RM.Fin.Lan.IService.dll, RM.Fin.Lan.Service.dll

## 11.83.55.160

* **[Ticket: 07\TSGXYX]** Melhoria na integração com Protheus para envio de item contabil, classe de valor e natureza financeira na mensageria única.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.161

* **[Ticket: 07\TSPFER]** Alteração na criação do tipo de objeto que envia as informações de item contábil e classe de valor, para inteiro ao inves de string.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Lan.IService.dll

* **[Ticket: 07\TSOR85]** Melhoria na funcionalidade de Lançamento para validar os valores de integração do financeiro com o SGI ao abrir a tela de Lançamento.

Arquivo: RM.Fin.Lan.Data.dll

## 11.83.55.162

* **[Ticket: 07\TSONVH]** Ajustes Lei 13.137/2015

Arquivos: RM.Fin.Parametros.Form.dll, RM.Fin.Lan.Intf.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lib.dll, RM.Fin.Lan.Form.dll, RM.Fin.Parametros.Intf.dll, RM.Fin.Facade.dll, RM.Fin.Parametros.Data.dll, RM.Fin.Banco.Form.dll, RM.Fin.Lan.IService.dll, RM.Fin.Lan.Data.dll

* **[Ticket: Alterações Gerais]** Ajuste Lei 13.137/2015

Arquivo: RM.Fin.Facade.dll

## 11.83.55.163

* **[Ticket: 07\TSONVH]** Ajustes Lei 13.137/2015

Arquivo: RM.Fin.Parametros.Form.dll

## 11.83.55.164

* **[Ticket: 07\TSOSHN]** Otimização no processo de baixa. Agora o sistema valida corretamente a cotação da taxa Selic.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Moeda.IService.dll, RM.Fin.Moeda.Service.dll

* **[Ticket: 07\TSONVH]** Ajustes Lei 13.137/2015

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 07\TSRKCX]** Corrige falha que impedia baixa de lançamentos em Oracle

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.166

* **[Ticket: 07\TSRXQT]** Lei 13.137/2015 para a cumulatividade diária de retenção do PCC.

Arquivos: RM.Fin.Lan.Data.dll, RM.Fin.Parametros.Form.dll, RM.Fin.Lan.Service.dll, RM.Fin.Parametros.Data.dll, RM.Fin.Lan.Form.dll, RM.Fin.Banco.Form.dll, RM.Fin.Lan.Intf.dll, RM.Fin.Parametros.Intf.dll, RM.Fin.Lan.IService.dll

* **[Ticket: 07\TSQJEJ]** Otimização no processo de baixa de lançamento. Agora os valores do Item de Baixa correspondem com os valores informados na baixa do lançamento. A alteração foi a validação correta da parametrização da baixa em finais de semana e feriados com base nos dados do cliente.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.172

* **[Ticket: 07\TTAGJK]** Otimizado retorno bancário para que o adiantamento seja gerado com data de vencimento igual a data de emissão

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.174

* **[Ticket: 07\TSSKUV]** Otimizado processo de vinculo de devolução para exibição do lançamento com saldo restante da devolução para ser vinculado a outro lançamento

Arquivo: RM.Fin.Lan.Intf.dll

## 11.83.55.178

* **[Ticket: 07\TTAEPR]** Otimizado o processo de cancelamento de baixa para lançamentos faturados do Totvs Incorporação;

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 07\TTGYGO]** Foi criado no perfil de usuário a permissão - "Pemite Alterar na baixa valor de multa e juros de tributos".Esta permissão está relácionada ao cadastro de - "Lançamentos" dentro do perfil de usuário.Tem o objetivo de garantir que se autorizado o usuário consiga alterar o valor de juros e multa que é calculado de acordo com os parâmetros da etapa IRRF/INSS.Com esta opção desabilitada, o sistema sempre calculará o valor de juros e multa de lançamentos que representam tributos.Com esta opção habilitada, o sistema irá verificar se o juros e multa foi informado pelo usuário e se sim não irá refazer o cálculo de juros e multa e considerará no cálculo do valor líquido o valores informados pelo usuário.Classificação dos lançamentos afetados por essa permissão.IRRF PJ - 6,IRRF PF - 7,INSS Empregado - 11,INSS Empregador - 12,CSLL - 18,PIS - 19,COFINS - 20, Contribuição Social - 21,INSS Liber - 31,IRRF Liber 32,Obs: Esta funcionalidade está relacionada ao valor líquido calculado para baixa, pois nesses processo o usuário poderá informar os valores de juros e multa antes da baixa.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.dll, RM.Fin.Lib.dll

## 11.83.55.183

* **[Ticket: 07\TTLEUX]** Melhoria na alteração de contabilização de baixa, possibilitando alteração mesmo que a contabilização já tenha passado por um integração ao lote zero, e em seguida tenha sido regerada.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.190

* **[Ticket: 07\TTSANJ]** Ajuste na integração Educacional X Protheus Backoffice.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Lan.Data.dll

* **[Ticket: 07\TTSANJ]** Ajuste na integração Educacional X Protheus Backoffice

Arquivos: RM.Fin.Lan.Data.dll, RM.Fin.Lan.Service.dll

* **[Ticket: 07\TTP800]** Otimizado alteração da contabilização de baixa sem que seja necessário excluir a contabilização antiga.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.204

* **[Ticket: 07\TUAUBU]** Ajuste na criação dos vencimentos de fatura quando executado processo de acordo no Protheus.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.205

* **[Ticket: 07\TUBO48]** Foi realizada uma alteração para que lançamentos financeiros em que o Código de Receita informado no IRRF PJ tenha uma numeração e, o Código Oficial do mesmo no cadastro de Códigos de Receita do RM Fluxus tenha outra, sejam gerados normalmente na DIRF.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.206

* **[Ticket: 07\TTYRHU]** Otimizado processo de baixa por acordo com lançamentos do educacional

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 07\TUBOPT]** O sistema está retornando na consulta dos Rendimentos das Retenções dos Lançamentos Financeiros, lançamentos em que houve acumulatividade e depois a retenção do devido imposto na baixa de outro Lançamento Financeiro. Nesse caso, esses lançamentos devem ser desconsiderados, pois na Baixa do Lançamento em que houve a retenção já é considerado o valor e a base de cálculo do Lançamento que acumulou.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.208

* **[Ticket: 07\TUDRW7]** Foi constatado que não estão sendo gerados na DIRF Lançamentos Financeiros, que possuam IRRF PF, em que não houve a retenção do imposto durante o ano, porém a soma dos valores superou 6.000,00. Foi realizada uma alteração para que sejam contemplados na geração da DIRF rendimentos de Cli/For que superaram 6.000,00 durante o ano, mesmo que não tenha havido retenção para o Cli/For.Foi identificado que, ao gerar a Rotina para Lançamentos de Pessoa Jurídica que possuam retenção do IRRF PJ, o sistema estava considerando a Data de Apuração do IRRF PF. Foi realizada uma alteração para que, no caso de Lançamentos Financeiros com IRRF PJ, o sistema considere a parametrização da Data de Apuração conforme informado na parametrização do RM Fluxus para esse Tributo.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fis.RotinasFiscais.Service.dll

## 11.83.55.209

* **[Ticket: 07\TUDXFN]** Foi identificado que determinado Lançamento Financeiro não está sendo gerado na DIRF. Seguem as carcterísticas do Lançamento:- incidência do IRRF PF (apuração do IRRF PF pela Data de Vencimento)- Faturado- Vencimento de Fatura foi BaixadoForam realizadas alterações para que, quando o IRRF for apurado pela Data de Vencimento, Lançamentos Financeiros Faturados sejam considerados na geração da DIRF.

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 07\TUFOJ2]** Ao gerar a DIRF em ambiente 3 camadas, marcando as opções do Fluxus, em que o formato de Data do Servidor de Aplicação esteja diferente do formato de Data do Servidor de Banco de Dados Oracle, o sistema estava emitindo a seguinte mensagem: "not a valid month". Foi realizada uma alteração para que essa mensagem não ocorra mais.

Arquivos: RM.Fin.Lib.dll, RM.Fin.Lan.Service.dll

* **[Ticket: 07\TUDLFL]** Na geração da DIRF, foi identificado que o sistema estava duplicando os valores para determinado Lançamento Financeiro em que havia as Contribuições. Essa questão acontecia devido ao fato de que o Serviço que retona os Lançamentos Financeiros (em que exista as contribuições) para Lançamentos que estão na Nova Baixa, estava retornando também valores referentes à Lançamentos Financeiros que estão na Baixa Antiga. O Lançamento Financeiro em questão é referente à Baixa Antiga, e estava sendo retornado duas vezes, causando duplicidade de valor. Foi realizada uma alteração para que Lançamentos que estiverem na Baixa Antiga, não sejam retornados nas consultas referentes à Nova Baixa.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.210

* **[Ticket: 07\TUFCGS]** Foram realizadas alterações para que Lançamentos Financeiros com incidência do IRRF PF, em que não houve retenção do Imposto e foram Faturados, sejam considerados na geração da DIRF.Foi realizada uma alteração na geração da DIRF para que não sejam gerados Lançamentos Financeiros a Receber.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.211

* **[Ticket: 07\TUETGM]** Ao gerar a DIRF para Lançamentos Financeiros com incidência do IRRF PF, com mais de uma Baixa, mas que não retiveram o imposto, o sistema estava gerando valores errôneos para esse lançamento nos registros RTRT e RTPO.Ao gerar a DIRF para Lançamento Financeiro com incidência do CSRF, com mais de uma Baixa, em que nas Baixas houve retenção do imposto, o sistema estava retornando somente os rendimentos referente à Base de Cálculo do Imposto de uma das Baixas.Ao gerar a DIRF selecionando as Retenções do Fluxus, o sistema estava emitindo a seguinte mensagem: "A cadeia de caracteres de entrada não estava em um formato incorreto". Isso acontecia devido ao código da Receita utilizado para o Tributo CSRF ter um “ponto”. Foi realizada uma alteração para que no caso das Retenções, o sistema também utilize o Codigo de Receita Oficial (Cadastro de Códigos de Receita no RMFluxus), como hoje já é o comportamento para o IRRF.Ao gerar a DIRF para Lançamento em que houve retenção das Contribuições, em que houveram duas Baixas em meses diferentes, o sistema não estava considerando a segunda Baixa.

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 07\TUGVEL]** Ao gerar a DIRF para Lançamentos com Redução da Base de Cálculo do IRRF PF, em que não houve a retenção do imposto, o sistema não está gerando o registro RIO com o valor de Isenção. Após as alterações, o registro foi gerado com sucesso.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fis.RotinasFiscais.Service.dll

## 11.83.55.218

* **[Ticket: 07\TULOPS]** Retirada validação de cancelamento de itens de baixa com vínculo para os lançamentos de tributos. Como esse tipo de lançamento é a "ponta" final do vínculo, seu cancelamento não pode depender do cancelamento do lançamento que o gerou.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.219

* **[Ticket: 07\TUMLXV]** Ajustado o processo de retorno bancário, para que, considere o desconto de crédito de adiantamento somente quandoainda não tiver sido baixado os creditos vinculados ao lançamento.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.220

### Rotina: Cancelamento fatura integração Protheus

* **[Ticket: RMCTBFIN-52]** Ajuste no cancelamento de lançamentos de origem no Totvs Gestão do Estoque, Compras e Movimento chamada pelo cancelamento de acordo quando a integração "Educacaional x Protheus" está ativa.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.226

* **[Ticket: 07\TUTEDL]** Criação do campo Classificação do Pagamento ou Recebimento no lançamento financeiro a ser utilizado pelo Fiscal

Arquivos: RM.Fin.Parametros.Intf.dll, RM.Fin.Lan.IService.dll, RM.Fin.Lib.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lan.Intf.dll, RM.Fin.Parametros.Data.dll, RM.Fin.Lan.Data.dll, RM.Fin.Lan.Form.dll

## 11.83.55.242

* **[Ticket: 07\TVGA05]** Otimização no processo de importação de arquivo de cobrança. Agora o sistema realiza a importação dos valores opcionais de forma correta como feito na baixa manual.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.256

### Rotina: Alteração de título em bordero

* **[Ticket: MEDU-669]** Melhoria no processo de alteração de data de vencimento em integrações por mensageria única, possibilitando abortar a operação caso algum erro ocorra.

Arquivos: RM.EduPS.Facade.Server.dll, RM.Fin.Lib.dll, RM.EduPS.Processos.Data.dll, RM.Fin.Lan.Data.dll, RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll, RM.Edu.Financeiro.Data.dll, RM.Con.Utils.dll, RM.Fin.Facade.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lan.IService.dll

## 11.83.55.263

* **[Ticket: Alterações Gerais]**

Arquivos: WSTotvs.RegrasECommerceMaster.dll, RM.Glb.Live.SSO.Auth.dll, WSTotvs.RegrasECommerce.dll

## 11.83.55.271

### Rotina: Project-473170 IMPORTAÇÃO DE ARQUIVO DE RETORNO Project-473170

* **[Ticket: 498905 / FINANCEIRO01-81]** Otimização no processo de importação de arquivo de retorno de cobrança. Agora o sistema realiza o processo corretamente quando o código de ocorrência não estiver informado no arquivo de retorno.

Arquivo: RM.Fin.Banco.Data.dll

## 11.83.55.280

### Rotina: Project-721325 Erro para geração de Remessa Project-721325

* **[Ticket: 794573 / FINANCEIRO01-557]** Ajustado serviço de alteração de lançamentos, a partir de agora, o clientefornecedor de lançamentos provenientes do Totvs Gestão Educacional, não podem ser alterados.

Arquivo: RM.Fin.Lan.Service.dll

## 11.83.55.293

### Rotina: BOLETO ALTERAR DATA DE VENCIMENTO FIN 036

* **[Ticket: 1120718 / FINANCEIRO01-1444]** Ajuste na consistência de alteração de dados do lançamento em processo de alteração global.

Arquivos: RM.Fin.Lan.Data.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lib.dll

## 11.83.55.314

### Rotina: Project-1719730 Template de Acordo Project-1719730

* **[Ticket: 1740291 / FINANCEIRO01-3977]** Ajustado formulário de geração de acordo para que ao exibir a aba de valores do acordo todos os valores estejam atualizados.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: SESSAO DE CAIXA FECHAR SESSAO FIN 273

* **[Ticket: 1702858 / FINANCEIRO01-3853]** Ajuste para que ao finalizar uma sessão de caixa o sistema guarde o campo CODUSUARIOFECHAMENTO com o código do usuário que fechou a sessão.

Arquivos: RM.Fin.SessaoCaixa.Data.dll, RM.Fin.SessaoCaixa.Form.dll, RM.Fin.SessaoCaixa.Intf.dll

# TOTVS Gestão Fiscal

## 11.83.55.100

* **[Ticket: 07\TQQXLM]** Ao consultar autorização de uma NF-e denegada, a NF-e será identificada com status denegado.

Arquivos: RM.Fis.NFe.Service.dll, RM.Fis.NFe.Data.dll

## 11.83.55.102

* **[Ticket: 07\TQVHHT]** - Implementação da Importação da Planilha IBPTax modelo 14.2- Inclusão dos campos IBPT no anexo do cadastro do produto "Dados Fiscais por UF"- Demonstração dos valores aproximados nas Informações adicionais do produto da NF-e

Arquivos: RM.Fis.LancFiscal.Intf.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.Cadastros.Data.dll, RM.Fis.NFe.Service.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.Cadastros.Form.dll, RM.Fis.Cadastros.Intf.dll, RM.Fis.Cadastros.Services.dll, RM.Fis.Cadastros.IService.dll

* **[Ticket: 07\TQVHHT]** Implementação da Importação da Planilha IBPTax modelo 14.2

Arquivo: RM.Fis.Cadastros.Services.dll

## 11.83.55.103

* **[Ticket: 07\TQVHHT]** Ajuste no carregamento dos valores IBPTax da tabela TITMMOV para TITMMOVFISCAL.

Arquivos: RM.Fis.NFe.Service.dll, RM.Fis.LancFiscal.Form.dll

## 11.83.55.106

* **[Ticket: 07\TQUEMV]** Os valores de frete, seguro, desconto, seguro, acréscimos, descontos e outros descontos deverão afetar a base de IPI conforme parametrizado pela regra de IPI vinculada a natureza de operação.

Arquivo: RM.Fis.LancFiscal.IService.dll

## 11.83.55.108

* **[Ticket: 07\TRDXQT]** Melhorias no processo responsável pelo Sincronismo de Documentos (MD-e)

Arquivo: RM.Fis.TSS.Service.dll

* **[Ticket: 07\TQTIYZ]** Ao gerar o SPED para Lançamento, cuja Natureza seja do Tipo ICMS ST, o sistema não estava gerando o registro C420 com a linha com o código "Can-T". Foi realizada uma alteração para que essa linha seja gerada para o caso citado anteriormente.

Arquivo: RM.Fis.Sped.Server.dll

* **[Ticket: 07\TRCQKF]** Ao realizar a Baixa de Lançamento com Retenções, o sistema está emitindo a mensagem de consistência do Período de Apuração Encerrado ou não Criado:"O Período de apuração do tributo para a data 17/12/2014 está encerrado para movimentação ou não existe."Pode ser observado a falta do código do Tributo na mensagem, fazendo com que o usuário não consiga identicar o respectivo período que deverá ser aberto/criado.Foi realizada uma alteração para que o código do Tributo seja emitido na mensagem.

Arquivo: RM.Fis.ApuracaoTrb.Service.dll

## 11.83.55.114

* **[Ticket: 07\TRFBLK]** Melhoria na seleção das informações de Produtos Globais para geração na Rotina Federal EFD Contribuições.

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.Data.dll, RM.Fis.Sped.Server.dll

## 11.83.55.130

* **[Ticket: 07\TQZCWC]** Implementada tributação ICMSST Pautado

Arquivos: RM.Fis.LancFiscal.Form.dll, RM.Fis.Tributo.Service.dll, RM.Fis.Tributo.Data.dll

## 11.83.55.133

* **[Ticket: 07\TRVD26]** Adicionado campo 11 -VL\_ITEM\_IR - (Valor do item para efeitos do Imposto de Renda) na geração do registro H010.

Arquivos: RM.Fis.Cadastros.Form.dll, RM.Fis.Sped.Engine.dll, RM.Fis.Cadastros.Data.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.Sped.Server.dll, RM.Fis.Cadastros.Intf.dll

## 11.83.55.137

* **[Ticket: Alterações Gerais]**

Arquivos: RM.Fis.Cadastros.Intf.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.Sped.Server.dll, RM.Fis.NaturezaOper.Form.dll, RM.Fis.TSS.IService.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Lib.Server.dll, RM.Fis.NaturezaOper.Service.dll, RM.Fis.Cadastros.Data.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.Sped.Form.dll, RM.Fis.NFe.Service.dll, RM.Fis.NFe.Intf.dll, RM.Fis.TSS.Service.dll, RM.Fis.Sped.Engine.dll, RM.Fis.Lib.dll, RM.Fis.Tributo.Data.dll, RM.Fis.Sped.Intf.dll, RM.Fis.Cadastros.Form.dll, RM.Fis.Tributo.Service.dll, RM.Fis.LancFiscal.Form.dll

* **[Ticket: 07\TRRPUF]** A SEFAZ para o estado do Mato Grosso, não permite tags vazias ou nulas.

Arquivo: RM.Fis.NFe.Service.dll

## 11.83.55.138

* **[Ticket: 07\TRSPBN]** Foi modificado o processo de emissão da NF-e 3.10 quando o destinatario/remetente for do exterior para que o campo idEstrangeiro seja gerado como nulo não obrigando o preenchimento da informação.

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: 07\TQTRPF]** Legislação Vias de transporte: adição das opções 11-Courier e 12-Handcarry.

Arquivos: RM.Fis.NFe.Service.dll, RM.Fis.Lib.dll

* **[Ticket: 07\TQZNUU]** Foi modificado o processo de emissão da NF-e para gerar notas com desoneração de ICMS

Arquivos: RM.Fis.NFe.Intf.dll, RM.Fis.NFe.Service.dll

## 11.83.55.143

* **[Ticket: 07\TSBNCA]** Em ambientes da TOTVS, não será enviado NFSe para o município de Cubatão - SP

Arquivos: RM.Fis.Utils.Intf.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Utils.Server.dll

* **[Ticket: 07\TSAPVX]** Ajuste no envio da NFSe de Cubatão-SP.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 11.83.55.151

* **[Ticket: 07\TSFXZD]** Atualização da Versão 11.83 conforme Versão 11.82 da biblioteca RM

Arquivos: RM.Fis.LancFiscal.IService.dll, RM.Fis.ApuracaoTrb.IService.dll, RM.Fis.Cadastros.Data.dll, RM.Fis.Utils.Server.dll, RM.Fis.dll, RM.Fis.RotinasFiscais.Data.dll, RM.Fis.Utils.Intf.dll, RM.Fis.NaturezaOper.Form.dll, RM.Fis.NFe.Service.dll, RM.Fis.Lib.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.ObrigacoesFederais.Data.dll, RM.Fiscal.exe, RM.Fis.Tributo.Service.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.Sped.Server.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.Facade.dll, RM.Fis.RegrasTributarias.IService.dll, RM.Fis.RegrasTributarias.Data.dll, RM.Fis.Cadastros.Intf.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Sped.Form.dll, RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.Filial.Intf.dll, RM.Fis.RegrasTributarias.Form.dll, RM.Fis.Cadastros.Form.dll, RM.Fis.ApuracaoTrb.Data.dll, RM.Fis.RegrasTributarias.Intf.dll, RM.Fis.Filial.Form.dll, RM.Fis.Sped.Intf.dll, RM.Fis.ObrigacoesFederais.Form.dll, RM.Fis.TSS.Service.dll, RM.Fis.ObrigacoesFederais.Intf.dll, RM.Fis.ApuracaoTrb.Form.dll, RM.Fis.NaturezaOper.IService.dll, RM.Fis.NaturezaOper.Service.dll, RM.Fis.Filial.Data.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.NFe.Intf.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.Sped.Engine.dll

* **[Ticket: 07\TQLCGC]** Implementação do envio de NFS-e de Porto Velho - RO, validação para que não permita o envio de NFS-e de substituição para este município.

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.Data.dll

* **[Ticket: 07\TSBXWS]** - Melhoria na geração do registro G140 do Sped Fiscal para correta geração no arquivo.

Arquivo: RM.Fis.Sped.Server.dll

## 11.83.55.154

* **[Ticket: 07\TSGAP6]** Ajuste no contexto da Rotina federal ECF onde o campo CODECF foi alterado conforme estrutura de dados atual.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: 07\TSITWZ]** Otimização no envio de NFS-e para o município de Belo Horizonte - MG.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 11.83.55.157

* **[Ticket: 07\TSIYMA]** Otimização na geração das tags motDesICMS e vICMSDeson para serem geradas para o CST 30

Arquivo: RM.Fis.NFe.Service.dll

## 11.83.55.161

* **[Ticket: 07\TQLSOW]** Melhoria na geração dos Registros N500/N650 da ECF.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: 07\TQLSOW]** Melhoria na Rotina Fiscal ECF - Bloco M

Arquivos: RM.Fis.ObrigacoesFederais.Form.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.NFe.Service.dll, RM.Fis.Sped.Server.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.Lib.dll, RM.Fis.NaturezaOper.Form.dll, RM.Fis.RegrasTributarias.Intf.dll, RM.Fis.RegrasTributarias.Data.dll, RM.Fis.RegrasTributarias.Form.dll, RM.Fis.RegrasTributarias.IService.dll, RM.Fis.ObrigacoesFederais.Data.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.NaturezaOper.IService.dll, RM.Fis.Cadastros.IService.dll, RM.Fis.Cadastros.Data.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.NFe.Form.dll, RM.Fis.RotinasFiscais.IService.dll, RM.Fis.NaturezaOper.Intf.dll, RM.Fis.Tributo.Service.dll, RM.Fis.RotinasFiscais.Data.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.NFe.Intf.dll, RM.Fis.Filial.Data.dll, RM.Fis.ObrigacoesFederais.Intf.dll, RM.Fis.Utils.Server.dll, RM.Fis.Facade.dll, RM.Fis.Utils.Intf.dll, RM.Fis.Cadastros.Services.dll, RM.Fis.Filial.Intf.dll, RM.Fis.Filial.Form.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.Sped.Form.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.NaturezaOper.Service.dll

## 11.83.55.163

* **[Ticket: 07\TSDZEI]** Melhoria na Geração da ECf Registro M410 - Ajuste na geração do campo IND\_VAL\_LAN\_LALB\_PB

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.RegrasTributarias.Data.dll, RM.Fis.RegrasTributarias.Intf.dll, RM.Fis.RegrasTributarias.Form.dll, RM.Fis.ApuracaoTrb.Service.dll

## 11.83.55.167

* **[Ticket: 07\TSV336]** Melhoria na Geração da ECF - Diversos registros

Arquivos: RM.Fis.ObrigacoesFederais.Form.dll, RM.Fis.NaturezaOper.Service.dll, RM.Fis.RegrasTributarias.Form.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.NFe.Form.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.RegrasTributarias.Data.dll, RM.Fis.TSS.Service.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.NFe.IService.dll, RM.Fis.Lib.Server.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.NFe.Data.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.Sped.Server.dll, RM.Fis.RegrasTributarias.IService.dll, RM.Fis.NaturezaOper.Intf.dll, RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.Facade.dll, RM.Fis.NaturezaOper.Data.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.NFe.Service.dll, RM.Fis.Formula.dll, RM.Fis.ApuracaoTrb.Form.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.Lib.dll, RM.Fis.NFe.Intf.dll

## 11.83.55.169

* **[Ticket: 07\TSFLH4]** Melhoria: Carregar o Log de desempenho do contábil no processamento da ECF

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Lib.dll

* **[Ticket: 07\TSFLH4]** Melhoria: Implementação do Log do processamento da rotina ECF. Efeito: Quando o arquivo ECF é gerado será gerado também um arquivo separado de Log.

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.Facade.dll, RM.Fis.Lib.dll

## 11.83.55.171

* **[Ticket: 07\TSUMNI]** Ao enviar a NFSe de Cubatão, o sistema está apresentando a seguinte mensagem:"TSS - Erro na validação desta nota.TSS : 003 - Metodo nao disponivel para o codigo de municipio informado ou configurado para esta entidade."Foi constatado que o sistema não deveria executar o método de Validação de Schema para o município de Cubatão. Foi realizada uma alteração para que esse método não seja executado para esse município.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 11.83.55.177

* **[Ticket: 07\TTEWPO]** Sincronismo do Fiscal versão 11.82 Atual Para Versão 11.83.55 Melhoria

Arquivos: RM.Fis.NFe.Intf.dll, RM.Fis.RegrasTributarias.Intf.dll, RM.Fis.NFe.Service.dll, RM.Fis.NFe.IService.dll, RM.Fis.NFe.Form.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.RegrasTributarias.Data.dll, RM.Fis.NaturezaOper.Form.dll, RM.Fis.Utils.Server.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.ApuracaoTrb.Form.dll, RM.Fis.Lib.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.RegrasTributarias.Form.dll, RM.Fis.Sped.Server.dll, RM.Fis.NFe.Data.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.TSS.Service.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.NaturezaOper.Intf.dll

* **[Ticket: 07\TTASID]** - Para o grupo compensação de prejuizo será gravado no detalhamento da apuração Item com valor zero. Obs: O tratamento acima será realizado para ter onde vincular o lançamento lalur b ao item da apuração.- No momento da Geração da ECF não serão levados itens de apuração com valor zero.

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.ApuracaoTrb.Service.dll

## 11.83.55.179

* **[Ticket: 07\TTDKH3]** Tratamento no processamento da ECF para contemplar cisão

Arquivos: RM.Fis.RegrasTributarias.Service.dll, RM.Fis.ApuracaoTrb.Service.dll

* **[Ticket: 07\TTFZSX]** - Para o Lucro Real - Mensal EstimadoQuando o "Valor do imposto do mês anterior" for aplicado na apuração do tributo, neste valor devem estar contidos os valores das compensações.

Arquivos: RM.Fis.RegrasTributarias.Form.dll, RM.Fis.RegrasTributarias.IService.dll, RM.Fis.RegrasTributarias.Service.dll

* **[Ticket: 07\TTDKH3]** Implementação da ocorrência de cisão no período de apuração e na rotina federal ECF.

Arquivos: RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.RotinasFiscais.Service.dll

## 11.83.55.184

* **[Ticket: 07\TTLGIU]** Ao preencher as TAG's dhEmi e dhSaiEnt do XML da NF-e serão observados os parâmetros "Identificação de Horário de Verão" e "Identificação do Horário" dos parâmetros da Carta de Correção Eletrônica. As tag's dhEmi e dhSaiEnt serão preenchidas também com o fuso horário conforme parametrizado.

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: 07\TTLVWM]** Ao executar o Processo de Cancelamento da NFS-e para Filial do município de Campinas, o sistema não disponibiliza a Tela para informar o Motivo do Cancelamento, fazendo com que a TAG para essa informação não seja gerada, causando uma rejeição da Prefeitura. Esse problema ocorreu pois a Prefeitura passou a validar o Motivo do Cancelamento, não sendo previsível essa mudança por parte da Prefeitura.

Arquivo: RM.Fis.RotinasFiscais.Form.dll

## 11.83.55.191

* **[Ticket: 07\TTUGFW]** Atualização da versão 11.83 conforme versão 11.82 da biblioteca no produto gestão fiscal

Arquivos: RM.Fis.RegrasTributarias.Form.dll, RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.ObrigacoesFederais.Intf.dll, RM.Fis.Cadastros.Form.dll, RM.Fis.Sped.Engine.dll, RM.Fis.NFe.Data.dll, RM.Fis.ApuracaoTrb.Data.dll, RM.Fis.Facade.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.ObrigacoesFederais.Data.dll, RM.Fis.Utils.Intf.dll, RM.Fis.NFe.Service.dll, RM.Fis.Tributo.Form.dll, RM.Fis.Utils.Server.dll, RM.Fis.NaturezaOper.Data.dll, RM.Fis.Sped.Server.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.RegrasTributarias.IService.dll, RM.Fis.Cadastros.Intf.dll, RM.Fis.NFe.Intf.dll, RM.Fis.NaturezaOper.IService.dll, RM.Fis.NFe.Form.dll, RM.Fis.NFe.IService.dll, RM.Fis.ObrigacoesFederais.Form.dll, RM.Fis.Cadastros.Data.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.Tributo.Service.dll, RM.Fis.NaturezaOper.Service.dll, RM.Fis.Sped.Form.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.Exportacao.Service.dll, RM.Fis.NaturezaOper.Form.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.Lib.dll, RM.Fis.NaturezaOper.Intf.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.ApuracaoTrb.Service.dll

## 11.83.55.192

* **[Ticket: 07\TTUZC2]** Melhoria no sped fiscal onde foi implementado um novo parâmetro habilitando ou não a geração do Bloco K.

Arquivos: RM.Fis.Sped.Form.dll, RM.Fis.Sped.Server.dll, RM.Fis.Sped.Intf.dll, RM.Fis.Sped.Engine.dll

## 11.83.55.196

* **[Ticket: 07\TTSWL0]** Melhoria na geração da tag refNFe para que não ocorra duplicidade de chave de acesso da NF-e

Arquivos: RM.Fis.NFe.Service.dll, RM.Fis.Facade.dll

## 11.83.55.204

* **[Ticket: 07\TUBJUP]** Implementações referentes à DIRF 2016

Arquivos: RM.Fin.Lan.Service.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.Facade.dll, RM.Fis.RotinasFiscais.Data.dll, RM.Fis.dll, RM.Fin.Lib.dll, RM.Fis.RotinasFiscais.IService.dll, RM.Fin.Lan.IService.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.Intf.dll

## 11.83.55.208

* **[Ticket: 07\TUDGC9]** Ao gerar a DIRF, foi constatado que na geração do arquivo, clientes/fornecedores com mesmo CNPJ não estão sendo agrupados na geração do arquivo.Foi realizada uma alteração na geração da DIRF para que no caso de Clientes/Fornecedores que possuam mesmo CNPJ, o sistema agrupe os valores conforme Layout do Manual da Rotina.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.IService.dll

## 11.83.55.209

* **[Ticket: 07\TUAHPP]** Legislação: Implementação da Legislação Federal do ICMS Diferencial de Aliquota.

Arquivos: RM.Fis.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.Tributo.IService.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Cadastros.Intf.dll, RM.Fis.RotinasFiscais.Data.dll, RM.Fis.NaturezaOper.Form.dll, RM.Fis.NaturezaOper.Intf.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.Sped.Engine.dll, RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.Cadastros.Data.dll, RM.Fis.Sped.Server.dll, RM.Fis.Lib.Server.dll, RM.Fis.Cadastros.Form.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.Tributo.Service.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.NFe.Data.dll, RM.Fis.NaturezaOper.Service.dll, RM.Fis.NFe.Service.dll, RM.Fis.Lib.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.ApuracaoTrb.IService.dll, RM.Fis.ApuracaoTrb.Form.dll, RM.Fis.NaturezaOper.IService.dll, RM.Fis.ApuracaoTrb.Data.dll

## 11.83.55.213

* **[Ticket: 07\TUHWYY]** Ao gerar a DIRF, foi constatado que o sistema não estava gerando valores no registro RTPO para o primeiro mês que houvesse valor a ser gerado. Após as alterações, o sistema gerou o valor com sucesso.

Arquivos: RM.Fin.Lib.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.RotinasFiscais.Data.dll, RM.Fin.Lan.IService.dll, RM.Fin.Lan.Service.dll, RM.Fis.RotinasFiscais.Intf.dll

## 11.83.55.214

* **[Ticket: 07\TUJVCQ]** Otimização na geração das informações de combustível

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: 07\TUGFLL]** Ajuste no Fonte do DataSet acertando a Sincronização

Arquivo: RM.Fis.Cadastros.Intf.dll

## 11.83.55.218

* **[Ticket: 07\TTYHIN]** Implementação do Serviço de Tributação que calcula a Base de Cálculo do ICMS na UF de Destino no Item do Movimento.

Arquivos: RM.Fis.Tributo.Service.dll, RM.Fis.Tributo.IService.dll, RM.Fis.Lib.dll

## 11.83.55.228

* **[Ticket: 07\TUSLGC]** Implementação da ECF 2016

Arquivos: RM.Fis.RegrasTributarias.IService.dll, RM.Fis.Facade.dll, RM.Fis.NFe.Service.dll, RM.Fis.RegrasTributarias.Form.dll, RM.Fis.Utils.Intf.dll, RM.Fis.NFe.IService.dll, RM.Fis.Tributo.Form.dll, RM.Fis.ApuracaoTrb.Form.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.NaturezaOper.IService.dll, RM.Fis.NFe.Form.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.NaturezaOper.Data.dll, RM.Fis.Filial.Intf.dll, RM.Fis.Filial.Data.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.NaturezaOper.Form.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.Parametros.Data.dll, RM.Fis.Cadastros.Form.dll, RM.Fis.NaturezaOper.Service.dll, RM.Fis.Formula.dll, RM.Fis.Sped.Server.dll, RM.Fis.dll, RM.Fis.NaturezaOper.Intf.dll, RM.Fis.NFe.Data.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.RotinasFiscais.IService.dll, RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.Parametros.Intf.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.Tributo.Service.dll, RM.Fis.Utils.Server.dll, RM.Fis.Parametros.Form.dll, RM.Fis.NFe.Intf.dll, RM.Fis.Cadastros.Intf.dll, RM.Fis.RegrasTributarias.Intf.dll, RM.Fis.Filial.Service.dll, RM.Fis.Tributo.IService.dll, RM.Fis.Sped.Engine.dll, RM.Fis.Filial.Form.dll, RM.Fis.RegrasTributarias.Data.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.ObrigacoesFederais.Data.dll, RM.Fis.RotinasFiscais.Data.dll, RM.Fis.ApuracaoTrb.Data.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.ApuracaoTrb.IService.dll, RM.Fis.Lib.dll, RM.Fis.RotinasFiscais.Form.dll

* **[Ticket: 07\TUSLGC]** Implementação da ECF 2016

Arquivo: RM.Fis.RegrasTributarias.Intf.dll

## 11.83.55.233

* **[Ticket: 07\TTEWZO]** Implementação dos registros X430 e X450 da ECF.

Arquivos: RM.Fis.RegrasTributarias.Service.dll, RM.Fis.Filial.Form.dll, RM.Fis.Filial.Intf.dll, RM.Fis.RegrasTributarias.Data.dll, RM.Fis.Facade.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RegrasTributarias.Form.dll, RM.Fis.ApuracaoTrb.Intf.dll

## 11.83.55.239

* **[Ticket: 07\TVFOAY]** - Ajuste no cálculo do grupo Lucro da Exploração para considerar o Valor do resultado contábil do Evento Pai em seu processamento.- Na exibição da Simulação na pasta Lucro Exploração considerar o valor do resultado contábil nos Itens.

Arquivos: RM.Fis.Tributo.Service.dll, RM.Fis.LancFiscal.IService.dll, RM.Fis.Cadastros.Data.dll, RM.Fis.ObrigacoesFederais.Data.dll, RM.Fis.RegrasTributarias.Form.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.Utils.Intf.dll, RM.Fis.Tributo.IService.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.Facade.dll, RM.Fis.Sped.Engine.dll, RM.Fis.Sped.Intf.dll, RM.Fis.RegrasTributarias.Data.dll, RM.Fis.RegrasTributarias.Service.dll, RM.Fis.ApuracaoTrb.IService.dll, RM.Fis.NaturezaOper.Form.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RegrasTributarias.Intf.dll, RM.Fis.NFe.Service.dll, RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.Sped.Server.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.TSS.Service.dll, RM.Fis.Lib.dll

# TOTVS Gestão Hospitalar

## 11.83.55.100

* **[Ticket: 07\TQGDIA]** Ajuste na geração de lançamentos financeiros

Arquivos: RM.Sau.Produto.Intf.dll, RM.Sau.Facade.dll

# TOTVS Gestão Patrimonial

## 11.83.55.105

* **[Ticket: 07\TQXCCJ]** Modificado o processo de geração de lançamentos contábeis por parte do TOTVS Gestão Patrimonial de forma a permitir o uso de variáveis pré-definidas durante a contabilização.

Arquivos: RM.Pat.Contabilizacao.Form.dll, RM.Pat.Contabilizacao.Service.dll, RM.Pat.Contabilizacao.IService.dll

## 11.83.55.125

* **[Ticket: 07\TRPEQB]** \* Atualiação do relatório Ficha de Imobilizado.

Arquivo: RM.Pat.Relatorio.Data.dll

# TOTVS Incorporação

## 11.83.55.158

* **[Ticket: 07\TSNORB]** Melhoria no processo de efetivação da venda.

Arquivo: RM.Imb.Contratos.Server.dll

## 11.83.55.178

* **[Ticket: 07\TSSRIU]** Incluída mensagem esclarecedora quanto à necessidade de se cadastrar valores opcionais para os componentes envolvidos no processo de aditivo.

Arquivo: RM.Imb.Facade.dll

# TOTVS Processo Seletivo

## 11.83.55.100

* **[Ticket: 07\TR8502]** Melhoria na exibição dos anexos de informações de integração com o Protheus.

Arquivo: RM.EduPS.Cadastros.Form.dll

## 11.83.55.110

* **[Ticket: 07\TRAEDR]** Otimizado processo de impressão de 2ª via de comprovante de inscrição no Processo Seletivo.

Arquivos: RM.EduPS.Lib.Server.dll, App\_Web\_edupsrelatoriodotnetwebform.aspx.ca9058f9.dll

## 11.83.55.154

* **[Ticket: 07\TSI519]** Melhoria no pocesso de cancelamento de inscrição quando o sistema Processo Seletivo estiver integrado ao BackOffice Protheus.

Arquivo: RM.EduPS.Inscricoes.Server.dll

## 11.83.55.155

### Rotina: EDU-Teste Protheus

* **[Ticket: PCREQ-3488]** Ajuste no processo de alteração de data vencimento para que seja trafega a informação do código do processo seletivo da inscrição para tratamento de informações manipuladas pela integração com o Protheus.

Arquivos: RM.EduPS.Processos.Data.dll, RM.EduPS.Facade.Server.dll

## 11.83.55.158

* **[Ticket: 07\TSMVG5]** Otimizado processo de exclusão de lançamentos de inscrições anônimas não importadas.

Arquivo: RM.EduPS.Processos.Data.dll

## 11.83.55.160

* **[Ticket: 07\TSNA11]** Criação da importação do layout do ENEM 2014.

Arquivos: RM.EduPS.Processos.Data.dll, RM.EduPS.Processos.Form.dll, RM.EduPS.Processos.Intf.dll

## 11.83.55.164

* **[Ticket: 07\TSSKHK]** Ajuste para envio do Item Contábil e Classe de Valor ao gerar lançamento financeiro na inscrição de candidato do Processo Seletivo.

Arquivos: RM.EduPS.Lib.Intf.dll, RM.EduPS.Cadastros.Data.dll, RM.EduPS.ProcessoSeletivo.Server.dll

* **[Ticket: 07\TSRSIE]** Otimizado processo de alteração de data de inscrição em processos seletivos.

Arquivo: RM.EduPS.Cadastros.Data.dll

## 11.83.55.169

* **[Ticket: 07\TSPLAF]** Otimizado processo criação de contexto no processo seletivo.

Arquivo: RM.EduPS.Cadastros.Data.dll

## 11.83.55.176

* **[Ticket: 07\TSMJ72]** Otimizado processo de importação de notas do ENEM utilizando o arquivo do INEP.

Arquivo: RM.EduPS.Utils.dll

## 11.83.55.187

* **[Ticket: 07\TSFMJ5]** Acerto ortográfrico.

Arquivo: RM.EduPS.Cadastros.Form.dll

## 11.83.55.198

* **[Ticket: 07\TTSDMC]** Ajuste no envio de emails de informações da prova.

Arquivos: RM.EduPS.Processos.Data.dll, RM.EduPS.Processos.Intf.dll

## 11.83.55.222

* **[Ticket: 07\TUPJDF]** Ajuste no processo se alocação de profissionais.

Arquivo: RM.EduPS.Processos.Data.dll

## 11.83.55.229

* **[Ticket: 07\TUUMJU]** Ajuste na chamada de candidatos aprovados.

Arquivo: RM.EduPS.Apuracoes.Server.dll

* **[Ticket: 07\TUULIP]** Ajuste na exibição profissionais alocados.

Arquivo: RM.EduPS.Cadastros.Data.dll

## 11.83.55.230

* **[Ticket: 07\TUZBG1]** Ajuste no processo de alteração de parâmetros de etapas.

Arquivo: RM.EduPS.Processos.Form.dll

## 11.83.55.254

* **[Ticket: 07\TWARGZ]** Ajuste na alocação de recursos.

Arquivo: RM.EduPS.Inscricoes.Server.dll

## 11.83.55.285

### Rotina: remetente de e-mail enviado a partir do processo seletivo não está sendo gravado em "historico de envio de e-mail"

* **[Ticket: 900925 / EDUCACIONAL01-951]** Incluído nos parâmetros de envio de e-mail do Processo Seletivo o campo de Nome do Remetente de e-mail, tal campo tem função de informar qual foi o remetente que enviou aquele e-mail, onde este será gravado no histórico de envio de e-mail.

Arquivos: RM.EduPS.Processos.Intf.dll, RM.EduPS.Processos.Form.dll, RM.EduPS.Parametros.Intf.dll, RM.EduPS.Parametros.Form.dll, RM.EduPS.Processos.Data.dll

## 11.83.55.291

### Rotina: PROCESSO SELETIVO RM MATRICULAR EDU 50 393

* **[Ticket: 1075174 / EDUCACIONAL01-1597]** Ajuste no registro do RA gerado para aluno matriculado pelo processo seletivo RM.

Arquivos: RM.Edu.ProcSel.Server.dll, RM.EduPS.Inscricoes.Form.dll, RM.Edu.Aluno.Server.dll, RM.Edu.Facade.dll, RM.Edu.Matricula.Server.dll, RM.EduPS.Lib.Intf.dll, RM.Edu.Lib.Intf.dll, RM.EduPS.ProcessoSeletivo.Server.dll

## 11.83.55.293

### Rotina: Project-1115411 Envio de e-mail Processo Seletivo Project-1115411

* **[Ticket: 1132202 / EDUCACIONAL01-1789]** Ajuste no envio de e-mails de local de prova para candidados desclassificados.

Arquivos: RM.EduPS.Processos.Data.dll, RM.EduPS.Processos.Intf.dll

## 11.83.55.296

### Rotina: SQL Injection Portal do Processo Seletivo 11.83

* **[Ticket: PORTALMOBILE01-1330]** Ajustes de segurança no portal do processo seletivo, evitando SQL Injection.

Arquivos: RM.EduPS.Cadastros.Data.dll, App\_Web\_edupsresultadosgerais.ascx.b5bee319.dll, App\_Web\_edupsinscricaoareaofertada.ascx.58ed3fed.dll, App\_Web\_edupsprocessosseletivos.ascx.131e2aa5.dll

## 11.83.55.299

### Rotina: Alterar senha do candidato

* **[Ticket: 1235240 / PORTALMOBILE01-1352]** Alteração na consulta SQL que busca o usuário para envio de uma nova senha.

Arquivo: RM.EduPS.Cadastros.Server.dll

## 11.83.55.329

### Rotina: ÁREA DE INTERESSE (EDUPS.20.1013)

* **[Ticket: 2812993 / PORTALMOBILE01-4471]** Adequação do filtro por categoria baseado na parametrização da URL.

Arquivo: App\_Web\_edupsinscricaoareaofertada.ascx.58ed3fed.dll

## 11.83.55.332

### Rotina: CANDIDATOS INSCRITOS (EDUPS.20.1027)

* **[Ticket: 2907586 / PORTALMOBILE01-4737]** Adicionado o registro detalhado de log de inscrição de candidato

Arquivos: RM.EduPS.Cadastros.Data.dll, RM.EduPS.Facade.Server.dll

# TOTVS Segurança e Medicina do Trabalho

## 11.83.55.151

* **[Ticket: 07\TSCLST]** Implementação da geração de Exames Pendentes Demissionais. Ao cadastrar a rescisão de um funcionário, é verificado se o mesmo possui Exames Demissionais Pendentes. Caso possua, os mesmos são gerados na lista de Exames Pendentes.

Arquivos: RM.Smt.Clinico.Intf.dll, RM.Smt.Parametros.Data.dll, RM.Smt.Clinico.Data.dll, RM.Smt.Parametros.Form.dll, RM.Smt.Parametros.Intf.dll

## 11.83.55.251

* **[Ticket: 07\TVPJGV]** Colocado filtro de coligada, ao pesquisar perfis de exame pois o mesmo retornava perfis que não existiam na coligada em uso, quando esses exames eram usados processo dava erro.

Arquivo: RM.Smt.Lib.Form.dll
