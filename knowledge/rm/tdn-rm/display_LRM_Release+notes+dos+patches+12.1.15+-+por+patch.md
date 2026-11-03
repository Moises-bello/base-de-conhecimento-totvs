---
content_hash: 912efebf0126face26916d80f7e3b41a9b1044c9af6e418b3902c763ed0159c1
fetched_at: '2026-06-29T00:10:20.725726+00:00'
page_id: '490638058'
product: rm
source: tdn-rm
title: Release notes dos patches 12.1.15 - por patch
type: documentation
url: https://tdn.totvs.com/display/LRM/Release+notes+dos+patches+12.1.15+-+por+patch
version: 12
---

|  |
| --- |
| Esses são todos os patches gerados, porém nem todos estão disponíveis para todos os clientes. |

---

  
  

1square

---

  
  

# 12.1.15.100

## TOTVS Automação de Ponto

### Rotina: ALTERACOES GLOBAIS ESCALA DE HORARIO E DESCANSO PTO 35 1290

* **[Ticket: 407565 / MRH-5569]** Acertada a rotina de alteração global de descanso, pois o mesmo não realizada a exclusão de um registro.

Arquivo: RM.Pto.Horario.Data.dll

### Rotina: FORMULAS PTO 35 1179

* **[Ticket: 429669 / MRH-5942]** Quando existe ocorrências de um dia para o outro e utiliza-se quebra-por-dia ao concatenar as ocorrências para a próxima jornada estava dando erro no cálculo de tolerância. Feito o acerto para considerar corretamente o cálculo da fórmula HORARIODIASIT.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: PERIODO

* **[Ticket: MRH-5860]** Otimizado o refresh das informações de período no carregamento do espelho do ponto após a execução da rotina de definição de período ativo.

Arquivo: RM.Pto.Parametros.Data.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 95288 / MRH-5031]** Criado o parâmetro "Imprime abonos em jornadas não trabalhadas", para que seja impresso a descrição dos abonos nos dias de jornadas que não são de trabalho:Ex: Batida Nula, Feriado, etc.

Arquivos: RM.Pto.Relatorio.Intf.dll, RM.Pto.Relatorio.Data.dll, RM.Pto.Relatorio.Form.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** serviços cloud do atualizador

Arquivos: RM.Beta.upg, RM.Upgrade.upg, RM.Upg.Intf.dll, RM.Upg.Server.dll, RM.Upg.Client.dll

## TOTVS Construção e Projetos

### Rotina: CALCULO PROJETO PRJ 33 804

* **[Ticket: MCP-1673]** Sistema travando quando existem muitos projetos com revisões múltiplas

Arquivo: RM.Prj.Projeto.Form.dll

### Rotina: IMPORTAR TAREFAS VIA MS PROJECT PRJ 33 837

* **[Ticket: MCP-1685]** Ajuste na identificação do tipo de recurso ao realizar a importação de tarefas via MSProject.

Arquivo: RM.Prj.Tarefa.Data.dll

### Rotina: RELATORIOS FIXOS COMPOSICOES DO PROJETO PRJ 33 947

* **[Ticket: MCP-1696]** Ajuste nas fórmulas utilizadas para pesquisa dos valores das composições exibidas no relatório "Composições de Custo Unitário Utilizadas no Projeto".

Arquivo: RM.Prj.Formula.dll

### Rotina: RELATORIOS PERIODICOS PRJ 33 884

* **[Ticket: MCP-1680]** Ajuste na consulta do cronograma das tarefas de receitas ao gerar o Relatório Periódico - Histograma.

Arquivo: RM.Prj.Relatorios.Periodico.Server.dll

## TOTVS Folha de Pagamento

### Rotina: Desalinhamento no portal

* **[Ticket: 246650 / MRH-3097]** Alinhamento dos campos TELEFONE1, TELFONE2 e TELEFONE3 ao campo FAX no portal.

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: DIRF

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Informe de Rendimento conforme analise do validador

Arquivos: RM.Fop.Funcionario.Form.dll, RM.Fop.Informe.Data.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Informe.Data.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Informe.Data.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivos: RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Intf.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 - Alteração Informe de Rendimentos e DIRF Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 - Alteração Informe de Rendimentos e DIRF Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: FERIAS CALCULO FOP 34 402

* **[Ticket: 377451 / MRH-5560]** Ajuste no cálculo do INSS férias, para tratar o parâmetro "Limita desconto do INSS ao teto (férias em meses partidos)", quando o periodo de férias atingir 3 competências.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: IMPORTACAO DE DADOS DO RM LABORE LAB 01 26

* **[Ticket: 430388 / MRH-5932]** Ajuste log Historico assistencia a saude

Arquivo: RM.Fop.Importacao.Data.dll

### Rotina: PORTAL WEB GESTAO DE FERIAS LAB 01 208

* **[Ticket: 399693 / MRH-5403]** Acerto na busca de período aquisitivo na Sugestão de Férias pelo portal

Arquivo: RM.Fop.FuFerias.Data.dll

* **[Ticket: 372679 / MRH-5581]** Adição da legenda de férias na página de Gestão de Férias do portal

Arquivo: RM.Fop.FuFerias.WebForm.dll

### Rotina: RAIS

* **[Ticket: MRH-6149]** Otimizado RAIS para funcionários demitidos com projeção de aviso para o próximo ano e com rescisão complementar

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-5493]** Ajuste em rotina rais para verificação de seção de pagamento de adiantamento de 13º salário que era registrado com o mesmo valor em várias seções segundo o histórico de seções do funcionário.

Arquivo: RM.Fop.Dominio.dll

## TOTVS Framework

### Rotina: IMPRESSAO DELPHI REL 00008

* **[Ticket: 433331 / MFRWBH-1116]** O módulo 'Segurança e Saúde Ocupacional' compartilha o contexto com o módulo 'Gestão de Pessoas', com isso o código do sistema do seu contexto é o mesmo que do módulo 'Gestão de Pessoas' (Código V). Foi adicionada uma regra na seleção de Sistemas no cadastro de cubos para que permita somente a inclusão de sistemas com contextos validados pelos módulos do RM. Os cubos já cadastrados com o código do sistema igual a 'R' devem ser alterados para 'V'.

Arquivo: RM.Glb.Cadastros.Data.dll

### Rotina: RM X ECM GED SINCRONISMO DE USUARIO INT 00010

* **[Ticket: 415763 / MFRWBH-1073]** O Login no aplicativo RM.exe foi otimizado. Agora quando a integração SAML estiver ativa e possuir pendências na fila do Identity, a fila será processada.

Arquivos: RM.Lib.dll, RM.Lib.WinForms.dll, RM.Lib.Communication.Server.dll, RM.exe, RM.Lib.Server.dll, RM.Glb.IntegracaoFluig.Server.dll

## TOTVS Gestão Contábil

### Rotina: Ajuste nos Relatório para não limitarem tamanho de colunas em arquivo (TXT).

* **[Ticket: MEDU-2434]** Ajuste para permitir que relatórios emitidos em arquivo TXT não validem o tamanho das colunas permitindo que as ultrapassem a contagem especificadas para impressão como era feito nos relatórios antigos (Delphi).

Arquivos: RM.Ctb.Relatorios.Service.dll, RM.Ctb.Relatorios.Form.dll

### Rotina: RELATORIOS RAZAO CTB 38 114

* **[Ticket: 402631 / MEDU-2210]** Ajuste no subtítulo do relatório razão para que o calculo do espaçamento do saldo anterior seja calculado utilizando por base o valor absoluto do saldo.

Arquivos: RM.Ctb.Relatorios.Service.dll, RM.Ctb.Relatorios.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 383529 / MCP-1552]** Melhoria na cálculo da data de entrega

Arquivo: RM.Mov.CopiaMovimento.Service.dll

### Rotina: ORCAMENTO DE CONTRATO ORC 013

* **[Ticket: 355022 / MCP-1547]** Melhoria no processo de realocação orçamentária

Arquivo: RM.Ctr.Contrato.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS CURRICULOS EXTERNOS RHU 36 022

* **[Ticket: 240997 / MRH-3722]** Ajuste no enviar de e-mail customizado de esqueceu a senha

Arquivo: RM.Rhu.Curriculo.Server.dll

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 296409 / MRH-4571]** Acerto para excluir a Avaliação de Desempenho quando possui AD do mesmo código em coligada diferente e essa encontra-se finalizada.

Arquivo: RM.Rhu.AvalDesemp.Data.dll

## TOTVS Gestão Financeira

### Rotina: DOWNLOAD DE COTACOES FIN 133

* **[Ticket: 409242 / MEDU-2206]** Otimização no processo de download de cotações. Agora o sistema salva corretamente as configurações informadas na primeira utilização do download da moeda.

Arquivos: RM.Fin.Capital.Cadastros.Intf.dll, RM.Fin.Capital.Cadastros.Form.dll, RM.Fin.Capital.Cadastros.Data.dll

### Rotina: LANCAMENTO ALTERACAO FIN 172

* **[Ticket: 288333 / MEDU-1649]** Otimização ao clicar em Atualizar Filtros na visão de lançamentos e de extratos. Agora ao clicar em Atualizar Filtros na visão de lançamentos e de extrato o sistema respeita a configuração das colunas não restaurando para a configuração padrão.

Arquivos: RM.Fin.Lan.Form.dll, RM.Fin.Extrato.Form.dll

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 365927 / MEDU-2008]** Otimização no processo de baixa de um lançamento utilizando o meio de pagamento igual a cheque. Agora o sistema valida corretamente as opção inseridas no campo CPF/CNPJ da forma da opção marcada pelo usuário.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Lan.Form.dll

* **[Ticket: 365927 / MEDU-2008]** Otimização no processo de baixa de um lançamento utilizando o meio de pagamento igual a cheque. Agora o sistema valida corretamente as opção inseridas no campo CPF/CNPJ da forma da opção marcada pelo usuário.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: LANCAMENTO EMISSAO RECEBIMENTO DE CHEQUES FIN 197

* **[Ticket: 376123 / MEDU-2027]** Otimização no processo de emissão de cheque. Agora o sistema considera corretamente a parametrização default definida para a data de vencimento do cheque pré-datado.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: LANCAMENTO GERAR ACORDO FIN 199

* **[Ticket: 347457 / MEDU-2177]** Ajustado cálculo do valor líquido. Quando fórmula utilizada para cálculo de capitalização retornar valor negativo, esse valor será substituido por 0 (zero).

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RELATÓRIO - FLUXO DE CAIXA FIN230

* **[Ticket: 95193 / MEDU-2263]** Otimização no Relatório de Fluxo de Caixa pela MDI Delphi. Agora as opções de importar, exportar, incluir e etc, funcionam corretamente.

Arquivo: RM.Fin.FluxoCaixa.Form.dll

### Rotina: RETORNO DE PAGAMENTO FIN 238

* **[Ticket: 410571 / MEDU-2195]** Ajustado filtro do serviço de Cancelamento de baixa.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE FINALIZACAO LANCAMENTOS PARCIALMENTE BAIXADOS FIN 245

* **[Ticket: 380922 / MEDU-2258]** Apresentar os valores corretos ao calcular valor líquido de lançamentos que estão parcialmente baixados e com cheque emitido que possui fórmula no calculo de multa e juros ou juros/multa ao dia.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SESSAO DE CAIXA BAIXA FIN 269

* **[Ticket: 304816 / MEDU-1873]** Otimização no processo de impressão de relatório. Agora o sistema leva em consideração os filtros salvos do relatório no momento da impressão.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: Teste Sistêmico 12.1.16

* **[Ticket: EDUEDU001-1604]** Ajustes no pagamento de boleto via cartão.

Arquivo: RM.Fin.Lan.Data.dll

* **[Ticket: EDUEDU001-1604]** Ajustes no pagamento de boleto via cartão

Arquivo: RM.Fin.Lan.Data.dll

## TOTVS Gestão Fiscal

### Rotina: LANCAMENTO

* **[Ticket: MEDU-2186]** Implementada melhoria para sistema conseguir calcular corretamente o Valor do ICMS Interestadual mesmo com redução de base de cálculo do ICMSem lançamentos fiscais de entrada com diferencial de alíquota.

Arquivos: RM.Fis.LancFiscal.Intf.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.LancFiscal.Service.dll

### Rotina: PERIODO

* **[Ticket: MEDU-2356]** Na Calculo do Evento Tributário onde calcula os Prejuizos das Atividades Geral e Rural foram ajustadas para que seja considerado o Valor do Lucro Real após a compensação do prejuizo.

Arquivos: RM.Fis.RegrasTributarias.Service.dll, RM.Fis.ApuracaoTrb.Service.dll

* **[Ticket: MEDU-2356]** - No Calculo do Evento Tributário onde calcula os Prejuizos das Atividades Geral e Rural foram ajustadas para que seja considerado o Valor do Lucro Real após a compensação do prejuizo.- No processo "Gerar lançamentos automaticos Efeito Parte B" o lançamento Lalur B a ser gerado se proveniente de evento Atividade Rural o campo do Lançamento Lalur com mesmo nome será marcado e também foi implementado a consistência que verifica se a conta possui o Tributo cadastrado do lançamento que será gerado.

Arquivo: RM.Fis.RegrasTributarias.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: APURACAO E LANCAMENTO DE REPASSES SAU 47 1166

* **[Ticket: 395400 / MSAU-4962]** Ajuste realizado para que o código da tabela no xml seja o mesmo das condições contratuais caso não haja configuração de tabela específica ANS. (Ajuste solicitado pelo Bomba na props para conseguir gerar uma nova remessa.)

Arquivos: RM.Sau.Faturamento.Intf.dll, RM.Sau.Ans.Sever.dll

## TOTVS Incorporação

### Rotina: DIMOB GERACAO DE ARQUIVO POR EMPREENDIMENTO IMB 49 815

* **[Ticket: 360861 / MCP-1632]** Ajuste para visão de Venda e DIMOB tratar o Valor de Financiamento atualizado

Arquivos: RM.Imb.DIMOB.Server.dll, RM.Imb.Contratos.Data.dll, RM.Imb.Contratos.Server.dll

* **[Ticket: 413613 / MCP-1602]** Incidente: A DIMOB não estava considerando algumas parcelas pagas para alguns compradores devido ao horário de entrada dos mesmos no plano de financiamento, que estava sendo maior que o horário de baixa das parcelas (00:00:00)Solução: O horário de entrada dos compradores no plano de financiamento passou a ser desconsiderado ao buscar as parcelas pagas de cada comprador, validando-se apenas pela data.

Arquivo: RM.Imb.DIMOB.Server.dll

* **[Ticket: 360861 / MCP-1632]** Incidente:Ao gerar o arquivo da DIMOB, quando uma venda possui mais de um comprador (cada um com 50%) e o empreendimento possui repasse, o valor total da operação encontrado nos campos saem incorretos no arquivo. Estava saindo o valor de 100% (em relação ao total - repasse) para os dois compradoresSolução:Foi verificado que o sistema estava aplicando a porcentagem referente ao total - repasse em cima do valor total para os dois compradores, ao invés de aplicar sobre a metade do valor. O comportamento foi alterado para aplicar este valor em cima da porcentagem que cabe a cada comprador em questão.

Arquivo: RM.Imb.DIMOB.Server.dll

## TOTVS Manutenção

### Rotina: ORDEM DE SERVICO

* **[Ticket: MCP-1710]** Melhoria no processo de faturamento da OS

Arquivo: RM.Mnt.OrdemServico.Service.dll

## TOTVS Processo Seletivo

### Rotina: Teste Sistêmico 12.1.16

* **[Ticket: EDUEDU001-1604]** Cliente Piloto - Disponibilizado campos de indicação (Aluno, Fornecedor e Funcionário) no formulário de inscrição do novo portal.

Arquivos: FrameHTML

## TOTVS Segurança e Medicina do Trabalho

### Rotina: Filtro de Seleção - Seg. e Saúde Ocupacional

* **[Ticket: 220684 / MRH-3120]** Foi necessário criar uma condição para quando fosse funcionário, incluir o filtro personalizado. Pois o mesmo estava sendo ignorado.

Arquivo: RM.Smt.Pessoa.Data.dll

### Rotina: PPRA RECONHECIMENTO E AVALIACAO DE RISCO SMT 36 038

* **[Ticket: 437163 / MRH-6025]** Alterado a propriedade 'MaxLength' do campo 'NOMEFUNCAO' de 80 para 100. Mesmo tamanho da 'PFUNCAO.NOME'.

Arquivo: RM.Smt.Cadastros.Intf.dll

# 12.1.15.101

## TOTVS Automação de Ponto

### Rotina: CONFIGURACOES PARAMETRIZADOR SINDICATO PTO 35 1217

* **[Ticket: 413943 / MRH-5667]** Para corrigir o problema, os dados de evento são armazenados antes de serem deletados e em caso de erro de importação do XML, os dados previamente cadastrados são inseridos novamente.

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 436697 / MRH-6042]** No processo de importação de batidas, especificamente no método que identifica o funcionário pelo PIS, foi feita uma validação para funcionários com duas chapas.

Arquivos: RM.Pto.Funcionario.Intf.dll, RM.Pto.Horario.Data.dll, RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: ESPECIFICACAO DE PRODUTOS QIPA010

* **[Ticket: MRH-6424]** Otimizado o cálculo do horário semi-flexível quando o intervalo executado está dentro da ausência com tempo planejado.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: MANUTENCAO CATEGORIA PONTO ELETRONICO PE0180

* **[Ticket: MRH-6420]** Ajuste realizado na validação de interseção entre as faixas de extras na parametrização do sindicato quando a mesma é por intervalo.

Arquivo: RM.Pto.Parametros.Data.dll

### Rotina: PROCESSO DE CALCULO DE HORAS EXTRAS PTO 35 1238

* **[Ticket: 446604 / MRH-6173]** Ajuste realizado na montagem do grid das extras a serem aprovadas (Por intervalo)

Arquivo: RM.Pto.Extra.dll

### Rotina: PROCESSO DE CÁLCULO DE HORAS EXTRAS PTO351238

* **[Ticket: MRH-5655]** Foi ajustado um erro que ocorria na tela de lançamento de extra sintético por horas, de modo que, ao não determinar o número de horas de extra a aprovar não mais será apresentado o erro: “A cadeia de caracteres de entrada não estava em um formato incorreto.”

Arquivo: RM.Pto.Extra.dll

### Rotina: Project-398082 Visualização de ocorrências Project-398082

* **[Ticket: 398847 / MRH-5476]** Verificação do contexto do portal para utilizar um filtro com a chapa do funcionário logado. Dessa forma, na tela de ocorrências calculadas, apenas as informações do próprio funcionário são visualizadas.

Arquivo: RM.Pto.Ocorrencia.Data.dll

### Rotina: Réplica de correções de issues para RM Chronus 12.1.15

* **[Ticket: MRH-6268]** Merge dos changesets da versão 12.1.16 das issues apresentadas no chamado para a versão 12.1.15

Arquivo: RM.Pto.Extra.dll

## TOTVS Business Connect

### Rotina: CONSULTA MOVIMENTO DA INTEGRACAO LAB 01 96

* **[Ticket: 443463 / MRH-6248]** Acerto no script de criação da tabela HTPAGRECISAO para integração Folha de Pagamento x Averbação

Arquivo: RM.Con.ConfiguraIntegracao.TotvsFolhaTools.dll

### Rotina: Piloto Cetec

* **[Ticket: 309864 / EDUCTB001-538]** Ajuste na mensagem de Lista de Baixas na nova integração Educacional x Backoffice Protheus.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## TOTVS Construção e Projetos

### Rotina: APROPRIACAO DE SERVICOS INSUMOS PRJ 33 803

* **[Ticket: MCP-1691]** Erro na apropriação ao utilizar insumos com mais de 25 caracteres no código

Arquivos: RM.Prj.Insumo.Intf.dll, RM.Prj.CalculoFormula.Intf.dll, RM.Prj.Tarefa.Intf.dll

### Rotina: COMPOSICAO CADASTRO PRJ 33 809

* **[Ticket: 424908 / MCP-1652]** Ajuste realizado ao Copiar e Colar composição através do processo disponibilizado com o click direito do mouse

Arquivo: RM.Prj.Composicao.Data.dll

### Rotina: CONTRATOS CADASTRO PRJ 33 937

* **[Ticket: MCP-1687]** Importação MS-Excel para o Cronograma não está mantendo os registros quando informado 0 (zero) nas celulas, e não estava removendo os períodos que possuem valores com espaço em branco nas células.

Arquivos: RM.Prj.BackupRestore.Intf.dll, RM.Prj.Projeto.Form.dll, RM.Prj.GrupoCusto.Data.dll, RM.Prj.Parametros.Form.dll, RM.Prj.GrupoCusto.Intf.dll, RM.Prj.BackupRestore.Form.dll, RM.Prj.Composicao.Intf.dll, RM.Prj.Cronograma.Data.dll

### Rotina: CONTRATOS MEDICAO PRJ 33 941

* **[Ticket: MCP-1659]** Alteração do label da coluna Valor Retido para Valor Retido/Deduzido

Arquivo: RM.Prj.Contrato.Intf.dll

### Rotina: GERAR LANCAMENTO FINANCEIRO LANCAR CRONOGRAMA DE DESEMBOLSO PRJ 33 825

* **[Ticket: 401483 / MCP-1701]** Ajuste para identificar a natureza orçamentaria informada nos parâmetro de projeto ao executar o processo de gerar lançamentos financeiros do anexo "Cronograma de Desembolso / Lançamentos no Financeiro" em "Projetos | Planejamento | Gerar Lançamento Financeiro".

Arquivo: RM.Prj.IntegracaoFinanceiro.Data.dll

### Rotina: PERFIS SEGURANCA MENUS FRW 00057

* **[Ticket: 385570 / MCP-1544]** Mesmo com o perfil liberado para “inserir histórico de projeto” o sistema não libera a permissão se a opção “criar novo projeto” estiver liberada.

Arquivo: RM.Prj.Projeto.Form.dll

### Rotina: PLANILHAS TAREFAS PRJ 33 872

* **[Ticket: 444580 / MCP-1720]** Ajuste no processo de transformar cenário e principal para exibir os vínculos consistido ao validar a execução.

Arquivos: RM.Prj.Planilhas.Intf.dll, RM.Prj.Planilhas.Form.dll, RM.Prj.Planilhas.Data.dll

## TOTVS Educacional

### Rotina: CENSO

* **[Ticket: MEDU-2285]** Ajustes do Censo da Educação Superior 2016

Arquivos: RM.Edu.Consts.dll, RM.Edu.dll, RM.Edu.Academico.Form.dll, RM.Edu.Cadastros.Intf.dll, RM.Edu.Cadastros.Form.dll

* **[Ticket: MEDU-2489]** Ajuste na rotina de Importação de Dados do Censo Superior conforme leiaute 2016.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: Definição de bolsistas sem apontar a pessoa do bolsista

* **[Ticket: EDUEDU004-59]** Ajuste na parametrização de pesquisa e extensão para correta gravação do parametro de "Ativar “Bolsista responsável” na submissão de projeto de extensão"

Arquivo: RM.Edu.Parametros.Intf.dll

### Rotina: Erro ao cadastrar Turma Disciplina

* **[Ticket: 420214 / MEDU-2264]** Otimizado validação do cadastro de Avaliações para permitir que o código da prova permita digitar zero.Caso algum cliente queira especificamente bloquear o valor zero para o campo código da prova, deverá utilizar uma fórmula visual para emitir a mensagem de erro. A alteração afetará o cadastro de avaliações na Turma/Disciplina e no Período Letivo/ Modelo de avaliações por período letivo.

Arquivos: RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.PeriodoLetivo.Data.dll

### Rotina: Evoluções na Gestão de Estágio

* **[Ticket: EDUEDU004-1]** Ajustes no cadastro de funcionários na solicitação de estágio

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.dll, RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.MatrizCurricular.Server.dll, RM.Edu.MatrizCurricular.Data.dll, App\_Web\_eduestagiosolicitacaofuncionariowebform.ascx.1d4ca059.dll

### Rotina: GERACAO DE USUARIOS ALUNO PAIS RESPONSAVEIS EDU 50 231

* **[Ticket: MEDU-2278]** Melhoria no processo de geração de usuário, evitando que o usuário do responsável financeiro seja gerado sem necessidade no caso do responsável financeiro ser o aluno ou algum outro responsável (pai, mãe, responsável acadêmico), neste caso o sistema irá apenas vincular o usuário já gerado ao cliente/fornecedor.

Arquivos: RM.Edu.Processos.Server.dll, RM.Edu.Processos.Data.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: MEDU-2325]** Ajuste no processo de criação de comunidade no fluig (Academia social), possibilitando utilizar id de pasta do fluig utilizando grandes numerações.

Arquivo: RM.Edu.Lib.WinForms.dll

### Rotina: TURMAS DISCIPLINAS EDU 50 454

* **[Ticket: 433934 / MEDU-2371]** Verificação se horário da aula coincide com período de horário informado no feriado do calendário considerado para geração do plano de aula.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## TOTVS Folha de Pagamento

### Rotina: COMPARATIVO SEFIP X FOLHA ANALITICA LAB 01 49

* **[Ticket: 113931 / MRH-2509]** Remoção da opção de “Agendamento do Processo “ para possibilitar o cliente gerar SEFIP normalmente.

Arquivo: RM.Fop.Sefip.Form.dll

### Rotina: DIRF

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo - Alinhamento nas despesas de reembolso

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** DIRF 2017 - Dados do RRA quando há pensão alimentícia.

Arquivo: RM.Fop.Infraestrutura.Repositorios.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Informe.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Informe.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Informe.Data.dll

* **[Ticket: MRH-3260]** Implementação DIRF 2017 - Ajuste nas informações referente pensão do RRA

Arquivo: RM.Fop.Infraestrutura.Repositorios.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo. Quebra do nome do advogado campo 7 informações complementar em varias linhas para que não seja truncado e a apresentação fique compativel com o informe PDF

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: PROCESSOS ADMISSAO DE FUNCIONARIO FOP 34 466

* **[Ticket: 280093 / MRH-6198]** Acerto de vazamento de memória no cadastro de funcionários

Arquivo: RM.Fop.Funcionario.Form.dll

### Rotina: Project-390310 Não está trazendo identificação do funcionário ao selecionar algum na guia Subordinados Project-390310

* **[Ticket: 395242 / MRH-5357]** Correção de item de menu do portal que não deveria ser exibido

Arquivo: RM.Fop.Server.dll

### Rotina: RAIS

* **[Ticket: MRH-5493]** Ajuste em Rotina RAIS para forçar valor de R$0,01 ao mesmo mês de remuneração que o mês de rescisão quando não houver remuneração nos meses do ano base. A verificaação passa a Ser somente após o ajuste de verbas de diferença.

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-5493]** Ajuste em Rotina RAIS para forçar valor de R$0,01 ao mesmo mês de remuneração que o mês de rescisão quando não houver remuneração nos meses do ano base. A verificaação passa a Ser somente após o ajuste de verbas de diferença.

Arquivo: RM.Fop.Dominio.dll

### Rotina: RELATÓRIO TRCT FOP34546

* **[Ticket: 96211 / MRH-102]** Alterar o tratamento de arredondamento do valores gravados na tabela PFFERRESCTRCT, para evitar diferenças entre o relatório e os valores lançados no envelope de rescisão.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: RESCISAO CALCULO DE RESCISAO FOP 34 401

* **[Ticket: 402421 / MRH-5651]** Ajuste na apuração dos avos de férias proporcionais na rescisão quando ocorre extensão do periodo aquisitivo devido a afastamento.

Arquivo: RM.Fop.Calc.CalculosBase.dll

* **[Ticket: 298906 / MRH-3994]** Otimizado processo de transferência para copiar as informações do histórico de horário de jornada

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Framework

### Rotina: COMPOSICAO CADASTRO PRJ 33 809

* **[Ticket: 424908 / MCP-1652]** -Durante o processo de copiar e colar o sistema deve atribuir automaticamente os valores para as chaves primárias

Arquivo: RM.Lib.WinForms.dll

### Rotina: EXPRESSAO RPT 00021

* **[Ticket: MFRWBH-991]** Ao utilizar expressões que resultam em data o sistema deve exibir corretamente o resultado no relatório.

Arquivo: RM.Lib.dll

### Rotina: FORMULA VISUAL FVS 01

* **[Ticket: 450880 / MFRWBH-1148]** A fórmula visual deve ser executada corretamente dentro do seu objetivo final.

Arquivo: RM.Lib.Workflow.Activities.dll

### Rotina: INTERPRETAÇÃO DA DEMANDA: Erro apresentado ao utilizar metadados com campos do tipo data e hora : "Não é possível conve

* **[Ticket: 253582 / MFRWBH-1109]** Ajuste interno no grid contido em lookups para exibir colunas de horas corretamente.

Arquivo: RM.Lib.WinForms.dll

### Rotina: LOOKUP FRW00050

* **[Ticket: MFRWBH-1040]** Melhoria no componente de lookup para evitar que a descrição não seja carregada

Arquivo: RM.Lib.WinForms.dll

### Rotina: MDI FRW 00051

* **[Ticket: MFRWBH-1145]** -Ao utilizar a tradução com o menuserver habilitado o sistema deve ser traduzido normalmente.

Arquivo: RM.Lib.Server.dll

### Rotina: MENU

* **[Ticket: MFRWBH-1131]** Acerto do ícone do menu Código de Acesso

Arquivo: RM.Glb.dll

### Rotina: PARAMETRIZADOR LAB 01 33

* **[Ticket: MFRWBH-1127]** -Ao trocar de coligada deve-se verificar se o usuário tem permissão no módulo corrente. Caso não tenha permissão o sistema irá liberar uma lista dos módulos permitidos para seleção.

Arquivos: RM.Lib.WinForms.dll, RM.Lib.dll, RM.Lib.Server.dll, RM.exe

### Rotina: PERFIL

* **[Ticket: MFRWBH-1150]** Criação na árvore de permissões dos Serviços Globais as opções de Gerenciar e Incluir fluxo de trabalho

Arquivos: RM.Glb.dll, RM.Lib.WinForms.dll, RM.Glb.Server.dll

### Rotina: PLANILHA NET EXECUCAO BIS 00047

* **[Ticket: MFRWBH-1132]** As consultas SQL da planilha RM devem ser executadas em tempo hábil.

Arquivo: RM.Glb.PlanilhaNet.Windows.dll

### Rotina: RM X ECM GED SINCRONISMO DE USUARIO INT 00010

* **[Ticket: 415763 / MFRWBH-1073]** O Login no aplicativo RM.exe foi otimizado. Agora quando a integração SAML estiver ativa e possuir pendências na fila do Identity, a fila será processada.

Arquivos: RM.Glb.IntegracaoFluig.Server.dll, RM.Glb.IntegracaoFluig.Form.dll, RM.Lib.Server.dll, RM.Lib.Communication.Server.dll

## TOTVS Gerador de Relatórios

### Rotina: GERACAO DE RELATORIO RPT 00005

* **[Ticket: MFRWBH-1147]** -Ao realizar a previsualização do relatório que será impresso o sistema deve permitir o reajuste das margens.

Arquivo: RM.Rpt.Reports.Form.dll

## TOTVS Gestão Bibliotecária

### Rotina: PESQUISA PUBLICA BIB 10 1069

* **[Ticket: 444488 / MEDU-2413]** Ajuste na concorrência da pesquisa pública.

Arquivos: RM.Bib.Pesquisa.Server.dll, RM.Bib.Pesquisa.Data.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS RAZAO CTB 38 114

* **[Ticket: MEDU-2190]** O razão de c/f passa a buscar valores na CCONT, para se tornar compatível com o agrupamento.

Arquivo: RM.Ctb.Relatorios.Service.dll

* **[Ticket: 414975 / MEDU-2392]** Ajuste para permitir que relatório emitidos em arquivo TXT não validem o tamanho das colunas permitindo que as ultrapassem a contagem especificadas para impressão como era feito nos relatórios antigos (Delphi).

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CONSULTA SALDOS E CUSTOS EST005

* **[Ticket: MCP-1733]** Melhoria na visualização de saldos e custos do produto

Arquivo: RM.Est.Produto.Data.dll

### Rotina: CONTRATOS - MEDIÇÃO PRJ33941

* **[Ticket: MCP-1355]** Ajuste ao gerar contrato que utiliza medição nos items; valores das medições.

Arquivos: RM.Ctr.Contrato.Service.dll, RM.Ctr.Contrato.Data.dll

### Rotina: COTACAO VIA WEB COM 019

* **[Ticket: 392248 / MCP-1549]** Agora, ao acionar o botão salvar/fechar em uma cotação no portal, caso ocorra uma exceção por parte da fórmula visual, a sessão não será encerrada e a mensagem será exibida.

Arquivo: App\_Web\_cmpcotregorcamentowebform.ascx.49ff8280.dll

### Rotina: FATURAMENTORECEBIMENTO MOV007

* **[Ticket: MCP-1725]** Melhoria no faturamento de movimento parametrizado para editar município.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: FLUIG APROVACAO FATURAMENTO MOVIMENTO FLG 004

* **[Ticket: 279340 / MCP-1656]** Melhoria ao excluir item de movimento integrado com o Fluig.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: IMPORTACAO DE MOVIMENTO MOV 039

* **[Ticket: 415920 / MCP-1607]** Ajuste na geração do número das parcelas do pagamento.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: IMPORTAÇÃO DE MOVIMENTO MOV039

* **[Ticket: MCP-1736]** Melhoria no log de inclusão de redução Z via conceito

Arquivo: RM.Mov.CupomFiscal.Service.dll

### Rotina: IMPRIMIR MOVIMENTO MOV 023

* **[Ticket: 315120 / MCP-1380]** Ajuste ao acionar o processo de imprimir movimentos, quando a opção de renumerar está marcada.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO

* **[Ticket: MCP-1728]** Melhoria na inclusão de movimento. Ajuste na consistência quando o movimento está parametrizado para utilizar data de saida

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 357760 / MCP-1594]** Melhoria na inclusão de itens de movimento parametrizado para baixar estoque.

Arquivo: RM.Est.Baixa.Service.dll

* **[Ticket: 410823 / MCP-1662]** Ajuste no controle de visibilidade do campo Início Aproveit.Créd.Ativo.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: MOVIMENTACAO

* **[Ticket: MCP-1741]** Melhoria na visualização do cadastro de valores orçados

Arquivo: RM.Mov.Orcamento.Form.dll

### Rotina: MOVIMENTOS

* **[Ticket: MCP-1729]** Melhoria na inclusão de movimento. Ajuste no processo de retorno de industrialização efetuada por terceiros

Arquivos: RM.Mov.CopiaMovimento.Form.dll, RM.Mov.Processos.Form.dll, RM.Mov.Processos.Data.dll

### Rotina: O movimento de destino estamos marcando a opção “Consiste quantidade a maior mas não realizar a consistência corretament

* **[Ticket: 290255 / MCP-1278]** Ao faturar um movimento para outro que esteja com o parâmetro "Consiste Quantidade a Maior" marcado e o parâmetro "Visualizar Quantidade Original" desmarcado, o sistema ira realizar a consistência de quantidade corretamente.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: PARAMETRIZACAO TIPO DE MOVIMENTO PAR 014

* **[Ticket: 119174 / MCP-432]** Agora, a filial default será preenchida automaticamente no portal de acordo com a configuração do tipo de movimento selecionado.

Arquivos: Portal Corpore.Net

### Rotina: RECEBIMENTO DE MATERIAIS COM003

* **[Ticket: 95598 / MCP-176]** Ajuste no cálculo do ICMSST.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: REGERAR SALDOS E CUSTOS EST013

* **[Ticket: MCP-1730]** Melhoria na regeração de saldos e custos para produtos com serie

Arquivo: RM.Est.Estoque.Service.dll

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: MCP-1605]** Ao acionar o processo de inclusão de movimento via Arquivo XML, se a opção "Receber Pedido" for desmarcada, os campos referentes ao pedido na aba "Tradução de Itens" ficarão invisíveis, caso a mesma opção for marcada, os mesmos campos se tornarão visíveis automaticamente.

Arquivos: RM.Mov.Integracoes.Form.dll, RM.Mov.Integracoes.Intf.dll

* **[Ticket: MCP-1446]** Customização: Inclusão de códigos do Entry-Point da Modec.

Arquivos: RM.Mov.Customizacao.Intf.dll, RM.Mov.Integracoes.Service.dll

* **[Ticket: 346467 / MCP-1463]** Ajuste para não buscar o fuso horário da Data de Emissão do XML.

Arquivo: RM.Mov.Integracoes.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 96265 / MRH-6002]** Implementado o filtro por usuário no lookup Tipo de Anotação no cadastro de Anotações Pessoais para que respeite o filtro por usuário criado para a tabela PTPANOTACAO.

Arquivos: RM.Rhu.Pessoa.Intf.dll, RM.Rhu.Pessoa.Form.dll, RM.Rhu.Pessoa.Data.dll

## TOTVS Gestão Financeira

### Rotina: ACORDO ALTERACAO EXCLUSAO FIN 001

* **[Ticket: 98342 / MEDU-326]** Ajuste no processo de retorno bancário, para boletos que agrupam vários lançamentos, onde o sistema está parametrizado para substituir os valores calculados pelo sistema, pelos valores informados no arquivo de retorno bancario. O cálculo da proporção de cada valor dos lançamentos compoem o boleto foi otimizado.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: APLICACAO FINANCEIRA INTEGRACAO CONTABIL FIN 015

* **[Ticket: MEDU-2408]** Otimização no processo de Estorno Contábil e integração contábil. Agora o sistema realiza o processo corretamente.

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

### Rotina: BAIXAS REALIZADAS CANCELAMENTO DE ITEM DE BAIXA FIN 024

* **[Ticket: 225614 / MEDU-1521]** Otimização no processo de cancelamento de baixa. Agora o sistema faz o tratamento corretamente para acumular a retenção de acordo com o radical do CNPJ.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: BAIXAS REALIZADAS IMPRIMIR CHEQUES FIN 028

* **[Ticket: MEDU-2236]** Correção em tratamento de emissão de cheque, quando dois ou mais lançamentos associados ao mesmo boleto.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: BOLETO ALTERAR DATA DE VENCIMENTO FIN 036

* **[Ticket: 395690 / MEDU-2176]** Removida validação da data de alteração sendo menor que a data do sistema.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: CLIENTE FORNECEDOR INCLUSAO ALTERACAO EXCLUSAO FIN 104

* **[Ticket: 433854 / MEDU-2360]** Atualizar no cadastro de cliente/fornecedor as informações de "último Fornecedor" e "Último Cliente" após salvar um novo cliente/fornecedor.

Arquivos: RM.Fin.CliFor.Intf.dll, RM.Fin.CliFor.Data.dll, RM.Fin.CliFor.Form.dll

* **[Ticket: 398172 / MEDU-2162]** Ajustado cadastro de cliente fornecedor, a partir de agora, ao realizar a cópia do endereço principal para o endereço de entrega ou de pagamento, somente os campos que o usuário tem permissão de alteração serão copiados.

Arquivo: RM.Fin.CliFor.Form.dll

### Rotina: DESCONTO DE DUPLICATA DEVOLVER FIN 130

* **[Ticket: 385692 / MEDU-2087]** Ajustado processo de desconto de duplicata para passar a data do sistema para o serviço de cancelamento.

Arquivo: RM.Fin.Lan.Data.dll

### Rotina: LANCAMENTO

* **[Ticket: MEDU-2508]** Ajuste no Fonte FinMoedaMod para buscar cotações.

Arquivo: RM.Fin.Moeda.Service.dll

### Rotina: LANÇAMENTO - ANEXO RETENÇÕES ACUMULADAS FIN183

* **[Ticket: MEDU-1839]** Corrige apresentação de base de cálculo no recebimento via cheque.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 372773 / MEDU-2033]** Otimizada a busca das cotações de um Índice.

Arquivo: RM.Fin.Moeda.Service.dll

### Rotina: LANCAMENTO EMISSAO RECEBIMENTO DE CHEQUES FIN 197

* **[Ticket: 367953 / MEDU-2011]** Otimizado processo de baixa completa com cheque para preencher os dados do cheque no extrato.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Extrato.Service.dll

### Rotina: LANCAMENTO MANUTENCAO PARCELAMENTO FIN 209

* **[Ticket: 364373 / MEDU-2012]** Adicionado a Flag "Manter data de Vencimento" na tela de Processo do Parcelamento.

Arquivos: RM.Fin.Lan.IService.dll, RM.Fin.Lan.Form.dll, RM.Fin.Lan.Service.dll

### Rotina: PADRAO

* **[Ticket: MEDU-2300]** Melhoria no processo de download de cotação

Arquivo: RM.Fin.Capital.Lib.dll

### Rotina: REPLICA - ECF - Registro Q100: Demonstrativo do Livro Caixa

* **[Ticket: MEDU-2433]** Demonstrativo de Livro Caixa

Arquivos: RM.Fin.Lan.IService.dll, RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE CONTABILIZACAO FIN 323

* **[Ticket: 411933 / MEDU-2203]** Recriado o Parâmetro "Inverte default contábil de mútuo para extrato de saque"

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Parametros.Data.dll, RM.Fin.Extrato.IService.dll, RM.Fin.Parametros.Intf.dll, RM.Fin.Extrato.Service.dll, RM.Fin.Parametros.Form.dll

### Rotina: SERVICO DE VALIDACAO DA EXCLUSAO OPERACAO CONTABIL FIN 268

* **[Ticket: 415182 / MEDU-2395]** Ajustado serviço de regeração de contabilização integrada ao lote zero.A partir de agora, este serviço passa a informar a data de previsão da baixado lançamento para o serviço de contabilização do lançamento.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NF E CONSULTAR EVENTO TOTVS COLABORACAO NF 01 0034

* **[Ticket: 348512 / MEDU-2108]** Alteração no processo de consulta de evento de cancelamento do TOTVS Colaboração 1.0 para atender a demanda, onde, para TOTVS Colaboração deve ser utilizados os métodos "RetornaNotas" e "MonitorFaixa" na consulta de evento de Cancelamento.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 375930 / MEDU-2120]** Implementação da funcionalidade para poder enviar NF-e referenciando uma NFC-e.

Arquivos: RM.Fis.Utils.Server.dll, RM.Fis.NFe.Service.dll

* **[Ticket: 388689 / MEDU-2143]** Implementada melhoria no preenchimento da tag vprod, caso o cliente parametrize "Edita preço total" no tipo de movimento e marque a flag Preço Total Editado no item do movimento, será levado para a tag vprod o valor digitado no campo Preço total com a quantidade de casas decimais utilizada, informamos ao cliente sempre utilizar 2 para que o calculo não dê divergências.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 333473 / MEDU-2400]** Envio de NFS-e para Limeira-SP, parametrização de quando o ISS for retido (valissret maior que zero), a tag de valor do iss (valiss) deverá ir zerada.

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Lib.dll

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS ECF LI 01 0032

* **[Ticket: 349431 / MEDU-2010]** Implementação ECF Versão 3

Arquivos: RM.Fis.Filial.Intf.dll, RM.Fis.Lib.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Filial.Data.dll, RM.Fis.Filial.Form.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - ECF LI010032

* **[Ticket: 97128 / MEDU-215]** Implementação do Registro Y620 ECF - Participações Avaliadas Pelo Método de Equivalência Patrimonial

Arquivos: RM.Fis.Filial.Intf.dll, RM.Fis.Filial.Form.dll, RM.Fis.Filial.Data.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 413849 / MEDU-2292]** Alteração no layout do SPED Fiscal para que o campo 13 do registro 0200 aceite zeros a esquerda.

Arquivos: RM.Fis.Sped.Engine.dll, RM.Fis.Sped.Server.dll

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS

* **[Ticket: MEDU-675]** Atualização de contextos do Gerador de Saídas para serem utilizados pelo Layout TAF fiscal.

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Sped.Server.dll

## TOTVS Gestão Hospitalar

### Rotina: AUDITORIA INTERNA SAU 47 1143

* **[Ticket: 399746 / MSAU-5100]** Ao efetuar o Faturamento para convênios selecionando a opção "Gerar XML para terceiros" de contas que contenham MatMed é apresentado uma mensagem informando que a coluna "NGUIA" não pertence a tabela Lista. Alterado o sistema para faturar as contas sem apresentar a mensagem e gerar o XML.

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: Erro na rotina de lançamento automático de diárias

* **[Ticket: 411817 / MSAU-5052]** Ajuste realizado para que o sistema faça o lançamento de todas as diárias passíveis de lançamento sem criticar o usuário quando for através do job.

Arquivos: RM.Sau.Faturamento.Server.dll, RM.Sau.Common.Data.dll

### Rotina: erro no xml 3.01.01

* **[Ticket: 454817 / MSAU-5185]** Ao efetuar o faturamento e a geração de uma remessa do XML da versão 3.03.01 da tiss o sistema estava gerando os valores dos procedimentos zerado. Alterado o sistema para gerar o valor dos procedimentos corretamente ao gerar o XML da tiss versão 3.03.01.

Arquivo: RM.Sau.Produto.Intf.dll

## TOTVS Gestão Patrimonial

### Rotina: INTEGRACOES INTEGRACAO AQUISICOES COMPRAS RM NUCLEUS PAT 37 64

* **[Ticket: 368063 / MEDU-2439]** Atualização na rotina de cálculo das quantidades devolvidas do movimento

Arquivo: RM.Pat.Integracao.Service.dll

### Rotina: RELATORIOS RELATORIO DE DEPRECIACOES PAT 37 116

* **[Ticket: 122237 / MEDU-1286]** Implementação de 3 novos relatórios (Relatório de Depreciação Completo, Relatório de Depreciação Completo (Sintético) e Relatório de Depreciação Completo por Filial (Sintético))onde a coluna Depreciação / Realizações teve o valor do Ajuste Acumulada retirado para uma nova coluna, fazendo com que o valor da depreciação do período seja apresentado corretamente.

Arquivos: RM.Pat.Relatorio.Intf.dll, RM.Pat.Calculo.Service.dll, RM.Pat.Relatorio.Data.dll

### Rotina: UTILITARIOS REVISAO DE VIDA UTIL PAT 37 112

* **[Ticket: 339274 / MEDU-1925]** Atualização do processo de revisão de vida útil referente à data de início de vigência da taxa revista.

Arquivo: RM.Pat.Patrimonio.Service.dll

## TOTVS Incorporação

### Rotina: CONTRATOS IMB49813

* **[Ticket: 97890 / MCP-1]** Incidente: No TIN revitalizado existe o processo "Cancelar Contrato" em "Contratos de Venda", porém não existia a opção de controlar as permissões de acesso a este menu na árvore do "Cadastro de Perfis"Solução: Foi criada a opção na árvore do Cadastro de Perfis para controlar as permissões de acesso

Arquivo: RM.Imb.Venda.Contrato.Form.dll

### Rotina: DIMOB - LAYOUT IMB49816

* **[Ticket: MCP-1667]** Incidente:Foi verificado que a DIMOB estava considerando que a primeira parcela do segundo comprador era do primeiro, pois a data de pagamento era igual à data de troca de comprador.Solução: O processo foi alterado para que quando haja parcelas com data de pagamento igual à data de troca de comprador as mesmas fiquem sob a responsabilidade do novo comprador

Arquivo: RM.Imb.DIMOB.Server.dll

### Rotina: DIMOB GERACAO DE ARQUIVO POR EMPREENDIMENTO IMB 49 815

* **[Ticket: 413613 / MCP-1602]** Incidente: A DIMOB não estava considerando algumas parcelas pagas para alguns compradores devido ao horário de entrada dos mesmos no plano de financiamento, que estava sendo maior que o horário de baixa das parcelas (00:00:00)Solução: O horário de entrada dos compradores no plano de financiamento passou a ser desconsiderado ao buscar as parcelas pagas de cada comprador, validando-se apenas pela data.

Arquivo: RM.Imb.DIMOB.Server.dll

### Rotina: DISTRATO BILATERAL IMB 49 817

* **[Ticket: 407961 / MCP-1608]** Alterada a consulta SQL que obtém os dados da subunidade para desconsiderar vendas com distrato efetivado.

Arquivo: RM.Imb.Venda.Empreendimento.Data.dll

### Rotina: EMPREENDIMENTO CADASTRO IMB 49 823

* **[Ticket: 312331 / MCP-1354]** Incidente: Após preencher uma vez os campos de combobox do cadastro de empreendimento na aba "EFD-PIS/Cofins" o sistema não permitia limpá-los.Solução: Foi adicionada uma nova opção em branco para que o usuário possa limpar o campo (é a primeira opção da lista).

Arquivos: RM.Imb.Venda.Empreendimento.Form.dll, RM.Imb.Venda.Lib.Intf.dll

### Rotina: REAJUSTE

* **[Ticket: MCP-1383]** Incidente:No processo de Atualização da Data do Reajuste, havia duas colunas com a label fora do padrão:"- Venda: " e "DataReajuste: {0}"Solução: As labels foram respectivamente trocadas por "Venda" e "Data Reajuste"

Arquivo: RM.Imb.Contratos.Data.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 400605 / MCP-1575]** Ajuste realizado para que a CM Antes e o Juros Antes sejam considerados apenas uma vez como base de cálculo para CM Após e Juros Após respectivamente

Arquivo: RM.Imb.Reajuste.Server.dll

### Rotina: RESÍDUO DE CM IMB49855

* **[Ticket: 97917 / MCP-9]** Mudança na label do campo XREGRACOMPONENTEVENDA.PARCELAFORAPERIODO de "Não gerar resíduo no reajuste das parcelas fora do período" para "Reajustar mensalmente as parcelas fora do período de resíduo"

Arquivo: RM.Imb.Recursos.dll

### Rotina: TABELA DE PRECOS IMB 49 860

* **[Ticket: 337482 / MCP-1443]** Incidente:Foi verificado que o processo não estava sendo concluído, pois o sistema estava informando que na planilha importada não havia informação de preço para todas as subunidades do empreendimento. Na versão 12.1.14 este processo havia sido modificado e não mostrava o log de quais subunidades foram importadas e quais não foram. Então foi feita uma segunda mudança para mostrar este log, contudo, quando o log era exibido, não era possível concluir o processo somente com as subunidades importadasSolução:O comportamento do sistema foi alterado para permitir que se conclua o processo mesmo quando houver warnings, desde que pelo menos uma subunidade tenha sido importada com sucesso. O warning continuará sendo exibido, porém permitirá avançar para a próxima etapa do processo

Arquivo: RM.Imb.TabelaPreco.Form.dll

### Rotina: VENDA CADASTRO

* **[Ticket: MCP-1588]** Incidente:\* No aditivo de troca de comprador, quando houver mais de um comprador, ambos devem ser incluídos com a mesma data/hora. Foi verificado que atualmente no sistema, a inclusão é feita utilizando DateTime.Now e isso pode gerar inconsistências ao gerar o arquivo da DIMOB. Se houver uma diferença de alguns segundos, o sistema considera que os compradores foram incluídos separadamente e atribui 100% da compra para cada um deles. \* Na inclusão de compradores, deve-se sugerir o horário 00h00 para a inclusão de todos os compradores, para evitar que os mesmos fiquem com horários diferentesSolução:\* O aditivo foi alterado para incluir todos os compradores com exatamente o mesmo horário \* A inclusão de compradores foi alterada para sugerir o horário 00h00 no campo "data de entrada"

Arquivos: RM.Imb.Aditivos.Server.dll, RM.Imb.Contratos.Form.dll

* **[Ticket: MCP-1588]** A inclusão de compradores foi alterada para sugerir o horário 00h00 no campo "data de entrada"

Arquivo: RM.Imb.Contratos.Form.dll

## TOTVS Planejamento e Controle da Produção

### Rotina: BAIXA DE MATERIAIS PCP 44 285

* **[Ticket: 448056 / MCP-1699]** Acerto na baixa para considerar o lote associado aquele foi empenhado.

Arquivo: RM.PCP.BaixaMateriais.Service.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: Afastamento

* **[Ticket: 98802 / MRH-704]** Realizado ajuste no cadastro de Atestados para que ao alterar o "Motivo" de um atestado lançado, o motivo do Histórico de situação e do Histórico de Afastamento também seja alterado automaticamente.

Arquivo: RM.Smt.Pessoa.Data.dll

### Rotina: CONTROLE DE EXAMES AGENDA DE EXAMES SMT 36 001

* **[Ticket: 410868 / MRH-5754]** Criado um evento na opção funcionario, que filtra os dados por coligada corrente.

Arquivo: RM.Smt.Lib.Form.dll

### Rotina: RELATORIOS TIPOS DE RELATORIOS SMT 36 044

* **[Ticket: 239942 / MRH-6259]** Ajustado a função que carrega os riscos, passando a data correta quando a data do exame é inferior a data de admissão.

Arquivo: RM.Smt.Pessoa.Data.dll

# 12.1.15.102

## TOTVS Automação de Ponto

### Rotina: ALTERACAO SOCIAL

* **[Ticket: MRH-6491]** Melhoria de performance na importação de batidas

Arquivos: RM.Pto.Contexto.Server.dll, RM.Pto.ImportacaoExportacao.Intf.dll, RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 353126 / MRH-5775]** Otimizado a importação de batidas de forma que seja evitado o erro de chave na tabela AAFDT.

Arquivos: RM.Pto.ImportacaoExportacao.Data.dll, RM.Pto.Common.Intf.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** Ajuste na conversão do endereço do Host

Arquivo: RM.Upg.Server.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS CADASTRO PRJ 33 937

* **[Ticket: 475227 / MCP-1752]** Verificado o cadastro de Contratos, quando o parâmetro Consistir datas do Contrato for selecionado para o projeto do contexto.

Arquivo: RM.Prj.Contrato.Data.dll

## TOTVS Educacional

### Rotina: Classificação dos projetos após aprovação

* **[Ticket: EDUEDU004-62]** Implementação da alteração de situação do projeto de pesquisa.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.dll, RM.Edu.MatrizCurricular.Server.dll, RM.Edu.PesquisaExtensao.Data.dll, RM.Edu.PesquisaExtensao.Form.dll, RM.Edu.Server.dll

### Rotina: Fluxo de aprovação de criação de aluno

* **[Ticket: EDUEDU004-11]** Página publica de cadastro de egresso foi ajustada para atender ao padrão

Arquivos: Portal Corpore.Net

### Rotina: RESERVA DE RECURSO E INSTALAÇÃO EDU50425

* **[Ticket: MEDU-2482]** Melhoria na usabilidade do processo de alocação manual de salas.

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3763]** Legislação DIRF: No Informe txt foi implementado a Quebra do nome do advogado no campo 7 conforme é feito no portal e pdf

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** Otimizado geração da DIRF quando utiliza declarante pessoa física.

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: DIRF LAB 01 11

* **[Ticket: 466706 / MRH-6488]** Otimizado geração da DIRF quando utiliza declarante pessoa física.

Arquivos: RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Intf.dll

### Rotina: RESCISAO CALCULO DE RESCISAO FOP 34 401

* **[Ticket: 451628 / MRH-6450]** Otimizado rescisão de estagiário quando o mesmo não possui sindicato informado

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Framework

### Rotina: RM X ECM GED SINCRONISMO DE USUARIO INT 00010

* **[Ticket: 415763 / MFRWBH-1073]** O Login no aplicativo RM.exe foi otimizado. Agora quando a integração SAML estiver ativa e possuir pendências na fila do Identity, a fila será processada.

Arquivo: RM.Glb.IntegracaoFluig.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CONTRATOS - MEDIÇÃO PRJ33941

* **[Ticket: MCP-1355]** Ajuste ao gerar contrato que utiliza medição nos items; valores das medições.

Arquivo: RM.Ctr.Contrato.Form.dll

### Rotina: INCLUSAO DE MOVIMENTO

* **[Ticket: MCP-1754]** Melhoria no processo de estoque de movimentos.

Arquivo: RM.Est.Baixa.Service.dll

### Rotina: ITENS DE CONTRATO RELACIONADOS MOV036

* **[Ticket: 98979 / MCP-227]** As informações que estão sendo inseridas ou apagadas do campo Observação não estão sendo salvas ao navegar entre os itens.

Arquivo: RM.Ctr.Contrato.Form.dll

## TOTVS Gestão Fiscal

### Rotina: NF E SALVAR XML NF 01 0049

* **[Ticket: 192389 / MEDU-1666]** Alteração no processo de salvar XML da CC-e quando utilizado RM.Host.Service.exe

Arquivos: RM.Fis.NFe.Form.dll, RM.Fis.NFe.Service.dll, RM.Fis.NFe.Data.dll

## TOTVS Incorporação

### Rotina: ADITIVO ANTECIPACAO DE PARCELA IMB 49 781

* **[Ticket: 194460 / MCP-1392]** Melhoria na chamada para cálculo de juros e multa do TIN para o Fluxus. Foi alinhado a utilização dos parâmetros que determinam se irá utilizar valores reajustados até a data presente ou utilizar valores existentes na base de dados.

Arquivos: RM.Imb.Contratos.Server.dll, RM.Imb.Parametros.Data.dll, RM.Imb.Aditivos.Server.dll, RM.Imb.Facade.dll, RM.Imb.Parametros.Form.dll

### Rotina: DIMOB GERACAO DE ARQUIVO POR EMPREENDIMENTO IMB 49 815

* **[Ticket: 467627 / MCP-1734]** Alterado para gerar no registro R01 do DIMOB o código do município da Coligada e no R03 o código do município do Empreendimento

Arquivo: RM.Imb.DIMOB.Server.dll

### Rotina: EMPREENDIMENTO CADASTRO IMB 49 823

* **[Ticket: 392916 / MCP-1567]** Incidente:Não estava sendo possível alterar o campo "Quantidade Apto" no cadastro de torres para um número menor do que já estava preenchido. Foi verificado que o sistema estava fazendo uma validação indevida. Solução:A validação foi alterada para funcionar da seguinte forma: 1. O campo "Quantidade Apto" pode ficar em branco apenas se não houver nenhum apto cadastrado. 2. Se houver pelo menos um apto cadastrado, o campo "Quantidade Apto" deverá ser obrigatoriamente preenchido com um valor maior ou igual ao número de aptos cadastrados. 3. Só é possível cadastrar um novo apto caso a quantidade de aptos já cadastrados ainda não seja igual ao número definido no campo "Quantidade Apto" (quantidade máxima), caso contrário será necessário alterar este campo antes de concluir o cadastro do novo apto. 4. Ao cadastrar o primeiro Apto da torre, caso o campo "Quantidade Apto" esteja em branco, será necessário preenchê-lo antes que se conclua o cadastro

Arquivo: RM.Imb.Venda.Empreendimento.Data.dll

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhoria no menu client

Arquivos: RM.Imb.dll, RM.Imb.Facade.dll

## TOTVS Processo Seletivo

### Rotina: Teste Sistêmico 12.1.16

* **[Ticket: EDUEDU001-1604]** Otimização da rotina de carregamento de lista de processos seletivos, arquivos e download de arquivos por processo seletivo no novo portal.

Arquivos: RM.EduPS.Cadastros.Server.dll, RM.EduPS.Cadastros.Data.dll, RM.Edu.Cadastros.Form.dll

# 12.1.15.103

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3260]** DIRF 2017 - Unificação dos dados do plano de saúde quando utiliza múltiplos vínculos.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RAIS

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS para levar corretamente motivo de desligamento

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-6143]** Ajuste no processo da geração da RAIS quando a opção "Gerar registro para alteração de cei"

Arquivo: RM.Fop.Dominio.dll

### Rotina: VALIDAÇÃO DA BASE DE DADOS

* **[Ticket: 456843 / MRH-6391]** Ajustes na validação do histórico de situação durante validação da base de dados

Arquivo: RM.Fop.Rotinas.Server.dll

## TOTVS Framework

### Rotina: PAINEL DE METAS IMPORTACAO EXPORTACAO BIS 00043

* **[Ticket: 452396 / MFRWBH-1156]** -Ao importar o painel de metas é necessário informar a fonte de dados e após salvar as alterações o serão exibidos os gráficos referentes ao painel.

Arquivo: RM.Glb.ImpExp.Server.dll

## TOTVS Gestão Financeira

### Rotina: PADRAO

* **[Ticket: MEDU-2565]** Corrigido parametrizador quanto ao ID 1100

Arquivo: RM.Fin.Parametros.Data.dll

## TOTVS Gestão Hospitalar

### Rotina: Erro na rotina de cópia de diárias

* **[Ticket: 207253 / MSAU-4143]** Ajuste realizado para que o sistema faça a cópia das diárias de um convênio para outro corretamente.

Arquivos: RM.Sau.CadastrosFat.Form.dll, RM.Sau.CadastrosFat.Server.dll

# 12.1.15.105

## TOTVS Automação de Ponto

### Rotina: HORARIOS PTO 35 1180

* **[Ticket: 258988 / MRH-3670]** Ajustada a rotina de visualização de horário no espelho, para que seja exibida jornada de descanso.

Arquivo: RM.Pto.VisualizarHorario.Data.dll

### Rotina: TREINAMENTO TURMAS RHU 36 055

* **[Ticket: 209504 / MRH-6511]** Alterações no processo integrado de abonos com o RM Vitae, com o objetivo de processar as informações necessárias.

Arquivos: RM.Pto.Lib.Intf.dll, RM.Rhu.Utils.Server.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS ASSOCIACAO DE ITENS PRJ 33 939

* **[Ticket: 454999 / MCP-1763]** Verificar o saldo do objeto (insumo) selecionado no contrato, através do processo que realiza o rateio de contrato no pedido de material.

Arquivo: RM.Prj.PedidoMaterial.Data.dll

### Rotina: CURVA S PRJ33818

* **[Ticket: 97101 / MCP-50]** Otimizando o processo de geração de solicitação de material.

Arquivos: RM.Prj.Calculo.Form.dll, RM.Prj.Calculo.Server.dll, RM.Prj.PedidoMaterial.Intf.dll, RM.Prj.PedidoMaterial.Form.dll, RM.Prj.PedidoMaterial.Server.dll

## TOTVS Educacional

### Rotina: Alocação de Sala e Reserva de Sala e Recurso [Alterar a reserva, sem precisar cancelar e criar nova]

* **[Ticket: EDUEDU001-707]** Acerto no choque de horario da reserva de recurso quando vinculada a reserva de instalacao.

Arquivos: RM.Edu.Academico.Server.dll, RM.Edu.Professor.Server.dll, RM.Edu.Interfaces.Intf.dll

### Rotina: CONTRATOS BOLSA EDU 50 140

* **[Ticket: MEDU-2487]** Foi realizada otimização do processo de baixa de lançamentos financeiros, permitindo ao sistema, baixar uma lançamento com bolsas escalonáveis e especiais quando o sistema não estiver parametrizado para utilizar escalonamento de bolsas.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: PORTAL PROFESSOR UPLOAD MATERIAIS EDU 50 386

* **[Ticket: MEDU-2473]** Ajuste na passagem das chaves para o anexo do arquivo quando parametrizado com a integração ECM para que não ocorra erro de referência de objeto.

Arquivos: Portal Corpore.Net

### Rotina: RESERVA DE RECURSO E INSTALAÇÃO EDU50425

* **[Ticket: MEDU-2482]** Ajuste na tela de alocação manual de salas para melhorar a visualização de seus componentes.

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 445479 / MEDU-2558]** Otimização no processo de baixa integrada ao Protheus. A alteração fopi alterar o fonte ACCOUNTRECEIVABLEDOCUMENTDISCHARGE da integração TOTVS Educacional x BackOffice Protheus com a funcionalidade de que quando realizar a baixa via Protheus e o mesmo não possui a informação do banco, é então informado o dado do banco a partir do próprio lançamento.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** DIRF 2017 - Otimizado pensão de décimo terceiro do RRA

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 - Alteração Informe de Rendimentos e DIRF Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Informe.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: Erro na rotina de Escala de Férias

* **[Ticket: 100044 / MRH-656]** Ao realizar o processo de “Escala de Férias” o sistema está apresentado seguinte erro:Given cell at position (2,3), intersects with another cell at position (1,3) 'JANEIRO'O erro é apresentando quando é salvo um perfil para este processo no qual selecionou-se a opção de escala anual. Foi feita uma correção para sanar o erro.

Arquivo: RM.Fop.Lib.WinForms.dll

### Rotina: FUNCOES LAB 01 183

* **[Ticket: 301419 / MRH-3773]** Desfazendo alteração de validação ao inativar função

Arquivo: RM.Fop.Cadastros.Data.dll

* **[Ticket: 301419 / MRH-3773]** Validação da existência de funcionários ao desativar função

Arquivo: RM.Fop.Cadastros.Data.dll

* **[Ticket: 301419 / MRH-3773]** Validação da existência de funcionários ao desativar função

Arquivos: RM.Fop.Funcionario.Intf.dll, RM.Fop.Cadastros.Form.dll, RM.Fop.Funcionario.Server.dll

* **[Ticket: 466571 / MRH-6568]** Ajuste na alteração global de campos de funcionário para permitir inserção de histórico na alteração de nível salarial

Arquivos: RM.Fop.Rotinas.Data.dll, RM.Fop.Rotinas.Form.dll

### Rotina: INFORME DE RENDIMENTOS FOP 34 431

* **[Ticket: 431090 / MRH-5945]** DIRF 2017: Otimizado dedução de dependente quando há diferente de férias.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RAIS

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Infraestrutura.Repositorios.dll

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivos: RM.Fop.Infraestrutura.Repositorios.dll, RM.Fop.Dominio.dll

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Dominio.dll

## TOTVS Framework

### Rotina: HOST FRW00038

* **[Ticket: MFRWBH-1176]** Ajuste para o Broker não ser deletado.

Arquivo: RM.Host.Service.exe

## TOTVS Gerador de Relatórios

### Rotina: ARVORE DO RELATORIO RPT 00037

* **[Ticket: 421525 / MFRWBH-1164]** O processo de geração de relatórios foi otimizado.

Arquivos: RM.Rpt.Executor.Service.dll, RM.Rpt.Reports.Form.dll

## TOTVS Gestão Contábil

### Rotina: GESTAO RM CONECTOR CTB 39 005

* **[Ticket: 293826 / MEDU-2072]** Evolução na rotina que importa lançamentos via conceito para que seja possível realizar o processo utilizando o código reduzido das contas contábeis.

Arquivos: RM.Ctb.Lan.Data.dll, RM.Ctb.Lan.Service.dll, RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E RELATORIO CTE 004

* **[Ticket: 415981 / MCP-1706]** Melhoria para exibir o CPF (caso ele exista) no DACTe

Arquivo: RM.Mov.Reports.Server.dll

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 460737 / MCP-1782]** Melhoria no processo de devolução.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 349724 / MCP-1705]** Acerto para considerar as casas decimais no Rateio de acordo com o parametro de valores.

Arquivo: RM.Mov.Movimento.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: Gestão de Pessoas - Problemas na criação do Perfil de Vaga

* **[Ticket: 354307 / MRH-4690]** Ajuste em exibição de campos em tela de Perfil de Vagas / Definições

Arquivo: RM.Rhu.Captacao.Form.dll

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 395803 / MRH-5648]** Ajuste realizado ao cancelar o cadastro do funcionário fechando o formulário através do botão fechar.

Arquivo: RM.Rhu.Lib.WinForms.dll

### Rotina: REQUISICOES ALTERACOES DE DADOS FUNCIONAIS RHU 36 505

* **[Ticket: 399199 / MRH-5568]** Ajuste no tempo de função na listagem de requisição

Arquivo: RM.Rhu.Requisicao.Server.dll

### Rotina: REQUISICOES DESLIGAMENTO RHU 36 503

* **[Ticket: 423928 / MRH-6015]** Realizado ajuste no processo de cancelamento de requisições.

Arquivo: RM.Rhu.Requisicao.Server.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO

* **[Ticket: MEDU-2567]** Otimização de performance no processo de baixa de lançamento

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NF-E ENVIO NF010045

* **[Ticket: 94397 / MEDU-275]** Envio de NFS-e para São Paulo - SP, quando parametrizado optante pelo simples nacional com tributação (T – Tributado em São Paulo).

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: ACH

* **[Ticket: 480891 / MSAU-5344]** Ajuste para correto preenchimento do sequencial de longa permanência para AIHs do tipo 7.

Arquivo: RM.Sau.Sus.Server.dll

### Rotina: Ao atender requisição de um item com a quantidade "2" e bipar lotes diferentes, o sistema não grava no XML o 2° Lote

* **[Ticket: 309241 / MSAU-4036]** Ao processar um mapa de dispensação com item selecionando dois lotes diferentes, não estava sendo enviado na integração os dois lotes, somente um destes. Alterado o sistema para quando for selecionado mais de um lote para o mesmo item, ser enviado na integração os lotes selecionados.

Arquivo: RM.Sau.Produto.Server.dll

### Rotina: Cronograma de pagamento do Convênio

* **[Ticket: 198987 / SAUHRM02-596]** Correção no ID do parâmetro CopiaAnamneseEspecial

Arquivo: RM.Sau.Parametros.Intf.dll

### Rotina: erro no xml 3.01.01

* **[Ticket: 454817 / MSAU-5185]** Ao efetuar o faturamento e a geração de uma remessa do XML da versão 3.03.01 da tiss o sistema estava gerando os valores dos procedimentos zerado. Alterado o sistema para gerar o valor dos procedimentos corretamente ao gerar o XML da tiss versão 3.03.01.

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: Homologar RM para TISS 3.03.01

* **[Ticket: 345293 / MSAU-4574]** Realizado ajuste para não enviar a tag <ans: indicacaoClinica> quando solicitamos a autorização de guia pela agenda de atendimentos.

Arquivos: RM.Sau.AgendaAtendimento.Form.dll, RM.Sau.Ans.Sever.dll

### Rotina: Lentidão no controle de documentos - Confirmar vários registros

* **[Ticket: 334802 / MSAU-4119]** Melhoria implementada na performance das consultas da base de dados no controle de documentos.

Arquivo: RM.Sau.ControleDocumentos.Data.dll

### Rotina: Registro de Informações Cirúrgicas

* **[Ticket: 436555 / MSAU-5150]** Ajustado o envio de dados para faturamento para que o sistema envie para a conta os itens da cirurgia.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: RÉPLICA para 12.1.16 - RM Saude - Erro ao buscar a mãe no cadastro de recém nascido.

* **[Ticket: MSAU-5137]** Ao acessar o sistema TOTVS Gestão Hospitalar, ir ao menu Atendimento/Internação/Cadastro de Recém Nascido, cadastrar um novo RN, buscar pela mãe na aba "Atendimentos do dia" era gerada a mensagem "A coluna 'Sexo' não pertence a tabela de Atendimento".

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: Valor Brasindice

* **[Ticket: 196992 / MSAU-3996]** Ajuste para correto cálculo de itens com fracionamento

Arquivos: RM.Sau.Produto.Intf.dll, RM.Sau.Produto.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: UTILITARIOS FECHAMENTO DE PERIODO PAT 37 93

* **[Ticket: 398246 / MEDU-2183]** \* Atualização da leitura dos parâmetros de ano/mes do sistema

Arquivos: RM.Pat.Parametros.Intf.dll, RM.Pat.Parametros.Data.dll, RM.Pat.Periodicidade.Data.dll

## TOTVS Incorporação

### Rotina: ADITIVO ANTECIPACAO DE PARCELA IMB 49 781

* **[Ticket: 194460 / MCP-1392]** Melhoria na chamada para cálculo de juros e multa do TIN para o Fluxus. Foi alinhado a utilização dos parâmetros que determinam se irá utilizar valores reajustados até a data presente ou utilizar valores existentes na base de dados.

Arquivo: RM.Imb.Parametros.Data.dll

* **[Ticket: 194460 / MCP-1392]** Melhoria na chamada para cálculo de juros e multa do TIN para o Fluxus. Foi alinhado a utilização dos
  parâmetros que determinam se irá utilizar valores reajustados até a data presente ou utilizar valores
  existentes na base de dados.

Arquivo: RM.Imb.Facade.dll

### Rotina: ALUGUEL EVENTO FINANCEIRO IMB 49 776

* **[Ticket: 117886 / MCP-796]** Alterada a rotina de verificação de habilitação do cancelamento do lançamento financeiro para levantar exceção e manter a sincronicidade entre a parcela de aluguel e o lançamento financeiro.

Arquivo: RM.Imb.Aluguel.Lancamento.Server.dll

## TOTVS Processo Seletivo

### Rotina: QUERO ME INSCREVER PORTAL EDUPS 20 1083

* **[Ticket: 485584 / MEDU-2584]** Ajuste na exibição de processos seletivos pelo portal.

Arquivo: RM.EduPS.PgPrincipal.Data.dll

* **[Ticket: 485584 / MEDU-2584]** Ajuste na exibição de processos seletivos pelo portal.

Arquivo: App\_Web\_edupsinscricaoareaofertada.ascx.58ed3fed.dll

### Rotina: Teste Sistêmico 12.1.16

* **[Ticket: EDUEDU001-1604]** Tratamento dos campos do tipo checkbox para gravar o valro correto

Arquivo: RM.EduPS.Rest.Server.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: CONTROLE DE EXAMES AGENDA DE EXAMES SMT 36 001

* **[Ticket: 424274 / MRH-6571]** Alterado o valor default da QueryValue para ZERO.

Arquivo: RM.Smt.Clinico.Data.dll

### Rotina: FUNCIONARIOS DADOS INDIVIDUAIS PTO 35 1181

* **[Ticket: 121521 / MRH-3196]** No processo de cadastro de atestados, foi inserida uma verificação para o respectivo funcionário em relação a utilização do cartão de ponto. É verificado se, caso o funcionário não utilize cartão de ponto na data de início do afastamento, é permitido o cadastro de atestados fora do período ativo. Caso contrário, é feita a validação do Chronus.

Arquivos: RM.Pto.Funcionario.Data.dll, RM.Smt.Facade.dll, RM.Smt.Pessoa.Data.dll, RM.Smt.Pessoa.Form.dll, RM.Pto.Lib.Intf.dll, RM.Smt.Pessoa.Intf.dll

### Rotina: PCMSO x PPRA 12.1.15

* **[Ticket: RHRHU001-313]** Melhorias no processo de geração de exames pelo PPRA

Arquivos: RM.Fop.Calc.Interfaces.dll, RM.Smt.Clinico.Intf.dll, RM.Fop.Facade.dll, RM.Fop.Rescisao.Data.dll, RM.Fop.Rescisao.Form.dll, RM.Smt.Clinico.Data.dll, RM.Smt.Pessoa.Data.dll, RM.Fop.Calc.Calculos.dll

### Rotina: SMT COMISSAO INTERNA DE PREVENCAO DE ACIDENTES CIPA SMT 36 012

* **[Ticket: 440247 / MRH-6393]** O erro estava sendo gerado, pois o sistema não deixa inserir o candidato com a mesma coligada e data.Inserido uma mensagem de erro quando o candidato já tem uma estabilidade cadastrada na mesma coligada e data.

Arquivo: RM.Smt.Cipa.Data.dll

* **[Ticket: 440247 / MRH-6393]** Estava aparecendo o texto '<BR<BR>', ajustado a mensagem de erro

Arquivo: RM.Smt.Cipa.Data.dll

# 12.1.15.106

## TOTVS Educacional

### Rotina: ALTERAR PLANO DE PAGAMENTO EDU 50 008

* **[Ticket: MEDU-2124]** Sistema passou a buscar as informações do plano de pagamento por período no anexo de planos de pagamento, anteriormente, o sistema mostrava os valores zerados.

Arquivos: RM.Edu.Matricula.Intf.dll, RM.Edu.Matricula.Data.dll, App\_Web\_edumatriculaonlinecontratofinanceiro.aspx.f55b27f4.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivos: RM.Fop.Informe.Data.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: PORTAL WEB ENVELOPE PGTO LAB 01 206

* **[Ticket: 215646 / MRH-2875]** Ajuste na impressão de eventos do modelo Lab04 de envelope de pagamento do portal

Arquivo: RM.Fop.Envelope.Data.dll

### Rotina: RAIS

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Dominio.dll

### Rotina: Restituição / Arredondamento.

* **[Ticket: 306401 / MRH-5815]** Ajuste no cálculo do IRRF, para efetuar o abatimento do valor já descontado no mês, após arredondar o desconto calculado.

Arquivo: RM.Fop.Calc.CalculosBase.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 393265 / MCP-1800]** Melhoria no faturamento agrupado de movimento que afeta estoque

Arquivo: RM.Est.Baixa.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO

* **[Ticket: MCP-1809]** Melhoria na inclusão de movimento parametrizado para utilização de dados fiscais no item

Arquivo: RM.Mov.Movimento.Form.dll

## TOTVS Gestão Patrimonial

### Rotina: CONTABILIZACAO DEPRECIACAO PAT 37 110

* **[Ticket: 422718 / MEDU-2456]** Atualização no processo de cálculo de depreciação pelo produto

Arquivo: RM.Pat.Calculo.Service.dll

# 12.1.15.107

## Outros

### Rotina: PORTAL

* **[Ticket: MFRWBH-1201]** Retirada validação de Browser do Portal RM e FrameHTML

Arquivos: FrameHTML

## TOTVS Educacional

### Rotina: Teste Sistêmico 12.1.15

* **[Ticket: EDUEDU001-1248]** Ajuste na tela de cadastro de professor ao utilizar o recurso de buscar pessoa cadastrada no sistema.

Arquivo: RM.Edu.Professor.Form.dll

## TOTVS Folha de Pagamento

### Rotina: CONTABILIZACAO PARAMETRIZACAO FOP 34 381

* **[Ticket: 387471 / MRH-6523]** Ajuste no processo de geração de encargos

Arquivo: RM.Fop.Dominio.dll

### Rotina: RM REPORTS LAB 01 188

* **[Ticket: 346904 / MRH-4849]** Ajuste para relatório de envelope de pagamento com valores de base de IRRF

Arquivo: RM.Fop.Calc.Formulas.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: TOTVS COLAB FATURAMENTO MOVIMENTO A PARTIR DE XML CLB 008

* **[Ticket: 423337 / MCP-1640]** Melhoria na inclusão de movimento através de XML - TOTVS Colaboração. Definido como default “Marcado” a flag “Abrir Edição do Movimento”

Arquivo: RM.Mov.Integracoes.Form.dll

## TOTVS Gestão Financeira

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 419730 / MEDU-2306]** Otimizado evento contábil para carregar os Defaults Contábeis das Bolsas corretamente.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO EMISSAO RECEBIMENTO DE CHEQUES FIN 197

* **[Ticket: 376601 / MEDU-2084]** No caso de cheques pré-datados, somente será necessário recalcular o valor do cheque, quando a flag “Considerar a Data de vencimento para o Cálculo do Valor do Cheque" estiver marcada e a data do vencimento for diferente da data do cheque.

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: PERIODO

* **[Ticket: MEDU-2356]** http://tdn.totvs.com/x/vlgtE

Arquivo: RM.Fis.RegrasTributarias.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Data de Nascimento Esta Cortando na Tela de Cadastro de Paciente (em .NET)

* **[Ticket: 461527 / MSAU-5210]** Ajuste para mostrar a idade por extenso do paciente.

Arquivo: RM.Sau.Paciente.Form.dll

# 12.1.15.108

## TOTVS Automação de Ponto

### Rotina: PARAMETROS GLOBAIS PTO 35 1215

* **[Ticket: 462279 / MRH-6374]** Foi realizado o ajuste para que o sistema verifique se o dia em que o feriado foi incluído é um dia de jornada de descanso do funcionário evitando assim a emissão de aviso de semana com menos de 24 horas contínuas de descanso indevidamente.

Arquivo: RM.Pto.Aviso.Intf.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** SGBD: SQL SERVER, ORACLEScript: /\*WESLEY MAGNO DE OLIVEIRA COSTA - FS.2015.09\_02 - OC.:TTEESG - 21/09/2015 VERSAO.: 12.1.8 - EQUIPE:MANUT \*/Chamado: MGCADBH-117Descrição: Alteração das cláusulas WHERE dos UPDATES nas tabelas FLAN e FLANBAIXA, para contemplar os resultados das colunas COTACAOINCLUSAO e COTACAOBAIXA sejam eles negativos ou positivos.

Arquivo: Cvn.12.1.8.sql

## TOTVS Educacional

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 422949 / MEDU-2542]** Melhoria no processo de geração de lançamento financeiro em lote para que não seja apresentada nenhuma não conformidade quando o campo “Carteira” do convenio parametrizado for composto por uma string, por exemplo, “CSR”.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: PORTAL ALUNO MATRICULA ONLINE EDU 50 356

* **[Ticket: 494870 / MEDU-2637]** Alteração na consulta de verificação de inadimplência que não estava considerando a tabela SBOLSA no JOIN fazendo com que bolsas não relacionadas ao contrato do aluno fossem retornadas causando o timeout na execução da query.

Arquivo: RM.Edu.Services.Server.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** DIRF 2017: Ajuste na previdência complementar que estava abatendo indevidamente no rendimento tributável.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: DIRF LAB 01 11

* **[Ticket: 471314 / MRH-6552]** DIRF 2017 - Ajuste na previdência complementar de décimo terceiro no Informe de Rendimentos.DIRF 2017 - Ajuste na restituição de décimo terceiro no Informe de Rendimentos e DIRF para Conferência.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: FERIAS CADASTRO FOP 34 538

* **[Ticket: 386843 / MRH-6212]** Ajustado a navegação entre registros de funcionários que estão com férias marcadas

Arquivo: RM.Fop.FuFerias.Form.dll

### Rotina: FOLHA ANALITICA LAB 01 112

* **[Ticket: 435352 / MRH-6461]** Otimizado geração da folha analítica por centro de custo para respeitar os parâmetros "Filtro para centro de custo" e "Código de quebra para centro de custo"

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Relatorios.Data.dll

### Rotina: PARAMETROS GLOBAIS LAB 01 191

* **[Ticket: 476158 / MRH-6680]** Ajuste no cadastro da máscara de chapa para aceitar o caracter de ponto final

Arquivo: RM.Fop.Parametros.Form.dll

## TOTVS Framework

### Rotina: LICENCESERVER FRW 00044

* **[Ticket: MFRWBH-1210]** Melhoria para que o sistema não verifique licença em base de testes quando está executando chamadas soap

Arquivo: RM.Lib.Server.dll

### Rotina: PERFIS FRW 00055

* **[Ticket: 490938 / MFRWBH-1203]** Melhoria no cadastro de usuários para que os perfis sejam listados sem inconsistências independente dos caracteres presentes nos códigos dos perfis.

Arquivo: RM.Glb.Seguranca.Form.dll

### Rotina: PLANILHA NET EXECUCAO BIS 00047

* **[Ticket: 489509 / MFRWBH-1185]** A planilha RM deve incluir uma nova coluna ou células corretamente.

Arquivo: RM.Glb.PlanilhaNet.Core.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: Bloco K - Geração do Registro K280

* **[Ticket: 270950 / MCP-1360]** Implementação do Bloco K280

Arquivos: RM.Est.Estoque.Service.dll, RM.Mov.Parametros.Data.dll, RM.Est.Homologacao.Intf.dll, RM.Est.Homologacao.Data.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Parametros.Intf.dll, RM.Est.Estoque.IService.dll, RM.Mov.Consts.dll, RM.Mov.Parametros.Form.dll, RM.Est.Homologacao.Form.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 97045 / MCP-1760]** Melhoria na inclusão de movimentos

Arquivos: RM.Mov.Movimento.Service.dll, RM.Mov.Movimento.Intf.dll, RM.Mov.Movimento.Form.dll, RM.Mov.Movimento.Data.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO CANCELAR LANCAMENTO FIN 194

* **[Ticket: 97135 / MEDU-1544]** Ao cancelar um lançamento, caso a data de cancelamento não seja informada, será utilizada como data de cancelamento a data de emissão do lançamento.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SESSAO DE CAIXA GERENCIAR CAIXAS INFORMACAO FIN 277

* **[Ticket: MEDU-2556]** Otimização no processo de pesquisa de lançamentos na sessão de caixa. Agora o sistema pesquisa os lançamentos com boleto de status cancelado corretamente e sem duplicidade.

Arquivos: RM.Fin.SessaoCaixa.Intf.dll, RM.Fin.SessaoCaixa.Data.dll

## TOTVS Gestão Fiscal

### Rotina: ESCRITURACAO

* **[Ticket: MEDU-2629]** Ajuste no Processo de Escrituração para que quando na Base do Cliente o campo SEGUNDONUMERO do Movimento tiver mais de 10 caracteres este valor seja truncado em 10 posições para ser atribuido no campo NROSEGURANCA do Lançamento Fiscal

Arquivo: RM.Fis.EscrituracaoFiscal.Service.dll

### Rotina: SPED FISCAL (SPED FISCAL

* **[Ticket: MEDU-2527]** Implementação BlocoK Registro K280

Arquivos: RM.Fis.Lib.dll, RM.Fis.Facade.dll, RM.Fis.Sped.Engine.dll, RM.Fis.Sped.Server.dll

# 12.1.15.109

## TOTVS Automação de Ponto

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 467698 / MRH-6709]** Foi incluído no log de avisos a informação de que o cadastro de seção está inconsistente sendo apresentado ao final da execução da geração do relatório.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Construção e Projetos

### Rotina: Project-484392 Relatório de Erro Versão 12.1.15 - Erro ao associar serviços em atividades Project-484392

* **[Ticket: 498558 / MCP-1808]** Na associação entre Serviçoes e Atividades ocorre erro no drag n drop

Arquivos: RM.Prj.Planilhas.Intf.dll, RM.Prj.Planilhas.Form.dll

## TOTVS Educacional

### Rotina: Classificação dos projetos após aprovação

* **[Ticket: EDUEDU004-62]** Habilitando parametro relacionado projeto de pesquisa (Atribuir a situação "Recomendado" nos projetos de pesquisa quando estes forem aprovados por nota no workflow)

Arquivo: RM.Edu.Parametros.Form.dll

### Rotina: Evoluções na Gestão de Estágio

* **[Ticket: EDUEDU004-1]** Alteração no cadastro de funcionário da soliciação de estágio

Arquivos: Portal Corpore.Net

* **[Ticket: EDUEDU004-1]** Ajustes na montagem da permissão a partir do server

Arquivo: RM.Edu.Server.dll

### Rotina: Fluxo de aprovação de criação de aluno

* **[Ticket: EDUEDU004-11]** Ajuste na página pública para cadastro de aluno egresso

Arquivos: Portal Corpore.Net

## TOTVS Folha de Pagamento

### Rotina: Comprovante de Rendimentos 2017

* **[Ticket: 323103 / MRH-4134]** DIRF 2017 - Ajuste na previdência complementar de décimo terceiro no Informe de Rendimentos.DIRF 2017 - Ajuste na restituição de décimo terceiro no Informe de Rendimentos e DIRF para Conferência.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: DIRF

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: FUNCIONARIOS ENVELOPE LAB 01 137

* **[Ticket: 496206 / MRH-6819]** Manutenção em Primary Key das tabelas PGPS, PFUNCEXCLUIDO, PCONTROLERECALC

Arquivo: RM.Fop.Processos.Data.dll

### Rotina: Visualização de Equipe - Chefe Supervisor

* **[Ticket: 157839 / MRH-4279]** Ajuste no cadastro de chefe/supervisor para exibir a Equipe do Supervisor

Arquivo: RM.Fop.ChefeSupervisor.Form.dll

## TOTVS Framework

### Rotina: INTEGRACAO MATERIAIS CRM 321454

* **[Ticket: 485587 / MFRWBH-1213]** Melhoria na criação de Fluxo de Trabalho

Arquivo: RM.Lib.WinForms.dll

### Rotina: RM X FLUIG GED PARAMETROS DE CONFIGURACAO INT 00013

* **[Ticket: 489886 / MFRWBH-1190]** O processo foi removido pois não pode ser utilizado quando a integração com o identity estiver ativa, onde a manipulação de perfis deve ser realizada somente através do identity.

Arquivos: RM.exe, RM.Glb.Seguranca.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 351886 / MCP-1502]** Agora, ao clicar no "X" da coluna de itens marcados para o faturamento, todos os registros serão marcados ou desmarcados da mesma forma que ocorre com as demais telas.

Arquivo: RM.Mov.Faturamento.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS CURRICULOS EXTERNOS RHU 36 022

* **[Ticket: 473928 / MRH-6528]** Já é possível exibir o perfil corretamente.

Arquivos: FrameHTML

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 391119 / MEDU-2569]** Implementa método DemonstrativoLivroCaixa, por demanda do Liber

Arquivos: RM.Fin.Lan.IService.dll, RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO VINCULAR LANCAMENTOS FIN 214

* **[Ticket: 408047 / MEDU-2633]** Otimizada abertura da tela de vínculo

Arquivo: RM.Fin.Lan.Data.dll

### Rotina: Piloto Cetec

* **[Ticket: 500486 / EDUCTB001-538]** Ajuste na mensagem de acordo na nova Integração Educacional x Backoffice Protheus

Arquivos: RM.Fin.Lan.Form.dll, RM.Fin.Lan.Service.dll

### Rotina: SESSAO DE CAIXA VALOR LIQUIDO FIN 283

* **[Ticket: 471896 / MEDU-2608]** Otimização no processo de somatório total do valor líquido e do valor a pagar na sessão de caixa. Agora o sistema soma o valor líquido e o valor a pagar corretamente dos lançamentos, não deixando repetir quando é apresentado o mesmo lançamento duas vezes na visão.

Arquivo: RM.Fin.SessaoCaixa.Form.dll

## TOTVS Gestão Fiscal

### Rotina: NF E CONSULTAR EVENTO TOTVS COLABORACAO NF 01 0034

* **[Ticket: 312661 / MEDU-1849]** Inclusão da validação para o cStat 155 (Cancelamento Homologado fora do prazo) referente ao processo de consulta evento de cancelamento para Totvs Colaboração 2.0

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 269218 / MEDU-2200]** Alterada validação no envio dos dados do Endereco do destinatário da NF-e.Segundo a legislação Lei 13143/2016, se o endereço de entrega da mercadoria e o endereço do emitente forem do mesmo Estado, esta operação e considerada interna e neste caso as tags do grupo EnderDest devem ser enviadas com o endereço de entrega.Realizamos esta implementação onde:1- Utilizar o parâmetro "Buscar Endereço de Entrega do Movimento" para que neste caso, utilizando os dados de coleta e entrega, o grupo EnderDest será gerado com os dados do endereço cadastro nas informações de Entrega. Importante:Lembrando que, neste caso é necessário preencher os dados de coleta com os mesmos dados da entrega.2- Em uma situação onde o cliente marque "Buscar Endereço de Entrega do Movimento" e NÃO PREENCHA os dados de coleta e entrega, os dados da tag EnderDest serão levadas com o endereço principal do Cli/For (destinatário da Nota). 3- Caso seja utilizado a opção "Endereço Principal do Cli/For" o processo funcionará conforme era antes, onde as tags do grupo EnderDest serão levadas com o endereço principal do Cli/For (destinatário da Nota).

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: ROTINAS LEGAIS FEDERAIS DIRF LI 01 0063

* **[Ticket: 477310 / MEDU-2615]** Foi criado o campo "IRRF Pessoa Física (Fluxus) – Códigos de Receitas Autônomos", onde o usuário poderá informar os Códigos de Receita que serão considerados para geração dos lançamentos de pessoa física oriundos do Fluxus, que possuam o tributo IRRF, em que não houve retenção e que durante o período os rendimentos não superaram R$ 6.000,00. Os códigos deverão estar separados por “;” (ponto e vírgula). Esse campo somente será visível caso a opção “IRRF Pessoa Física – Autônomos que não tiveram rendimentos superiores a R$ 6.000,00” estiver marcada. O sistema trará como valor default para o campo os códigos 0588 e 3208.

Arquivos: RM.Fin.Lan.IService.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.RotinasFiscais.Data.dll

### Rotina: UTILITARIOS LANCAMENTOS FISCAIS LI 01 0070

* **[Ticket: 481466 / MEDU-2646]** Alteração no calculos da tela de resumo dos tributos.

Arquivos: RM.Fis.NaturezaOper.Service.dll, RM.Fis.Tributo.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: DMED

* **[Ticket: MSAU-4937]** Ajuste no arquivo de exportação da DMED para atender o layout do padrão 2017.

Arquivos: RM.Sau.Faturamento.Data.dll, RM.Sau.Faturamento.Form.dll

### Rotina: ELABORACAO DE AIHS SAU 47 1144

* **[Ticket: 494928 / MSAU-5448]** Ajuste para deixar o espaço em branco no começo do CID

Arquivo: RM.Sau.Sus.Server.dll

## TOTVS Incorporação

### Rotina: ALUGUEL EVENTO FINANCEIRO IMB 49 776

* **[Ticket: 117886 / MCP-796]** Alterada a rotina de verificação de habilitação do cancelamento do lançamento financeiro para levantar exceção e manter a sincronicidade entre a parcela de aluguel e o lançamento financeiro.

Arquivos: RM.Lib.dll, RM.Imb.Aluguel.Lancamento.Server.dll

## TOTVS Planejamento e Controle da Produção

### Rotina: CALCULO DO CUSTO DA PRODUCAO PCP 44 258

* **[Ticket: 434189 / MCP-1791]** Permitir que seja retornado o custo do último mês informado caso não encontre do período apontado.

Arquivo: RM.PCP.RecalculoCusto.Service.dll

# 12.1.15.110

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO LANCAMENTO EVENTOS RM LABORE PTO 35 1191

* **[Ticket: 503683 / MRH-7087]** Foi implementada uma restrição no sistema para limitar o valor de faltas diárias.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 473326 / MRH-6893]** Ajuste realizado no recálculo para funcionários que tenham número de horas de Tempo mínimo entre jornadas informado no parametrizador do funcionário.

Arquivo: RM.Pto.Calculo.Service.dll

* **[Ticket: 483583 / MRH-6894]** Realizadas alterações no processo de abono durante jornada, para tratar horários flexíveis.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: PROCESSO DE CALCULO DE HORAS EXTRAS PTO 35 1238

* **[Ticket: 488987 / MRH-6820]** Foi realizado o ajuste para evitar erro no recálculo para funcionários que tenham abonos lançados no período que tem parametrização de "Incluir nas horas trabalhadas".

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: RELATORIOS GERADOR BANCO DE HORAS PTO 35 1212

* **[Ticket: 506539 / MRH-7041]** Correções feitas no sistema para considerar duas ocorrências com códigos diferentes para uma mesma data.

Arquivo: RM.Pto.BancoDeHoras.Data.dll

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 465298 / MEDU-2498]** Ajuste no upload de arquivos no portal, para que quando exceder a quantidade de caracteres do nome do arquivo exiba uma mensagem informativa com este detalhamento.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Cadastros.Server.dll

### Rotina: ATIVIDADES CURRICULARES EDU 50 043

* **[Ticket: 504451 / MEDU-2652]** Ajuste ao salvar a atividade curricular do aluno para que seja salvo o campo observação também caso possua digitado algum valor.

Arquivo: RM.Edu.AtvCurricular.Data.dll

### Rotina: BOLSAS EDU 50 082

* **[Ticket: 459118 / MEDU-2568]** Melhoria na digitação do campo percentual do processo de bolsa retroativa para que seja possível digitar mais de 2 casas decimais.

Arquivos: RM.Edu.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Consts.dll

* **[Ticket: 493042 / MEDU-2625]** Tratamento de ajustes de descontos quando os valores de descontos somados são menores que o valor original do lançamento.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: Classificação dos projetos após aprovação

* **[Ticket: EDUEDU004-62]** Ajustes na funcionalidade de alteração de situação do projeto de pesquisa

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.PesquisaExtensao.Data.dll, RM.Edu.PesquisaExtensao.Form.dll

* **[Ticket: EDUEDU004-62]** Interface da situação do projeto já preenche o filtro de filial com a filial do contexto ao iniciar.

Arquivo: RM.Edu.PesquisaExtensao.Form.dll

### Rotina: Piloto - Portal Aluno 12.1.15

* **[Ticket: EDUEDU002-802]** Ajuste para exibir a legenda cancelado apenas quando o parâmetro "não exibir lançamentos cancelados" estiver desmarcado

Arquivo: RM.Edu.Rest.Server.dll

### Rotina: PORTAL ALUNO ESTAGIO EDU 50 352

* **[Ticket: 455406 / MEDU-2437]** Melhoria no processo de inscrição do aluno a vagas de estágio, refatoração do DataServer para que seja possível vincular uma formula visual ao processo.

Arquivos: RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.MatrizCurricular.Data.dll, App\_Web\_eduvagasinscricaoalunowebform.aspx.1d4ca059.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3763]** Para os graus de parentesco abaixo o sistema não irá gerar log de erro e sim de informação ao validar a data de nascimento na DIRF, a saber: Mãe: 7; Pai: 6; Sogra: 8, S; Companheiro: C, P; Outros: 9.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: DIRF LAB 01 11

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: FERIAS CADASTRO FOP 34 538

* **[Ticket: 411830 / MRH-5910]** Ajuste no cálculo do IRRF Férias para deduzir também o desconto de INSS do terceiro mês das férias.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: FOLHA ANALITICA LAB 01 112

* **[Ticket: 431169 / MRH-6119]** Otimizado geração da folha analítica para verificar a incidência de estorno de IRRF de férias dos eventos

Arquivo: RM.Fop.Infraestrutura.Repositorios.dll

### Rotina: INFORME DE RENDIMENTOS FOP 34 431

* **[Ticket: 488170 / MRH-7017]** DIRF 2017 - Informe de Rendimentos: Ajuste na dedução da Previdência de Décimo Terceiro.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: PCMSO x PPRA 12.1.15

* **[Ticket: RHRHU001-313]** Melhoria na atualização de exames pendentes após transferência de funcionário com troca de chapa no demitido

Arquivos: RM.Fop.Facade.dll, RM.Smt.Clinico.Data.dll, RM.Fop.Funcionario.Form.dll, RM.Fop.Rescisao.Form.dll, RM.Smt.Clinico.Intf.dll, RM.Fop.Calc.Calculos.dll

### Rotina: RAIS

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-6143]** Ajuste em rotina RAIS

Arquivo: RM.Fop.Dominio.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS BALANCETE CTB 38 113

* **[Ticket: 327374 / MEDU-2592]** Com um plano de contas que possui mais de 60.000 contas contábeis, foi necessário mudar a forma como essas contas são selecionadas para terem seus saldos calculados.

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CUPOM FISCAL COM 022

* **[Ticket: 450071 / MCP-1777]** Acerto para buscar default de CST, Aliquota, Naturea e Tributação na inclusão de produto no Item de Cupom Fiscal.

Arquivos: RM.Mov.CupomFiscal.IService.dll, RM.Mov.CupomFiscal.Intf.dll, RM.Mov.CupomFiscal.Service.dll, RM.Mov.CupomFiscal.Data.dll, RM.Mov.CupomFiscal.Form.dll

### Rotina: EDICAO DE MOVIMENTO MOV 002

* **[Ticket: 361515 / MCP-1483]** Melhoria no processo de movimentação

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: IMPORTACAO DE MOVIMENTO MOV 039

* **[Ticket: 115873 / MCP-1624]** Criação do Parâmetro "Emitir Cupom Fiscal" no Conceito de Importação de Movimento para sobrescrever o parâmetro do Tipo de Movimento. Foi criado para que a Automação Comercial funcione corretamente.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO

* **[Ticket: MCP-1754]** Melhoria na inclusão de itens de movimento parametrizado para baixar estoque.

Arquivos: RM.Est.Baixa.Service.dll, RM.Est.Reserva.Service.dll, RM.Est.Terceiros.Service.dll

### Rotina: TOTVS COLAB FATURAMENTO MOVIMENTO A PARTIR DE XML CLB 008

* **[Ticket: 508595 / MCP-1851]** Melhoria na inclusão de movimento Totvs Colaboração através de arquivo XML

Arquivo: RM.Mov.Integracoes.Form.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: ATENDIMENTOS CRM 321443

* **[Ticket: 501392 / MCP-1829]** Ajuste ao setar valores para os parâmetros do tipo de atendimento ao utilizar o serviço de criar atendimentos por sentença sql.

Arquivo: RM.CRM.Servicos.Form.dll

### Rotina: Re: Alteração da regra de agendar a responder um atendimento

* **[Ticket: 303604 / MCP-1579]** Agora, ao acionar o processo "Agendado respondido", não será validado o preenchimento do campo solução.

Arquivo: RM.CRM.Atendimento.Data.dll

## TOTVS Gestão Financeira

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 467468 / MEDU-2657]** Evitar que ocorra erro no processo de retorno de cobrança quando é utilizado base oracle12. Mensagem de erro: <target>.IDBOLETOLAN e <source>.IDBOLETOLAN têm propriedades conflitantes: propriedade DataType incompatível

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: CADASTROS NATUREZA DE OPERACAO LI 01 0015

* **[Ticket: 391727 / MEDU-2411]** Alteração no DataServer NaturezaData.cs para permitir a importação via conceito para atualização de dados da natureza de operação.

Arquivo: RM.Fis.NaturezaOper.Data.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - ECF LI010032

* **[Ticket: 94637 / MEDU-62]** Implementação do arquivo com registros do Bloco Q na ECF.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: 94637 / MEDU-62]** Implementação do arquivo com registros do Bloco Q na ECF.

Arquivos: RM.Fis.Facade.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES PRINCIPAIS APURACAO ICMS LI 01 0037

* **[Ticket: 469159 / MEDU-2612]** Alteração no encerramento do periodo de apuração do ICMS.

Arquivo: RM.Fis.Utils.Intf.dll

### Rotina: ROTINAS LEGAIS FEDERAIS DIRF LI 01 0063

* **[Ticket: 477310 / MEDU-2615]** Foi realizada uma alteração na tela de geração da DIRF para que o campo “IRRF Pessoa Física (Fluxus) – Códigos de Receita Autônomos” aceite 100 caracteres.

Arquivo: RM.Fis.RotinasFiscais.Form.dll

## TOTVS Gestão Hospitalar

### Rotina: MOVIMENTACOES DE ESTOQUE SAU 47 1126

* **[Ticket: 466717 / MSAU-5262]** Realizado o ajuste para permitir checar medicamentos que não baixam estoque e que não foram processados pela movimentação de estoque.

Arquivo: RM.Sau.PepHis.Server.dll

### Rotina: PEP OUTROS REGISTROS SAU 47 1120

* **[Ticket: 286655 / MSAU-4952]** Realizado ajuste no campo de busca da aleta assinatura digital.

Arquivo: RM.Sau.PepHis.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: UTILITARIOS FECHAMENTO DE PERIODO PAT 37 93

* **[Ticket: 398246 / MEDU-2183]** Atualização da leitura dos parâmetros de mes/ano calculo ao reabrir ou liberar competência

Arquivos: RM.Pat.Utils.Intf.dll, RM.Pat.Periodicidade.Intf.dll, RM.Pat.Periodicidade.Data.dll, RM.Pat.Periodicidade.Form.dll, RM.Pat.Utils.Server.dll

## TOTVS Incorporação

### Rotina: DIMOB - LAYOUT IMB49816

* **[Ticket: MCP-1845]** Incidente:Ao gerar a DIMOB, somente estavam sendo considerados os municípios com codificação da receita federal. O parâmetro desta codificação estava fixo no código. Solução: O processo foi modificado para considerar a codificação de município informada na parametrização na tela do processo

Arquivo: RM.Imb.DIMOB.Server.dll

### Rotina: REAJUSTE DE CM

* **[Ticket: MCP-1848]** Ajuste para a variação do período ser considerada corretamente para o cálculo final no cenário de Ignorar Deflação por Periodicidade

Arquivo: RM.Imb.Reajuste.Lib.dll

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhoria para o projeto de revitalização.

Arquivo: RM.Imb.Venda.Upg.Data.dll

# 12.1.15.111

## TOTVS Construção e Projetos

### Rotina: CURVA S PRJ 33 818

* **[Ticket: 513860 / MCP-1846]** Calcular Histograma durante a Solicitação de Material em base Oracle

Arquivo: RM.Prj.Calculo.Server.dll

* **[Ticket: 513860 / MCP-1846]** Calcular Histograma durante a Solicitação de Material em base Oracle

Arquivo: RM.Prj.Calculo.Server.dll

### Rotina: RELATORIOS PERIODICOS PRJ 33 884

* **[Ticket: 514143 / MCP-1847]** Gerar Relatório de Histograma selecionando o Calculo da Curva S

Arquivo: RM.Prj.Calculo.Form.dll

## TOTVS Educacional

### Rotina: CONTABILIZACAO

* **[Ticket: MEDU-2471]** Ajuste na localização dos componentes para atualização do designer da tela.

Arquivo: RM.Edu.Contabil.Form.dll

### Rotina: Piloto - Portal Aluno 12.1.15

* **[Ticket: EDUEDU002-802]** Melhoria no Novo Portal do Aluno, para que apresente o campo observação das informações das Atividades Curriculares cadastrados no sistema.

Arquivos: RM.Edu.AtvCurricular.Data.dll, RM.Edu.Rest.Server.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF LAB 01 11

* **[Ticket: 514895 / MRH-7202]** DIRF 2017: Ajustado opção Subtrair na geração da DIRF/Informe de Rendimentos.

Arquivo: RM.Fop.Relatorios.Intf.dll

### Rotina: FOLHA PAGAMENTO

* **[Ticket: MRH-6936]** Ajuste no cadastro de Seção para aceitar CPF no caso de Pessoa Física

Arquivos: RM.Fop.Secao.Form.dll, RM.Fop.Secao.Services.dll

## TOTVS Framework

### Rotina: ACTIONS ANEXAS FRW 00001

* **[Ticket: 481187 / MFRWBH-1222]** Melhoria na integração RM x Fluig no Fluxo de Trabalho para enviar os dados chaves do cadastro

Arquivo: RM.Lib.Server.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 329244 / MEDU-1882]** Com objetivo de atender aos clientes que querem entregar o SPED Contábil e não precisam entregar o bloco K por se tratar de um registro facultativo para o ano base 2016, iremos liberar uma versão do SPED Contábil 5.0 sem contemplar algumas evoluções:- Bloco K: Conglomerados Econômicos (Facultativo para o ano-calendário 2016)Em função do nível de complexidade dos recursos acima os mesmos serão disponibilizados em versões posteriores.

Arquivos: RM.Ctb.Sped.Intf.dll, RM.Ctb.Sped.Form.dll, RM.Ctb.Sped.Service.dll, RM.Ctb.Sped.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: Bloco K - Geração do Registro K280

* **[Ticket: 270950 / MCP-1360]** Implementação Bloco K280

Arquivos: RM.Est.Estoque.Service.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Parametros.Data.dll

### Rotina: CUPOM FISCAL COM 022

* **[Ticket: 114574 / MCP-1625]** Caso não esteja preenchido o Número do Movimento na Inclusão de Cupom, é utilizado o Número do Cupom.

Arquivo: RM.Mov.CupomFiscal.Service.dll

### Rotina: TOTVS COLAB FATURAMENTO MOVIMENTO A PARTIR DE XML CLB 008

* **[Ticket: 459771 / MCP-1821]** Melhoria na inclusão de movimento Totvs Colaboração através de arquivo XML

Arquivo: RM.Mov.Movimento.Form.dll

## TOTVS Gestão Fiscal

### Rotina: ESCRITURACAO LI 01 0025

* **[Ticket: 505081 / MEDU-2694]** O serviço de tributação do movimento foi ajustado para que seja verificado se o Item do Movimento possui IPI de acordo com a parametrização da Natureza.

Arquivos: RM.Fis.Utils.Intf.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.NaturezaOper.Service.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.EscrituracaoFiscal.Service.dll

### Rotina: REPLICA - ECF - Registro Q100: Demonstrativo do Livro Caixa

* **[Ticket: MEDU-2433]** Implementa novos campos DATASALDOANTERIORCAIXA e SALDOANTERIORCAIXA no cadastro de Dados Fiscais da Filial.

Arquivos: RM.Fis.Filial.Intf.dll, RM.Fis.Filial.Data.dll, RM.Fis.Filial.Form.dll

## TOTVS Incorporação

### Rotina: DISTRATO BILATERAL IMB 49 817

* **[Ticket: 514803 / MCP-1854]** Melhoria na efetivação do distrato para desbloquear a parcela antes de reajustar a venda

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: Verificar status do distrato

* **[Ticket: 255583 / MCP-1165]** Melhoria no processamento de baixa de parcelas em lote para parcelas a pagar, oriundas de distrato, o sistema
  passa a verificar todas as vendas distratadas que estão com parcelas sendo baixadas e se for a ultima parcela
  quitar o distrato da mesma.

Arquivo: RM.Imb.Venda.Financeiro.Server.dll

# 12.1.15.112

## TOTVS Automação de Ponto

### Rotina: PARAMETROS RM PORTAL PTO 35 1218

* **[Ticket: 284553 / MRH-4355]** O erro estava ocorrendo, pois os subordinados de um usuário, que não é funcionário, estavam sendo carregados. Para corrigir o problema, foi feita uma condição para que os usuários que não sejam funcionários, possam editar os filtros do RM Portal.

Arquivos: RM.Pto.Abono.Data.dll, RM.Pto.Batida.Data.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 493021 / MRH-6812]** Foi realizado o ajuste para que sejam impressos todos os abonos lançados para uma mesma jornada caso um dos parâmetros "Código do abono" ou "Descrição do abono" estejam marcados.

Arquivo: RM.Pto.Relatorio.Data.dll

### Rotina: TOTVS AUTOMACAO DE PONTO DO USUARIO PTO 35 1219

* **[Ticket: 484501 / MRH-7170]** Foram feitas alterações no sistema em relação a validação da data de referência da ocorrência.

Arquivo: RM.Pto.AprovaHorasExtras.Data.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** SGBD: SQL Server | ORACLEScript: /\*EDER LOPES TEIXEIRA - SD.2016.11\_01 - OC.:MEDU-684 - 04/01/2017 VERSAO.: 12.1.15 - EQUIPE:MANUT\*/Chamado: 07\EXCEÇÃODescrição: Conforme solicitado pelo analista Wesley Magno de Oliveira Costa, recriamos a tabela FRELLANPAI\_BKPTIN removida pelo Script da versão 12.1.15 SD.2016.11\_01 e validar as bases que não tiverem rodado o Script para realizar a criação de uma PK.SGBD: SQL Server | ORACLEScript: /\*LEONARDO MONTEIRO DOS SANTOS - CN.2016.12\_03 - OC.:MEDU-1489 - 05/01/2017 VERSAO.: 12.1.15 - EQUIPE:MANUT \*/Chamado: 07\EXCEÇÃODescrição: Remoção da UNIQUE CONSTRAINT UNCODINEPCURSO da tabela SCURSOMEC, devido a regra de negócio do produto.

Arquivo: Cvn.12.1.15.sql

## TOTVS Construção e Projetos

### Rotina: APROPRIACAO DE SERVICOS INSUMOS PRJ 33 803

* **[Ticket: 530927 / MCP-1886]** Verificado o comportamento de Edição das quantidades solicitadas via Histograma Agrupado.

Arquivos: RM.Prj.PedidoMaterial.Form.dll, RM.Prj.PedidoMaterial.Server.dll

### Rotina: PERFIS SEGURANCA CAMPOS FRW 00056

* **[Ticket: 488685 / MCP-1838]** Campos livres de projetos sendo exibidos para usuários não possuem permissão

Arquivo: RM.Prj.Projeto.Form.dll

### Rotina: PLANILHAS IMPORTAR CRONOGRAMA VIA EXCEL PRJ 33 869

* **[Ticket: 510552 / MCP-1840]** Ao fazer a importação de cronograma via planilha excel o sistema apaga os períodos anteriores.

Arquivo: RM.Prj.Cronograma.Data.dll

## TOTVS Educacional

### Rotina: Classificação dos projetos de pesquisa após aprovação

* **[Ticket: EDUEDU004-62]** Ajustes na interface de situação de projeto de pesquisa - edital deve ser filtrado pela filial selecionada

Arquivo: RM.Edu.PesquisaExtensao.Form.dll

* **[Ticket: EDUEDU004-62]** Ajuste da consulta que traz o projetos vinculados ao edital para que o item planejamento não seja obrigatório

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

### Rotina: Definição de bolsistas sem apontar a pessoa do bolsista para os projetos de Pesquisa e Extensão

* **[Ticket: EDUEDU004-59]** Ajustes no fluxo de cadastro de bolsista para tratar corretamente a utilização do bolsista responsável, vinculado ao plano de trabalho cadastrado na submissão de proposta.

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

### Rotina: Erro ao gerar contabilização

* **[Ticket: 443052 / MEDU-2620]** Foi realizada otimização do processo de contabilização por competência, de forma que seja possível definir, através do cadastro de bolsas, quais bolsas que devem ser consideradas pelo processo de contabilização por competência.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Contabil.Server.dll, RM.Edu.Financeiro.Data.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Financeiro.Intf.dll, RM.Edu.Financeiro.Server.dll

### Rotina: Piloto Cetec

* **[Ticket: 525145 / EDUCTB001-538]** Ajustes na chamada da funcionalidade de apontamento de falta quando o menu é criado a partir da camada cliente.

Arquivo: RM.Edu.dll

### Rotina: PORTAL - ALUNO - MATRÍCULA ONLINE EDU50356

* **[Ticket: MEDU-2483]** O parâmetro 'Usar valor do credito financeiro da matriz do aluno' passou a ser verificado na obtenção de valores de créditos para disciplinas matriculadas de turmas livres que não estão na grade do aluno.

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Edu.Matricula.Data.dll

## TOTVS Folha de Pagamento

### Rotina: CAMPOS COMPLEMENTARES FUNCIONARIOS LAB 01 19

* **[Ticket: 409567 / MRH-6023]** Retorno do tipo "V" (Aviso Prévio) para o lookup de situação.

Arquivo: RM.Fop.Funcionario.Form.dll

### Rotina: DIRF LAB 01 11

* **[Ticket: 511843 / MRH-7315]** Ajustado preenchimento do campo 'Alocação do residente ou domiciliado no exterior' no cadastro do funcionário e ficha financeira.

Arquivo: RM.Fop.Funcionario.Form.dll

* **[Ticket: 529275 / MRH-7352]** DIRF 2017: Ajuste unificação de dados da pensão alimentícia quando há movimentação referente a PLR.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 524112 / MRH-7263]** O nome do dependente passa a ser informado de forma alinhada no informe de rendimento PDF nas "Despesas Médico-Odonto-Hospitalares" para o "Valor pago no ano referente aos dependentes".

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: FERIAS CALCULO FOP 34 402

* **[Ticket: 412028 / MRH-6298]** Ajuste para considerar também o periodo de afastamento tipo W para prorrogar o periodo concessivo das férias, para pagamento em dobro.

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.FuFerias.Data.dll

### Rotina: FOLHA

* **[Ticket: MRH-7258]** Ajuste geração de encargos referente ao FGTS de 13º salário.

Arquivo: RM.Fop.Dominio.dll

### Rotina: FUNCIONARIOS CADASTRO LAB 01 128

* **[Ticket: 257419 / MRH-3401]** Ajuste de filtro de coligada no histórico de compra de vale transporte

Arquivos: RM.Fop.Funcionario.Data.dll, RM.Fop.Funcionario.Form.dll

### Rotina: INFORME DE RENDIMENTOS FOP 34 431

* **[Ticket: 534377 / MRH-7429]** Realizando ajuste no campo de informações complementares para não somar a base de 13º salário.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RESCISÃO - CADASTRO DE RESCISÃO FOP34400

* **[Ticket: 95673 / MRH-413]** O valor da dedução para o 13º salário de dependente está sendo multiplicado pelo número de dependentes que incide IRRF quando informado nas demais chapas estando o parâmetro "Calcular IRRF/INSS de múltiplos vínculos sem chapa centralizadora" desmarcado.

Arquivo: RM.Fop.Relatorios.Data.dll

## TOTVS Framework

### Rotina: FORMULA VISUAL (FVS 01)

* **[Ticket: MFRWBH-1238]** Otimização de memória em fórmula visual e envio de email assincronamente em fórmulas visuais

Arquivo: RM.Lib.Workflow.Activities.dll

### Rotina: OUTROS

* **[Ticket: MFRWBH-1240]** Shelve do Gustavo Shelve do Gustavo

Arquivo: RM.Lib.WinForms.dll

### Rotina: SQL

* **[Ticket: MFRWBH-1226]** Melhorias em queries internas visando otimizar o desempenho do sistema

Arquivos: RM.Lib.Server.dll, RM.Lib.Jobs.Server.dll

## TOTVS Framework Web

### Rotina: PORTAL WEB GESTAO DE FERIAS LAB 01 208

* **[Ticket: 395555 / MFRWBH-1237]** Melhoria na exibição dos menus do RH para que todos os submenus sejam exibidos sem que haja necessidade entrar novamente no portal do RH.

Arquivo: RM.Lib.WebForms.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: QUADRO COMPARATIVO COTACAO COM 009

* **[Ticket: 499111 / MCP-1832]** Considerar o valor minimo da coluna de produtos para que a mesma não fique oculta devido ao nr de fornecedores.

Arquivo: RM.Cmp.Cotacao.Form.dll

* **[Ticket: 469809 / MCP-1850]** Melhoria no processo de cotacao

Arquivo: RM.Cmp.Cotacao.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS CURRICULOS EXTERNOS RHU 36 022

* **[Ticket: 412731 / MRH-5665]** Devido a atualização do Novo Banco de Talentos a propriedade 'DESENTIDADE' não existe mais. Assim o sistema só considera 'NOMEENTIDADE'.

Arquivo: RM.Rhu.Pessoa.Data.dll

### Rotina: REQUISICOES ALTERACOES DE DADOS FUNCIONAIS RHU 36 505

* **[Ticket: 298758 / MRH-5339]** Realizada melhoria de forma a possibilitar a progressão salarial em requisição de Transferência com Alteração de Dados Funcionais entre filiais.

Arquivos: RM.Rhu.Requisicao.Intf.dll, RM.Rhu.Requisicao.Form.dll, RM.Rhu.Requisicao.Server.dll, RM.Rhu.Funcionario.Data.dll, App\_Web\_rhureqtransfpromocao.ascx.5b96ec5.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO BAIXA IMPORTACAO FIN 191

* **[Ticket: 453010 / MEDU-2709]** Otimização no processo de importação de baixa. Agora o sistema realiza a baixa corretamente da forma que foi parametrizado pelo cliente, considerando os valores zerados no arquivo dos valores de Multa / Juros / Desconto / Valores Opcionais.

Arquivos: RM.Fin.Lan.Intf.dll, RM.Fin.Lan.Form.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lan.Data.dll

### Rotina: PADRAO

* **[Ticket: MEDU-2727]** Otimização no processo de revitalização do TIN/Financeiro

Arquivo: RM.Fin.Conversor.Service.dll

* **[Ticket: MEDU-2727]** Ajuste no Código da Coligada para ser fixo 0.

Arquivo: RM.Fin.Conversor.Service.dll

## TOTVS Gestão Fiscal

### Rotina: ESCRITURACAO

* **[Ticket: MEDU-2382]** Implementada melhoria na escrituração para conseguir calcular corretamente o Valor do ICMS Interestadual mesmo com redução de base de cálculo do ICMSem lançamentos fiscais de entrada com diferencial de alíquota (Este chamado trata-se de implementar a correção da Issue MEDU-2158 na escrituração).

Arquivo: RM.Fis.EscrituracaoFiscal.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 412569 / MEDU-2733]** Alteração na geração dos dados de construção.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: ATESTADO MEDICO PEP0008

* **[Ticket: 478636 / MSAU-5359]** Realizado ajuste para importar as informações de observação de exames do PEP 2.0

Arquivo: RM.Sau.PepHis.Server.dll

### Rotina: Erro ao solicitar autorização de guia

* **[Ticket: 466319 / MSAU-5231]** Ao acessar o sistema TOTVS Gestão Hospitalar, ir ao menu Atendimento/"Pronto Atendimento/Ambulatório"/Registro de Atendimento Externo, selecionar um paciente, ir a aba "Guia de Autorização", registrar uma "Guia de Solicitação de SP/SADT" e clicar no botão "Solicitar autorização TISS", exibia a mensagem "Campo Guia precisa ter um valor".

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: Geração de XML Raiox

* **[Ticket: 482465 / MSAU-5383]** Ajuste realizado para que o sistema faça a integração corretamente gerando os arquivos de xml.

Arquivo: RM.Sau.Integracoes.Server.dll

### Rotina: PEP DILUICOES SAU 47 1111

* **[Ticket: 382365 / MSAU-5203]** Realizado ajuste para que o sistema apresente a diluição em todas as unidade de atendimento quando não existir nenhuma unidade configurada no padrão de diluição.

Arquivo: RM.Sau.PepHis.Implementation.dll

### Rotina: PEP PRESCRICAO MEDICA SAU 47 1121

* **[Ticket: 439547 / MSAU-5090]** Realizado ajuste para carregar corretamente o cadastro de frequência na integração com o PEP 2.0

Arquivos: TOTVS.PEP.Integration.dll, RM.Sau.PepHis.Implementation.dll, RM.Sau.PepHis.Server.dll

* **[Ticket: 498140 / MSAU-5451]** Realizado ajuste para excluir o registro de cirurgia do PEP 2.0.

Arquivo: RM.Sau.PepHis.Server.dll

### Rotina: RM Saude - Erros na movimentação de leitos

* **[Ticket: 404109 / MSAU-5319]** Ajuste realizado para que o sistema faça a o registro do recém-nascido sem liberar o leito em que a mãe está internada.

Arquivo: RM.Sau.RegistroAtendimento.Data.dll

### Rotina: Sistema apresenta mensagem de erro ao prescrever Soros e Componentes (item específico)

* **[Ticket: 297094 / MSAU-4027]** Realizado tratamento na mensagem apresentada ao liberar uma prescrição de soros e componentes

Arquivo: RM.Sau.PepHis.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: UTILITARIOS FECHAMENTO DE PERIODO PAT 37 93

* **[Ticket: 398246 / MEDU-2183]** Atualização da leitura dos parâmetros do sistema

Arquivos: RM.Pat.Parametros.Data.dll, RM.Pat.Patrimonio.Form.dll, RM.Pat.Periodicidade.Data.dll

## TOTVS Incorporação

### Rotina: DIMOB GERACAO DE ARQUIVO POR EMPREENDIMENTO IMB 49 815

* **[Ticket: 512242 / MCP-1866]** Alterada a rotina da DIMOB para aluguel antigo para que seja enviado o código da cidade do empreendimento.

Arquivo: RM.Imb.DIMOB.Server.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: FUNCIONARIOS CONTROLE DE ATESTADOS RHU 36 571

* **[Ticket: 435117 / MRH-6087]** Realizado ajuste para que seja possível lançar atestado para funcionários de férias, desde que o período do atestado não faça interseção com o período de férias.

Arquivo: RM.Smt.Pessoa.Form.dll

# 12.1.15.114

## TOTVS Automação de Ponto

### Rotina: ALTERACOES GLOBAIS CARTAO DE PONTO PTO 35 1288

* **[Ticket: 389139 / MRH-5427]** Alterações no sistema, para verificação do contexto de acesso do usuário que está tentando inserir a batida para funcionários de coligadas diferentes.

Arquivo: RM.Pto.Batida.Data.dll

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 95549 / MRH-6329]** Otimização de performance no processo de importação de batidas.

Arquivos: RM.Pto.Funcionario.Data.dll, RM.Pto.Batida.Data.dll, RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 486715 / MRH-7154]** Otimizado o cálculo do horário por jornada de forma que o erro de chave duplicada não ocorra mais quando existir descansos cadastrados.

Arquivo: RM.Pto.Horario.Data.dll

### Rotina: PROCESSO DE CALCULO DE HORAS EXTRAS PTO 35 1238

* **[Ticket: 488987 / MRH-7596]** Foi realizado o ajuste para evitar erro no recálculo para funcionários que tenham abonos lançados no período que tem parametrização de "Incluir nas horas trabalhadas".

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: RECALCULO

* **[Ticket: MRH-7720]** Criado um parâmetro para considerar ou não Extra de Nona Hora na distribuição de horas extras.

Arquivos: RM.Pto.Parametros.Intf.dll, RM.Pto.Contexto.Server.dll, RM.Pto.Parametros.Data.dll, RM.Pto.Parametros.Form.dll, RM.Pto.Calculo.Service.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** Acerto na validação da marcação /\*IGOR MARANI ALVES - FS.2017.02\_04 - OC.:07\EXCEÇÃO - 20/02/2017 VERSAO.: 12.1.16 - EQUIPE:MANUT \*/

Arquivo: Cvn.12.1.15.sql

## TOTVS Business Connect

### Rotina: INTEGRACAO TIN X BACKOFFICE PROTHEUS CADASTROS IMB 49 833

* **[Ticket: 472913 / MCP-1762]** Melhoria na geração do código reduzido para contas SINTÉTICAS, os sistema passa a concatenar 'S' para o inicio
  dos códigos reduzidos gerados para as contas do tipo SINTETICA
  originadas do cadastro do Protheus

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

### Rotina: Integração TFS Tools Consignado x RM Labore - Script configuração integração – ORACLE

* **[Ticket: 366725 / MRH-5003]** Ajuste na consulta oracle para integração Folha x Averbações

Arquivo: RM.Con.ConfiguraIntegracao.TotvsFolhaTools.dll

### Rotina: MENSAGEM UNICA CADASTRO PROJETO OBRA E TAREFA PRJ 33 918

* **[Ticket: 544072 / MCP-1912]** Este ajuste aplica-se somente para integrações do TOP com o PROTHEUS por procedure. Alterado o procedimento de alteração da tabela de tarefas para reconhecer a alteração no nome da tarefa. É necessário executar o configurador para atualizar a base de dados.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsObrasProjetosProtheus.dll

### Rotina: STORED PROCEDURE PROCESSO CONTRATOS PEDIDO DE COMPRA A

* **[Ticket: MCP-1743]** Adicionado processo na visão de pedidos para realizar a verificação da existência de eliminação de resíduos quando integrado via procedure com o PROTHEUS. A pesquisa é realizada via comando SQL direto na base do PROTHEUS. Para que seja possível foi criado nos parâmetros da integração por procedure a possíbilidade de informar o linked server da base do prohteus e as tabelas de pedidos e solicitações.

Arquivos: RM.Con.Obras.Data.dll, RM.Prj.Facade.dll

### Rotina: WEBSERVICE EDU 50 493

* **[Ticket: 543300 / MEDU-2780]** Ajuste no serviço de emissão de boleto disponibilizado via webservice para que passe a considerar a tabela FBOLETO.

Arquivo: RM.Con.EducacionalWebEnsino.Data.dll

## TOTVS Construção e Projetos

### Rotina: COPIA DE ITENS PRJ 33 779

* **[Ticket: 508911 / MCP-1864]** Retirar a mensagem solicitando a informação do cenário para projetos que não utilizam cenário durante a cópia de itens.

Arquivo: RM.Prj.Projeto.Form.dll

### Rotina: CURVA ABC PRJ 33 817

* **[Ticket: 155386 / MCP-1804]** Ajuste realizado em exportação da Curva ABC de insumos para que respeite as configurações de colunas definidas pelo usuário

Arquivo: RM.Prj.Calculo.Form.dll

### Rotina: PLANILHAS EXPORTAR ALOCACAO PARA O QUADRO DE PERMANENCIA PRJ 33 980

* **[Ticket: 520931 / MCP-1874]** Ajuste realizado ao exportar a alocação para o quadro de permanência

Arquivos: RM.Prj.Planilhas.Data.dll, RM.Prj.AlocacaoRecurso.Data.dll

### Rotina: RELATORIOS PERIODICOS PRJ 33 884

* **[Ticket: 534673 / MCP-1902]** Permitir que as quantidades planejadas, medidas e realizadas sejam impressas no relatório quando a opção for selecionada nos parâmetros do relatório.

Arquivo: RM.Prj.Relatorios.Periodico.Form.dll

### Rotina: STORED PROCEDURE PROCESSO CONTRATOS PEDIDO DE COMPRA A

* **[Ticket: MCP-1743]** Adicionado processo na visão de pedidos para realizar a verificação da existência de eliminação de resíduos quando integrado via procedure com o PROTHEUS. A pesquisa é realizada via comando SQL direto na base do PROTHEUS. Para que seja possível foi criado nos parâmetros da integração por procedure a possíbilidade de informar o linked server da base do prohteus e as tabelas de pedidos e solicitações.

Arquivos: RM.Prj.Integracao.Server.dll, RM.Prj.PedidoMaterial.Data.dll, RM.Prj.PedidoMaterial.Intf.dll, RM.Con.Conector.Server.dll, RM.Con.Conector.Service.dll, RM.Con.Facade.Delphi.dll, RM.Con.Obras.Data.dll, RM.Con.Parametrizador.Form.dll, RM.Prj.Integracao.Intf.dll, RM.Prj.PedidoMaterial.Form.dll, RM.Con.ConfiguraIntegracao.Form.dll, RM.Prj.Facade.dll, RM.Prj.Utils.Server.dll, RM.Prj.Contrato.Data.dll, RM.Prj.Contrato.Server.dll, RM.Prj.PedidoMaterial.Server.dll, RM.Con.Conector.Interface.dll, RM.Con.ConfiguraIntegracao.TotvsObrasProjetosProtheus.dll, RM.Con.Parametrizador.Intf.dll, RM.Prj.Facade.Intf.dll

* **[Ticket: MCP-1743]** Adicionado processo na visão de pedidos para realizar a verificação da existência de eliminação de resíduos quando integrado via procedure com o PROTHEUS. A pesquisa é realizada via comando SQL direto na base do PROTHEUS. Para que seja possível foi criado nos parâmetros da integração por procedure a possíbilidade de informar o linked server da base do prohteus e as tabelas de pedidos e solicitações.

Arquivo: RM.Prj.Integracao.Server.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: Alinhamento do procedimento de origem com o procedimento NHSN

* **[Ticket: 438823 / MSAU-5115]** Cliente solicitou que quando os procedimentos NHSN fossem alterados nos procedimentos de origem os mesmos valores deveriam ser alterados também na cirurgia. Alterar o sistema para quando for realizado a alteração do procedimento nhsn do procedimento de origem o mesmo seja alterado nas cirurgias também

Arquivos: RM.SauIH.Paciente.Intf.dll, RM.SauIH.Cadastros.Data.dll, RM.SauIH.Cadastros.Form.dll, RM.SauIH.Paciente.Data.dll, RM.SauIH.Paciente.Form.dll, RM.SauIH.Cadastros.Intf.dll

## TOTVS Educacional

### Rotina: CENSO

* **[Ticket: MEDU-2285]** Foi retirado o anexo "Instituição do MEC" da tela de Parâmetros Gerais (Coligada) do Educacional

Arquivo: RM.Edu.Cadastros.Form.dll

### Rotina: Classificação dos projetos de pesquisa após aprovação

* **[Ticket: EDUEDU004-62]** Ajuste de mensagem na aprovação do projeto de pesquisa

Arquivo: RM.Edu.PesquisaExtensao.Form.dll

### Rotina: Fluxo de aprovação de criação de aluno

* **[Ticket: EDUEDU004-11]** Ajuste na emissão de mensagem de campos obrigatórios

Arquivos: Portal Corpore.Net

* **[Ticket: EDUEDU004-11]** Ajuste na ordenação dos campos exibidos na página pública de cadastro de egresso

Arquivos: Portal Corpore.Net

### Rotina: GERACAO DE MOVIMENTO POR COMPETENCIA EDU 50 230

* **[Ticket: 520667 / MEDU-2785]** Permitir exclusão de lançamentos com vínculo com movimento (TMOVLAN)

Arquivo: RM.Edu.Services.Server.dll

### Rotina: MUDAR TURMA EDU 50 314

* **[Ticket: 508775 / MEDU-2770]** Otimização no processo de mudança de turma.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: Piloto Cetec

* **[Ticket: 512871 / EDUCTB001-538]** Ajuste nos dados de partida em lançamentos contábeis quando integração Educacional x Protheus SigaCTB ativa.

Arquivo: RM.Edu.Contabil.Server.dll

### Rotina: PORTAL PROFESSOR AVALIACOES EDU 50 371

* **[Ticket: 492057 / MEDU-2607]** Ajuste na execução da avaliação descritiva no portal, para que quando a data limite da etapa expirar não seja possível executar a avaliação descritiva, somente será visualizada as avaliações concluídas, porém em modo de somente leitura.

Arquivos: Portal Corpore.Net

### Rotina: valor do boleto é exibido incorretamente, ou seja, não está sendo deduzido do valor a pagar o valor já baixado anteriorm

* **[Ticket: 534703 / MEDU-2756]** Feito um tratamento na consulta de seleção de lançamentos (para clientes que utilizam o conceito de boletos parciais) a fim de filtrar somente os lançamentos em aberto e baixados parcialmente no cálculo do valor líquido do boleto.

Arquivo: RM.Edu.Facade.dll

## TOTVS Folha de Pagamento

### Rotina: Comprovante de Rendimentos 2017

* **[Ticket: 323103 / MRH-4134]** DIRF 2017: Otimizado ajuste na DIRF referente aos dados do plano de saúde.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 323103 / MRH-4134]** DIRF 2017: Ajuste na unificação dos dados de pensão referente a PLR.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: DIRF LAB 01 11

* **[Ticket: 521406 / MRH-7232]** Otimizado geração da DIRF para funcionários que utilizam múltiplos vínculos com chapa centralizadora

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 523112 / MRH-7531]** DIRF 2017: Alterado para permitir evento do tipo provento marcar a opção Subtrair.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: FERIAS PWSA100A

* **[Ticket: MRH-2974]** Ajuste na validação de parcelas de empréstimo na marcação de férias

Arquivo: RM.Fop.FuFerias.Data.dll

* **[Ticket: MRH-2973]** Ajustes na tela de cadastro de férias do funcionário

Arquivo: RM.Fop.FuFerias.Form.dll

### Rotina: Project-521584 Informe do Portal x Informe do Sistema Project-521584

* **[Ticket: 531938 / MRH-7403]** Ajuste no Informe de Rendimentos Web para caber em uma página

Arquivos: RM.Fop.Informe.Data.dll, RM.Fop.Utils.Server.dll

### Rotina: Project-551992 Ajuda de Custo no Informe Project-551992

* **[Ticket: 552678 / MRH-7751]** Otimizado geração da DIRF no campo ajuda de custo

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RAIS

* **[Ticket: MRH-6143]** Ajuste no processo da geração da RAIS - REPLICA

Arquivo: RM.Fop.Dominio.dll

## TOTVS Framework

### Rotina: CONFIGURACOES FRW 00016

* **[Ticket: 369156 / MFRWBH-1232]** Melhoria na abertura da agenda, recuperando os compromissos independentemente da recorrência utilizada por eles.

Arquivo: RM.Lib.Utils.dll

### Rotina: INSTALACAO FRW 00042

* **[Ticket: 466019 / MFRWBH-1207]** Melhoria no Totvs Update para que envie o arquivo RM.exe.config

Arquivo: RM.Lib.dll

### Rotina: RM X FLUIG GED: PARÂMETROS DE CONFIGURAÇÃO INT00013

* **[Ticket: MFRWBH-1246]** A integração do RM com o Identity Foi Otimizada.

Arquivos: RM.Glb.IntegracaoFluig.Form.dll, RM.Lib.Communication.Server.dll, RM.Glb.IntegracaoFluig.Server.dll

### Rotina: SERVIDORES DE APLICAÇÃO FRW00066

* **[Ticket: MFRWBH-1249]** Ajuste no Critical Log

Arquivos: RM.Lib.dll, RM.Lib.Server.dll, RM.Lib.Server.Custom.dll

## TOTVS Gestão Bibliotecária

### Rotina: DEVOLUCAO BIB 10 1029

* **[Ticket: 527869 / MEDU-2745]** Ajuste na exibição boletos com registros de empréstimos agrupados.

Arquivos: Portal Corpore.Net

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS CADASTROS CTB 39 011

* **[Ticket: 418530 / MEDU-2275]** Com objetivo de atender aos clientes que querem entregar o SPED Contábil e não precisam entregar o bloco K por se tratar de um registro facultativo para o ano base 2016, iremos liberar uma versão do SPED Contábil 5.0 sem contemplar algumas evoluções:- Bloco K: Conglomerados Econômicos (Facultativo para o ano-calendário 2016)Em função do nível de complexidade dos recursos acima os mesmos serão disponibilizados em versões posteriores.

Arquivo: RM.Ctb.Sped.Intf.dll

### Rotina: Piloto Cetec

* **[Ticket: 512871 / EDUCTB001-538]** Ajuste nos dados de partida em lançamentos contábeis quando integração Educacional x Protheus SigaCTB ativa.

Arquivos: RM.Ctb.Lan.IService.dll, RM.Imb.Aluguel.ContratoLoc.Server.dll, RM.Imb.Contabilidade.Server.dll, RM.Ctb.Lib.dll, RM.Ctb.Lan.Form.dll, RM.Ctb.Lan.Service.dll, RM.Fin.AplicacaoFinanceira.Server.dll, RM.Fin.Lan.Service.dll, RM.Ctb.Lib.Server.dll, RM.Ctb.Lib.WinForms.dll, RM.Fin.Lan.Form.dll, RM.Fin.Utils.Server.dll, RM.Imb.Aluguel.Contabilidade.IService.dll, RM.Imb.Facade.dll, RM.Mov.Movimento.Service.dll, RM.Ctb.Lan.Data.dll

### Rotina: RELATORIOS BALANCETE CTB 38 113

* **[Ticket: 476839 / MEDU-2642]** Ajuste na geração dos relatório para que caso seja selecionado a opção "Imprimir níveis superiores em negrito" e o arquivo de saída seja "TXT ?" o relatório ignore a opção de negrito para que o arquivo seja exibido corretamente.

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: BLOCO K FIS 006

* **[Ticket: 519828 / MCP-1860]** Inclusão de produtos com a Situação de Mercadoria "Produto Intermediario" como produtos para envio no K200

Arquivo: RM.Est.Estoque.Service.dll

### Rotina: CONTROLE ORCAMENTARIO

* **[Ticket: MCP-1023]** Ajuste ao gerar contrato que utiliza medição nos items; valores das medições.

Arquivo: RM.Ctr.Contrato.Form.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 474126 / MCP-1859]** Exibir o botão “Incluir” na aba de lotes para itens inseridos durante o faturamento.

Arquivo: RM.Mov.Movimento.Form.dll

* **[Ticket: 342637 / MCP-1487]** Melhoria na inclusão de itens de movimento selecionando a Flag "Manter Preço Unitário"

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: ITENS COTAÇÃO COM011

* **[Ticket: 96568 / MCP-207]** Feito o acerto no arredondamento da quantidade estornado do item.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: MDF E REJEICAO MDF 003

* **[Ticket: 116077 / MCP-772]** Melhoria para implementação do Horário de Verão no MDF-e

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: NT 2016/001 – Tabela de Unidade de Medidas

* **[Ticket: 123902 / MCP-1875]** Acerto para atender o Mercado Interno e Exportação na Unidade Tributável.

Arquivos: RM.Est.Cadastros.Intf.dll, RM.Est.Cadastros.IService.dll, RM.Est.Utils.Server.dll, RM.Est.Cadastros.Service.dll, RM.Est.Produto.Intf.dll, RM.Est.Produto.Form.dll

### Rotina: ORDEM DE COMPRA COM 002

* **[Ticket: 382579 / MCP-1857]** Foi necessário incluir um filtro ao selecionar um projeto no rateio do centro de custo de um item de movimento para que não seja possível selecionar projetos aos quais o usuário não tem acesso.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: SOLICITACAO DE COMPRAS VIA WEB COM 020

* **[Ticket: 491453 / MCP-1837]** Ajuste para que ao selecionar um tipo de movimento no portal, a filial default carregada fique habilitada para alteração quando a parametrização permitir.

Arquivos: Portal Corpore.Net

## TOTVS Gestão de Pessoas

### Rotina: CARACTERÍSTICAS PESSOAISHABILIDADES RHU36003

* **[Ticket: 97854 / MRH-662]** Ajuste ao sugerir data de expiração

Arquivo: RM.Rhu.Pessoa.Form.dll

### Rotina: PROCESSO DE LANCAMENTO DE ABONOS LINHA RM PTO 35 1240

* **[Ticket: 525656 / MRH-7293]** Correção da inserção de valores de abono para funcionários inseridos em turmas com aulas, cuja parametrização permite abono integral.

Arquivo: RM.Rhu.Utils.Server.dll

### Rotina: REQUISIÇÕES- ALTERAÇÕES DE DADOS FUNCIONAIS RHU36505

* **[Ticket: MRH-6774]** Realizado ajuste para que não ocorra erros ao excluir uma progresão através do processo "Remover Alteração de Dados Funcionais Progressiva".

Arquivo: RM.Rhu.Requisicao.Server.dll

## TOTVS Gestão Financeira

### Rotina: AJUSTE VALOR PRESENTE FIN 005

* **[Ticket: 510586 / MEDU-2759]** Otimização no processo de Ajuste a Valor Presente (AVP). Agora o sistema respeita corretamente o parâmetro "número de documento obrigatório".

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: BOLETO INCLUSAO EXCLUSAO FIN 045

* **[Ticket: 466260 / MEDU-2654]** Otimização no processo de inclusão de boleto.

Arquivos: RM.Fin.Lan.Form.dll, RM.Fin.Lan.Intf.dll

### Rotina: BOLETOS

* **[Ticket: MEDU-2792]** Melhoria no Validador de Boletos Registrados para ser apresentado no Conversor da 12.1.15

Arquivos: RM.Fin.Lan.IService.dll, RM.Fin.Upg.Client.dll, RM.Fin.Lan.Intf.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lan.Data.dll, RM.Fin.Lan.Form.dll, RM.Fin.dll, RM.Fin.Upg.Server.dll

* **[Ticket: MEDU-2792]** Melhoria no Validador de Boletos Registrados

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: emanda já resolvida a partir do envio das dlls RM.Fin.Formula.dll e RM.Fin.Lib.dll. Ticket registrado para "subir" os

* **[Ticket: 540601 / MEDU-2774]** Ajustado o provider de formula do lançamento para que, quando o contexto de execução for a tabela fboleto as funções de formula baseadas em idlan possam ser executadas a partir do idboleto

Arquivos: RM.Fin.Lib.dll, RM.Fin.Formula.dll

### Rotina: FATURAS A PAGAR

* **[Ticket: MEDU-2817]** Disponibilizado para a Fórmula Visual os parâmetros do FinLanFaturaParamsProc.Faturas e FinFaturaParamsProc.lancamentosFaturados

Arquivo: RM.Fin.Lan.Intf.dll

* **[Ticket: MEDU-2817]** Disponibilizado para a Fórmula Visual os parâmetros do FinLanFaturaParamsProc.Faturas e FinFaturaParamsProc.lancamentosFaturados

Arquivos: RM.Fin.Lan.Data.dll, RM.Fin.Lan.Form.dll

### Rotina: LANCAMENTO ALTERACAO FIN 172

* **[Ticket: 508098 / MEDU-2677]** Otimização no processo de inclusão/alteração de lançamentos. Agora o sistema exibe corretamente o campo "Número da autenticação" nos lançamentos com Natureza "A Pagar".

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: Registro On-line Santander

* **[Ticket: EDUCTB002-198]** Ajustes no processo de validação da alteração de boleto registrado para quando o mesmo for chamado do Atualizador.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Upg.Server.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 490842 / MEDU-2708]** Melhoria de Performance no retorno bancário

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: DANFE

* **[Ticket: MEDU-2793]** Alteração na DANFE para destacar em negrito e sublinhado os produtos caracterizados perigosos

Arquivo: RM.Fis.Lib.Server.dll

### Rotina: ENVIO NF-E SAIDA VDP9202

* **[Ticket: MEDU-2794]** O disposto na NT 2016/001 aplica-se apenas aos contribuintes que operem no Comércio Exterior, relativamente às notas fiscais relacionadas a Operações de Exportação (tpNF=1-Saída e idDest=3) ou nas Operações vinculadas à Exportação (CFOP=1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505).Caso não atenda a legislação acima a utrib deve buscar a unidade base tributável da unidade do movimento ( comportamento antigo)

Arquivo: RM.Fis.Facade.dll

* **[Ticket: MEDU-2794]** O disposto na NT 2016/001 aplica-se apenas aos contribuintes que operem no Comércio Exterior, relativamente às notas fiscais relacionadas a Operações de Exportação (tpNF=1-Saída e idDest=3) ou nas Operações vinculadas à Exportação (CFOP=1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505).Caso não atenda a legislação acima a utrib deve buscar a unidade base tributável da unidade do movimento ( comportamento antigo)

Arquivos: RM.Fis.NFe.Service.dll, RM.Fis.Facade.dll

### Rotina: ESCRITURACAO LI 01 0025

* **[Ticket: 507161 / MEDU-2750]** Efetuada melhoria para que o processo de escrituração e recálculo do lançamento fiscal funcionem devidamente quando o valor de ipi compõe a base de icms.

Arquivo: RM.Fis.LancFiscal.Service.dll

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 502781 / MEDU-2776]** Geração da tag DrawBack no envio da NF-e

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: ROTINA DE INTEGRACAO

* **[Ticket: MEDU-2513]** - Não verificar versão da ECF para geração de aliquota CSLL no TAF- Ajuste no Calculo do Evento Tributário para que o a verificação do limite de compensação do prejuizo sejá realizada após a inclusão dos lançamentos automaticos Lalur B na Atividade Rural.

Arquivos: RM.Fis.RegrasTributarias.Service.dll, RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Porte da taxa que está sendo cobrada é MENOR do que o porte previsto no procedimento ao qual está vinculada.

* **[Ticket: 456923 / MSAU-5048]** Caso não haja porte, não haverá validação de porte de taxas vinculadas.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: Alteração do cadastro do Parâmetro EMS

* **[Ticket: 468116 / MSAU-5264]** Ao salvar a edição de um item com campo Filial Default marcado na tela, o sistema verifica se já existe outro item marcado como filial default e desconsidera se for o mesmo.

Arquivo: RM.Sau.Parametros.Data.dll

### Rotina: Médico responsável pelo RN não cai na Elaboração de Contas

* **[Ticket: 477631 / MSAU-5297]** Ajuste realizado no formulário para que o profissional cadastrado no formulário Cadastro de Recém Nascido, seja exibido no formulário de Elaboração de Contas, no paciente RN cadastrado.

Arquivo: RM.Sau.RegistroAtendimento.Data.dll

### Rotina: Não permiti excluir condições contratuais do convênio

* **[Ticket: 512358 / MSAU-5575]** Foi habilitado o botão que permite excluír condições contratuais com convênios.

Arquivo: RM.Sau.CadastrosFat.Form.dll

### Rotina: PARAMETROS GERAIS SAU 47 1108

* **[Ticket: 374239 / MSAU-4569]** Alterada a propriedade FormatFromMetaData (false) para exibir a descrição correta e corrigida a posição do checkbox na tela.

Arquivo: RM.Sau.CadastrosFat.Form.dll

### Rotina: PEP PRESCRICAO MEDICA SAU 47 1121

* **[Ticket: 186892 / MSAU-5630]** Realizado ajuste para carregar o material biológico e vasilhame default para as solicitações de exames realizadas no PEP 2.0.

Arquivo: RM.Sau.PepHis.Server.dll

### Rotina: PRONTUARIO ELETRONICO - Ajuste na Justificativa de Prescrição

* **[Ticket: 399031 / MSAU-4941]** Ajuste realizado para que os itens do tipo restrito também apareçam na justificativa da prescrição.

Arquivo: RM.Sau.Pep.Data.dll

### Rotina: Registro de Informações Cirúrgicas

* **[Ticket: 436555 / MSAU-5798]** Ajuste para o correto envio de dados para faturamento.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: Tamanho de tabelas distintas

* **[Ticket: 275536 / MSAU-3431]** Realizado ajuste para salvar a prescrição quando o usuário ultrapassar o limite de caracteres permitido no banco de dados.

Arquivo: RM.Sau.PepHis.Server.dll

### Rotina: XML Gerado na versão 3.03.01

* **[Ticket: 538746 / MSAU-5754]** Ajuste para caso não haja número de CNS do paciente, para que a TAG seja omitida

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Gestão Patrimonial

### Rotina: UTILITARIOS FECHAMENTO DE PERIODO PAT 37 93

* **[Ticket: 398246 / MEDU-2183]** Atualiação da informação do período de cálculo atual na barra de tarefa do produto

Arquivos: RM.Pat.dll, RM.Pat.Patrimonio.Form.dll, RM.Pat.Parametros.Intf.dll

* **[Ticket: 398246 / MEDU-2183]** Atualização no processo de leitura de mes/ano fechamento

Arquivo: RM.Pat.Periodicidade.Form.dll

* **[Ticket: 398246 / MEDU-2183]** Atualização da leitura de parâmetros do sistema

Arquivos: RM.Pat.Calculo.Form.dll, RM.Pat.Contabilizacao.Form.dll, RM.Pat.Patrimonio.Form.dll

## TOTVS Incorporação

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 405660 / MCP-1765]** Alterado o processo de Aditivos para permitir incluir novas regras de Financiamento Minha Casa Minha Vida, desde que as anteriores estejam com todas as parcelas canceladas, ou, estejam sendo canceladas no mesmo aditivo

Arquivos: RM.Imb.Contratos.Form.dll, RM.Imb.Contratos.Server.dll, RM.Imb.Recursos.dll, RM.Imb.UserControls.dll, RM.Imb.Empreendimento.Form.dll, RM.Imb.Empreendimento.Server.dll

* **[Ticket: 405660 / MCP-1765]** Alterado o processo de Aditivos para permitir incluir novas regras de Financiamento Minha Casa Minha Vida, desde que as anteriores estejam com todas as parcelas canceladas, ou, estejam sendo canceladas no mesmo aditivo

Arquivos: RM.Imb.Contratos.Server.dll, RM.Imb.Aditivos.Form.dll, RM.Imb.Aditivos.Server.dll, RM.Imb.Contratos.Data.dll, RM.Imb.Recursos.dll, RM.Imb.Contratos.IServer.dll, RM.Imb.UserControls.dll, RM.Imb.Aditivos.IServer.dll, RM.Imb.Empreendimento.Data.dll

* **[Ticket: 405660 / MCP-1765]** Alterado o processo de Aditivos para permitir incluir novas regras de Financiamento Minha Casa Minha Vida, desde que as anteriores estejam com todas as parcelas canceladas, ou, estejam sendo canceladas no mesmo aditivo

Arquivo: RM.Imb.UserControls.dll

* **[Ticket: 405660 / MCP-1765]** Alterado o processo de Aditivos para permitir incluir novas regras de Financiamento Minha Casa Minha Vida, desde que as anteriores estejam com todas as parcelas canceladas, ou, estejam sendo canceladas no mesmo aditivo

Arquivo: RM.Imb.Empreendimento.Data.dll

### Rotina: DIMOB LAYOUT IMB 49 816

* **[Ticket: 519357 / MCP-1887]** Alterada a estrutura da tabela de coligadas para que o código do município seja tratado como texto e não número.

Arquivo: RM.Imb.DIMOB.Server.dll

### Rotina: DIMOB GERACAO DE ARQUIVO POR EMPREENDIMENTO IMB 49 815

* **[Ticket: 512242 / MCP-1866]** Alterada a rotina da DIMOB para aluguel antigo para que seja enviado o código da cidade do empreendimento.

Arquivo: RM.Imb.DIMOB.Server.dll

## TOTVS Manutenção

### Rotina: FUNCIONARIOS

* **[Ticket: MCP-1694]** Melhoria no acesso aos menus officina

Arquivo: RM.Mnt.Server.dll

## TOTVS Processo Seletivo

### Rotina: Boleto - Processo Seletivo

* **[Ticket: 511213 / MEDU-2683]** Ajuste na validação da tabela master dos relatórios utilizados para boleto de inscrição do processo seletivo.

Arquivos: App\_Web\_edupsimpressoes.ascx.ca9058f9.dll, App\_Web\_edupsrelatoriodotnetwebform.aspx.ca9058f9.dll, App\_Web\_edupsboleto.ascx.784c668b.dll, RM.EduPS.dll, RM.EduPS.LibWeb.WebForm.dll

# 12.1.15.116

## TOTVS Automação de Ponto

### Rotina: Erro Alterar Horário por Intervalo

* **[Ticket: 219799 / MRH-2830]** Foram realizadas alterações no sistema na parte de armazenamento de histórico de horários, permitindo a mudança de escala para um funcionário.

Arquivo: RM.Pto.Horario.Data.dll

## TOTVS Construção e Projetos

### Rotina: GERACAO DE PEDIDOS PRJ 33 828

* **[Ticket: 543334 / MCP-1953]** Verificado a conversão de valores nulos de insumos globais, durante o cálculo do histograma.

Arquivo: RM.Prj.Calculo.Server.dll

## TOTVS Educacional

### Rotina: CENSO

* **[Ticket: EDUCACIONAL01-134]** Alteração do Censo da Educação Básica para trabalhar com o cadastro de Instituição do MEC, que pode ser por filial ou por nível de ensino.

Arquivos: RM.Edu.Cadastros.Intf.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.Cadastros.Data.dll, RM.Edu.Cadastros.Form.dll, RM.Edu.Academico.Data.dll, RM.Edu.Academico.Form.dll, RM.Edu.Parametros.Form.dll

### Rotina: GERACAO DE MOVIMENTO POR COMPETENCIA EDU 50 230

* **[Ticket: 509087 / MEDU-2805]** Ajuste na consulta de contratos de forma que o comportamento setado para as bolsas em cascata não zerassem o valor do item de movimento.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: Piloto - Portal Aluno 12.1.15

* **[Ticket: EDUEDU002-802]** Ajuste para exibir os arquivos das aulas na tela de arquivos

Arquivos: FrameHTML

### Rotina: WEBSERVICE EDU 50 493

* **[Ticket: 546236 / MEDU-2799]** Ajuste no DataServer EduAprovacaoFrequenciaDiariaData, possibilitando que se execute o SaveRecord sem informar registro de frequência.

Arquivos: RM.Edu.NotaFalta.Intf.dll, RM.Edu.NotaFalta.Data.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIO

* **[Ticket: MRH-3208]** Ajuste na tela de envelope de pagamento

Arquivo: RM.Fop.Envelope.Form.dll

### Rotina: FUNCIONARIOS CADASTRO LAB 01 128

* **[Ticket: 548410 / MRH-7748]** Ajuste no controle de validação do número de salário composto

Arquivo: RM.Fop.Funcionario.Form.dll

### Rotina: FUNCIONARIOS RESCISAO LAB 01 177

* **[Ticket: 458130 / MRH-7769]** Ao calcular rescisão de funcionários com valores de férias e aviso, ocorria erro de chave duplicada caso a data do calculo e do aviso fossem iguais

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Framework

### Rotina: Bug , RM realiza a verificação de atualizações quando abre actions pelo fluig ,mesmo quando o cliente já está aberto na

* **[Ticket: 491061 / MFRWBH-1212]** Alteração para que ao acessar uma action através do fluig estando o RM já aberto, não verifique atualizações.

Arquivo: RM.exe

### Rotina: CADASTRO

* **[Ticket: MFRWBH-1278]** O transfermode foi alterado para Streamed novamente.

Arquivo: RM.Lib.dll

### Rotina: LOG DE AUDITORIA - CONFIGURAÇÃO FRW00046

* **[Ticket: MFRWBH-1277]** A rotina de cadastro de log no critical log foi otimizada.

Arquivo: RM.Lib.dll

### Rotina: PROJETO GERACAO DO PROJETO MTD 00010

* **[Ticket: 538148 / MFRWBH-1270]** -Os objetos que compõem o metadados devem ser importados corretamente.

Arquivo: RM.Glb.ImpExp.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CALCULOS

* **[Ticket: MCP-1954]** NF-e - Calculo de ICMS desonerado

Arquivos: RM.Mov.Facade.dll, RM.Mov.Movimento.Service.dll

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 206703 / MCP-1949]** Melhoria no faturamento de movimento de ordem de compra para movimento de nota fiscal

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: TAB AUX MOTIVO REFERENCIA AUX 014

* **[Ticket: 416578 / MCP-1901]** Inclusão do motivo Cópia por Referência - NFeProdutorRural na lista de Devolução de Movimentos Relacionados.

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GERENCIA DE RH TABELAS SALARIAIS VINCULACAO RHU 36 045

* **[Ticket: 300068 / MRH-3918]** Realizado ajuste de forma a permitir a vinculação de uma tabela salarial para duas ou mais lotações distintas.

Arquivo: RM.Rhu.TabelaSalarial.Data.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO ALTERACAO FIN 172

* **[Ticket: 501570 / MEDU-2693]** Ajustado a validação de campos somente leitura dos lançamentos financeiros.

Arquivo: RM.Fin.Lib.dll

* **[Ticket: 481418 / MEDU-2593]** Otimização no processo de inclusão/alteração de lançamentos. Agora o sistema exibe corretamente o campo "Nosso Número" nos lançamentos com Natureza "A Pagar".

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 413083 / MEDU-2778]** Alteração no calculo do DIFAL no envio da NF-e

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: 394018 / MEDU-2777]** Alteração no envio de NF-e de Devolução de exportação.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NF E PARAMETRIZACAO DE MOVIMENTO RELACIONADO A NF E NF 01 0048

* **[Ticket: 471091 / MEDU-2771]** Alteração no calculo do ICMS desonerado, quando a base de calculo do tributo possui redução.

Arquivos: RM.Fis.Tributo.Service.dll, RM.Fis.Tributo.IService.dll

* **[Ticket: 471091 / MEDU-2771]** Alteração no calculo do ICMS Desonerado

Arquivo: RM.Fis.NFe.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Erro na geração da DMED

* **[Ticket: 515562 / MSAU-5611]** Realizado ajuste para gerar o arquivo DMED para cliente que utilizam a integração com backoffice DataSul.

Arquivo: RM.Sau.Faturamento.Data.dll

### Rotina: PRONTUARIO ELETRONICO - Ajuste na Justificativa de Prescrição

* **[Ticket: 399031 / MSAU-4941]** Rollback no commit pois a funcionalidade está correta.

Arquivo: RM.Sau.Pep.Data.dll

## TOTVS Gestão Patrimonial

### Rotina: OPERACOES PATRIMONIAIS TRANSFERENCIA MONETARIA PAT 37 47

* **[Ticket: 443539 / MEDU-2798]** Atualização no processo de transferência de controle referente à data da ocorrência

Arquivo: RM.Pat.Ocorrencia.Service.dll

## TOTVS Incorporação

### Rotina: ADITIVO - TROCA DE COMPRADOR IMB49785

* **[Ticket: MCP-1959]** Resource de histórico de cancelamento de lançamentos foi restaurado

Arquivo: RM.Imb.Recursos.dll

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Ajuste no conversor para revitalização que nçao estava tratando a conversão para clientes que usam titulo bloqueados no protheus

Arquivo: RM.Imb.Venda.Upg.Data.dll

# 12.1.15.117

## TOTVS Educacional

### Rotina: Usuario sem permissão de editar horarios da turma/disc , e mesmo assim sistema permite edição e altera data final da tur

* **[Ticket: 548633 / MEDU-2808]** Alteração no comportamento do sistema para não alterar automaticamente a data final e nem a data inicial do Horário da Turma/Disciplina quando as mesmas estão inconsistentes.O sistema continuará emitindo mensagem de alerta e caberá ao usuário alterar esta data para um valor válido, caso este usuário tenha permissão de acesso para alteração/inclusão.As validações destas datas serão apresentadas sempre que um registro for Salvo OU quando clicamos/sairmos dos campos de data.

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

## TOTVS Framework

### Rotina: LOG DE AUDITORIA - CONFIGURAÇÃO FRW00046

* **[Ticket: MFRWBH-1285]** O Critical Log foi otimizado.

Arquivo: RM.Lib.Server.dll

### Rotina: LOGIN FRW 00048

* **[Ticket: 439260 / MFRWBH-1267]** O cadastro de usuário foi otimizado, onde agora é obrigado preenchar o campo Início de validade.

Arquivo: RM.Glb.Seguranca.Intf.dll

## TOTVS Gestão Contábil

### Rotina: CONTABILIZACAO

* **[Ticket: MEDU-2861]** Ajuste na tela compartilhada de lançamentos contábeis.

Arquivos: RM.Ctb.Utils.Server.dll, RM.Ctb.Lib.WinForms.dll

## TOTVS Gestão de Pessoas

### Rotina: Cadastro de Municípios eSocial

* **[Ticket: 94946 / MRH-261]** Ajuste no cadastro de funcionário para valor default do campo Estado no Endereço Principal

Arquivo: RM.Rhu.Lib.WinForms.dll

### Rotina: PROCESSO DE LANCAMENTO DE ABONOS LINHA RM PTO 35 1240

* **[Ticket: 525656 / MRH-7904]** Correção da utilização de abono integral para funcionários em inseridos em turmas com aulas.

Arquivo: RM.Rhu.Utils.Server.dll

## TOTVS Gestão Financeira

### Rotina: SESSAO DE CAIXA BAIXA FIN 269

* **[Ticket: 538842 / MEDU-2803]** Otimização no processo de baixa de lançamento via sessão de caixa. Agora os sistema preenche corretamente o valor da baixa.

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 547916 / MEDU-2851]** Alteração na tag vDespAdu quando o valor das despesas Aduneiras é zero.

Arquivo: RM.Fis.NFe.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: AGENDAMENTO SAU 47 1135

* **[Ticket: 445112 / MSAU-5149]** Ao efetuar a configuração de um período para agendamento o sistema mostra as informações de data para agendamento somente quando o usuário seleciona uma data dentro do período selecionado. Alterado o sistema para sempre exibir os período de agendamento configurado na tela de agenda de atendimentos.

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

### Rotina: Carteira de Convênio - Pesquisa do Paciente

* **[Ticket: 428287 / MSAU-4992]** Ajuste realizado na pesquisa de paciente para que seja exibido apenas um registro de paciente baseando-se na data mais atual.

Arquivo: RM.Sau.Common.Data.dll

## TOTVS Gestão Patrimonial

### Rotina: CADASTROS PATRIMONIOS PAT 37 39

* **[Ticket: 421630 / MEDU-2328]** Implementação no modo de atualização da imagem do cadastro de patrimônio

Arquivo: RM.Pat.Patrimonio.Form.dll

# 12.1.15.118

## Outros

* **[Ticket: Alterações Gerais]** Alteração nos arquivos de atualização do atualizador para contemplar o processo Financeiro (Fin): Verificação de Impactos na estrutura do Novo Boleto Registrado

Arquivos: RM.Beta.upg, RM.Upgrade.upg

## TOTVS Automação de Ponto

### Rotina: Espelho Cartão de Ponto exibe horas extras sem acréscimo.

* **[Ticket: 228716 / MRH-3799]** Alterações na rotina de impressão do relatório do espelho para considerar fórmulas cadastradas em eventos do sindicato.

Arquivos: RM.Pto.Ocorrencia.Data.dll, RM.Pto.Relatorio.Data.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** SGBD: SQL SERVER / ORACLEScript: /\*LEONARDO MONTEIRO DOS SANTOS - CN.2016.12\_03 - OC.:MEDU-1489 - 05/01/2017 VERSAO.: 12.1.15 - EQUIPE:MANUT \*/ISSUE: MGCADBH-130Descrição: Validação de duplicidade de registros.

Arquivo: Cvn.12.1.15.sql

## TOTVS Controle de Infecção Hospitalar

### Rotina: "Via de Acesso" do BI de Procedimento Cirúrgico

* **[Ticket: 400402 / MSAU-5586]** Ao realizar a visualização dos dados do BI de procedimento cirúrgico o sistema não apresenta o número da via de acesso correta. Alterado o sistema no BI de procedimento de cirúrgico para apresentar o mesmo número da via de acesso do cadastro de cirurgia.

Arquivo: RM.SauIH.Estatisticos.Data.dll

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 390514 / MEDU-2110]** Ajuste na grid de filiação do aluno, evitando que o campo FALECIDO quando estiver NULL na base o check box fique colorido de amarelo.

Arquivo: RM.Edu.Aluno.Form.dll

### Rotina: Evoluções na Gestão de Estágio

* **[Ticket: EDUEDU004-1]** Ajustes na chamada a página para criação de funcionários na solicitação de estágio

Arquivos: Portal Corpore.Net

### Rotina: Project-548731 CENSO - Erro causado por professor lecionar em outras filiais Project-548731

* **[Ticket: 563237 / MEDU-2855]** Alteração na geração do arquivo de docentes do Censo da Educação Superior para filtrar os dados por filial.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: Réplica de alterações na matrícula para o Ser Educacional

* **[Ticket: EDUEDU001-1689]** Piloto - matrícula entre níveis de ensino

Arquivos: RM.Edu.Consts.dll, RM.Edu.Global.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.Formula.dll, RM.Edu.Matricula.Data.dll, RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.Facade.Intf.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Intf.dll, RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Parametros.Intf.dll, RM.Edu.PeriodoLetivo.Intf.dll, RM.Edu.Server.dll, RM.Edu.Utils.Server.dll, RM.Edu.dll, RM.Edu.Academico.Form.dll, RM.Edu.Matricula.Form.dll, RM.Edu.MatrizCurricular.Form.dll, RM.Edu.Parametros.Form.dll, RM.Edu.PeriodoLetivo.Form.dll, RM.Edu.Services.Server.dll, RM.Edu.Financeiro.Server.dll, RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.Matricula.Server.dll, RM.Edu.MatrizCurricular.Data.dll

* **[Ticket: EDUEDU001-1689]** Merge da implmenteção: Matricula entre níveis de ensino da 11.80 para 12.1.15

Arquivos: RM.Edu.ProcSel.Data.dll, RM.Edu.ProcSel.Server.dll

## TOTVS Framework

### Rotina: LOGIN FWB 00011

* **[Ticket: 565696 / MFRWBH-1287]** Durante a alteração de senha no próximo login utilizando a integração LDAP, o sistema tem que validar corretamente as senhas informadas antes de realizar a alteração para a nova senha.

Arquivos: RM.Lib.dll, RM.Lib.Server.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS BALANCETE CTB 38 113

* **[Ticket: 178929 / MEDU-2579]** Alteração do layout do relatório Balancete Centro de Custo / Contábil para que apresente os caracteres marcadores como era feito na versão Delphi.

Arquivos: RM.Ctb.Relatorios.Service.dll, RM.Ctb.Lan.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: EDICAO DE MOVIMENTO MOV 002

* **[Ticket: 361515 / MCP-1483]** Melhoria no processo de movimentação

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: FATURAMENTO DE CONTRATO CTR 010

* **[Ticket: 269365 / MCP-1238]** Ajuste para aumentar a quantidade de caracteres da Serie do Tipo de Movimento Para Venda

Arquivos: RM.Ctr.Faturamento.Intf.dll, RM.Mov.TipoMovimento.Intf.dll

### Rotina: IMPORTACAO DE MOVIMENTO MOV 039

* **[Ticket: 427100 / MCP-1647]** Melhoria no processo de Importação de Movimento via Conceito para atualizar Cupom Fiscal vinculado.

Arquivos: RM.Mov.CupomFiscal.Service.dll, RM.Mov.Movimento.Service.dll

### Rotina: REDUCAO Z COM 023

* **[Ticket: 208553 / MCP-1878]** Ajuste para alterar a nomenclatura dos campos Cupom Inicial e Cupom Final para COO Inicial e COO Final

Arquivos: RM.Mov.CupomFiscal.Intf.dll, RM.Mov.CupomFiscal.Form.dll

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: 391627 / MCP-1654]** Melhoria no processo de comparação de tributos.

Arquivo: RM.Mov.Movimento.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS CURRICULOS EXTERNOS RHU 36 022

* **[Ticket: 541147 / MRH-7602]** A configuração estava sendo salva somente para o Tipo de Pessoa = Candidato. Ajustado para salvar a configuração para todos os outros tipos.

Arquivo: RM.Rhu.CadCurriculo.Form.dll

### Rotina: PROCESSO DE CALCULO DE ABONO PTO 35 1300

* **[Ticket: 537030 / MRH-7822]** Foram feitas alterações no método de abono do Vitae com o intuito de identificar um funcionário com duplo vínculo em diferentes coligadas.

Arquivo: RM.Rhu.Utils.Server.dll

* **[Ticket: 537030 / MRH-7822]** Foram feitas alterações no método de abono do Vitae com o intuito de identificar um funcionário com duplo vínculo em diferentes coligadas.

Arquivo: RM.Rhu.Utils.Server.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: ATENDIMENTOS CRM 321443

* **[Ticket: 425612 / MCP-1690]** Ao salvar um atendimento usando o cliente online, caso esse não de a opção de alterar o local de entrega, o seu valor anterior não será apagado.

Arquivo: App\_Web\_crmclienteonlineedicao.ascx.72e19a66.dll

## TOTVS Gestão Financeira

### Rotina: BOLETO REMESSA COBRANCA ELETRONICA FIN 046

* **[Ticket: 427841 / MEDU-2686]** Otimização no processo de importação de arquivo de retorno por agrupamento de extrato. Agora o sistema realiza o agrupamento corretamente quando o parâmetro de agrupamento de extrato estiver marcado.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: BORDERO CANCELAMENTO DE REMESSA DE PAGAMENTO FIN 051

* **[Ticket: 475673 / MEDU-2726]** Otimização no processo de retorno de pagamento. Agora o sistema executa o processo corretamente.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NF E CONSULTAR EVENTO TOTVS COLABORACAO NF 01 0034

* **[Ticket: 468517 / MEDU-2801]** Alteração para que a mensagem de rejeição apresentada no log do historico do evento, seja mostrada também no log da consulta autorização do evento.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS EFD PIS COFINS LI 01 0033

* **[Ticket: 441111 / MEDU-2522]** Modificação do Contexto do Gerador de Saídas: Carregar o CNPJ da Filial Matriz dos Parâmetros do Gestão Fiscal.

Arquivo: RM.Fis.Sped.Server.dll

## TOTVS Gestão Hospitalar

### Rotina: AGENDAMENTO SAU 47 1135

* **[Ticket: 445112 / MSAU-5149]** Ao efetuar a configuração de um período para agendamento o sistema mostra as informações de data para agendamento somente quando o usuário seleciona uma data dentro do período selecionado. Alterado o sistema para sempre exibir os período de agendamento configurado na tela de agenda de atendimentos.

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

### Rotina: Carteira de Convênio - Pesquisa do Paciente

* **[Ticket: 428287 / MSAU-4992]** Ajuste realizado na pesquisa de paciente para que seja exibido apenas um registro de paciente baseando-se na data mais atual.

Arquivo: RM.Sau.Common.Data.dll

### Rotina: Teste de Aceitação (Homologação) - 12.1.10

* **[Ticket: SAUHRM01-711]** Ajuste na ordenação dos atendimentos na worklist

Arquivo: RM.Sau.PepHis.Server.dll

## TOTVS Incorporação

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhoria do projeto de revitalização para clientes piloto.

Arquivos: RM.Imb.Aluguel.ContratoAdm.Form.dll, RM.Imb.Aluguel.ContratoLoc.Form.dll, RM.Imb.Venda.Lib.WinForms.dll, RM.Imb.Contratos.Form.dll, RM.Imb.Venda.Upg.Intf.dll, RM.Imb.dll, RM.Imb.Conversor.Form.dll, RM.Imb.Propostas.Form.dll

* **[Ticket: CPTIN001-478]** Melhoria na descrição das mensagens do projeto de revitalização.

Arquivo: RM.Imb.Venda.Upg.Intf.dll

* **[Ticket: CPTIN001-478]** Melhoria do projeto de revitalização para clientes novos.

Arquivos: RM.Imb.dll, RM.Imb.Venda.Upg.Intf.dll, RM.Imb.Aluguel.ContratoAdm.Form.dll, RM.Imb.Aluguel.ContratoLoc.Form.dll, RM.Imb.Venda.Lib.WinForms.dll, RM.Imb.Venda.Upg.Data.dll, RM.Imb.Contratos.Form.dll, RM.Imb.Propostas.Form.dll

# 12.1.15.119

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB ABONAR ATRASOS E FALTAS PTO 35 1257

* **[Ticket: 512444 / MRH-7994]** Foram realizadas adaptações do processo do espelho do RM Chronus para a tela "Abonar" do portal com o objetivo de apresentar corretamente os abonos gerados por atestados do tipo "Afastamento".

Arquivo: RM.Pto.Abono.Data.dll

### Rotina: PORTAL WEB VISUALIZAR JUSTIFICATIVAS PTO 35 1253

* **[Ticket: 574829 / MRH-7964]** Otimizada a tela de aprovação de abonos para demonstrar a justificativa dos abonos antes da compensação.

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Business Connect

### Rotina: PADRAO

* **[Ticket: MFRWBH-1316]** Foi realizada uma melhoria no log do conceito a fim de informar com mais detalhes os erros ocorridos.

Arquivo: RM.Con.Concept.Server.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS MEDICAO PRJ 33 941

* **[Ticket: 543927 / MCP-1963]** Ajuste para utilizar o número de casas monetários definido no parâmetro do projeto para o campo valor total do contratado exibido na medição.

Arquivo: RM.Prj.Contrato.Data.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: Erro do log de validação automática de cirurgias

* **[Ticket: 401015 / MSAU-4954]** Ao realizar a importação de cirurgias com dois médicos setados como principais para a mesma cirurgia o sistema não apresenta mensagem de alerta para dois cirurgiões principais. Ao realizar a importação de cirurgias com dois médicos Principais o sistema apresenta a mensagem "Cada via de acesso deve ter um cirurgião principal."

Arquivo: RM.SauIH.Importacao.Data.dll

## TOTVS Educacional

### Rotina: Piloto - Portal Aluno 12.1.15

* **[Ticket: EDUEDU002-802]** Melhoria na visualização de avaliações no Portal do Aluno

Arquivos: RM.Edu.Rest.Server.dll, RM.Edu.NotaFalta.Data.dll

### Rotina: Réplica de alterações na matrícula para o Ser Educacional

* **[Ticket: EDUEDU001-1689]** Ajustes na nomenclatura da funcionalidade de equivalência

Arquivos: RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.Integracoes.Intf.dll, RM.Edu.Integracoes.Form.dll

## TOTVS Folha de Pagamento

### Rotina: SEFIP > Atualizar CEI tomador'

* **[Ticket: 262844 / MRH-3456]** O processo de "Alterar CEI do Tomador" não era executado ao clicar no item de menu

Arquivos: RM.Fop.Sefip.Data.dll, RM.FopFolha.dll

### Rotina: IMPORTACAO DO SAP LAB 01 28

* **[Ticket: 570533 / MRH-8034]** Otimizado processo de Importação SAPpara não exibir mensagem de campo IDADE obrigatório

Arquivo: RM.Fop.Importacao.Data.dll

## TOTVS Framework

### Rotina: USUARIOS COPIA DE PERMISSAO FRW 00072

* **[Ticket: 561146 / MFRWBH-1296]** Melhoria na execução do relatório de permissões dos usuários nas coligadas

Arquivo: RM.Glb.Seguranca.Form.dll

## TOTVS Gerador de Relatórios

### Rotina: RELATORIO

* **[Ticket: MFRWBH-1315]** Foi realizada uma melhoria para permitir adicionar consulta SQL em relatório de provider.Os seguintes critértios devem ser atendidos:1- Os parâmetros de filtro (where) da consulta sql devem ter o mesmo nome dos controles do relatório aos quais eles se referem. Por exemplo:select \* from gcoligada (NOLOCK) where codcoligada = :CODCOLIGADA1 onde CODCOLIGADA1 é o nome do controle na tela do relatório.2- Verificar a ordenação dos campos pelo botão “Ordenação de controles”. Os campos da consulta devem ser movidos para o final nesta lista.

Arquivos: RM.Rpt.Lib.dll, RM.Rpt.Reports.Form.dll

### Rotina: TOTALIZADOR RPT 00020

* **[Ticket: 566633 / MFRWBH-1305]** Ao inserir um valor inicial com expressão, o resultado do totalizador é apresentado corretamente.

Arquivo: RM.Rpt.Executor.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CONTRATOS

* **[Ticket: MCP-1926]** Ajuste para não limpar campos obrigatórios do item de contrato ao salvar o mesmo.

Arquivo: RM.Ctr.Contrato.Form.dll

### Rotina: COPIA A PARTIR DE OUTRO MOVIMENTO

* **[Ticket: MCP-363]** Melhoria na inclusão de movimentos

Arquivo: RM.Mov.Movimento.Form.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: ATENDIMENTOS CRM 321443

* **[Ticket: 494428 / MCP-1899]** Ajuste ao realizar uma pesquisa em um parâmetro do tipo de atendimento, baseado em uma sentença sql específica.

Arquivo: RM.CRM.TipoAtendimento.Data.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA ENCERRAMENTO DE PERIODO FIN 010

* **[Ticket: 519984 / MEDU-2699]** Melhoria em conversor de aplicação financeira

Arquivos: RM.Fin.AplicacaoFinanceira.Intf.dll, RM.Fin.AplicacaoFinanceira.Server.dll, RM.Fin.AplicacaoFinanceira.Data.dll

* **[Ticket: 519984 / MEDU-2699]** Melhoria em conversor de aplicação financeira

Arquivos: RM.Fin.AplicacaoFinanceira.Server.dll, RM.Fin.AplicacaoFinanceira.Data.dll

## TOTVS Gestão Fiscal

### Rotina: CADASTROS MUNICIPIO LI 01 0014

* **[Ticket: 421159 / MEDU-2737]** Alteração na geração do grupo da transportadora.

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: 421159 / MEDU-2737]** Alteração na geração do grupo da transportadora.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 431535 / MEDU-2819]** Alteração na montagem do grupo do XML responsável pelos valores do DIFAL, o valores de diferencial de aliquota devem ser enviados zerados quando a aliquota interestadual for maior que a aliquota interna do estado de destino.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 466454 / MEDU-2931]** Alteração para atender a legislação, onde a informação da inscrição municipal do tomador deve ser enviada com a máscara para o municipio de Cuiabá - MT.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: 375435 / MEDU-2025]** Criação de um parâmetro que será utilizado para validar se as acentuações irão ou não no XML da Nota Fiscal.

Arquivos: RM.Fis.Utils.Server.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES ACESSORIAS ESTADUAIS SEF II LI 01 0029

* **[Ticket: 585399 / MEDU-2939]** Ajuste nas Tags do Menu dos Cadastros referentes ao Prodepe para que os botões de Incluir, Editar e Excluir sejam apresentados corretamente.

Arquivos: RM.Fis.dll, RM.Fis.ApuracaoTrb.Form.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - ECF LI010032

* **[Ticket: MEDU-2910]** - ECF Na geração da ECF o registro 0021 será gerado verificando se o campo "PJ habilitada no Repes, Recap, Padis, ..." estiver marcado.- Cadastro Parâmetros da ECFO campo "PJ Habilitada no Repes, Recap e etc..." foi alterado para a pasta "Mais Informações".O grupo de Programas e Regimes Especiais será habilitado conforme a marcação do campo anterior.

Arquivos: RM.Fis.Filial.Data.dll, RM.Fis.Filial.Form.dll

## TOTVS Gestão Hospitalar

### Rotina: AUDITORIA INTERNA SAU 47 1143

* **[Ticket: 572320 / MSAU-6017]** Ajuste para que o sistema confirme apenas os documentos a confirmar selecionados.

Arquivo: RM.Sau.ControleDocumentos.Form.dll

### Rotina: Erro ao excluir cadastro de RN

* **[Ticket: 477713 / MSAU-5298]** Ao acessar o sistema TOTVS Gestão Hospitalar, ir ao menu Atendimento/Internação/Cadastro de Recém Nascido, selecionar um registro do cadastro de Recém Nascido, exibir o cadastro, clicar no botão delete é exibido uma mensagem de exceção, o que coibia o processo de deleção do registro.

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: OUTROS PROCESSOS SAU 47 1173

* **[Ticket: 99700 / MSAU-5946]** Ajuste na importação do código do município

Arquivo: RM.Sau.Integracoes.Server.dll

## TOTVS Incorporação

### Rotina: Erro Reajuste Contrato - SGI

* **[Ticket: 561024 / MCP-1960]** Alterada a rotina que calcula a variação do pró-rata-dia temporis final para que nos casos onde a correção NÃO É CAPITALIZADA seja removido o fator de multiplicação.

Arquivo: RM.Imb.Reajuste.Server.dll

## TOTVS Planejamento e Controle da Produção

### Rotina: BAIXA DE MATERIAIS PCP 44 285

* **[Ticket: 522061 / MCP-1927]** Melhoria no processo de Baixa estoque de matéria prima para a ordem selecionada

Arquivo: RM.PCP.BaixaMateriais.Service.dll

# 12.1.15.120

## TOTVS Automação de Ponto

### Rotina: PROCESSO DE CALCULO OCORRENCIA 0043 PTO 35 1280

* **[Ticket: 564935 / MRH-8060]** Ajuste realizado no refresh do espelho, antes da correção não estava carregando as informações ao clicar no botão atualizar.

Arquivo: RM.Pto.Batida.Form.dll

## TOTVS Construção e Projetos

### Rotina: Project-331589 Status no anexo de Alterações aprovação de contrato Fluig Project-331589

* **[Ticket: 581789 / MCP-1998]** Atualizando os status do Atendimento gerados, através das alterações realizados no contrato.

Arquivo: RM.Prj.Fluig.Server.dll

## TOTVS Educacional

### Rotina: Project-574353 Bolsas que não devem ser contabilizadas por competência Project-574353

* **[Ticket: 574471 / MEDU-2897]** Foi realizada otimização do processo de contabilização por competência, de forma que seja possível definir, através do cadastro de bolsas, quais bolsas que devem ser consideradas pelo processo de contabilização por competência.

Arquivos: RM.Edu.Contabil.Server.dll, RM.Edu.Financeiro.Form.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF LAB 01 11

* **[Ticket: 562446 / MRH-8089]** Otimizado geração do log da DIRF para exibir os eventos de reembolso do plano de saúde que deverão subtrair o valor

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: INCONSISTENCIAS SGBD 90 9

* **[Ticket: 539138 / MRH-8152]** Ajustes em consulta de AutoInc para melhoria de performance e correção de estouro de conexões em bases Oracle no processo de bloqueio de recalculo

Arquivo: RM.Fop.Processos.Data.dll

## TOTVS Framework

### Rotina: Project-567845 Gatilhos e processos FV não exibem a lista completa de actions disponíveis Project-567845

* **[Ticket: 580892 / MFRWBH-1309]** Correção da pesquisa de actions na aba de Processos de Fórmula visual.

Arquivo: RM.Glb.Workflow.Form.dll

## TOTVS Gerador de Relatórios

### Rotina: GERACAO DE RELATORIO RPT 00005

* **[Ticket: 483301 / MFRWBH-1199]** Ao criar a cópia de um relatório global, o filtro é gravado na coligada 0 fazendo com que esse relatório seja devidamente filtrado.

Arquivo: RM.Rpt.Lib.dll

## TOTVS Gestão Contábil

### Rotina: ESCRITURACAO CONTABIL EXERCICIOS CTB 39 009

* **[Ticket: 472782 / MEDU-2891]** Melhoria em uma consulta feita para a tabela CCONT e melhoria de performance no processo que gera o Saldo Anterior.

Arquivos: RM.Ctb.ConsisteLancamento.Service.dll, RM.Ctb.ExercicioContabil.Service.dll

## TOTVS Gestão Fiscal

### Rotina: ENVIO NF-E SAIDA (VDP9202

* **[Ticket: FISCAL01-12]** Criação de um parâmetro que será utilizado para validar se as acentuações irão ou não no XML da Nota Fiscal.

Arquivo: RM.Fis.Utils.Server.dll

### Rotina: MDF E CONSULTA DE EVENTO MDF 007

* **[Ticket: 150824 / MCP-1213]** Melhoria na consulta do MDF-e quando há rejeição

Arquivo: RM.Fis.TSS.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Integração Shift x Totvs

* **[Ticket: 540405 / MSAU-5721]** Ao realizar a integração com web service shift o sistema não estava conseguindo se comunicar com o web service. Atualizado as web reference de integração com a shift, o sistema esta se comunicando com o web service.

Arquivo: RM.Sau.Integracoes.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: CONTABILIZACAO DEPRECIACAO

* **[Ticket: MEDU-736]** Implementação de serviço para retornar a depreciação ajustada do patrimônio

Arquivos: RM.Pat.Utils.Intf.dll, RM.Pat.Utils.Server.dll

### Rotina: INTEGRACOES INTEGRACAO AQUISICOES COMPRAS RM NUCLEUS PAT 37 64

* **[Ticket: 368063 / MEDU-2439]** Atualização na rotina de cálculo das quantidades devolvidas do movimento

Arquivo: RM.Pat.Integracao.Data.dll

## TOTVS Incorporação

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 567278 / MCP-1968]** Alteração no processo de Reajuste para considerar corretamente os componentes que devem ser usados no cálculo

Arquivo: RM.Imb.Reajuste.Server.dll

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhorias de performance no Utilitários de lançamentos financeiros.

Arquivos: RM.Imb.Conversor.Data.dll, RM.Imb.Conversor.Server.dll

## TOTVS Planejamento e Controle da Produção

### Rotina: BAIXA DE MATERIAIS PCP 44 285

* **[Ticket: 522061 / MCP-1927]** Melhoria no processo de Baixa estoque de matéria prima para a ordem selecionada

Arquivo: RM.PCP.BaixaMateriais.Service.dll

# 12.1.15.121

## TOTVS Automação de Ponto

### Rotina: PROCESSO DE LANCAMENTO DE ABONOS LINHA RM PTO 35 1240

* **[Ticket: 578556 / MRH-8002]** Foram feitas alterações no log do processo de abono global com o objetivo de corrigir as informações mostradas ao final do processo. A correção permitiu mostrar a quantidade de tempo certa abonada

Arquivo: RM.Pto.Abono.Intf.dll

### Rotina: Project-282784 APROVACAO DE ABONO - DOIS PERIODOS Project-282784

* **[Ticket: 289106 / MRH-3543]** Foram realizadas alterações na rotina de visualização de ocorrências para o funcionário no portal, com o objetivo de permitir que o sistema apresente todas as ocorrências para determinado funcionário.

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Construção e Projetos

### Rotina: PLANILHAS CRONOGRAMA PRJ 33 866

* **[Ticket: 586654 / MCP-2015]** Adicionado o valor do ressuprimento no calculo de datas, do cronograma de desembolso

Arquivo: RM.Prj.Cronograma.Server.dll

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 390514 / MEDU-2110]** Ajuste na grid de filiação do aluno, evitando que o campo FALECIDO quando estiver NULL na base o check box fique colorido de amarelo.

Arquivos: RM.Edu.Aluno.Intf.dll, RM.Edu.Aluno.Data.dll

### Rotina: Definição de bolsistas sem apontar a pessoa do bolsista para os projetos de Pesquisa e Extensão

* **[Ticket: EDUEDU004-59]** Ajustes nos fluxos de pesquisa e extensão

Arquivo: RM.Edu.PesquisaExtensao.Form.dll

## TOTVS Folha de Pagamento

### Rotina: MAQUINA DE CALCULO FOP 1 4 1 91

* **[Ticket: 592074 / MRH-8146]** Ajuste no cálculo de média da provisão de férias para considerar a perda do periodo aquisitivo somente quando o funcionário ficar 31 dias ou mais com afastamento tipo R - Licença Remunerada.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: PORTAL WEB GESTAO DE FERIAS LAB 01 208

* **[Ticket: 521382 / MRH-7229]** Tratar na apuração das faltas do cadastro de férias do executável, para subtrair a referência do CC 128 somente quando o evento for do tipo Provento.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: RAIS LAB 01 12

* **[Ticket: 530771 / MRH-8160]** Ajuste na rotina RAIS quando funcionário não possuir vínculo com sindicato.

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 504006 / MRH-8164]** Ajuste no processo de geração da RAIS

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 411518 / MRH-7854]** Ajuste na rotina RAIS para não considerar data de pagamento do evento para códigos de cálculo 96 e 37 e sim mês e ano de competência para comparação com data de desligamento.

Arquivos: RM.Fop.BaseDados.Data.dll, RM.Fop.Dominio.dll

## TOTVS Framework

### Rotina: HOST FRW00038

* **[Ticket: MFRWBH-1329]** Foi realizado nas permissões Alterar e Excluir que estavam invertidas em anexos customizados

Arquivo: RM.Lib.Client.Custom.dll

## TOTVS Gestão Contábil

### Rotina: ESCRITURACAO CONTABIL LANCAMENTOS ALTERACAO DA DISTRIBU CTB 38 157

* **[Ticket: 586308 / MEDU-2957]** Ajuste no Processo de Alteração de Partidas em Grupo para que não seja exibida a mensagem e a validação continue sem interrupções.

Arquivo: RM.Ctb.Lan.IService.dll

## TOTVS Gestão de Pessoas

### Rotina: PDI RHU 36 089

* **[Ticket: 456866 / MRH-7138]** Ajuste ao iniciar PDI

Arquivos: RM.Rhu.AvalDesemp.Intf.dll, RM.Rhu.AvalDesemp.Data.dll, App\_Web\_rhupdidetalhe.ascx.72531707.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: PARAMETROS DO AGILIS CRM 321441

* **[Ticket: 524354 / MCP-1871]** Ajuste de layout para uma melhor visualização dos textos de acompanhamento.

Arquivos: Portal Corpore.Net

## TOTVS Gestão Financeira

### Rotina: EXTRATO DE CAIXA COMPENSAR FIN 144

* **[Ticket: 411226 / MEDU-2973]** Melhoria no sistema para não carregar a hora nos campos de Data nos processos de Baixa e Compensação de Extrato.

Arquivos: RM.Fin.Extrato.Service.dll, RM.Fin.Lan.Form.dll, RM.Fin.Lan.Service.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 384106 / FINANCEIRO01-87]** Ajustado o cancelamento de baixa, para poder limpar o valor da diferença a maior ou menor dos campos BX do lançamento.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: BUG QUANDO MUDA PARAMETRO DA CLASSIFICACAO DE RISCO

* **[Ticket: 574194 / MSAU-5993]** Ajuste para a correta visualização após a troca de parâmetros.

Arquivos: RM.Sau.RegistroAtendimento.Data.dll, RM.Sau.RegistroAtendimento.Form.dll

### Rotina: problema antigo Erro no calculo de procedimento

* **[Ticket: 555300 / MSAU-6134]** Ajuste para o cálculo correto do procedimento ao faturar uma remessa.

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Gestão Patrimonial

### Rotina: CONTABILIZACAO DEPRECIACAO

* **[Ticket: MEDU-736]** Atualização do serviço de retorno da depreciação ajustada para trazer dois cenários

Arquivos: RM.Pat.Utils.Intf.dll, RM.Pat.Utils.Server.dll

## TOTVS Incorporação

### Rotina: O processo de distratar a venda não está cancelando o residuo de parcelas

* **[Ticket: 255527 / MCP-1144]** Incidente:O processo de gerar parcela de resíduo estava permitindo selecionar parcelas de vendas que estavam distratadas, somente fazendo a validação ao final do processo. Foi solicitado que a validação fosse feita logo no início do processo.Solução: Foi inserida uma mensagem no início do processo caso o usuário selecione parcelas de vendas distratadas

Arquivos: RM.Imb.Venda.Contrato.Data.dll, RM.Imb.Venda.Contrato.Form.dll

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhorias de performance para o Utilitários de lançamentos financeiros.

Arquivos: RM.Imb.Venda.Lib.Intf.dll, RM.Imb.Conversor.Data.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: RELATORIOS PERFIL PROFISSIOGRAFICO PREVIDENCIARIO PPP SMT 36 578

* **[Ticket: 301427 / MRH-4008]** Realizado ajuste na geração do PPP de forma que o campo 13.1 exiba corretamente as informações quando o funcionário possuir vínculo em tomador de serviços.

Arquivo: RM.Smt.Relatorio.Data.dll

# 12.1.15.122

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO CANCELAMENTO DE MOVIMENTO PTO 35 1188

* **[Ticket: 602980 / MRH-8304]** Alterações no processo de exclusão do histórico do cartão de ponto para permitir a exclusão de registros que sejam anteriores a data de admissão do funcionário

Arquivo: RM.Pto.Funcionario.Data.dll

## TOTVS Construção e Projetos

### Rotina: INTEGRACAO MANUTENCAO PRJ 33 934

* **[Ticket: 594994 / MCP-2023]** Na integração com MNT, o turno está sendo enviado errado quando a apropriação vai de um dia para outro

Arquivo: RM.Prj.Mobilidade.Server.dll

### Rotina: Project-545675 Descrição do Preço do Insumo Project-545675

* **[Ticket: 598587 / MCP-2032]** Permitir que o Preço ativado seja alterado, e que os preços com a mesma descrição sejam modificados de acordo com necessidade do cliente.

Arquivo: RM.Prj.Insumo.Data.dll

## TOTVS Educacional

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 514671 / MEDU-2903]** Ajuste na query de filtro no cálculo de valores de bolsas de crédito para considerar o código da bolsa como alfanumérico.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: GERAR CONTABILIZACAO EDU 50 234

* **[Ticket: 593813 / MEDU-2989]** Foi realizada otimização do processo de contabilização por competência, permitindo ao sistema, contabilizar um contrato que tenha sido contabilizado em uma versão anterior a release 12.1.14 e que tenha sido estornado.

Arquivo: RM.Edu.Contabil.Server.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIOS RESCISAO LAB 01 177

* **[Ticket: 283767 / MRH-7530]** Otimizado processo de transferência para preencher as informações de sucessão de vinculo

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: RELATORIOS SALARIO CONTRIBUICAO FOP 34 428

* **[Ticket: 545391 / MRH-7779]** Otimizado log da guia de INSS

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: RESCISAO HOMOLOGNET LAB 01 219

* **[Ticket: 98321 / MRH-764]** Criado o parametro "Desconsiderar incidência em salário para base de periculosidade" na geração do Homolognet.

Arquivos: RM.Fop.Processos.Intf.dll, RM.Fop.Lib.Intf.dll, RM.Fop.Processos.Data.dll, RM.Fop.Processos.Form.dll

* **[Ticket: 557222 / MRH-8151]** Otimizado geração do homolognet para preencher a tag "VLAdiantamentoSalarial"

Arquivo: RM.Fop.Processos.Data.dll

## TOTVS Framework

### Rotina: ACTIONS DO SISTEMA FRW 00002

* **[Ticket: 577972 / MFRWBH-1344]** Foi realizada a migração dos registros, das tabelas antigas do Agilis para as novas de Globais.

Arquivos: RM.Lib.dll, RM.Lib.Server.dll, RM.Lib.WinForms.dll

### Rotina: PERT GANTT PRJ 33 862

* **[Ticket: 558129 / MCP-1964]** Lentidão na alteração do Pert

Arquivo: RM.Lib.WinForms.Gantt.dll

## TOTVS Gerador de saídas

### Rotina: LAYOUT DOCUMENTACAO GEN 02

* **[Ticket: 547092 / MFRWBH-1332]** Melhoria ao editar layouts específicos no Gerador de Saídas.

Arquivo: RM.Gen.Engine.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 574976 / MCP-2034]** Melhoria no envio de notas

Arquivos: RM.Mov.Movimento.Intf.dll, RM.Mov.Movimento.Form.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Movimento.Data.dll

* **[Ticket: 551254 / MCP-1975]** Melhoria na inclusão de movimentos com número de série.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: TAB AUX MOTIVO REFERENCIA AUX 014

* **[Ticket: 416578 / MCP-1901]** Inconsistência na geração da tag "<NFref>"

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS USUARIOS DO CURRICULO RHU 36 029

* **[Ticket: 409837 / MRH-7629]** Foi criado um parametro no RM que permite um usuário já cadastrado como funcionário ou ex-funcionario, quando for cadastrar um currículo, já venha preenchido os dados pessoais.

Arquivos: FrameHTML

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 503097 / MRH-6965]** Foi criado um parâmetro no RM que permite que o nome da pessoa seja cadastrado sem sobrenome.

Arquivos: RM.Rhu.Parametros.Intf.dll, RM.Rhu.Lib.WinForms.dll, RM.Rhu.Parametros.Form.dll

## TOTVS Gestão Financeira

### Rotina: Project-596743 FINANC - Valores errados no retorno bancário Project-596743

* **[Ticket: 602729 / FINANCEIRO01-79]** Otimização no processo de retorno de cobrança. Agora o sistema ajusta o cálculo da proporção de cada valor dos lançamentos que compõem o boleto corretamente.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS MUNICIPAIS LI 01 0034

* **[Ticket: 479182 / MEDU-2623]** Adequações realizadas no layout SIMPLISS de Piracicaba

Arquivo: RM.Fis.Sped.Server.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 475542 / MEDU-2983]** Alteração na criação dos registros D100, no que se diz na geração do 0200 quando o mesmo for referenciado em outro bloco.

Arquivo: RM.Fis.Sped.Server.dll

### Rotina: PERIODO

* **[Ticket: FISCAL01-48]** - Efetuada melhoria no processo de Fechamento/Abertura do período fiscal para que seu processamento interno ocorra mês a mês. Tal implementação impede que o log de transação do banco fique cheio a ponto de suspender a execução do processo.- Implementados os status "Aberto parcial" e "Fechado parcial". Um período fiscal ficará com status Aberto/Fechado parcial quando ocorrer problema durante o fechamento ou abertura dele e já tenha ocorrido o processamento de pelo menos um mês.- Efetuada melhoria nas rotinas fiscais EFD Contribuições, SPED Fiscal, ECF – Escrituração Contábil\Fiscal, TAF, DAPI, SINTEGRApara não serem geradas quando suas datas de geração estiverem compreendidas dentro de um período fiscal aberto/fechado parcial.

Arquivos: RM.Fis.Lib.dll, RM.Fis.PeriodoFiscal.Service.dll, RM.Fis.Utils.Server.dll, RM.Fis.PeriodoFiscal.Data.dll

## TOTVS Gestão Hospitalar

### Rotina: Paciente novo não aparece na tela de pesquisa

* **[Ticket: 600727 / MSAU-6236]** Ajuste realizado no formulário do Agenda de Atendimentos, para exibir os pacientes pesquisados independente da forma de como foram criados.

Arquivo: RM.Sau.Common.Data.dll

### Rotina: Período Especial - Agenda de Atendimento

* **[Ticket: 603195 / MSAU-6278]** Ajuste na listagem de períodos especiais da agenda

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

### Rotina: Teste de Aceitação (Homologação) - 12.1.10

* **[Ticket: SAUHRM01-711]** Ajuste na integração com o Sanemob

Arquivo: RM.Sau.Integracoes.Server.dll

## TOTVS Planejamento e Controle da Produção

### Rotina: BAIXA DE MATERIAIS PCP 44 285

* **[Ticket: 597287 / MCP-2029]** Melhoria na baixa para não considerar lote quando não foi controlado por lote.

Arquivo: RM.PCP.BaixaMateriais.Service.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: RELATORIOS PERFIL PROFISSIOGRAFICO PREVIDENCIARIO PPP SMT 36 578

* **[Ticket: 473844 / MRH-6897]** Realizado ajuste na geração do relatório PPP, no que tange a validação de lotação (seção e função).

Arquivo: RM.Smt.Relatorio.Data.dll

# 12.1.15.123

## TOTVS Automação de Ponto

### Rotina: CONFIGURACOES PARAMETRIZADOR INICIAIS PTO 35 1216

* **[Ticket: 608763 / MRH-8338]** Foram realizadas alterações no processo de lançamento global de abonos, para permitir que funcionários com data de admissão posterior a data de início definida no processo, possam ter abonos lançados nos dias válidos do intervalo.

Arquivo: RM.Pto.Ocorrencia.Data.dll

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 535444 / MRH-8192]** Realizado ajuste na rotina de importação de batidas quando a mesma vai processar itens de períodos futuros. Antes do ajuste estava ocorrendo erro de PK na AAFDTCRC

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: PORTAL WEB ESPELHO DO CARTAO PTO 35 1250

* **[Ticket: 437382 / MRH-6327]** Foram realizadas alterações na rotina que calcula o tempo mínimo de ausência para refeição, possibilitando a correção do espelho para estes tipos de ocorrência

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: RELATORIOS PORTARIA 1 510 2009 AFDT PTO 35 1271

* **[Ticket: 608852 / MRH-8347]** Realizada otimização no relatório AFDT da portaria 1510 para atender as regras do layout a respeito de batidas pré assinaladas e ordenação das batidas no arquivo.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Business Connect

### Rotina: REAJUSTE

* **[Ticket: TINPAD001-46]** Implementação de Controle de Renegociação de Títulos do Protheus (Aglutinação de Títulos Vencidos para Baixa)

Arquivo: RM.Con.ConfiguraIntegracao.TotvsIncorporacaoProtheus.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS MEDICAO PRJ 33 941

* **[Ticket: 478006 / MCP-1935]** Verificado o saldo do Adiantamento de contratos, nos período em que foram cometidos os abatimentos das deduções do tipo adiantamento.

Arquivo: RM.Prj.PedidoMaterial.Form.dll

### Rotina: PARAMETROS GERAIS PRJ 33 858

* **[Ticket: 484061 / MCP-2045]** Email de aprovação de pedido extra sendo enviado, o remetente do email não está respeitando as configurações de globais

Arquivo: RM.Prj.PedidoMaterial.Server.dll

## TOTVS Educacional

### Rotina: BOOK DE RELATORIOS EDU 50 088

* **[Ticket: 486349 / MEDU-2858]** Ajuste no provider de dados do histórico de ensino médio, garantindo a ordenação das disciplinas por parte do histórico.

Arquivo: RM.Edu.Lib.Server.dll

* **[Ticket: 486363 / MEDU-2648]** Ajuste no relatório do Histórico Escolar do Ensino Médio (EDUREL0002) para que seja montado de forma correta o campo Parte do Histórico.

Arquivo: RM.Edu.Lib.Server.dll

### Rotina: Definição de bolsistas sem apontar a pessoa do bolsista para os projetos de Pesquisa e Extensão

* **[Ticket: EDUEDU004-59]** Ajustes nos fluxos de Pesquisa e Extensão

Arquivos: RM.Edu.Aluno.Data.dll, RM.Edu.MatrizCurricular.Data.dll

## TOTVS Folha de Pagamento

### Rotina: FERIAS CADASTRO FOP 34 538

* **[Ticket: 590004 / MRH-8137]** Ajuste de permissão na execução do recalculo de férias via tela de recibo de férias

Arquivo: RM.Fop.FuFerias.Form.dll

### Rotina: PARAMETROS LOCAIS LAB 01 31

* **[Ticket: 597706 / MRH-8274]** Melhoria na opção 'Cadastro automático de chapas seqüenciais (Exclusivamente numéricas, onde o valor da chapa seja menor que 2147483647)' para apresentar a mensagem 'Valor da chapa cadastrada é superior a 2147483647.' quando o valor da chapa for superior a 2147483647.

Arquivos: RM.Fop.Parametros.Data.dll, RM.Fop.Parametros.Form.dll

### Rotina: RAIS LAB 01 12

* **[Ticket: 597290 / MRH-8390]** Ajuste em rotina RAIS para não processar Aposentado por invalidez em ano anterior ao ano base.

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 607699 / FOPROTINAS01-311]** Ajustado o processo da RAIS, para ser verificado se o funcionário está aposentado quando a situação do funcionário for igual a demitido e a data de projeção for maior que a data limite da RAIS.

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 602134 / MRH-8414]** Realizado ajuste na RAIS realizando validação com data de desligamento, para o casos de: funcionário tem folha para cálculo de aviso lançado para o próximo mês. Desta forma o aviso foi lançado no mês anterior à rescisão.

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 612758 / FOPROTINAS01-310]** Ajuste no processo de geração da RAIS, para levar o código do desligamento igual a 20 quando o tipo de rescisão for Rescisão Indireta.

Arquivo: RM.Fop.Dominio.dll

### Rotina: RESCISAO HOMOLOGNET LAB 01 219

* **[Ticket: 119509 / MRH-3435]** Otimizado geração do homolognet para que a base de insalubridade seja enviada com base no valor fixo de salário mínimo

Arquivos: RM.Fop.Utils.Server.dll, RM.Fop.Processos.Data.dll

## TOTVS Framework

### Rotina: ACTIONS DO SISTEMA FRW 00002

* **[Ticket: 316284 / MEDU-3077]** A criação de fluxo de trabalho automatico foi otimizada.

Arquivo: RM.Lib.Server.dll

### Rotina: FORMULA VISUAL FVS 01

* **[Ticket: 468811 / MFRWBH-1166]** Criado um novo tipo de gatilho denominado "Ativado Parando Execução em Caso de Exceções". Ao selecionar esse tipo, caso ocorra erro na fórmula em questão, as demais não serão executadas.

Arquivos: RM.Lib.dll, RM.Glb.Workflow.Form.dll, RM.Glb.Workflow.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CUPOM FISCAL COM 022

* **[Ticket: 604746 / MCP-2051]** Melhoria no processo de calculo da Redução Z para permitir selecionar vários registros.

Arquivo: RM.Mov.CupomFiscal.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: FUNCIONARIOS RHU 36 035

* **[Ticket: 408763 / MRH-5662]** Ajuste nas tags de menu do lançamento de benefícios

Arquivos: RM.Rhu.Beneficios.Data.dll, RM.Rhu.Beneficios.Form.dll

### Rotina: RECLASSIFICAR

* **[Ticket: MRH-1335]** Ajustado o parametros para quando a unicidade for por 'Nome, Dt. Nascimento, Estado natal e Cidade natal' sempre tornar os campos obrigatórios, independente de ser um registro novo ou antigo.

Arquivo: RM.Rhu.Lib.WinForms.dll

### Rotina: REQUISICOES GERAL RHU 36 508

* **[Ticket: 584493 / MRH-8193]** Ajuste ao salvar um anexo

Arquivo: RM.Rhu.Requisicao.Intf.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA ENCERRAMENTO DE PERIODO FIN 010

* **[Ticket: 519984 / MEDU-2699]** Melhoria em Conversor de Aplicação Financeira

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

### Rotina: CARTAO DE CREDITO TRANSACOES FIN 068

* **[Ticket: 587109 / MEDU-2945]** Feito tratamento para evitar duplicidade no pagamento de cartão de crédito através do portal do aluno.

Arquivos: RM.Fin.Lan.Service.dll, App\_Web\_finlancartaopagamentocielo2uc.ascx.51ca41ad.dll

### Rotina: SERVICO DE CONTABILIZACAO FIN 323

* **[Ticket: 597858 / MEDU-2988]** Ajuste no serviço de contabilização de inclusão de lançamento, relacionado ao default contabil de bolsa quando o lançamento não possui bolsa.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS MUNICIPAIS LI 01 0034

* **[Ticket: 99892 / FISCAL01-7]** Foi realizada a implementação do processo de envio/cancelamento das Notas Fiscais Recebidas de Salvador (NFTS).

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.Data.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.IService.dll

### Rotina: OBRIGACOES PRINCIPAIS APURACAO ICMS

* **[Ticket: FISCAL01-73]** Implementada melhoria na escrituração para que os campos "TIPORENDIMENTO" e "FORMATRIBUTACAO" recebam seus valorespadrão quando seus campos equivalentes no movimento não estiverem preenchidos.

Arquivo: RM.Fis.EscrituracaoFiscal.Service.dll

### Rotina: PERIODO

* **[Ticket: FISCAL01-48]** Implementada melhoria no log do processo de fechamento/abertura de período fiscal.

Arquivos: RM.Fis.PeriodoFiscal.IService.dll, RM.Fis.PeriodoFiscal.Service.dll, RM.Fis.PeriodoFiscal.Data.dll

## TOTVS Gestão Hospitalar

### Rotina: APURACAO E LANCAMENTO DE REPASSES SAU 47 1166

* **[Ticket: 529299 / MSAU-5712]** Realizado ajuste para buscar a especialidade correta de acordo com o procedimento lançado na AIH.

Arquivos: RM.Sau.Sus.Intf.dll, RM.Sau.Sus.Data.dll, RM.Sau.Sus.Form.dll, RM.Sau.Sus.Server.dll

### Rotina: MOVIMENTACOES DE ESTOQUE SAU 47 1126

* **[Ticket: 553478 / MSAU-6211]** Ajuste na devolução de itens grátis.

Arquivo: RM.Sau.Produto.Server.dll

### Rotina: o nome do paciente não esta aparecendo na agenda de cirurgia

* **[Ticket: 568588 / MSAU-6121]** Ajuste realizado para que o sistema traga o primeiro nome não nulo da condição, o que fazia anteriormente e parou de fazer.

Arquivo: RM.Sau.AgendaCirurgia.Data.dll

### Rotina: OUTROS PROCESSOS SAU 47 1173

* **[Ticket: 576692 / MSAU-6198]** Realizado ajuste no arquivo de exportação da DMED para que o campo valor pago apareça nulo para os responsáveis pelo atendimento que não tiveram atendimento no ano.

Arquivo: RM.Sau.Faturamento.Data.dll

### Rotina: PEP PRESCRICAO MEDICA SAU 47 1121

* **[Ticket: 612238 / MSAU-6372]** Ajuste para que o sistema também espere uma classificação vazia do PEP 2.0

Arquivo: RM.Sau.PepHis.Server.dll

### Rotina: REGISTRO DE ATENDIMENTO EXTERNO SAU 47 1141

* **[Ticket: 513424 / MSAU-6106]** Ao realizar a verificação de elegibilidade das telas de registro de internação e registro de atendimento externo o sistema não exibe a mensagem de retorno do convênio somente a mensagem da tabela da ANS. Alterado o sistema para exibir tanto a descrição do erro na tabela da ans quanto o retorno do convênio ao solicitar a elegibilidade.

Arquivos: RM.Sau.AgendaAtendimento.Data.dll, RM.Sau.Ans.Sever.dll

## TOTVS Incorporação

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 532813 / MCP-2044]** Alterada a rotina que reajusta a baixa parcial para que não mas retroceda um mês em parcelas no momento após para componetes de juros que incidam sobre correção antes da entrega.

Arquivo: RM.Imb.Reajuste.Server.dll

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhorias Ficha Financeira, apenas para projeto de revitalização.

Arquivos: RM.Imb.Relatorio.Data.dll, RM.Fin.HistoricoLan.Service.dll, RM.Imb.Parametros.Data.dll

# 12.1.15.124

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB ABONAR ANTES DA COMPENSACAO PTO 35 1258

* **[Ticket: 520995 / MRH-7380]** Foram realizadas alterações no processamento da visão da tela de "abonos antes da compensação" para que o processo fosse realizado com sucesso.

Arquivo: RM.Pto.Ocorrencia.Data.dll

### Rotina: PORTAL WEB APROVAR HORAS EXTRAS PTO 35 1260

* **[Ticket: 607851 / MRH-8378]** Foram feitas alterações no sistema em relação a validação da data de referência da ocorrência.

Arquivo: RM.Pto.AprovaHorasExtras.Data.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** SGBD: SQL SERVER / ORACLEScript: /\*GUILHERME COUTO ROCHA - CN.2016.11\_13 - OC.:EDUEDU001-1096 - 22/12/2016 VERSAO.: 12.1.15 - EQUIPE:INOV \*/ /\*GUILHERME COUTO ROCHA - CN.2016.12\_08 - OC.:EDUEDU001-1200 - 03/01/2017 VERSAO.: 12.1.15 - EQUIPE:INOV \*/ ISSUE: 07\EXCEÇÃODescrição: Remoção dos comandos de Criação e Exclusão das constraints FKSPSLOGINSCRICAOPS\_PPESSOA e FKSPSLOGINSCRICAOPS\_SPSUSUARIO.

Arquivo: Cvn.12.1.15.sql

## TOTVS Educacional

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 577902 / MEDU-3004]** Foi realizada otimização do processo de geração de movimento por competência, permitindo ao sistema, calcular o valor de descontos para contratos que possuam apenas descontos concedidos nas suas parcelas e não possuam bolsas.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: GERACAO DO HISTORICO EDU 50 233

* **[Ticket: 508414 / MEDU-2714]** Ajuste na formatação do campo carga horária da disciplina do histórico, podendo ser informado decimal (hora/aula) e string (hora relógio).

Arquivo: RM.Edu.Historico.Data.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 583658 / MEDU-3031]** Foi alterada a mensagem gerada na importação de dados do censo, pois não está sendo possível identificar os alunos que não estão sendo encontrados no sistema. O INEP não está enviando mais o RA no arquivo. Será utilizado o CPF para a verificação.

Arquivo: RM.Edu.Academico.Server.dll

## TOTVS Folha de Pagamento

### Rotina: CONSULTA MOVIMENTO DA INTEGRACAO LAB 01 96

* **[Ticket: 562111 / MRH-8501]** Habilitado o menu de Integração SAP para o cliente GRAVIA

Arquivos: RM.Fop.Lib.Extensions.dll, RM.Fop.Utils.Intf.dll, RM.Fop.Utils.Server.dll, RM.Fop.Server.dll, RM.FopFolha.dll, RM.Fop.Parametros.Form.dll

### Rotina: PORTAL WEB ALTERAR EQUIPE LAB 01 195

* **[Ticket: 521285 / FOPROTINAS01-208]** Ajuste na tela de parâmetros do RH Portal para clientes com customização

Arquivo: RM.Fop.Paramquiosque.Data.dll

## TOTVS Gestão Contábil

### Rotina: CADASTROS PLANO DE CONTAS CONTABIL CTB 38 78

* **[Ticket: 393105 / MEDU-2840]** Melhoria no processo de cadastro de Código Reduzido de Contas Contábil/Gerencial para que o usuário tenha a opção parametrizável de gerar o código sequencialmente preenchendo ou não as lacunas que ficam após a exclusão de alguma conta.

Arquivos: RM.Ctb.Parametros.Intf.dll, RM.Ctb.Contas.Form.dll, RM.Ctb.Parametros.Form.dll, RM.Ctb.Utils.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 534543 / MCP-2010]** Melhoria para não consultar a TLOTEPRDLOC quando for movimento de entrada.

Arquivo: RM.Mov.Movimento.Form.dll

## TOTVS Gestão Fiscal

### Rotina: ACTIONS DO SISTEMA FRW 00002

* **[Ticket: 316284 / MEDU-3077]** Alteração no cadastro de guia de periodo normal do ICMS.

Arquivo: RM.Fis.ApuracaoTrb.Data.dll

### Rotina: ESCRITURACAO LI 01 0025

* **[Ticket: 493710 / MEDU-3073]** - Ajuste no cálculo do lançamento fiscal para considerar corretamente o parâmetro "ICMS ST Não considera ICMS Próprio" da regra de ICMS.- No lançamento fiscal o campo "ICMS Proprío" da pasta "Substituição Tributária" não será visivel se o campo "ICMS ST Não considera ICMS Próprio" da regra de ICMS estiver marcado.

Arquivos: RM.Fis.LancFiscal.Form.dll, RM.Fis.LancFiscal.Service.dll

### Rotina: NF E CONSULTAR EVENTOS NF 01 0016

* **[Ticket: 582188 / MEDU-3051]** Alteração no processo de configuração do TSS no envio da NF-e.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: OBRIGACOES PRINCIPAIS ENTRADA SAIDA LI 01 0046

* **[Ticket: 387321 / MEDU-2238]** Efetuada melhoria para que o valor do ICMS Próprio seja calculado corretamente quando a opção ICMS ST considera redução no cálculo do ICMS próprio estiver marcada no CFOP.

Arquivos: RM.Fis.LancFiscal.Intf.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.Utils.Intf.dll

## TOTVS Gestão Hospitalar

### Rotina: Teste de Aceitação (Homologação) - 12.1.10

* **[Ticket: SAUHRM01-711]** Ajuste na integração com o SaneMob

Arquivo: RM.Sau.Integracoes.Server.dll

### Rotina: XML com valores de consultas zerados - HOSPITAL SANTA ROSA

* **[Ticket: 621241 / MSAU-6455]** Ajuste para correta precificação dos itens no XML de faturamento

Arquivos: RM.Sau.Ans.Sever.dll, RM.Sau.Utils.Intf.dll

## TOTVS Incorporação

### Rotina: ADITIVO ANTECIPACAO DE PARCELA IMB 49 781

* **[Ticket: 563672 / MCP-1985]** Incidente: Ao criar um aditivo de antecipação de parcelas, uma parcela estava ficando com diferença de um centavoSolução:Foi verificado que a diferença ocorria pelo fato de o cálculo do desconto pela antecipação estar sendo feito com mais de duas casas decimais, isso gerou a diferença ao realizar arredondamento no cálculo. O aditivo foi modificado para realizar o cálculo somente com duas casas decimais.

Arquivos: RM.Imb.Aditivos.IServer.dll, RM.Imb.Aditivos.Data.dll, RM.Imb.Aditivos.Server.dll

### Rotina: ADITIVO DIA DE VENCIMENTO DO CONTRATO IMB 49 794

* **[Ticket: 607868 / MCP-2071]** Voltando versão dos arquivos de Design da Tela de Aditivos de Renegociação com as barras de rolagem disponíveis

Arquivo: RM.Imb.Aditivos.Form.dll

### Rotina: aviso sistema

* **[Ticket: 544470 / TINPAD001-34]** Incidente: Ao editar um componente principal PRICE de uma venda o sistema estava apresentando uma mensagem dizendo que não era possível concluir a edição pois já havia um componente de juros inserido.Solução:Esta validação foi modificada para ocorrer somente na inclusão de um novo componente, pois na modalidade PRICE o componente de juros depende do componente principal, sendo assim, é necessário que seja o último componente a ser adicionado.

Arquivo: RM.Imb.Venda.Regra.Data.dll

# 12.1.15.125

## TOTVS Automação de Ponto

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 544041 / MRH-8341]** Foram realizadas alterações no processo de formatação das horas extras do relatório do cartão de ponto, com o objetivo de apresentar de forma correta os dados.

Arquivo: RM.Pto.Relatorio.Data.dll

### Rotina: RELATORIOS PORTARIA 1 510 2009 AFDT PTO 35 1271

* **[Ticket: 626473 / MRH-8566]** Otimizado a emissão do relatório AFDT para evitar erro de coluna nula no dataTable que é trabalhado para gerar as informações do relatório.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** SGBD: SQL SERVER / ORACLEScript: /\*ALLYSSON MEZENCIO DOS SANTOS - CN1200\_129 - OC.:THQ100 - 17/12/2013 \*/ISSUE: MGCADBH-24Descrição: Validação de duplicidade de registros.

Arquivo: RMCMelhoria\_1100e8354.sql

* **[Ticket: Alterações Gerais]** SGBD: SQL SERVER / ORACLEScript: /\*JEFFERSON DUARTE RODRIGUES - VI.2016.10\_02 - OC.:TVNPRS - 11/11/2016 VERSAO.: 12.1.14 - EQUIPE:MANUT \*/ISSUE: MGCADBH-121Descrição: Validação de duplicidade de registros.

Arquivo: Cvn.12.1.15.sql

* **[Ticket: Alterações Gerais]** SGBD: ORACLEScript: /\*DARLAN ALVYSSON ALVES - CN.2016.11\_03 - OC.:TWCV49 - 11/11/2016 VERSAO.: 12.1.15 - EQUIPE:MANUT \*/ISSUE: MGCADBH-129Descrição: Validação de duplicidade de registros.

Arquivo: Cvn.12.1.15.sql

## TOTVS Business Connect

### Rotina: REAJUSTE

* **[Ticket: TINPAD001-46]** Implementação de Cálculo de Desconto no Reajuste quando ocorre antecipação de Parcelas de Modelo PRICE

Arquivo: RM.Con.ConfiguraIntegracao.TotvsIncorporacaoProtheus.dll

### Rotina: WEBSERVICE EDU 50 493

* **[Ticket: 485350 / MFRWBH-1355]** Melhoria na geração de log de processos através do WSProcess

Arquivo: RM.Con.TotvsMessage.Server.dll

## TOTVS Construção e Projetos

### Rotina: COPIA DE ITENS PRJ 33 779

* **[Ticket: 615876 / MCP-2085]** Disponibilizar na cópia de itens, a opção de de copiar entre os projetos as equipes de TimeSheet

Arquivos: RM.Prj.Projeto.Intf.dll, RM.Prj.Projeto.Data.dll, RM.Prj.Projeto.Form.dll

### Rotina: TIMESHEET EQUIPE DE TIMESHEET PRJ 33 798

* **[Ticket: 599501 / MCP-2074]** Permitir em equipes de TimeSheet , informem um funcionário (membro) em uma ou mais equipe

Arquivo: RM.Prj.EquipeProjeto.Data.dll

## TOTVS Educacional

### Rotina: CENSO

* **[Ticket: EDUCACIONAL01-134]** Foi incluído uma mensagem informando que não há dados.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: Erro processo "mudar turma"

* **[Ticket: 585529 / MEDU-2941]** Otimizado processo de Mudança de Turma, quando o aluno está matriculado no período letivo utilizando Currículo Individual do Aluno.

Arquivo: RM.Edu.Matricula.Data.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 593709 / MEDU-3028]** Correção para permitir editar o Curso do MEC de dentro da pesquisa na tela de Matriz Aplicada.

Arquivo: RM.Edu.MatrizCurricular.Data.dll

## TOTVS Folha de Pagamento

### Rotina: DECIMO TERCEIRO SALARIO DIFERENCA FOP 34 516

* **[Ticket: 549818 / MRH-8063]** Ajuste no cálculo da diferença de 13º em janeiro para guardar na pasta "Verbas geradas por Diferença" da ficha financeira, os valores originais de media de 13º Salário.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: IMPORTACAO DE DADOS DO RM LABORE LAB 01 26

* **[Ticket: 598914 / MRH-8422]** Otimizado importação de dados do Labore para emitir erro em linhas inválidas e processar as linhas corretas

Arquivo: RM.Fop.Importacao.Data.dll

### Rotina: importação de dados no RM Labore

* **[Ticket: 566980 / MRH-8576]** Otimizado importação de dados do Labore

Arquivo: RM.Fop.Importacao.Data.dll

### Rotina: RESCISAO CADASTRO DE RESCISAO FOP 34 400

* **[Ticket: 533101 / FOPROTINAS01-238]** Ajuste nos parâmetros de rescisão para que sejam informadas chapa e coligada em leitura via fórmula visual.

Arquivos: RM.Fop.Rescisao.Intf.dll, RM.Fop.Rescisao.Form.dll

## TOTVS Framework

* **[Ticket: Alterações Gerais]** 07\exceção

Arquivos: RM.Lib.dll, RM.exe

### Rotina: PERMISSÕES DE ACESSO FRW00058

* **[Ticket: MFRWBH-1380]** Quando o sistema estiver integrado com o Identity será exibido os itens de menu de módulos que possuem tagmenu < 800000000

Arquivo: RM.MDI.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: EFEITO ORCAMENTO MOVIMENTOS ORC 012

* **[Ticket: 533734 / MCP-2043]** Melhoria no cancelamento de movimentos.

Arquivos: RM.Ctr.Contrato.IService.dll, RM.Mov.Movimento.Service.dll, RM.Ctr.Contrato.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: RELATORIOS RELATORIOS DE SEGURANCA SMT 36 043

* **[Ticket: 525657 / RHU01-234]** Realizado ajuste na geração do relatório PPRA de forma a corrigir a ordenação do relatório que não era respeitada quando um dos ítens do mesmo gerava mais de 9 páginas.

Arquivo: RM.Smt.Relatorio.Form.dll

### Rotina: REQUISICOES AUMENTO DE QUADRO RHU 36 095

* **[Ticket: 191142 / MRH-5734]** Realizado ajuste na busca de candidatos na tela de pré-cadastro de Funcionário.

Arquivo: RM.Rhu.Pessoa.Data.dll

### Rotina: SELECAO PAINEL DE SELECAO RHU 36 100

* **[Ticket: 420219 / MRH-7060]** Ajustado consulta sql que estava gerando o erro.

Arquivo: RM.Rhu.Captacao.Data.dll

## TOTVS Gestão Financeira

### Rotina: Project-596743 FINANC - Valores errados no retorno bancário Project-596743

* **[Ticket: 602729 / FINANCEIRO01-79]** Otimização no processo de retorno de cobrança. Agora o sistema ajusta o cálculo da proporção de cada valor dos lançamentos que compõem o boleto corretamente.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: ACTIONS DO SISTEMA FRW 00002

* **[Ticket: 316284 / MEDU-3077]** Alteração no cadastro de guia de periodo normal do ICMS.

Arquivo: RM.Fis.ApuracaoTrb.Data.dll

### Rotina: NFS-E ATUALIZAÇÃO DE MUNICÍPIOS HOMOLOGADOS NF010023

* **[Ticket: 95457 / MEDU-222]** Implementação do municipio Taubaté-SP para emissão de nfs-e via Webservice

Arquivo: RM.Fis.RotinasFiscais.Data.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 602913 / MEDU-3072]** Realizado tratativa no select que realiza a carga de dados para geração do SPED Fiscal.

Arquivo: RM.Fis.Sped.Server.dll

### Rotina: ROTINAS LEGAIS

* **[Ticket: FISCAL01-22]** Foram realizadas as alterações referente ao Layout da Rotina ICMS 115/03 que passou a vigorar a partir de 01/01/2017.

Arquivos: RM.Fin.CliFor.Data.dll, RM.Fin.CliFor.Intf.dll, RM.Fin.CliFor.Service.dll, RM.Fis.LancFiscal.Intf.dll, RM.Fis.LancFiscal.Service.dll, RM.Fin.CliFor.Form.dll, RM.Fis.LancFiscal.Data.dll, RM.Fis.LancFiscal.Form.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Exportacao.Service.dll, RM.Fis.Lib.dll, RM.Fin.CliFor.IService.dll, RM.Fis.LancFiscal.IService.dll

## TOTVS Gestão Hospitalar

### Rotina: AGENDAMENTO SAU 47 1135

* **[Ticket: 609481 / MSAU-6335]** Ajuste para não ocorrer a deleção do agendamento cancelado

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: Erro ao solicitar exames no prontuário

* **[Ticket: 620467 / MSAU-6481]** Ajuste na inserção do exame quando integrado com a shift.

Arquivo: RM.Sau.Integracoes.Server.dll

### Rotina: INTEGRACAO NUCLEUS FATURAMENTO SAU 47 1130

* **[Ticket: 624666 / MSAU-6496]** Ajuste para o correto recebimento do código do procedimento durante a integração com SaneMob

Arquivo: RM.Sau.Integracoes.Server.dll

### Rotina: OUTROS PROCESSOS SAU 47 1173

* **[Ticket: 594527 / MSAU-6310]** Criado parâmetro na tela de geração da DMED para que o usuário tenha a opção de gerar o arquivo com a informação de todas as unidades de faturamento.

Arquivos: RM.Sau.Faturamento.Intf.dll, RM.Sau.Faturamento.Data.dll, RM.Sau.Faturamento.Form.dll

### Rotina: Utilização do Painel de Chamadas - Sem TRIAGEM

* **[Ticket: 611208 / MSAU-6392]** Ajuste para a correta geração de senha de com duas unidades distintas e sem a utilização do filtro por especialidade.

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: OPERACOES PATRIMONIAIS TRANSFERENCIA MONETARIA PAT 37 47

* **[Ticket: 601892 / MEDU-3044]** Atualização no processo de verificação de ocorrências no período

Arquivo: RM.Pat.Ocorrencia.Service.dll

* **[Ticket: 601892 / MEDU-3044]** Verificar se o tipo do ownerData ao processar a exclusão da ocorrência

Arquivo: RM.Pat.Ocorrencia.Service.dll

## TOTVS Incorporação

### Rotina: ADITIVO ALTERACAO DAS TAXAS DE REAJUSTE IMB 49 791

* **[Ticket: 551575 / MCP-2094]** Removida a obrigatoriedade de histórico de reajuste para determinar o próximo identificador do histório do reajuste no momento da efetivação do aditivo.

Arquivo: RM.Imb.Aluguel.ContratoLoc.Server.dll

### Rotina: ADITIVO RENEGOCIACAO DE CONTRATO IMB 49 784

* **[Ticket: 405660 / MCP-2109]** Removido código que copiava o número do contrato para a coluna FORMULACODIGO

Arquivo: RM.Imb.Aditivos.Form.dll

### Rotina: Minha casa minha vida

* **[Ticket: 608711 / TINPAD001-36]** Alterado na máquina de cálculo para não carregar parcelas canceladas no cálculo de componentes MCMV.

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

### Rotina: REAJUSTE

* **[Ticket: TINPAD001-46]** Implementação de Cálculo de Desconto no Reajuste quando ocorre antecipação de Parcelas de Modelo PRICE

Arquivo: RM.Imb.Reajuste.Server.dll

* **[Ticket: TINPAD001-46]** Implementação de Cálculo de Desconto no Reajuste quando ocorre antecipação de Parcelas de Modelo PRICE

Arquivos: RM.Imb.Reajuste.Server.dll, RM.Imb.Reajuste.Data.dll, RM.Imb.Reajuste.IServer.dll, RM.Imb.Reajuste.Intf.dll

# 12.1.15.126

## TOTVS Automação de Ponto

### Rotina: HORARIOS PTO 35 1180

* **[Ticket: 627024 / MRH-8656]** Alterações no processo de atualização de histórico de horários para permitir que a exibição dos dados do funcionário, em relação ao código de horário, seja apresentada de maneira correta.

Arquivo: RM.Pto.Horario.Data.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** SGBD: SQL SERVER / ORACLEScript: /\*PAULO HENRIQUE VIEIRA NEVES - CP.2016.12\_12 - OC.:FRW\_FRW002-216 - 03/01/2017 VERSAO.: 12.1.15 - EQUIPE:INOV \*/ISSUE: MFRWBH-1386Descrição: Alteração do Default da coluna HABILITARANALISEPREDITIVA de 1 para 0

Arquivo: Cvn.12.1.15.sql

## TOTVS Educacional

### Rotina: RELATORIO

* **[Ticket: EDUCACIONAL01-44]** Implementação de mensagens de alerta para o usuário quanto à tabela master dos relatórios de boletos.

Arquivos: RM.Edu.Lib.WinForms.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Consts.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Utils.Server.dll, RM.Edu.dll

## TOTVS Framework

### Rotina: Ao utilizar os botões de navegação na tela de detalhamento do Job as informações de avisos não são atualizadas

* **[Ticket: 486743 / MFRWBH-1381]** A tela de exibição de Job´s foi otimizada.

Arquivo: RM.Lib.WinForms.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES PRINCIPAIS APURACAO ICMS

* **[Ticket: FISCAL01-73]** Efetuada melhoria no recálculo do lançamento fiscal para que o valor do IPI Tributado seja calculado corretamente.

Arquivo: RM.Fis.LancFiscal.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: AGENDAMENTO SAU 47 1135

* **[Ticket: 584463 / MSAU-6096]** Ajuste para que o sistema não gere erro ao solicitar procedimento pela agenda de atendimentos.

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

## TOTVS Gestão Patrimonial

### Rotina: OPCOES PARAMETROS RM BONUM PAT 37 60

* **[Ticket: 505961 / MEDU-2768]** Atualização na validação da parametrização ref. validação da quantidade de zeros à esquerda para uma base ainda sem patrimônios.

Arquivos: RM.Pat.Parametros.Data.dll, RM.Pat.Parametros.Form.dll

## TOTVS Incorporação

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhoria no conversor da revitalização.

Arquivos: RM.Imb.Conversor.Data.dll, RM.Imb.Conversor.Server.dll

# 12.1.15.127

## TOTVS Automação de Ponto

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 416123 / MRH-8247]** Realizada otimização de performance na emissão do relatório de espelho do cartão.

Arquivos: RM.Pto.Horario.Intf.dll, RM.Pto.Horario.Data.dll, RM.Pto.Relatorio.Data.dll

## TOTVS Educacional

### Rotina: FOLHA DE PAGAMENTO PROFESSOR EDU 50 217

* **[Ticket: 575931 / MEDU-2905]** Foi realizada otimização do processo de geração de lançamentos, permitindo ao sistema, gerar lançamentos para parcelas de contratos sem vínculo com uma matriz aplicada.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: GERACAO DO HISTORICO EDU 50 233

* **[Ticket: 623607 / MEDU-3180]** Ajuste na formatação do campo carga horária da disciplina do histórico, podendo ser informado decimal (hora/aula) e string (hora relógio).

Arquivo: RM.Edu.Historico.Data.dll

### Rotina: INTEGRACAO FLUIG

* **[Ticket: EDUCACIONAL01-295]** Melhoria na integração entre TOTVS Educacional e Fluig LMS

Arquivos: RM.Edu.Server.dll, RM.Edu.dll, RM.Edu.Integracoes.Form.dll, RM.Edu.Matricula.Server.dll, RM.Edu.Facade.dll, RM.Edu.Integracoes.Intf.dll, RM.Edu.Integracoes.Server.dll, RM.Edu.MatrizCurricular.Form.dll, RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.Professor.Data.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.PeriodoLetivo.Data.dll, RM.Edu.Aluno.Data.dll, RM.Edu.Matricula.Data.dll, RM.Edu.ConfiguraIntegracao.TotvsLMSFluig.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.MatrizCurricular.Intf.dll

* **[Ticket: EDUCACIONAL01-295]** Melhoria na integração entre TOTVS Educacional e Fluig LMS

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsLMSFluig.dll

### Rotina: Piloto Cetec

* **[Ticket: 617739 / EDUCTB001-538]** Ajuste no envio de dados de acordo na integração Educacional x Backoffice Protheus

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Fin.Facade.Intf.dll, RM.Fin.Lan.Service.dll, RM.Edu.Financeiro.Server.dll

* **[Ticket: 580554 / EDUCTB001-538]** Ajuste na validação de fornecedor associado ao cliente no processo de zerar conta corrente do aluno.

Arquivo: RM.Edu.Financeiro.Data.dll

## TOTVS Folha de Pagamento

### Rotina: HOMOLOGNET

* **[Ticket: 353156 / FOPCALCULO01-81]** Ajuste no processo do homolognet para concaterar os campos "Tipo Logradouro" com "Logradouro" no cadastro da Seção e do Funcionário.

Arquivo: RM.Fop.Processos.Data.dll

### Rotina: MANAD LAB 01 122

* **[Ticket: 629632 / FOPROTINAS01-381]** Ajuste na rotina de geração MANAD para gerar registro de autônomo com valor zerado nos meses relativos ao intervalo passado quando existir pelo menos lançamento de preferência com valores em filiais distintas.

Arquivo: RM.Fop.Manad.Data.dll

### Rotina: PORTAL WEB ENVELOPE PGTO LAB 01 206

* **[Ticket: 637207 / MRH-8683]** Ajuste na permissão de visualização de envelope no portal

Arquivo: RM.Fop.Envelope.Data.dll

## TOTVS Framework

### Rotina: GERACAO DE RELATORIO RPT 00005

* **[Ticket: 607901 / MFRWBH-1362]** Melhoria para ambientes com UpdateServer ativo

Arquivo: RM.Lib.Server.dll

### Rotina: PAINEL DE METAS PERFIS ASSOCIADOS BIS 00044

* **[Ticket: 593250 / MFRWBH-1378]** Melhoria para que somente usuários vinculados ao peril associado ao painel de metas possam visualizar o mesmo.

Arquivos: RM.Glb.BalancedScorecard.Intf.dll, RM.Glb.BalancedScorecard.Data.dll, RM.Glb.BalancedScorecard.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: IMPRIMIR MOVIMENTO MOV 023

* **[Ticket: 526718 / MCP-1938]** Melhoria na impressão de movimento

Arquivo: RM.Mov.Processos.Form.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 574976 / MCP-2123]** Melhoria no processo de preenchimento do campo código serviço.

Arquivos: RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS USUARIOS DO CURRICULO RHU 36 029

* **[Ticket: 621182 / MRH-8499]** O problema estava sendo gerado por causa das aspas duplas " colocadas na descrição da vaga, e gerava erro no html. Assim foi feito uma tratativa que converte a aspas dupla " em aspas simples ' para que seja mostrado na tela do Portal de Talentos.

Arquivo: RM.Rhu.Curriculo.Server.dll

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 636166 / MRH-8684]** Ajuste ao inserir comentario em avaliação

Arquivos: Portal Corpore.Net

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO VINCULAR LANCAMENTOS FIN 214

* **[Ticket: 527525 / MEDU-3033]** Ajustes no serviço de conversão de vinculos referentes a refatoração dos vinculos.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: Piloto Cetec

* **[Ticket: 580554 / EDUCTB001-538]** Ajuste na validação de fornecedor associado ao cliente no processo de zerar conta corrente do aluno.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Chamado 113105, Solicitação / Cancelamento de Guia

* **[Ticket: 558164 / MSAU-6368]** Ao efetuar o cancelamento de guias do tipo resumo de internação quando existe integração por web service o sistema não estava considerando a versão de transição. Alterado o sistema para quando for efetuado o cancelamento de guia com integração por web service considerar a versão de transição quando esta estiver selecionada.

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Incorporação

### Rotina: REAJUSTE

* **[Ticket: MCP-2120]** Melhoria no reajuste para verificar o parâmetro se considera o juros antes para o calculo do juros apos

Arquivo: RM.Imb.Reajuste.Server.dll

### Rotina: Teste Sistêmico 12.1.16

* **[Ticket: CPTIN001-840]** Melhoria no aditivo de renegociação para permitir data de vencimento anterior a data do aditivo

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll

## TOTVS Processo Seletivo

### Rotina: CADASTRO

* **[Ticket: MEDU-3170]** Ajuste na tela inicial do processo seletivo.

Arquivo: App\_Web\_edupsprocessosseletivos.ascx.131e2aa5.dll

# 12.1.15.128

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB ABONAR ANTES DA COMPENSACAO PTO 35 1258

* **[Ticket: 520995 / MRH-7380]** Foram realizadas alterações no processamento da visão da tela de "abonos antes da compensação" para que o processo fosse realizado com sucesso.

Arquivo: App\_Web\_ptocodabono.ascx.7d151a08.dll

### Rotina: RELATORIOS PORTARIA 1 510 2009 AFDT PTO 35 1271

* **[Ticket: 591528 / MRH-8230]** Ajuste na emissão do relatório ACJEF para não incluir funcionários demitidos em períodos anteriores aos da geração do relatório.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Business Connect

### Rotina: REAJUSTE

* **[Ticket: TINPAD001-46]** Ajuste no Source Code para suportar motivo de baixa vazio

Arquivo: RM.Con.ConfiguraIntegracao.TotvsIncorporacaoProtheus.dll

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: MFRWBH-1418]** Ao executar o wsdataserver contendo o schema dentro do xml, o sistema irá desconsiderar as tags vazias para a execução do processo.

Arquivo: RM.Con.Utils.dll

## TOTVS Construção e Projetos

### Rotina: GERACAO DE PEDIDOS PRJ 33 828

* **[Ticket: 627136 / TOPEXECONTROL01-33]** Ajuste no evento da mensagem de nota fiscal (INVOICE) da integração "1002-TOTVS Obras e Projetos x BackOffice Protheus". É necessário a atualização desta mensagem na integração. Ajuste no processo de exclusão de notas fiscais ao excluir os pedidos de histórico gerados pelo processo de eliminação de resíduos de algum pedido.

Arquivos: RM.Prj.Integracao.Server.dll, RM.Prj.TotvsMessage.Configurador.Protheus.dll

## TOTVS Educacional

### Rotina: EDUCAMOBILE ALUNO SOLICITACOES EDU 51025

* **[Ticket: 577493 / MEDU-3098]** Ajuste ao logar com usuário que possui foto cadastrada, para que seja feito o redimensionamento de forma correta e não ocorra erro ao logar.

Arquivo: RM.Edu.Contexto.Data.dll

### Rotina: Teste Sistêmico 12.1.16

* **[Ticket: EDUEDU001-1604]** Retirado funcionalidades do novo portal, ainda não liberadas.

Arquivos: RM.Edu.Parametros.Intf.dll, RM.Edu.Parametros.Form.dll

* **[Ticket: EDUEDU001-1604]** Ajuste nos fluxos do projeto de pesquisa e extensão e tela de Alteração da situação do projeto de pesquisa

Arquivos: RM.Edu.PesquisaExtensao.Form.dll, RM.Edu.PesquisaExtensao.Data.dll

* **[Ticket: EDUEDU001-1604]** Retirada das permissões das funcionalidades do novo portal.

Arquivo: RM.Edu.dll

## TOTVS Folha de Pagamento

### Rotina: CONTABILIZACAO FOP 34 523

* **[Ticket: 431042 / FOPROTINAS01-312]** Ajuste no log do processo de geração de encargos.

Arquivo: RM.Fop.Dominio.dll

### Rotina: GPS - Código de pagamento

* **[Ticket: 511039 / MRH-8047]** Foi ajustado o sistema para para que no momento em que o parâmetro de código de pagamento for preenchido e o tomador for o administrativo o sistema respeite o parâmetro preenchido porém para os demais tomadores o sistema respeite o cadastro de cliente/fornecedor.

Arquivo: RM.Fop.Dominio.dll

### Rotina: LANCAMENTOS FINANCEIROS PARAMETRIZACAO FOP 34 383

* **[Ticket: 419822 / MRH-6121]** Criação de dois tipos de lançamentos financeiros de pensão nas férias para discriminar os eventos

Arquivos: RM.Fop.Const.Intf.dll, RM.Fop.Dominio.dll, RM.Fop.Rotinas.Server.dll

## TOTVS Framework

### Rotina: WIZARD RPT 00010

* **[Ticket: 364083 / MFRWBH-1038]** 1) A regra para a função de Salvar Preview é que, somente ao abrir o design do relatório e mandar Executar o Preview é que o mesmo pode ser salvo. Ao gerar o relatório pela visão dos Relatórios, o preview não poderá ser salvo.2) Ao definir como anexo obrigatório ou como anexo de carregamento automático pela tela de Preferência de Anexos, basta fechar a janela de Relatórios e abri-la novamente.

Arquivo: RM.Glb.Broker.Form.dll

## TOTVS Gerador de Relatórios

### Rotina: CONSULTA SQL RPT 00013

* **[Ticket: 321313 / MFRWBH-919]** Agora é permitido que o componente Filtro funcione em Consulta SQL vinculada a banda.

Arquivos: RM.Rpt.Executor.IService.dll, RM.Rpt.Lib.dll, RM.Rpt.Executor.Service.dll

## TOTVS Gestão Contábil

### Rotina: CADASTROS CENTROS DE CUSTOS CTB 38 83

* **[Ticket: 609608 / MEDU-3089]** Melhoria na parametrização contábil para que o código reduzido de centro de custo seja aplicado por módulo.

Arquivos: RM.Ctb.Parametros.Intf.dll, RM.Ctb.Lib.WinForms.dll, RM.Ctb.Parametros.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INTERFERENCIACOTACAO COM 012

* **[Ticket: 531504 / MCP-1976]** Acerto para que ao Restaurar a Interferência a Qtde Efetivada Total seja calculada.

Arquivo: RM.Cmp.Cotacao.Form.dll

### Rotina: REALIZACAO ORCAMENTARIA ORC 009

* **[Ticket: 586410 / MCP-2143]** Melhoria no lookup de centro de custos no processo de Realocação Orçamentária de Movimentos.

Arquivo: RM.Mov.Processos.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: REQUISIÇÕES- TRANSFERÊNCIA COM ALTERAÇÃO DE DADOS FUNCIONAIS RHU36507

* **[Ticket: MRH-7981]** Realizado ajuste na Efetivação da Requisição de Transferência com Alteração de Dados Funcionais dentro da mesma filial com progressão salarial.

Arquivo: RM.Rhu.Requisicao.Form.dll

## TOTVS Gestão Financeira

### Rotina: REAJUSTE

* **[Ticket: TINPAD001-46]** Melhoria para validação de Listas vazias

Arquivo: RM.Fin.Lan.Data.dll

## TOTVS Gestão Hospitalar

### Rotina: ELABORACAO DE CONTA SAU 47 1147

* **[Ticket: 628852 / MSAU-6611]** Ajuste para que caso a mãe ainda esteja internada, que os itens sejam lançados na conta dela.

Arquivo: RM.Sau.PepHis.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: RELATORIOS RELATORIO CONTABIL PAT 37 114

* **[Ticket: 573123 / MEDU-3063]** Atualização do relatório de contabilização para quebrar por centro de custo.

Arquivo: RM.Pat.Relatorio.Data.dll

## TOTVS Incorporação

### Rotina: BAIXA DE TITULOS FIN10060

* **[Ticket: MCP-2147]** Incidente: Foi verificado que o sistema apresentava erro ao realizar o cancelamento da baixa de uma parcela.Solução: Estava faltando uma validação no processo de cancelamento de baixa. A mesma foi incluída.

Arquivo: RM.Imb.Reajuste.Server.dll

# 12.1.15.129

## Outros

### Rotina: HOST FRW00038

* **[Ticket: MFRWBH-1457]** O parâmetro StackTraceVisible foi ampliado de forma que, quando o mesmo é falso, não serão exibidos os traces e também os textos das exceções.

Arquivo: App\_Web\_errorpage.aspx.b0135eee.dll

### Rotina: WebService

* **[Ticket: 587015 / MFRWBH-1391]** Foi realizado um ajuste na validação da sessão do usuário

Arquivos: Portal Corpore.Net

## TOTVS Automação de Ponto

### Rotina: CADASTRO HORARIOS ALTERNATIVOS PTO 35 1293

* **[Ticket: 597085 / MRH-8327]** Para adequar o sistema ao incidente relatado, foram realizadas mudanças no processo de geração de avisos. Quando um funcionário tiver menos de uma hora de intervalo planejado, o aviso "Menos de 1 hora de refeição" nunca é gerado, independentemente da quantidade de tempo executada pelo funcionário. Caso ele utilize um intervalo de ausência planejada maior ou igual a uma hora, o aviso é gerado normalmente quando o funcionário executa menos que uma hora de refeição.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: PROCESSO DE CALCULO OCORRENCIA 0043 PTO 35 1280

* **[Ticket: 636305 / MRH-8767]** Mudanças realizadas no cálculo do sistema para permitir que seja realizada desautorização de horas extras, mesmo que um funcionário seja parametrizado para ter um número de horas autorizados por período.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: PROCESSO DE CALCULO DO ADICIONAL NOTURNO PTO 35 1242

* **[Ticket: 376878 / MRH-8030]** Alterações realizadas no cálculo de adicional noturno. Agora, as ocorrências de intervalo de refeição, quando a parametrização de sindicato "Calcula adicional noturno para o intervalo de refeição" estiver marcada, são geradas corretamente para funcionários que utilizam horário rígido.

Arquivo: RM.Pto.Calculo.Service.dll

## TOTVS Business Connect

### Rotina: MENSAGEM UNICA PROCESSO CONTRATOS PEDIDO DE COMPRA ABA PRJ 33 921

* **[Ticket: 322804 / MCP-2125]** Enviar o usuário que executa o processo de gerar movimento referente a medição de contratos na TAG "UserInternalId" da mensagem "ORDER".

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

### Rotina: PADRAO

* **[Ticket: MFRWBH-1452]** A integração de sistemas foi otimizada.

Arquivo: RM.Con.Utils.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS ASSOCIACAO DE ITENS PRJ 33 939

* **[Ticket: 615667 / MCP-2069]** Selecionar apenas os valores dos insumos que compõem o grupo de custo 'Mão de Obra', para o cálculo do valor unitário do serviço no contrato.

Arquivos: RM.Prj.Contrato.Form.dll, RM.Prj.EquipeProjeto.Form.dll

### Rotina: INTEGRACAO MANUTENCAO PRJ 33 934

* **[Ticket: 662291 / TOPEXECONTROL01-34]** Ajuste no processo para adicionar turnos ao equipamento.

Arquivo: RM.Prj.Mobilidade.Server.dll

### Rotina: PLANILHAS CRONOGRAMA PRJ 33 866

* **[Ticket: 608142 / MCP-2075]** Ajuste realizado para que seja calculado as demais grandezas no cronograma quando a tarefa estiver com o valor negativo

Arquivo: RM.Prj.Cronograma.Intf.dll

### Rotina: STORED PROCEDURE PROCESSO CONTRATOS PEDIDO DE COMPRA A

* **[Ticket: MCP-1743]** Ajustada a leitura dos parametros das tabelas do PROTHEUS quando informados por empresa.

Arquivo: RM.Prj.Facade.dll

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 635876 / MEDU-3186]** Ajuste no anexo de Dados Educacionais no cadastro de filiais, deixando o mesmo visível para as novas filiais.

Arquivo: RM.Edu.Services.Server.dll

### Rotina: BOLETOS EDU 50 069

* **[Ticket: 460047 / EDUCACIONAL01-80]** Sistema passou a considerar os valores de pagamento a maior e a menor informados na baixa original do lançamento.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: EQUIVALENCIA DE DISCIPLINAS EDU 50 206

* **[Ticket: 599701 / MEDU-3016]** Ajuste na analise curricular, evitando que o aluno esteja em curso por equivalência se ele já estiver concluído a disciplina da grade via aproveitamento de estudos.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: INTEGRACAO FLUIG

* **[Ticket: EDUCACIONAL01-295]** Melhoria na integração entre TOTVS Educacional e Fluig LMS

Arquivo: RM.Edu.Integracoes.Server.dll

### Rotina: PROCESSO RESERVA DE INSTALACAO EDU 50 390

* **[Ticket: 601256 / MEDU-3050]** Ajuste na validação de colisão entre reserva de instalação para o mesmo dia.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: Project-643642 Erro na geração do plano de aula devido a quantidade de caracteres do campo ‘locacao’.

* **[Ticket: 648695 / MEDU-3204]** Aumento dos campos LOCACAO de 50 para 60 da tabela SPLANOAULA, LOCACAOATUAL de 50 para 60 da tabela SLOGPLANOAULA e LOCACAOANTERIOR de 50 para 60 da tabela SLOGPLANOAULA.

Arquivo: RM.Edu.PeriodoLetivo.Intf.dll

### Rotina: Project-648277 Dúvidas na tela de frequencia diária do professor após a implentação do abono e justificativa de faltas P

* **[Ticket: 657708 / MEDU-3251]** Ajuste no erro de concordância de português da frase "O abono das justificativas podem ou não serem aprovadas pelo coordenador" para "O abono das justificativas pode ou não ser aprovado pelo coordenador" na tela de frequência diária no portal.

Arquivos: Portal Corpore.Net

## TOTVS Folha de Pagamento

### Rotina: EVENTOS LANCAMENTOS VINCULADOS LAB 01 87

* **[Ticket: MRH-8870]** Ajuste no cálculo do CC 352 no mês de 31 dias para funcionários mensalistas.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: FUNCIONARIOS ANOTACAO PESSOAL LAB 01 126

* **[Ticket: 648317 / FOPROTINAS01-236]** Ajuste na exclusão de funcionário

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: FUNCIONARIOS CODIGOS FIXOS LAB 01 131

* **[Ticket: 487269 / FOPROTINAS01-253]** Ajuste no envio de mensagem para a integração BackOffice RM x SigaMNT na exclusão de funcionário

Arquivo: RM.Fop.TotvsMessage.Services.dll

### Rotina: FUNCIONARIOS ENVIAR EMAIL PARA FUNCIONARIOS LAB 01 138

* **[Ticket: 545939 / FOPROTINAS01-255]** Ajuste na transferência de funcionário para atualizar a chapa no contexto do Portal

Arquivo: RM.Fop.Calc.Calculos.dll

* **[Ticket: 545939 / FOPROTINAS01-255]** Ajuste no envio de relatório por e-mail para funcionários.

Arquivo: RM.Fop.Lib.Data.dll

### Rotina: HOMOLOGNET GERACAO DAS INFORMACOES

* **[Ticket: FOPCALCULO01-56]** Ajuste processo HomologNet

Arquivo: RM.Fop.Processos.Data.dll

### Rotina: INFORME DE RENDIMENTOS FOP 34 431

* **[Ticket: 616969 / FOPROTINAS01-318]** Foi ajustado o sistema para gerar informe de rendimentos de funcionários transferidos, quando o processoera realizado para toda empresa sem filtros.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: LANCAMENTOS FINANCEIROS PARAMETRIZACAO FOP 34 383

* **[Ticket: 660378 / MRH-8992]** Otimizado geração do lançamento financeiro por fórmula para abater o valor negativo do valor total quando o lançamento é agrupado

Arquivo: RM.Fop.Dominio.dll

### Rotina: Teste Sistêmico Folha de Pagamento - 12.1.16

* **[Ticket: RHFOP001-1264]** Retira o novo campo INSALUBCONSIDSALMINSIND da importação de dados do sindicato.

Arquivo: RM.Fop.Importacao.Data.dll

## TOTVS Framework

### Rotina: CONCLUIR CONTRATO CTR 016

* **[Ticket: 573418 / MFRWBH-1415]** Melhoria na integração de Fluxo de Trabalho do RM com o Fluig

Arquivos: RM.Lib.Server.dll, RM.Lib.WinForms.dll

### Rotina: PERFIL

* **[Ticket: MFRWBH-1421]** Os campos complementares agora estão sendo enviados para o Identity.

Arquivos: RM.Glb.IntegracaoFluig.Server.dll, RM.Lib.Communication.Server.dll

## TOTVS Framework Web

### Rotina: SEGURANCA

* **[Ticket: MFRWBH-1425]** Melhorias de segurança no portal para evitar ataques Cross Site Scripting.

Arquivos: RM.Lib.WebForms.dll, Web.config, jquery.mask.js, jquery-latest.min.js

## TOTVS Gerador de Relatórios

### Rotina: GERACAO DE RELATORIO RPT 00005

* **[Ticket: 635858 / MFRWBH-1406]** O formato {0:c} é aplicado corretamente.

Arquivo: RM.Rpt.Executor.Service.dll

## TOTVS Gestão Bibliotecária

### Rotina: PESQUISA PUBLICA BIB 10 1069

* **[Ticket: 646181 / MEDU-3197]** Ajuste na exibição dos detalhes da publicação ao utilizar a pesquisa pública pelo portal.

Arquivo: RM.Bib.Publicacao.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CADASTRO DE FORMULA FRM 001

* **[Ticket: 619708 / MCP-2092]** Acerto para utilizar a TPRDFISCAL nas formulas da view TPRD.

Arquivo: RM.Mov.Formula.dll

### Rotina: CÓPIA POR REFERENCIA MOV014

* **[Ticket: MCP-2149]** Ao realizar o ajuste para permitir a expansão da Grid de Itens de Movimentos no Assistente de Cópia por referência, os eventos de BeforeLooup e AfterLookup do item foram removidos do arquivo designer.cs, gerando o bug de não habilitar o botão de Avançar ao selecionar os itens.

Arquivo: RM.Mov.Processos.Form.dll

### Rotina: NATUREZA ORCAMENTARIA FINANCEIRA ORC 011

* **[Ticket: 620761 / MCP-2168]** Acerto para que ao realizar a Cópiar Natureza Orçamentária entre Coligada considerar no Rateio a Coligada destino.

Arquivo: RM.Mov.Orcamento.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: TREINAMENTO TURMAS RHU 36 055

* **[Ticket: 505376 / MRH-7027]** Ajustado o query sql que estava inserindo somente o primeiro registro.

Arquivo: RM.Rhu.Treinamento.Data.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA ENCERRAMENTO DE PERIODO FIN 010

* **[Ticket: 509721 / MEDU-3013]** Melhoria em conversor de aplicação financeira

Arquivos: RM.Fin.AplicacaoFinanceira.Server.dll, RM.Fin.AplicacaoFinanceira.Data.dll

### Rotina: RELATORIO FLUXO DE CAIXA FIN 230

* **[Ticket: 465624 / FINANCEIRO01-117]** Otimização no processo de emissão do relatório de Fluxo de Caixa. Agora o sistema carrega as coligadas corretamente.

Arquivo: RM.Fin.FluxoCaixa.Form.dll

## TOTVS Gestão Fiscal

### Rotina: NF E CONSULTA AUTORIZACAO NF 01 0046

* **[Ticket: 635942 / MEDU-3257]** Alterações no preenchimento do XML da NF-e, integrada com a NeoGrid - Totvs Colaboração 2.0

Arquivos: RM.Fis.NFe.Intf.dll, RM.Fis.NFe.Service.dll

* **[Ticket: 526037 / MEDU-2784]** Criação de um parâmetro que será utilizado para validar se as acentuações irão ou não no XML da Nota Fiscal.Criado um parâmetro na TPARFILIAL, coluna RETIRAACENTOS, para validar se o XML da nota irá com as acentuações ou se elas serão retiradas durante a montagem do XML.

Arquivos: RM.Fis.Utils.Server.dll, RM.Fis.NFe.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 583213 / MEDU-3209]** Alteração no envio da NFS-e, no momento de carregar os dados do Tomador da nota fiscal.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Erro ao processar Remessas

* **[Ticket: 546839 / MSAU-5825]** Ajuste para que não seja gerado erro com faturamento acima de 100 contas

Arquivos: RM.Sau.Faturamento.Intf.dll, RM.Sau.Faturamento.Server.dll

## TOTVS Incorporação

### Rotina: ADITIVO ALTERACAO DAS TAXAS DE REAJUSTE IMB 49 791

* **[Ticket: 551575 / MCP-2094]** Removida a obrigatoriedade de histórico de reajuste para determinar o próximo identificador do histório do reajuste no momento da efetivação do aditivo.

Arquivo: RM.Imb.Reajuste.Server.dll

### Rotina: REAJUSTE

* **[Ticket: TINPAD001-46]** Implementação para Reajuste com antecipação PRICE

Arquivo: RM.Imb.Reajuste.Intf.dll

## TOTVS Processo Seletivo

### Rotina: CADASTRO

* **[Ticket: MEDU-3244]** Ajuste na tela de listagem de resultados para tratamento de exceção.

Arquivos: RM.EduPS.Cadastros.Data.dll, App\_Web\_edupsresultadosgerais.ascx.b5bee319.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: FUNCIONARIOS CONTROLE DE ATESTADOS RHU 36 571

* **[Ticket: 567984 / MRH-7966]** Realizado ajuste no lançamento de atestados.

Arquivo: RM.Smt.Pessoa.Form.dll

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 612069 / MRH-8463]** Realizado ajuste no cadastro de prontuário Médico.

Arquivo: RM.Smt.Pessoa.Form.dll

# 12.1.15.130

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO OCORRENCIAS PTO 35 1193

* **[Ticket: 639513 / PONTO01-277]**  Ajuste realizado no módulo de Lançamento de batidas pelo horário planejado para que as batidas referentes à ausência planejada sejam lançadas também em dias de compensado ou descanso quando estas estão devidamente cadastradas no horário do funcionário.

Arquivo: RM.Pto.Batida.Data.dll

### Rotina: PERIODOS CADASTRO DE PERIODO PTO 35 1284

* **[Ticket: 614498 / MRH-8439]** Alterações no processo de edição de batidas, para permitir a alteração ou inserção de batidas corretamente no espelho.

Arquivo: RM.Pto.Batida.Data.dll

### Rotina: PERIODOS DEFINICAO DO PERIODO DE APURACAO PTO 35 1233

* **[Ticket: 408638 / MRH-5676]** Ajustada a rotina de transferência de registros para tabela de arquivo morto ao transferir os dados de um período para a tabela de produção o sistema não está transferindo para a tabela AMOVFUN, os dados da AMOVFUNAM.

Arquivo: RM.Pto.Periodo.Data.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 660053 / MRH-8989]** Ajuste realizado para que a geração do relatório de espelho seja concluída com sucesso.

Arquivos: RM.Pto.Horario.Intf.dll, RM.Pto.Horario.Data.dll

## TOTVS Business Connect

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 95522 / TINPAD001-11]** Melhoria na geração de titulos para o Protheus, o sistema passa a informar o tipo de documento correto ao Protheus para que o titulo seja gerado com o tipo pré determinado no TIN.

Arquivos: RM.Con.ConfiguraIntegracao.TotvsIncorporacaoProtheus.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: 647718 / MFRWBH-1416]** Retorno do método AutenticaAcesso no wsBase do TBC Host

Arquivos: RM.Con.Conector.Service.dll, RM.Con.Conector.Interface.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS LIBERACAO ENVIAR PARA SUPRIMENTOS PRJ 33 995

* **[Ticket: 620989 / MCP-2135]** Ajuste realizado para que ao ser liberado o período de contrato para o suprimento/Faturamento o percentual de reajuste aplicado permaneça informado no período

Arquivo: RM.Prj.Contrato.Data.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: Falha de Importação Cultura Final por Arquivo .dat

* **[Ticket: 638762 / MSAU-6671]** Ajuste para importar corretamente os arquivos de cultura

Arquivo: RM.SauIH.Importacao.Data.dll

## TOTVS Educacional

### Rotina: BOLETOS EDU 50 069

* **[Ticket: 460047 / EDUCACIONAL01-80]** Ajuste na inclusão da bolsa retroativa que não estava considerando pagamento a maior ou a menor já existente na conta corrente do aluno

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: BOLSA RETROATIVA EDU 50 479

* **[Ticket: 613513 / MEDU-3117]** Melhoria processo de bolsa retroativa para que não seja apresentada nenhuma não conformidade quando o boleto do lançamento já estiver código de barras gerado ou remetido ao banco.

Arquivos: RM.Fin.Lan.Service.dll, RM.Edu.Facade.dll, RM.Edu.Financeiro.Server.dll, RM.Edu.Lib.Intf.dll, RM.Fin.Lib.dll, RM.Edu.Financeiro.Intf.dll

### Rotina: CONTRATOS CONTABILIZACAO EDU 50 141

* **[Ticket: 597531 / EDUCACIONAL01-43]** Foi feito o ajuste na rotina de arredondamento de valores para identificar corretamente a última parcela do contrato e efetuar o devido ajuste em seu valor fazendo com que o valor financeiro do contrato financeiro visualizado pela rotina de contabilização fique correto e não mais sejam geradosregistros de aumentos ou cancelamentos de contabilizações indevidos.

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Lib.WinForms.dll

### Rotina: GERACAO DE MOVIMENTO EDU 50 229

* **[Ticket: 595038 / MEDU-3127]** Melhoria no processo de geração de movimento, pois para determinados cenários quando utilizamos tag ”[ALU.D]” no campo histórico do movimento o sistema estava apresentandoo nome de outro aluno.

Arquivo: RM.Edu.Facade.dll

## TOTVS Folha de Pagamento

### Rotina: DIFERENCA SALARIAL LAB 01 109

* **[Ticket: 654991 / MRH-8982]** SEFIP 650 passa a considerar para o registro 30 "Registro do Trabalhador" campo 20 "Valor Descontado do Segurado" o valor dos eventos de código de cálculo 132 "Diferença de INSS Férias próximo mês".

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: EVENTOS LANCAMENTOS VINCULADOS LAB 01 87

* **[Ticket: MRH-9094]** Criação do parâmetro "Salário maternidade complementar (tipo W) considera dias corridos do mês".

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

### Rotina: FOLHA RECALCULO LAB 01 111

* **[Ticket: 366235 / MRH-8923]** Exclusão do registro do empréstimo inserido pelo processo de Lançamento das Férias.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: GRUPO DE EVENTOS LAB 01 116

* **[Ticket: 648855 / MRH-8875]** Criação de parâmetro para considerar as fórmulas adicionais para Licença Maternidade no cálculo do CC 352.

Arquivos: RM.Fop.Parametros.Intf.dll, RM.Fop.Parametros.Form.dll

### Rotina: HOMOLOGNET GERACAO DO ARQUIVO XML

* **[Ticket: FOPCALCULO01-55]** Ajuste processo HomologNet

Arquivo: RM.Fop.Processos.Data.dll

## TOTVS Framework

### Rotina: FORMULA VISUAL FVS 01

* **[Ticket: 635018 / MFRWBH-1390]** Melhoria na associação de data servers a gatilhos de fórmula visual, informando ao usuário dos data servers que não podem ser utilizados.

Arquivo: RM.Glb.Workflow.Form.dll

* **[Ticket: 635018 / MFRWBH-1390]** Melhoria na associação de data servers a gatilhos de fórmula visual, informando ao usuário dos data servers que não podem ser utilizados.

Arquivo: RM.Glb.Workflow.Form.dll

### Rotina: PLANILHA NET EXECUCAO BIS 00047

* **[Ticket: 550401 / MFRWBH-1463]** Quando os parametros são informados através da planilha.Net e não tem o tipo reconhecido, devem ser considerados como alfanumérico.A consulta ABSENTEÍSMO 2016 - FILIAL 02, assim como algumas de suas similares das outras filiais, contém parametros MES, ANO, MES\_S e ANO\_S. Porém na planilha.Net somente existem os parametros MES e ANO. Provavelmente os parametros MES\_S e ANO\_S foram adicionados posteriormente, sendo assim não são adicionados automaticamente a planilha.Net.Ao removermos a consulta da planilha e reinseri-la novamente preenchedo os parametros a consulta é executada corretamente.Já as consultas abaixo, assim como as suas similares das outras filiais, não executam pelo cadastro de consultas do RM e nem mesmo diretamente pelo Banco de Dados. Sendo assim, o cliente deve verificar o problema e ajustar cada uma das consultas.TUNOVER - FILIAL 02TURNOVER 2016 - FILIAL 02TURNOVER DEMITIDOS - FILIAL 02NRº DE EMPREGADOS ATIVOS - FILIAL 02Nº EMPREGADOS ATIVOS 2016 - FILIAL 02

Arquivo: RM.Lib.Server.dll

* **[Ticket: 550401 / MFRWBH-1463]** Quando os parametros são informados através da planilha.Net e não tem o tipo reconhecido, devem ser considerados como alfanumérico.A consulta ABSENTEÍSMO 2016 - FILIAL 02, assim como algumas de suas similares das outras filiais, contém parametros MES, ANO, MES\_S e ANO\_S. Porém na planilha.Net somente existem os parametros MES e ANO. Provavelmente os parametros MES\_S e ANO\_S foram adicionados posteriormente, sendo assim não são adicionados automaticamente a planilha.Net.Ao removermos a consulta da planilha e reinseri-la novamente preenchedo os parametros a consulta é executada corretamente.Já as consultas abaixo, assim como as suas similares das outras filiais, não executam pelo cadastro de consultas do RM e nem mesmo diretamente pelo Banco de Dados. Sendo assim, o cliente deve verificar o problema e ajustar cada uma das consultas.TUNOVER - FILIAL 02TURNOVER 2016 - FILIAL 02TURNOVER DEMITIDOS - FILIAL 02NRº DE EMPREGADOS ATIVOS - FILIAL 02Nº EMPREGADOS ATIVOS 2016 - FILIAL 02

Arquivos: RM.Lib.Server.dll, RM.Glb.PlanilhaNet.API.dll

## TOTVS Gerador de saídas

### Rotina: GERACAO DA SAIDA DA CLASSE E DO S ARQUIVO S TEXTO GEN 05

* **[Ticket: 638543 / MFRWBH-1393]** Melhoria para que ao salvar um arquivo do gerador de saídas em uma pasta do servidor, ocorra uma substituição caso já exista um arquivo com o mesmo nome.

Arquivo: RM.Gen.Engine.Server.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS BALANCETE CTB 38 113

* **[Ticket: 96255 / CONTROLADORIA01-66]** Através da tela de parâmetros do módulo contábil é possível definir as máscaras que serão aplicadas nas contas, contábeis e gerenciais, dos relatórios fixos do sistema. Para atender essa configuração que existia na versão delphi todos os relatórios foram alterados.

Arquivos: RM.Ctb.Relatorios.Service.dll, RM.Ctb.Sped.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: ANALISE DE RESSUPRIMENTO EST 017

* **[Ticket: 610099 / MCP-2057]** Melhoria para selecionar somente itens (e não agrupadores) na Análise de Sugestão de ressuprimento

Arquivos: RM.Est.Ressuprimento.Form.dll, RM.Est.Ressuprimento.Service.dll

### Rotina: ASSISTENTE COTACAO COM 007

* **[Ticket: 529386 / MCP-2105]** Melhoria para permitir que após a importação da cotação da WEB, o sistema permita o registro de novos

Arquivo: RM.Cmp.Cotacao.Service.dll

### Rotina: CADASTRO DE PRODUTOS PRD 001

* **[Ticket: 440360 / MATESTCNTFTOF01-27]** Ajuste na cópia de produtos compostos entre coligadas.

Arquivo: RM.Est.Produto.Data.dll

### Rotina: COMUNICARFORNECEDORES COTACAO COM 016

* **[Ticket: 511200 / MCP-2164]** Acerto para consistir produtos fornecidos de acordo com a Coligada da Solicitação.

Arquivos: RM.Cmp.Cotacao.Intf.dll, RM.Cmp.Cotacao.IService.dll, RM.Cmp.Cotacao.Service.dll, RM.Cmp.Cotacao.Data.dll, RM.Cmp.Cotacao.Form.dll

### Rotina: ENVIO DE EVENTOS MANIFESTACAO MDE 002

* **[Ticket: 613604 / MCP-2162]** Melhoria para verificar o status do MD\_E no retorno de eventos ao invéz de verificar o número do Erro.

Arquivo: RM.Mov.TOTVSColab.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 574976 / MCP-2123]** Melhoria no processo de preenchimento do campo código serviço

Arquivo: RM.Mov.Movimento.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: MAPA DE CONHECIMENTO DEFINICAO POR COMPETENCIAS RHU 36 080

* **[Ticket: 524849 / MRH-7525]** Ajuste ao inserir participantes em avaliação por vinculo de tarefa

Arquivo: RM.Rhu.AvalDesemp.Server.dll

### Rotina: VALIDACAO DA LIBERACAO DE COMPETENCIA LAB 01 124

* **[Ticket: 604105 / MRH-8714]** Ajuste ao executar parametrizador para verificar se existe integração com labore ao executar update

Arquivo: RM.Rhu.Parametros.Data.dll

## TOTVS Gestão Financeira

### Rotina: CONTA CAIXA INCLUSAO ALTERACAO EXCLUSAO FIN 116

* **[Ticket: 605886 / FINANCEIRO01-116]** Verificar se a conta caixa possui lançamentos para poder barrar a alteração dos campos Banco/Agência/Conta Corrente, no momento de salvar a conta caixa

Arquivo: RM.Fin.ContaCaixa.Data.dll

### Rotina: SESSAO DE CAIXA INCLUIR LANCAMENTO FIN 280

* **[Ticket: 625552 / FINANCEIRO01-63]** Otimizada a busca de lançamentos através do responsável financeiro (CliFor) Global.

Arquivo: RM.Fin.SessaoCaixa.Data.dll

## TOTVS Gestão Fiscal

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 660282 / MEDU-3303]** Alteração no preenchimento dos dados do IPI no envio da NF-e.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NF E IMPRESSAO DE DANFE NF 01 0001

* **[Ticket: 646823 / MEDU-3284]** Retira o campo Numero do endereço do Emitente que era gerado desnecessariamente no DANFE.

Arquivo: RM.Fis.Lib.Server.dll

### Rotina: OBRIGACOES ACESSORIAS MUNICIPAIS LI 01 0034

* **[Ticket: 598793 / MEDU-3271]** Foram identificadas alterações na rotina NFTS de São Paulo. Foram adicionados dois campos no registro “4 - Detalhe”, Cadastro Específico do INSS (CEI) e Número de inscrição da obra.O campo “30 - Cadastro Específico do INSS (CEI)” será preenchido da seguinte forma:- Caso o CNPJ do Projeto seja um código CEI válido o sistema irá preencher com o mesmo. Caso o CNPJ do Projeto não seja um código CEI válido, o sistema irá preencher com o CNPJ da Filial caso o mesmo seja um CEI válido. Se nenhum dos dois campos for um CEI válido, o sistema irá gerar o campo zerado.O campo “31 – Número de inscrição da obra” será preenchido através da criação de um campo complementar no Projeto. O campo deverá ser chamado “NUMINSCOBRA”, do tipo alfanumérico tamanho 12.

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.Sped.Server.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADASAÍDA LI010046

* **[Ticket: 100120 / FISCAL01-94]** Foi identificado que, ao realizar as alterações referentes à melhorias no cálculo do Diferencial de Alíquota do ICMS Interestadual na Entrada, não foi previsto que pudesse existir a redução na Base de Cálculo do ICMS Interno e no ICMS Interestadual, e que o valor dos dois tributos pudesse ser o mesmo. Quando esse caso acontecia, o sistema não realizava o cálculo de forma correta, trazendo o valor do Diferencial de alíquota diferente de Zero.

Arquivos: RM.Fis.LancFiscal.Intf.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.EscrituracaoFiscal.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: #PEP #ARARAS - Na execução de um procedimento ele está informando que o procedimento está fora da conta

* **[Ticket: SAUPEP01-1211]** Caso o prestador seja o prestador principal, seu lançamento será gerado como Dentro da Conta

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: 12.1.15 - Erro ao copiar agendamento de Grupo

* **[Ticket: 545886 / MSAU-6080]** Ajustes no agendamento de grupo.

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: BOTAO associar retorno de autorizaçao!

* **[Ticket: 634817 / MSAU-6607]** Ajuste para que a solicitação seja realizada com sucesso para pacientes internados

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: Cadastro de RN

* **[Ticket: 643471 / MSAU-7105]** Ajuste para o correto cadastro de recém nascidos no sistema.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: PRONTUARIO ELETRONICO - Ajuste na Justificativa de Prescrição

* **[Ticket: 399031 / MSAU-6227]** Ajuste realizado para que o sistema exiba a justificativa tanto para antimicrobianos quanto para itens restritos não padronizados.

Arquivos: RM.Sau.Pep.Intf.dll, RM.Sau.Pep.Data.dll, RM.Sau.Pep.Form.dll

## TOTVS Incorporação

### Rotina: ADITIVO TROCA DE COMPRADOR IMB 49 785

* **[Ticket: 665504 / MCP-2196]** Melhoria no Aditivo com reajuste para sincronizar somente os valores de integração do financeiro com o TIN,

Arquivos: RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll

### Rotina: ALUGUEL ADITIVOS DO CONTRATO DE LOCACAO IMB 49 779

* **[Ticket: 637779 / MCP-2152]** Melhoria no processo de desfazer aditivo no módulo de aluguel.

Arquivos: RM.Imb.Aluguel.Lancamento.IServer.dll, RM.Imb.Aluguel.Lancamento.Server.dll

### Rotina: formula visual versão 12

* **[Ticket: 481421 / MCP-2041]** Ajuste na efetivação de aditivo de troca de comprador e renegociação para executar corretamente formulas visuais

Arquivos: RM.Imb.Aditivos.IServer.dll, RM.Imb.Aditivos.Server.dll

### Rotina: RELATORIOS INCORPORACAO IMB 49 854

* **[Ticket: 667163 / MCP-2182]** Melhoria na ficha financeira para exibir no quadro de resumos os valores aditivados no contrato.

Arquivos: RM.Imb.Relatorio.Data.dll, RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Relatorio.Intf.dll

# 12.1.15.131

## TOTVS Banco de Dados

### Rotina: CONVERSAO DA BASE DE DADOS 90 6

* **[Ticket: 624886 / MGCADBH-137]** SGBD: ORACLECHAMADO: MGCADBH-137JUSTIFICATIVA: Quando tenta realizar a conversão em uma instância com mais de um schema é retornado um erro de ORA-01422: exact fetch returns more than requested number of rows, sendo assim foi reavaliado a tratativa para verificar o esquema correto.

Arquivos: Cvn.12.1.1.sql, Cvn.12.1.10.sql, Cvn.12.1.12.sql, Cvn.12.1.15.sql, Cvn.12.1.3.sql, Cvn.12.1.4.sql, Cvn.12.1.7.sql, Cvn.12.1.8.sql, Cvn.12.1.9.sql, RMCMelhoria\_1100e8354.sql

## TOTVS Business Connect

### Rotina: Integração RM - GED

* **[Ticket: 667178 / MFRWBH-1480]** Melhoria na sincronização de usuários na integração com o GED para que os usuários possam ser sincronizados sem inconsistências, ou que as inconsistências da sincronização sejam exibidas para o usuário.

Arquivo: RM.Con.GED.Server.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS GERACAO DE PEDIDOS PRJ 33 938

* **[Ticket: 673776 / TOPEXECONTROL01-32]** Durante a inclusão do pedido de material, a opção 'Utiliza Preço Orçado', será selecionado por padrão.

Arquivo: RM.Prj.PedidoMaterial.Server.dll

* **[Ticket: 673776 / TOPEXECONTROL01-32]** Durante a inclusão do pedido de material, a opção 'Utiliza Preço Orçado', será selecionado por padrão.

Arquivo: RM.Prj.PedidoMaterial.Server.dll

### Rotina: PLANILHAS CRONOGRAMA PRJ 33 866

* **[Ticket: 672730 / TOPEXECONTROL01-37]** Ajuste na visão de cronograma como planilha, atualizando as colunas de data quando alterado o projeto

Arquivo: RM.Prj.Cronograma.Form.dll

### Rotina: PLANILHAS - TAREFAS PRJ33872

* **[Ticket: TOPORCAPLAN001-14]** Validar a quantidade dos recursos da tarefa após a alteraçã com as quantidades já pedidas e consumidas

Arquivos: RM.Prj.Parametros.Intf.dll, RM.Prj.Contrato.Intf.dll, RM.Prj.Parametros.Data.dll, RM.Prj.Parametros.Form.dll, RM.Prj.PedidoMaterial.Intf.dll, RM.Prj.Planilhas.Data.dll, RM.Prj.Calculo.Server.dll, RM.Prj.Contrato.Data.dll, RM.Prj.PedidoMaterial.Server.dll

### Rotina: RELATORIOS FIXOS COMPOSICOES DO PROJETO PRJ 33 947

* **[Ticket: 596873 / TOPORCAPLAN001-26]** Ajuste na exibição do campo Valor Unitario do Relatório de 'Planilha de composição analítica por tarefas com BDI Diferenciado'

Arquivo: RM.Prj.Formula.dll

## TOTVS Educacional

### Rotina: BAIXAS REALIZADAS CANCELAMENTO DE ITEM DE BAIXA FIN 024

* **[Ticket: 615015 / FINANCEIRO01-123]** Melhoria processo de bolsa retroativa para que não seja apresentado erro quando o lançamento tiver mais de uma baixa com datas distintas

Arquivo: RM.Edu.Facade.dll

### Rotina: CAMPOS COMPLEMENTARES TURMA DISCIPLINA EDU 50 109

* **[Ticket: 620134 / EDUCACIONAL01-91]** Melhoria no processo Cadastrar Turmas/Disciplinas para a Turma, registrando os dados de campos complementares na tabela STURMADISCCOMPL.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 590910 / EDUCACIONAL01-37]** Alteração da mensagem de alerta nos parâmetros do sistema quando o tipo contábil for por serviço deixando explícito que o não preenchimento do tipo contábil no serviço, fará com que o respectivo lançamento seja gerado como "Não contábil".O não preenchimento do tipo contábil no serviço passou a ser informado como Warning (Aviso) na geração de lançamentos. A mensagem também foi alterada a fim de deixar claro que o respectivo lançamento será gerado como "Não contábil"

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Edu.Parametros.Form.dll

### Rotina: MATRICULA EM DISCIPLINAS EDU 50 295

* **[Ticket: 666900 / EDUCACIONAL01-25]** Ajustes no processo de Matricular alunos em disciplinas incluídas na matriz curricular quando o total de registros no processo excedem o limite de parâmetros.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: MUDAR TURMA EDU 50 314

* **[Ticket: 624361 / EDUCACIONAL01-23]** Otimizado processo de mudança de turma, ensino básico, para permitir transferir o aluno de uma turma que tenha o mesmo código da turma em períodos letivos diferentes, por exemplo Turma 01 existe no período letivo 2016 e 2017.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: PORTAL ALUNO TCC EDU 50 368

* **[Ticket: 607660 / MEDU-3084]** Melhoria no upload de arquivo do TCC, emitindo mensagem de aviso para o aluno independente do navegador utilizado.

Arquivos: Portal Corpore.Net

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 653298 / EDUCACIONAL01-24]** O sistema será alterado para considerar o campo complementar Licenciatura com o valor "S" ou "1". Antes considerava apenas "S", mas existe uma mensagem no sistema pedindo para que esse campo seja cadastrado como inteiro.

Arquivo: RM.Edu.Academico.Server.dll

## TOTVS Folha de Pagamento

### Rotina: FOLHA

* **[Ticket: MRH-9228]** Retirado o botão de acesso a tela do SIRETT do sistema.

Arquivos: RM.Fop.Server.dll, RM.FopFolha.dll

### Rotina: PROCESSOS ADMISSAO DE FUNCIONARIO FOP 34 466

* **[Ticket: 647073 / MRH-9152]** Ajuste na rescisão por transferência para preencher as colunas RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY e RECMODIFIEDON com o usuário corrente e data do dia, no registro da nova chapa na PFUNC.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: RM REPORTS LAB 01 188

* **[Ticket: 476616 / MRH-8138]** Criado novo parâmetro no demonstrativo de pagamento do portal para considerar ou não as chaves ativas dos eventos para serem exibidos no relatório do portal

Arquivos: RM.Fop.Paramquiosque.Intf.dll, RM.Fop.Parametros.Form.dll, RM.Fop.Envelope.Data.dll

* **[Ticket: 476616 / MRH-8138]** Criado novo parâmetro no demonstrativo de pagamento do portal para considerar ou não as chaves ativas dos eventos para serem exibidos no relatório do portal

Arquivo: RM.Fop.Parametros.Form.dll

## TOTVS Framework

### Rotina: PERT GANTT PRJ 33 862

* **[Ticket: 626923 / TOPORCAPLAN001-65]** Verificar o cálculo das durações dos nodos(etapas) agrupadores no pert.

Arquivo: RM.Lib.WinForms.Gantt.dll

### Rotina: PLANILHA NET EXECUCAO BIS 00047

* **[Ticket: 666504 / MFRWBH-1487]** O sistema deve abrir a planilha.Net em sistemas que contenham apenas o Excel 2016 normalmente.

Arquivo: RM.Glb.PlanilhaNet.Intf.dll

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: 650340 / MFRWBH-1417]** A autenticação do usuário deve ser validada corretamente durante o consumo de serviços.

Arquivo: RM.Lib.Server.dll

## TOTVS Gestão Bibliotecária

### Rotina: EDITORAS BIB 10 1031

* **[Ticket: 664302 / MEDU-3312]** Ajuste no filtro de Editora do cadastro de publicação.

Arquivos: RM.Bib.Cadastros.Data.dll, RM.Bib.Cadastros.Intf.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS BALANCETE CTB 38 113

* **[Ticket: 647536 / CONTROLADORIA01-68]** Melhoria para que o filtro do centro de custo consiga trabalhar com os intervalos nos casos de códigos que possuem letra.

Arquivo: RM.Ctb.Lib.WinForms.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CADASTRO REPRESENTANTE REP 001

* **[Ticket: 330118 / MATFATCMPCRM01-33]** Ajustado mensagem de consistência ao incluir registro de representante inválido.

Arquivo: RM.Mov.Cadastros.Data.dll

### Rotina: DESCANCELAR CONTRATO CTR 008

* **[Ticket: 114383 / MATESTCNTFTOF01-44]** Sistema apresenta inconsistência ao descancelar contrato

Arquivo: RM.Ctr.Contrato.Service.dll

### Rotina: GERAR ORDEM DE COMPRA COTAÇÃO COM010

* **[Ticket: 96766 / MATFATCMPCRM01-126]** Melhorias no processo de estorno de item não recebido quando a ordem de compra foi gerada pelo processo de cotação.

Arquivo: RM.Cmp.Cotacao.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 579353 / MATESTCNTFTOF01-37]** Ajuste no dataserver de Lotes de Produto para correto funcionamento na inclusão de produtos com lote no movimento.

Arquivos: RM.Est.Produto.Data.dll, RM.Mov.Movimento.Form.dll

### Rotina: ORDEM DE COMPRA COM002

* **[Ticket: 95568 / MATFATCMPCRM01-83]** Ao estornar item não recebido para movimento faturado parcialmente por valor, a quantidade do produto fica zerada.

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS PAINEL DE OPCOES RHU 36 027

* **[Ticket: 677104 / MRH-9206]** O problema estava acontecendo quando tentava salvar mais de uma vez o registro de bairro no mesmo dia. Pois quando salvava a tela era preenchido um historico na tabela PFHSTEND. Mas na tabela CODPESSOA E DTMUDANCA são KEYS e o sistema estava tentando criar um novo registro com datas iguais, pois ele não gerava data com hora e somente a data.

Arquivo: RM.Rhu.Curriculo.Server.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 568228 / FINANCEIRO01-77]** Ajustes no serviço de baixa de lançamentos, para fazer o update dos rateios de centro de custo e departamento dos itens de baixa gerados pela inclusão do borderô de pagamento, quando o sistema estiver parametrizado para baixa one log (parâmetro: "Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa” habilitado).

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 635770 / FINANCEIRO01-78]** Melhoria Retorno de cobrança - Evitar erro " - inclusão de registro cujo valor da chave primária já existe - inclusão de registro cujo valor do índice único já existe" quando efetuar retorno de cobrança bancária utilizando o parâmetro "Contas a Receber > Integração Bancária > No retorno bancário utilizar os valores (Juros, multa e desconto) do arquivo, sobrepondo os do lançamento" marcado

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: Retrabalho - erro ao integrar cliente e fornecedor ao protheus

* **[Ticket: TINPAD001-40]** Melhoria na entidade CUSTOMERVENDOR 2.002 para efetuar o cadastro de cliente/fornecedor do TIN para o Protheus. Quando o Protos enviar o prospect do cliente para que o mesmo seja salvo como cliente no TIN o mesmo passa a ser enviado ao Protheus também.

Arquivo: RM.Fin.CliFor.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 463002 / MEDU-3159]** Foram realizadas alterações no envio da NFS-e para que sejam enviadas as seguintes informações:Cadastro Específico do INSS (CEI): será enviado o valor do campo “CNPJ” do Projeto, caso o mesmo seja um código CEI válido. Caso não seja, será enviado o CNPJ da Filial, caso seja um código CEI válido. Caso nenhuma das informações citadas seja um CEI válido, o sistema enviará o CNPJ do Projeto.Número da Obra: será preenchido através da criação de um campo complementar no Projeto. O campo deverá ser chamado “NUMINSCOBRA”, do tipo alfanumérico tamanho 15 (a NFS-e de São Paulo aceita somente 12 caracteres).

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS LI 01 0031

* **[Ticket: 121850 / MEDU-798]** Foram realizadas alterações na geração da rotina SISCOSERV para que seja gerada a tag <MotivoNaoPreenchimentoNif>. A geração da tag será de acordo com o valor informado no campo “Situação do NIF” do Cliente/Fornecedor:Caso seja informada a opção “Beneficiário Dispensado do NIF”, será gerado o valor “1” na tag.Caso seja informada a opção “País não Exige NIF”, será gerado o valor “2” na tag.Caso seja informada a opção “Informar Número de Identificação Fiscal”, a tag não será gerada.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: ELABORACAO DE AIHS SAU 47 1144

* **[Ticket: 686273 / MSAU-7072]** Realizado ajuste no sistema para tratar a mensagem apresentada ao selecionar o procedimento principal da AIH.

Arquivos: RM.Sau.Sus.Data.dll, RM.Sau.Sus.Form.dll, RM.Sau.Sus.Server.dll

* **[Ticket: 686273 / MSAU-7072]** Realizado ajuste no sistema para tratar a mensagem apresentada ao selecionar o procedimento principal da AIH.

Arquivo: RM.Sau.Sus.Form.dll

### Rotina: OUTROS PROCESSOS SAU 47 1173

* **[Ticket: 558164 / MSAU-6707]** Ajuste para que o sistema utilize o número da guia operadora retornado no XML do convênio.

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: RÉPLICA para 12.1.16 - Lentidão no processo de faturamento

* **[Ticket: MSAU-4911]** Ajuste na performance da rotina de faturmento para convênios.

Arquivos: RM.Sau.Ans.Intf.dll, RM.Sau.Services.Server.dll, RM.Sau.Repasse.Server.dll, RM.Sau.Ans.Sever.dll, RM.Sau.Faturamento.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: OPERACOES PATRIMONIAIS ACRESCIMO PAT 37 48

* **[Ticket: 512712 / CONTROLADORIA01-65]** A cotação da moeda passou a ser retornada corretamente durante a execução do processo de avaliação patrimonial.

Arquivo: RM.Pat.Ocorrencia.Service.dll

## TOTVS Incorporação

### Rotina: ADITIVO ALTERACAO DE VENCIMENTO IMB 49 780

* **[Ticket: 679253 / TINPAD001-17]** Melhoria no aditivo de vencimento, apenas versão revitalizada.

Arquivo: RM.Imb.Venda.Aditivo.Form.dll

### Rotina: Erro ao gravar rescisão versão revitalizada

* **[Ticket: 649791 / TINPAD001-54]** Melhoria na efetivação do distrato para se existe regra com origem distrato e tenha parcela gerada para motivos que gerem parcelas de devolução

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

### Rotina: Erro ao salvar o contrato

* **[Ticket: 627688 / TINPAD001-10]** Incidente:Ao gerar contrato estava sendo apresentada uma mensagem de erro reportando que o valor inserido no campo CONF\_FRE ("Confrontação Frente") excedia o tamanho máximo permitido. Porém o valor informado possuía 200 caracteres, exatamente o máximo permitido no banco de dados para este campo.Solução: Foi verificado que para gerar o contrato este campo estava configurado para aceitar no máximo 35 caracteres, o que ocasionava o erro. O campo foi modificado para aceitar no máximo 200 caracteres.

Arquivo: RM.Imb.Contratos.Intf.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 548689 / TINPAD001-8]** Melhoria no rateio por centro de custo.

Arquivos: RM.Imb.Facade.dll, RM.Imb.Reajuste.Server.dll

### Rotina: RELATORIOS INCORPORACAO IMB 49 854

* **[Ticket: 667115 / TINPAD001-6]** Ajuste no lookup de cliente da tela de relatório

Arquivo: RM.Imb.Venda.Contrato.Data.dll

### Rotina: Revitalização

* **[Ticket: TINPAD001-14]** Melhoria nas condições de venda do aditivo e distrato, somente clientes revitalizados.

Arquivos: RM.Imb.Consts.dll, RM.Imb.Venda.Lib.Intf.dll, RM.Imb.Venda.Regra.Data.dll, RM.Imb.Venda.Regra.Form.dll, RM.Imb.Venda.Calc.Lib.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll

* **[Ticket: TINPAD001-14]** Melhoria no rateio de centro de custo, somente clientes revitalizados.

Arquivos: RM.Imb.Venda.Calc.Lib.dll, RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.dll

### Rotina: TABELA DE PRECOS IMB 49 860

* **[Ticket: 555560 / MCP-1962]** O sistema passou a reajustar simultaneamente tabelas de preço com o mesmo empreendimento.

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: CONTROLE DE EXAMES AGENDA DE EXAMES SMT 36 545

* **[Ticket: 524044 / MRH-7274]** Ajuste realizado para mostrar a listagem de exames corretamente.

Arquivo: RM.Smt.Clinico.Form.dll

### Rotina: CONTROLE DE EXAMES EXAMES SMT 36 004

* **[Ticket: 618479 / MRH-8465]** Adicionada uma mensagem em caso de modificação de contexto de coligada com a visão do prontuário aberta.

Arquivo: RM.Smt.Clinico.Form.dll

# 12.1.15.133

## TOTVS Automação de Ponto

### Rotina: PARAMETROS RM PORTAL PTO 35 1218

* **[Ticket: 664256 / MRH-9085]** Alterações realizadas no processo de cancelamento de batidas do portal, para considerar o parâmetro de envio de email de cancelamento de batidas.

Arquivos: RM.Pto.Parametros.Intf.dll, RM.Pto.Batida.Data.dll

### Rotina: PROCESSO DE CALCULO DE ABONO PTO 35 1300

* **[Ticket: 665895 / MRH-9030]** Alterações no processo de lançamento global de abonos, especificamente na parte onde era definido o código do tipo do abono, onde o erro era ocasionado.

Arquivo: RM.Pto.Ocorrencia.Data.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 667669 / MRH-9071]** Alterações no processo de impressão do relatório do espelho do cartão para considerar não somente os descansos cadastrados no grupo de descanso, mas também os descansos do horário planejado do funcionário.

Arquivos: RM.Pto.Funcionario.Data.dll, RM.Pto.Relatorio.Data.dll

* **[Ticket: 471616 / MRH-8990]** Foi ajustado o filtro do relatório do espelho do cartão de modo que o mesmo seja respeitado.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Business Connect

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 668578 / EDUCACIONAL01-77]** Sistema passou a obedecer a parametrização de valores do convênio para cálculo do código de barras e IPTE via WebServices.

Arquivo: RM.Con.EducacionalWebEnsino.Data.dll

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 95522 / TINPAD001-11]** Melhoria na geração de titulos para o Protheus, o sistema passa a informar o tipo de documento correto ao Protheus para que o titulo seja gerado com o tipo pré determinado no TIN.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsIncorporacaoProtheus.dll

### Rotina: Project-692300 Erro na execução de DataServers Project-692300

* **[Ticket: 697125 / MFRWBH-1517]** Otimização do SaveRecord para o WSDataServer

Arquivo: RM.Con.Utils.dll

## TOTVS Construção e Projetos

### Rotina: COPIA DE ITENS PRJ 33 779

* **[Ticket: 667334 / TOPORCAPLAN001-64]** Ajuste na cópia de itens para possibilitar a cópia da quantidade da obra.

Arquivo: RM.Prj.Projeto.Data.dll

### Rotina: MENSAGEM UNICA PROCESSO CONTRATOS ADIANTAMENTO TITUL PRJ 33 924

* **[Ticket: 682874 / TOPEXECONTROL01-1]** O parâmetro de projeto para liberação de contrato "Considerar produtos associados no faturamento de contrato de insumos" foi substituído pelo parâmetro "Produto da Liberação (Contrato de Insumos)" com as seguintes opções: "Produtos Associados ou Default", "Produtos Associados" e "Default".Produtos Associados ou Default - Ao gerar a integração com suprimentos / faturamento o sistema exibe os insumos associados e permite informar um produto default que é utilizado para ser relacionado aos insumos que não tenha o produto principal informado.Produtos Associados - Ao gerar a integração o sistema exibe somente os insumos associados não permitindo a informação de um produto default. Neste caso o sistema orienta a forma de correção caso haja algum insumo sem produto.Produto Default - Ao gerar a integração o sistema não exibe os insumos associados e permite informar um produto default que é utilizado para relacionar a insumos que não tenha o produto principal informado.

Arquivos: RM.Prj.Parametros.Intf.dll, RM.Prj.Contrato.Data.dll, RM.Prj.Contrato.Form.dll, RM.Prj.Parametros.Form.dll

* **[Ticket: 682874 / TOPEXECONTROL01-1]** O parâmetro de projeto para liberação de contrato "Considerar produtos associados no faturamento de contrato de insumos" foi substituído pelo parâmetro "Produto da Liberação (Contrato de Insumos)" com as seguintes opções: "Produto Associado ou Default (quando não houver Produto Associado)", "Produto Associado" e "Default".Produto Associado ou Default (quando não houver Produto Associado) - Ao gerar a integração com suprimentos / faturamento o sistema exibe os insumos associados e permite informar um produto default que é utilizado para ser relacionado aos insumos que não tenha o produto principal informado.Produto Associado - Ao gerar a integração o sistema exibe somente os insumos associados não permitindo a informação de um produto default. Neste caso o sistema orienta a forma de correção caso haja algum insumo sem produto.Produto Default - Ao gerar a integração o sistema não exibe os insumos associados e obriga informar um produto default que é utilizado para relacionar a todos os insumos, substituindo os que tenham produto informado.

Arquivos: RM.Prj.Parametros.Intf.dll, RM.Prj.Contrato.Form.dll, RM.Prj.Contrato.Server.dll, RM.Prj.Parametros.Form.dll

### Rotina: PLANILHAS CRONOGRAMA PRJ 33 866

* **[Ticket: 672730 / TOPEXECONTROL01-37]** Ajuste na visão de cronograma como planilha, para que ao trocar projetos as colunas sejam atualizadas

Arquivo: RM.Prj.Cronograma.Form.dll

### Rotina: PLANILHAS - TAREFAS PRJ33872

* **[Ticket: TOPORCAPLAN001-47]** Ajuste realizado para que o toolbar de inclusão de produtos ao insumo seja exibida corretamente na primeira edição do recursos(insumos) da tarefa através do lookup

Arquivo: RM.Prj.Insumo.Form.dll

### Rotina: RELATORIOS FIXOS COMPOSICOES DO PROJETO PRJ 33 947

* **[Ticket: 668149 / TOPORCAPLAN001-12]** Ajuste realizado para que o relatório TOREL0047 seja gerado exibindo as composições auxiliares

Arquivo: RM.Prj.Composicao.Data.dll

## TOTVS Educacional

### Rotina: CENSO

* **[Ticket: EDUCACIONAL01-133]** Alterar a rotina do Censo para permitir mais de uma instituição por filial e nível de ensino

Arquivos: RM.Edu.Consts.dll, RM.Edu.Cadastros.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Utils.Server.dll, RM.Edu.Academico.Form.dll, RM.Edu.Cadastros.Data.dll, RM.Edu.Cadastros.Form.dll, RM.Edu.MatrizCurricular.Data.dll

### Rotina: GERACAO DE MOVIMENTO EDU 50 229

* **[Ticket: 575799 / EDUCACIONAL01-34]** Melhoria no processo de geração de movimento para que sejam listado os movimentos em que o campo "NF-e Estadual" (Etapa 67) esteja configurado como a opção diferente de "Não integrado".

Arquivos: RM.Edu.dll, RM.Edu.Lib.WinForms.dll

### Rotina: PORTAL PROFESSOR PLANO DE AULA EDU 50 381

* **[Ticket: 515774 / EDUCACIONAL01-49]** Ajuste no portal do professor para que no plano de aula obedeça o filtro da subturma selecionado.

Arquivo: RM.Edu.PeriodoLetivo.WebForm.dll

## TOTVS Folha de Pagamento

### Rotina: CONSULTA MOVIMENTO DA INTEGRACAO LAB 01 96

* **[Ticket: 693404 / FOPCALCULO01-77]** Ajuste na rotina de Integração RM x SAP voltando o funcionamento da forma antiga.

Arquivos: RM.Fop.Rotinas.Data.dll, RM.Fop.Rotinas.Form.dll, RM.Fop.Rotinas.Intf.dll

* **[Ticket: 693404 / FOPCALCULO01-77]** Ajuste na Integração RM x Sap

Arquivo: RM.Fop.Rotinas.Data.dll

### Rotina: CONSULTA SALDO DE COMPENSACOES LAB 01 50

* **[Ticket: 437667 / MRH-9298]** O sistema no log de cálculo da GUIA de INSS o valor da "Compensação de retenção" passa a abater o valor "Empresa". Caso o campo Empresa fique negativo será zerado.

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: CONTABILIZACAO PARAMETRIZACAO FOP 34 381

* **[Ticket: 699460 / FOPCALCULO01-8]** Ajuste geração de encargos referente ao FGTS de 13º salário.

Arquivo: RM.Fop.Dominio.dll

### Rotina: DIFERENCA SALARIAL LAB 01 109

* **[Ticket: 673465 / MRH-9288]** Ajuste na diferença salarial para não gravar valores incorretos de movimento de pensão em meses que o funcionário ficou afastado.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: FERIAS CALCULO FOP 34 402

* **[Ticket: 196042 / MRH-5664]** Ajuste no cálculo de INSS para ignorar restituição de 1 centavo no caso de lançamento de férias para o envelope.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: FOLHA ANALITICA LAB 01 112

* **[Ticket: 406507 / FOPROTINAS01-237]** Otimizado geração da folha analítica por centro de custo para respeitar o parâmetro "Filtro para centro de custo"

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: MANAD LAB 01 122

* **[Ticket: 629632 / FOPROTINAS01-381]** Retirada data de admissão quando registro de funcionário for do tipo Autônomo (conforme layout)

Arquivo: RM.Fop.Manad.Data.dll

### Rotina: Valores default na rescisão

* **[Ticket: 368028 / MRH-5549]** Utilização de valores default nos campos do cadastro de Rescisão

Arquivos: RM.Fop.Funcionario.Server.dll, RM.Fop.Rescisao.Form.dll

## TOTVS Framework

### Rotina: HOST FRW00038

* **[Ticket: MFRWBH-1512]** Foi realizada um ajuste para evitar o vazamento de memória no RMSFormView

Arquivo: RM.Lib.WinForms.dll

### Rotina: PREFERENCIAS DE ANEXOS FRW 00059

* **[Ticket: 700672 / MFRWBH-1520]** Foi realizado um ajuste na chamada da tela de perfis na visão de definição de grupos de visualização

Arquivo: RM.Glb.Seguranca.Data.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS RETROSPECTIVA CONTABIL GERENCIAL CTB 38 124

* **[Ticket: 585369 / MEDU-3104]** Ajuste no relatório Retrospectiva para que caso no intervalo de meses selecionado a conta fique zerada por exemplo a partir de um determinado mês, essa conta seja exibida para que mostre o saldo nos demais meses quando é marcado para gerar o relatório por Saldo.

Arquivo: RM.Ctb.Relatorios.Service.dll

### Rotina: RELATORIOS RETROSPECTIVA DE SALDOS CTB 38 123

* **[Ticket: 672537 / CONTROLADORIA01-57]** A coluna Centro de Custo passou a ser exibida sem cortes.

Arquivos: RM.Ctb.Relatorios.Form.dll, RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CANCELAR MOVIMENTO MOV 004

* **[Ticket: 618213 / MATFATCMPCRM01-61]** Melhoria no cancelamento de cupom fiscal vinculado a um movimento através WebService

Arquivo: RM.Mov.CupomFiscal.Service.dll

### Rotina: PROCESSO PRODUTIVO SIMPLES EST 021

* **[Ticket: 519451 / MATFATCMPCRM01-79]** Melhoria na rotina de Faturamento de Movimento.

Arquivos: RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Form.dll

## TOTVS Gestão Financeira

### Rotina: ADITIVO TROCA DE COMPRADOR IMB 49 785

* **[Ticket: 400733 / FINANCEIRO01-56]** Ajustes no serviço de finalização de lançamentos

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: FATURAS ANEXO LANCAMENTO FIN 156

* **[Ticket: 612867 / FINANCEIRO01-59]** Ajuste no processo de Inclusão de Fatura quando lançamento está vinculado a boleto com outro lançamento vinculado.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO DE PAGAMENTO FIN 238

* **[Ticket: 657767 / FINANCEIRO01-11]** Otimizado a busca pelo default do meio de pagamento em extratos de mútuo.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE CONTABILIZACAO FIN 323

* **[Ticket: 530582 / FINANCEIRO01-4]** Otimizado o sistema para recalcular o percentual do rateio caso o mesmo tenha sido salvo na base com valor 0.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NFS E CONSULTA AUTORIZACAO CANCELAMENTO NF 01 0051

* **[Ticket: 496930 / MEDU-3403]** Alteração do envio de NFS-e de Goiânia para atender a melhoria, onde existe um parâmetro que retira todos os caracteres especiais e acentuações do XML.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: \*\*\*URGENTE\*\*\* DMED

* **[Ticket: 666495 / MSAU-7036]** Ajuste para gerar DMED mesmo com o parâmetro "Não gera DMED para tipo de atendimento" estiver vazio

Arquivo: RM.Sau.Faturamento.Data.dll

### Rotina: CLASSIFICACAO DE RISCO TOTEM SAU 47 1195

* **[Ticket: 376518 / MSAU-6527]** Ao acessar o menu server existem menus que não estão na versão padrão do RM Saúde, Toten de Pronto Atendimento e Registro de Notificação de Doenças e Agravos. Alterado o menu do RM para conter o toten e o registro de notificação.

Arquivos: RM.Sau.dll, RM.Sau.RegistroAtendimento.Form.dll

### Rotina: Erro ao selecionar action no metadados

* **[Ticket: 665533 / MSAU-7176]** Ajuste para a correta seleção de metadados de AIH.

Arquivo: RM.Sau.Sus.Data.dll

## TOTVS Incorporação

### Rotina: Aditivo Prorrogação

* **[Ticket: 670859 / TINPAD001-7]** No aditivo de prorrogação da data de vencimento o sistema passou a exibir a coluna de juros de acordo conforme era apresentado na versão 11.82

Arquivo: RM.Imb.Aditivos.Form.dll

### Rotina: BAIXA - ATUALIZAÇÃO DE VALORES IMB49804

* **[Ticket: TINPAD001-13]** Melhoria no processo de reajuste, o mesmo passa a abrir o processo corretamente.

Arquivos: RM.Imb.Reajuste.Intf.dll, RM.Imb.Reajuste.Data.dll

### Rotina: Erro ao salvar o contrato

* **[Ticket: 627688 / TINPAD001-10]** Incidente: ao gerar contrato estava sendo apresentada uma mensagem de erro reportando que os valores inseridos nos campos CONF\_DIR,CONF\_ESQ,CONF\_FUN excedia o tamanho máximo permitido. Porém os valores informados possuíam 200 caracteres, exatamente o máximo permitido no banco de dados para este campo.Solução: Foi verificado que para gerar o contrato este campo estava configurado para aceitar no máximo 35 caracteres, o que ocasionava o erro. O campo foi modificado para aceitar no máximo 200 caracteres.

Arquivo: RM.Imb.Contratos.Intf.dll

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 631232 / TINPAD001-19]** Melhoria de performance no processo de exclusão de plano de financiamento.

Arquivo: RM.Imb.Log.Server.dll

### Rotina: Minha casa minha vida

* **[Ticket: 608711 / TINPAD001-36]** Removido código que copiava o número do contrato para a coluna FORMULACODIGO

Arquivo: RM.Imb.Aditivos.Form.dll

### Rotina: REAJUSTE

* **[Ticket: TINPAD001-46]** Ajuste Implementação Antecipação PRICE

Arquivos: RM.Imb.Reajuste.Intf.dll, RM.Imb.Reajuste.Server.dll, RM.Imb.Reajuste.Data.dll

## TOTVS Processo Seletivo

### Rotina: AGENDAMENTOS EDUPS 20 1004

* **[Ticket: 642707 / MEDU-3388]** Ajuste no cancelamento e exclusão de inscrições do processo seletivo.

Arquivo: RM.EduPS.Inscricoes.Server.dll

# 12.1.15.134

## TOTVS Educacional

### Rotina: PADRAO

* **[Ticket: EDUCACIONAL01-16]** Ajustes no processo de mudança de turno/turma

Arquivo: RM.Edu.Matricula.Server.dll

## TOTVS Folha de Pagamento

### Rotina: RM REPORTS LAB 01 188

* **[Ticket: 476616 / MRH-8138]** Ajuste no parâmetro de chaves ativas para envelope de pagamento do portal

Arquivo: RM.Fop.Parametros.Form.dll

### Rotina: SECOES VALORES ASSOCIADOS LAB 01 231

* **[Ticket: 662857 / FOPROTINAS01-9]** Liberação da rotina de Reestruturação de Seção

Arquivos: RM.FopFolha.dll, RM.Fop.Secao.Form.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS RAZAO CTB 38 114

* **[Ticket: 707372 / MEDU-3426]** Ajuste na consulta que busca o saldo anterior para que considere corretamente os valores das contabilidades de baixa do antigo modelo de baixa (Baixa Antiga).

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO EMISSAO RECEBIMENTO DE CHEQUES FIN 197

* **[Ticket: 691377 / FINANCEIRO01-88]** Otimizado o sistema para guardar corretamente o valor do cheque no lançamento. Gerado script corretivo para os lançamentos na base do cliente.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 644312 / MEDU-3304]** Alteração no envio da NFS-e, permitindo que seja enviado a nota contendo o tributo ISS com base de calculo zerada.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

## TOTVS Incorporação

### Rotina: DIMOB

* **[Ticket: 499155 / TINPAD001-30]** Incidente:Ao gerar a DIMOB com o parâmetro "gerar um arquivo por parceiro de acordo com o repasse" marcado, estavam sendo gerados vários arquivos, porém alguns deles não possuíam registros de venda pelo fato de não haver venda para o ano em que a DIMOB foi gerada.Solução: O processo da DIMOB foi modificado para gerar o arquivo para cada empreendimento/parceiro somente quando houver vendas para o ano em questão.

Arquivo: RM.Imb.DIMOB.Server.dll

# 12.1.15.135

## TOTVS Automação de Ponto

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 659375 / MRH-9104]** Ajuste realizado na definição de natureza da batida para o horário semi-flexível

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** SGBD: ORACLE/SQL SERVERManutenção do bloco dividindo o mesmo em blocos de 1000 inserts.Chamado: MGCADBH-134/\*$Versao=CP.2016.07\_05\*//\*IGOR MARANI ALVES - CP.2016.07\_05 - OC.:TSLELB - 22/08/2016 VERSAO.: 12.1.13 - EQUIPE:MANUT \*/Script: /\*LEONARDO MONTEIRO DOS SANTOS - CN.2016.12\_03 - OC.:MEDU-1489 - 05/01/2017 VERSAO.: 12.1.15 - EQUIPE:MANUT \*/ISSUE: MGCADBH-142Descrição: Correção do tipo de dado das colunas ESPECIALFUNDEJA, SISRESPREGULACAO, ESCOLASEDEVINCULADA e IESVINCULADA da table SINSTITUICAOMECScript: /\*WESLEY MAGNO DE OLIVEIRA COSTA - FS.2015.09\_02 - OC.:TTEESG - 21/09/2015 VERSAO.: 12.1.8 - EQUIPE:MANUT \*/Chamado: MGCADBH-141Descrição: Inclusão de update para registros da tabela FLANBAIXA com mais de 6 dígitos a esquerda evitando erro ao executar o comando ALTER TABLE FLANBAIXA ALTER COLUMN COTACAOBAIXA NUMERIC(15,9) NULLCHAMADO: MGCADBH-137JUSTIFICATIVA: Quando tenta realizar a conversão em uma instância com mais de um schema é retornado um erro de ORA-01422: exact fetch returns more than requested number of rows, sendo assim foi reavaliado a tratativa para verificar o esquema correto.

Arquivos: Cvn.12.1.13.sql, Cvn.12.1.15.sql

## TOTVS Business Connect

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 702068 / MFRWBH-1538]** Melhoria na conversão das informações recebidas via web service em DataSet para manipulação e utilização nos Data Servers do RM.

Arquivo: RM.Con.Utils.dll

## TOTVS Construção e Projetos

### Rotina: RELATORIOS FIXOS MEDICAO COMPLETA PRJ 33 951

* **[Ticket: 715270 / TOPEXECONTROL01-65]** Ajuste realizado onde foii criado uma função de fórmula que irá retornar o valor medido substituindo o recalculo do mesmo no relatório

Arquivo: RM.Prj.Formula.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: Erro ao importar Internação/Alta

* **[Ticket: 670248 / MSAU-7129]** Ajuste para a importação dos dados do paciente conforme padrão da view disponibilizado no TDN

Arquivo: RM.SauIH.Importacao.Data.dll

### Rotina: Falha de BI - Perfil de Sensibilidade

* **[Ticket: 644556 / MSAU-6725]** Ajuste para que a coluna de Multirresistência seja listada com sucesso no BI de Perfil de Sensibilidade

Arquivo: RM.SauIH.Utils.Intf.dll

## TOTVS Educacional

### Rotina: ATUALIZA PARCELAS DO CONTRATO EDU 50 050

* **[Ticket: 707492 / EDUCACIONAL01-56]** Melhoria no processo de atualização das parcelas do contrato para que sempre que o usuário selecionar o campo “Valor do desconto” automaticamente o sistema selecionara o campo “Tipo de desconto” ou vice versa, garantindo assim que as duas informações fiquem atualizadas, pois uma impacta diretamente na outra’.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: CADASTRO

* **[Ticket: EDUCACIONAL01-48]** Criação de um parâmetro interno para apresentação do item de menu Filho Sem Fila no executável.

Arquivos: RM.Lib.Params.Wizard.xml, RM.Edu.Consts.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Parametros.Intf.dll, RM.Edu.PeriodoLetivo.Form.dll, RM.Edu.Server.dll, RM.Edu.Utils.Server.dll, RM.Edu.dll, RM.Edu.Integracoes.Form.dll, RM.Edu.Integracoes.Server.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Integracoes.Data.dll

### Rotina: PORTAL ALUNO MATRICULA ONLINE EDU 50 356

* **[Ticket: 671416 / EDUCACIONAL01-65]** Foi realizada otimização do processo de geração de lançamentos, permitindo ao sistema, concluir a alteração na matrícula, através do portal, nos casos onde as alterações realizadas tentar gerar lançamentos para as parcelas que já tenham seus lançamentos gerados e baixados.

Arquivos: RM.Edu.Matricula.Server.dll, RM.Edu.Matricula.Data.dll, RM.Edu.Consts.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Financeiro.Server.dll

### Rotina: PORTAL - ALUNO - QUADRO DE AVISOS EDU50364

* **[Ticket: 95452 / PORTALMOBILE01-104]** Ajuste para filtrar corretamente as disciplinas no quadro de aviso de acordo com parametrização da situação de matrícula informada.

Arquivo: RM.Edu.NotaFalta.Data.dll

### Rotina: PORTAL PROFESSOR UPLOAD MATERIAIS EDU 50 386

* **[Ticket: 650772 / PORTALMOBILE01-116]** Ajuste na visualização dos arquivos por disciplina no portal, exibindo também os arquivos das turmas/disciplinas que o aluno esteja matriculado em outra filial.

Arquivos: RM.Edu.Materiais.Data.dll, RM.Edu.Materiais.WebForm.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 648886 / EDUCACIONAL01-52]** Correção na geração de dados do Censo para buscar informações de FIES

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.Academico.Form.dll, RM.Edu.Academico.Server.dll, RM.Edu.Academico.Data.dll

* **[Ticket: 696690 / EDUCACIONAL01-4]** Correção na verificação de grade sem carga horária para não trazer grades de outras filiais.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: Project-715165 CENSO - Professores que deveriam aparecer no arquivo não aparecem. Project-715165

* **[Ticket: 717774 / EDUCACIONAL01-67]** Melhoria no processo de atualização das parcelas do contrato para que sempre que o usuário selecionar o campo “Valor do desconto” automaticamente o sistema selecionara o campo “Tipo de desconto” ou vice versa, garantindo assim que as duas informações fiquem atualizadas, pois uma impacta diretamente na outra’.

Arquivos: RM.Edu.Financeiro.Server.dll, RM.Edu.Financeiro.Form.dll

## TOTVS Folha de Pagamento

### Rotina: EVENTOS LAB 01 83

* **[Ticket: 510758 / MRH-8623]** Ajuste na proporcionalização da engenharia reversa no meses de afastamento para considerar na divisão somente os dias efetivamente trabalhados pelo funcionário.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: FORMULAS NET FOP 34 528

* **[Ticket: 722885 / FOPCALCULO01-149]** Corrigido o problema e o funcionário esta salvando normalmente.

Arquivo: RM.Fop.Funcionario.Form.dll

### Rotina: GRUPO DE EVENTOS ASSISTENTE NET FOP 34 510

* **[Ticket: 516892 / FOPROTINAS01-256]** Ajuste no wizard de Reprogramação Salarial

Arquivo: RM.Fop.Educacional.Form.dll

### Rotina: O sistema não considera o bloqueio do campo salário disponível na tela de quadro de vagas (cálculo) no menu de orçamento

* **[Ticket: 315322 / MRH-4207]** Realizando validação do campo de salário no cadastro do orçamento de acordo com o filtro por perfil.

Arquivos: RM.Fop.Orcamento.Intf.dll, RM.Fop.Orcamento.Data.dll, RM.Fop.Orcamento.Form.dll

### Rotina: O sistema não considera o filtro por usuário para demonstrar informações de funcionários apenas da seção informada no ca

* **[Ticket: 327165 / MRH-4208]** Realizando validação do filtro por perfil no cadastro de seção.

Arquivo: RM.Fop.Secao.Data.dll

### Rotina: Valores default na rescisão

* **[Ticket: 368028 / MRH-5549]** Utilização de valores default nos campos do cadastro de Rescisão

Arquivo: RM.Fop.Rescisao.Form.dll

## TOTVS Framework

### Rotina: FERIAS CADASTRO FOP 34 538

* **[Ticket: 554207 / MFRWBH-1529]** Melhoria na execução de sentença sql na segurança estendida

Arquivo: RM.Lib.Data.dll

### Rotina: FOLHA ANALITICA LAB 01 112

* **[Ticket: 691279 / MFRWBH-1509]** Diminuição no Comsumo do Host (Folha Analítica)

Arquivos: RM.Lib.dll, RM.Lib.Server.dll, RM.Lib.WinForms.dll, RM.Rpt.Executor.Service.dll

### Rotina: OUTROS

* **[Ticket: MFRWBH-1349]** Melhoria no servidor de Jobs para Job Recorrente

Arquivo: RM.Lib.Data.dll

### Rotina: PERFIS FRW 00055

* **[Ticket: 561112 / MFRWBH-1320]** Melhoria na opção de Associar/Retirar perfil de todas as coligadas no cadastro do usuário

Arquivo: RM.Glb.Seguranca.Form.dll

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: 709683 / MFRWBH-1543]** O DataServer GlbLoginData foi decorado com o atributo de segurança.

Arquivo: RM.Glb.Cadastros.Data.dll

## TOTVS Gerador de Relatórios

### Rotina: RELATORIO

* **[Ticket: MFRWBH-1548]** A opção de Tornar Bandas Invisíveis está disponível.

Arquivos: RM.Rpt.Executor.Intf.dll, RM.Rpt.Executor.IService.dll, RM.Rpt.Executor.Service.dll, RM.Rpt.Executor.Client.dll

### Rotina: RELATORIO CADASTRO REL 00013

* **[Ticket: 697551 / MFRWBH-1534]** Foi realizado um ajuste na parte de segurança onde ao tentar abrir a visão será Delphi, será verificado se o usuário possúi permissão ao gerador de relatórios por módulo ou se ele é supervisor. Na visão .Net também será feita a validação onde só serão exibidos os módulos que o usuário possui permissão ao gerador de relatórios ou os que ele é supervisor.

Arquivo: RM.Rpt.Reports.Data.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS RAZAO CTB 38 114

* **[Ticket: 547461 / MEDU-3416]** Ajuste na consulta de saldo anterior do relatório por cliente/fornecedor para pegar o valor das partidas através da tabela CCONT para que a consulta não agrupe o valor pela ORIGEM/CPARTIDA causando a duplicação de valores em alguns casos específicos.

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E INCONSISTENCIA CTE 002

* **[Ticket: 645614 / MATFATCMPCRM01-20]** Implementação da tag autXML

Arquivo: RM.Mov.CTe.Service.dll

### Rotina: GERAR ORDEM DE COMPRA COTACAO COM 010

* **[Ticket: 380456 / MATFATCMPCRM01-40]** Melhoria no processo de gerar ordem de comprar a partir de uma cotação

Arquivo: RM.Cmp.OrdemCompra.Form.dll

### Rotina: MOVIMENTOS

* **[Ticket: MATFATCMPCRM01-234]** Melhoria na impressão de movimento

Arquivos: RM.Mov.Movimento.Service.dll, RM.Mov.Processos.Form.dll

### Rotina: NOTAS FISCAIS

* **[Ticket: MATFATCMPCRM01-166]** Foi criado um novo parâmetro no sistema com o objetivo de definir se os caracteres especiais e acentuações devem ser mantidos no XML da Nota Fiscal (Estadual e Municipal).

Arquivos: RM.Mov.Parametros.Intf.dll, RM.Mov.Parametros.Data.dll, RM.Mov.Parametros.Form.dll

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: 444649 / MATFATCMPCRM01-129]** Melhoria na Importação de XML de CT-e (Compra) para preenchimento do Histórico do movimento

Arquivos: RM.Mov.Integracoes.Form.dll, RM.Mov.Integracoes.Service.dll

* **[Ticket: 444649 / MATFATCMPCRM01-129]** Melhoria na Importação de XML de CT-e (Compra) para preenchimento do Histórico do movimento

Arquivo: RM.Mov.Integracoes.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: ENTIDADES RHU 36 032

* **[Ticket: 586115 / MRH-8090]** Ajuste ao utilizar máscara de telefone com digito flutuante

Arquivo: RM.Rhu.Cadastros.Data.dll

### Rotina: EXTERNO RHU 36 034

* **[Ticket: 338637 / MRH-4385]** Correção permitindo realizar filtro com Descrição perfil profissional

Arquivo: RM.Rhu.Pessoa.Data.dll

### Rotina: FUNCIONARIOS RHU 36 035

* **[Ticket: 390655 / MRH-5292]** Ajuste ao salvar participantes duplicados na avaliação de desempenho

Arquivo: RM.Rhu.Lib.WinForms.dll

## TOTVS Gestão Financeira

### Rotina: EXTRATO DE CAIXA REGERAR CONTABILIZACAO FIN 152

* **[Ticket: 587825 / FINANCEIRO01-115]** Não apresentar erro "Não foi possível validar CPF/CNPJ - Campo "Categoria" do Emitente deve ser preenchido." ao tentar alterar um extrato proveniente de uma baixa com o meio de pagamento cheque

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 708287 / MEDU-3445]** Geração do drawback na nota fiscal eletrônica, onde não existe nota referenciada.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 722173 / MEDU-3462]** Ajuste para que quando o Código da Obra estiver nulo não gere:Erro: Referência de objeto não definida para uma instância de um objeto

Arquivo: RM.Fis.Facade.dll

## TOTVS Gestão Hospitalar

### Rotina: CLASSIFICACAO DE RISCO FILAS DE ATENDIMENTO SAU 47 1198

* **[Ticket: 680369 / MSAU-7295]** Ao clicar no botão "Chamar" na aba de "Atendimento Médico", o sistema irá efetuar a chamada de acordo com a ordem de urgência

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

### Rotina: Problema de prioridade na chamada de pacientes sem classificação de risco.

* **[Ticket: 691028 / MSAU-7305]** Ao clicar no botão "Chamar" na aba de "Atendimento Médico", o sistema irá efetuar a chamada de acordo com a ordem de urgência

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

### Rotina: RÉPLICA para 12.1.16 - Lentidão no processo de faturamento

* **[Ticket: MSAU-4911]** Ajuste na performance da rotina de faturmento para convênios.

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: RM - Ajuste no arquivo ACH para campos com preenchimento "zero"

* **[Ticket: 664166 / MSAU-7067]** Para AIH inicial, o sistema lançará no arquivo o número "0"

Arquivo: RM.Sau.Sus.Server.dll

## TOTVS Incorporação

### Rotina: Arquitetura do Reajuste Revitalizado

* **[Ticket: TINREV001-1]** Melhoria para o utilitários.

Arquivos: RM.Imb.Conversor.Data.dll, RM.Imb.Conversor.Server.dll

* **[Ticket: TINREV001-1]** Melhoria no processo de geração de plano de financiamento, somente clientes revitalizados.

Arquivos: RM.Imb.Venda.Resources.dll, RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Regra.Intf.dll, RM.Imb.Venda.Calc.Calculos.dll, RM.Imb.Venda.Calc.CalculosBase.Controller.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Venda.Regra.Data.dll, RM.Imb.Venda.Regra.Form.dll

### Rotina: FORMULA VISUAL IMB 49 876

* **[Ticket: 518960 / TINPAD001-21]** Incidente: Foi verificado que a fórmula visual não estava funcionando corretamente devido à ausência de um parâmetro que a mesma esperava (NumeroTabelaPreco)Solução: O processo de efetivar tabela de preço foi modificado para retornar o número da tabela de preço

Arquivo: RM.Imb.Venda.Lib.Intf.dll

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: TINPAD001-73]** Melhoria nos processos de geração e exclusão de plano de financiamento.

Arquivo: RM.Imb.Log.Server.dll

### Rotina: Minha casa minha vida

* **[Ticket: 608711 / TINPAD001-36]** Melhoria no plano de financiamento MCMV, somente clientes revitalizados.

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Conversor.Data.dll, RM.Imb.Conversor.Server.dll, RM.Imb.Relatorio.Form.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll

### Rotina: PORTAL DE VENDAS IMOBILIARIO PVI IMB 49 875

* **[Ticket: 672602 / TINPAD001-71]** Incidente:Ao tentar gerar uma proposta no PVI estava sendo exibida a mensagem "Você não está autorizado a utilizar esta funcionalidade do sistema". Foi identificado que esta mensagem estava sendo exibida devido a falta de permissão em um recurso do RM utilizado pelo PVISolução: Foi criada no RM uma tag de segurança para realizar o controle de acesso deste recursoTexto no menu: Simulador de Propostas PVI

Arquivos: RM.Imb.dll, RM.Imb.Server.dll

## TOTVS Planejamento e Controle da Produção

### Rotina: EMPRENHO PCP 44 284

* **[Ticket: 538632 / MATESTCNTFTOF01-5]** Melhoria para listar materiais com saldo de estoque zerado tela de empenho de acordo com a Flag criada.

Arquivos: RM.PCP.Empenho.Form.dll, RM.PCP.Empenho.Service.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: RELATORIOS PERFIL PROFISSIOGRAFICO PREVIDENCIARIO PPP SMT 36 578

* **[Ticket: 672193 / RHU01-3]** Reparo ao emitir PPP com funcionário sem locais de trabalho

Arquivo: RM.Smt.Relatorio.Data.dll

# 12.1.15.136

## TOTVS Automação de Ponto

### Rotina: ALTERACOES GLOBAIS CARTAO DE PONTO PTO 35 1288

* **[Ticket: 464517 / MRH-6442]** Foi realizado o ajuste para que a verificação do período de utilização de cartão de ponto fique correta e evite cálculo de faltas incorretamente para períodos anteriores a utilização do ponto.

Arquivo: RM.Pto.Funcionario.Data.dll

* **[Ticket: 464517 / MRH-6442]** Foi realizado o ajuste para que a verificação do período de utilização de cartão de ponto fique correta e evite cálculo de faltas incorretamente para períodos anteriores a utilização do ponto.

Arquivos: RM.Pto.Contexto.Server.dll, RM.Pto.Funcionario.Data.dll, RM.Pto.Utils.Server.dll, RM.Pto.ImportacaoExportacao.Data.dll, RM.Pto.Relatorio.Data.dll

## TOTVS Business Connect

### Rotina: GERAL

* **[Ticket: MFRWBH-1559]** O ws ServiceInfo foi criado.

Arquivo: RM.Con.Conector.Service.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 674700 / EDUCACIONAL01-10]** Otimização do webservice WsDataServer

Arquivo: RM.Con.Conector.Server.dll

### Rotina: RM X ECM GED SINCRONISMO DE USUARIO INT 00010

* **[Ticket: 615794 / MFRWBH-1374]** Melhoria no log do processo Sincronizar usuários do Corpore com o GED

Arquivos: RM.Con.Localizacao.dll, RM.Con.GED.Server.dll

## TOTVS Construção e Projetos

### Rotina: PLANILHAS IMPORTAR CRONOGRAMA VIA EXCEL PRJ 33 869

* **[Ticket: 714657 / TOPORCAPLAN001-90]** Erro na importação de arquivo excel

Arquivo: RM.Prj.Cronograma.Data.dll

### Rotina: PROJETO

* **[Ticket: TOPORCAPLAN001-85]** Ajuste realizado para que o processo Especializar Insumo seja executado também através da tela de edição do insumo

Arquivos: RM.Prj.Insumo.Intf.dll, RM.Prj.Insumo.Data.dll, RM.Prj.Insumo.Form.dll

### Rotina: TIMESHEET EQUIPE DE TIMESHEET PRJ 33 798

* **[Ticket: 732272 / TOPEXECONTROL01-77]** Ajuste no cadastro de equipe de gestão de risco e mobilidade.

Arquivo: RM.Prj.EquipeProjeto.Data.dll

## TOTVS Educacional

### Rotina: ATIVIDADES CURRICULARES EDU 50 043

* **[Ticket: 719613 / EDUCACIONAL01-90]** Ajuste ao salvar a atividade curricular do aluno para que seja salvo o campo Local também caso possua digitado algum valor no cadastro do aluno | anexos Curso / habilitação | Anexos | Atividades Curriculares.

Arquivo: RM.Edu.AtvCurricular.Data.dll

### Rotina: CAMPOS COMPLEMENTARES TURMA DISCIPLINA EDU 50 109

* **[Ticket: 620134 / EDUCACIONAL01-91]** Ajuste no processo de geração de turma/disciplina para que seja criado o registro de campos complementares.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

### Rotina: Piloto Cetec

* **[Ticket: 580554 / EDUCTB001-538]** Ajuste na integração Totvs Educacional x Backoffice Protheus (Financeiro).

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: PORTAL ALUNO EXTRATO FINANCEIRO EDU 50 353

* **[Ticket: 705958 / PORTALMOBILE01-93]** Correção no download do boleto no navegador Google Chrome.

Arquivo: App\_Web\_eduboletodotnetviswebform.aspx.dc12fd66.dll

### Rotina: Project-709220 Análise de demanda após validação de entrega do ticket 546236 Project-709220

* **[Ticket: 712618 / EDUCACIONAL01-55]** Foi realizada otimização da funcionalidade de exclusão de registro de aprovação de freqüência, através do webservice wsDataServer,de forma que o sistema consiga carregar o registro e excluí-lo com sucesso.

Arquivo: RM.Edu.NotaFalta.Intf.dll

### Rotina: Project-714344 CENSO - Arquivo não reflete alteração de naturalidade no cadastro do professor Project-714344

* **[Ticket: 717702 / EDUCACIONAL01-66]** -Ao gerar o arquivo do censo correspondente a "Censup - Censo da Educação Superior - Docente - Registro 31 - 32", o sistema não estava gerando as informações correspondente ao professor em quea data de término esteja sem preencher (informações do professor vinculado a turma/disciplina).-Ao gerar o arquivo do censo correspondente a "Censup - Censo da Educação Superior - Docente - Registro 31 - 32", o sistema não estava considerando as informações do campo "Naturalidade" e sim "Cidade".Realizamos um ajuste para considerar o campo "Naturalidade".

Arquivo: RM.Edu.Academico.Server.dll

## TOTVS Folha de Pagamento

### Rotina: ALTERACOES GLOBAIS ALTERACAO CAMPOS DO CADASTRO LAB 01 1

* **[Ticket: 734234 / FOPCALCULO01-32]** Ajuste na rotina quando alteração diz respeito à PFHSTFCO, atribuindo valor nulo quando não possui código da faixa salarial e/ou código nível salarial.

Arquivo: RM.Fop.Rotinas.Data.dll

### Rotina: FUNCIONARIOS CADASTRO LAB 01 128

* **[Ticket: 689499 / MRH-9357]** Ajuste ao recuperar valor de jornada no banco de dados que foi salva com valor null de forma errada. Sistema trata como valor zero.

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: FUNCIONARIOS GERAR RELATORIOS DE FERIAS LAB 01 145

* **[Ticket: 406696 / MRH-7794]** Criação do método GetFuncaoDIADIRFER, para ser chamado da fórmula executada em Deplhi.

Arquivos: RM.Fop.Integracao.Intf.dll, RM.Fop.Interop.Intf.dll, RM.Fop.Calc.Integracao.dll, RM.Fop.Integracao.Services.dll, RM.Fop.Interop.Data.dll, RM.Fop.Interop.Form.dll

### Rotina: IMPORTACAO DE DADOS DO RM LABORE LAB 01 26

* **[Ticket: 653340 / MRH-9261]** Ajustes de inconsistência na importação de campos complementares do funcionário

Arquivo: RM.Fop.Importacao.Data.dll

### Rotina: LANCAMENTOS FINANCEIROS PARAMETRIZACAO FOP 34 383

* **[Ticket: 712598 / FOPROTINAS01-28]** Correção na integração financeira RM x Backoffice Protheus

Arquivos: RM.Fop.TotvsMessage.OutrosBackoffices.Intf.dll, RM.Fop.Facade.dll, RM.Fop.TotvsMessage.OutrosBackoffices.Services.dll

### Rotina: LOCALIZACAO FRW 00045

* **[Ticket: 679885 / FOPROTINAS01-8]** Ajuste no portal para traduzir o campo 'Carregar detalhes dos subordinados (mais lento)'. Verificado que os demais campos desse ticket estava faltando tradução no processo de Traduzir do sistema.

Arquivos: Portal Corpore.Net

### Rotina: MANAD LAB 01 122

* **[Ticket: 717116 / MRH-9445]** Ajuste no processo de geração do Manad para não preencher o campo Data de Admissão para funcionários autonomos quando a opção 'Utiliza mais de um vínculo nas transferências' estiver marcada.

Arquivo: RM.Fop.Manad.Data.dll

### Rotina: PARAMETRIZADOR FOLHA DE PAGAMENTO LAB 01 36

* **[Ticket: 656652 / FOPROTINAS01-203]** Ajuste no cálculo do orçamento para considerar os dados do funcionário na lotação na hora de fazer a seleção para lançamento do grupo de eventos

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Calc.Integracao.dll

### Rotina: RESCISAO CADASTRO DE RESCISAO FOP 34 400

* **[Ticket: 721837 / FOPCALCULO01-17]** Ajuste na tela de rescisão de funcionário

Arquivo: RM.Fop.Rescisao.Form.dll

* **[Ticket: 721837 / FOPCALCULO01-17]** Ajuste na tela de rescisão de funcionário

Arquivo: RM.Fop.Rescisao.Form.dll

## TOTVS Framework

### Rotina: LOGIN FWB 00011

* **[Ticket: 565696 / MFRWBH-1555]** Durante a alteração de senha no próximo login utilizando a integração LDAP, o sistema tem que validar corretamente as senhas informadas antes de realizar a alteração para a nova senha.

Arquivo: RM.Lib.Server.dll

## TOTVS Gestão Contábil

### Rotina: Melhoria no Lookup de Demonstrações da tela do SPED Contábil

* **[Ticket: MEDU-3472]** Melhoria no lookup de Demonstrações Contábeis da tela de processo de geração do arquivo da ECD (SPEED Contábil) para que seja apresentado somente as demonstrações da coligada corrente.

Arquivo: RM.Ctb.Sped.Form.dll

### Rotina: RELATORIOS BALANCETE CTB 38 113

* **[Ticket: 170672 / CONTROLADORIA01-58]** O dígito verificador passou a compor as contas analíticas, contábeis e gerenciais, exibidas pelos relatórios fixos do módulo contábil. Vale ressaltar que o parâmetro de sistema ‘Usa dígito verificador’ deve estar marcado.

Arquivos: RM.Ctb.Relatorios.IService.dll, RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CORRIGIR MOVIMENTOS TRIBUTOS ULT 003

* **[Ticket: 518218 / MATFATCMPCRM01-233]** Melhoria na execução do processo de Corrigir Tipo de Movimentos -Tributos

Arquivo: RM.Mov.Processos.Data.dll

### Rotina: IMPORTACAO DE PRODUTO PRD 004

* **[Ticket: 623652 / MATESTCNTFTOF01-26]** Melhoria na rotina de importação de produto layout versão 03.

Arquivo: RM.Est.Produto.Service.dll

### Rotina: NATUREZA ORCAMENTARIA FINANCEIRA ORC 011

* **[Ticket: 688136 / MATFATCMPCRM01-190]** Melhorias no processo responsável por copiar natureza orçamentária financeira entre coligadas.

Arquivo: RM.Mov.Processos.Data.dll

### Rotina: PROCESSOS DE RESSUPRIMENTO EST 018

* **[Ticket: 657796 / MATESTCNTFTOF01-132]** Melhoria no processamento de ressuprimento

Arquivo: RM.Est.Ressuprimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 590403 / MRH-8139]** Ajuste ao abrir avaliação de desempenho com escalas francionadas

Arquivo: App\_Web\_rhuavaliacaodesempenhoexecucao.ascx.246e283e.dll

## TOTVS Gestão Financeira

### Rotina: Piloto Cetec

* **[Ticket: 580554 / EDUCTB001-538]** Ajuste na integração Totvs Educacional x Backoffice Protheus (Financeiro).

Arquivos: RM.Fin.Lan.Service.dll, RM.Edu.Financeiro.Server.dll

### Rotina: RELATORIO FLUXO DE CAIXA FIN 230

* **[Ticket: 493914 / FINANCEIRO01-120]** Otimização no processo de emitir o relatório de Fluxo de Caixa. Agora o sistema não busca o saldo disponível da aplicação financeira caso o mesmo não tenha movimentação.

Arquivo: RM.Fin.FluxoCaixa.Data.dll

## TOTVS Gestão Fiscal

### Rotina: GERAR ARQUIVO

* **[Ticket: FISCAL01-6]** Foi criada uma consistência na geração da Rotina ICMS 115/03 para que seja exigida a execução dos Scripts de marcação "LI.2017.02\_01" e "LI.2017.04\_01". Essa consistência será criada nas versões 12.1.14, 12.1.15 e 12.1.16. Na versão 12.1.17 a execução desses Scritps já se encontra no Atualizador da Base de Dados.

Arquivo: RM.Fis.RotinasFiscais.Form.dll

### Rotina: OBRIGACOES ACESSORIAS MUNICIPAIS LI 01 0034

* **[Ticket: 479182 / MEDU-2623]** Ajuste na Geração da Rotina SIMPLISS para geração correta do campo 8 conforme layout

Arquivo: RM.Fis.Sped.Server.dll

## TOTVS Gestão Hospitalar

### Rotina: ELABORACAO DE AIHS SAU 47 1144

* **[Ticket: 681575 / MSAU-7156]** Ajustes na tela de Registro da AIH

Arquivo: RM.Sau.Sus.Form.dll

### Rotina: EMISSAO DE FATURAS SAU 47 1148

* **[Ticket: 198699 / MSAU-7217]** Realizado ajuste para informar a unidade de medida no arquivo de faturamento do IPERGS quando o convênio possuir uma tabela de MATMED especial

Arquivos: RM.Sau.Faturamento.Intf.dll, RM.Sau.Faturamento.Server.dll

### Rotina: NAO IMPRMIR PRESCISAO DE RN

* **[Ticket: 682151 / MSAU-7182]** Sistema não está permitindo imprimir a prescrição do RN cadastrado.

Arquivo: RM.Sau.RegistroAtendimento.Data.dll

## TOTVS Gestão Patrimonial

### Rotina: RELATORIOS CONTABILIZACAO PAT 37 57

* **[Ticket: 351055 / CONTROLADORIA01-60]** Atualização da rotida de emissão do relatório contábil por filial visível para todas as coligadas.

Arquivo: RM.Pat.Relatorio.Data.dll

## TOTVS Incorporação

### Rotina: aviso sistema

* **[Ticket: 544470 / TINPAD001-34]** Incidente: Ao editar um componente principal PRICE de uma venda o sistema estava apresentando uma mensagem dizendo que não era possível concluir a edição pois já havia um componente de juros inserido.Solução: Esta validação foi modificada para ocorrer somente se:- Usuário incluir um componente com modelo de cálculo diferente do já inserido- Usuário alterar o modelo de cálculo do componente principal de PADRÃO para um componente de juros pré fixado- Grupo possuir dois componentes prinacipais com o mesmo modelo de cálculo e o usuário tentar alterar um dos modelos de cálculo

Arquivos: RM.Imb.Venda.Regra.Data.dll, RM.Imb.Venda.Regra.Form.dll

# 12.1.15.137

## CORPORE RM

### Rotina: FILTRO FWB 00010

* **[Ticket: 623216 / MFRWBH-1532]** -A criação de filtros de usuário para a gestão de conteúdos será realizada através da MDI.

Arquivo: RM.Prt.Cadastros.Form.dll

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB ABONAR ATRASOS E FALTAS PTO 35 1257

* **[Ticket: 433306 / MRH-9252]** Ajuste realizado no acesso ao item de solicitação de abono no portal.

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Business Connect

### Rotina: CONCEITO IMPORTACAO EXPORTACAO CON 11

* **[Ticket: 682915 / MFRWBH-1563]** -O novo conceito deve utilizar o filtro selecionado pelo usuário normalmente.-OBS.: é necessário refazer as operações de lookup e atulizar os novos valores nas ligações de dados.

Arquivos: RM.Con.Concept.dll, RM.Con.Concept.Form.dll

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 95522 / TINPAD001-11]** Melhoria na solicitação de geração das parcelas do TIN para o backoffice Protheus. O RM (TIN) passa a enviar o tipo de documento para a gerção dos titulos correspondentes no Protheus.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsIncorporacaoProtheus.dll

## TOTVS Construção e Projetos

### Rotina: PROJETO REVISAO MULTIPLA PRJ 33 879

* **[Ticket: 631345 / TOPORCAPLAN001-1]** Foi realizado um ajuste na revisão multipla quando o projeto a ser revisado, possui um projeto vinculado. Nesse caso o projeto vinculado precisa seguir a mesma fase do projeto principal, ressalva a alteração de escopo.

Arquivos: RM.Prj.Projeto.Intf.dll, RM.Prj.Projeto.Data.dll, RM.Prj.Projeto.Form.dll, RM.Prj.Planilhas.Data.dll

## TOTVS Educacional

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 708733 / EDUCACIONAL01-75]** Alteração na tela de Curso do MEC para mostrar o campo de Licenciatura.

Arquivo: RM.Edu.MatrizCurricular.Form.dll

## TOTVS Folha de Pagamento

### Rotina: RESCISAO CADASTRO DE RESCISAO FOP 34 400

* **[Ticket: 721837 / FOPCALCULO01-17]** Ajuste na tela de rescisão de funcionário

Arquivo: RM.Fop.Rescisao.Form.dll

## TOTVS Gerador de Relatórios

### Rotina: ARVORE DO RELATORIO RPT 00037

* **[Ticket: 687616 / MFRWBH-1565]** O sistema não mais repete a informação do primeiro registro no texto rico.

Arquivo: RM.Rpt.Lib.dll

## TOTVS Gestão Contábil

### Rotina: CENTRO CUSTO CTBR440

* **[Ticket: CONTROLADORIA01-62]** Melhoria no processo de gravação de máscara de centro de custo.

Arquivo: RM.Ctb.Parametros.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: REQUISICOES TRANSFERENCIA COM ALTERACAO DE DADOS FUNCIONAIS RHU 36 507

* **[Ticket: 662580 / MRH-8996]** Realizado ajuste na segurança de campos do campo Salário em Requisição de Transferência com Alteração de Dados Funcionais.

Arquivo: App\_Web\_rhureqtransfpromocao.ascx.5b96ec5.dll

## TOTVS Gestão Fiscal

### Rotina: NF E IMPRESSAO DE DANFE NF 01 0001

* **[Ticket: 544284 / MEDU-3149]** Ajustes nos relatórios Danfe Provider: Fechamento dos dados da filial com a natureza de operação, fechamento da chave de acesso com o caminho do site de consulta de autenticidade e centralização das informações de Consulta Autenticidade.

Arquivo: RM.Fis.Lib.Server.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 545099 / MEDU-3320]** Realizado tratativa para que quando a emissão do RPS for para a prefeitura de Cubatão, os serviços não sejam agrupados.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADASAÍDA LI010046

* **[Ticket: 100120 / FISCAL01-94]** Foram realizadas alterações para que ao Escriturar o Lote, em que haja um lançamento cujo campo “Preço Total” do Item esteja zerado, o sistema não emita a mensagem: “Tentativa de divisão por zero”. Após as alterações, o sistema não emitiu mais a mensagem.

Arquivo: RM.Fis.EscrituracaoFiscal.Service.dll

### Rotina: UTILITARIOS LANCAMENTOS FISCAIS LI 01 0070

* **[Ticket: 659083 / MEDU-3410]** Alteração no momento de contabilizar o lançamento fiscal, para que seja considerados os tributos PIS e COFINS do item.

Arquivo: RM.Fis.LancFiscal.IService.dll

## TOTVS Gestão Hospitalar

### Rotina: ELABORACAO DE AIHS SAU 47 1144

* **[Ticket: 681575 / MSAU-7156]** Ajustes na tela de Registro da AIH

Arquivos: RM.Sau.Sus.Intf.dll, RM.Sau.Sus.Data.dll, RM.Sau.Sus.Form.dll

# 12.1.15.138

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 698779 / EDUCACIONAL01-15]** Ajuste nas permissões de notas e faltas para que seja separado a permissão de consultar notas e faltas de etapa na central do aluno e na digitação de notas e faltas de etapas no menu. Com isso um novo parâmetro, chamado Visualizar consulta de notas e faltas na central do aluno, nos Parâmetros Educacionais | Aba Notas e Faltas foi criado para dar a permissão de Visualizar consulta de notas e faltas na central do aluno, onde este parâmetro nasce com permissão para todos os perfis.

Arquivos: RM.Edu.Parametros.Intf.dll, RM.Edu.Aluno.Form.dll, RM.Edu.NotaFalta.Data.dll, RM.Edu.NotaFalta.Form.dll, RM.Edu.Parametros.Form.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 664571 / EDUCACIONAL01-14]** Melhoria na validação de cadastro de bolsas do edital, a fim de não permitir a inclusão de quantidades que ultrapassem o valor total cadastrado no edital.

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

### Rotina: MATRICULAR ALUNO NAS DISCIPLINAS EDU 50 301

* **[Ticket: 718881 / EDUCACIONAL01-74]** Otimização no processo “Matricular alunos em disciplinas incluídas na matriz curricular” para permitir processar mais de 2100 registros (número alunos x quantidade de disciplinas). Apresentava mensagem de “The incoming tabular data stream (TDS) remote procedure call (RPC) protocol stream is incorrect. Too many parameters were provided in this RPC request. The maximum is 2100”

Arquivo: RM.Edu.Matricula.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: TOTVS COLAB - INCLUSÃO MOVIMENTO A PARTIR DE XML CLB007

* **[Ticket: 98854 / MATFATCMPCRM01-72]** Ajuste para buscar campo VALORMERCADORIAS do XML do CT-e

Arquivos: RM.Mov.Integracoes.Form.dll, RM.Mov.Integracoes.Service.dll

# 12.1.15.139

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 668578 / EDUCACIONAL01-77]** Melhoria no serviço de geração do código de barra via o webservice wsEdu para que seja considerada a data do cálculo informada.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Con.EducacionalWebEnsino.Data.dll, RM.Edu.Formula.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E INCONSISTENCIA CTE 002

* **[Ticket: 729332 / MATFATCMPCRM01-243]** Melhoria no processo d einutilização para analisa rcorretamente os Status de CT-es já existentes.

Arquivo: RM.Mov.CTe.Service.dll

### Rotina: ORCAMENTO DE CONTRATO ORC 013

* **[Ticket: 123266 / MATESTCNTFTOF01-31]** Melhoria no processo de estorno do Orçamento de Contrato.

Arquivos: RM.Ctr.Utils.Server.dll, RM.Ctr.Contrato.Service.dll, RM.Ctr.Faturamento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 705837 / RHU01-63]** Adicionado a funcionalidade de quando selecionado no RM a configuração de exibição no portal "Ocultar Nota da Competência para o Avaliador" para uma avaliação de desempenho a nota total somada da avaliação não será mostrada na tela de resposta da avaliação.

Arquivo: App\_Web\_rhuavaliacaodesempenhoexecucao.ascx.246e283e.dll

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 309318 / MRH-3882]** Grava valor default na opção falecido

Arquivo: RM.Rhu.Pessoa.Data.dll

### Rotina: REQUISICOES ALTERACOES DE DADOS FUNCIONAIS RHU 36 505

* **[Ticket: 198851 / MRH-8190]** Realizado ajuste para que seja exibida a mensagem ao desmarcar a opção Gerar Substituição apenas se o sistema estiver parametrizado para utilizar controle de lotação.

Arquivo: RM.Rhu.Requisicao.Form.dll

## TOTVS Gestão Financeira

### Rotina: GERAÇÃO DE RELATÓRIO RPT00005

* **[Ticket: 98707 / FINANCEIRO01-126]** Otimização no processo de envio de relatóriuo por e-mail. Agora ao gerar um relatório por e-mail com um anexo .html ou exportar para HTML, as imagens aparecem corretamente.

Arquivo: RM.Fin.Lan.Data.dll

### Rotina: Piloto Cetec

* **[Ticket: 580554 / EDUCTB001-538]** Ajuste na integração Totvs Educacional x Backoffice Protheus (Financeiro).

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 580554 / EDUCTB001-538]** Ajuste na integração Totvs Educacional x Backoffice Protheus (Financeiro).

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 580554 / EDUCTB001-538]** Ajuste na integração Totvs Educacional x Backoffice Protheus (Financeiro).

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NFS E CANCELAR NF 01 0050

* **[Ticket: 701587 / FISCAL01-32]** Ao realizar o envio do cancelamento de NFS-e estava sendo retornada a seguinte mensagem: "Imput String is not an correct format."Foi realizada uma alteração para que essa mensagem não seja emitida.

Arquivo: RM.Fis.RotinasFiscais.Data.dll

### Rotina: PARAMETRIZAÇÃO - TIPO DE MOVIMENTO PAR014

* **[Ticket: 94394 / FISCAL01-2]** Criação do Tipo de Tributo FUNRural para inclusão no Movimento e Geração nos Dados Adcionais da NFe.

Arquivo: RM.Fis.Lib.dll

### Rotina: PERIODO

* **[Ticket: FISCAL01-48]** - Criado campo "Log detalhado" em "Utilitários\Cadastro Período Fiscal\Anexo Log Cadastro Período Fiscal".- Melhoria para que o registro de execução do processo de fechamento/abertura do período fiscal seja inserido apenas uma vez no anexo de Logs.- Melhoria no código da rotina visando unificar regras comuns aos processos de fechamento e abertura.

Arquivos: RM.Fis.PeriodoFiscal.Intf.dll, RM.Fis.PeriodoFiscal.Service.dll, RM.Fis.PeriodoFiscal.Data.dll, RM.Fis.PeriodoFiscal.Form.dll

## TOTVS Gestão Hospitalar

### Rotina: AGENDAMENTO SAU 47 1135

* **[Ticket: 646016 / MSAU-6983]** Ao acessar o sistema TOTVS Gestão Hospitalar, ir ao menu Atendimento/Agendamento/Agenda de Atendimentos, selecionar a Unidade de Atendimento o nome do profissional ou sala, selecionar a data, selecionar o horário será exibido o formulário de pesquisa do paciente. Se preenchermos o campo do código do convênio com um convênio inativo, será pesquisado e exibido no campo, e possibilitará que o registro seja salvo com o convênio inativo.

Arquivos: RM.Sau.AgendaAtendimento.Form.dll, RM.Sau.Cadastros.Data.dll

### Rotina: Criação de um Parâmetro para buscar dados do Credenciamento do Prestador para lançamentos do SUS

* **[Ticket: 192070 / MSAU-6597]** Realizado ajuste na elaboração de AIH para que o sistema já carregue os dados de credenciamento do médico executante quando o mesmo for credenciado direto no convênio SUS.

Arquivos: RM.Sau.Sus.Form.dll, RM.Sau.Sus.Server.dll

### Rotina: Erro no envio de informações no XML de solicitação SADT

* **[Ticket: 631643 / MSAU-6969]** Ajuste realizado para que o sistema envie corretamente o código de CBO do profissional.

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: PEP PRESCRICAO MEDICA SAU 47 1121

* **[Ticket: 684096 / MSAU-7643]** Ao prescrever sinais vitais, eles virão desmarcados como default e o médico deverá marcar os sinais vitais desejados

Arquivo: RM.Sau.PepHis.Implementation.dll

## TOTVS Gestão Patrimonial

### Rotina: CADASTROS EVENTOS CONTABEIS PAT 37 38

* **[Ticket: 719864 / CONTROLADORIA01-46]** O processo de contabilização de baixa da avaliação foi alterado para que as contas de apuração de perda ou ganho não sejam apresentadas quando o parâmetro "Apura perda e ganho", existente no processo de baixa, estiver desmarcado.

Arquivo: RM.Pat.Contabilizacao.Form.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: PCMSO CID SMT 36 548

* **[Ticket: 687949 / RHU01-16]** Criado um nova parametro na aba de configurações de impressão do ASO, que define para ser utilizado o endereço da filial do funcionário. Caso seja marcado também substitui o parametro de exibir endereço da coligada no cabecçalho.

Arquivos: RM.Smt.Lib.Intf.dll, RM.Smt.Pessoa.Intf.dll, RM.Smt.Lib.Form.dll, RM.Smt.Pessoa.Data.dll, RM.Smt.Pessoa.Form.dll

# 12.1.15.140

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO CANCELAMENTO DE MOVIMENTO PTO 35 1188

* **[Ticket: 697807 / PONTO01-7]** O processo de lançamento de horário foi corrigido para permitir que os usuários possam lançar as batidas normalmente para os funcionários.

Arquivo: RM.Pto.Horario.Data.dll

### Rotina: PROCESSO DE CALCULO DE HORAS EXTRAS PTO 35 1238

* **[Ticket: 594685 / MRH-8502]** Exclusão da opção "Justificativa de Horas Extras" do executar.

Arquivo: RM.Pto.Extras.Form.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 731978 / PONTO01-71]** Ajustado o período de datas para verificação da utilização do cartão de ponto na geração do relatório de espelho.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Construção e Projetos

### Rotina: GERACAO DE PEDIDOS PRJ 33 828

* **[Ticket: 694905 / TOPEXECONTROL01-80]** Verificado o preenchimento do fornecedor default, para o tipo de movimento. Contudo, não é aconselhado utilizar o fornecedor como emitente.

Arquivos: RM.Prj.Facade.Intf.dll, RM.Prj.Facade.dll, RM.Prj.Contrato.Data.dll, RM.Prj.Contrato.Server.dll, RM.Prj.PedidoMaterial.Server.dll

## TOTVS Educacional

### Rotina: ALTERAR SITUACAO DE MATRICULA EDU 50 009

* **[Ticket: 593087 / EDUCACIONAL01-154]** Otimização dos Gabaritos para listar somente aqueles que pertencem ao período letivo da filial logada.

Arquivo: RM.Edu.Academico.Form.dll

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 668578 / EDUCACIONAL01-77]** Melhoria no serviço de geração do código de barra via o webservice wsEdu para que seja considerada a data do cálculo informada.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Con.EducacionalWebEnsino.Data.dll, RM.Edu.Formula.dll

### Rotina: CENSO

* **[Ticket: EDUCACIONAL01-134]** Não mostrar o campo Curso do MEC na tela de Matriz Aplicada para o Ensino Básico

Arquivo: RM.Edu.MatrizCurricular.Form.dll

### Rotina: CENTRAL DE ESTAGIO EDU 50 117

* **[Ticket: 733650 / EDUCACIONAL01-152]** Ajuste no campo que traz a listagem dos funcionário para que seja exibido a coluna função além do nome e cargo do funcionário na solicitação de um estágio feito pelo aluno no portal.

Arquivos: Portal Corpore.Net

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 724360 / EDUCACIONAL01-120]** Alguns processos no educacional permitem que os usuários utilizem consultas SQL previamente cadastradas no RM para carregar informações que serão processadas.Realizamos um ajuste para que as variáveis documentadas no link abaixo sejam interpretadas caso sejam utilizadas em uma das consultas SQL.http://tdn.totvs.com/pages/viewpage.action?pageId=63275590

Arquivos: RM.Edu.Financeiro.Form.dll, RM.Edu.Lib.Server.dll, RM.Edu.PeriodoLetivo.Form.dll

* **[Ticket: 722151 / EDUCACIONAL01-85]** Foi realizada otimização do processo de geração de lançamentos, de forma que o sistema não gere valor para parcelas calculadas por créditos financeiros quando todas as disciplinas do contrato do aluno possuírem as suas disciplinas canceladas.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: FOLHA PAGAMENTO

* **[Ticket: EDUCACIONAL01-172]** Ajustes no parametrizador com a integração com a Folha.

Arquivos: RM.Edu.Parametros.Intf.dll, RM.Edu.Parametros.Form.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 664729 / EDUCACIONAL01-30]** Melhorias nos fluxos de publicação de editais e cadastro de projeto de pesquisa dos workflows do Fluig.

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

* **[Ticket: 675748 / EDUCACIONAL01-11]** Otimizado workflow de acompanhamento de frequência do bolsista, para possibilitar o carregamento das bolsas a serem pagas ao bolsista.

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

* **[Ticket: 721320 / EDUCACIONAL01-146]** Disponibilizado novo tipo para equipe do projeto de extensão, para possibilitar ao usuário classificar um membro da equipe como "externo".

Arquivo: RM.Edu.Consts.dll

### Rotina: PORTAL ALUNO MATRICULA ONLINE EDU 50 356

* **[Ticket: 395590 / PORTALMOBILE01-143]** Melhoria na validação de co-requisito da matricula online, validando se o aluno está realizando troca de turma da disciplina de co-requisito.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 610621 / EDUCACIONAL01-168]** Correção no Censo para que a nacionalidade do aluno saia corretamente quando ele é alterado para estrangeiro.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: PROCESSO SELETIVO RM DESMATRICULAR EDU 50 392

* **[Ticket: 620882 / EDUCACIONAL01-156]** Ajustes no processo de desmatrícula de alunos provenientes do processo seletivo.

Arquivo: RM.Edu.ProcSel.Server.dll

### Rotina: RELATORIO

* **[Ticket: EDUCACIONAL01-44]** Acréscimo do link do tdn para cobrança registrada feito pelo financeiro nas mensagens de alerta de tabela master do relatório de boleto.Tratamento quando o relatório era selecionado pelo usuário e o wizard era cancelado. Anteriormente, o sistema emitia uma mensagem de validação dos campos do relatório mesmo com o cancelamento do processo.Volta do comportamento antigo em que, ao parametrizar o sistema para trabalhar com o Gerador Delphi (Parâmetros do sistema -> Tesouraria -> Relatórios) de forma que o usuário tenha a opção de gerar relatórios do gerador antigo e do RM Reports.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Lib.WinForms.dll, RM.Edu.Financeiro.Form.dll

## TOTVS Folha de Pagamento

### Rotina: FOLHA ANALITICA LAB 01 112

* **[Ticket: 385217 / FOPROTINAS01-206]** A Folha Analítica .Net quando na quebra de seção for utilizada um código especifico de seção nos cabeçalhos será usado os dados de seção especificada. Os dados da matriz (Coligada) só será usado quando a quebra for informada com máscaras.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: Geração GPS Eletronica

* **[Ticket: 375884 / FOPROTINAS01-205]** Otimizado o processo de geração de GPS Eletrônica, para que a emissão do arquivo seja após a geração dos dados

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: Project-724979 Perda de Acesso após a Conversão Anotação Pessoal Project-724979

* **[Ticket: 725709 / FOPCALCULO01-20]** Acerto de Tag de segurança para Anotações Pessoais e Gestão de Férias

Arquivos: RM.Fop.Server.dll, RM.Fop.Utils.Server.dll

* **[Ticket: 725709 / FOPCALCULO01-20]** Acerto de Tag de segurança para Anotações Pessoais e Gestão de Férias

Arquivo: RM.Fop.Utils.Server.dll

* **[Ticket: 725709 / FOPCALCULO01-20]** Acerto de Tag de segurança para Anotações Pessoais, Gestão de Férias e Dependentes Eventos Pensão

Arquivo: RM.Fop.Utils.Server.dll

### Rotina: RESCISAO CADASTRO DE RESCISAO FOP 34 400

* **[Ticket: 667685 / FOPCALCULO01-82]** O Campo Antiga Seção não estava sendo atualizado, ajustado para atualizar o campo.

Arquivo: RM.Fop.Calc.Calculos.dll

* **[Ticket: 667685 / FOPCALCULO01-82]** O Campo Antiga Seção não estava sendo atualizado, ajustado para atualizar o campo.

Arquivos: RM.Fop.Calc.Calculos.dll, RM.Fop.Rescisao.Data.dll

### Rotina: RESCISAO COMPLEMENTAR FOP 34 397

* **[Ticket: 654725 / FOPCALCULO01-80]** Ajuste no cálculo da rescisão complementar para aceitar alteração na data da demissão da rescisão original, e alterar os dias trabalhados pagos no evento de saldo salário.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: SECOES VALORES ASSOCIADOS LAB 01 231

* **[Ticket: 662857 / FOPROTINAS01-9]** Liberação da rotina de Reestruturação de Seção

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Utils.Server.dll, RM.FopFolha.dll

## TOTVS Framework

### Rotina: FORMULA VISUAL (FVS 01)

* **[Ticket: MFRWBH-1238]** Desenvolvimento do envio de email assincronamente em fórmulas visuais

Arquivos: RM.Lib.dll, RM.Lib.Workflow.Activities.dll, RM.Lib.Server.dll

### Rotina: FORMULA VISUAL WKF 001

* **[Ticket: MFRWBH-1608]** Criada propriedade na Fórmula Visual para que o usuário possa definir o nome do arquivo de log que será gerado durante a execução da FV.

Arquivo: RM.Lib.Workflow.Activities.dll

### Rotina: PLANILHA NET - EXECUÇÃO BIS00047

* **[Ticket: MFRWBH-1622]** Ao utilizar a opção "Salvar como" da planilha.Net o sistema deve remover as customizações e assim funcionará como uma planilha comum do Excel.

Arquivo: RM.Glb.PlanilhaNet.API.dll

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: 672756 / MFRWBH-1577]** -A segurança de dados será aplicada via webservice desde que o contexto venha preenchido.

Arquivos: RM.Lib.dll, RM.Lib.Server.dll

## TOTVS Gerador de Relatórios

### Rotina: IMPRESSAO RPT 00006

* **[Ticket: 508069 / MFRWBH-1273]** Ao definir a impressora padrão do relatório, a impressora utilizada é a escolhida.

Arquivos: RM.Rpt.Executor.Client.dll, RM.Rpt.Reports.Form.dll

### Rotina: INCLUSAO EDICAO EXCLUSAO RPT 00011

* **[Ticket: 665227 / MFRWBH-1579]** Melhoria na exclusão de relatórios.

Arquivo: RM.Rpt.Reports.Data.dll

* **[Ticket: 741948 / MFRWBH-1591]** Melhoria na quebra por máscara quando não está sendo utilizado campo da tabela principal.

Arquivo: RM.Rpt.Executor.Service.dll

### Rotina: RELATORIO

* **[Ticket: MFRWBH-1616]** É possivel reexecutar o relatório através da tela de parâmetros que estará disponivel na tela de preview do relatorio.

Arquivo: RM.Rpt.Reports.Form.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 664929 / CONTROLADORIA01-45]** Ajuste na consulta que retorna o Saldo Anterior que compõem o saldo de um determinado grupo para que contas com natureza do SPED do tipo "Não Informado" não sejam consideradas no somatório.

Arquivo: RM.Ctb.Sped.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CONCLUIR PEDIDO MOV 008

* **[Ticket: 709834 / MATFATCMPCRM01-205]** Melhoria para permitir que o processo de Concluir Pedido seja executado para Movimentos Bloqueados

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: INCLUSAO DE CONTRATO

* **[Ticket: MATESTCNTFTOF01-35]** Melhoria na processo de copiar / colar contrato.

Arquivo: RM.Ctr.Contrato.Intf.dll

### Rotina: REGERAR SALDOS E CUSTOS EST 013

* **[Ticket: 693353 / MATESTCNTFTOF01-160]** Ajuste na rotina de regerar saldos e custos de produtos que usam cálculo do custo igual a PEPS - Primeiro a entrar/Primeiro a sair.

Arquivo: RM.Est.Estoque.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: ADMINISTRACAO DE TAREFAS ADMINISTRACAO DE TAREFAS RHU 36 609

* **[Ticket: 706817 / RHU01-9]** Realizado ajuste no cadastro de tarefa para que o campo "Nome Abreviado" fique sempre visível.

Arquivo: RM.Rhu.Tarefas.Form.dll

### Rotina: CURRICULOS USUARIOS DO CURRICULO RHU 36 029

* **[Ticket: 572325 / MRH-8318]** No back-end e front-end a coluna CODMUNICIPIO não estava sendo setada pelo banco de talentos, gerando excessão de chave estrangeira no banco de dados.

Arquivos: FrameHTML

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 708306 / RHU01-66]** Aumentado o tamanho das colunas que estavam menores, distribuindo melhor o tamanho da colunas.

Arquivos: Portal Corpore.Net

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 725025 / RHU01-64]** Correção realizada ao tentar salvar um cadastro de pessoa com código de ocupação alfanumérico

Arquivo: RM.Rhu.Pessoa.Data.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: GRUPO DE ATENDIMENTOS CRM 321415

* **[Ticket: 654557 / MATFATCMPCRM01-4]** Melhorias no processo responsável por gerar atendimento através de grupo de e-mail.

Arquivos: RM.CRM.Atendimento.Data.dll, RM.CRM.Servicos.Server.dll

## TOTVS Gestão Financeira

### Rotina: BAIXAS REALIZADAS CANCELAMENTO DE ITEM DE BAIXA FIN 024

* **[Ticket: 615015 / FINANCEIRO01-123]** Ajuste no processo de cancelamento de baixa com boletos gerados via baixa parcial e vinculados.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 588109 / FINANCEIRO01-149]** Ajuste na consistência de rateios pode departamento no processo de inclusão de lançametno financeiro.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE CONTABILIZACAO FIN 323

* **[Ticket: 718569 / FINANCEIRO01-145]** Ajuste na contabilização de evento contábil que contém item com fórmula 'VALORTRBLAN'.

Arquivos: RM.Fin.Lan.Intf.dll, RM.Fin.Lan.Data.dll

### Rotina: SERVICO DE GERACAO DE NOSSO NUMERO FIN 247

* **[Ticket: 604425 / FINANCEIRO01-150]** Otimização no processo de atualização de conta/caixa e data de vencimento de boleto quando o lançamento for gerado pelo RM Classis Ensino Básico ou Superior. Agora o sistema não deve possibilitar a utilização desses processos por realizar uma regra para a geração de nosso número de forma diferente.

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 604425 / FINANCEIRO01-150]** Otimização no processo de atualização de conta/caixa e data de vencimento de boleto quando o lançamento for gerado pelo RM Classis Ensino Básico ou Superior. Agora o sistema não deve possibilitar a utilização desses processos por realizar uma regra para a geração de nosso número de forma diferente.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: IMPORTACAO DE MOVIMENTO MOV 039

* **[Ticket: 381381 / MATFATCMPCRM01-253]** Alteração nas validações da Natureza de Operação.

Arquivo: RM.Fis.Tributo.Service.dll

### Rotina: NATUREZA DE OPERACAO VDP0050

* **[Ticket: FISCAL01-55]** Alteração no serviço que preencher a natureza de operação.

Arquivo: RM.Fis.Tributo.Service.dll

### Rotina: OBRIGACOES ACESSORIAS ESTADUAIS LI 01 0027

* **[Ticket: 669925 / FISCAL01-28]** Implementada melhoria para o parâmetro Cadastro de Filiais\Anexo Dados Fiscais\Campo Incentivador Cultural afete o sistemada seguinte forma:- Na tela de período de apuração a aba "Incetivos Fiscais" seja habilitada apenas se parâmetro estiver habilitado e se for uma filial de Minas Gerais;- Os valores de dedução deverão ser carregados na linha 23 da DAPI-MG se parâmetro estiver habilitado.

Arquivos: RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.ApuracaoTrb.Data.dll, RM.Fis.ApuracaoTrb.Form.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 392939 / FISCAL01-19]** Para os lançamentos de Saida deve ser gerado no C197 o Valor Codigo de Ajuste no campo VL\_IMCS, caso possua Código de Ajuste e as informações dos campos VL\_BC\_ICMS e ALIQ\_ICMS serão geradas zeradas.

Arquivo: RM.Fis.Sped.Server.dll

### Rotina: OBRIGACOES PRINCIPAIS ENTRADA SAIDA LI 01 0046

* **[Ticket: 740796 / FISCAL01-34]** Realizado a tratativa para que ao clicar no ícone da calculadora do ICMS ST os campos de base "ICMS ST" e "valor de ICMS ST" em Dados Fiscais | Valor ICMS do item do lançamento, sejam calculados.

Arquivo: RM.Fis.LancFiscal.Form.dll

### Rotina: UTILITARIOS LANCAMENTOS FISCAIS LI 01 0070

* **[Ticket: 659083 / MEDU-3410]** Contabilização dos tributos PIS/COFINS

Arquivo: RM.Fis.Formula.dll

## TOTVS Gestão Hospitalar

### Rotina: AGENDAMENTO SAU 47 1135

* **[Ticket: 646016 / MSAU-6983]** Ajuste no formulário de pesquisa de cliente pois era possivel pesquisar um convênio inativo e se pesquisasse um convênio ativo e retornasse para o campo de codigo para pesquisar um convênio inativo o campo de descrição continuava com os valores da pesquisa anterior, criando confusão para o usuário.

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: Erro ao cadastrar regra de lançamento dentro e fora da conta

* **[Ticket: 685955 / MSAU-7259]** Ajustes na tela de Regra de Lançamento Dentro ou Fora da Conta

Arquivo: RM.Sau.CadastrosFat.Data.dll

### Rotina: PAINEL DE CLASSIFICACAO DE RISCO

* **[Ticket: 716626 / MSAU-7564]** O sistema não permitirá chamadas de senhas inativas. Para chamá-las, o paciente deve retornar para a fila.

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: Painel de Eletivos , aba de registro de atendimento não publicar no painel de chamadas quando o atendente clicar no botã

* **[Ticket: 544350 / MSAU-6113]** Criado paramento para não realizar chamada no painel de atendimentos eletivos quando a senha estiver em registro de atendimento.

Arquivos: RM.Sau.Utils.Intf.dll, RM.Sau.RegistroAtendimento.Server.dll

* **[Ticket: 544350 / MSAU-6113]** Correção na mensagem apresentada ao realizar a chamada de senha em bases Oracle

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

### Rotina: XML da Glosa NÃO GERA

* **[Ticket: 760888 / MSAU-8029]** Ajuste na geração de XML de recurso de glosa

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Gestão Patrimonial

### Rotina: OPCOES PARAMETROS RM BONUM PAT 37 60

* **[Ticket: 505961 / CONTROLADORIA01-82]** A tela de parâmetros do módulo patrimonial foi alterada para que seja possível gravar as modificações realizadas.

Arquivo: RM.Pat.Parametros.Data.dll

### Rotina: OPERACOES PATRIMONIAIS IMPAIRMENT PAT 37 105

* **[Ticket: 376207 / CONTROLADORIA01-37]** Atualização do processo de impairment para apurar o valor base corrigido do cenário selecionado pelo usuário.

Arquivos: RM.Pat.Ocorrencia.Service.dll, RM.Pat.PatrimonioMoeda.IService.dll, RM.Pat.Patrimonio.Service.dll, RM.Pat.PatrimonioMoeda.Service.dll, RM.Pat.Relatorio.Data.dll

* **[Ticket: 376207 / CONTROLADORIA01-37]** Atualização do processo de impairment para apurar o valor base corrigido do cenário selecionado pelo usuário

Arquivos: RM.Pat.PatrimonioMoeda.IService.dll, RM.Pat.Patrimonio.Service.dll, RM.Pat.PatrimonioMoeda.Service.dll, RM.Pat.Relatorio.Data.dll, RM.Pat.Ocorrencia.Service.dll

* **[Ticket: 695028 / CONTROLADORIA01-44]** Os processos de avaliação patrimonial, impairment e reversão de impairment foram alterados para que seja possível informar taxa de depreciação ou vida útil restante iguais ou superiores a zero.

Arquivos: RM.Pat.Ocorrencia.Data.dll, RM.Pat.Ocorrencia.Form.dll

## TOTVS Incorporação

### Rotina: ALUGUEL CADASTROS BASICOS IMB 49 769

* **[Ticket: 703760 / TINPAD001-79]** Melhoria no cadastro de característica do imóvel no módulo de aluguel.

Arquivo: RM.Imb.Aluguel.Imovel.Form.dll

### Rotina: FORMULA VISUAL IMB 49 876

* **[Ticket: 686712 / TINPAD001-68]** Ajuste na validação do Tipo de data de vencimento

Arquivo: RM.Imb.Venda.Regra.Form.dll

* **[Ticket: 686712 / TINPAD001-68]** Ajustes no preenchimento da data base dos componentes de Juros e CM

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Regra.Intf.dll, RM.Imb.Venda.Regra.Data.dll, RM.Imb.Venda.Regra.Form.dll

### Rotina: VENDA CADASTRO IMB 49 868

* **[Ticket: 581534 / TINPAD001-25]** Incidente: foi verificado que o campo "Data Cancelamento" estava ficando habilitado no momento da inclusão de uma nova vendaSolução: o campo foi desabilitado no momento da inclusão

Arquivo: RM.Imb.Contratos.Data.dll

# 12.1.15.141

## Outros

### Rotina: BANCO DE TALENTOS TABELAS AUXILIARES CAMPOS COMPLEMENTAR RHU 36 060

* **[Ticket: 627647 / MRH-8659]** Ajuste realizado ao desconsiderar acentos no filtro de cidade e estado

Arquivos: FrameHTML

## TOTVS Automação de Ponto

### Rotina: ALTO CONSUMO DE RECURSOS SGBD 90 25

* **[Ticket: 716465 / PONTO01-73]** Ajuste realizado para corrigir problema de vazamento de memória/performance de processo na execução do cálculo.

Arquivos: RM.Pto.Facade.dll, RM.Pto.Horario.Intf.dll, RM.Pto.EventosCalculados.Data.dll, RM.Pto.Calculo.Intf.dll, RM.Pto.Formula.dll

### Rotina: PORTAL WEB ABONAR ATRASOS E FALTAS PTO 35 1257

* **[Ticket: 687768 / MRH-9287]** Foi realizado o ajuste do filtro que retorna as ocorrências passíveis de serem abonadas de acordo com o parâmetro do sindicato referente a compensação "Realiza compensação de extras e atrasos antes da autorização e cálculo do abono", a parametrização do abono nos parâmetros iniciais está informada como Intervalo.

Arquivos: RM.Pto.Abono.Data.dll, RM.Pto.Abono.Form.dll

## TOTVS Construção e Projetos

### Rotina: BACKUP RESTAURACAO

* **[Ticket: TOPORCAPLAN001-163]** Restore demorando indefenidamente

Arquivo: RM.Prj.BackupRestore.Data.dll

## TOTVS Educacional

### Rotina: CENTRAL DE ESTAGIO EDU 50 117

* **[Ticket: 732350 / EDUCACIONAL01-151]** Realizado uma melhoria para que seja possível cadastrar um aluno de egresso em uma vaga de emprego mesmo que ele não tenha histórico de matricula naquele curso.Regras para permitir:- A vaga tem que ser de emprego- No cadastro do aluno tem que ter a habilitação conforme o perfil da vaga, e a situação de matricula que consta no cadastro tem que estar marcada com a opção que indica a conclusão do curso.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.MatrizCurricular.Form.dll, RM.Edu.MatrizCurricular.Server.dll, RM.Edu.MatrizCurricular.Data.dll

### Rotina: MATRICULA EM DISCIPLINAS

* **[Ticket: EDUCACIONAL01-255]** Otimização no processo “Matricular aluno nas disciplinas” para executar com sucesso quando o aluno já tenha alguma disciplina já matriculada anteriormente.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: PORTAL PROFESSOR ESTAGIO EDU 50 376

* **[Ticket: 749656 / PORTALMOBILE01-222]** Ajuste para permitir o correto envio do arquivo na tela de relatório final de estágio.

Arquivo: App\_Web\_eduestagioavaliacaofinalalunowebform.ascx.1d4ca059.dll

### Rotina: Project-702072 [RM\_12.1.15.128-Testes] Processo copiar avaliações não está apresentando opções de turmas Project-702072

* **[Ticket: 725139 / EDUCACIONAL01-96]** Ajuste no processo de cópia de avalições entre as turmas/disciplinas

Arquivo: RM.Edu.Services.Server.dll

## TOTVS Folha de Pagamento

### Rotina: EVENTOS RELATORIOS DE EVENTOS LAB 01 88

* **[Ticket: 667444 / FOPROTINAS01-35]** Feito a tratativa na GRCSU para completar com zeros a esquerda uma vez que o CPF tem 11 dígitos e este valor é usado no campo nosso número que exige o tamanho de 12.

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: Mensagem de Férias em Dobro Improcedente

* **[Ticket: 699934 / FOPROTINAS01-24]** Foi ajustada a exibição de Informações Adicionais no Cadastro de Férias do funcionário para apresentar mensagem que deve-se pagar férias em dobro apenas quando o limite de início de gozo do funcionário vence na competência atual e não existir período de gozo cadastrado, ou o período de gozo ultrapassa total ou parcialmente o fim do 2º período aquisitivo, ou restarem dias a marcar ou sem abono. Além disso, foi ajustado para apresentar em Informações Adicionais uma mensagem de risco de férias em dobro 6 meses após início do período concessivo apenas se não houver período de gozo cadastrado, ou restarem dias a marcar ou sem abono.

Arquivos: RM.Fop.FuFerias.Intf.dll, RM.Fop.FuFerias.Form.dll, RM.Fop.FuFerias.Data.dll

### Rotina: RESCISAO CADASTRO DE RESCISAO FOP 34 400

* **[Ticket: 667685 / FOPCALCULO01-82]** O Campo Antiga Seção não estava sendo atualizado, ajustado para atualizar o campo.

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Framework

### Rotina: Falha na tradução no windows 2012 server

* **[Ticket: MFRWBH-1624]** Foi realizado um ajuste na geração da tradução. Também foram atualizados os utilitários al.exe e resgen.exe.

Arquivos: RM.Lib.dll, al.exe, ResGen.exe

### Rotina: USUARIOS IDENTIFICACAO FRW 00073

* **[Ticket: 648318 / MFRWBH-1411]** Ajuste para melhor funcionamento do filtro por coluna juntamente com a utilização da opção de localizar registro numa visão do sistema

Arquivo: RM.Lib.WinForms.dll

## TOTVS Gestão Bibliotecária

### Rotina: PUBLICACOES BIB 10 1070

* **[Ticket: 704261 / EDUCACIONAL01-93]** Ajuste no processo de cópia de publicações.

Arquivo: RM.Bib.Processos.Data.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 742718 / CONTROLADORIA01-88]** Ajuste do cadastro de signatário para aceitar cadastros com CNPJ e ajuste da tabela do mesmo para adequação da mudança da legislação.

Arquivos: RM.Ctb.Sped.Intf.dll, RM.Ctb.Sped.Data.dll, RM.Ctb.Sped.Form.dll

### Rotina: RELATORIOS DIARIO CTB 38 112

* **[Ticket: 681008 / CONTROLADORIA01-106]** O relatório Diário passou a ser emitido sem apresentar quebras de página indevidas.

Arquivo: RM.Ctb.Relatorios.Service.dll

* **[Ticket: 729367 / CONTROLADORIA01-81]** O relatório Diário passou a ser emitido sem apresentar quebras de páginas indevidas.

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: :: Baixa Automática ::

* **[Ticket: 504752 / MATFATCMPCRM01-89]** Sistema parametrizado para efetuar baixa automática porém, quando faz o vinculo e tenta salva movimento sistema apresenta mensagem de consistência.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 562308 / MATFATCMPCRM01-207]** Ao faturar movimento, excluindo os itens do movimento de origem e salvando o sistema está apresentando mensagem de inconsistencia: Referência de objeto não definida para uma instância de um objeto.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: QUADRO COMPARATIVO COTACAO COM 009

* **[Ticket: 96666 / MATFATCMPCRM01-75]** Ao usar o valor do frete no calculo do IPI, deve ser usado o frete rateado para tal calculo.

Arquivo: RM.Cmp.Cotacao.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: CARACTERISTICAS PESSOAIS LANCAMENTO DE CARACTERISTICAS PES RHU 36 071

* **[Ticket: 721368 / RHU01-18]** Permite que o usuário copie as características com uma das opções (Pessoa ou Função).

Arquivo: RM.Rhu.CaracteristicaPessoal.Form.dll

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 735796 / PONTO01-33]** Foi ajustado o cálculo de abono de funcionários incluídos em turmas de modo que, sendo uma base SQL server, não mais ocorrerá o erro de inexistência da coluna DURACAOPROGRAMADA.

Arquivo: RM.Rhu.Utils.Server.dll

## TOTVS Gestão Financeira

### Rotina: BAIXA DE TITULOS FIN10060

* **[Ticket: FINANCEIRO01-239]** Adicionando atributo Serializable na classe FinTBCBaixaPagamento

Arquivo: RM.Fin.Lan.Intf.dll

### Rotina: BOLETOS

* **[Ticket: FINANCEIRO01-259]** Otimização no processo de Alteração de Conta Caixa e Convênio. Agora o sistema apresenta a mensagem correta no log.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 588109 / FINANCEIRO01-149]** Ajuste na consistência de rateios pode departamento no processo de inclusão de lançametno financeiro.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE ATUALIZACAO DA BAIXA FIN 313

* **[Ticket: 739155 / FINANCEIRO01-166]** Melhoria na baixa de lançamento para que não ocorra erro ao tentar baixar um lançamento que não possui data de previsão de baixa e o parâmetro de data baixa default seja igual data de previsão

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADASAÍDA LI010046

* **[Ticket: 100120 / FISCAL01-94]** Foi identificado que, ao realizar as alterações referentes à melhorias no cálculo do Diferencial de Alíquota do ICMS Interestadual na Entrada, não foi previsto que pudesse existir a redução na Base de Cálculo do ICMS Interno e no ICMS Interestadual, e que o valor dos dois tributos pudesse ser o mesmo. Quando esse caso acontecia, o sistema não realizava o cálculo de forma correta, trazendo o valor do Diferencial de alíquota diferente de Zero.

Arquivo: RM.Fis.LancFiscal.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Itens Restritos, Não padrão e Antimicrobianos

* **[Ticket: 765490 / MSAU-8089]** O sistema está emitindo um erro ao solicitar a justificativa de itens não padronizados

Arquivo: RM.Sau.Pep.Data.dll

## TOTVS Incorporação

### Rotina: ALUGUEL EVENTO FINANCEIRO IMB 49 776

* **[Ticket: 727478 / TINPAD001-139]** Ajuste na validação para criação de evento financeiro

Arquivo: RM.Imb.Aluguel.Lancamento.Server.dll

# 12.1.15.142

## TOTVS Automação de Ponto

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 691716 / PONTO01-206]** Validação de registros fora do período corrigida.

Arquivo: RM.Pto.Batida.Intf.dll

* **[Ticket: 659375 / PONTO01-80]** Foi realizado o ajuste para que a natureza no processo de importação de batidas quando parametrizada para considerar o horário planejado seja calculada corretamente.

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: MOVIMENTO CANCELAMENTO DE MOVIMENTO PTO 35 1188

* **[Ticket: 697285 / PONTO01-4]** O processo de lançamento de horário foi corrigido para permitir que os usuários possam lançar as batidas normalmente para os funcionários.

Arquivo: RM.Pto.Horario.Data.dll

### Rotina: PORTAL WEB VISUALIZACAO DE OCORRENCIAS PTO 35 1252

* **[Ticket: 735788 / PONTO01-70]** A lógica da listagem de ocorrências abonáveis no portal foi reformulada para se igualar as ocorrências apresentadas no aplicativo.

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Avaliação e Pesquisa

### Rotina: LICENCESERVER FRW 00044

* **[Ticket: 748761 / PORTALMOBILE01-355]** Ajuste no consumo de licença do executor web.

Arquivo: App\_Web\_tstmain.aspx.e95fadbb.dll

## TOTVS Business Connect

### Rotina: INTEGRACAO PROTHEUS BACKOFFICE EDU 50 466

* **[Ticket: 796603 / EDUCTB001-566]** Ajuste na integração Educacacional x Backoffice Protheus tratando a tag BankInternalId da mensagem de baixa de lançamentos.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

### Rotina: MNT CONSULTA DE SALDO MNT 008

* **[Ticket: 721149 / MATESTCNTFTOF01-166]** Melhoria no adapter de integração de Cliente/Fornecedor - mensagem única CustomerVendor versão 2.002 - para que seja permitido sincronizar registro que possui classificação igual a Ambos.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

### Rotina: WEBSERVICE <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:br="http://www.totvs.com.br

* **[Ticket: 574558 / MATFATCMPCRM01-8]** Melhoria no processo de avançar a etapa de um atendimento via webservice (TBC)

Arquivo: RM.Con.Conector.WebService.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS CADASTRO PRJ 33 937

* **[Ticket: 769474 / TOPORCAPLAN001-177]** Ajuste realizado em Concorrência Eletrônica para geração de contrato em projeto em negociação

Arquivo: RM.Prj.Contrato.Form.dll

### Rotina: CONTRATOS MEDICAO PRJ 33 941

* **[Ticket: 591543 / TOPEXECONTROL01-107]** Realizado ajuste acumular o valor medido automaticamente ao realizar a medição de um período de contrato.

Arquivo: RM.Prj.Contrato.Form.dll

### Rotina: liberacao de contrato a receber

* **[Ticket: 763420 / TOPEXECONTROL01-102]** Ajuste ao definir o tipo de item do contrato (planilha ou serviços) para contratos a receber na geração do movimento relacionado a medição do período.

Arquivo: RM.Prj.Contrato.Data.dll

## TOTVS Educacional

### Rotina: BOLSA RETROATIVA EDU 50 479

* **[Ticket: 756687 / EDUCACIONAL01-231]** Sistema passou a desconsiderar o aproveitamento de valores em conta corrente na exclusão de bolsa retroativa utilizando a opção de baixa parcial.

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: 756687 / EDUCACIONAL01-231]** Sistema passou a desconsiderar o aproveitamento de valores em conta corrente na exclusão de bolsa retroativa utilizando a opção de baixa parcial.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: CONTRATOS CONTABILIZACAO EDU 50 141

* **[Ticket: 691270 / EDUCACIONAL01-242]** O processo de contabilização do novo modelo contabiliza as diferenças que podem ocorrer no contrato (aumento ou redução) e em função de arredondamento o processo estava identificando um valor de diferença muito baixo, exemplo, -0,00120, e neste caso o sistema estava acionando o evento contábil para processar a redução no contrato.Realizado uma melhoria para que seja processado valor maior ou igual a 0,01.

Arquivo: RM.Edu.Contabil.Server.dll

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 626025 / EDUCACIONAL01-243]** Melhoria no serviço de geração de lançamento financeiro para que não seja apresenta a mensagem “O lançamento não pode ser gerado pois o valor é menor que zero.” Para alunos que tenham valores na conta corrente superior ao valor líquido do lançamento financeiro.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 780403 / EDUCACIONAL01-604]** Realizada uma validação ao selecionar as informações do projeto na alteração de situação de projeto e pesquisa para que seja apresentada uma mensagem informando que nenhum projeto foi encontrado, pois quando não existia projeto o sistema estava apresentando uma mensagem de não conformidade não tratada e agora tratamos a mensagem.

Arquivo: RM.Edu.PesquisaExtensao.Form.dll

### Rotina: PORTAL ALUNO ATIVIDADES CURRICULARES EDU 50 344

* **[Ticket: 715461 / PORTALMOBILE01-185]** Melhoria na inscrição de atividade ofertada pelo portal, evitando validações indevidas de carga horária.

Arquivos: RM.Edu.Academico.Server.dll, RM.Edu.Processos.Data.dll

* **[Ticket: 715461 / PORTALMOBILE01-185]** Melhoria na inscrição de atividade ofertada pelo portal, evitando validações indevidas de carga horária.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: PORTAL PROFESSOR ESTAGIO EDU 50 376

* **[Ticket: 749656 / PORTALMOBILE01-364]** Ajuste para corrigir o filtro no momento de exibir os arquivos anexos da avaliação final, quando logado no portal como Professor.

Arquivo: App\_Web\_eduestagioavaliacaofinalprofessorwebform.ascx.497dfae.dll

### Rotina: Project-729514 #FIEMG - Geração Plano de Aula Project-729514

* **[Ticket: 735680 / EDUCACIONAL01-131]** Ajuste na geração do plano de aula quando selecionar para que não seja gerado aula para eventos acadêmicos, não gere aula para tais dias.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

### Rotina: Project-741712 FIEMG - Geração automático Professor Project-741712

* **[Ticket: 747097 / EDUCACIONAL01-618]** Ajuste na geração automática de usuários para o professor.

Arquivo: RM.Edu.Professor.Data.dll

### Rotina: TCC EDU 50 491

* **[Ticket: 614453 / EDUCACIONAL01-169]** Otimização da análise curricular do aluno, para permitir demonstrar nas informações de TCC disciplinas concluídas por equivalência recíproca. Por exemplo, a disciplina “A” é equivalente recíproca à disciplina “B”, onde “A” foi reprovada no período letivo anterior, mas a disciplina “B” foi aprovada no período letivo atual.

Arquivos: RM.Edu.Matricula.Server.dll, RM.Edu.MatrizCurricular.Server.dll

## TOTVS Folha de Pagamento

### Rotina: GRUPO DE EVENTOS LAB 01 116

* **[Ticket: 776820 / FOPROTINAS01-242]** No modulo de orçamento / Dados do Orçamento / Quadro de vagas não estava contabilizando admissões sem Código de perfil que não fosse gerada por transferência

Arquivo: RM.Fop.Orcamento.Data.dll

* **[Ticket: 785380 / FOPROTINAS01-249]** O quadro de vagas do orçamento não estava considerando promoções de anos anteriores, não refletindo a situação fidedigna da função no ano corrente

Arquivo: RM.Fop.Orcamento.Data.dll

### Rotina: PARAMETRIZADOR FOLHA DE PAGAMENTO LAB 01 36

* **[Ticket: 656652 / FOPROTINAS01-203]** Ajuste no processo de geração do Orçamento

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: PORTAL WEB SUBORDINADOS LAB 01 213

* **[Ticket: 652366 / FOPROTINAS01-142]** Ao acessar a tela de subordinados do portal não será mais exibida a coluna de situação de férias caso o usuário não possua permissão para cadastrar as férias

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: RHU 36 659

* **[Ticket: RHU01-114]** RollBack de ajustes feitos anteriormentes.

Arquivos: RM.Fop.Calc.Calculos.dll, RM.Fop.Rescisao.Data.dll

## TOTVS Framework

### Rotina: CURRICULOS USUARIOS DO CURRICULO RHU 36 029

* **[Ticket: 703226 / RHU01-10]** Corrigido o erro de ortografia.

Arquivos: FrameHTML

### Rotina: FLUIG RHU 36 659

* **[Ticket: MFRWBH-1656]** O Processamento da fila de integração foi otimizado.

Arquivo: RM.Glb.IntegracaoFluig.Server.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 720877 / MFRWBH-1576]** Melhoria na validação dos menus de anexo a serem exibidos, possibilitando a exibição de itens ativados pelos produtos.

Arquivo: RM.Lib.WinForms.dll

### Rotina: PADRAO

* **[Ticket: MFRWBH-1647]** Otimizaçõe realizadas ao incluir uma nova consulta SQL na planilha.Net quando contém parametros

Arquivo: RM.Glb.PlanilhaNet.API.dll

### Rotina: PERFIS FRW 00055

* **[Ticket: 776950 / MFRWBH-1665]** A permissão para utilizar o assistente de criação de gráficos agora está associada à permissão de incluir e editar Gráficos

Arquivo: RM.Glb.Grafico.Form.dll

### Rotina: PROJETO GERACAO DO PROJETO MTD 00010

* **[Ticket: 789967 / MFRWBH-1671]** -O valor de tamanho máximo não deve ser atribuído à campos do tipo imagem

Arquivos: RM.Glb.Metadata.Form.dll, RM.Lib.MetadataProvider.Server.dll

### Rotina: RM X FLUIG GED: PARÂMETROS DE CONFIGURAÇÃO INT00013

* **[Ticket: MFRWBH-1246]** A integração do RM com o Identity Foi Otimizada.

Arquivo: RM.Glb.IntegracaoFluig.Server.dll

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: 773888 / MFRWBH-1646]** Melhoria na exclusão de registros via Web Service para que os registros possam ser removidos sem inconsistências.

Arquivo: RM.Lib.Server.dll

## TOTVS Gerador de Relatórios

### Rotina: LINHAS MULTIBANDAS RPT 00031

* **[Ticket: 669641 / MFRWBH-1503]** Melhoria na função de esconder detalhe

Arquivo: RM.Rpt.Executor.Service.dll

### Rotina: RELATORIO

* **[Ticket: MFRWBH-1635]** Após a modificação a DANFE é mostrada sem a exceção "Não há linha na posição 0. Código da Informação: [d566755151cca1c8c40adf9c10af7118]" ser apresentada.

Arquivo: RM.Rpt.Reports.Form.dll

## TOTVS Gestão Bibliotecária

### Rotina: USUARIOS BIB 10 1095

* **[Ticket: 688477 / EDUCACIONAL01-3]** Ajuste na alteração do cadastro de usuários.

Arquivo: RM.Bib.Facade.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 742718 / CONTROLADORIA01-88]** Ajuste do cadastro de signatário para aceitar cadastros com CNPJ e ajuste da tabela do mesmo para adequação da mudança da legislação.

Arquivo: RM.Ctb.Sped.Data.dll

* **[Ticket: 766999 / CONTROLADORIA01-124]** O problema ocorre pois os fatos que representam o grupo do Ativo no balanço foram cadastrados com "01" no lugar de "1" e isto fez com que a geração do arquivo ficasse incorreta. Desta forma foi feito ajuste para que o processo consiga identificar o grupo Ativo e Passivo desde que os mesmos comecem com 1 e 2 respectivamente ou ainda comecem com (01, 001, 0001,...) ou (02, 002, 0002,...).

Arquivo: RM.Ctb.Sped.Service.dll

* **[Ticket: 770037 / CONTROLADORIA01-131]** Ajuste na geração do registro J150 para que contas analíticas não sejam mostradas no arquivo quando o parâmetro "Não mostrar as contas analíticas na demonstração de resultado do exercício (Registro J150)." for marcado e existirem contas analíticas que possuem “VL\_CTA\_ULT\_DRE”-(Valor inicial total constante na DRE do último período informado)

Arquivo: RM.Ctb.Sped.Service.dll

### Rotina: RELATORIOS RAZAO CTB 38 114

* **[Ticket: 709082 / CONTROLADORIA01-86]** O Relatório Razão Gerencial / Contábil foi modificado para que o saldo atual leve em consideração o saldo anterior quando o período informado não possuir movimentação.

Arquivo: RM.Ctb.Relatorios.Service.dll

### Rotina: RELATORIOS RETROSPECTIVA CONTABIL GERENCIAL CTB 38 124

* **[Ticket: 769453 / CONTROLADORIA01-127]** O relatório Retrospectiva Gerencial Contábil foi alterado para que, ao selecionar Movimento na opção Totalização, sejam exibidas apenas contas gerenciais associadas a contas contábeis que possuem movimentação.

Arquivo: RM.Ctb.Relatorios.Service.dll

### Rotina: UTILITARIOS IMPORTACAO POR TEXTO CTB 38 142

* **[Ticket: 697886 / CONTROLADORIA01-80]** A importação do saldo anterior, via conceito, foi modificada para que o processo possa ser executado com sucesso.

Arquivos: RM.Ctb.Lan.Intf.dll, RM.Ctb.Lan.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CADASTRO DE FORMULA FRM 001

* **[Ticket: 663878 / MATFATCMPCRM01-261]** Ao inserir o contexto de fórmula CMOMETODOULTIMA(TABMOV('DATAEMISSAO','D')) o mesmo está retornando valor 1, porém deveria retornar o valor da última cotação cadastrada ou o valor da contação para a data informada.

Arquivo: RM.Mov.Formula.dll

### Rotina: CADASTRO DE PRODUTOS PRD 001

* **[Ticket: 766530 / MATESTCNTFTOF01-179]** Melhoria no processo de inclusão de código de barras do Produto.

Arquivo: RM.Est.Produto.Service.dll

### Rotina: CADASTRO FUNCIONARIO FUN 001

* **[Ticket: 163595 / MATFATCMPCRM01-47]** Melhorias no cadastro de vendedor.

Arquivo: RM.Mov.Cadastros.Form.dll

### Rotina: FORMULA VISUAL WKF 001

* **[Ticket: 771920 / MATFATCMPCRM01-318]** Melhorias no processo de faturamento quando executado através de Fórmula Visual.

Arquivos: RM.Mov.FormulaVisual.Activities.dll, RM.Mov.Movimento.Service.dll

### Rotina: INTERFERENCIACOTACAO COM 012

* **[Ticket: 717643 / MATFATCMPCRM01-226]** Melhorias no processo de interferência da cotação.

Arquivo: RM.Cmp.Cotacao.Form.dll

### Rotina: INVENTARIO IMPORTACAO DE CONTAGEM TXT EST 022

* **[Ticket: 655675 / MATESTCNTFTOF01-173]** Melhoria no processo de importação de itens de inventário via conceito.

Arquivo: RM.Est.Inventario.Service.dll

### Rotina: INVENTARIO ENCERRAR

* **[Ticket: MATESTCNTFTOF01-39]** Ajuste no filtro de inclusão de Produtos do Inventário.

Arquivos: RM.Est.Inventario.IService.dll, RM.Est.Inventario.Service.dll, RM.Est.Inventario.Data.dll

* **[Ticket: MATESTCNTFTOF01-39]** Ajuste no filtro de inclusão de Produtos do Inventário.

Arquivo: RM.Est.Inventario.Data.dll

### Rotina: MDF-E - PARAMETRIZAÇÃO DE MOVIMENTO MDF001

* **[Ticket: MATFATCMPCRM01-333]** Mensagem de aviso da data de liberação do MDF-e 3.0

Arquivo: RM.Est.dll

### Rotina: Project-729589 Impressão de Contrato Project-729589

* **[Ticket: 735206 / MATESTCNTFTOF01-157]** Melhoria na rotina de impressão de contratos ao selecionar o tipo de relatório.

Arquivo: RM.Mov.Processos.Form.dll

### Rotina: REGERAR SALDOS E CUSTOS EST 013

* **[Ticket: 744952 / MATESTCNTFTOF01-162]** Melhoria no processo de regeração de saldos e custos para possibilitar filtrar a faixa de produtos pelo identificador.

Arquivos: RM.Est.Estoque.Service.dll, RM.Est.Processos.Form.dll

### Rotina: TOTVS COLAB CONSULTA EVENTOS MDF E CLB 027

* **[Ticket: 693328 / MATFATCMPCRM01-189]** Melhorias no processo responsável pelo sincronismo de MD-e no TOTVS Colaboração 2.0.

Arquivo: RM.Mov.TOTVSColab.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: avaliação de desempenho com escala por intervalo

* **[Ticket: 314413 / MRH-5385]** Ajuste realizado para começar a considerar os intervalos das escalas

Arquivo: RM.Rhu.AvalDesemp.Server.dll

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 706020 / MRH-9372]** Adicionada a funcionalidade de dimensionamento dos campos de texto na tela de avaliação de desempenho.

Arquivos: Portal Corpore.Net

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 705005 / RHU01-7]** Adicionada a funcionalidade de "visualizar nome dos campos" a tela de Pessoa.

Arquivo: RM.Rhu.Pessoa.Form.dll

### Rotina: REGIAO

* **[Ticket: MRH-9673]** Solicitação da Fábrica de Software para adequação da avaliação de Desempenho à utilização de plugins.

Arquivos: RM.Rhu.Customizacao.Intf.dll, RM.Rhu.AvalDesemp.Server.dll, RM.Rhu.AvalDesemp.Data.dll

### Rotina: REQUISICOES SUBSTITUICAO RHU 36 504

* **[Ticket: 501248 / MRH-7953]** Realizado ajuste no processo "Inserir em Processo de Movimentação".

Arquivos: RM.Rhu.Lib.WinForms.dll, RM.Rhu.Pessoa.Form.dll

### Rotina: REQUISICOES TRANSFERENCIA COM ALTERACAO DE DADOS FUNCIONAIS RHU 36 507

* **[Ticket: 668152 / MRH-9091]** Permite que o usuário altere campos que não seja filial, seção, função e salário, caso tenha uma requisição pendente.

Arquivos: RM.Rhu.Utils.Server.dll, RM.Rhu.Funcionario.Data.dll

### Rotina: RHU 36 659

* **[Ticket: RHU01-114]** Realizado ajuste em requisição de Transferência com Alteração de Dados Funcionais.

Arquivo: RM.Rhu.Requisicao.Server.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: ATENDIMENTOS CRM 321443

* **[Ticket: 761825 / MATFATCMPCRM01-278]** Melhorias no processo responsável por repassar atendimento.

Arquivo: RM.CRM.Atendimento.Data.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA RESGATE FIN 017

* **[Ticket: 762649 / FINANCEIRO01-229]** Ajuste na aplicação financeira para não verificar o parâmetro "considerar sábado com dia util".

Arquivo: RM.Fin.Facade.dll

### Rotina: BAIXA ATUALIZACAO DE VALORES IMB 49 804

* **[Ticket: 711396 / FINANCEIRO01-536]** Ajustado serviço de alteração de lançamento, para não validar se a contabilidade esta exportada quando serviço estiver sendo utilizado pelo processo de finalização do lançamento.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: BAIXAS REALIZADAS ANEXO LANCAMENTO FIN 022

* **[Ticket: 504342 / FINANCEIRO01-297]** Otimização no processo de baixa de lançamentos. Agora o sistema realiza a baixa corretamente dos lançamentos com boletos diferentes gerando um extrato de caixa para todos quando o parâmetro (Contas a Pagar -> Baixa -> Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa) está marcado.

Arquivo: RM.Fin.Extrato.Service.dll

### Rotina: BOLETO ANEXO LANCAMENTOS DO BOLETO FIN 037

* **[Ticket: 686815 / FINANCEIRO01-54]** Permitir geração de boleto para lançamentos de Devolução, Nota de Crédito ou Crédito de Adiantamento desde que não estejam vinculados.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: INTEGRACAO PROTHEUS BACKOFFICE EDU 50 466

* **[Ticket: 796603 / EDUCTB001-566]** Ajuste na integração Educacacional x Backoffice Protheus tratando a tag BankInternalId da mensagem de baixa de lançamentos.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO ALTERACAO FIN 172

* **[Ticket: 696644 / FINANCEIRO01-89]** Ajuste na permissão de alteração do centro de custo do lançamento, se boleto com código de barras já gerado irá permitir.

Arquivo: RM.Fin.Lib.dll

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 469907 / FINANCEIRO01-187]** Otimizado o sistema para não deixar realizar a exclusão de um tipo de documento que esteja vinculado nos parâmetros de tipo de documento das etapas: Geração IRRF-PJ, Geração IRRF-PF, Geração INSS e Geração das Retenções.

Arquivo: RM.Fin.TipoDoc.Data.dll

### Rotina: LANCAMENTO MANUTENCAO REGERAR CONTABILIZACAO INCLUSAO FIN 210

* **[Ticket: 721779 / FINANCEIRO01-133]** Melhoria no processo de regerar contabilização de inclusão e baixa - Não barrar a regeração contábil para lançamento remetido devido ao mesmo não influenciar valores que já foram remetidos

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE GERACAO DE NOSSO NUMERO FIN 247

* **[Ticket: 682815 / FINANCEIRO01-192]** Ajuste no cálculo do dígito verificar do nosso número para o banco UNICRED.

Arquivo: RM.Fin.Banco.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 727050 / FISCAL01-119]** Realizado tratativa no SELECT responsável pelo retorno dos movimentos a serem enviados para a SEFAZ.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 375435 / FISCAL01-123]** Realizado tratativa para não remover os caracteres: @, #, $, % e \*.

Arquivo: RM.Fis.Utils.Server.dll

### Rotina: OBRIGACOES ACESSORIAS ESTADUAIS LI 01 0027

* **[Ticket: 788767 / FISCAL01-130]** Ao gerar a rotina Convênio ICMS 115/03, o sistema está emitindo a mensagem de consistência “Prezado Cliente, identificamos que não foram executados os Scripts "LI.2017.02\_01" e "LI.2017.04\_01" necessários para geração da rotina Convênio ICMS 115/03. Favor entrar em contato com o Suporte para que os Scritps sejam disponibilizados.”, mesmo após os scripts terem sido executados na Base de Dados.Foi constatado que a validação está verificando um dos Scripts de forma errônea. O sistema está verificando o código “LI.2017.04\_01”, enquanto o correto seria “LI.2017.04\_02”.Foi realizada uma alteração na geração da rotina Convênio ICMS 115/03 para que seja verificada a execução do Script “LI.2017.04\_02” em vez do Script “LI.2017.04\_01”.

Arquivo: RM.Fis.RotinasFiscais.Form.dll

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS EFD PIS COFINS LI 01 0033

* **[Ticket: 637128 / FISCAL01-117]** Ao gerar a EFD Contribuições, o sistema não estava contemplando determinado lançamento Financeiro (Id. Lan. 1600), gerado no registro “F525”, ao somar os valores a serem gerados no campo “VL\_TOT\_REC” do registro “1900”.Foi constatado que o Lançamento Financeiro não estava sendo contemplado no somatório do campo no registro “1900” pelo fato de não ter um CFOP válido. Foi analisado que essa situação pode acontecer, pois se trata de um recibo de Aluguel.Foi realizada uma alteração na geração do campo “VL\_TOT\_REC” do registro “1900” para que sejam contemplados no somatório do campo Lançamentos Financeiros que não possuam CFOP.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 734177 / FISCAL01-111]** Alteração no processo do SPED Fiscal para somar os valores do C197 gerando apenas 1 registro quando o codigo de ajuste for o mesmo.

Arquivo: RM.Fis.Sped.Server.dll

## TOTVS Gestão Hospitalar

### Rotina: ALTO CONSUMO DE RECURSOS SGBD 90 25

* **[Ticket: 653588 / MSAU-7760]** Melhorias de performance no sistema em busca de nolocks faltando nas tabelas: 'SZATENDIMENTO’, ’SZSUSPROCREGISTRO’, ’SZTIPOATENDIMENTO’, ’SZESPECPRESTADOR’, ’SZESPECIALIDADE’

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: sistema não está considerando o calendário vinculado à Unidade de Atendimento

* **[Ticket: 705892 / MSAU-7390]** Ajustes na Agenda de atendimentos.

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

### Rotina: Tag de Senha vazia

* **[Ticket: 694052 / MSAU-7387]** Ajuste para que o sistema não emita a tag senha caso não haja dados para o mesmo

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Gestão Patrimonial

### Rotina: CONCEITO IMPORTAÇÃOEXPORTAÇÃO CON11

* **[Ticket: CONTROLADORIA01-143]** Atualizaçao do serviço solicitado pelo fiscal para retornar os valores da depreciação ajustada também da tabela histórica de calculo.

Arquivo: RM.Pat.Utils.Server.dll

### Rotina: OPERACOES PATRIMONIAIS BAIXA PAT 37 46

* **[Ticket: 651321 / CONTROLADORIA01-79]** Atualização no processo de baixa de patrimônios avaliados

Arquivo: RM.Pat.Ocorrencia.Service.dll

## TOTVS Incorporação

### Rotina: ADITIVO ANTECIPACAO DE PARCELA IMB 49 781

* **[Ticket: 720310 / TINPAD001-141]** Melhoria no cálculo da antecipação de parcelas utilizando o tipo "Valor Presente Meses"

Arquivos: RM.Imb.Venda.Calc.CalculosBase.Controller.dll, RM.Imb.Aditivos.Server.dll

### Rotina: Arquitetura do Reajuste Revitalizado

* **[Ticket: TINREV001-1]** Incluir o CNPJ da construtora Segura como piloto da revitalização.

Arquivos: RM.Imb.Conversor.Server.dll, RM.Imb.Venda.Upg.Data.dll

* **[Ticket: TINREV001-1]** melhoria no importador de parcelas para manter a data de pagamento informado na xaparcelapagamento e respeitar a configuração do nro de documento informado pelo parâmetro

Arquivos: RM.Imb.Conversor.Form.dll, RM.Imb.Facade.dll, RM.Imb.Conversor.Data.dll

* **[Ticket: TINREV001-1]** As parcelas já estão bloqueadas por divergências do sistema não podem ser bloqueadas novamente.

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

* **[Ticket: TINREV001-1]** melhoria no importador de parcelas para manter a data de pagamento informado na xaparcelapagamento e respeitar a configuração do nro de documento informado pelo parâmetro

Arquivos: RM.Imb.Contratos.Server.dll, RM.Imb.Conversor.Data.dll

### Rotina: Desconto com 4 casas decimais

* **[Ticket: 443485 / TINPAD001-99]** Melhoria no aditivo de antecipação de parcelas para gerar os valores de desconto com duas casas decimais.

Arquivo: RM.Imb.Aditivos.Server.dll

### Rotina: Reajuste diferente entre versões - URGENTE

* **[Ticket: 731371 / TINPAD001-143]** Ajuste para calcular corretamente o valor de CM que compõe a base de cálculo do juros (VO+CM do Mês de Reajuste), considerando o parâmetro de Ignorar Deflação para calcular .

Arquivo: RM.Imb.Reajuste.Server.dll

### Rotina: VENDA - CADASTRO IMB49868

* **[Ticket: TINPAD001-174]** Incluir a Unicos como piloto

Arquivo: RM.Imb.Venda.Upg.Data.dll

## TOTVS Manutenção

### Rotina: ORDEM DE SERVICOS MNT 1 5 4 4

* **[Ticket: 702485 / MATESTCNTFTOF01-165]** Melhoria no processo de Cancelar Ordem de Serviço para correta execução pela Nova MDI.

Arquivos: RM.Mnt.OrdemServico.Form.dll, RM.Mnt.OrdemServico.Service.dll, RM.Mnt.OrdemServico.Data.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: SMT COMISSAO INTERNA DE PREVENCAO DE ACIDENTES CIPA SMT 36 012

* **[Ticket: 596445 / MRH-8199]** Correção ao cancelar uma eleição, eliminando primeiramente a estabilidade,bloqueio ao tentar realizar cancelamento de uma eleição finalizada efoi retirada a trava para excluir candidato após o cancelamento da eleição.

Arquivos: RM.Smt.Cipa.Intf.dll, RM.Smt.Cipa.Data.dll, RM.Smt.Cipa.Form.dll

* **[Ticket: 596445 / MRH-8199]** Correção ao deletar candidato.

Arquivo: RM.Smt.Cipa.Data.dll

# 12.1.15.143

## Outros

### Rotina: FRM 001

* **[Ticket: MFRWBH-1687]** Retorno correto do Contexto no método GetXmlSession do WebMethod wsCorporeNet do Portal

Arquivos: Portal Corpore.Net

## TOTVS Automação de Ponto

### Rotina: FAIXAS DE HE AUTORIZADAS PONA300

* **[Ticket: MRH-6192]** Foi alterado o processo de inclusão de faixas extras com o objetivo de corrigir o erro apresentado.

Arquivo: RM.Pto.Parametros.Data.dll

### Rotina: PROCESSO DE CALCULO OCORRENCIA 0043 PTO 35 1280

* **[Ticket: 743165 / PONTO01-77]** Alterações no processo de modificação de batidas para permitir a exclusão de batidas provenientes da integração.

Arquivo: RM.Pto.Batida.Data.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 609891 / MRH-8517]** Foi criada a opção que permite escolher para quais funcionários serão exibidas as descrições de feriados

Arquivos: RM.Pto.Funcionario.Data.dll, RM.Pto.Relatorio.Form.dll, RM.Pto.Relatorio.Data.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** Alteração da criação da PKVEXAMESPENDENTES na tabela VEXAMESPENDENTES para que não ocorra o erro de violação de chave primária

Arquivo: Cvn.12.1.15.sql

## TOTVS Business Connect

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: 734461 / MFRWBH-1567]** Melhoria no serviço WsProcess para que retorne o schema necessário para execução do processo a partir do nome da classe de processo.

Arquivos: RM.Lib.dll, RM.Con.Conector.Interface.dll, RM.Con.TotvsMessage.Intf.dll, RM.Lib.Server.dll, RM.Con.Conector.Service.dll, RM.Con.TotvsMessage.Server.dll

## TOTVS Construção e Projetos

### Rotina: ARVORE DO RELATORIO RPT 00037

* **[Ticket: 769260 / TOPORCAPLAN001-210]** Relatório TOPREL043 não está exibindo composições globais

Arquivo: RM.Prj.Relatorios.Server.dll

### Rotina: IMPORTAR ARQUIVOS EMOP PRJ 33 832

* **[Ticket: 661845 / TOPORCAPLAN001-206]** Ajustado para que seja possível utilizar os arquivos convertidos em XML para importação EMOP em ambientes 62 bits.Esta conversão deve ser realizada através do aplicativo “RM.ConvertDBToXML.exe” existente no diretório de instalação, o mesmo consiste em converter o(s) arquivo(s) \*.DBF para o formato \*.XML.

Arquivos: RM.Prj.Utils.Intf.dll, RM.Prj.Importacao.Form.dll

## TOTVS Educacional

### Rotina: ACADEMIA SOCIAL EDU 51036

* **[Ticket: 753632 / EDUCACIONAL01-633]** Ajuste no cadastro da equivalência para que quando se apaga uma equivalência seja apagado os dados das tabelas SDISCGRUPOEQ e SGRUPOEQ referente a sua equivalência.

Arquivos: RM.Edu.Matricula.Server.dll, RM.Edu.MatrizCurricular.Data.dll

### Rotina: GERACAO DE MOVIMENTO EDU 50 229

* **[Ticket: 771827 / EDUCACIONAL01-634]** Melhoria na geração de lançamento para que não seja gerado TMOVLAN quando ocorreu a geração de movimento por competência para o contrato e utilizou o recurso de cálculo do valor líquido do movimento por fórmula.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: PORTAL CONTEXTO EDU 50 475

* **[Ticket: 579181 / PORTALMOBILE01-295]** Ajuste nas consultas do contexto para validar quando o coordenador e os professores listados estão demitidos ou não.

Arquivo: RM.Edu.Contexto.Data.dll

### Rotina: Project-774348 #pilotoparticipativos – Reserva de recurso: hora de alteração do cadastro não está sendo gravada Project-

* **[Ticket: 776551 / EDUCACIONAL01-588]** Otimizado tela de Reserva de instalação, para demonstrar no campo “Data Alteração” a hora também.

Arquivos: RM.Edu.Professor.Intf.dll, RM.Edu.Professor.Form.dll

## TOTVS Folha de Pagamento

### Rotina: FOLHA ANALITICA LAB 01 112

* **[Ticket: 739656 / FOPCALCULO01-43]** Ajuste na rotina de geração de Folha Analítica, para não considerar caracteres especiais no tratamento da descrição.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: GRUPO DE EVENTOS LAB 01 116

* **[Ticket: 799249 / FOPROTINAS01-290]** Para que as manutenções de lotação de anos anteriores fossem contempladas no primeiro mês do ano corrente todas as manutenções de lotação de anos anteriores passam a ser processadas para que seja refletida a situação fidedigna de cada funcionário no ano corrente do orçamento.

Arquivo: RM.Fop.Orcamento.Data.dll

## TOTVS Framework

### Rotina: FILTRO FILTRO DE PERFIL CADASTRO FRW 00026

* **[Ticket: 588888 / MFRWBH-1682]** -As permissões concedidas em acesso a campos devem ser refletidas nas telas de parametros dos produtos.

Arquivo: RM.Lib.WinForms.dll

### Rotina: FORMULA VISUAL FVS 01

* **[Ticket: MFRWBH-1689]** Melhoria na atividade Ler Parâmetros do Processo da Fórmula Visual

Arquivo: RM.Lib.Workflow.Activities.dll

### Rotina: GERENCIAMENTO DE JOBS FRW 00036

* **[Ticket: 807129 / MFRWBH-1693]** Duarante a execução do processo via jobsRunner será exibido o alias que o processo está relacionado.

Arquivo: RM.Lib.Jobs.Server.dll

### Rotina: TABELA MTD 00013

* **[Ticket: 798064 / MFRWBH-1678]** -Ao modificar uma tabela do metadados o sistema deve salvar as alterações corretamente.

Arquivo: RM.Glb.Metadata.Data.dll

## TOTVS Gerador de Relatórios

### Rotina: GERACAO DE RELATORIO RPT 00005

* **[Ticket: 770972 / MFRWBH-1631]** Margens do relatório desabilitadas.

Arquivo: RM.Rpt.Reports.Form.dll

### Rotina: RELATORIO

* **[Ticket: MFRWBH-1688]** Relatórios que são submetidos após a alteração dos parâmetros, agora apresenta uma janela informando a geração dos mesmos.

Arquivo: RM.Rpt.Reports.Form.dll

* **[Ticket: MFRWBH-1692]** -Resources da Mensagem de Geração de Relatórios Adicionados na v12.1.15-Remoção de código comentado da funcionalidade de Rotação de Imagem que deve ser disponível a partir da versão 12.1.17.

Arquivo: RM.Rpt.Reports.Form.dll

## TOTVS Gestão Contábil

### Rotina: SPED CONTABIL CADASTROS CTB 38 132

* **[Ticket: 744766 / CONTROLADORIA01-134]** Ajuste na geração do registro I157 para que mostre todas as contas quando existe a transferência de saldo de mais de uma conta para apenas uma conforme esta previsto no manual.

Arquivo: RM.Ctb.Sped.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CONCLUIR PEDIDO MOV 008

* **[Ticket: 623177 / MATFATCMPCRM01-97]** Se selecionarmos dois movimentos com o status(Parc.Faturado) e tentar concluir os movimentos o sistema irá alterar o status de um dos movimentos para "Faturado" eo outro continuará como "Parc.Faturado porém se tentar concluir apenas um movimento o sistema apresentará a mensagem: "O movimento selecionado não possui item originados deste módulo para serem concluídos".

Arquivo: RM.Mov.Processos.Data.dll

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 538357 / MATFATCMPCRM01-260]** Melhorias no processo responsável por agrupar itens repetidos no faturamento.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: INVENTARIO ENCERRAR

* **[Ticket: MATESTCNTFTOF01-39]** Melhoria na manutenção de Item de Inventário para incluir o Número do Lote automaticamente quando o Inventário for por Número de Série.

Arquivos: RM.Est.Inventario.Data.dll, RM.Est.Inventario.Form.dll

### Rotina: MEDICAO DE CONTRATO CTR 017

* **[Ticket: 798967 / MATESTCNTFTOF01-198]** Ajuste na rotina que verifica se a soma/quantidade das medições estão corretas.

Arquivo: RM.Ctr.Contrato.Service.dll

### Rotina: PARAMETRIZAÇÃO - TIPO DE MOVIMENTO PAR014

* **[Ticket: 95207 / MATFATCMPCRM01-25]** Implementação para que ao gerar faturamento automático no movimento e quando possui os tributos PIS/COFINS seja apresentado o campo TIPOCREDITO no movimento 2.1xx.

Arquivo: RM.Mov.Movimento.Data.dll

### Rotina: PROCESSOS DO PRODUTO PRD 002

* **[Ticket: 672227 / MATESTCNTFTOF01-178]** Melhoria no processo de Cópia de Produtos entre Coligadas para consistir alteração da Unidade de Controle do Produto. Quando a Unidade de Controle do Produto for alterada na Coligada Origem, ao realizar a Cópia deste produto para Coligada Destino, caso este produto possua movimentação de estoque na coligada destino a cópia não será realizada.

Arquivos: RM.Est.Produto.Service.dll, RM.Est.Produto.Data.dll

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: 662515 / MATFATCMPCRM01-172]** Melhorias na tela de recebimento de NF-e do TOTVS Colaboração.

Arquivos: RM.Mov.Integracoes.Intf.dll, RM.Mov.Integracoes.Data.dll, RM.Mov.Integracoes.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: REQUISICOES GERAL RHU 36 508

* **[Ticket: 740099 / RHU01-29]** Realizado ajuste em filtro por perfil em requisição de substituição.

Arquivo: RM.Rhu.Requisicao.Server.dll

## TOTVS Gestão Financeira

### Rotina: ACORDO ALTERACAO EXCLUSAO FIN 001

* **[Ticket: 707787 / FINANCEIRO01-529]** Adicionada a validação da database de geração do Imposto de Renda para os lançamentos selecionados para geração do acordo.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO DE PAGAMENTO FIN 238

* **[Ticket: 636655 / FINANCEIRO01-109]** Otimização no processo de importação de arquivo de retorno de pagamento. Agora o sistema importa e interpreta arquivos de retorno do bano Deutsche - 487 que possuem assentos. Os arquivos são convertidos para o formato UTF-8 (Tabelas código "65001") para tratamento de acentuação e caracteres especiais.

Arquivos: RM.Fin.Banco.Data.dll, RM.Fin.Lib.dll

### Rotina: SESSAO DE CAIXA BAIXA FIN 269

* **[Ticket: 773111 / FINANCEIRO01-558]** Ajuste na pesquisa pelo IPTE no modulo de caixa

Arquivo: RM.Fin.SessaoCaixa.Data.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS EFD PIS COFINS LI 01 0033

* **[Ticket: 637128 / FISCAL01-117]** Ao gerar a EFD Contribuições, o sistema não estava contemplando determinado lançamento Financeiro (Id. Lan. 1600), gerado no registro “F525”, ao somar os valores a serem gerados no campo “VL\_TOT\_REC” do registro “1900”.Foi constatado que o Lançamento Financeiro não estava sendo contemplado no somatório do campo no registro “1900” pelo fato de não ter um CFOP válido. Foi analisado que essa situação pode acontecer, pois se trata de um recibo de Aluguel.Foi realizada uma alteração na geração do campo “VL\_TOT\_REC” do registro “1900” para que sejam contemplados no somatório do campo Lançamentos Financeiros que não possuam CFOP.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: CADASTRO DE PACIENTE SAU 47 1193

* **[Ticket: 614043 / MSAU-8168]** Ajuste realizado para que o sistema não atualize o campo de referencia com o código incorreto quando acontecer qualquer exceção no código.

Arquivo: RM.Sau.Cadastros.Server.dll

### Rotina: Tiss - Unimed

* **[Ticket: 761680 / MSAU-8048]** Ajuste realizado no formulário Faturamento/Faturamento para Convênios, para que ao faturar a conta seja inserido o número correto de encerramento.

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: PCMSO CID SMT 36 548

* **[Ticket: 632405 / MRH-9178]** Realizado ajuste no assistente de agendamento automático.

Arquivo: RM.Smt.Clinico.Data.dll

# 12.1.15.144

## TOTVS Automação de Ponto

### Rotina: CADASTRO

* **[Ticket: PONTO01-13]** Alterações no método de cadastro de horários de funcionários.

Arquivo: RM.Pto.Horario.Data.dll

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 659375 / PONTO01-80]** Foi realizado o ajuste para que a natureza no processo de importação de batidas quando parametrizada para considerar o horário planejado seja calculada corretamente.

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: PORTAL WEB ABONAR ATRASOS E FALTAS PTO 35 1257

* **[Ticket: 433306 / MRH-9252]** Correções feitas na tela de solicitação de abono para permitir o processo de edição de abonos.

Arquivo: RM.Pto.AprovarAbonos.WebForm.dll

## TOTVS Business Connect

### Rotina: IMPORTACAO DE OBJETOS GERENCIAIS FRW 00041

* **[Ticket: 770922 / MFRWBH-1703]** -Otimização do conceito quando utiliza planilha Excel.

Arquivo: RM.Con.Concept.dll

## TOTVS Construção e Projetos

### Rotina: MENSAGEM UNICA CADASTRO PROJETO OBRA E TAREFA PRJ 33 918

* **[Ticket: 812287 / TOPEXECONTROL01-118]** Ajuste no SOURCECODE das mensagens de envio de obra e etapa da integração "TOTVS Obras e Projetos x BackOffice Protheus".

Arquivo: RM.Prj.TotvsMessage.Configurador.Protheus.dll

### Rotina: PRJ 33 902

* **[Ticket: TOPORCAPLAN001-243]** Erro no sincronismo com project ao utilizar o project como mandatário

Arquivos: RM.Prj.Planilhas.Data.dll, RM.Prj.Contrato.Intf.dll, RM.Prj.Contrato.Data.dll

## TOTVS Educacional

### Rotina: CERTIFICADOS DIPLOMAS TIPOS DE CERTIFICACAO EDU 50 123

* **[Ticket: 726324 / EDUCACIONAL01-149]** Novos tipos de certificados. Alteração no processo de geração de certificados e no cadastro de certificados para permitir que sejam gerados os novos tipos de certificados e que possam ser rastreados com base nos registros que os certificados foram gerados.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Lib.Intf.dll, RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.PesquisaExtensao.Intf.dll, RM.Edu.Academico.Data.dll, RM.Edu.Academico.Form.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.PesquisaExtensao.Data.dll

### Rotina: PORTAL ALUNO DADOS PESSOAIS EDU 50 349

* **[Ticket: 763744 / PORTALMOBILE01-264]** Alteração para exibir o Nome Social no Portal Educacional, quando isso está parametrizado na base do cliente.

Arquivos: RM.Edu.Contexto.Data.dll, RM.Edu.Matricula.Data.dll, RM.Edu.Processos.Server.dll, RM.Edu.Aluno.Data.dll, App\_Web\_edualunowebform.ascx.1d4ca059.dll

### Rotina: Project-774348 #pilotoparticipativos – Reserva de recurso: hora de alteração do cadastro não está sendo gravada Project-

* **[Ticket: 776551 / EDUCACIONAL01-588]** Ao realizar o processo de reserva de recurso, o sistema emitia incorretamente mensagem de “Não existe recurso disponível para o horário”, caso o recurso não tenha preenchido o anexo “Associação de recurso ao espaço físico”. Um recurso poderá ter ou não espaço físico associado, portanto deverá permitir a reserva independente do espaço físico. Este efeito existia desde a criação do anexo.

Arquivo: RM.Edu.Professor.Server.dll

### Rotina: Project-784239 Problema com complemento de disciplinas Project-784239

* **[Ticket: 789357 / PORTALMOBILE01-358]** Melhoria no processo de liberação de complemento da disciplina, validando se o professor está autorizado a atualizar o complemento.

Arquivos: RM.Edu.MatrizCurricular.Data.dll, App\_Web\_eduprofcompldiscwebform.ascx.9bc05ab5.dll, App\_Web\_edudisciplinasprofwebform.ascx.497dfae.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIOS HISTORICOS FOP 34 499

* **[Ticket: 733177 / FOPCALCULO01-204]** Ajustado para só apagar os dados caso esteja sendo considerado a Tabela Salarial.Onde o Nível e a Faixa não estejam vinculado a Tabela Salarial.

Arquivos: RM.Fop.Funcionario.Intf.dll, RM.Fop.Funcionario.Data.dll, RM.Fop.Funcionario.Form.dll

### Rotina: PARAMETRIZADOR FOLHA DE PAGAMENTO LAB 01 36

* **[Ticket: 656652 / FOPROTINAS01-203]** Ajuste no cálculo do orçamento para considerar os dados do funcionário na lotação na hora de fazer a seleção para lançamento do grupo de eventos

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Orcamento.Data.dll

## TOTVS Framework

### Rotina: RELACIONAMENTO MTD 00011

* **[Ticket: 763305 / MFRWBH-1623]** Melhoria na configuração de anexos para os cadastros

Arquivo: RM.Lib.WinForms.dll

## TOTVS Framework Web

### Rotina: PORTAL

* **[Ticket: MFRWBH-1699]** Melhoria na aplicação de Mascara contendo hífen no portal

Arquivo: RM.Lib.Web.dll

## TOTVS Gerador de Relatórios

### Rotina: IMPRESSAO DELPHI REL 00008

* **[Ticket: 547053 / MFRWBH-1268]** Melhoria para que a expressão possa utilizar as células de tabelas.

Arquivo: RM.Rpt.Reports.Form.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 746744 / CONTROLADORIA01-99]** Adequação do layout 5.0 para atender a mudança na legislação e passar a preencher o campo 18 do registro 0000 com o CNPJ da SCP quando o tipo de ECD for "ECD da SCP" como determinado no manual da ECD.

Arquivos: RM.Ctb.Sped.Service.dll, RM.Ctb.Sped.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: MOV ESTOQUE TERCEIROS EST 004

* **[Ticket: 610402 / MATESTCNTFTOF01-41]** Melhoria no processo de parametrização de Estoque de Terceiros / De Terceiros. O Motivo de Referência = 11 – Retorno de Mercadoria não Aplicada na Industrialização passa a aceitar o efeito no saldo como "Diminui" para o Saldo Com Terceiros ou para o Saldo De Terceiros.

Arquivo: RM.Mov.Parametros.Data.dll

### Rotina: PARAMETRIZAÇÃO - TIPO DE MOVIMENTO PAR014

* **[Ticket: 95207 / MATFATCMPCRM01-25]** Remoção da regra aplicada à NF-e Estadual, tendo em vista que um movimento do tipo 2.1.xx não pode gerar este documento, tanto manualmente quanto automaticamente. Somente um movimento do tipo 2.2.xx poderá possuir tais características.

Arquivo: RM.Mov.Movimento.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: FUNCIONARIOS RHU 36 035

* **[Ticket: 741104 / FOPROTINAS01-332]** Realizado ajuste de forma a melhorar a performance da AD.

Arquivo: RM.Rhu.Facade.dll

### Rotina: REQUISICOES AUMENTO DE QUADRO RHU 36 095

* **[Ticket: 747439 / RHU01-87]** Agora os e-mails estão sendo enviados com o usuário logado.

Arquivo: RM.Rhu.Requisicao.Server.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA RESGATE FIN 017

* **[Ticket: 586771 / FINANCEIRO01-91]** Tratamento cálculo IR/IOF quando rendimento negativo.

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

* **[Ticket: 716341 / FINANCEIRO01-131]** Disponibiliza predisposição prara registro de log de processamento

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

### Rotina: EXTRATO DE CAIXA REGERAR CONTABILIZACAO FIN 152

* **[Ticket: 723632 / FINANCEIRO01-181]** Melhorado a busca do lançamento em contextos de contabilização de extrato.

Arquivo: RM.Fin.Formula.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 807185 / FINANCEIRO01-586]** Melhoria no processo de retorno bancário - Efetuar a baixa do boleto ao realizar o retorno agrupando os lançamentos em um único extrato

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SESSAO DE CAIXA BAIXA FIN 269

* **[Ticket: 773111 / FINANCEIRO01-558]** Ajuste na sentença sql da pesquisa pelo historico do boleto para funcionar em base oracle

Arquivo: RM.Fin.SessaoCaixa.Data.dll

## TOTVS Gestão Fiscal

### Rotina: NFS E ATUALIZACAO DE MUNICIPIOS HOMOLOGADOS NF 01 0023

* **[Ticket: 810120 / FISCAL01-310]** Alteração do layout do envio de NFS-e para o municipio de Niterói - RJ

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS EFD PIS COFINS LI 01 0033

* **[Ticket: 292183 / FISCAL01-99]** Foi criado um novo parâmetro para a geração da EFD Contribuições, trata-se do “Gerar no Registro C100 notas de Entrada Sem Direito a Crédito (PIS/COFINS)”. Ao informar “Não” nesse parâmetro, o sistema não gerará no registro C100 as notas de Entrada, no Regime Cumulativo, cujo CST dos tributos PIS e COFINS seja 70,71,72,74,75 ou 98.

Arquivos: RM.Fis.Sped.Intf.dll, RM.Fis.Sped.Server.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES PRINCIPAIS SIMPLES NACIONAL LI 01 0050

* **[Ticket: 716763 / FISCAL01-87]** - Criado script para excluir dados de últimas receitas vinculados a cenários que não existem no sistema e criação de constraint entre as tabelas DPERIODOSN e DCENARIOSN;- Efetuada melhoria na apuração do Simples Nacional para que o valor do campo "Receita 12 últimos" seja calculado corretamente no mês de janeiro quando não há apuração no ano anterior. Na situação citada, sistema deverá carregar o valor das receitasapuradas em janeiro e multiplicar por 12. Nos demais meses sistema fará a média aritmética entre o valor das receitas anteriorese quantidade de meses anteriores apurados multiplicada por 12.

Arquivo: RM.Fis.ApuracaoTrb.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: erro no registro de plantão

* **[Ticket: 678766 / MSAU-7326]** Ajustes na tela de Plantão e criação de novo processo para Inativação de Plantões

Arquivos: RM.Sau.RegistroAtendimento.Intf.dll, RM.Sau.RegistroAtendimento.Data.dll, RM.Sau.RegistroAtendimento.Form.dll

### Rotina: Tiss - Unimed

* **[Ticket: 761680 / MSAU-8048]** Ajuste realizado no formulário Faturamento/Faturamento para Convênios, para que ao faturar a conta seja inserido o número correto de encerramento.

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Gestão Patrimonial

### Rotina: OPERACOES PATRIMONIAIS IMPAIRMENT PAT 37 105

* **[Ticket: 636248 / CONTROLADORIA01-32]** Foi adicionado o campo Valor Impairment na aba Saldo do Cálculo Patrimonial, existente nos cenários de cálculo do cadastro de patrimônio. Ele deve ser preenchido após o fechamento de todos os períodos anteriores a competência atual e, em seguida, a depreciação do patrimônio deve ser recalculada. Após este procedimento é possível realizar a recuperação do impairmet.

Arquivos: RM.Pat.CalculoPatrimonio.Intf.dll, RM.Pat.CalculoPatrimonio.Data.dll, RM.Pat.CalculoPatrimonio.Form.dll

### Rotina: OUTROS

* **[Ticket: CONTROLADORIA01-145]** O processo de fechamento de período sofreu modificações para que seja possível realizar reversão de impairment após o fechamento.

Arquivo: RM.Pat.Periodicidade.Data.dll

## TOTVS Incorporação

### Rotina: Arquitetura do Reajuste Revitalizado

* **[Ticket: TINREV001-1]** melhoria no cálculo da ficha financeira para tratar valor nulo da parcela na regra

Arquivo: RM.Imb.Relatorio.Data.dll

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhoria para o processo de revitalização.

Arquivo: RM.Imb.Venda.Upg.Data.dll

# 12.1.15.145

## TOTVS Automação de Ponto

### Rotina: CALCULO PONTO ELETRONICO

* **[Ticket: PONTO01-152]** Realizado uma melhoria no cálculo para um problema de performance que envolvia a GAUTOINC.

Arquivo: RM.Pto.Facade.dll

### Rotina: PROCESSO DE CALCULO OCORRENCIA 0043 PTO 35 1280

* **[Ticket: 720489 / PONTO01-17]** O processamento de alteração de de atitude de ocorrência teve sua performance melhorada reduzindo simplificando o uso do banco de dados.

Arquivo: RM.Pto.Ocorrencia.Data.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** Remoção da Primary Key PKVPDIMETAS da tabela VPDIMETAS.

Arquivo: Cvn.12.1.15.sql

## TOTVS Construção e Projetos

### Rotina: GERACAO DE PEDIDOS EXTRA PRJ 33 829

* **[Ticket: 783737 / TOPEXECONTROL01-121]** Ajuste realizado ao gerar o código do pedido extra.

Arquivos: FrameHTML

## TOTVS Educacional

### Rotina: CERTIFICADOS DIPLOMAS TIPOS DE CERTIFICACAO EDU 50 123

* **[Ticket: 726324 / EDUCACIONAL01-149]** Novos tipos de certificados. Alteração no processo de geração de certificados e no cadastro de certificados para permitir que sejam gerados os novos tipos de certificados e que possam ser rastreados com base nos registros que os certificados foram gerados.

Arquivo: RM.Edu.Academico.Form.dll

### Rotina: Erro ao acessar o Portal com o Login do professor

* **[Ticket: PORTALMOBILE01-417]** Ajuste na consulta que verifica se o professor e coordenador não estão demitidos

Arquivo: RM.Edu.Contexto.Data.dll

### Rotina: IMPRIMIR RELATORIO TURMAS DISCIPLINAS EDU 50 274

* **[Ticket: 790525 / EDUCACIONAL01-681]** Melhoria no cadastro de complemento da disciplina para que a formatação do texto respeite a parametrização do recuo de parágrafo.

Arquivo: RM.Edu.Lib.WinForms.dll

### Rotina: OUTROS

* **[Ticket: EDUCACIONAL01-171]** As configurações do Censo foram alteradas para permitir selecionar apenas consultas da coligada do contexto.

Arquivo: RM.Edu.Cadastros.Form.dll

## TOTVS Folha de Pagamento

### Rotina: FOLHA ANALITICA LAB 01 112

* **[Ticket: 449081 / FOPROTINAS01-141]** Para controlar a exibição dos totais de seção contendo base de FGTS de afastados, foi criado o parâmetro "Filtrar Base de FGTS de Afastados por Período" através de um checkbox no Wizard da Folha Analítica. Quando esse parâmetro é marcado, o sistema exibirá os totais apenas das seções onde há funcionários com movimento no período (considerando que o cliente não marcou o parâmetro para imprimir funcionários sem movimento). Se o parâmetro permanecer desabilitado, o sistema continuará exibindo totais de seção contendo base de FGTS de afastados onde há funcionários afastados no período, mesmo que o funcionário não tenha movimento.

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Data.Intf.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Data.Server.dll, RM.Fop.Relatorios.Data.dll

### Rotina: FUNCIONARIOS HISTORICOS FOP 34 499

* **[Ticket: 733177 / FOPCALCULO01-204]** Ajuste Correção Retrabalho

Arquivos: RM.Fop.Funcionario.Intf.dll, RM.Fop.Funcionario.Data.dll, RM.Fop.Funcionario.Form.dll

## TOTVS Framework

### Rotina: ACTIONS ANEXAS FRW 00001

* **[Ticket: 614672 / MFRWBH-1691]** Melhoria na abertura da visão de produtos quando a action de Dados Fiscais por UF está configurada como um anexo ativo e obrigatório na action de produtos.

Arquivo: RM.Lib.WinForms.dll

### Rotina: FORMULA VISUAL FVS 01

* **[Ticket: 677061 / MFRWBH-1501]** Melhoria na atividade de fórmula visual para executar web services, permitindo a utilização dos métodos disponíveis no serviço.

Arquivo: RM.Lib.Workflow.Activities.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: BLOCO K FIS 006

* **[Ticket: 717572 / MATESTCNTFTOF01-159]** Melhoria ao gerar o Bloco K. Para os registros que necessitam da consistência da "Situação da Mercadoria" em Anexos | Dados Fiscais do Produto, seja considerada também a consistência da aba Informações por Filial campo "Situação da Mercadoria". Isso porque em alguns casos um mesmo Produto pode ter classificação diferente por Filial. Primeiramente será verificado se existe a informação da situação da mercadoria na tabela de informações por filial. Caso não exista, será utilizado a informação disponível no cadastro de dados fiscais do produto.

Arquivo: RM.Est.Estoque.Service.dll

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 538357 / MATFATCMPCRM01-260]** Ao editar a quantidade dos itens que são controlados por lote para menor antes de realizar o agrupamento o sistema acusa o seguinte erro:"Objeto não pode ser convertido de DBNull em outros tipos."

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: QUADRO COMPARATIVO COTACAO COM 009

* **[Ticket: 580659 / MATFATCMPCRM01-124]** Houve um ajuste ao gerar o quadro comparativo na tela, agora esse ajuste, foi replicado para o processo que imprime o quadro comparativo em um relatório.

Arquivo: RM.Cmp.Cotacao.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: REQUISICOES SUBSTITUICAO RHU 36 504

* **[Ticket: 758997 / RHU01-80]** Ajuste para efetivar requisição de substituição de horista com salário correto

Arquivos: RM.Rhu.Requisicao.Intf.dll, RM.Rhu.Lib.WinForms.dll, RM.Rhu.Requisicao.Data.dll

## TOTVS Gestão Financeira

### Rotina: BAIXAS REALIZADAS ANEXO LANCAMENTO FIN 022

* **[Ticket: 462701 / FINANCEIRO01-351]** Ajuste feito no processo de "Baixar Créditos/Devoluções Vinculados" para calcular corretamente as retenções após a baixa, quando é baixado totalmente o lançamento de nota fiscal.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: BOLETO REMESSA COBRANCA ELETRONICA FIN 046

* **[Ticket: 742125 / FINANCEIRO01-178]** Ajuste na montagem do código de barras para banco Caixa Econômica Federal e carteira 11, nesse caso o valor não deve ser gerado.

Arquivos: RM.Fin.Banco.Service.dll, RM.Fin.Lan.Service.dll

### Rotina: INTEGRACAO PROTHEUS BACKOFFICE EDU 50 466

* **[Ticket: 788142 / EDUCTB001-568]** Ajuste na nova Integração Educacinal x BackofficeProtheus.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS MUNICIPAIS LI 01 0034

* **[Ticket: 639694 / FISCAL01-1]** Implementação da Rotina Municipal RMD (Registro de Materiais Dedutíveis)

Arquivo: RM.Fis.Sped.Server.dll

## TOTVS Gestão Hospitalar

### Rotina: erro no registro de plantão

* **[Ticket: 678766 / MSAU-7326]** Ajustes na tela de registro de plantão.

Arquivos: RM.Sau.RegistroAtendimento.Intf.dll, RM.Sau.RegistroAtendimento.Data.dll, RM.Sau.RegistroAtendimento.Form.dll

### Rotina: PEP OUTROS REGISTROS SAU 47 1120

* **[Ticket: 810463 / MSAU-8497]** Ajuste na liberação da prescrição de enfermagem.

Arquivo: RM.Sau.PepHis.Server.dll

## TOTVS Incorporação

### Rotina: Aditivo Cancelamento de Parcela

* **[Ticket: 717082 / TINPAD001-171]** Foi retirada a trava para executar o aditivo com o parâmetro "permitir renegociar sem multa de atraso e juros de mora" sempre desmarcado.Agora deverá ser executado sempre com este parâmetro marcadoO mesmo comportamento ocorre se o aditivo for de inclusão

Arquivos: RM.Imb.Aditivos.Form.dll, RM.Imb.Aditivos.Server.dll

### Rotina: Revitalização divergência de valores - Piloto

* **[Ticket: CPTIN001-478]** Melhoria no cadastro de condições de financiamento.

Arquivo: RM.Imb.Venda.Regra.Intf.dll

## TOTVS Planejamento e Controle da Produção

### Rotina: ESTRUTURA PCP 44 241

* **[Ticket: 616505 / MATESTCNTFTOF01-118]** Melhoria na seleção de estrutura

Arquivos: RM.PCP.Estruturas.Data.dll, RM.PCP.ItemOrdem.Form.dll

* **[Ticket: 616505 / MATESTCNTFTOF01-118]** Melhoria na seleção de estrutura

Arquivo: RM.PCP.Estruturas.Data.dll

# 12.1.15.146

## TOTVS Automação de Ponto

### Rotina: CALCULO PONTO ELETRONICO

* **[Ticket: PONTO01-152]** Correção do problema da criação de diversos jobs durante a solicitação de recálculo.

Arquivos: RM.Pto.Abono.Data.dll, RM.Pto.JustExcecao.WebForm.dll

* **[Ticket: PONTO01-152]** Otimização do cálculo para melhorar a performance

Arquivos: RM.Pto.BancoDeHoras.Data.dll, RM.Pto.Batida.Data.dll, RM.Pto.Calculo.Service.dll

## TOTVS Folha de Pagamento

### Rotina: Lançamento por centro de custo

* **[Ticket: 735123 / FOPROTINAS01-303]** Ajustado internamente para que o botão 'Lançamento por centro de custo' seja habilitado conforme parametrização informada no TDN

Arquivo: RM.Fop.Parametros.Form.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS ACOMPANHAMENTO ORCAMENTARIO CTB 38 125

* **[Ticket: 96687 / CONTROLADORIA01-102]** Ajuste no relatório para que as datas de Acumulo, Inicial e Final não geraram interseção nas duas pesquisas com a data Inicial ou seja, (Data Acumulo / Data Inicial) e (Data Inicial / Data Final).

Arquivo: RM.Ctb.Relatorios.Service.dll

### Rotina: RELATORIOS RAZAO CTB 38 114

* **[Ticket: 773664 / CONTROLADORIA01-149]** O relatório Razão Contábil foi alterado para que o Saldo Anterior das contas seja exibido sem cortes.

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INT PARAMETRIZACAO TBC WEBSERVICE INT 001

* **[Ticket: 672756 / MATFATCMPCRM01-372]** Melhorias na segurança do consumo de WebService.

Arquivo: RM.Mov.Movimento.Data.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA RESGATE FIN 017

* **[Ticket: 716341 / FINANCEIRO01-131]** Tratamento da rentabilidade do dia seguinte ao come-cotas.

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES PRINCIPAIS SIMPLES NACIONAL LI 01 0050

* **[Ticket: 755590 / FISCAL01-86]** Efetuada melhoria para que a partir de janeiro de 2016 os valores do campo "Receitas 12 úlitmos meses" sejam dividos por cenário de apuração do simples nacional.

Arquivo: RM.Fis.ApuracaoTrb.Service.dll

# 12.1.15.147

## CORPORE RM

### Rotina: PORTAL ALUNO MENSAGENS EDU 50 496

* **[Ticket: 775299 / MFRWBH-1403]** O envio de mensagens através do portal foi ajustado.

Arquivo: RM.Prt.Mensagens.Data.dll

## TOTVS Automação de Ponto

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 793333 / PONTO01-138]** Alteração no processo de importação de batidas para considerar de forma correta funcionários com dupla chapa em diferentes coligadas.

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: HORARIOS PTO 35 1180

* **[Ticket: 699901 / PONTO01-8]** Foi ajustado o registro de tolerâncias no cadastro de intervalos planejados de modo que o mesmo seja registrado e carregado adequadamente.

Arquivos: RM.Pto.Horario.Form.dll, RM.Pto.Horario.Data.dll

### Rotina: HORÁRIOS PTO351180

* **[Ticket: 97255 / MRH-267]** Mudanças realizadas para permitir que alterações realizadas no histórico de horário do portal reflitam no cadastro do funcionário.

Arquivos: Portal Corpore.Net

* **[Ticket: PONTO01-168]** Foi adicionado os tipos de ocorrência de extra e extras que foram compensados como consideração para o calculo de horas trabalhadas.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 745265 / PONTO01-93]** Método que valida se os funcionários selecionados pelo filtro possuem compensação de horas não considerava o filtro de quebra de seção. Foi feita a correção para considerar a quebra de seção na validação de compensação de horas.

Arquivos: RM.Pto.BancoDeHoras.Intf.dll, RM.Pto.Calculo.Form.dll, RM.Pto.BancoDeHoras.Data.dll

### Rotina: PORTAL WEB ABONAR ATRASOS E FALTAS PTO 35 1257

* **[Ticket: 824534 / PONTO01-150]** Foi realizado o ajuste do filtro que apresenta as ocorrências passíveis de serem abonadas no Portal Web.

Arquivo: RM.Pto.Abono.Data.dll

### Rotina: PROCESSO DE CALCULO DE HORAS EXTRAS PTO 35 1238

* **[Ticket: 788616 / PONTO01-124]** Correção do processo de distribuição de faixas extras para considerar a atitude do evento de forma correta, quando a opção estiver marcada na parametrização do sindicato.

Arquivo: RM.Pto.Calculo.Service.dll

## TOTVS Business Connect

### Rotina: ERRO DE SALDO AO REQUISITAR MATERIAL

* **[Ticket: 834981 / TOPEXECONTROL01-141]** Ajuste na composição do saldo solicitado em pedidos.

Arquivos: RM.Con.Obras.Data.dll, RM.Prj.Facade.dll, RM.Prj.PedidoMaterial.Server.dll

### Rotina: INTEGRACAO COM RM

* **[Ticket: 801714 / FOPROTINAS01-354]** Adicionado tratamento na mensagem de integração de funcionário do Protheus x RM para enviar o motivo de alteração salarial com 3 dígitos

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

* **[Ticket: 801714 / FOPROTINAS01-354]** Adicionado tratamento na mensagem de integração de funcionário do Protheus x RM para enviar o motivo de alteração salarial com 3 dígitos

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## TOTVS Construção e Projetos

### Rotina: COMPOSICAO CADASTRO PRJ 33 809

* **[Ticket: 712817 / TOPORCAPLAN001-244]** Lentidão na tela de edição de composição

Arquivo: RM.Prj.Contrato.Data.dll

* **[Ticket: 712817 / TOPORCAPLAN001-244]** Lentidão na tela de edição de composição

Arquivo: RM.Prj.Composicao.Form.dll

### Rotina: CONTRATOS ASSOCIACAO DE ITENS PRJ 33 939

* **[Ticket: 766263 / TOPEXECONTROL01-122]** Ajuste no processo de associar objetos no aditivo de contrato.

Arquivo: RM.Prj.Contrato.Form.dll

### Rotina: COPIA DE ITENS PRJ 33 779

* **[Ticket: 826616 / TOPORCAPLAN001-253]** Cópia de insumos com insumos ligados a planilhas e campo CODAPLIC nulo

Arquivo: RM.Prj.Insumo.Data.dll

## TOTVS Educacional

### Rotina: CERTIFICADOS DIPLOMAS TIPOS DE CERTIFICACAO EDU 50 123

* **[Ticket: 726324 / EDUCACIONAL01-149]** Ajustes no caption referente ao nome da pessoa na emissão do certificado do tipo Ações de extensão, comissão avaliadora.

Arquivos: RM.Edu.PesquisaExtensao.Data.dll, RM.Edu.PesquisaExtensao.Intf.dll

* **[Ticket: 726324 / EDUCACIONAL01-149]** Ajustes na criação de filtros nos novos tipos de certificados disponibilizados.

Arquivos: RM.Edu.Academico.Form.dll, RM.Edu.MatrizCurricular.Intf.dll

* **[Ticket: 726324 / EDUCACIONAL01-149]** Ajustes na execução do fluxo de inscrição de aluno em visitas técnicas.

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

* **[Ticket: 726324 / EDUCACIONAL01-149]** Novos tipos de certificados. Alteração no processo de geração de certificados e no cadastro de certificados para permitir que sejam gerados os novos tipos de certificados e que possam ser rastreados com base nos registros que os certificados foram gerados.

Arquivo: RM.Edu.Academico.Form.dll

* **[Ticket: 726324 / EDUCACIONAL01-149]** Ajustes na geração do certificado do tipo Estágio.

Arquivos: RM.Edu.dll, RM.Edu.Academico.Form.dll, RM.Edu.PesquisaExtensao.Intf.dll

### Rotina: IMPORTADOR CURRICULO LATTES PROFESSOR EDU 50 269

* **[Ticket: 723618 / EDUCACIONAL01-99]** Otimizado importação de currículo Lattes, para tratar as seguintes situações:- Foi aumentado o tamanho dos campos Instituição Promotora de Evento e Curso da Orientação para 256 caracteres. Necessário executar script marcação = CN.2017.05\_09 para alteração do banco de dados, além da instalação do patch específico.- Permitir que seja possível importar arquivo xml que tenha a mesma palavra chave para produções bibliográficas diferentes.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Professor.Intf.dll, RM.Edu.Professor.Server.dll, RM.Edu.Professor.Data.dll, RM.Edu.Professor.Form.dll, RM.Edu.Consts.dll

* **[Ticket: 723618 / EDUCACIONAL01-99]** Otimizado importação de currículo Lattes, para tratar as seguintes situações:- Foi aumentado o tamanho dos campos Instituição Promotora de Evento e Curso da Orientação para 256 caracteres. Necessário executar script marcação = CN.2017.05\_09 para alteração do banco de dados, além da instalação do patch específico.- Permitir que seja possível importar arquivo xml que tenha a mesma palavra chave para produções bibliográficas diferentes.

Arquivo: RM.Edu.Professor.Form.dll

### Rotina: INTEGRAÇÃO FINANCEIRA- CONTAS A PAGARRECEBER FNC001

* **[Ticket: EDUCACIONAL01-805]** Ajuste no preenchimento da mensagem de retorno para o Protheus com a coligada correta da natureza orçamentária na geração de lançamentos.

Arquivos: RM.Edu.Integracoes.Server.dll, RM.Edu.Financeiro.Server.dll

### Rotina: PADRAO

* **[Ticket: EDUCACIONAL01-292]** Ajuste no processo de Preparação de arquivo do Censo, removendo a mensagem informando que é necessário criar o campo complementar licenciatura bem como sua validação.

Arquivos: RM.Edu.Academico.Data.dll, RM.Edu.Academico.Form.dll

### Rotina: Project-774680 #pilotoparticipativos –Erro ao acessar os arquivos anexos da reserva pela agenda Project-774680

* **[Ticket: 776623 / EDUCACIONAL01-589]** Melhoria no acesso aos anexos da reserva de instalação através da agenda para que não seja apresentada nenhuma mensagem de não conformidade.

Arquivo: RM.Edu.Professor.Form.dll

### Rotina: Project-810756 IFMG - Análise Solicitação de Estágio Project-810756

* **[Ticket: 811746 / EDUCACIONAL01-718]** Ao aprovar a solicitação de estágio, caso o aluno seja menor de idade, deverá ser preenchido o campo “Responsável Legal” para que esta informação seja levada para o Termo de Compromisso. Necessário script para criação do campo SESTAGIOSOLICITACAO.CODRESPLEGAL CN.2017.05\_07.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Lib.Intf.dll, RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.MatrizCurricular.Server.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.MatrizCurricular.Form.dll

### Rotina: Project-810807 #IFMG - Cadastro Funcionário pelo Aluno Project-810807

* **[Ticket: 811591 / EDUCACIONAL01-716]** Melhoria nos procedimentos da gestão de estágio adicionando o novo parâmetro “Obrigar o preenchimento dos campos CPF, RG e endereço para funcionário “Responsável Legal" na solicitação de estágio.”

Arquivos: RM.Edu.Consts.dll, RM.Edu.MatrizCurricular.Intf.dll, RM.Edu.MatrizCurricular.Form.dll, RM.Edu.MatrizCurricular.Server.dll, RM.Edu.Parametros.Data.dll, RM.Edu.Parametros.Form.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Parametros.Intf.dll

## TOTVS Folha de Pagamento

### Rotina: FERIAS CADASTRO FOP 34 538

* **[Ticket: 829991 / FOPCALCULO01-251]** Foi gerado um novo parâmetro 'Calcular Recibo de Férias Automaticamente', que permite retirar o calculo automático de férias no recibo.

Arquivos: RM.Fop.FuFerias.Form.dll, RM.Fop.Parametros.Form.dll, RM.Fop.Parametros.Intf.dll

### Rotina: FUNCIONARIOS HISTORICOS FOP 34 499

* **[Ticket: 629278 / FOPCALCULO01-206]** Ajuste no cadastro para aceitar alteração do tipo 'T' ou 'E' para outros tipos.

Arquivo: RM.Fop.Funcionario.Form.dll

### Rotina: FUNCIONARIOS RHU 36 035

* **[Ticket: 741104 / FOPROTINAS01-332]** Otimização de função de subordinados para diminuir tempo de carregamento

Arquivo: RM.Fop.Funcionario.Server.dll

* **[Ticket: 741104 / FOPROTINAS01-332]** Otimização de função de subordinados para diminuir tempo de carregamento

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RESCISAO COMPLEMENTAR FOP 34 397

* **[Ticket: 727163 / FOPCALCULO01-23]** Retirado filtro que não permitia ao usuário informar o evento com código de cálculo 28 nos eventos a serem somados a rescisão complementar.

Arquivo: RM.Fop.Rescisao.Form.dll

## TOTVS Framework

### Rotina: FRW 00023

* **[Ticket: MFRWBH-1719]** Melhoria na postagem de documento na integração GED

Arquivos: RM.Lib.dll, RM.Lib.Server.dll, RM.Con.GED.Server.dll

## TOTVS Gerador de Relatórios

### Rotina: CONSULTA SQL RPT 00013

* **[Ticket: 680491 / MFRWBH-1492]** Melhoria no Reports para permitir a ediçao de consultas SQL em relatórios criados por providers dos produtos da linha RM.

Arquivo: RM.Rpt.Reports.Form.dll

### Rotina: GERACAO DE RELATORIO RPT 00005

* **[Ticket: 764088 / MFRWBH-1670]** Melhoria na visualização de relatórios pesados no Portal.

Arquivo: App\_Web\_rptreportviewer.aspx.ffa54ff2.dll

## TOTVS Gestão Contábil

### Rotina: CADASTROS PLANO DE CONTAS CONTABIL CTB 38 78

* **[Ticket: 335565 / CONTROLADORIA01-47]** O processo de alteração do código de contas contábeis foi modificado para que o histórico de alteração seja gerado com sucesso, eliminando algumas mensagem de aviso que eram exibidas no log.

Arquivo: RM.Ctb.Processos.Data.dll

### Rotina: ESCRITURACAO CONTABIL TRANSFERENCIA DE GRUPOS CONTABEIS CTB 38 90

* **[Ticket: 792384 / CONTROLADORIA01-137]** Ajuste na mensagem da validação do processo de Transferência de Grupos Contábeis para que não seja referenciado o processo "Zeramento do Saldo Anterior" que foi descontinuado.

Arquivo: RM.Ctb.Utils.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: ANALISE DE RESSUPRIMENTO EST 017

* **[Ticket: 767088 / MATESTCNTFTOF01-184]** Melhoria no processo de ressuprimento

Arquivo: RM.Est.Ressuprimento.Form.dll

### Rotina: CADASTRO DE PRODUTOS PRD 001

* **[Ticket: 618331 / MATESTCNTFTOF01-40]** Ajuste na action de Produto para que seja apresentado os botões de Incluir e Editar do cadastro de Código de Barras e Informações por Filial.

Arquivo: RM.Est.Produto.Form.dll

### Rotina: CANCELAR CONTRATO CTR 007

* **[Ticket: 793745 / MATESTCNTFTOF01-191]** Melhoria no cancelamento de contratos

Arquivo: RM.Ctr.Contrato.Service.dll

### Rotina: PERIODO ORCAMENTO ORC 002

* **[Ticket: 686137 / MATFATCMPCRM01-174]** Ajuste na sequencia de IDs para novos itens de período de orçamento.

Arquivo: RM.Mov.Orcamento.Data.dll

### Rotina: REGISTRAR ORCAMENTO COTACAO COM 008

* **[Ticket: 768349 / MATFATCMPCRM01-284]** Ao editar unidade de medida em registro de orçamento da cotação sistema converte incorretamente a unidade orçada do produto.

Arquivos: RM.Cmp.Facade.Intf.dll, RM.Cmp.Cotacao.Form.dll, RM.Cmp.Cotacao.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: FUNCIONARIO

* **[Ticket: RHU01-166]** Ajuste na listagem de requisição de alteração de dados funcionais ao exibir o tempo de casa

Arquivo: RM.Rhu.Requisicao.Server.dll

### Rotina: FUNCIONARIOS RESCISAO LAB 01 177

* **[Ticket: 384070 / RHU01-101]** Corrigido a lógica de recuperação de funcionário em requisição de transferência com promoção com mudança de chapa

Arquivo: RM.Rhu.Requisicao.Server.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA RESGATE FIN 017

* **[Ticket: 716341 / FINANCEIRO01-131]** Corrige falha em encerramento de período da aplicação financeira.

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

### Rotina: DISTRATO BILATERAL IMB 49 817

* **[Ticket: 821472 / FINANCEIRO01-618]** Ajustado a sincronização relacionada a baixa de lançamento financeiro e baixa das parcelas de Distrato do SGI.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: INTEGRACAO GOODATA FIN 334

* **[Ticket: 854570 / FINANCEIRO01-729]** Ajuste no cálculo de valores no serviço de baixa quando realizada via integração com Protheus e Totvs Incorporação.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: PARAMETROS FIN 228

* **[Ticket: 764361 / FINANCEIRO01-241]** Otimização no processo de parametrização da máscara do Cliente/Fornecedor. Agora o sistema permite a inclusão da máscara corretamente.

Arquivo: RM.Fin.Parametros.Data.dll

### Rotina: RELATORIO EXTRATO DE CLIENTE FORNECEDOR FIN 229

* **[Ticket: 572905 / FINANCEIRO01-132]** Ajuste no Relatório de Extrato de Cliente/Fornecedor.

Arquivos: RM.Fin.Relatorio.Data.dll, RM.Fin.Relatorio.Form.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 594278 / FINANCEIRO01-312]** Melhoria no processo de retorno bancário para o tratamento correto quando no arquivo existir mais de uma linha para o mesmo boleto que esteja associado a mais de um lançamento.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE ATUALIZACAO DA BAIXA FIN 313

* **[Ticket: 827359 / FINANCEIRO01-653]** Otimização no calculo do valor líquido na baixa de lançamentos. Agora o sistema calcula corretamente os valores de integração do SGI de forma que é acrescentado apenas o valor que falta para baixar.

Arquivos: RM.Fin.Lan.Data.dll, RM.Fin.Lan.Form.dll

### Rotina: SESSAO DE CAIXA BAIXA FIN 269

* **[Ticket: 525878 / FINANCEIRO01-361]** Ajustado validação de alteração dos valores do lançamento, no formulário de baixa. Desta forma, quando o formulário estiver sendo utilizado pela Sessão de Caixa, irá obedecer as regras pertinentes ao processo.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: SESSAO DE CAIXA FECHAR SESSAO FIN 273

* **[Ticket: 746345 / FINANCEIRO01-191]** Melhoria no sistema para relacionada a segurança para fechar a sessão de caixa.

Arquivos: RM.Fin.dll, RM.Fin.SessaoCaixa.Form.dll

## TOTVS Gestão Fiscal

### Rotina: Envio NFS-E Rio Grande - Inscrição Municipal Negativa Project-823989

* **[Ticket: 843328 / FISCAL01-360]** Alteração para que seja enviado o hifen (-) na frente da inscrição municipal do tomador para o municipio de Rio Grande - RS.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: NF E ENVIO TOTVS COLABORACAO NF 01 0026

* **[Ticket: 839793 / FISCAL01-358]** Alteração na montagem do XML da NF-e integrada com o Totvs Colaboração 2.0

Arquivos: RM.Fis.NFe.Service.dll, RM.Fis.NFe.Intf.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 719290 / FISCAL01-348]** Ajuste realizado na Rotina para retirar a consistência da geração do campo "07 SERIE do registro C100", com isto o mesmo sempre será gerado.

Arquivo: RM.Fis.Sped.Server.dll

## TOTVS Gestão Hospitalar

### Rotina: AGENDAMENTO SAU 47 1135

* **[Ticket: 846330 / MSAU-8910]** Ajuste realizado para que o sistema faça a exibição das informações da agenda corretamente.

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

* **[Ticket: 846330 / MSAU-8910]** Ajuste realizado para que o sistema faça a exibição das informações da agenda corretamente.

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

### Rotina: ERRO ENCERRAMENTO DE CONTAS SEM DEBITO

* **[Ticket: 837618 / MSAU-8914]** Ajuste nas propriedades da descrição da Unidade de Atendimento na tela de Encerramento de Contas sem Débitos.

Arquivo: RM.Sau.Faturamento.Intf.dll

### Rotina: TISS - GERACAO DOS XMLS SAU471159

* **[Ticket: 830125 / MSAU-7675]** Implementação da TISS 3.03.02

Arquivos: RM.Sau.Faturamento.Form.dll, RM.Sau.AgendaAtendimento.Form.dll, RM.Sau.Faturamento.Intf.dll, RM.Sau.Utils.Intf.dll, RM.Sau.Ans.Intf.dll, RM.Sau.Ans.Sever.dll, RM.Sau.Faturamento.Server.dll, RM.Sau.Ans.Form.dll

## TOTVS Gestão Patrimonial

### Rotina: UTILITARIOS ALTERACAO DE MULTIPLOS PATRIMONIOS PAT 37 96

* **[Ticket: 722404 / CONTROLADORIA01-48]** O processo de alteração de múltiplos patrimônios foi modificado para que seja possível alterar mais de 1000 patrimônios por execução.

Arquivo: RM.Pat.Patrimonio.Data.dll

## TOTVS Incorporação

### Rotina: Arquitetura do Reajuste Revitalizado

* **[Ticket: TINREV001-1]** ajuste na ficha financeira no valor de arredondamento

Arquivo: RM.Imb.Relatorio.Data.dll

## TOTVS Manutenção

### Rotina: TIPOLOGIA MNT 41 155

* **[Ticket: 574368 / MATESTCNTFTOF01-18]** Ajuste na rotina de Incluir Objeto de Manutenção para que seja considerado a Data de Criação do Objeto como a Data de Transferência para Filial, Localização, Centro de Custo. A data de criação também será aplicada como data de coleta para o Histórico de Indicador de Uso.

Arquivo: RM.Mnt.ObjOficina.Data.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: CAMPOS COMPLEMENTARES SMT 36 020

* **[Ticket: 746146 / RHU01-97]** Corrigido erro de associação do código de coligada com a visão. Tela de prontuário abrindo corretamente agora.

Arquivo: RM.Smt.Pessoa.Form.dll

### Rotina: EXAMES ASSIST IMPORTACAO DE RESULTADO DE EXAMES SMT 36 030

* **[Ticket: 513112 / MRH-7376]** Importação de exames agora atualiza os exames pendentes relacionados.

Arquivo: RM.Smt.Clinico.Data.dll

# 12.1.15.148

## TOTVS Automação de Ponto

### Rotina: RECALCULO

* **[Ticket: PONTO01-200]** - Realizado acerto no cálculo para calcular atitude correta quando possui evento 0043- Melhoria na performance do Portal RH, no módulo Subordinados/Abonar e processo Abonar.- Acerto ao editar um abono no Portal RH, módulo Subordinados/Abonar

Arquivos: RM.Pto.Ocorrencia.Data.dll, RM.Pto.Abono.Data.dll, RM.Pto.Calculo.Service.dll

## TOTVS Construção e Projetos

### Rotina: PLANILHAS CRONOGRAMA PRJ 33 866

* **[Ticket: 747009 / TOPEXECONTROL01-133]** Ajuste no processo de recalcular o cronograma ao executar o exportar PERT para cronograma da planilha de atividades. Passa a gerar warnings quando houver ocorrências no cálculo do cronograma.

Arquivos: RM.Prj.Cronograma.Server.dll, RM.Prj.Tarefa.Data.dll

## TOTVS Educacional

### Rotina: CERTIFICADOS DIPLOMAS TIPOS DE CERTIFICACAO EDU 50 123

* **[Ticket: 726324 / EDUCACIONAL01-149]** Ajuste nas obrigatoriedades de colunas dos certificados.

Arquivo: RM.Edu.PesquisaExtensao.Intf.dll

### Rotina: PORTAL ALUNO FREQUENCIA DIARIA EDU 50 354

* **[Ticket: 721463 / EDUCACIONAL01-749]** Otimizado no Portal do Professor, link Diário de Classe, a ordenação da frequência diária do aluno que poderá ser Por Nome (inclusive nome social).Foi criado novo parâmetro Educacional de Matricula para Tipo de Numeração, com a opção “Por nome (inclusive nome social)”. Caso seja marcado, o sistema irá ordenar os alunos pelo nome, inclusive o nome social. Na opção Tipo de Numeração igual a “Por Nome”, a ordenação é feita pelo nome civil apenas.Importante: Como a ordenação do aluno observa também o número do diário, caso opte pelo novo parâmetro, será necessário gerar novamente o processo “Numeração de turma”.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Parametros.Intf.dll, RM.Edu.Processos.Intf.dll, RM.Edu.Matricula.Server.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Processos.Data.dll, RM.Edu.Processos.Form.dll

### Rotina: Project-810807 #IFMG - Cadastro Funcionário pelo Aluno Project-810807

* **[Ticket: 811591 / EDUCACIONAL01-716]** Melhoria nos procedimentos da gestão de estágio adicionando o novo parâmetro "Obrigar o preenchimento dos campos CPF, RG e endereço para funcionário "Responsável Legal" na solicitação de estágio.".

Arquivos: Portal Corpore.Net

* **[Ticket: 811591 / EDUCACIONAL01-716]** Melhoria nos procedimentos da gestão de estágio adicionando o novo parâmetro "Obrigar o preenchimento dos campos CPF, RG e endereço para funcionário "Responsável Legal" na solicitação de estágio.".

Arquivos: Portal Corpore.Net

### Rotina: WEBSERVICE EDU 50 493

* **[Ticket: 841359 / EDUCACIONAL01-818]** Ajustes para não permitir a utilização dos dataservers EduConsultaFaltaEtapaData e EduConsultaNotaEtapaData via webservice.

Arquivo: RM.Edu.NotaFalta.Data.dll

## TOTVS Framework

### Rotina: LICENSE SERVER LS FL119

* **[Ticket: MFRWBH-1753]** Envio da propriedade ProductLine para o License Server

Arquivos: Totvs.Licence.Client.dll, RM.Lib.Server.dll

## TOTVS Gerador de Relatórios

### Rotina: IMPRESSAO RPT 00006

* **[Ticket: 618698 / MFRWBH-1430]** Melhoria na exibição do aviso de Margem de Impressão

Arquivo: RM.Rpt.Executor.Client.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CONCLUIR PEDIDO MOV 008

* **[Ticket: 670293 / MATFATCMPCRM01-48]** Ao concluir um pedido, não devem ser listados como itens passiveis de conclusão os que estiverem em cotação.

Arquivos: RM.Mov.Processos.Data.dll, RM.Mov.Processos.Form.dll

* **[Ticket: 670293 / MATFATCMPCRM01-48]** Ao concluir um pedido, não devem ser listados como itens passiveis de conclusão os que estiverem em cotação.

Arquivos: RM.Mov.Processos.Data.dll, RM.Mov.Processos.Form.dll

### Rotina: RELATORIO DE FICHA FISICA FINANCEIRA EST 006

* **[Ticket: 831621 / MATESTCNTFTOF01-215]** Melhoria no processo de geração da Ficha Física Financeira para ter o mesmo comportamento da Regeração de Saldos e Custos em relação ao parâmetro "Produto Estocável na Filial", disponível no "Cadastro de Produto | Informações por Filial".

Arquivo: RM.Est.Estoque.Service.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: ENVIO DE E MAILS CRM 321455

* **[Ticket: 738903 / MATFATCMPCRM01-321]** Melhorias no processo responsável por movimentar atendimentos através de fórmula.

Arquivos: RM.CRM.Atendimento.Intf.dll, RM.CRM.Classes.dll, RM.CRM.Atendimento.Data.dll

## TOTVS Gestão Financeira

### Rotina: BOLETO INCLUSAO EXCLUSAO FIN 045

* **[Ticket: 837151 / FINANCEIRO01-688]** Retirada a validação no processo de alteração da conta caixa e convenio do boleto para os lançamentos oriundos do TIN.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 813652 / FINANCEIRO01-702]** Ajustado o formulário da baixa, para que ao carregar a data da baixa, e a mesma estiver em final de semana ou feriado, caso o sistema estiver parametrizado para data baixa proximo dia util ou dia util anterior, o sistema apresente mensagem questionado se o cliente deseja fazer a alteração da data.

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: CADASTROS NATUREZA DE OPERACAO LI 01 0015

* **[Ticket: 648224 / FISCAL01-143]** Implementação no serviço seleção de Natureza: Quando o movimento for empresa x empresa será considerado também a coleta\entrega além do próprio endereço da filial.

Arquivo: RM.Fis.NaturezaOper.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 824079 / FISCAL01-343]** Alteração no layout do XML para o município de Juiz de Fora - MG, conforme solicitação do TSS.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: AGENDAMENTO SAU 47 1135

* **[Ticket: 793619 / MSAU-8612]** Ajustes na tela de Agendamento.

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

## TOTVS Gestão Patrimonial

### Rotina: RELATORIOS FICHA DE IMOBILIZADO PAT 37 90

* **[Ticket: 754655 / CONTROLADORIA01-153]** Atualização na emissão do relatório ficha imobilizado referente ao cálculo do saldo anterior de patrimônios avaliados.

Arquivo: RM.Pat.Relatorio.Data.dll

## TOTVS Incorporação

### Rotina: BAIXA - ATUALIZAÇÃO DE VALORES IMB49804

* **[Ticket: TINPAD001-13]** Melhoria no cálculo para montar o plano de financiamento do modelo PRICE, o mesmo passa a deixar no valor principal somente o montante de origem e não soma o juros price de carencia, quando houver carência e o parametro ACERTAVALORORIGINALCARENCIA for igual a 1

Arquivo: RM.Imb.Contratos.Server.dll

### Rotina: VENDA EFETIVACAO GERACAO PLANO DE FINANCIAMENTO IMB 49 869

* **[Ticket: 841078 / TINPAD001-284]** Melhoria no processo de cópia de modalidade por coligada.

Arquivo: RM.Imb.Venda.Regra.Data.dll

# 12.1.15.149

## TOTVS Automação de Ponto

### Rotina: CALCULO PONTO ELETRONICO

* **[Ticket: PONTO01-495]** Alterações no processo de criação de jobs para o processo de solicitação de recálculo no portal.

Arquivo: RM.Pto.JustExcecao.WebForm.dll

### Rotina: ENTRADA DE DADOS IMPORTAR PTO 35 1186

* **[Ticket: 407649 / PONTO01-19]** Função que gera id's para a importação de batidas foi corrigida para garantir que não sejam gerados os mesmos id's por outros processos.

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 816479 / PONTO01-155]** Ajuste realizado no processo de importação de batidas quando o tipo de horário utilizado é semi flexível e a batida está contida no intervalo de ausência de refeição.

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: PORTAL WEB APROVAR HORAS EXTRAS PTO 35 1260

* **[Ticket: 817509 / PONTO01-135]** Foi ajustado a aprovação de extras de subordinados pelo portal, de modo que a mesma seja registrada sem erro independentemente do tipo de horário vinculado ao subordinado.

Arquivo: RM.Pto.HoraExtra.Data.dll

### Rotina: PROCESSO DE CALCULO DO ADICIONAL NOTURNO PTO 35 1242

* **[Ticket: 562419 / PONTO01-280]** Foi incluída na listagem de ocorrências a serem toleradas de acordo com o parâmetro de adicional noturno do sindicato, 'Tolerância diária para adicional noturno', as ocorrências de adicional noturno oriundas de hora extra não autorizada, desta forma o sistema passa a incluir no total tolerado de adicional noturno os valores oriundos de horas extras não autorizadas.

Arquivos: RM.Pto.Parametros.Form.dll, RM.Pto.Calculo.Service.dll

## TOTVS Educacional

### Rotina: CENTRAL DO ALUNO EDU 50 118

* **[Ticket: 772244 / EDUCACIONAL01-607]** Ajuste na central do aluno para volte a exibir os dados financeiros (Parcelas e Bolsas).

Arquivo: RM.Edu.Aluno.Form.dll

### Rotina: FOLHA DE PAGAMENTO PROFESSOR EDU 50 217

* **[Ticket: 862111 / EDUCACIONAL01-875]** Evolução no serviço de exclusão de movimento por competência para que se já existir um cancelamento do movimento o mesmo seja excluído, caso

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: INTEGRAÇÃO FINANCEIRA- CONTAS A PAGARRECEBER FNC001

* **[Ticket: EDUCACIONAL01-805]** Ajuste no preenchimento da mensagem de retorno para o Protheus com a coligada correta da natureza orçamentária na geração de lançamentos.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: PORTAL ALUNO DADOS PESSOAIS EDU 50 349

* **[Ticket: 763744 / PORTALMOBILE01-264]** Ajustado o nome social, conforme parametrização, exibido no título da página de Histórico no Portal do Corpore.Net.

Arquivo: RM.Edu.Historico.Data.dll

### Rotina: PORTAL ALUNO QUADRO DE AVISOS EDU 50 364

* **[Ticket: 627230 / PORTALMOBILE01-146]** Ajuste no quadro de aviso para exibir corretamente o percentual de frequência do aluno.

Arquivo: RM.Edu.NotaFalta.Data.dll

## TOTVS Folha de Pagamento

### Rotina: FOLHA ANALITICA LAB 01 112

* **[Ticket: 732425 / FOPROTINAS01-58]** Foi realizado ajuste para realizar a verificação se foram recuperadas bases de funcionário antes de tentar acessá-las.

Arquivo: RM.Fop.Relatorios.Data.dll

## TOTVS Framework

### Rotina: ACTIONS DO SISTEMA FRW 00002

* **[Ticket: 839683 / MFRWBH-1760]** Melhoria no método GetSchema do WsProcess para que os tipos derivados de ObjectList também sejam instanciados e exibidos para que o usuário preencha os seus respectivos valores.

Arquivo: RM.Lib.Server.dll

### Rotina: CENARIOS MODO TELA CHEIA BIS 00003

* **[Ticket: 860678 / MFRWBH-1772]** Melhoria no portal para que seja exibida mensagem informando que os gráficos do tipo drill down não são compatíveis com o mesmo.

Arquivos: Portal Corpore.Net

### Rotina: GERENCIAMENTO DE JOBS FRW 00036

* **[Ticket: 847501 / MFRWBH-1739]** Melhoria na geração de relatórios Delphi quando o JobRunner está ativado para que seja exibida a tela de aguardando a geração.

Arquivo: RM.Lib.Gerador.Client.dll

### Rotina: PADRAO

* **[Ticket: MFRWBH-1781]** -A data do sistema dentro do contexto da aplicação não deve conter informação de horas.

Arquivo: RM.Lib.WinForms.dll

### Rotina: PERT GANTT PRJ 33 862

* **[Ticket: 718717 / TOPEXECONTROL01-115]** Verificado a inconsistência durante a alteração da duração em etapas com predecessoras ou sucessoras.

Arquivo: RM.Lib.WinForms.Gantt.dll

### Rotina: RM X FLUIG GED PARAMETROS DE CONFIGURACAO INT 00013

* **[Ticket: 856897 / MFRWBH-1770]** A parametrização da integração foi otimizada, para que ele aceite somente um metadata.

Arquivo: RM.Glb.Cadastros.Form.dll

### Rotina: SubMenu customizado não aparece na versão 12.1.16.

* **[Ticket: 850738 / MFRWBH-1752]** -O sistema deve exibir corretamente os submenus da customização na ribbon principal do sistema.

Arquivo: RM.Lib.Server.dll

## TOTVS Gerador de Relatórios

### Rotina: GERACAO DE RELATORIO RPT 00005

* **[Ticket: 835191 / MFRWBH-1742]** Melhoria na utilização de filtros na visão .NET de relatórios delphi.

Arquivo: RM.Rpt.Reports.Data.dll

### Rotina: IMPORTACAO RPT 00004

* **[Ticket: 853196 / MFRWBH-1771]** Melhoria na importação de relatórios alterando o código de consultas SQL.

Arquivo: RM.Rpt.Reports.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: BLOCO K FIS 006

* **[Ticket: MATESTCNTFTOF01-33]** Melhoria na geração do bloco K280. Podem existir tipos de movimento que estejam parametrizados para afetar ao mesmo tempo o Saldo Atual e o Saldo com Terceiros e, nestes casos, deverá ser gerado para o mesmo item e na mesma data, um Registro K280 para cada saldo que está sendo afetado.

Arquivo: RM.Est.Estoque.Service.dll

### Rotina: Erro ao Exececutar WsProcess MovEnviarCTeProc Project-796373

* **[Ticket: 838918 / MATFATCMPCRM01-391]** Melhorias nos processos de envio do CT-e e MDF-e quando executados via WebService.

Arquivo: RM.Mov.CTe.Data.dll

### Rotina: FATURAMENTO

* **[Ticket: MATFATCMPCRM01-426]** Melhorias nas consistências do processo de faturamento.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: MOV BAIXA DE ESTOQUE EST 002

* **[Ticket: 290560 / MATESTCNTFTOF01-34]** Melhoria no processo de regerar saldos e custos para movimentação de transferência de estoque

Arquivo: RM.Est.Estoque.Service.dll

### Rotina: O S CORRETIVA MNTA420

* **[Ticket: 781640 / MATESTCNTFTOF01-218]** Melhoria na exclusão de itens

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: OBRIGACOES ACESSORIAS FCI LI 01 0030

* **[Ticket: 631236 / MATESTCNTFTOF01-202]** Ajuste na rotina de cálculo do FCI para que não sejam considerados os movimentos cancelados.

Arquivo: RM.Est.Estoque.Service.dll

### Rotina: REGISTRAR ORCAMENTO COTACAO COM 008

* **[Ticket: 800862 / MATFATCMPCRM01-342]** O valor do preço unitário na planilha de cotação padrão, deve ter 4 casas decimais.

Arquivo: RM.Cmp.Cotacao.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GESTAO POR QUADRANTES RHU 36 079

* **[Ticket: 810620 / RHU01-141]** A Gestão por Quadrantes associada a uma Avaliação de Desempenho 180 considera as avaliações consensuais para realizar a atribuição de quadrantes.

Arquivo: RM.Rhu.GestaoQuadrantes.Server.dll

### Rotina: TREINAMENTO TURMAS RHU 36 055

* **[Ticket: 526133 / RHU01-261]** Corrigido a lógica de concessão de requisitos de acesso no fechamento de avaliação de conhecimento.

Arquivo: RM.Rhu.Turmas.Server.dll

## TOTVS Gestão Financeira

### Rotina: [Versão Específica] - Erro ao acessar aplicação financeira do tipo poupança

* **[Ticket: FINANCEIRO01-749]** Tratamento defensivo, cálculo rentabilidade de IOF, em IR ComeCotas

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

### Rotina: BOLETO INCLUSAO EXCLUSAO FIN 045

* **[Ticket: 837151 / FINANCEIRO01-688]** Retirada a validação no processo de alteração da conta caixa e convenio do boleto para os lançamentos oriundos do TIN.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 756108 / FINANCEIRO01-716]** Ajuste nas sentenças SQL do processo de retorno bancário para carregar corretamente os dados dos lançamentos/boletos.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE CALCULO DO VALOR LIQUIDO DO LANCAMENTO FIN 243

* **[Ticket: 559447 / FINANCEIRO01-325]** Ajuste na carga de dados de tributos no cálculo de valor líquido e baixa, não considerava valores da tabela FTRBLAN com campo CODRETENCAO nulo.

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Banco.Data.dll, RM.Fin.Lan.Data.dll

## TOTVS Gestão Fiscal

### Rotina: NFS E CONSULTA AUTORIZACAO CANCELAMENTO NF 01 0051

* **[Ticket: 788661 / FISCAL01-398]** Alteração na geração das informações do valor do ISS Retido.

Arquivos: RM.Fis.RotinasFiscais.Form.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 605980 / FISCAL01-131]** homologação do municipio de Osasco - SP.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 702932 / FISCAL01-127]** Foram realizadas as seguintes alterações no Processo de Encerramento do Período de Apuração e Geração Automática de Guias:- Ao encerrar o Período, caso o estado não seja RJ, o sistema irá verificar o parâmetro “Considera Diferencial Alíquota – Outros Débitos”. Caso o parâmetro esteja marcado, o sistema se comportará como atualmente, somará o valor do diferencial de alíquota ao valor do ICMS próprio na apuração. Caso não esteja marcado , o sistema não considerará o valor do diferencial de alíquota na apuração.- Foi criado o parâmetro por Filial “Gera valor Difal por Nota Fiscal”. Caso o parâmetro estiver marcado, o sistema gerará as Guias referentes ao Difal nota a nota. Caso contrário, a geração será realizada consolidada por UF.

Arquivos: RM.Fis.Parametros.Intf.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.Parametros.Data.dll, RM.Fis.Parametros.Form.dll

### Rotina: ROTINAS LEGAIS ESTADUAIS LIVRO ELETRONICO ATO COTEPE LI 01 0059

* **[Ticket: 780431 / FISCAL01-341]** Retirar a Consistência na geração da Guia – Valor da Guia. Deve sempre desconsiderar o Valor da Dedução dos lançamentos de Outros Debito\Credito do Tipo Dedução.

Arquivos: RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.LancFiscal.Form.dll

## TOTVS Gestão Hospitalar

### Rotina: APURACAO E LANCAMENTO DE REPASSES SAU 47 1166

* **[Ticket: 794928 / MSAU-8861]** Ajustes na tela de registro de informação cirúrgica.

Arquivo: RM.Sau.RegistroInfCirurgia.Data.dll

### Rotina: Caderno de Gabaritos

* **[Ticket: 859159 / MSAU-9048]** Correção no Cadastro de CAderno de Gabaritos

Arquivo: RM.Sau.Faturamento.Data.dll

## TOTVS Incorporação

### Rotina: Arquitetura do Reajuste Revitalizado

* **[Ticket: TINREV001-1]** Melhorias nos aditivos de alteração de valor, renegociação e vencimento, apenas para versão revitalizada.

Arquivos: RM.Imb.Venda.Aditivo.Form.dll, RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll

### Rotina: Controle de garantia das unidades

* **[Ticket: TINPAD001-80]** Retirada Constraint indevida

Arquivo: RM.Imb.Contratos.Intf.dll

* **[Ticket: TINPAD001-80]** Exclusão de testes unitários que, devido a evolução do processo de aditivos, não são mais necessários

Arquivo: RM.Imb.Contratos.Server.dll

* **[Ticket: TINPAD001-80]** TINxProtheus (Chave Backoffice) - Melhoria para que a visão de parcelas do TIN, passe a exibir a chave Nr. Titulo e Prefixo do Protheus backoffice para melhor visão do cliente.

Arquivo: RM.Imb.Contratos.Server.dll

# 12.1.15.150

## TOTVS Automação de Ponto

### Rotina: HORÁRIOS PTO351180

* **[Ticket: 96244 / PONTO01-229]** Alterações no processo de exclusão de horários cadastrados, impedindo a exclusão indevida de seus respectivos índices.

Arquivo: RM.Pto.Horario.Data.dll

## TOTVS Construção e Projetos

### Rotina: ANALISE DE VALOR AGREGADO PRJ 33 802

* **[Ticket: 563228 / TOPEXECONTROL01-104]** Ajuste realizado para cálculo dos índices acumulados.

Arquivo: RM.Prj.AnaliseDeValorAgregado.Data.dll

## TOTVS Educacional

### Rotina: BOLETOS EDU 50 069

* **[Ticket: 829998 / EDUCACIONAL01-829]** Foi realizada otimização do processo de geração de movimento em regime de competência, de forma a não criar vínculos entre lançamentos financeiros e movimentos gerados em regime de competência.

Arquivo: RM.Edu.Financeiro.Server.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIOS CADASTRO LAB 01 128

* **[Ticket: 591894 / FOPCALCULO01-101]** Ajuste em campo de Situação para carregar valor default ao incluir novo funcionário.

Arquivos: RM.Fop.Funcionario.Form.dll, RM.Fop.Funcionario.Server.dll

### Rotina: Geração de Chapa através de fórmula(Transferência Coletiva)

* **[Ticket: FOPCALCULO01-317]** Geração de Chapa no processo de transferência coletiva por fórmula

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Parametros.Intf.dll, RM.Fop.Parametros.Form.dll, RM.Fop.Lib.Extensions.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Parametros.Data.dll, RM.Fop.Utils.Server.dll

### Rotina: PORTAL WEB GESTAO DE FERIAS LAB 01 208

* **[Ticket: 651205 / FOPROTINAS01-337]** Criação de permissões de Inclusão, Edição e Remoção para Escala de Férias no Portal (acessado através da Gestão de Férias)

Arquivos: Portal Corpore.Net

## TOTVS Framework

### Rotina: LANCAMENTO ANEXO VINCULOS FIN 184

* **[Ticket: 720655 / FINANCEIRO01-550]** Otimização no processo de alteração de lançamento. Agora o sistema irá permitir a alteração do lançamento do SGI quando o mesmo estiver vinculado e for executado pelo processo de Distrato pelo TIN.

Arquivo: RM.Fin.Lib.dll

### Rotina: MODELO DE NEGOCIO ESTRUTURA DE DADOS MTD 00007

* **[Ticket: 764056 / MFRWBH-1626]** É necessário alterar a ordem dos itens da tabela para que os mesmos fiquem iguais as chaves do lookup configurado.

Arquivos: RM.Lib.Utils.dll, RM.Glb.Metadata.Form.dll, RM.Glb.Metadata.Data.dll, RM.Lib.MetadataProvider.Server.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 812790 / CONTROLADORIA01-167]** Melhoria no cadastro e no processo de importação para geração do Registro I157 para que o mesmo contemple o código da Filial para geração do registro.

Arquivos: RM.Ctb.Sped.Data.dll, RM.Ctb.Sped.Form.dll, RM.Ctb.Sped.Intf.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: ITENS COTAÇÃO COM011

* **[Ticket: 96681 / MATFATCMPCRM01-96]** Melhorias no processo responsável por estornar itens não recebidos.

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão Financeira

### Rotina: Piloto Cetec

* **[Ticket: 580554 / EDUCTB001-538]** Ajuste na nova Integração Educacinal x BackofficeProtheus para processo de aproveitamento de saldo de conta corrente gerando lançamento a pagar, buscar natureza financeira do rateio.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO DE PAGAMENTO FIN 238

* **[Ticket: 659347 / FINANCEIRO01-315]** Ajuste no processo de retorno de pagamento (padrão febraban 240) para considerar o código de ocorrencia '03 - Débito Autorizado pela Agência - Efetuado' como registrado.

Arquivo: RM.Fin.Banco.Data.dll

## TOTVS Gestão Fiscal

### Rotina: SIMPLES NACIONAL

* **[Ticket: FISCAL01-313]** - Criado cadastro de últimas receitas para permitir ao usuário dar entrada nas receitas dos últimos 12 meses do simples nacional;- Excluído processo "Últimas Receitas - Carga Inicial" do cadastro de cenários;- Implementada exclusão em cascata do cadastro de cenários quando não existir período de apuração encerrado dentro de sua vigência;

Arquivos: RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.ApuracaoTrb.Data.dll, RM.Fis.ApuracaoTrb.Form.dll

## TOTVS Gestão Hospitalar

### Rotina: OUTROS PROCESSOS SAU 47 1173

* **[Ticket: 876324 / MSAU-9200]** Realizado ajuste para não realizar chamada no painel de atendimentos eletivos quando a senha estiver em registro de atendimento.

Arquivo: RM.Sau.Utils.Intf.dll

# 12.1.15.151

## TOTVS Automação de Ponto

### Rotina: Abono não funciona no portal

* **[Ticket: 799126 / PONTO01-156]** Foi ajustado a listagem de abonos de subordinados de modo que os dados de aprovação e código de abono serão exibidos corretamente.

Arquivo: RM.Pto.Abono.Data.dll

### Rotina: CONFIGURACOES PARAMETRIZADOR INICIAIS PTO 35 1216

* **[Ticket: 847558 / PONTO01-174]** Ajuste no filtro de ocorrências a serem apresentadas na tela de solicitação de abonos através do Portal.

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Educacional

### Rotina: BOLSA GERAR LANCAMENTO EDU 50 076

* **[Ticket: 855734 / EDUCACIONAL01-867]** Preenchimento de valores defaults de fórmulas associadas a campos do lançamento na inclusão de lançamentos de bolsa de crédito.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: CENTRAL DE NOTIFICACOES EDU 51037

* **[Ticket: 627722 / EDUCACIONAL01-198]** Ajuste na digitação de notas e faltas por etapas ao digitar a nota que seja enviado e-mail para o aluno quando assim parametrizado na central do aluno.

Arquivo: RM.Edu.NotaFalta.Server.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 840403 / EDUCACIONAL01-823]** Ajuste no componente de seleção da empresa para que seja possível filtrar pelo nome da empresa ao digitar no campo. O filtro funcioná do tipo que contém, ou seja, se digitar a Totvs, irá aparecer todas empresas que contém a palavra Totvs. O mesmo foi efetuado para o campo de funcionário ao se cadastrar/editar o mesmo.

Arquivos: Portal Corpore.Net

### Rotina: PORTAL ALUNO FREQUENCIA DIARIA EDU 50 354

* **[Ticket: 721463 / EDUCACIONAL01-749]** Na MDI, menu Notas de Avaliação (Digitação de Notas de Provas), ao passar o mouse na coluna Nome, caso mostre o nome social no grid, o sistema deverá mostrar o nome civil correspondente.

Arquivo: RM.Edu.NotaFalta.Form.dll

### Rotina: Project-871586 Gerar Plano de Aula - gerando aula para tipo de evento selecionado Project-871586

* **[Ticket: 876381 / EDUCACIONAL01-904]** Ajuste na geração de plano de aula para que ao selecionar para "Não gerar plano de aula para eventos acadêmicos do tipo", selecionando dois Tipos sistema o sistema obedeça e não gere aula para os tipo selecionados.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## TOTVS Folha de Pagamento

### Rotina: Buffer Sprint 18/05

* **[Ticket: FOPROTINAS01-268]** Gráfico Comparativo Oneração x Desoneração

Arquivos: RM.Fop.Common.Intf.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Dominio.dll, RM.Fop.Relatorios.Server.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: FOPROTINAS01-268]** Gráfico Comparativo Oneração x Desoneração

Arquivos: RM.Fop.Common.Intf.dll, RM.Fop.Server.dll, RM.FopFolha.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Dominio.dll, RM.Fop.Relatorios.Data.dll

### Rotina: Geração de Chapa através de fórmula(Transferência Coletiva)

* **[Ticket: FOPCALCULO01-317]** Ajuste dos parâmetros

Arquivo: RM.Fop.Parametros.Intf.dll

* **[Ticket: FOPCALCULO01-317]** Ajustes da condicional para tratativa do nova geração de chapa por fórmula

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Framework

### Rotina: RM X FLUIG GED DOCUMENTOS INT 00011

* **[Ticket: 681308 / MFRWBH-1789]** A utilização do workflow foi otimizada.

Arquivos: RM.Lib.dll, RM.Lib.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: MDF-E - PARAMETRIZAÇÃO DE MOVIMENTO MDF001

* **[Ticket: 97393 / MATFATCMPCRM01-116]** Melhoria no envio de MDF-e. Ajuste no log do processo caso não exista veículo de transporte associado.

Arquivo: RM.Mov.CTe.Service.dll

### Rotina: MDF-e Layout 3.0

* **[Ticket: MATFATCMPCRM01-163]** Implementação MDF-e 3.0

Arquivos: RM.Est.dll, RM.Est.Server.dll, RM.Mov.Consts.dll, RM.Mov.CTe.Intf.dll, RM.Mov.Cadastros.Intf.dll, RM.Mov.Movimento.IService.dll, RM.Mov.Utils.Intf.dll, RM.Mov.Movimento.Intf.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Parametros.Data.dll, RM.Mov.Parametros.Form.dll, RM.Mov.Cadastros.Data.dll, RM.Mov.Cadastros.Form.dll, RM.Mov.CopiaMovimento.Service.dll, RM.Mov.CTe.Service.dll, RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Form.dll, RM.Mov.CTe.Data.dll

## TOTVS Gestão Financeira

### Rotina: INCLUSAO DE CONTRATOS PARA ALUNOS EDU 50 279

* **[Ticket: 846804 / EDUCACIONAL01-906]** Foi realizada otimização do processo de geração de lançamentos financeiros do tipo contábil para que, ao buscar as contas contábeis das bolsas aplicadas a parcela, considere apenas as bolsas que compõe o lançamento financeiro, ou seja, as que possuem valor.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: INTEGRACAO GOODATA FIN 334

* **[Ticket: 854570 / FINANCEIRO01-729]** Se parâmetro "Ajustar Diferença de Arredondamento na Baixa integração Protheus" marcado o valor original na baixa deve ficar intacto já que a diferença irá para uma valor de integração.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO ALTERACAO FIN 172

* **[Ticket: 527245 / FINANCEIRO01-313]** Ajuste no estorno de orçamento no processo de alteração de lançamento financeiro, se nenhum dos cmapos que afeta o orçamento foi alterado o estorno não deve ser realizado.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: Visão de Recebíveis/Pagáveis utilizando o recurso de Cubos RM

* **[Ticket: FINANCEIRO01-667]** Elaboração de provider para cubo financeiro de valor líquido

Arquivo: RM.Fin.Relatorio.Data.dll

* **[Ticket: FINANCEIRO01-667]** Elaboração do provider para cubo financeiro de valor líquido

Arquivos: RM.Fin.Lan.IService.dll, RM.Fin.Relatorio.Intf.dll, RM.Fin.Relatorio.Data.dll

## TOTVS Incorporação

### Rotina: Arquitetura do Reajuste Revitalizado

* **[Ticket: TINREV001-1]** melhoria para não permitir inserir o componente do tipo IPTU no aditivo alteração de valor de parcelas

Arquivo: RM.Imb.Venda.Aditivo.Intf.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: CADASTROS TABELAS AUXILIARES TIPOS DE ATESTADOS RHU 36 067

* **[Ticket: 713703 / RHU01-619]** Realizada melhoria em Atestados para que seja possível lançar atestado para funcionários de férias, licença maternidade e aviso prévio. Desde que o período do atestado não faça interseção com o período de férias ou da licença maternidade.

Arquivo: RM.Smt.Pessoa.Form.dll

* **[Ticket: 713703 / RHU01-619]** Realizada melhoria em Atestados para que seja possível lançar atestado para funcionários de férias, licença maternidade e aviso prévio. Desde que o período do atestado não faça interseção com o período de férias ou da licença maternidade.

Arquivos: RM.Smt.Pessoa.Form.dll, RM.Smt.Pessoa.Data.dll, RM.Smt.Pessoa.Intf.dll

# 12.1.15.152

## TOTVS Automação de Ponto

### Rotina: PROCESSO DE CALCULO DE HORAS EXTRAS PTO 35 1238

* **[Ticket: 872302 / PONTO01-507]** Alterações no processo de recálculo, especificamente na parte de geração de avisos, para permitir a execução correta do processo.

Arquivo: RM.Pto.Calculo.Service.dll

## TOTVS Construção e Projetos

### Rotina: Erro na Integração de Medição

* **[Ticket: 881499 / TOPEXECONTROL01-158]** Permitir que o movimento oriundo de contratos com itens de Contrato associado com quantidade zerada (permitida via parâmetro de projeto).

Arquivo: RM.Prj.Contrato.Server.dll

## TOTVS Educacional

### Rotina: GERACAO DE USUARIOS ALUNO PAIS RESPONSAVEIS EDU 50 231

* **[Ticket: 375550 / EDUCACIONAL01-159]** Quando o pai tiver usuário gerado e ele for responsável financeiro, ao gerar o usuário para o responsável financeiro deve ser associado o mesmo usuário do pai.

Arquivos: RM.Edu.Processos.Server.dll, RM.Edu.Processos.Data.dll

### Rotina: INTEGRAÇÃO FINANCEIRA- CONTAS A PAGARRECEBER FNC001

* **[Ticket: EDUCACIONAL01-805]** Atualização do source code responsável pela gravação do DE-PARA (HCINTEGRACAOID) a fim de gravar a coligada zero quando o Nucleus estiver parametrizado para trabalhar com coligada global.

Arquivo: RM.Edu.ConfiguraIntegracao.TotvsEduBackOfficeProtheus.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 858919 / EDUCACIONAL01-871]** Ajustes nos filtros quando utilizado o perído letivo.

Arquivo: RM.Edu.Integracoes.Server.dll

### Rotina: PADRAO

* **[Ticket: EDUCACIONAL01-909]** No cadastro de dados do censo do aluno, ao abrir o anexo, caso esteja Desmarcado o campo “Deficiência Visual” não deverá permitir marcas seus respectivos tipos (baixa visão, cegueira). O mesmo para “Deficiência Física”.Por se tratar de Censo, serão alteradas as versões 12.1.13, 12.1.14, 12.1.15 As versões 12.1.16 e 12.1.17 não foram alterada por ter um novo tratamento para deficiências.

Arquivos: RM.Edu.Lib.WinForms.dll, RM.Edu.Aluno.Form.dll

### Rotina: PESQUISAS

* **[Ticket: EDUCACIONAL01-879]** Ajustes ao selecionar o tipo de certifico Ação de extensão, tipo coordenador.

Arquivo: RM.Edu.Academico.Form.dll

* **[Ticket: EDUCACIONAL01-879]** Ajustes no cadastro de certificados.

Arquivos: RM.Edu.PesquisaExtensao.Data.dll, RM.Edu.Academico.Form.dll, RM.Edu.MatrizCurricular.Data.dll

### Rotina: Project-871586 Gerar Plano de Aula - gerando aula para tipo de evento selecionado Project-871586

* **[Ticket: 876381 / EDUCACIONAL01-904]** Alterado a mensagem no log para: A data [data da aula] está cadastrada como uma Atividade Acadêmica no calendário de código [código do calendário].

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

### Rotina: TURMAS DISCIPLINAS EDU 50 454

* **[Ticket: 812378 / EDUCACIONAL01-721]** Melhoria no gerenciamento de aula da turma para que a ordenação leve em consideração o horário de início e término.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## TOTVS Folha de Pagamento

### Rotina: Geração de Chapa através de fórmula(Transferência Coletiva)

* **[Ticket: FOPCALCULO01-317]** Correção na implementação do novo parâmetro de geração de chapa por fórmula

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: importação de dados no RM Labore

* **[Ticket: 566980 / FOPROTINAS01-61]** Ajuste na importação de campos complementares de dependentes para seguir a alteração que foi feita na importação de campos complementares de funcionário. Não é mais necessário informar todos os campos, apenas os que deseja alterar.

Arquivo: RM.Fop.Importacao.Data.dll

### Rotina: LANCAMENTOS FINANCEIROS PARAMETRIZACAO FOP 34 383

* **[Ticket: 791486 / FOPCALCULO01-315]** Ajuste na rotina para evitar aceitar registro sem valor para idceitomador.Sistema tentava salvar valor -1 para campo chave estrangeira.

Arquivo: RM.Fop.Dominio.dll

### Rotina: Marcação de férias web permite saldo menor que 10 dias.

* **[Ticket: 590947 / FOPROTINAS01-368]** Melhoria na organização do código,

Arquivo: RM.Fop.FuFerias.Intf.dll

* **[Ticket: 590947 / FOPROTINAS01-368]** Ajuste no RM Portal, ao realizar a marcação de férias, o sistema deve verificar o parâmetro "nº min. de dias de férias p/ férias partidas" e não permitir que a sugestão de férias seja realizada quando o saldo restante seja menor que o valor informado no parametrizador.

Arquivos: RM.Fop.FuFerias.Intf.dll, RM.Fop.FuFerias.Data.dll

## TOTVS Framework

### Rotina: MODELO DE NEGOCIO ESTRUTURA DE DADOS MTD 00007

* **[Ticket: 764056 / MFRWBH-1626]** É necessário alterar a ordem dos itens da tabela para que os mesmos fiquem iguais as chaves do lookup configurado.

Arquivos: RM.Glb.Metadata.Form.dll, RM.Glb.Metadata.Data.dll

## TOTVS Gerador de Relatórios

### Rotina: IMPRESSAO RPT 00006

* **[Ticket: 874162 / MFRWBH-1805]** Melhoria no preview do Reports para que o botão de imprimir o relatório não suma ao avançarmos para as demais páginas.

Arquivo: RM.Rpt.Reports.Form.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 819526 / CONTROLADORIA01-183]** Mudança na rotina que ajusta a lista de Plano de Contas para que a mesma ordene a lista das contas antes de fazer os ajustes que informam quem são as contas superiores de cada conta do plano.

Arquivo: RM.Ctb.Sped.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: FLUIG APROVACAO FATURAMENTO MOVIMENTO FLG 004

* **[Ticket: 472743 / MATESTCNTFTOF01-258]** Melhoria ao alterar movimento integrado ao Fluig. Foi criado uma validação no sistema para impedir o usuário de editar a solicitação sem que ele esteja no mesmo mecanismo de atribuição do usuário que criou a mesma. Apresentando uma mensagem que impeça de editar o movimento sem atender a esta premissa.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: MDF-E - PARAMETRIZAÇÃO DE MOVIMENTO MDF001

* **[Ticket: 97393 / MATFATCMPCRM01-116]** Melhoria no envio de MDF-e. Ajuste no log do processo caso não exista veículo de transporte associado.

Arquivo: RM.Mov.CTe.Service.dll

### Rotina: MDF-e Layout 3.0

* **[Ticket: MATFATCMPCRM01-163]** Implementação do MDF-e 3.0

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 854606 / RHU01-307]** Realizado ajuste em avaliação de desempenho.

Arquivo: RM.Rhu.AvalDesemp.Server.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA RESGATE FIN 017

* **[Ticket: 716341 / FINANCEIRO01-131]** Melhoria em cálculo da rentabilidade acumulada

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

## TOTVS Gestão Fiscal

### Rotina: SIMPLES NACIONAL

* **[Ticket: FISCAL01-313]** Efetuada melhoria em "Obrigações Principais\Simples Nacioal\Cenários de Apuração\Anexo Últimas Receitas"para validar se o ano e mês inseridos são validos.

Arquivos: RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.ApuracaoTrb.Data.dll

## TOTVS Gestão Patrimonial

### Rotina: OPERACOES PATRIMONIAIS IMPAIRMENT PAT 37 105

* **[Ticket: 756288 / CONTROLADORIA01-148]** O processo de impairment sofreu algumas modificações para possibilitar a realização de impairment de bens, avaliados pelo custo atribuído, em versões mais antigas do módulo patrimonial.

Arquivos: RM.Pat.PatrimonioMoeda.IService.dll, RM.Pat.Contabilizacao.Service.dll, RM.Pat.Ocorrencia.IService.dll, RM.Pat.PatrimonioMoeda.Service.dll, RM.Pat.Contabilizacao.Data.dll, RM.Pat.Ocorrencia.Intf.dll, RM.Pat.Ocorrencia.Service.dll, RM.Pat.Ocorrencia.Data.dll, RM.Pat.Ocorrencia.Form.dll

## TOTVS Incorporação

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 851414 / TINPAD001-340]** Ajuste para não calcular residuo, caso não exista a regra

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

# 12.1.15.153

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB APROVAR ABONOS PTO 35 1268

* **[Ticket: 810323 / PONTO01-121]** O sistema foi alterado para apresentar a justificativa e o horário referentes ao abono na solicitação de abono web.

Arquivo: RM.Pto.Ocorrencia.Data.dll

* **[Ticket: 810323 / PONTO01-121]** O sistema foi alterado para apresentar a justificativa e o horário referentes ao abono na solicitação de abono web.

Arquivos: RM.Pto.Ocorrencia.Data.dll, RM.Pto.Abono.Data.dll

### Rotina: PROCESSO DE CALCULO OCORRENCIA 0043 PTO 35 1280

* **[Ticket: 720489 / PONTO01-17]** Processo de alteração de ocorrencia alterado para gravar o usuário e a data de alteração do registro

Arquivo: RM.Pto.Ocorrencia.Data.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 838896 / PONTO01-170]** Alterações realizadas no processo de geração do relatório do espelho para permitir a impressão correta dos descansos, compensados e descrição dos feriados, mesmo sem a utilização do parâmetro "Imprimir horário contíguo".

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Construção e Projetos

### Rotina: PLANILHAS EXPORTAR PLANILHA PARA O EXCEL COM FORMULAS PRJ 33 867

* **[Ticket: 869618 / TOPORCAPLAN001-337]** Exportação de tarefas para excel com fórmulas apresenta erro nas fórmulas quando as obras possuem quantidade diferente de 1.

Arquivo: RM.Prj.Planilhas.Form.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: Falha no processo de classificação das cirurgias

* **[Ticket: 854202 / MSAU-8985]** Ao realizar a inserção de procedimentos na cirurgia manualmente no cadastro do paciente o sistema não estava permitindo inserir, a tela abre e fecha sozinha. Alterado o sistema para permitir que seja inserido manualmente o procedimento na cirurgia.

Arquivos: RM.SauIH.Paciente.Data.dll, RM.SauIH.Paciente.Form.dll

## TOTVS Educacional

### Rotina: GERACAO DO HISTORICO EDU 50 233

* **[Ticket: 823322 / EDUCACIONAL01-751]** Ajustar consulta que busca as notas ou faltas de etapas para que não sejam retornados valores duplicados violando restrição de valores únicos.Tratamento de preenchimento de carga horária de disciplina quando não existem registros de nota ou falta de etapa.

Arquivo: RM.Edu.Historico.Server.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 840403 / EDUCACIONAL01-823]** Ajustes na solicitação de estágio.

Arquivos: Portal Corpore.Net

### Rotina: OUTROS

* **[Ticket: EDUCACIONAL01-911]** Correção na geração do arquivo do Educacenso para Instituições por Nível de Ensino.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.Academico.Form.dll, RM.Edu.Academico.Server.dll, RM.Edu.Academico.Data.dll

* **[Ticket: EDUCACIONAL01-910]** Ajuste para que o campo Código da IES não exiba no ensino básico sobrepondo o outro campo.

Arquivo: RM.Edu.Cadastros.Form.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 881584 / EDUCACIONAL01-916]** Otimizado no Cadastro de Filial | Anexos | Dados Educacionais | Anexos | Instituição MEC, para permitir inserir registro mesmo quando a filial não possui no endereço o campo Estado preenchido.

Arquivo: RM.Edu.Cadastros.Data.dll

### Rotina: PROFESSORES EDU 50 403

* **[Ticket: 871334 / PORTALMOBILE01-562]** Ajuste na validação de situação do funcionário vinculado ao coordenador do curso quando a pessoa tem mais de um funcionário.

Arquivo: RM.Edu.Contexto.Data.dll

### Rotina: Project-840328 Cadastro Modalidade Project-840328

* **[Ticket: 841013 / EDUCACIONAL01-897]** Melhoria para que seja possível no cadastro de Atividades Curriculares cadastrar uma nova Modalidade através do componente de pesquisa (Lookup).

Arquivo: RM.Edu.AtvCurricular.Form.dll

* **[Ticket: 841013 / EDUCACIONAL01-897]** Melhoria para que seja possível no cadastro de Atividades Curriculares cadastrar uma nova Modalidade através do componente de pesquisa (Lookup).

Arquivo: RM.Edu.AtvCurricular.Form.dll

## TOTVS Folha de Pagamento

### Rotina: CONTABILIZACAO FOP 34 523

* **[Ticket: 661604 / FOPROTINAS01-147]** Ajuste no processo de geração dos encargos referente 'Dedução 13º Ref a Licença Maternidade' deve ser considerado os eventos com código de cálculo: • 322 - 2ª Parcela 13º Salário Licença Maternidade • 323 - Diferença 13º Salario Licença Maternidade • 324 - Décimo Terceiro Salário Rescisão Licença Maternidade • 325 - Diferença 13 Salário Rescisão Licença Maternidade

Arquivos: RM.Fop.Const.Intf.dll, RM.Fop.Dominio.dll

### Rotina: FERIAS CALCULO FOP 34 529

* **[Ticket: 674604 / FOPCALCULO01-221]** Ajuste para desconsiderar meses de afastamento (quando 5 dias ou mais de afastamento) no cálculo de média das férias.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: Homolognet

* **[Ticket: 756199 / FOPROTINAS01-247]** Correção da validação do tipo de demissão para HomologNet

Arquivos: RM.Fop.Calc.Calculos.dll, RM.Fop.Rescisao.Form.dll

### Rotina: IMPORTACAO DE DADOS DO RM LABORE LAB 01 26

* **[Ticket: 801961 / FOPCALCULO01-232]** Realizado ajuste na validação de valor zerado para o campo "número de salário" no processo de importação de salário composto

Arquivo: RM.Fop.Importacao.Data.dll

### Rotina: Marcação de férias web permite saldo menor que 10 dias.

* **[Ticket: 590947 / FOPROTINAS01-368]** Ajuste para considerar o número de dias de abono pecuniário para cálculo do saldo restante para próximo período aquisitivo.

Arquivo: RM.Fop.FuFerias.Data.dll

* **[Ticket: 590947 / FOPROTINAS01-368]** Ajuste no código para realizar a conversão para int32 pois o tipo da variável é int e ajustado a validação se o saldo restante para o próximo período aquisitivo é igual a zero.

Arquivo: RM.Fop.FuFerias.Data.dll

## TOTVS Framework

### Rotina: ACTIONS DO SISTEMA FRW 00002

* **[Ticket: 782071 / MFRWBH-1785]** Ao clicar no botão de copiar natureza do movimento, todos os itens serão alterados conforme esperado.

Arquivo: RM.Lib.WinForms.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 805451 / FISCAL01-431]** NFS-e - Rio Claro - SP:Concatenar os campos de endereço, tipo logradouro e logradouro na tag de logradouro;Concatenar os campos de bairro, tipo bairro e bairro na tag de bairro;

Arquivos: RM.Fis.Lib.dll, RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: 813537 / FISCAL01-399]** Foi realizada uma alteração para que, ao enviar a NFS-e para o município de Nova Lima, o sistema retire do código de serviço federal o caracter “.”, caso estiver cadastrado com o mesmo.

Arquivos: RM.Fis.Lib.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: PADRAO

* **[Ticket: MFRWBH-1823]** A propriedade EnableAutoFillPkOnInsert foi criada.

Arquivo: RM.Lib.WinForms.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 874432 / CONTROLADORIA01-206]** Ajuste no cadastro do plano de contas anterior (I157) para que as Contas Gerenciais sejam apresentadas corretamente.

Arquivo: RM.Ctb.Sped.Form.dll

* **[Ticket: 854628 / CONTROLADORIA01-174]** Ao gerar o ECD, no registro I155, a conta que tiver saldo final igual a zero irá sair com o indicador da situação do saldo final (campo 9) igual a sua natureza.

Arquivo: RM.Ctb.Sped.Service.dll

* **[Ticket: 838446 / CONTROLADORIA01-211]** Ajuste na rotina que retorna o saldo anterior que não consta na tabela CSALDOEXERCICIO para que a mesma passe a contar com filtro por tipo de Natureza do Sped.

Arquivo: RM.Ctb.Sped.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CADASTRO

* **[Ticket: MATFATCMPCRM01-413]** Melhorias no cadastro de mensagens e parâmetros por Filial.

Arquivo: RM.Mov.Parametros.Form.dll

### Rotina: MDF-e Layout 3.0

* **[Ticket: MATFATCMPCRM01-163]** Implementação MDF-e 3.0

Arquivo: RM.Mov.Cadastros.Form.dll

* **[Ticket: MATFATCMPCRM01-163]** Implementação do MDF-e 3.0

Arquivo: RM.Mov.Cadastros.Data.dll

### Rotina: REGERAR SALDOS E CUSTOS EST 013

* **[Ticket: 797875 / MATESTCNTFTOF01-220]** Melhoria no processo de geração da Ficha Física Financeira para verificar a permissão de Regeração de Saldos e Custos caso este seja solicitado. Caso não tenho permissão nem será exibido a opção de Regerar Saldos e Custos antes de gerar a Ficha Física.

Arquivo: RM.Est.Processos.Form.dll

## TOTVS Gestão Financeira

### Rotina: BORDERO INCLUSAO FIN 054

* **[Ticket: 734488 / FINANCEIRO01-148]** Permitir gerar borderô de pagamento para fornecedor bloqueado quando a tag de segurança "Incluir Lçto para cli/for bloqueado" concedida.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 813652 / FINANCEIRO01-702]** Ajustado o formulário da baixa, para que ao carregar a data da baixa, e a mesma estiver em final de semana ou feriado, caso o sistema estiver parametrizado para data baixa proximo dia util ou dia util anterior, o sistema apresente mensagem questionado se o cliente deseja fazer a alteração da data.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: Visão de Recebíveis/Pagáveis utilizando o recurso de Cubos RM

* **[Ticket: FINANCEIRO01-667]** Ajustes no provider do cubo financeiro

Arquivos: RM.Fin.Relatorio.Intf.dll, RM.Fin.Relatorio.Data.dll

## TOTVS Gestão Fiscal

### Rotina: PARAMETRIZACAO

* **[Ticket: FISCAL01-441]** Ao editar um movimento, o sistema está emitindo a seguinte mensagem: "expressão não encontrada".Foi realizada uma alteração para que o sistema não emita essa mensagem.

Arquivo: RM.Fis.Parametros.Data.dll

## TOTVS Gestão Hospitalar

### Rotina: ERRO NA GERACAO DO XML MEDICOS MAIS DE UM CBO

* **[Ticket: 871479 / MSAU-9197]** Ajuste na rotina de verificação das regras gerais de CBO para considerá-las de acordo com o tipo de XML e TAG.

Arquivos: RM.Sau.Ans.Sever.dll, RM.Sau.Faturamento.Server.dll

### Rotina: RECURSO DE GLOSAS SAU 47 1165

* **[Ticket: 869758 / MSAU-9190]** Ajuste nas Guias TISS para validar o parâmetro "Utiliza número da remessa original do faturamento de recurso de glosa”.

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Gestão Patrimonial

### Rotina: CADASTROS PATRIMONIOS PAT 37 39

* **[Ticket: CONTROLADORIA01-180]** Atualização da máquina de cálculo

Arquivo: RM.Pat.Calculo.Service.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: CADASTROS TABELAS AUXILIARES TIPOS DE ATESTADOS RHU 36 067

* **[Ticket: 713703 / RHU01-619]** Realizada melhoria em Atestados para que seja possível lançar atestado para funcionários de férias, licença maternidade e aviso prévio. Desde que o período do atestado não faça interseção com o período de férias ou da licença maternidade.

Arquivo: RM.Smt.Pessoa.Data.dll

### Rotina: RELATORIOS PERFIL PROFISSIOGRAFICO PREVIDENCIARIO PPP SMT 36 578

* **[Ticket: 654347 / RHU01-154]** Tratamento para geração de PPP sem riscos de local de trabalho associados devido a data de contratação ser superior a data de fim do risco.

Arquivo: RM.Smt.Relatorio.Data.dll

# 12.1.15.154

## TOTVS Automação de Ponto

### Rotina: CONFIGURACOES PARAMETRIZADOR SINDICATO PTO 35 1217

* **[Ticket: 823338 / PONTO01-157]** Acerto na função de fórmula HORASTRABDESC passando o parâmetro igual a "2" para trazer as horas trabalhadas em dia de feriados. Não estava considerando as horas em um intervalo noturno, onde ele buscava os valores da jornada.

Arquivo: RM.Pto.Formula.dll

### Rotina: Erro no cadastro de intervalos planejados quando não há ordem das batidas

* **[Ticket: PONTO01-565]** Ajustado a definição do valor da ordem do índice da tolerância de modo que seja registrado adequadamente evitando erros durante o cadastro de jornadas planejada para horários rígidos.

Arquivo: RM.Pto.Horario.Data.dll

## TOTVS Construção e Projetos

### Rotina: MENSAGEM UNICA CADASTRO PROJETO OBRA E TAREFA PRJ 33 918

* **[Ticket: 784232 / TOPEXECONTROL01-139]** Ajuste na atividade de fórmula visual para integração de tarefas.

Arquivo: RM.Prj.FormulaVisual.Activities.dll

### Rotina: PLANILHAS LANCAMENTOS MULTIPLOS CRONOGRAMA PRJ 33 873

* **[Ticket: 842842 / TOPORCAPLAN001-327]** Má performance no processo de Alteração Múltipla do Cronograma

Arquivos: RM.Prj.Calculo.Intf.dll, RM.Prj.Cronograma.Form.dll, RM.Prj.Cronograma.Server.dll, RM.Prj.Calculo.Server.dll, RM.Prj.Cronograma.Data.dll

## TOTVS Educacional

### Rotina: TURMAS DISCIPLINAS EDU 50 454

* **[Ticket: 756948 / EDUCACIONAL01-645]** Ajuste no processo de cópia de avaliações entre turmar/disciplinas.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## TOTVS Folha de Pagamento

### Rotina: ALTERACOES GLOBAIS ALTERACAO DE SALARIOS LAB 01 3

* **[Ticket: 681150 / FOPROTINAS01-112]** Feitos ajustes para verificar antes de tentar acesso que pode ocasionar a exceção mencionada.

Arquivos: RM.Fop.Funcionario.Form.dll, RM.Fop.Rotinas.Data.dll

* **[Ticket: 665092 / FOPCALCULO01-203]** Feitos ajustes na distribuição por centro de custo dos eventos que compõe salário de funcionário para que cada evento reajustado seja distribuido uma única vez, considerando apenas o valor do próprio evento reajustado e seus centros de custo.

Arquivo: RM.Fop.Rotinas.Data.dll

### Rotina: Buffer Sprint 18/05

* **[Ticket: FOPROTINAS01-268]** Ajustes no processo do gráfico de comparativo desonaração para informar receita bruta e percentual redutor da seção.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Dominio.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Server.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: FOPROTINAS01-268]** Ajustes no processo do gráfico de comparativo desonaração para informar receita bruta e percentual redutor da seção.

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: CONTABILIZACAO FOP 34 523

* **[Ticket: 827199 / FOPROTINAS01-436]** Correção da contabilização de encargos quando o mesmo utiliza alíquota FAP por filial.

Arquivo: RM.Fop.Dominio.dll

### Rotina: FERIAS CALCULO FOP 34 529

* **[Ticket: 674604 / FOPCALCULO01-221]** Ajuste no tratamento do parâmetro "Substitui periodo de afastamento por meses anteriores" quando existe a ocorrência de afastamentos e férias no mesmo período de apuração das medias.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: FopRotinas - Manutenção

* **[Ticket: FOPROTINAS01-267]** Criação do metodo para calcular avos de dereito através de vigência fixa.

Arquivos: RM.Fop.Integracao.Intf.dll, RM.Fop.Calc.Integracao.dll, RM.Fop.Integracao.Services.dll, RM.Fop.Dominio.dll

### Rotina: GPS Oneração Folha de Pagamento

* **[Ticket: FOPROTINAS01-269]** Reoneração para Guia de INSS e calculo do avos desonerados.

Arquivos: RM.Fop.Common.Intf.dll, RM.Fop.Lib.Intf.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Dominio.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: FOPROTINAS01-269]** Acerto no recalculo da Guia de INSS devido a referencia de objeto

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: FOPROTINAS01-269]** Avos de 13 Salario respeitando vigência

Arquivo: RM.Fop.Calc.Integracao.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: MOVIMENTO DE EXPORTACAO VEN 003

* **[Ticket: 687281 / MATFATCMPCRM01-421]** Sistema deveria permitir vincular à nota de exportação uma compra ou entrada do produto acabado no sistema, com ou sem cliente/fornecedor, pois a mercadoria para exportação pode ser comprada de um fornecedor ou produzida pela própria empresa. Mas o sistema não está permitindo vincular um movimento de transferência, sem o cliente/fornecedor.

Arquivo: RM.Mov.Movimento.Data.dll

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: 810634 / MATFATCMPCRM01-410]** Melhoria na inclusão de movimento Totvs Colaboração através de arquivo XML

Arquivo: RM.Mov.Integracoes.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GERENCIAMENTO DE ALERTAS GESTAO DE HIERARQUIA RHU 38 005

* **[Ticket: 777864 / RHU01-182]** Corrigido o problema específico da criação de requisições com funcionários da gestão hierarquica sem seção vinculada.

Arquivo: RM.Rhu.Requisicao.Server.dll

## TOTVS Gestão Financeira

### Rotina: BOLETO BAIXAR LANCAMENTO FIN 038

* **[Ticket: 657373 / FINANCEIRO01-334]** Agora o sistema carrega o tipo do Boleto que está em processo de baixa parcial e transfere seu tipo para o novo boleto que será gerado.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: EXTRATO DE CAIXA ANEXO LANCAMENTOS FIN 138

* **[Ticket: 622845 / FINANCEIRO01-344]** Ajustado a visualização de anexos de "Lançamentos" e "Baixa de Lançamentos" de extratos que tiveram contabilização de mutuo.

Arquivo: RM.Fin.Extrato.Form.dll

### Rotina: LANCAMENTO GERAR ACORDO FIN 199

* **[Ticket: 868971 / FINANCEIRO01-752]** Retirada da validação que não permitia a gerar acordo de lançamentos vinculados a movimentos diferentes.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: CADASTROS EVENTOS CONTABEIS LI 01 0008

* **[Ticket: 848671 / FISCAL01-390]** Efetuada melhoria ao contabilizar lançamento fiscal para que evento contábilvinculado a uma determinada fórmula seja carregado corretamente.

Arquivo: RM.Fis.Formula.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 874069 / FISCAL01-435]** No processo de envio da NFS-e será verificado se a nota possui mais de 1 tributo ISS então remove todos os tributos ISS com base de cálculo zero.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: RECURSO DE GLOSAS SAU 47 1165

* **[Ticket: 870198 / MSAU-9419]** Cliente deseja que seja informado, na geração do XML de Recurso, o número Guia Prestador na tag 'GuiaOrigem'.

Arquivos: RM.Sau.Parametros.Intf.dll, RM.Sau.Ans.Sever.dll, RM.Sau.CadastrosFat.Form.dll

## TOTVS Incorporação

### Rotina: ADITIVO RENEGOCIACAO DE CONTRATO IMB 49 784

* **[Ticket: 823150 / TINPAD001-278]** Ajuste para que, ao cancelar lançamentos (via aditivos de renegociação, troca de compradores ou via distrato), a data de cancelamento será definida com a data do aditivo ou do distrato.

Arquivos: RM.Imb.Financeiro.IServer.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Facade.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll, RM.Imb.Contratos.Server.dll, RM.Imb.Distrato.Server.dll, RM.Imb.Aditivos.Server.dll

### Rotina: DISTRATO BILATERAL IMB 49 817

* **[Ticket: 860157 / TINPAD001-345]** O sistema passou a exibir uma interface na geração do plano para selecionar o fornecedor.

Arquivos: RM.Imb.Parametros.Intf.dll, RM.Imb.Venda.Lib.Intf.dll, RM.Imb.Parametros.Data.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll, RM.Imb.Venda.Regra.Intf.dll, RM.Imb.Venda.Regra.Data.dll, RM.Imb.Venda.Regra.Form.dll

# 12.1.15.155

## TOTVS Automação de Ponto

### Rotina: CADASTRO HORARIO POR JORNADA PTO 35 1295

* **[Ticket: 856184 / PONTO01-190]** Foi realizado o ajuste de modo que somente sejam somadas as horas trabalhadas as horas oriundas das ocorrências de trabalho e de horas extras.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: PORTAL WEB ABONAR ATRASOS E FALTAS PTO 35 1257

* **[Ticket: 898861 / PONTO01-552]** As telas de abono foram alteradas para exibir as ocorrências do tipo "Atraso".

Arquivo: RM.Pto.Abono.Data.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 883771 / PONTO01-531]** Alterações realizadas no processo para gerar o relatório do espelho do cartão do funcionário, permitindo que as ocorrências e suas respectivas durações sejam impressas corretamente.

Arquivo: RM.Pto.Relatorio.Data.dll

### Rotina: RELATORIOS PORTARIA 1 510 2009 AFDT PTO 35 1271

* **[Ticket: 865183 / PONTO01-546]** Ajuste realizado na geração do relatório AFDT quando marcado o parâmetro "Considerar batidas pré assinaladas".

Arquivos: RM.Pto.Horario.Data.dll, RM.Pto.Relatorio.Data.dll

## TOTVS Construção e Projetos

### Rotina: EXPORTAR INSUMOS PARA SUPRIMENTOS FATURAMENTO PRJ 33 821

* **[Ticket: 876328 / TOPEXECONTROL01-162]** Melhoria na edição bloqueada dos movimento de Suprimento/Faturamento quando o período do contrado vinculado ao movimento tenha valor de dedução

Arquivo: RM.Prj.Contrato.Server.dll

### Rotina: MOBILIDADE EQUIPE DE MOBILIDADE PRJ 33 989

* **[Ticket: 908342 / TOPEXECONTROL01-161]** Ajuste para permitir a escolha de uma equipe na visão do cadastro de equipes e uma folha tarefa na execução do relatório quando executado pelo processo desta visão. Alterado o relatório para utilizar o parâmetro de equipe. Deve ser importado com substituição dos SQLs. Quando o relatório é executado pela visão de equipe são exibidas para todas as folhas tarefas. Quando o relatório é executado pelo menu "Relatórios | Membros de Equipe" será exibido somente para a tarefa e equipe selecionada. Neste opção são exibidas somente equipes com alocação na tarefa selecionada.

Arquivo: RM.Prj.Mobilidade.Form.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: Chamado Totvs: Classificação Errada das Culturas

* **[Ticket: 888233 / MSAU-9499]** Alterado o cadastro de cultura do paciente para validar quando a relevância clínica for patogênica verificar se o grupo de material é um dos permitidos no cadastro do sítio.

Arquivo: RM.SauIH.Paciente.Data.dll

## TOTVS Educacional

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 825620 / EDUCACIONAL01-753]** Ajustes na avaliação institucional para alunos egressos.

Arquivo: RM.Edu.AvaliacaoInstitucional.Server.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR

* **[Ticket: EDUCACIONAL01-948]** Correções no campo CONSIDERADOCENSO do aluno para o Educacenso

Arquivo: RM.Edu.Academico.Form.dll

* **[Ticket: EDUCACIONAL01-948]** Correções no campo CONSIDERADOCENSO do aluno para o Educacenso

Arquivos: RM.Edu.Matricula.Intf.dll, RM.Edu.Matricula.Data.dll, RM.Edu.Matricula.Form.dll

* **[Ticket: EDUCACIONAL01-948]** Alteração na matrícula de período letivo, no processo de “Atualização de dados do MEC e SISTEC” ao chamar a funcionalidade ocorria erro "Referência de objeto".

Arquivo: RM.Edu.Matricula.Data.dll

### Rotina: TURMAS DISCIPLINAS EDU 50 454

* **[Ticket: 756948 / EDUCACIONAL01-645]** Ajustes no processo de cópia de avaliações entre disciplinas.

Arquivos: RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.Lib.Intf.dll

## TOTVS Folha de Pagamento

### Rotina: CONSULTA MOVIMENTO DA INTEGRACAO LAB 01 96

* **[Ticket: 931593 / FOPROTINAS01-505]** Ajuste na integração de lançamentos contábeis com o Protheus para permitir a geração de número da linha em branco, de forma que será gerada automaticamente no Protheus (necessário marcação de parâmetro)

Arquivos: RM.Fop.Parametros.Intf.dll, RM.Fop.Parametros.Form.dll, RM.Fop.TotvsMessage.OutrosBackoffices.Services.dll

### Rotina: CONTABILIZACAO FOP 34 523

* **[Ticket: 827199 / FOPROTINAS01-436]** Correção da contabilização de encargos quando o mesmo utiliza alíquota FAP por filial.

Arquivo: RM.Fop.Dominio.dll

### Rotina: FERIAS CADASTRO FOP 34 538

* **[Ticket: 749598 / FOPCALCULO01-181]** Ajustado desconto das horas do evento CC128, estornando as faltas do funcionário a nível de férias.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: FUNCIONARIOS RESCISAO LAB 01 177

* **[Ticket: 752703 / FOPCALCULO01-231]** Ajuste no TRCT para validação de 1 centavo no valor do evento de Férias Proporcionais

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: Geração de Chapa através de fórmula(Transferência Coletiva)

* **[Ticket: FOPCALCULO01-317]** Validar se a nova chapa retornada pela fórmula atende a parametrização de chapa do labore

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: MANAD LAB 01 122

* **[Ticket: 699031 / FOPROTINAS01-227]** Ajuste no processo do MANAD para levar o campo DATA DE ADMISSÃO em branco no caso de funcionário Autônomo para o registro K050, conforme documentação

Arquivo: RM.Fop.Manad.Data.dll

## TOTVS Gestão Contábil

### Rotina: Cancelamento de parcela de aluguel com erro

* **[Ticket: 889524 / CONTROLADORIA01-218]** Foram realizadas algumas modificações para possibilitar a realização do aditivo de venda. Para realizar esta operação a data do lançamento deverá estar dentro do período para manutenção definido para o usuário.

Arquivo: RM.Ctb.Lan.Service.dll

### Rotina: CADASTROS PLANO DE CONTAS CONTABIL CTB 38 78

* **[Ticket: 897000 / CONTROLADORIA01-223]** Ajuste na rotina ( Alteração do campo “Tem distribuição gerencial” ) para que altere corretamente os rateios gerenciais quando o valor do rateio é negativo.

Arquivo: RM.Ctb.Utils.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CADASTRO DE FORMULA FRM 001

* **[Ticket: 665938 / MATFATCMPCRM01-287]** Forma de calcular o rateio de valores do movimento em uma fórmula, deve ser a mesma usada no calculo do movimento.

Arquivo: RM.Mov.Formula.dll

### Rotina: CONTRATOS

* **[Ticket: MATESTCNTFTOF01-167]** Ao excluir os faturamentos do contrato pelo Lote, apenas o status do primeiro item de Orçamento estava voltando para o status "A Faturar".

Arquivo: RM.Ctr.Contrato.Service.dll

### Rotina: MDF E REJEICAO MDF 003

* **[Ticket: 917072 / MATFATCMPCRM01-490]** Quando não existir Código Interno de Operação de Transporte no CT-e vinculado e o Tipo do Transportador for igual a Prestador de Serviço de Transporte o sistema irá gerar a tag infContratante com o CNPJ do contratante do MDF-e

Arquivos: RM.Mov.Movimento.Intf.dll, RM.Mov.CTe.Service.dll, RM.Mov.Movimento.Form.dll

### Rotina: SOLICITACAO DE COMPRAS COM 001

* **[Ticket: 665299 / MATFATCMPCRM01-393]** Melhoria no processo de gerar ordem de compra a partir de uma cotação parametrizada para utilizar tributação no item de movimento

Arquivo: RM.Cmp.OrdemCompra.Service.dll

### Rotina: TOTVS COLAB RECEBIMENTO NF E CLB 032

* **[Ticket: 717815 / MATFATCMPCRM01-382]** Melhorias no processo de recebimento de NF-e.

Arquivos: RM.Mov.Integracoes.Intf.dll, RM.Mov.Integracoes.Form.dll, RM.Mov.Integracoes.Service.dll, RM.Mov.Integracoes.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS CURRICULOS EXTERNOS RHU 36 022

* **[Ticket: 724445 / RHU01-174]** Ajuste realizado para o login no banco de talentos através do Portal

Arquivo: RM.Rhu.Curriculo.Intf.dll

### Rotina: Erro na Data de Expiração de Característica Pessoal

* **[Ticket: 856930 / RHU01-309]** Correção ao editar uma característica pessoal. A data de expiração acompanha a data informada pelo usuário no cadastro, a data de expiração somente é calculada com base no parametrizador apenas caso esse campo esteja vazio e a data de aquisição seja alterada.

Arquivo: RM.Rhu.Pessoa.Form.dll

### Rotina: GESTAO POR COMPETENCIAS ESCALA PADRAO RHU 36 048

* **[Ticket: 674302 / RHU01-116]** Corrigido o processo de inserção para permitir a inserção de participantes com competências com itens de performace inativos.

Arquivo: RM.Rhu.AvalDesemp.Server.dll

### Rotina: Processo de Hierarquia do Posição Multi-Coligadas

* **[Ticket: 778229 / RHU01-183]** Realizado ajuste de forma a corrigir inconsistência ao ativar gestão por hierarquia.

Arquivos: RM.Rhu.Hierarquia.Service.dll, RM.Rhu.Hierarquia.Data.dll

## TOTVS Gestão Financeira

### Rotina: BAIXAS PAGAR AUT

* **[Ticket: FINANCEIRO01-179]** Ajuste no rateio gerencial de contabilização de extrato de mútuo quando parâmetro "Inverter o default contábil de mútuo para extrato de saque" marcado.

Arquivo: RM.Fin.Extrato.Service.dll

### Rotina: Desabilitar contabilização do item de baixa não contábil

* **[Ticket: FINANCEIRO01-850]** Desabilitar o botão Contabilização e processos relacionados quando o status contábil do item de baixa for "Não Contábil".

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: LANCAMENTO BAIXA CREDITOS DEVOLUCOES VINCULADOS FIN 189

* **[Ticket: 607151 / FINANCEIRO01-333]** Inclusão do campo "Valor Vínculo" no anexo de Vínculos do lançamento.

Arquivos: RM.Fin.Lan.Intf.dll, RM.Fin.Lan.Data.dll

### Rotina: LANCAMENTO GERAR ACORDO FIN 199

* **[Ticket: 664278 / FINANCEIRO01-339]** Caso o lançamento seja Gerado por Acordo o sistema irá permitir que o rateio por departamento possua filiais diferentes.

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 868971 / FINANCEIRO01-752]** Ajuste sentença sql para oracle no processo de gerar acordo

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO BAIXA

* **[Ticket: FINANCEIRO01-352]** Ajuste na baixa de lançamentos vinculados armazenando corretamente os valores de referência de baixa.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: OUTROS

* **[Ticket: FINANCEIRO01-849]** Criação das propriedades ValorDevolucao e ValorNotaCreditoAdiantamento na classe FinDadosItemDeBaixa.

Arquivos: RM.Fin.Lan.IService.dll, RM.Fin.Lan.Service.dll

### Rotina: SERVICO DE CONTABILIZACAO FIN 323

* **[Ticket: 756528 / FINANCEIRO01-530]** Otimização na alteração de lançamentos. Agora o sistema não permite a alteração da conta/caixa de uma lançamento com a contabilização de inclusão integrada ao lote zero.

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 608708 / FINANCEIRO01-324]** Ajuste ao validar o parâmetro do Tipo de Documento e Não Contabilizar Baixa com Valor Zero.

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: CADASTROS PRODUTOS SERVICOS LI 01 0018

* **[Ticket: 720562 / FISCAL01-424]** Ajuste no processo de importação do código CEST:- Incluir ou Atualizar o código CEST na tabela TPRDFISCAL de produto "Global".

Arquivo: RM.Fis.Cadastros.Services.dll

### Rotina: ESCRITURACAO LI 01 0025

* **[Ticket: 863906 / FISCAL01-434]** Ajuste no Serviço de Tributação e na Escrituração para o calculo correto da Base do Diferencial de Aliquota quando o Movimento não possui valor de ICMS

Arquivo: RM.Fis.Tributo.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 877390 / FISCAL01-410]** Alteração no preenchimento da inscrição municipal do tomador para o município de Rio Grande - RS.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: ELABORACAO DE CONTA SAU 47 1147

* **[Ticket: 866389 / MSAU-9117]** O parâmetro "Permite alterar data de Mat/Med quando lançado via mov. de estoque" só será exibido na tela de perfil do usuário, quando houver permissão para a coligada visualizar esse parâmetro, pois ele foi criado para customizar o ambiente de um cliente específico.

Arquivos: RM.Sau.Parametros.Intf.dll, RM.Sau.Cadastros.Form.dll, RM.Sau.Parametros.Data.dll

### Rotina: Erro no Painel de Chamada

* **[Ticket: 819020 / MSAU-8629]** Ajuste realizado no formulário "Atendimento"/"Pronto Atendimento / Ambulatório"/"Painel de Classificação de Risco" , para que ao abrir seja exibido a mensagem informada e seja possível dar andamento do processo de registro da classificação de risco.

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

## TOTVS Gestão Patrimonial

### Rotina: EVENTOS

* **[Ticket: CONTROLADORIA01-163]** Ao tentar editar a classificação de um envento contábil estava sendo exibida uma mensagem de erro. Foram realizadas algumas alterações para que seja possível editá-lo.

Arquivo: RM.Pat.GrupoPatrimonio.Data.dll

### Rotina: INTEGRACOES INTEGRACAO AQUISICOES COMPRAS RM NUCLEUS PAT 37 64

* **[Ticket: 442337 / CONTROLADORIA01-33]** Atualização no processo de integração referente à nota devolvida pelo RMNucleus

Arquivo: RM.Pat.Integracao.Data.dll

* **[Ticket: 735597 / CONTROLADORIA01-113]** Atualização da validação do parâmetro "Considera a falta do Grupo de patrimônios como erro" conforme documentação em: http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.integraAquisicaoCompra.aspx

Arquivos: RM.Pat.Integracao.Intf.dll, RM.Pat.Integracao.Data.dll

## TOTVS Incorporação

### Rotina: Arquitetura do Reajuste Revitalizado

* **[Ticket: TINREV001-1]** Melhoria no processo de distrato, apenas clientes revitalizados TIN.

Arquivos: RM.Imb.Venda.Lib.Intf.dll, RM.Imb.Venda.Aditivo.Data.dll, RM.Imb.Venda.Aditivo.Form.dll, RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Financeiro.Server.dll, RM.Imb.Venda.Regra.Data.dll, RM.Imb.Venda.Calc.Calculos.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll

### Rotina: CADASTRO

* **[Ticket: TINPAD001-286]** Ajuste data de emissão do lançamento igual a data do aditivo

Arquivo: RM.Imb.Contratos.Server.dll

### Rotina: Erro Antecipação Parcela Price

* **[Ticket: 882229 / TINPAD001-370]** Ajuste na validação da Data para antecipação de parcela PRICE

Arquivo: RM.Imb.Reajuste.Server.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 877475 / TINPAD001-372]** Consulta de vendas no processo de reajuste.

Arquivo: RM.Imb.Reajuste.Data.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: RELATORIOS PERFIL PROFISSIOGRAFICO PREVIDENCIARIO PPP SMT 36 578

* **[Ticket: 753752 / RHU01-94]** campo 13.3 corrigido conforme o histório de seção

Arquivo: RM.Smt.Relatorio.Data.dll

# 12.1.15.156

## TOTVS Automação de Ponto

### Rotina: FORMULAS PTO 35 1179

* **[Ticket: 889293 / PONTO01-537]** Ajuste da fórmula HORARIODIASIT para verificar a lista de abonos do funcionário do tipo "Abono de Afastamento" e retornar o resultado como vazio para estes casos.

Arquivo: RM.Pto.Formula.dll

### Rotina: PORTAL WEB ESPELHO DO CARTAO PTO 35 1250

* **[Ticket: 899473 / PONTO01-554]** Sistema alterado para verificar se o funcionário para qual o cálculo foi solicitado utiliza período futuro.

Arquivos: RM.Pto.Contexto.Server.dll, RM.Pto.JustExcecao.WebForm.dll

## TOTVS Banco de Dados

* **[Ticket: Alterações Gerais]** Ajuste de script para converter string da coluna LICENCIATURA na tabela SHABILITACAOCOMPL

Arquivo: Cvn.12.1.15.sql

## TOTVS Construção e Projetos

### Rotina: MENSAGEM UNICA CADASTRO PROJETO OBRA E TAREFA PRJ 33 918

* **[Ticket: 784232 / TOPEXECONTROL01-139]** Ajustes ao acessar a atividade no cadastro de fórmula visual.

Arquivo: RM.Prj.FormulaVisual.Activities.dll

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 703021 / EDUCACIONAL01-729]** Otimizado processo de geração automática de usuário, para sempre criar o perfil do usuário do aluno/professor/funcionário empresa com sistema Educacional (tabela GUSRPERFIL campo CODSISTEMA igual a “S”) e não o contexto logado.

Arquivos: RM.Edu.MatrizCurricular.Server.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Processos.Form.dll, RM.Edu.Processos.Server.dll, RM.Edu.Aluno.Server.dll, RM.Edu.Professor.Data.dll

### Rotina: GERACAO DE MOVIMENTO EDU 50 229

* **[Ticket: 821668 / EDUCACIONAL01-793]** Foi realizada otimização do processo de geração de movimento por competência, de forma que o sistema consiga calcular o valor líquido do boleto para quando o sistema está parametrizado para não gerar boleto após uma baixa parcial.

Arquivos: RM.Edu.Facade.dll, RM.Edu.Financeiro.Server.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 825620 / EDUCACIONAL01-753]** Ajustes nos filtros disponibilizados para os alunos egressos no cadastro de avaliações institucionais.

Arquivos: RM.Edu.AvaliacaoInstitucional.Intf.dll, RM.Edu.AvaliacaoInstitucional.Form.dll

### Rotina: NOTAS E FALTAS DE ETAPA EDU 50 318

* **[Ticket: 872283 / EDUCACIONAL01-905]** Ajuste no método que salva as aulas dadas para que seja possível deixar o campo em branco na digitação de notas/faltas de etapas.

Arquivo: RM.Edu.NotaFalta.Form.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 907162 / EDUCACIONAL01-959]** O parâmetro para cadastro automático da data de cancelamento da matrícula foi alterado para permitir também limpar a data.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Intf.dll, RM.Edu.Matricula.Server.dll, RM.Edu.Academico.Intf.dll, RM.Edu.Matricula.Form.dll, RM.Edu.Academico.Form.dll

## TOTVS Folha de Pagamento

### Rotina: FERIAS ESCALA DE FERIAS FOP 34 408

* **[Ticket: 254098 / FOPROTINAS01-209]** Ajuste na rotina de aviso automático de férias em dobro para não selecionar funcionários que já estejam com férias marcadas.

Arquivo: RM.Fop.Cadastros.Data.dll

### Rotina: RESCISAO HOMOLOGNET LAB 01 219

* **[Ticket: 347882 / FOPROTINAS01-10]** Criado campo para que seja utilizada fórmula para informar se o salário referente ao mês anterior à rescisão do contrato de trabalho do funcionário já foi pago. Feitos ajustes para levar a tag VLSalarioLiquidoMesAnteriorRescisao para o XML do HomologNet apenas se o salário do mês anterior à rescisão não foi pago e a quitação da rescisão ocorrer até o quinto dia útil do mês seguinte a esse salário.

Arquivos: RM.Fop.Lib.Intf.dll, RM.Fop.Processos.Intf.dll, RM.Fop.Processos.Data.dll, RM.Fop.Processos.Form.dll

## TOTVS Framework

### Rotina: CENARIOS MODO TELA CHEIA BIS 00003

* **[Ticket: 927750 / MFRWBH-1878]** Melhoria na exibição de cenários no portal para que os itens sejam exibidos na vertical, dois a dois.

Arquivos: Portal Corpore.Net

### Rotina: LANCAMENTO MANUTENCAO ALTERACAO GLOBAL FIN 202

* **[Ticket: 561273 / MFRWBH-1877]** O Retorno do XML foi ajustado.

Arquivo: RM.Lib.Workflow.Activities.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INVENTARIO - CADASTRO EST023

* **[Ticket: 94364 / MATESTCNTFTOF01-28]** Melhoria no processo de inclusão de inventário para não exceder o número máximo de expressões em uma lista em base oracle.

Arquivo: RM.Est.Inventario.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: Erro na Data de Expiração de Característica Pessoal

* **[Ticket: RHU01-686]** Correção na data de Expiração de Característica Pessoal ao editar

Arquivo: RM.Rhu.Pessoa.Form.dll

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 737572 / RHU01-71]** Descrição dos itens abrem corretamente quando uma AD é aberta através de um link proveniente do email enviado aos avaliadores.

Arquivo: App\_Web\_rhuavaliacaodesempenhoexecucao.ascx.246e283e.dll

### Rotina: GESTAO POR COMPETENCIAS GRADUACAO DAS COMPETENCIAS RHU 36 532

* **[Ticket: 848108 / RHU01-621]** A validação de comentários para fatores organizacionais funciona corretamente agora.

Arquivos: Portal Corpore.Net

## TOTVS Gestão Financeira

### Rotina: Efeito colateral no TIN

* **[Ticket: FINANCEIRO01-884]** Ajuste na exibição dos processos disponíveis na visão de baixa de lançamento de acordo com status contábil.

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: ESCRITURACAO LI 01 0025

* **[Ticket: 863906 / FISCAL01-434]** Ajuste para o calculo da Base do ICMS DIFAL seja realizadocorretamente mesmo quando o Movimento tenha IPI

Arquivo: RM.Fis.Tributo.Service.dll

### Rotina: NFC-e - Valor de Desconto quando utilizado serviço vDesc e vDescincond

* **[Ticket: 801974 / FISCAL01-409]** Alteração na impressão do DANFE da NFC-e, para que o valor do desconto não seja mostrado duplicado.

Arquivo: RM.Fis.Lib.Server.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 702932 / FISCAL01-127]** Alteração:Quando marcado o parametro "Gerar valor DIFAL por nota fiscal"Serão geradas as guas GNR de FECP e de DIFAL com os dados do Estado de destino na aba GNR nota a nota;Serão geradas as guias de DIFAL para os dados do Estado de Origem na aba de Normal nota a nota;Quando o parametro estiver desmarcado:Serão geradas as guas GNR de FECP e de DIFAL com os dados do Estado de destino na aba GNR por estado;Serão geradas as guias de DIFAL para os dados do Estado de Origem na aba de Normal por estado;

Arquivo: RM.Fis.ApuracaoTrb.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Erro na atualização de valores RMSaude nova MDI

* **[Ticket: 933436 / MSAU-9692]** Realizado ajuste, na nova MDI, para concluir o processo de atualização de valores corretamente.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: FATURAMENTO DE CONTAS SAU 47 1149

* **[Ticket: 933369 / MSAU-9689]** Ao realizar o agrupamento de itens matmed, o sistema em alguns casos não estava considerando o parâmetro da condição contratual e acabava não agrupando todos os itens no XML da remessa. Alterado o sistema para sempre agrupar MATMED se o parâmetro estiver marcado na condição contratual do convênio.

Arquivo: RM.Sau.Ans.Sever.dll

## TOTVS Incorporação

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 862320 / TINPAD001-401]** Baixa parcial com valor de devolução.

Arquivos: RM.Imb.Lib.dll, RM.Imb.Facade.dll

# 12.1.15.157

## TOTVS Automação de Ponto

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 880665 / PONTO01-532]** Alterações no processo de geração do relatório do espelho do cartão, para permitir que usuários que utilizem fórmula possam ter suas ocorrências de abono devidamente descritas no relatório.

Arquivo: RM.Pto.Ocorrencia.Data.dll

* **[Ticket: 880665 / PONTO01-532]** Alterações no processo de geração do relatório do espelho do cartão, para permitir que usuários que utilizem fórmula possam ter suas ocorrências de abono devidamente descritas no relatório.

Arquivos: RM.Pto.Ocorrencia.Data.dll, RM.Pto.Relatorio.Data.dll

## TOTVS Avaliação e Pesquisa

### Rotina: Project-898694 Erro executor Project-898694

* **[Ticket: 920651 / EDUCACIONAL01-983]** Foi alterada a codificação de caracteres para UTF7 na geração da prova offline e importação de prova no Totvs.Executor. O erro ocorria porque no texto da questão existia o caracter unicode (0x8230) que fazia com que o xml gerado fosse inválido.

Arquivos: RM.Tst.Processos.Form.dll, RM.TstExec.Executor.exe

## TOTVS Educacional

### Rotina: MUDAR TURMA EDU 50 314

* **[Ticket: 731950 / EDUCACIONAL01-126]** Ajuste para que o sistema não mais obrigue o usuário informar a turma de destino quando a turma de origem estiver preenchida para execução do processo, ou seja, é possível mudar a turma sem que informe a turma de destino, apenas é selecionado as turmas/disciplinas.Além disso, foi criado um parâmetro na tela de mudança de turma chamado "Manter turma de origem", onde o mesmo apenas é habilitado e visível se a turma de origem estiver preenchida e a turma de destino estiver vazia. Caso a turma de destino estiver preenchida o parâmetro é desabilitado, porém visível. Nos demais casos o parâmetro ficará invisível. O parâmetro tem por objetivo manter a turma de origem quando não se preenche a turma de destino caso o parâmetro estiver marcado, caso contrário a turma não será mantida e será apagada ao final do processo. Tais implementações afetam apenas o nível de ensino superior.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Form.dll, RM.Edu.Matricula.Server.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 935660 / EDUCACIONAL01-1012]** A mensagem de aviso sobre as mudanças no Censo a partir da versão 12.1.15 foi alterada para incluir também o Censo da Educação Básica.

Arquivo: RM.Edu.dll

## TOTVS Folha de Pagamento

### Rotina: ALTERACOES GLOBAIS ALTERACAO CAMPOS DO CADASTRO LAB 01 1

* **[Ticket: 224763 / FOPCALCULO01-11]** Realizado ajuste para que a chapa sequencial seja preenchida automaticamente ao cadastrar funcionário

Arquivo: RM.Fop.Funcionario.Form.dll

### Rotina: EMPRESTIMOS LAB 01 135

* **[Ticket: 732280 / FOPCALCULO01-255]** Ajuste realizado para possibilitar filtrar funcionários pelo campo calculado idade

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: LOCALIZACAO FRW 00045

* **[Ticket: 679885 / FOPROTINAS01-520]** Ajustes para tradução dos botões de editar e atualizar na tela de Subordinados do portal

Arquivos: Portal Corpore.Net

### Rotina: PORTAL WEB SUBORDINADOS LAB 01 213

* **[Ticket: 945744 / FOPROTINAS01-521]** Ajuste na visão de subordinados do RM Portal para ocultar campos que estavam aparecendo na grid ao utilizar a funcionalidade de busca

Arquivo: App\_Web\_fopfuncsubordinadoswebform.ascx.88834ab6.dll

## TOTVS Framework

### Rotina: HOST FRW00038

* **[Ticket: MFRWBH-1901]** Foi realizado um ajuste na detecção de jobs ativos.

Arquivo: RM.Lib.Jobs.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CADASTRO DE PRODUTOS PRD 001

* **[Ticket: 869164 / MATESTCNTFTOF01-264]** Ajuste na consistência da máscara do Código do Produto para ter o mesmo comportamento da edição do campo.

Arquivo: RM.Est.Produto.Service.dll

### Rotina: MDF E RELATORIO MDF 004

* **[Ticket: 928854 / MATFATCMPCRM01-499]** Enviar Campo RNTRC no XML do MDF-e na tag infANTT

Arquivos: RM.Mov.CTe.Intf.dll, RM.Mov.CTe.Service.dll

### Rotina: PROCESSOS DE RESSUPRIMENTO EST 018

* **[Ticket: 819504 / MATESTCNTFTOF01-266]** Melhoria no Processo de Ressuprimentos para não gerar erro de chave duplicada.

Arquivos: RM.Est.Inventario.Data.dll, RM.Est.Ressuprimento.Form.dll

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: 717502 / MATFATCMPCRM01-242]** Melhoria na inclusão de movimento Totvs Colaboração atraves de arquivo XML

Arquivo: RM.Mov.Integracoes.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS USUARIOS DO CURRICULO RHU 36 029

* **[Ticket: 713850 / RHU01-17]** O filtro de função do "painelVagas/lista" listava todas as funções ativas ou inativas. Adicionado um filtro para listar apenas as ativas.

Arquivos: FrameHTML

### Rotina: Project-904065 Visualização de Vagas para Candidatos Project-904065

* **[Ticket: 917756 / RHU01-668]** correção ao resgatar as vagas que um candidato já está concorrendo: Vagas que já passaram da data de fechamento são exibidas como vagas que o candidato está concorrendo.

Arquivos: RM.Rhu.Curriculo.Intf.dll, RM.Rhu.Curriculo.Server.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA RESGATE FIN 017

* **[Ticket: 725814 / FINANCEIRO01-770]** Disponibiliza recurso de reabertura de período encerrado de aplicação financeira

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

## TOTVS Gestão Fiscal

### Rotina: ESCRITURACAO LI 01 0025

* **[Ticket: 863906 / FISCAL01-434]** Ajuste para o calculo da Base do ICMS DIFAL seja realizadocorretamente mesmo quando o Movimento tenha IPI e este afeta a Base do ICMS

Arquivo: RM.Fis.Tributo.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Erro na atualização de valores RMSaude nova MDI

* **[Ticket: 933436 / MSAU-9692]** Realizado ajuste, na nova MDI, para concluir o processo de atualização de valores corretamente.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: OUTROS PROCESSOS SAU 47 1173

* **[Ticket: 878716 / MSAU-9228]** Ajuste realizado no formulário "Atendimento"/"Pronto Atendimento / Ambulatório"/"Painel de Classificação de Risco" , para que ao abrir formulário de "Classificação de Risco", o campo de checagem "Fluxo de Atendimento de Enfermagem" esteja desmarcado.

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

## TOTVS Incorporação

### Rotina: ADITIVO RENEGOCIACAO DE CONTRATO IMB 49 784

* **[Ticket: 942585 / TINPAD001-433]** Ajuste para validar se existe data de próximo reajuste pendente antes da comparação.

Arquivo: RM.Imb.Reajuste.Server.dll

## TOTVS Processo Seletivo

### Rotina: AGENDAMENTOS EDUPS 20 1004

* **[Ticket: 857169 / EDUCACIONAL01-874]** Ajuste no processo de exportação de dados dos candidatos.

Arquivo: RM.EduPS.Processos.Data.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: SMT CATALOGO DE EPIS SMT 36 011

* **[Ticket: 812797 / RHU01-139]** Ajuste na listagem de EPI por Seção

Arquivo: RM.Smt.EPI.Data.dll

# 12.1.15.158

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 759368 / PONTO01-90]** Após a correção, o recalculo foi realizado com sucesso.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: PARAMETRIZADOR INICIAIS PTO 35 1234

* **[Ticket: 936785 / PONTO01-591]** Alterações na funcionalidade de inserção de batidas múltiplas no espelho do funcionário, para permitir o funcionamento correto do processo.

Arquivo: RM.Pto.Batida.Data.dll

### Rotina: Parte 2 - Recálculo Portal RH somente com necessidade de recálculo

* **[Ticket: PONTO01-538]** Adicionado validação que seta o funcionário com Status de necessidade de recalculo.

Arquivo: RM.Pto.HoraExtra.Data.dll

* **[Ticket: PONTO01-538]** Implementado um novo parâmetro do portal que, se habilitado, considerara o status do recálculo do funcionário de modo que se o mesmo estiver com status de não necessidade de recalculo ou recalculo em andamento o mesmo não será processador. O status mudará para recálculo necessário caso seja alterado alguma informação que modifique os dados de recálculo, como batidas, abonos, atitudes e o movimento.

Arquivos: RM.Pto.Funcionario.Intf.dll, RM.Pto.Parametros.Intf.dll, RM.Pto.Funcionario.Data.dll, RM.Pto.Horario.Data.dll, RM.Pto.JustExcecao.Intf.dll, RM.Pto.JustExcecao.WebForm.dll, RM.Pto.Utils.Server.dll, RM.Pto.Parametros.Form.dll, RM.Pto.AlterarHorarioLetra.Data.dll, RM.Pto.AprovaHorasExtras.Data.dll, RM.Pto.Autorizacao.Server.dll, RM.Pto.Extra.dll, RM.Pto.JustExcecao.Data.dll, RM.Pto.Ocorrencia.Data.dll, RM.Pto.Abono.Data.dll, RM.Pto.Batida.Data.dll, RM.Pto.Calculo.Service.dll, App\_Web\_ptoschedulechecker.aspx.14deb1c9.dll

## TOTVS Avaliação e Pesquisa

### Rotina: Project-898694 Erro executor Project-898694

* **[Ticket: 920651 / EDUCACIONAL01-983]** Foi alterada a codificação de caracteres para UTF7 na geração da prova offline e importação de prova no Totvs.Executor. O erro ocorria porque no texto da questão existia o caracter unicode (0x8230) que fazia com que o xml gerado fosse inválido.

Arquivo: RM.Tst.Processos.Form.dll

* **[Ticket: 920651 / EDUCACIONAL01-983]** Foi alterada a codificação de caracteres para UTF7 na geração da prova offline e importação de prova no Totvs.Executor. O erro ocorria porque no texto da questão existia o caracter unicode (0x8230) que fazia com que o xml gerado fosse inválido.

Arquivo: RM.TstExec.Executor.exe

## TOTVS Construção e Projetos

### Rotina: COMPOSICAO CADASTRO PRJ 33 809

* **[Ticket: 847216 / TOPORCAPLAN001-477]** Ambiente Go Global o componete de tipo de composição está sendo instanciado antes dos dados do BD serem carregados

Arquivo: RM.Prj.Composicao.Form.dll

### Rotina: CONTRATOS CADASTRO PRJ 33 937

* **[Ticket: 920603 / TOPEXECONTROL01-167]** Bloquear o acesso a dedução e retenção (Processo Liberação de Período), quando o usuário não obtiver permissão, para alterar ou incluir deduções e retenções no projeto.

Arquivo: RM.Prj.Contrato.Form.dll

### Rotina: Falha na integração de revaloração de mão de obra

* **[Ticket: TOPEXECONTROL01-189]** Ajuste no processo de revaloração de mão de obra para viabilizar integração com Protheus com chapa de funcionário customizada (diferente entre RM e Protheus).

Arquivos: RM.Prj.Facade.dll, RM.Prj.Mobilidade.Server.dll

## TOTVS Educacional

### Rotina: ATIVIDADE FORMULA VISUAL EDU 50 482

* **[Ticket: 617661 / EDUCACIONAL01-1093]** Otimizado Fómula Visual, ao utilizar a atividade “Ler Parâmetros do Processo” cujo nome do processo seja “EduCancelaContratoData”, será gravado em seus parâmetros RM.Edu.Financeiro.EduCancelaContratoParamsProc os campos CODFILIAL e CODTIPOCURSO do Contexto logado.

Arquivo: RM.Edu.Financeiro.Form.dll

### Rotina: ATIVIDADES CURRICULARES EDU 50 043

* **[Ticket: 572397 / EDUCACIONAL01-197]** Foi criado o parâmetro de processo "Permite inscrição duplicada de um mesmo aluno na mesma atividade" que virá desmarcado por default. Ao ser marcado, o processo permitirá a inscrição de um aluno na mesma atividade inscrita anteriormente.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.AtvCurricular.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.AtvCurricular.Form.dll

### Rotina: BOLSA RETROATIVA EDU 50 479

* **[Ticket: 866197 / EDUCACIONAL01-896]** Ajuste no processo de bolsa retroativa para que o sistema não permita que as informações dos valores da bolsa não sejam alteradas quando a bolsa estiver parametrizada para não permitir a alteração.

Arquivo: RM.Edu.Financeiro.Form.dll

### Rotina: Correção nos filtros do processo de avaliação institucional.

* **[Ticket: EDUCACIONAL01-1030]** Ajuste no cadastro de avaliação institucional para alunos egressos.

Arquivo: RM.Edu.AvaliacaoInstitucional.Form.dll

### Rotina: ERRO não insere autoinc quando é a primeira vez que gera a turma

* **[Ticket: EDUCACIONAL01-1091]** Otimização no Cadastro Rápido de Turma e Turma/Disciplina quando se tinha um curso recém criado.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

### Rotina: NOTAS E FALTAS DE ETAPA EDU 50 318

* **[Ticket: 872283 / EDUCACIONAL01-905]** Ajuste no método que replica as aulas dadas quando se preencher vazio na mesma. Além disso, foi ajustado para que o botão Salvar fique habilitado apenas quando houver uma alteração na grid ou quando houver replicação das aulas dadas para a grid dos alunos.

Arquivo: RM.Edu.NotaFalta.Form.dll

### Rotina: PROCESSO SELETIVO TERCEIRIZADO EDU 50 394

* **[Ticket: 824335 / EDUCACIONAL01-800]** Foi realizada otimização do processo de matrícula, dentro do processo seletivo terceirado, de forma que, ao selecionar um plano de pagamento, somente sejam listados os planos de pagamento vigentes.

Arquivo: RM.Edu.ProcSel.Form.dll

### Rotina: SITUACAO DE MATRICULA EDU 50 439

* **[Ticket: 761064 / EDUCACIONAL01-253]** Melhoria no cadastro de situação de matricula, pois a opção "validar inadimplência de aluno na matrícula pelo portal" não estava ficando disponível ao salvar o registro.

Arquivos: RM.Edu.Academico.Data.dll, RM.Edu.Academico.Form.dll

### Rotina: TURMAS DISCIPLINAS EDU 50 454

* **[Ticket: 492700 / EDUCACIONAL01-200]** Exibir o campo de número máximo de alunos nas subturmas de turmas mistas ou turmas livres do ensino superior.

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

### Rotina: TURMAS EDU 50 453

* **[Ticket: 924665 / EDUCACIONAL01-992]** Ajuste na geração do autoincremento para o código da turma a fim de se evitar travamentos no banco de dados.

Arquivos: RM.Edu.Utils.Server.dll, RM.Edu.PeriodoLetivo.Server.dll

## TOTVS Folha de Pagamento

### Rotina: EVENTOS EVENTOS RELACIONADOS REPROGRAMACAO SALARIAL LAB 01 86

* **[Ticket: 801973 / FOPCALCULO01-233]** Ajusta número salário composto

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: GRUPO DE EVENTOS LAB 01 116

* **[Ticket: 772047 / FOPCALCULO01-250]** Ajuste para manter o valor da função de fórmula DTD no processo de Diferença Salarial.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: MNT PEDIDO DE PAGAMENTO MNT 012

* **[Ticket: 874941 / FOPCALCULO01-370]** Criado o parâmetro "Utilizar Fórmula Visual em Integração (SIGAMNT)" Em: Parametrizador: Folha de Pagamento > Integrações > Outros BackOffice Com este parâmetro marcado a mensagem "EMPLOYEE" será disparada pelo gatilho definido na fórmula visual.

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Parametros.Intf.dll, RM.Fop.TotvsMessage.Services.dll, RM.Fop.Parametros.Form.dll

### Rotina: PORTAL WEB ENVELOPE PGTO LAB 01 206

* **[Ticket: 586525 / FOPROTINAS01-169]** Ajuste no processo de visualização do Envelope de pagamento no RM Portal quando a jornada do funcionário é inferior a 1h.

Arquivo: RM.Fop.Envelope.Data.dll

### Rotina: Reoneração do Encargo INSS 13

* **[Ticket: FOPROTINAS01-498]** Para tratar os valores de encargos de INSS de 13º salários calculados por formula para a desoneração e aplicar os valores na reoneração foi criado duas funções de formula, a saber:VALENCARGO( mês, ano, CodEncargo) está função retorna a o valor de um encargo em uma data competência para o funcionário;VALPROVISAO13(mês, ano) está função retorna o valor da provisão do 13º salário somado a média de 13º salário para um funcionário.

Arquivo: RM.Fop.Calc.Formulas.dll

### Rotina: RESCISAO HOMOLOGNET LAB 01 219

* **[Ticket: 845559 / FOPROTINAS01-515]** Alterada a codificação do arquivo XML gerado de UTF-8 para ISO-8859-1. Feitos ajustes para geração de vários campos no formato correto, conforme manual do HomologNet.

Arquivo: RM.Fop.Processos.Data.dll

## TOTVS Framework

### Rotina: FUNCIONARIOS ENVIAR EMAIL PARA FUNCIONARIOS LAB 01 138

* **[Ticket: 792741 / FOPROTINAS01-547]** O Envio de e-mail foi otimizado.

Arquivos: RM.Lib.Gerador.dll, RM.Lib.Server.dll, RM.Lib.Gerador.Server.dll

### Rotina: HOST FRW00038

* **[Ticket: MFRWBH-1901]** Foi realizado um ajuste na detecção de jobs ativos.

Arquivo: RM.Lib.Jobs.Server.dll

### Rotina: PADRAO

* **[Ticket: MFRWBH-1916]** A Inclusão/Edição de Menu do Portal foi otimizada.

Arquivo: RM.Lib.Server.dll

### Rotina: PARAMETRIZACAO TIPO DE MOVIMENTO PAR 014

* **[Ticket: 962544 / MFRWBH-1925]** A utilização do workflow foi otimizada.

Arquivo: RM.Lib.dll

## TOTVS Gerador de Relatórios

### Rotina: RELATORIOS GERADOS FRW 00062

* **[Ticket: 950964 / MFRWBH-1917]** Melhoria para que ao clicar na impressão rápida, o relatório seja impresso apenas uma vez.

Arquivo: RM.Rpt.Reports.Form.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 952544 / CONTROLADORIA01-236]** Ao gerar a ECD os registros I155, I157, I355 e J100 deverão imprimir a natureza da conta quando o saldo for zero.

Arquivo: RM.Ctb.Sped.Service.dll

* **[Ticket: 843876 / CONTROLADORIA01-191]** Mudança na forma como a rotina do SPED calcula os Fatos Contábeis baseados em Expressão para que leve em conta o sinal parametrizado na coluna do Fato Contábil.

Arquivos: RM.Ctb.DemonstracaoContabil.Service.dll, RM.Ctb.Sped.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: COPIA POR REFERENCIA MOV 014

* **[Ticket: 756228 / MATFATCMPCRM01-283]** Melhoria na visualização do LookUp de movimento no processo de cópia por referência.

Arquivo: RM.Mov.Movimento.Data.dll

### Rotina: EDICAO DE MOVIMENTO MOV 002

* **[Ticket: 876965 / MATFATCMPCRM01-507]** Melhoria na inclusão de movimento parametrizado para editar preço total do item.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: INCLUSAO DE CONTRATO CTR 006

* **[Ticket: 904067 / MATESTCNTFTOF01-284]** Ajuste no cadastro do histórico do item de contrato.

Arquivo: RM.Ctr.Contrato.Form.dll

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: 825570 / MATFATCMPCRM01-506]** Selecionar corretamente a natureza de primeiro nível quando há retorno de duas naturezas inversas sinteticas, mas o tipo de movimento não está parametrizado para Editar a Natureza 2

Arquivo: RM.Mov.Integracoes.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: Downgrade Issue MRH-9061

* **[Ticket: RHU01-716]** Acertado campos de observação e período da experiência profissional

Arquivo: RM.Rhu.Lib.WinForms.dll

### Rotina: GERENCIA DE RH TABELAS SALARIAIS TABELAS RHU 36 044

* **[Ticket: 934259 / RHU01-691]** Correção para que o dado 'CODHISTORICO' seja consultado da tabela correta, retornando o histórico de tabela salarial corretamente.

Arquivo: RM.Rhu.TabelaSalarial.Intf.dll

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 832913 / RHU01-160]** Foi feita a correção para que a visão de pessoas não retorne 1 pessoa repetidas vezes quando a mesma possui mais de 1 registro profissional.

Arquivo: RM.Rhu.Pessoa.Data.dll

* **[Ticket: 613891 / RHU01-233]** Foi realizado ajuste para que seja possível carregar anexo que utilize 'RhuPessoaAction' contendo join com a coluna 'CODIGO' da tabela 'PPESSOA'.

Arquivo: RM.Rhu.Pessoa.Intf.dll

## TOTVS Gestão Financeira

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 840450 / EDUCACIONAL01-824]** Evolução no processo de Vincular / Desvincular cliente fornecedor a Pessoa para que seja possível executar o processo para várias Pessoas simultaneamente, ou seja, selecionar mais de um registro.

Arquivos: RM.Fin.CliFor.Intf.dll, RM.Fin.CliFor.Form.dll, RM.Fin.CliFor.Service.dll, RM.Fin.CliFor.Data.dll

### Rotina: LANCAMENTO GERAR ACORDO FIN 199

* **[Ticket: 921595 / FINANCEIRO01-852]** Ajuste no cálculo da base de cálculo de retenções no processo de acordo.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 945319 / FINANCEIRO01-910]** Realizar a baixa dos títulos através do arquivo de retorno de cobrança quando o arquivo possui linhas de registro e linhas de baixa

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: Informação cirurgica a partir da agenda cirurgica

* **[Ticket: 813559 / MSAU-8611]** Ajustes na tela de agendamento de cirurgia para exibir os campos vinculados do atendimento.

Arquivo: RM.Sau.AgendaCirurgia.Data.dll

### Rotina: Tela de Registro de atendimento Painel de eletivos não esta finalizando as senhas - Clinica Medshopping Santos

* **[Ticket: 809042 / MSAU-8494]** Ao realizar a chamada de uma senha no toten para atendimento eletivo, registrar o atendimento e efetuar a classificação de risco a senha é exibida na aba de atendimento médico e na aba de registro de atendimento. Alterado o painel de atendimentos eletivos para ao efetuar o registro do atendimento e a classificação de risco a senha não volte a aparecer na aba de registro de atendimento.

Arquivos: RM.Sau.RegistroAtendimento.Form.dll, RM.Sau.RegistroAtendimento.Server.dll

## TOTVS Incorporação

### Rotina: ALUGUEL EVENTO FINANCEIRO IMB 49 776

* **[Ticket: 816939 / TINPAD001-264]** Mensagem amigável ao incluir lançamentos de evento financeiro avulso no módulo de aluguel.

Arquivo: RM.Imb.Aluguel.Lancamento.Server.dll

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 905689 / TINPAD001-409]** Permissao de cadastro de comprador com o plano de financiamento gerado em base revitalizada.

Arquivo: RM.Imb.Venda.Contrato.Form.dll

# 12.1.15.159

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 892739 / PONTO01-536]** Foi realizado o ajuste da função de fórmula HORASTRABDESC evitando erro ao efetuar o recálculo.

Arquivo: RM.Pto.Formula.dll

### Rotina: PORTAL WEB ABONAR ATRASOS E FALTAS PTO 35 1257

* **[Ticket: 961403 / PONTO01-632]** Foi adicionado uma validação que analisa se o chefe do subordinado é externo antes de carregar o contexto do funcionário.

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 811218 / EDUCACIONAL01-717]** Ajuste no processo de cadastrar o aluno como responsável financeiro quando o mesmo possuir apóstrofo em seu nome, para que seja cadastrado o cliente/fornecedor com o apóstrofo também.

Arquivo: RM.Edu.Aluno.Server.dll

### Rotina: MATRICULAR ALUNO NAS DISCIPLINAS EDU 50 301

* **[Ticket: 751376 / EDUCACIONAL01-236]** Alteração do nome do parâmetro de "Excluir matrícula com movimentação" para "Permitir excluir matrícula no período letivo com movimentação em notas e frequência" nos parâmetros Educacionais do perfil do usuário. Além disso, foi incluído a validação da frequência diária digitada na exclusão, ou seja, o se o aluno possuir alguma falta lançada pela frequência diária e este parâmetro não estiver marcado, seja bloqueado a exclusão.Foi incluído também a validação da frequência diária na exclusão da matrícula em disciplina no parâmetro "Bloqueia a exclusão de disciplina do aluno caso haja notas e/ou faltas digitadas" em Configurações | Parâmetros | Matrícula | Movimento 1/4.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Facade.Intf.dll, RM.Edu.Parametros.Intf.dll, RM.Edu.Matricula.Server.dll, RM.Edu.Parametros.Form.dll

### Rotina: PROFESSORES EDU 50 403

* **[Ticket: 967417 / EDUCACIONAL01-1178]** Ajuste na abertura do anexo Dados para o censo escolar e SISTEC do cadastro do professor quando o mesmo possuir em seu código um apóstrofo para que seja aberto de forma correta.

Arquivo: RM.Edu.Professor.Data.dll

## TOTVS Folha de Pagamento

### Rotina: Base Desonerada para avos 13º Salario obtida Na Provisão de 13º salário

* **[Ticket: FOPROTINAS01-553]** Na Guia de INSS a base Desonerada para o cálculo dos avos desonerados de 13º salário será obtida com as seguintes regras: 1) Provisão do 13º Salário se: a. Existir provisão de 13º salário para última competência informada em "Encargos / Guia de INSS / Parâmetros da Guia de INSS Desoneração"; b. Avos de direito na vigência informada em "Encargos / Guia de INSS / Parâmetros da Guia de INSS Desoneração", Caso não exista provisão de 13º salário conforme o item "a.".

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: FOPROTINAS01-553]** Atualização dos resources para mensagens do log da guia de inss

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: COMPARATIVO SEFIP X FOLHA ANALITICA LAB 01 49

* **[Ticket: 394972 / FOPROTINAS01-117]** Ajuste na geração da Guia de INSS por tomador quando se tem um tomador default para a seção.

Arquivo: RM.Fop.Dominio.dll

### Rotina: EVENTOS EVENTOS RELACIONADOS REPROGRAMACAO SALARIAL LAB 01 86

* **[Ticket: 801973 / FOPCALCULO01-233]** Ajusta o número do salário

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: FERIAS CADASTRO FOP 34 538

* **[Ticket: 740213 / FOPCALCULO01-45]** Ajuste realizado ao setar o Props do DataSet onde estava alterando a coluna 'SITUACAOFERIAS' para somente leitura

Arquivo: RM.Fop.FuFerias.Data.dll

### Rotina: FUNCIONARIOS HISTORICOS FOP 34 499

* **[Ticket: 817463 / FOPCALCULO01-240]** Ajuste para que o afastamento tipo Y seja cadastrado com 15 dias, ao invés de 20, referente ao periodo de prorrogação da Licença Paternidade, em virtude do programa “Empresa Cidadã”, sobre o qual terá o incentivo fiscal relativo.

Arquivos: RM.Fop.Funcionario.Form.dll, RM.Fop.Funcionario.Server.dll, RM.Fop.Funcionario.Data.dll

### Rotina: Parâmetro para considerar a forma de cálculo do percentual redutor

* **[Ticket: FOPROTINAS01-537]** Inclusão do parâmetro "Tipo de Percentual Redutor" para que o usuário possa escolher entre o Ultimo percentual redutor cadastrado ou o percentual médio.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Dominio.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Server.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: FOPROTINAS01-537]** Conferencia feita no método CalcValorEncargo para testar a quantidade de linhas do hst provisão para não ocorrer acesso de posição de memória indevida.

Arquivo: RM.Fop.Calc.Formulas.dll

### Rotina: RELATORIO TRCT FOP 34 546

* **[Ticket: 962109 / FOPROTINAS01-543]** Ajuste no processo de geração do TRCT.

Arquivo: RM.Fop.Relatorios.Data.dll

## TOTVS Framework

### Rotina: PADRAO

* **[Ticket: MFRWBH-1916]** A Inclusão/Edição de Menu do Portal foi otimizada.

Arquivos: RM.Glb.Cadastros.Intf.dll, RM.Lib.Server.dll

### Rotina: PLANILHA NET EXECUCAO BIS 00047

* **[Ticket: 944577 / MFRWBH-1922]** -Quando utiliza-se uma sentença SQL que contém parametros de expressão o sistema deve considera-los como tal para buscar o valor corretamente.

Arquivo: RM.Glb.PlanilhaNet.Core.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: Cadastro de Manutenção de Inventário por Número de Série

* **[Ticket: MATESTCNTFTOF01-316]** Melhoria interna ao realizar consistência de produtos com número de série no serviço de inventário.

Arquivo: RM.Est.Inventario.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 917063 / RHU01-685]** Corrigido o erro de referência de objeto no processo de fechamento de avaliação.

Arquivo: RM.Rhu.AvalDesemp.Server.dll

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 927678 / RHU01-680]** Foi feita alteração de forma com que se a 'Nacionalidade' for Brasileira, o campo 'Data de Chegada' não seja obrigatório caso o usuário tenha setado o mesmo como de preenchimento obrigatório.

Arquivo: RM.Rhu.Pessoa.Form.dll

### Rotina: Project-904065 Visualização de Vagas para Candidatos Project-904065

* **[Ticket: 917756 / RHU01-668]** correção ao resgatar as vagas que um candidato já está concorrendo: Vagas que já passaram da data de fechamento são exibidas como vagas que o candidato está concorrendo.

Arquivo: RM.Rhu.Curriculo.Server.dll

### Rotina: Project-957271 ERRO ADMISSAO - REQUISICOES Project-957271

* **[Ticket: 958418 / RHU01-722]** Realizado ajuste em admissão proviniente de uma requisição.

Arquivo: RM.Rhu.Requisicao.Data.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES PRINCIPAIS APURACAO ICMS LI 01 0037

* **[Ticket: 935361 / FISCAL01-478]** Cadastro de Guia:- Foi criada uma nova classificação para guia Normal de ICMS: "Diferencial de Alíquota - Origem".- Não será possível mais editar o campo classificação com outros textos.Processo "Geração de Guias Automaticamente":- A guia de Difal do Estado de origem será o valor apurado no remetente do Difal com a classificação "Diferencial de Alíquota - Origem".Processo Sped Fiscal:- Guia com classificação "Diferencial de Alíquota - Origem" será considerada no registro E316 e não mais no registro E116.

Arquivos: RM.Fis.ApuracaoTrb.Intf.dll, RM.Fis.Parametros.Form.dll, RM.Fis.ApuracaoTrb.Form.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.Sped.Server.dll

## TOTVS Gestão Hospitalar

### Rotina: CLASSIFICACAO DE RISCO TOTEM SAU 47 1195

* **[Ticket: 872013 / MSAU-9172]** Realizado ajuste para retirar os espaços no início e no final do nome do paciente, ao registrar um atendimento pelo painel de classificação de risco.

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: CONTROLE DE PEDIDOS DE EXAMES SAU 47 1169

* **[Ticket: 967996 / MSAU-9979]** Ajustes na tela de geração de relátorio de exame.

Arquivo: RM.Sau.Integracoes.Server.dll

### Rotina: Pegar pacientes em observacão

* **[Ticket: 786162 / MSAU-9428]** Alterado o sistema adicionando um parâmetro "Médico visualiza todos os pacientes em Observação e Finalizados no Atendimento Médico" para que seja possível se o mesmo estiver marcado o médico visualizar pacientes que estão em observação com outros médicos e que estejam finalizados.

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: PCMSO RESPONSAVEL PELA MONITORACAO BIOLOGICA SMT 36 552

* **[Ticket: 913837 / RHU01-664]** Correção na consulta para filtrar filial

Arquivo: RM.Smt.Pessoa.Data.dll

# 12.1.15.160

## TOTVS Automação de Ponto

### Rotina: 01 - Criação de Horário com Tolerância

* **[Ticket: PONTO01-674]** Ajustado a geração de horário planejados onde não mais ocorrerá erro de referência de objeto quando registrado tolerâncias para todas as batidas planejadas.

Arquivo: RM.Pto.Horario.Data.dll

### Rotina: PORTAL WEB VISUALIZACAO DE OCORRENCIAS PTO 35 1252

* **[Ticket: 886196 / PONTO01-605]** Ajuste realizado: Incluído tag de segurança para Controle de Presença (Portal) -

Arquivos: RM.Pto.dll, RM.Pto.Server.dll

### Rotina: PROCESSO DE CALCULO DE ABONO PTO 35 1300

* **[Ticket: 928052 / PONTO01-580]** Foi efetuado um ajuste no registro de abonos do funcionário de modo que não mais ocorre erro de chave duplicada quando for abono por período.

Arquivos: RM.Pto.Ocorrencia.Data.dll, RM.Pto.Abono.Data.dll

## TOTVS Business Connect

### Rotina: Integração SigaMNT - Criação de serviço e MU para retornar o status do movimento

* **[Ticket: MATESTCNTFTOF01-246]** Disponibilizado no configurador da integração Manutenção de Ativos x BackOffice RM mensage única que retorna o status dos movimentos de Solicitação de Armazém/Solicitação de Compras.

Arquivos: RM.Con.ConfiguraIntegracao.TotvsManutencaoAtivos.dll, RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## TOTVS Educacional

### Rotina: MUDAR TURMA EDU 50 314

* **[Ticket: 873943 / EDUCACIONAL01-901]** Alteração para armazenar o número do aluno no Histórico da Matrícula no momento da matrícula e da mudança de turma.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Server.dll

### Rotina: PORTAL ALUNO QUADRO DE AVISOS EDU 50 364

* **[Ticket: 954519 / PORTALMOBILE01-774]** Melhoria na exibição das disciplinas matriculadas pelo aluno no quadro de avisos.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Academico.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Utils.Server.dll, RM.Edu.Academico.Data.dll, RM.Edu.Academico.Form.dll, RM.Edu.NotaFalta.Data.dll

* **[Ticket: 954519 / PORTALMOBILE01-774]** Melhoria na exibição das disciplinas matriculadas pelo aluno no quadro de avisos.

Arquivo: RM.Edu.Academico.Intf.dll

### Rotina: Teste Sistêmico - Educacional - Teste - Bolsa Retroativa

* **[Ticket: EDUCACIONAL01-1130]** Ajuste no processo de bolsa retroativa:1º O sistema permite que o valor da bolsa seja controlado no campo "Desconto" e neste caso o sistema não vai parametrizar os campos de valores opcionais para bolsa e com isso algumas validações não podem ser aplicadas, pois o campo desconto guarda também outros descontos, como o desconto de parcela.2º Para algumas validações o sistema tem que levar em consideração o campo desconto quando o os campos de valor opcional de bolsa não estiverem parametrizados.

Arquivos: RM.Edu.Financeiro.Form.dll, RM.Edu.Financeiro.Server.dll

## TOTVS Folha de Pagamento

### Rotina: EVENTOS EVENTOS RELACIONADOS REPROGRAMACAO SALARIAL LAB 01 86

* **[Ticket: 801973 / FOPCALCULO01-233]** Verifica nulidade do código evento

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: Execução Plano de Teste

* **[Ticket: FOPROTINAS01-497]** Ajustado erro de divisão por zeroAjuste no layout pois na 12.1.13 imprimia tudo numa pagina só, ao exportar e importar na 12.1.17 na segunda página o cabeçalho fica numa página e o gráfico em outra. Foi então ajustado a estrutura do dataset usado na 12.1.13 para poder imprimir corretamente na 12.1.17.

Arquivo: RM.Fop.Dominio.dll

### Rotina: Project-945687 CRIAÇÃO DE USUÁRIO PORTAL EM LOTE APRESENTA ERRO Project-945687

* **[Ticket: 951877 / FOPCALCULO01-407]** Ajuste na validação/mensagem de inclusão de um usuário de acesso ao portal quando já existe outro cadastrado para a chapa/pessoa

Arquivo: RM.Fop.Funcionario.Server.dll

## TOTVS Framework

### Rotina: MENUS CFGX013

* **[Ticket: MFRWBH-1952]** Ajuste no Menu HTML, para novos perfis que quando criados não incluem TAGMENU igual 0, não exibindo o menu para o Produto.

Arquivo: RM.Lib.Server.dll

### Rotina: PLANILHA NET EXECUCAO BIS 00047

* **[Ticket: 712648 / MFRWBH-1721]** -Ao salvar a planilha.Net os dados alterados devem ser armazenados corretamente.

Arquivo: RM.Glb.PlanilhaNet.API.dll

## TOTVS Gerador de Relatórios

### Rotina: CONFIGURACOES FRW 00016

* **[Ticket: 947211 / MFRWBH-1948]** Melhoria na execução de relatório de cartão de ponto.

Arquivo: RM.Rpt.Executor.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: FATURAMENTO RECEBIMENTO MOV 007

* **[Ticket: 789030 / MATFATCMPCRM01-476]** Melhoria no processo de faturamento parcial de movimento

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE IR E OU INSS FNC 003

* **[Ticket: 498588 / MATFATCMPCRM01-277]** Melhorias no processo responsável por gerar lançamento financeiro.

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS CURRICULOS EXTERNOS RHU 36 022

* **[Ticket: 939025 / RHU01-690]** Ajuste no carregamento de contexto de usuário logado no banco de talentos

Arquivos: FrameHTML

### Rotina: Project-859365 Erro ao alterar dados de estagiários Project-859365

* **[Ticket: 868098 / RHU01-763]** Realizando ajuste de erro referente a violação de concorrência ao salvar dados de funcionários estagiários.

Arquivo: RM.Rhu.Lib.WinForms.dll

### Rotina: REQUISICOES AUMENTO DE QUADRO RHU 36 095

* **[Ticket: 987090 / RHU01-766]** Realizado ajuste no RMPortal para que possa ser criadas requisições de aumento de quadro para todas as coligadas em que o funcionário é chefe, quando o sistema estiver parametrizado para utilizar gestão por hierarquia.

Arquivo: RM.Rhu.Hierarquia.Service.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: SERVICOS CRM 321448

* **[Ticket: 863108 / MATFATCMPCRM01-435]** Melhorias no processo responsável por criar atendimento por grupo de e-mail.

Arquivo: RM.CRM.Mail.Server.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO MANUTENCAO ALTERACAO GLOBAL FIN 202

* **[Ticket: 984980 / FINANCEIRO01-982]** Ajuste no conversor para nova baixa dos lançamentos do TIN

Arquivo: RM.Fin.Conversor.Service.dll

## TOTVS Gestão Fiscal

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 926457 / FISCAL01-489]** Serviço do tributação do movimento: Carregar a Modalidade da Base de Calculo do tributo ICMS-ST baseado na UF da Filial de Destino quando não é informado o código do Cliente\Fornecedor.

Arquivos: RM.Fis.Tributo.IService.dll, RM.Fis.Tributo.Service.dll

### Rotina: OBRIGACOES PRINCIPAIS APURACAO ICMS LI 01 0037

* **[Ticket: 987662 / FISCAL01-568]** Na apuração do tributo ICMS para o valor do "Saldo Anterior" observar o parâmetro "Considera Diferencial de Alíquota - Outros Débitos" para totalizar o Valor do Diferencial de Alíquota na Apuração.

Arquivo: RM.Fis.ApuracaoTrb.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: CONTROLE DE GLOSAS SAU 47 1162

* **[Ticket: 899062 / MSAU-9743]** Realizada a inclusão de uma mensagem para o usuário, caso o arquivo de retorno seja um demonstrativo de análise de conta e estiver na versão 3.02.00 da TISS.

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: OUTROS PROCESSOS SAU 47 1173

* **[Ticket: 878716 / MSAU-9228]** Ajuste realizado no formulário "Atendimento"/"Pronto Atendimento / Ambulatório"/"Painel de Classificação de Risco" , para que ao abrir formulário de "Classificação de Risco", o campo de checagem "Fluxo de Atendimento de Enfermagem" esteja desmarcado.

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

## TOTVS Incorporação

### Rotina: Liberação Revitalização TIN (Ambiente de teste)

* **[Ticket: 972593 / TINPAD001-504]** Liberação do CNPJ para cliente piloto.

Arquivo: RM.Imb.Venda.Upg.Data.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: ENTIDADES RHU 36 032

* **[Ticket: 664770 / RHU01-103]** Filtra entidades ativas

Arquivo: RM.Smt.Pessoa.Form.dll

### Rotina: RELATORIOS PERFIL PROFISSIOGRAFICO PREVIDENCIARIO PPP SMT 36 578

* **[Ticket: 373967 / RHU01-742]** Realizado ajuste no relatório PPP.

Arquivo: RM.Smt.Relatorio.Data.dll

# 12.1.15.161

## TOTVS Automação de Ponto

### Rotina: CADASTRO

* **[Ticket: PONTO01-693]** Foi ajustado o processo de alteração de dados dos funcionários de modo que não ocorra erros quando atualizado o Status do recalculo referente ao modulo de Ponto quando este não estiver habilitado ou o funcionário não utilize o ponto no modulo.

Arquivo: RM.Pto.Funcionario.Data.dll

### Rotina: Teste Sistêmico 12.1.17 PTO

* **[Ticket: PONTO01-612]** Ajustes realizados no cadastro de descanso dentro do espelho do funcionário.

Arquivos: RM.Pto.GruposDeDescanso.Form.dll, RM.Pto.GruposDeDescanso.Data.dll

* **[Ticket: PONTO01-612]** Ajuste do processo de aprovação de batidas pelo aplicativo.

Arquivos: RM.Pto.Batida.Data.dll, RM.Pto.Batida.Form.dll

## TOTVS Avaliação e Pesquisa

### Rotina: PROVA TST 30 1037

* **[Ticket: 966592 / EDUCACIONAL01-1189]** Ajuste na execução de avaliações sem tempo limite para execução.

Arquivo: App\_Web\_tstcabecalho.ascx.eb34a1f9.dll

## TOTVS Business Connect

### Rotina: Integração SigaMNT - Criação de serviço e MU para retornar o status do movimento

* **[Ticket: MATESTCNTFTOF01-246]** Ajuste no adapter da mensagem TraceAbilityRequest\_1.001, para bloquear alteração de movimentos de baixa integrados ao Manutenção de Ativos (SigaMNT) com status igual a Parcialmente Recebido/Faturado.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsManutencaoAtivos.dll

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: 973915 / MFRWBH-1945]** O conceito é gerado normalmente.

Arquivo: RM.Con.Concept.Server.dll

## TOTVS Construção e Projetos

### Rotina: Consistência na Apropriação de Apontamentos quando integrado com Protheus

* **[Ticket: TOPEXECONTROL01-294]** Implementação da integração da consistência que confronta apontamento do coletor com o ponto do funcionário quando integrado ao controle de ponto Protheus.

Arquivos: RM.Prj.Mobilidade.Server.dll, RM.Prj.Mobilidade.Data.dll

* **[Ticket: TOPEXECONTROL01-294]** Implementação da integração da consistência que confronta apontamento do coletor com o ponto do funcionário quando integrado ao controle de ponto Protheus.

Arquivo: RM.Prj.Mobilidade.Server.dll

## TOTVS Educacional

### Rotina: Cadastro de aluno com necessidades educacionais especiais

* **[Ticket: 967014 / EDUCACIONAL01-1188]** Sistema passou a verificar se existe um registro de origem para validação de dados anteriores de deficiência. Verificamos o registro de origem se o mesmo existir, ou seja, na inclusão de um aluno, não será verificado se a pessoa desse aluno possui dados de deficiências.

Arquivo: RM.Edu.Lib.WinForms.dll

### Rotina: DIPLOMACAO CERTIFICACAO EDU 50 178

* **[Ticket: 723032 / EDUCACIONAL01-132]** Otimização no Certificado/Diploma, onde foi criado o processo “Atualização de dados do Certificado e Registro no Livro” para permitir alterações globais no certificado e no registro no livro do certificado.- Nome da action deste processo: EduAlteracaoGlobalRegistroNoLivroAction. - Necessário recriar o broker.dat.- Somente será habilitado este processo, se marcado no Perfil do usuário a permissão de acesso ao mesmo (Atividades Acadêmicas | Certificado/Diploma | Certificados/diplomas | Atualização de dados do Certificado e Registro no Livro).- Será permitido alterar somente alguns campos que são editáveis e que não tenham tratamentos específicos, são eles: Dados do Certificado: data do certificado e carga horária. Dados do Registro no Livro: data de conclusão, data conferência, data de emissão, data de registro.- O campo “Data de Registro” atualmente não é editável no sistema, para permitir sua alteração é necessário marcar a opção “Permitir alterar data de registro do Registro no Livro do Certificado” no anexo “Parâmetros educacionais” do perfil do usuário.

Arquivos: RM.Edu.Academico.Intf.dll, RM.Edu.Parametros.Intf.dll, RM.Edu.Lib.WinForms.dll, RM.Edu.dll, RM.Edu.Parametros.Form.dll, RM.Edu.Academico.Form.dll

* **[Ticket: 723032 / EDUCACIONAL01-132]** Otimização no Certificado/Diploma, onde foi criado o processo “Atualização de dados do Certificado e Registro no Livro” para permitir alterações globais no certificado e no registro no livro do certificado - Menu Server

Arquivo: RM.Edu.Server.dll

* **[Ticket: 723032 / EDUCACIONAL01-132]** No Cadastro de Certificados/diplomas, o campo "Data registro" deve ficar desabilitado quando incluído certificado manualmente, sem registro no livro.

Arquivo: RM.Edu.Academico.Form.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 921412 / EDUCACIONAL01-1255]** Ajuste no filtro da seleção de consulta sql na tela de parâmetros gerais do Educacenso, quando se está em outra coligada diferente de 1.

Arquivo: RM.Edu.Cadastros.Form.dll

* **[Ticket: 910038 / EDUCACIONAL01-961]** Alteração no assistente de preparação do arquivo para o Educacenso, para retornar apenas as informações condizentes com filial ou nível de ensino logado, conforme configuração da Instituição do MEC.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.Academico.Form.dll, RM.Edu.Academico.Server.dll, RM.Edu.Academico.Data.dll

* **[Ticket: 1005510 / EDUCACIONAL01-1353]** Substituição dos apóstrofos dos códigos dos professores a fim de que as consultas executem normalmente.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: Project-999082 Visão de notas e faltas das etapas está indisponível pela Central do Aluno. Project-999082

* **[Ticket: 1011654 / EDUCACIONAL01-1379]** Otimizado a Central do Aluno, para permitir visualizar notas e faltas das etapas, quando estiver marcado o parâmetro do perfil do usuário “Visualizar consulta de notas e faltas na central do aluno” em qualquer um dos perfis deste usuário.

Arquivo: RM.Edu.Parametros.Intf.dll

## TOTVS Folha de Pagamento

### Rotina: Codificação

* **[Ticket: FOPROTINAS01-634]** Feitos ajustes para verificar se a descrição do registro de país lido da base de dados não é nula. Se for nula, será utilizado o código do país seguido de ' - Sem Desc' para preencher o combobox de países.

Arquivos: RM.Fop.Sindicato.Intf.dll, RM.Fop.Sindicato.Data.dll, RM.Fop.Sindicato.Form.dll

## TOTVS Framework

### Rotina: PADRAO

* **[Ticket: MFRWBH-1979]** Ajustes de License Server identificados pelo Critical log

Arquivos: RM.Lib.dll, RM.Lib.Server.dll, RM.Lib.WinForms.dll

### Rotina: PERMISSOES DE ACESSO FRW 00058

* **[Ticket: 1009014 / MFRWBH-2004]** Foi realizado um ajuste nas permissões da tela de perfil.

Arquivo: RM.Glb.Seguranca.Form.dll

### Rotina: RESCISAO CALCULO DE RESCISAO FOP 34 401

* **[Ticket: 986468 / FOPCALCULO01-438]** Ajuste no cálculo da remuneração base, quando a demissão é no mes anterior ao vencimento das férias, e com a projeção do aviso prévio indenizado, ultrapassa o final do periodo aquisitivo.

Arquivo: RM.Fop.Calc.CalculosBase.dll

## TOTVS Gerador de Relatórios

### Rotina: FILTRO RPT 00007

* **[Ticket: 939527 / MFRWBH-1882]** Melhoria na exibição de valores de data preenchidos pelo usuário no filtro de relatórios para operadores ">".

Arquivo: RM.Rpt.Lib.dll

### Rotina: FORMATACAO CONDICIONAL RPT 00040

* **[Ticket: 992169 / MFRWBH-1986]** Melhoria no controle da visibilidade de imagens no reports via formatação condicional.

Arquivo: RM.Rpt.Lib.dll

## TOTVS Gestão Contábil

### Rotina: ECF - Alteração na geração do M310 quando o Item Tributário é uma conta sintética

* **[Ticket: FISCAL01-465]** Alteração na geração do bloco M registro M310 da rotina federal ECF.Quando houver alguma conta sintética informada no evento tributário, ela deve ser listada no bloco M (310 ou 360) porém mostrando a conta analítica conforme listado no K355.

Arquivo: RM.Ctb.ECF.Service.dll

* **[Ticket: FISCAL01-465]** Alteração na geração do bloco M registro M310 da rotina federal ECF.Quando houver alguma conta sintética informada no evento tributário, ela deve ser listada no bloco M (310 ou 360) porém mostrando a conta analítica conforme listado no K355 ou K155.

Arquivo: RM.Ctb.ECF.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INTEGRACAO FINANCEIRA CONTAS A PAGAR RECEBER FNC 001

* **[Ticket: 761463 / MATFATCMPCRM01-465]** Melhoria para, no faturamento por valor, o sistema excluir corretamente o lançamento do movimento de origem quando estiver parametrizado para excluir.

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: CONTROLE DE LOTACAO DISTRIBUICAO DA LOTACAO RHU 36 076

* **[Ticket: 282753 / RHU01-281]** Foi realizado ajuste para que o quadro de lotação passe a considerar os funcionários com situação Z - Admissão no próx. mês no campo 'Alocados'

Arquivo: RM.Rhu.Lib.Server.dll

### Rotina: GESTAO POR COMPETENCIAS REQUISITOS DE ACESSO RHU 36 531

* **[Ticket: 758063 / RHU01-79]** correção na forma de pegar os dados requisito de acesso agregado

Arquivos: RM.Rhu.Competencia.Data.dll, RM.Rhu.Competencia.Form.dll

### Rotina: Project-940831 Envio de E-mail para candidato Project-940831

* **[Ticket: 958526 / RHU01-708]** possibilita utilizar o filtro do relatório

Arquivo: RM.Rhu.Facade.dll

### Rotina: REQUISICOES AUMENTO DE QUADRO RHU 36 095

* **[Ticket: 987090 / RHU01-766]** Realizado ajuste no RMPortal para que possa ser criadas requisições de aumento de quadro para todas as coligadas em que o funcionário é chefe, quando o sistema estiver parametrizado para utilizar gestão por hierarquia.

Arquivo: RM.Rhu.Hierarquia.Service.dll

## TOTVS Gestão Financeira

### Rotina: BAIXAS REALIZADAS ANEXO LANCAMENTO FIN 022

* **[Ticket: 1010153 / FINANCEIRO01-1040]** Ajuste na nova integração Educacional x Backoffice Protheus (Financeiro).

Arquivos: RM.Fin.Lan.Form.dll, RM.Fin.Lan.Service.dll

### Rotina: RELATORIO FLUXO DE CAIXA FIN 230

* **[Ticket: 929979 / FINANCEIRO01-851]** Disponibiliza modo de cálculo de aplicação financeira, padrão 11.80.

Arquivos: RM.Fin.AplicacaoFinanceira.Intf.dll, RM.Fin.Parametros.Intf.dll, RM.Fin.AplicacaoFinanceira.Form.dll, RM.Fin.AplicacaoFinanceira.Server.dll, RM.Fin.Formula.dll, RM.Fin.AplicacaoFinanceira.Data.dll

## TOTVS Gestão Fiscal

### Rotina: NFC E ENVIO NF 01 0056

* **[Ticket: 875206 / FISCAL01-452]** Alterado o processo de envio da NFC-e para não permitir enviar um movimento que está com status em contingência.

Arquivos: RM.Fis.NFe.Service.dll, RM.Fis.NFe.Data.dll

## TOTVS Gestão Hospitalar

### Rotina: OUTROS PROCESSOS SAU 47 1173

* **[Ticket: 753618 / MSAU-8388]** Realizado ajuste para gerar a DMED com todos os créditos de adiantamento pagos no ano.

Arquivo: RM.Sau.Faturamento.Data.dll

### Rotina: STATUS PEDIDOS DE EXAMES

* **[Ticket: 912585 / MSAU-10021]** Realizado ajuste para não alterar a situação do exame, caso a utilização do laudo de retorno do Carestream não esteja configurada.

Arquivo: RM.Sau.Integracoes.Server.dll

## TOTVS Incorporação

### Rotina: MODELO DE CALCULO PRICE IMB 49 843

* **[Ticket: 947703 / TINPAD001-485]** Melhoria na geração do plano PRICE para gerar as parcelas com valores iguais.

Arquivo: RM.Imb.Venda.Calc.CalculosBase.Controller.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: Melhoria - Parâmetros de imprimir ASO

* **[Ticket: RHU01-776]** Ajuste na escolha da impressão do endereço

Arquivos: RM.Smt.Lib.Form.dll, RM.Smt.Pessoa.Form.dll

### Rotina: PCMSO RESPONSAVEL PELA MONITORACAO BIOLOGICA SMT 36 552

* **[Ticket: 744516 / RHU01-85]** Ajuste permite imprimir dados da filial no ASO

Arquivo: RM.Smt.Lib.Data.dll

* **[Ticket: 771443 / RHU01-743]** correção para que ao lançar resultados de exames que não contenham tipo, esses acompanharão o tipo da consulta não sendo necessário informar o tipo de cada um individualmente, já que é um campo obrigatório.

Arquivos: RM.Smt.Clinico.Data.dll, RM.Smt.Clinico.Form.dll

### Rotina: SMT COMISSAO INTERNA DE PREVENCAO DE ACIDENTES CIPA SMT 36 012

* **[Ticket: 795343 / RHU01-123]** Feito ajuste para que não ocorra erro ao abrir a tela de inclusão de uma 'Eleição' aonde a comissão ainda não foi cadastrada.

Arquivo: RM.Smt.Cipa.Form.dll

# 12.1.15.162

## TOTVS Automação de Ponto

### Rotina: CADASTRO HORARIOS ALTERNATIVOS PTO 35 1293

* **[Ticket: 948184 / PONTO01-706]** Ajustes realizados no cálculo, para permitir o funcionamento correto quando a flag para abater atrasos estiver marcada.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: Erro ao recalcular espelho de ponto

* **[Ticket: 416507 / PONTO01-259]** Ajustado o processamento das jornadas carregadas no gráfico do espelho, era removido o último registro o que disparava um erro em outro processo.

Arquivo: RM.Pto.Batida.Form.dll

## TOTVS Educacional

### Rotina: Project-999251 Bloqueio dos campos da atividade curricular do aluno devido a forma de preenchimento. Project-999251

* **[Ticket: 1003657 / EDUCACIONAL01-1351]** Ajuste no cadastro de atividades curriculares do aluno no campo Componente para que o mesmo ao ser selecionado não trave a tela de cadastro.

Arquivo: RM.Edu.AtvCurricular.Form.dll

## TOTVS Folha de Pagamento

### Rotina: RESCISAO COMPLEMENTAR FOP 34 397

* **[Ticket: 975009 / FOPCALCULO01-460]** Ajuste no cálculo de media na rescisão complementar para considerar outros periodos com a mesma data de pagamento do envelope original da rescisão.

Arquivos: RM.Fop.Calc.Calculos.dll, RM.Fop.Calc.Formulas.dll

## TOTVS Framework

### Rotina: Histórico de provisões

* **[Ticket: 673451 / FOPCALCULO01-273]** Ajustado o Calculo da Media, para aceitar valores negativos no cálculo da provisão.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: REQUISICOES AUMENTO DE QUADRO RHU 36 095

* **[Ticket: 851417 / RHU01-172]** correção ao contolar possibilidade de editar o campo salário através do portal

Arquivo: App\_Web\_rhucoligadafilialsecaofuncao.ascx.6868da05.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: Erro na exibição da visão do movimento de destino após o faturamento

* **[Ticket: MATFATCMPCRM01-642]** Melhoria no processo de faturamento parametrizado para exibir na visão o movimento de destino

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: MNT BAIXA ESTOQUE APLICACAO DIRETA MNT 007

* **[Ticket: 834945 / MATESTCNTFTOF01-329]** Melhoria no serviço de integração com Manutenção de Ativos (SigaMNT) para que o movimento seja recalculado e a contabilização do movimento seja atualizada quando for cancelado um item de Baixa de Estoque.

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GESTAO POR COMPETENCIAS FATORES ORGANIZACIONAIS RHU 36 534

* **[Ticket: 946120 / RHU01-693]** Busca os dados com o código original

Arquivo: App\_Web\_rhuavaliacaodesempenhoexecucao.ascx.246e283e.dll

## TOTVS Gestão Financeira

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 990120 / FINANCEIRO01-1042]** Realizar a baixa dos títulos através do arquivo de retorno de cobrança quando o arquivo possui linhas de registro e linhas de baixa

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 96541 / FINANCEIRO01-520]** Ajustes no serviço de cálculo de valor líquido relacionados ao reajuste de valores do TIN.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Patrimonial

### Rotina: RM - Contábil/Patrimonial Teste Sistêmico 12.1.17

* **[Ticket: CONTROLADORIA01-239]** O lookup de cliente fornecedor foi alterado para que a descrição seja exibida corretamente.

Arquivo: RM.Pat.Transferencia.Form.dll

## TOTVS Incorporação

### Rotina: Distrato/Aditivo Revitalizada

* **[Ticket: 995553 / TINPAD001-577]** Melhoria no processo de aditivo de distrato, apenas versão revitalizada.

Arquivo: RM.Imb.Venda.Financeiro.Server.dll

### Rotina: Modelo de Cálculo: Padrão - MC Padrão e MC Idibra Juros e CM

* **[Ticket: TINREV001-30]** Melhoria no processo de distrato, apenas versão revitalizada.

Arquivos: RM.Imb.Venda.Lib.Intf.dll, RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Regra.Intf.dll, RM.Imb.Venda.Regra.Form.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Venda.Regra.Data.dll

* **[Ticket: TINREV001-30]** Melhoria na tela de log da parcela.

Arquivo: RM.Imb.Venda.Contrato.Form.dll

* **[Ticket: TINREV001-30]** Melhoria no processo de distrato, apenas versão revitalizada.

Arquivo: RM.Imb.Venda.Regra.Form.dll

* **[Ticket: TINREV001-30]** Melhoria no processo de distrato, apenas versão revitalizada.

Arquivo: RM.Imb.Venda.Regra.Form.dll

# 12.1.15.163

## TOTVS Automação de Ponto

### Rotina: HORARIOS PTO 35 1180

* **[Ticket: 980151 / PONTO01-685]** Ajuste no processo de verificação de utilização de ponto para funcionários que começaram a utilizar ponto no último dia do período ativo.

Arquivo: RM.Pto.Contexto.Server.dll

## TOTVS Business Connect

### Rotina: RM X ECM GED DOCUMENTOS INT 00007

* **[Ticket: 975627 / MFRWBH-2027]** Melhoria no sincronismo automático dos arquivos postados através do GED

Arquivo: RM.Con.GED.Data.dll

## TOTVS Construção e Projetos

### Rotina: MOBILIDADE FOLHA TAREFA PRJ 33 856

* **[Ticket: 931170 / TOPEXECONTROL01-304]** Ajuste no cadastro de itens de folha tarefa.

Arquivos: RM.Prj.Mobilidade.Data.dll, RM.Prj.Mobilidade.Form.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: CAD PROCEDIMENTO DE ORIGEM SAUIH 55 600

* **[Ticket: 854202 / MSAU-10287]** Ao realizar a alteração do procedimento NHSN vinculado ao procedimento de origem, se não existir nenhum procedimento NHSN vinculado o sistema não está atualizando as cirurgias que contenham esse procedimento de origem. Alterado o CIH para que quando for alterado o procedimento NHSN de um procedimento de origem as cirurgias sejam todas atualizadas com o mesmo procedimento NHSN.

Arquivo: RM.SauIH.Cadastros.Data.dll

## TOTVS Educacional

### Rotina: PORTAL ALUNO QUADRO DE AVISOS EDU 50 364

* **[Ticket: 1017117 / PORTALMOBILE01-875]** Ajuste na exibição do quadro de avisos para o ensino básico

Arquivo: RM.Edu.NotaFalta.Data.dll

### Rotina: PORTAL ALUNO TCC EDU 50 368

* **[Ticket: 794710 / PORTALMOBILE01-368]** Ajuste no acompanhamento do TCC para validar data e hora final para entrega do arquivo.

Arquivo: RM.Edu.MatrizCurricular.Server.dll

## TOTVS Folha de Pagamento

### Rotina: ALTERACOES GLOBAIS ALTERACAO CAMPOS DO CADASTRO LAB 01 1

* **[Ticket: 730634 / FOPROTINAS01-430]** Ajuste para considerar também Item Contábil e Classe de Valor da Seção na geração de Lançamentos Contábeis rateados por centro de custo

Arquivo: RM.Fop.Dominio.dll

### Rotina: FUNCIONARIOS HISTORICO DE COMPRA DE VALE TRANSPORTE LAB 01 151

* **[Ticket: 657148 / FOPROTINAS01-538]** Ajuste na Consulta da visão de histórico de compra de Vale Transporte.

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: GESTAO EDUCACIONAL FOP 34 421

* **[Ticket: 801969 / FOPCALCULO01-238]** Ajuste na rotina de reprogramação para desconsiderar registros de histórico salarial zerado na admissão.

Arquivos: RM.Fop.Educacional.Data.dll, RM.Fop.Infraestrutura.Repositorios.dll, RM.Fop.Funcionario.Data.dll, RM.Fop.Dominio.dll, RM.Fop.Funcionario.Intf.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS RAZAO CTB 38 114

* **[Ticket: 798233 / CONTROLADORIA01-197]** Configuração da paginação do relatório Razao.

Arquivos: RM.Ctb.Relatorios.Intf.dll, RM.Ctb.Relatorios.Form.dll, RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NF E ENVIO TOTVS COLABORACAO NF 01 0026

* **[Ticket: 841442 / FISCAL01-528]** Ajuste nos campos de Valor para que as casas decimais sejam geradas no xml corretamente

Arquivos: RM.Fis.NFe.Service.dll, RM.Fis.RotinasFiscais.Service.dll

# 12.1.15.164

## TOTVS Automação de Ponto

### Rotina: PARAMETROS RM PORTAL PTO 35 1218

* **[Ticket: 975030 / PONTO01-662]** Foi ajustado o carregamento do ícone que informa se o funcionário utiliza cartão e ponto na tela de subordinados do portal.

Arquivo: RM.Pto.Utils.Server.dll

### Rotina: PROCESSO DE CALCULO DE HORAS EXTRAS PTO 35 1238

* **[Ticket: 759496 / PONTO01-106]** Ajustes no processo de lançamento de extra autorizado sintético para permitir que o processo se comporte da maneira correta.

Arquivos: RM.Pto.Batida.Data.dll, RM.Pto.Extra.dll

## TOTVS Educacional

### Rotina: APROVEITAR VALORES EM CONTA CORRENTE EDU 50 020

* **[Ticket: 1008894 / EDUCACIONAL01-1437]** Ajuste na consulta de créditos em conta corrente para que considere o responsável financeiro correto do crédito na conta corrente do aluno tendo em vista que, quando o sistema está integrado com o Protheus, ele gera o registro de conta corrente na baixa do lançamento para o responsável da parcela e, quando o sistema vai aproveitar o crédito, ele estava consultando o fornecedor do cliente da aba Protheus do "Cliente/Fornecedor" fazendo com que o crédito não fosse encontrado pois o lançamento a pagar é gerado para esse Fornecedor associado citado.Consideração de aproveitamento de crédito a menor em conta corrente quando o sistema está integrado com o Protheus (Anteriormente, o sistema não estava aproveitando pagamentos a menor quando o sistema estava integrado)

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Financeiro.Server.dll

### Rotina: PORTAL ALUNO FREQUENCIA DIARIA EDU 50 354

* **[Ticket: 989076 / PORTALMOBILE01-819]** Ajuste na exibição da porcentagem de faltas na tela de Quadro de Avisos.

Arquivo: App\_Web\_eduquadroavisowebform.ascx.1d4ca059.dll

## TOTVS Folha de Pagamento

### Rotina: ALTERACOES GLOBAIS ALTERACAO CAMPOS DO CADASTRO LAB 01 1

* **[Ticket: 730634 / FOPROTINAS01-430]** Ajuste na contabilização para pegar corretamente o Item Contábil e Classe de Valor do agrupamento de contas

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 730634 / FOPROTINAS01-430]** Ajuste na contabilização para pegar corretamente o Item Contábil e Classe de Valor do agrupamento de contas

Arquivo: RM.Fop.Dominio.dll

### Rotina: Processo virada de competência não executa

* **[Ticket: 1039901 / FOPROTINAS01-724]** Otimização da consulta de AAS na liberação de competência

Arquivo: RM.Fop.Data.Server.dll

* **[Ticket: 1039901 / FOPROTINAS01-724]** Otimização da consulta de AAS na liberação de competência

Arquivo: RM.Fop.Data.Server.dll

### Rotina: Project-825197 manad Project-825197

* **[Ticket: 915303 / FOPROTINAS01-510]** Feitos ajustes no arquivo gerado segundo layout MANAD (v 1.0.0.2) para não considerar código de cálculo ao classificar um item do envelope de pagamentoto como Outros, Provento ou Desconto no campo 09 do registro K300 (IND\_RUBR) quando um evento do tipo base não possuir nenhuma incidência ou estorno.

Arquivo: RM.Fop.Manad.Data.dll

## TOTVS Framework

### Rotina: FERIAS CALCULO FOP 34 529

* **[Ticket: 1035970 / FOPCALCULO01-518]** Ajuste na informação exibida no log de medias quando não existe periodo para apuração do cálculo de media

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: LICENCESERVER FRW 00044

* **[Ticket: 1034666 / MFRWBH-2051]** Melhoria na validação para base de dados de teste

Arquivos: RM.Glb.Cadastros.Form.dll, RM.Lib.Server.dll, RM.Lib.dll

### Rotina: Pensão alimentícia -movimentação da pensão de dependente

* **[Ticket: 693203 / FOPCALCULO01-7]** Ajuste na diferença do movimento de pensão alimentícia.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: USUARIO BCS30001

* **[Ticket: MFRWBH-2037]** Replicar o método ExecuteUpdateSenhaUsuarioPost implementado na versão 11.83.55 para a versão 12.1.14 e superiores

Arquivos: RM.Glb.Seguranca.Intf.dll, RM.Glb.Seguranca.Server.dll

* **[Ticket: MFRWBH-2038]** Replicar o método ExecuteUpdateSenhaUsuarioPost implementado na versão 11.83.55 para a versão 12.1.14 e superiores

Arquivo: RM.Glb.Seguranca.Server.dll

## TOTVS Gerador de Relatórios

### Rotina: MATRIZ RPT 00029

* **[Ticket: 837990 / MFRWBH-1870]** Melhoria para que a matriz do reports possa exibir valore nulos.

Arquivo: RM.Rpt.Lib.dll

## TOTVS Gestão Contábil

### Rotina: ECF - Alteração na geração do M310 quando o Item Tributário é uma conta sintética

* **[Ticket: FISCAL01-465]** Alteração na geração do bloco M registro M310 da rotina federal ECF.Quando houver alguma conta sintética informada no evento tributário, ela deve ser listada no bloco M (310 ou 360) porém mostrando a conta analítica conforme listado no K355 ou K155.

Arquivo: RM.Ctb.ECF.Service.dll

### Rotina: ESCRITURACAO CONTABIL LANCAMENTOS CTB 39 006

* **[Ticket: 714621 / CONTROLADORIA01-178]** Ao salvar um lançamento contábil o campo documento passou a respeitar o parâmetro "Preenchimento com zeros à esquerda".

Arquivo: RM.Ctb.Lan.Service.dll

### Rotina: RM - Contábil/Patrimonial Teste Sistêmico 12.1.17

* **[Ticket: CONTROLADORIA01-239]** Atualização no relatório Plano de Contas.

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: TREINAMENTO TURMAS RHU 36 055

* **[Ticket: 526133 / RHU01-818]** Corrigido a verificação de frequencia para considerar a frequência como um valor de percentual

Arquivo: RM.Rhu.Turmas.Server.dll

## TOTVS Gestão Fiscal

### Rotina: Codificação

* **[Ticket: FISCAL01-534]** Foram realizadas alterações para que ao gerar o registro M305 da ECF, quando o Tipo de Relacionamento do M300 for 3 (com conta contábil e lalur parte B), para que o sistema considere que o cálculo é acumulativo e, portanto considerar a movimentação da conta durante todo o período.

Arquivos: RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: FISCAL01-670]** Implementação da tag IdCnae no layout unico do TSS.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: ESCRITURACAO LI 01 0025

* **[Ticket: 896540 / FISCAL01-460]** Flag "ICMS por Dentro soma no valor contábil" sendo informado incorretamente na regras de geração do TipoNatICMS.

Arquivo: RM.Fis.NaturezaOper.Service.dll

### Rotina: IMPORTACAO DE PRODUTO PRD 004

* **[Ticket: 952659 / FISCAL01-675]** Foi identificado que o problema acontecia quando o Produto não possuía Dados Fiscais cadastrados.Foram realizadas alterações na Importação de Código CEST para que, quando o Produto não possuir Dados Fiscais cadastrados, o sistema não emita a mensagem: “Referência de objeto não definida para uma instância de uma classe”.

Arquivo: RM.Fis.Cadastros.Services.dll

* **[Ticket: 952659 / FISCAL01-675]** Retornei a alteração realizada na Issue FISCAL01-675. Pois a mesma era desnecessária na versão atual.

Arquivo: RM.Fis.Cadastros.Services.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 930671 / FISCAL01-482]** No processo de Envio da NFS-e através do Layout Unico foi implementado o preenchimento da TAG numeroEncap conforme orientação do TSS.Versão do TSS compativel: 2.71

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS E GERAR ARQUIVO TXT NF 01 0053

* **[Ticket: 905612 / FISCAL01-562]** Estamos deixando de validar o campo Codigo do Serviço do movimento, para o preenchimento do CNAE.Agora, será considerado CNAE:Se o campo Código de Receita Federal (dados fisicais do produto) estiver preenchido;Senão irá levar o CNAE da Filial Emitente.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: ELABORACAO DE BPA SAU 47 1146

* **[Ticket: 904721 / MSAU-9865]** Realizado ajuste para exibir o parâmetro que configura o sistema para realizar lançamento automático de BPA, na tela de parâmetros do SUS.

Arquivo: RM.Sau.Sus.Form.dll

### Rotina: MOVIMENTACOES DE ESTOQUE SAU 47 1126

* **[Ticket: 971219 / MSAU-10143]** Realizado ajuste para processar a requisição de estoque.

Arquivo: RM.Sau.Produto.Server.dll

### Rotina: UNIDADES DE ATENDIMENTO E FATURAMENTO SAU 47 1110

* **[Ticket: 1000735 / MSAU-10183]** Rollback pois não deve ser comitado nesta versão.

Arquivos: RM.Sau.CadastrosFat.Data.dll, RM.Sau.UnidadeDiagnostico.Data.dll

* **[Ticket: 1000735 / MSAU-10183]** Validado o parâmetro de Filtrar unidades de atendimento nas telas de Cadastro de Leitos, Cadastro de Exames e de Condições Financeiras com Convênio, e caso ele esteja marcado, filtrar as informações somente para as unidades de atendimento do perfil do usuário.

Arquivos: RM.Sau.CadastrosFat.Data.dll, RM.Sau.UnidadeDiagnostico.Data.dll

## TOTVS Gestão Patrimonial

### Rotina: INTEGRACOES INTEGRACAO OCORRENCIAS PENDENTES PAT 37 107

* **[Ticket: 857356 / CONTROLADORIA01-192]** O Lookup de responsável foi alterado para retornar todos os funcionários cuja situação seja diferente de D (demitido).

Arquivo: RM.Pat.Integracao.Form.dll

### Rotina: RM - Contábil/Patrimonial Teste Sistêmico 12.1.17

* **[Ticket: CONTROLADORIA01-239]** O relatório de contabilização foi alterado para retornar as contabilizações de impairment e reversão de impairment.

Arquivo: RM.Pat.Relatorio.Data.dll

## TOTVS Incorporação

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 807686 / TINPAD001-371]** Ajuste no DataSet de vendas, onde existiam tipos de campo diferentes entre a tabela XVENDA e algumas tabelas filhas.

Arquivo: RM.Imb.Contratos.Intf.dll

* **[Ticket: 807686 / TINPAD001-371]** Sem alteração. Apenas para forçar a compilação da DLL Server

Arquivo: RM.Imb.Contratos.Server.dll

### Rotina: Modelo de Cálculo: Padrão - MC Padrão e MC Idibra Juros e CM

* **[Ticket: TINREV001-30]** Melhoria para o utilitários de lançamentos imobiliários.

Arquivo: RM.Imb.Conversor.Data.dll

# 12.1.15.165

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO OCORRENCIAS PTO 35 1193

* **[Ticket: 951411 / PONTO01-608]** Ajustes no parâmetro "Substitui jornada planejada que iniciou no feriado", para permitir o cálculo correto das ocorrências em jornadas iniciadas após o feriado.

Arquivo: RM.Pto.Horario.Data.dll

## TOTVS Educacional

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 1036429 / EDUCACIONAL01-1471]** Acerto no processo de preparação de dados para o Censo, a fim de evitar validações entre códigos com capitalização diferentes entre a disciplina e a turma/disciplina.

Arquivo: RM.Edu.Academico.Server.dll

* **[Ticket: 1034509 / EDUCACIONAL01-1454]** Foi incluído o campo "Ensino fundamental realizado em ciclos" na tela de Dados do Censo da Filial (para a versão 12.1.13 e 12.1.14) e na tela de Instituição do MEC (a partir da versão 12.1.15).A rotina de preparação do arquivo para o Educacenso foi alterada para não enviar a informação de ensino fundamental realizado em ciclos quando não existir turmas de ensino fundamental na instituição.

Arquivos: RM.Edu.Cadastros.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.Cadastros.Form.dll

## TOTVS Folha de Pagamento

### Rotina: CENTROS DE CUSTO RM LABORE FOP 34 361

* **[Ticket: 730718 / FOPROTINAS01-360]** Correção no processo de sincronismo de centro de custo do Labore para casos de inconsistência de base onde o status da GCCusto estiver vazio.

Arquivo: RM.Fop.Cadastros.Data.dll

### Rotina: FUNCIONARIOS CADASTRO LAB 01 128

* **[Ticket: 883888 / FOPCALCULO01-417]** Ajustado para só apagar os dados caso esteja sendo considerado a Tabela Salarial. Onde o Nível e a Faixa não estejam vinculado a Tabela Salarial.

Arquivo: RM.Fop.Funcionario.Data.dll

## TOTVS Framework

### Rotina: FERIAS CALCULO FOP 34 402

* **[Ticket: 698315 / FOPCALCULO01-14]** Ajuste ao aplicar a última carga horária trabalhada, no caso de afastamento integral no mês.

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: PROCESSOS DO PRODUTO PRD 002

* **[Ticket: 818515 / MATESTCNTFTOF01-335]** Ajuste na rotina de Conversão de Produto Global para considerar a tabela Produtos TOTVS Colaboração.

Arquivo: RM.Est.Produto.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: MAPA DE CONHECIMENTO DEFINICAO POR COMPETENCIAS RHU 36 080

* **[Ticket: 787188 / RHU01-119]** correção ao gerar autoavaliação por arquivo XML

Arquivo: RM.Rhu.Lib.Server.dll

## TOTVS Gestão Financeira

### Rotina: FORMULAS FIN 171

* **[Ticket: 524304 / FINANCEIRO01-345]** Retornar valor correto da função de fórmula BAIXADO.

Arquivo: RM.Fin.Formula.dll

### Rotina: Melhoria na performance do Cubo de Recebíveis e Pagáveis

* **[Ticket: FINANCEIRO01-1165]** Melhoria de Perfomance no Cubo quanto ao Cálculo do Valor Liquido.

Arquivo: RM.Fin.Relatorio.Data.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 532593 / FISCAL01-144]** Alterado o preenchimento do registro E210, para que quando existir lançamento de entrada de débito, esta informação seja levada apenas no campo 10 VL\_AJ\_DEBITOS\_ST e não mais preencher o campo6 VL\_OUT\_CRED\_ST do registro E210.

Arquivos: RM.Fis.Utils.Intf.dll, RM.Fis.Sped.Engine.dll, RM.Fis.Sped.Server.dll, RM.Fis.RotinasFiscais.Service.dll

## TOTVS Incorporação

### Rotina: DISTRATO BILATERAL IMB 49 817

* **[Ticket: 1011925 / TINREV001-36]** Melhoria no processo de distrato (data cancelamento venda), apenas para versão revitalizada.

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

# 12.1.15.166

## Outros

### Rotina: USUÁRIOS - SEGURANÇA FRW00076

* **[Ticket: MFRWBH-2099]** Melhoria no acesso a base de teste pelo WebAPI

Arquivos: FrameHTML

## TOTVS Automação de Ponto

### Rotina: Relatório de Exceções

* **[Ticket: 312220 / PONTO01-279]** Foi ajustado os dados de batidas executadas no relatório de exceção de modo que estes sejam exibidos adequadamente e também prevenindo a exibição de datas que não tenham exceções dos funcionários.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Business Connect

### Rotina: PADRAO

* **[Ticket: MFRWBH-2094]** Melhoria na utilização do WsDataServer para que o valor default definido pelo usuário seja setado para os campos não preenchidos no registro independente da utilização do schema do data server.

Arquivo: RM.Con.Conector.Server.dll

## TOTVS Educacional

### Rotina: BOLSA RETROATIVA EDU 50 479

* **[Ticket: 756342 / EDUCACIONAL01-230]** Realizamos uma melhoria no log do processo de bolsa retroativa1º O Log passa a mostra informações das bolsas concedidas ou excluídas2º O log passa a detalhar de forma mais organizada e objetiva os contratos, RA, parcela e lançamentos que foram atualizados3º Os erros apresentado durante a execução do processo ficam separados ao final do log demostrando apenas informações dos contratos que e lançamentos que não foram atualizados

Arquivos: RM.Edu.Financeiro.Data.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Utils.Intf.dll, RM.Edu.Financeiro.Intf.dll, RM.Edu.Financeiro.Server.dll

* **[Ticket: 756342 / EDUCACIONAL01-230]** Realizamos uma melhoria no log do processo de bolsa retroativa1º O Log passa a mostra informações das bolsas concedidas ou excluídas2º O log passa a detalhar de forma mais organizada e objetiva os contratos, RA, parcela e lançamentos que foram atualizados3º Os erros apresentado durante a execução do processo ficam separados ao final do log demostrando apenas informações dos contratos que e lançamentos que não foram atualizados

Arquivo: RM.Edu.Financeiro.Data.dll

* **[Ticket: 867802 / EDUCACIONAL01-958]** Foi realizada otimização do processo de geração de lançamentos, de forma que, antes de aproveitar valores da conta corrente do aluno, o valor de bolsa exclusiva seja arredondado, conforme as regras do financeiro, afim de se evitar que valor líquido do lançamento fique negativo, devido arredondamento da bolsa exclusiva..

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 924244 / EDUCACIONAL01-1006]** Ajustes no agrupamento quando gerado os lançamentos.

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: 924244 / EDUCACIONAL01-1006]** Ajustes na ordenação utilizado no agrupamento quando gerado os lançamentos.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: GERACAO DE ARQUIVOS ENADE EDU 50 226

* **[Ticket: 934297 / EDUCACIONAL01-1260]** Adequação ao ENADE 2017 conforme regras do INEP

Arquivos: RM.Edu.Academico.Intf.dll, RM.Edu.Academico.Form.dll, RM.Edu.Academico.Server.dll

* **[Ticket: 1010863 / EDUCACIONAL01-1382]** Adequação do ENADE 2017 às alterações em Instituição do MEC e Curso do MEC

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Academico.Form.dll, RM.Edu.Academico.Server.dll

### Rotina: GERACAO DE CERTIFICADOS DIPLOMAS EDU 50 227

* **[Ticket: 721210 / EDUCACIONAL01-89]** Otimização no processo de “Geração de certificado/diploma”, para tratar corretamente o status Apto ou Pendente ao verificar o Enade do aluno Dispensado da prova.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: PORTAL CONTEXTO EDU 50 475

* **[Ticket: 970757 / PORTALMOBILE01-921]** Ajuste no corregamento de informações de contexto, quando o usuário logado é um coordenador de curso.

Arquivo: RM.Edu.Contexto.Data.dll

## TOTVS Folha de Pagamento

### Rotina: COMPARATIVO SEFIP X FOLHA ANALITICA LAB 01 49

* **[Ticket: 717513 / FOPROTINAS01-758]** Ajuste para correto cálculo da base de IRRF de férias

Arquivo: RM.Fop.Envelope.Data.dll

### Rotina: EVENTOS EVENTOS RELACIONADOS REPROGRAMACAO SALARIAL LAB 01 86

* **[Ticket: 1041831 / FOPCALCULO01-534]** Ajuste na rotina de reprogramação salarial para tratamento de divisão por zero.

Arquivos: RM.Fop.Educacional.Data.dll, RM.Fop.Funcionario.Data.dll

### Rotina: EVENTOS PROGRAMADOS LAB 01 139

* **[Ticket: 726970 / FOPCALCULO01-33]** Para que o número de ficha de registro não gere duplicidade é necessário entrar em "Configurações > Parametrizador > Folha de Pagamento > Funcionário > Configuração de Registro" e verificar se o campo "Número da Ficha de Registro gerado pelo sistema" está marcado. Após, continue avançando até concluir o processo.

Arquivo: RM.Fop.Parametros.Data.dll

### Rotina: IMPORTACAO DE DADOS DO RM LABORE LAB 01 26

* **[Ticket: 831769 / FOPROTINAS01-732]** Ajuste na importação de histórico de dados bancários do funcionário

Arquivo: RM.Fop.Importacao.Data.dll

### Rotina: LANCAMENTOS FINANCEIROS PARAMETRIZACAO FOP 34 383

* **[Ticket: 364645 / FOPROTINAS01-592]** Ajuste no processo de geração do Lançamento Financeiro através do SEFIP.

Arquivo: RM.Fop.Dominio.dll

### Rotina: PORTAL WEB GESTAO DE FERIAS LAB 01 208

* **[Ticket: 921376 / FOPROTINAS01-486]** Ajuste para correta validação do período aquisitivo com saldo para o funcionário na marcação de férias pelo RM Portal

Arquivo: RM.Fop.FuFerias.Data.dll

### Rotina: Project-960633 Importar movimento Project-960633

* **[Ticket: 964233 / FOPCALCULO01-414]** Ajuste realizado para validação da quantidade de horas a ser importada no movimento

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Framework

### Rotina: FERIAS CALCULO FOP 34 402

* **[Ticket: 698315 / FOPCALCULO01-14]** Ajuste no cálculo da remuneração base, quando a demissão é no mes anterior ao vencimento das férias, e com a projeção do aviso prévio indenizado, ultrapassa o final do periodo aquisitivo.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: FORMULAS EXECUCAO FRW 00033

* **[Ticket: 1070268 / MFRWBH-2107]** -Ao realizar a importação de objetos que contenham uma consulta SQL, e o sistema não possuir a consulta com o código informado, a consulta deve ser importada corretamente.

Arquivo: RM.Glb.ImpExp.Server.dll

### Rotina: RECLASSIFICAR

* **[Ticket: RHU01-272]** Foi implementada validação de CPF para validar se todos os dígitos são iguais, e retornar falso caso seja.

Arquivo: RM.Lib.dll

* **[Ticket: RHU01-272]** Retirada da validação de todos os dígitos iguais no CPF.

Arquivo: RM.Lib.dll

### Rotina: USUÁRIOS - SEGURANÇA FRW00076

* **[Ticket: MFRWBH-2005]** Melhoria na desconexão automática do usuário para liberação das licenças

Arquivo: RM.Lib.dll

## TOTVS Gerador de Relatórios

### Rotina: FILTRO RPT 00007

* **[Ticket: 712241 / MFRWBH-2102]** -Ao gerar um relatório pela visão contendo filtro por usuário ou perfil, o sistema deve atribuir corretamente os valores das variáveis para a execução do relatório.

Arquivo: RM.Rpt.Executor.Service.dll

### Rotina: IMAGEM RPT 00015

* **[Ticket: 1077703 / MFRWBH-2119]** Melhoria na visibilidade de imagens dentro do reports.

Arquivo: RM.Rpt.Lib.dll

## TOTVS Gestão Contábil

### Rotina: ESCRITURACAO CONTABIL FISCAL CTB 38 165

* **[Ticket: 849996 / CONTROLADORIA01-195]** Atualização da ECF para que o registro K355 não gere quebra por centro de custo no registro K155 quando este não tem conta parametrizada como rateio.

Arquivo: RM.Ctb.ECF.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CONTABILIZAR MOVIMENTO MOV 026

* **[Ticket: 794549 / MATFATCMPCRM01-570]** Ao importar um movimento a partir de um arquivo txt usando o Conceito, a data dos lançamentos contabeis não estavam respeitando a parâmetrização definida.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: CUPOM FISCAL COM 022

* **[Ticket: 757410 / MATFATCMPCRM01-656]** Melhorias no cadastro de cupom fiscal.

Arquivo: RM.Mov.CupomFiscal.Service.dll

### Rotina: IMPORTACAO DE MOVIMENTO MOV 039

* **[Ticket: 877626 / MATFATCMPCRM01-564]** Melhoria na importação de movimento de devolução

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: NFC E IMPRESSAO DE DANFE NF 01 0058

* **[Ticket: 383076 / MATFATCMPCRM01-610]** Melhorias no cadastro de meio de pagamento.

Arquivos: RM.Mov.Lib.dll, RM.Mov.Cadastros.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: CURRICULOS CURRICULOS EXTERNOS RHU 36 022

* **[Ticket: 649738 / RHU01-88]** Ajuste realizado para não ocorrer problema ao acessar o perfil no banco de talentos

Arquivo: RM.Rhu.Curriculo.Server.dll

## TOTVS Gestão Financeira

### Rotina: CADASTRO BANCARIO PAGAMENTO INCLUSAO ALTERACAO EXCLUSAO FIN 063

* **[Ticket: 945995 / FINANCEIRO01-927]** Otimização no processo de arquivo de retorno. Agora o sistema mantem a ordem de linha do arquivo quando não tiver no mesmo arquivo um registro para registrar e baixar. Quando acontecer de ter no mesmo arquivo um registro para registrar e baixar, o sistema irá separa-lo para executar-lo na ordem correta, primeiramente registra e logo após realiza a baixa.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANCAMENTO ALTERACAO FIN 172

* **[Ticket: 870391 / FINANCEIRO01-837]** Ajuste na permissão do campo de centro de custo do lançamento quando já remetido ou em borderô.

Arquivo: RM.Fin.Lib.dll

### Rotina: LANCAMENTO ANEXO BOLETO FIN 176

* **[Ticket: 578023 / FINANCEIRO01-180]** Ajuste na exibição de boletos a partir do anexo de lançamentos quando acessado pelos sistemas Educacional ou Biblioteca.

Arquivo: RM.Fin.Lan.Data.dll

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 656456 / FINANCEIRO01-1037]** Otimização no campo Histórico de cheque. Agora o sistema informa corretamente a informação dos mnemônicos formatados no campo Histórico utilizando o parâmetro "Histórico default cheque a pagar / a receber" durante a baixa, a emissão ou recebimento de cheque para somente um lançamento.

Arquivos: RM.Fin.Extrato.Intf.dll, RM.Fin.Extrato.Service.dll, RM.Fin.Lan.Data.dll, RM.Fin.Lan.Form.dll

### Rotina: LANCAMENTO VINCULAR LANCAMENTOS FIN 214

* **[Ticket: 1014271 / FINANCEIRO01-1190]** Permitir vinculo de devolução para lançamento classificado como "Gerado por Acordo" e tipo de documento "Devolução"

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: Permitir alterar a data de emissão dos lançamentos originados do Educacional e Processo Seletivo

* **[Ticket: FINANCEIRO01-830]** A data de emissão não deve ser travada se lançamento gerado pelo Educacional.

Arquivo: RM.Fin.Lib.dll

## TOTVS Gestão Fiscal

### Rotina: NFC E IMPRESSAO DE DANFE NF 01 0058

* **[Ticket: 383076 / FISCAL01-203]** Implementação da Tag pag de acordo com os Meios de Pagamento do Movimento NFC-e.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 973254 / FISCAL01-540]** Efetuada melhoria na NFS-e para que a tag <identificador> seja gerada carregando o valor do campo"Documento Estrangeiro" presente no cadastro de cliente/fornecedor (FCFO.DOCUMENTOESTRANGEIRO).

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES ACESSORIAS ESTADUAIS APURACAO ICMS LI 01 0028

* **[Ticket: 882002 / FISCAL01-437]** Foram realizadas as Implementações referentes as adquações da DIME/SC - Apartir de Abril de 2017

Arquivos: RM.Fis.Lib.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.LancFiscal.Form.dll

## TOTVS Gestão Hospitalar

### Rotina: ELABORACAO DE BPA SAU 47 1146

* **[Ticket: 1032847 / MSAU-10478]** Realizado ajuste para importar procedimentos iguais mas com médicos diferentes.

Arquivo: RM.Sau.Sus.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: MOVIMENTAÇÕES - AVALIAÇÃO PATRIMONIAL PAT3799

* **[Ticket: 95448 / CONTROLADORIA01-51]** Foram realizadas algumas melhorias no processo de importação de avaliações. As mensagens inseridas no log estão mais claras. Também foram adicionadas algumas validações para impedir a geração de avaliações negativas e revisões de vida útil desnecessárias.

Arquivos: RM.Pat.Ocorrencia.Data.dll, RM.Pat.Ocorrencia.Form.dll

### Rotina: OPCOES PREFERENCIAS DE USUARIO PAT 37 61

* **[Ticket: 591911 / CONTROLADORIA01-40]** Ajuste na tela para que ao fixar o campo "Tipo" o parâmetro "Geração automática do Nº do patrimônio" continue funcionando normalmente.

Arquivo: RM.Pat.Patrimonio.Form.dll

### Rotina: RELATORIOS CONTABILIZACAO PAT 37 57

* **[Ticket: 781226 / CONTROLADORIA01-215]** O relatório contábil, do módulo patrimonial, sofreu alterações para não duplicar os valores apresentados após a realização do agrupamento de lançamentos contábeis.

Arquivo: RM.Pat.Relatorio.Data.dll

## TOTVS Incorporação

### Rotina: ADITIVO RENEGOCIACAO DE CONTRATO IMB 49 784

* **[Ticket: 964512 / TINPAD001-547]** Ajuste na validação do aditivo de renegociação para permitir incluir parcelas que não sejam do plano MCMV

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll

### Rotina: Desenvolvimento dos parâmetros do Reajuste

* **[Ticket: TINREV001-40]** AJuste na tela de regra para não salvar sem alteração

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Regra.Intf.dll, RM.Imb.Venda.Regra.Data.dll, RM.Imb.Venda.Regra.Form.dll

### Rotina: REAJUSTE AGENDAMENTO IMB 49 850

* **[Ticket: 923811 / TINPAD001-443]** Ajsute no processo de exclusão do distrato para não excluir a data de próximo reajuste para as regras que não sejam do distrato

Arquivo: RM.Imb.Contratos.Server.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: Msg Funcionário com Licença Maternidade

* **[Ticket: 975909 / RHU01-860]** Realizado ajuste ao salvar um atestado duas vezes.

Arquivo: RM.Smt.Pessoa.Data.dll

### Rotina: SMT COMISSAO INTERNA DE PREVENCAO DE ACIDENTES CIPA SMT 36 012

* **[Ticket: 795343 / RHU01-123]** Realizado ajuste no cadastro da CIPA para que os anexos não fiquem disponíveis no momento da inclusão de um novo registro. O anexo estará disponível apenas quando o registro for salvo. Desta forma o usuário não conseguirá salvar o anexo antes de salvar o registro principal, evitando erros.

Arquivo: RM.Smt.Cipa.Form.dll

# 12.1.15.167

## TOTVS Automação de Ponto

### Rotina: Project-1069576 RH Online - Solicitar abonos Project-1069576

* **[Ticket: 1074980 / PONTO01-804]** Foi ajustado a exibição de ocorrências de atrasos e faltas no portal, de modo que estas sejam exibidas corretamente quando desmarcado o parâmetro “Realiza compensação de extras e atrasos antes da autorização e cálculo do abono”.

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Educacional

### Rotina: GERACAO DE ARQUIVOS ENADE EDU 50 226

* **[Ticket: 1010863 / EDUCACIONAL01-1382]** Adequação do ENADE 2017 às alterações em Instituição do MEC e Curso do MEC

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: LANCAMENTO INCLUSAO FIN 200

* **[Ticket: 1082883 / EDUCACIONAL01-1626]** Campo segundonumero passou a não ser mais copiado na regeração de um lançamento cancelado.

Arquivo: RM.Edu.Financeiro.Server.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIOS RESCISAO LAB 01 177

* **[Ticket: 990361 / FOPCALCULO01-479]** Criação do parâmetro "Forçar incidência de INSS no CC 62 e CC 99 até a data".

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Parametros.Intf.dll, RM.Fop.Calc.Calculos.dll, RM.Fop.Parametros.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: GESTAO POR COMPETENCIAS DICIONARIO RHU 36 047

* **[Ticket: 889849 / RHU01-658]** Permitido a inserção de novos participantes em uma avaliação de desempenho 360 em andamento

Arquivo: RM.Rhu.AvalDesemp.Form.dll

## TOTVS Gestão Financeira

### Rotina: BAIXAS REALIZADAS REGERAR CONTABILIZACAO DE BAIXA FIN 029

* **[Ticket: 1036045 / FINANCEIRO01-1157]** Desbloqueia exibição de menu de Regeração de Contabiliação e Solicitação de Exclusão Contábil

Arquivo: RM.Fin.Lan.Data.dll

## TOTVS Gestão Fiscal

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 490989 / FISCAL01-610]** Implementação do município de São João Del Rei - MG

Arquivos: RM.Fis.Lib.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - ECF LI010032

* **[Ticket: 94941 / FISCAL01-207]** ECF - Lucro da Exploração:Layout ECF:O registro N600 da ECF foi ajustado para comportar os calculos de valores de acordo com o código da tabela dinâmica e efetuar a soma corretamente.Apuração:Na apuração do registro N600 com código tabela dinâmica 46 quando a Despesa Financeira ficar maior que a Receita os Itens Tributários serão zerados conforme regra da ECF.

Arquivo: RM.Fis.RegrasTributarias.Service.dll

## TOTVS Gestão Patrimonial

### Rotina: MOVIMENTAÇÕES - AVALIAÇÃO PATRIMONIAL PAT3799

* **[Ticket: 95448 / CONTROLADORIA01-51]** Após a execução do processo de avaliação patrimonial estavam sendo criados, incorretamente, uma revisão de vida útil e um saldo residual zerado para o cenários avalíados.

Arquivos: RM.Pat.Patrimonio.Service.dll, RM.Pat.PatrimonioMoeda.Service.dll

## TOTVS Incorporação

### Rotina: ADITIVO TROCA DE COMPRADOR IMB 49 785

* **[Ticket: 1087369 / TINREV001-47]** AJuste na Troca de comprador para gravar 50 caracteres no campo nome por limitação do campo da base.

Arquivos: RM.Imb.Venda.Lib.Intf.dll, RM.Imb.Venda.Aditivo.Intf.dll, RM.Imb.Venda.Calc.Calculos.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Venda.Aditivo.Form.dll

# 12.1.15.168

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 908968 / PONTO01-788]** Alterações no processo de recálculo para validar corretamente alterações de atitude de ocorrências.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: PORTAL WEB APROVAR ABONOS PTO 35 1268

* **[Ticket: 909326 / PONTO01-564]** Alteração da rotina de preenchimento das informações no formulário de solicitação do abono.

Arquivos: RM.Pto.Ocorrencia.Intf.dll, RM.Pto.Abono.Intf.dll, RM.Pto.Abono.Data.dll, Web.config, App\_Web\_ptocodabono.ascx.7d151a08.dll

### Rotina: PORTAL WEB VISUALIZACAO DE OCORRENCIAS PTO 35 1252

* **[Ticket: 379789 / PONTO01-242]** Foi ajustado o processo de abono de ocorrências calculadas de modo que o mesmo sendo efetuado pelo Chefe do subordinado também irá validar a ocorrência.Todas as ocorrências estando validadas a sinalização, na tela de subordinados do portal, de que há ocorrências a serem validadas não será exibido.

Arquivos: RM.Pto.VisualizarOcorrencias.Data.dll, RM.Pto.Ocorrencia.Data.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 870285 / PONTO01-609]** Alterações no processo de geração do relatório do espelho do cartão, solucionando o problema de referência de objeto.

Arquivos: RM.Pto.EventosCalculados.Data.dll, RM.Pto.Relatorio.Data.dll

## TOTVS Construção e Projetos

### Rotina: BACKUP RESTAURACAO DE PROJETOS PRJ 33 781

* **[Ticket: 1086511 / TOPORCAPLAN001-751]** ERRO NA FÓRMULA DE INSUMOS AO RESTAURAR BACKUP DE PROJETOS

Arquivo: RM.Prj.BackupRestore.Data.dll

## TOTVS Educacional

### Rotina: BOLETOS EDU 50 069

* **[Ticket: 575893 / EDUCACIONAL01-158]** Alteração da chamada para geração do relatório que era assíncrona para chamada síncrona a fim de evitar que a tela de aguardando execução trave o sistema como um todo. Anteriormente, as duas chamadas assíncronas estavam entrando em conflito fazendo com que uma ficasse aguardando o término da execução da outra causando um travamento do sistema.

Arquivo: RM.Edu.Lib.WinForms.dll

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 975654 / EDUCACIONAL01-1257]** Foi realizada otimização do processo de geração de movimentação em regime de competência, permitindo ao sistema, gerar movimentação em regime de caixa para boletos oriundos de parcelas do tipo extra, mesmo quando o sistema estiver parametrizado para gerar movimento em regime de competência.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: GERACAO DE ARQUIVOS ENADE EDU 50 226

* **[Ticket: 1010863 / EDUCACIONAL01-1382]** Correção no filtro de alunos para NÃO verificar se o código do INEP da habilitação foi informado, pois esse campo não é mais utilizado.Correção na pesquisa de Curso do MEC na tela de Matriz Aplicada para permitir a inclusão de um novo curso através da pesquisa.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.MatrizCurricular.Data.dll, RM.Edu.MatrizCurricular.Form.dll

### Rotina: PORTAL ALUNO ESTAGIO EDU 50 352

* **[Ticket: 911258 / PORTALMOBILE01-670]** Ajuste na exibição de detalhes do termo de compromisso de estágio.

Arquivo: RM.Edu.MatrizCurricular.Data.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 1068659 / EDUCACIONAL01-1573]** Alteração no Censo para verificar se a data de início e término da turma do professor está de acordo com a data de referência do censo.

Arquivo: RM.Edu.Academico.Server.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIOS RESCISAO LAB 01 177

* **[Ticket: 990361 / FOPCALCULO01-479]** Ajuste no envelope para considerar parâmetro "Forçar incidência de INSS no CC62 e CC99 até a data:" (para demitidos até essa data). Este valor é mostrado na Aba Incidências no Envelope.

Arquivos: RM.Fop.Data.Intf.dll, RM.Fop.Data.Server.dll, RM.Fop.Envelope.Data.dll

## TOTVS Framework

### Rotina: URL EXTERNA CADASTRO FWB 00013

* **[Ticket: 889598 / MFRWBH-1950]** Melhoria no recurso de URLs externas do RM para que adicione as chaves do RM como parâmetros adicionais a URL.

Arquivo: RM.Glb.Cadastros.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: ANEXOS DO PRODUTO PRD 003

* **[Ticket: 978880 / MATESTCNTFTOF01-325]** Ao incluir no novo tributo o sistema estava deixando visível o Campo Código Receita, sendo que o mesmo só pode ser visível caso o tributo seja do tipo Contribuição Previdenciária.

Arquivo: RM.Est.Produto.Form.dll

### Rotina: CT E CONSULTA DE EVENTO CTE 007

* **[Ticket: 946982 / MATFATCMPCRM01-584]** Melhoria no cancelamento de movimento de CT-e

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 926457 / MATFATCMPCRM01-629]** Melhorias na rotina responsável por buscar os defaults do tributo no movimento.

Arquivos: RM.Mov.Movimento.Intf.dll, RM.Mov.Facade.dll, RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Form.dll

### Rotina: MNT PEDIDO DE PAGAMENTO MNT 012

* **[Ticket: 992211 / MATESTCNTFTOF01-361]** Ajuste na rotina que executa o gatilho de fórmula visual de integração da mensagem InfoOfParcelValues\_1.000

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: CANDIDATOS RHU 36 001

* **[Ticket: 823781 / RHU01-830]** Com o novo processo de seleção, o Perfil de Triagem não é mais vinculado a Função. O Perfil de Triagem é associado ao Perfil de Vaga da Seleção. Por esse motivo o campo está desabilitado no cadastro de Função e para melhor entendimento ele foi excluído.

Arquivo: RM.Rhu.Funcoes.Form.dll

### Rotina: Project-1061517 Iniciar processo de seleção/Executar triagem Project-1061517

* **[Ticket: 1063355 / RHU01-884]** Realizado ajuste no processo de triagem.

Arquivo: RM.Rhu.Captacao.Data.dll

### Rotina: REQUISICOES SUBSTITUICAO RHU 36 504

* **[Ticket: 942085 / RHU01-847]** Inclusão das premissões Incluir/Excluir/Editar nas permissões de perfil

Arquivo: RM.Rhu.Server.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: ATENDIMENTOS CRM 321443

* **[Ticket: 1018929 / MATFATCMPCRM01-702]** Melhoria na visualização de atendimentos parametrizado para restringir acesso de atendimentos por hierarquia de localidade

Arquivo: RM.CRM.Atendimento.Data.dll

## TOTVS Gestão Financeira

### Rotina: CADASTROS

* **[Ticket: FINANCEIRO01-360]** Ajuste no processo de validação de campos obrigatorios definidos pelo usuario supervisor na tela de cadastro do cliente/fornecedor.

Arquivo: RM.Fin.CliFor.Service.dll

### Rotina: CARTAO DE CREDITO TRANSACOES FIN 068

* **[Ticket: 1068009 / FINANCEIRO01-1238]** Melhoria no processo de pagamento por cartão de crédito Cielo Checkout - Utilizar o Id. Transação como OrderNumber

Arquivos: RM.Fin.Lan.Intf.dll, RM.Fin.Lan.Service.dll, RM.Fin.Lan.Data.dll, App\_Web\_finlancartaodadoscadastraisuc.ascx.51ca41ad.dll, App\_Web\_finlancartaomudancastatus.aspx.c12e96e5.dll, App\_Web\_finlancartaonotificacao.aspx.c12e96e5.dll

### Rotina: CheckOut - Ao realizar o ChargeBack para transação de cartão, o lançamento relacionado não é cancelado.

* **[Ticket: FINANCEIRO01-1093]** Melhoria no processo de pagamento por cartão de crédito Cielo Checkout

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: EXTRATO DE CAIXA INCLUSAO ALTERACAO EXCLUSAO FIN 151

* **[Ticket: 973244 / FINANCEIRO01-973]** Otimização no processo de baixa de um lançamento utilizando o meio de pagamento igual a cheque buscando dados default do emitente (Coligada). Agora o sistema carrega corretamente a opção tipo de inscrição ch da forma que o campo CPF/CNPJ estiver preenchida.

Arquivo: RM.Fin.Cheque.Form.dll

### Rotina: Nota de Crédito

* **[Ticket: 1060961 / FINANCEIRO01-1308]** Ajuste no cancelamento de de baixa de lançamento vinculado a uma Nota de Crédito, Nota de Crédito de Adiantamento ou Devolução que possui boleto.

Arquivos: RM.Fin.Utils.Server.dll, RM.Fin.Lan.Service.dll

* **[Ticket: 1060961 / FINANCEIRO01-1308]** Ajuste para não permitir gerar boleto para lançamentos de Devolução, Nota de Crédito e Nota de Crédito de Adiantamento que possuem vínculos em aberto.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO DE PAGAMENTO FIN 238

* **[Ticket: 659347 / FINANCEIRO01-1223]** Tratamento código de ocorrência 03 - CNAB240

Arquivo: RM.Fin.Banco.Data.dll

## TOTVS Gestão Fiscal

### Rotina: CADASTROS NATUREZA DE OPERACAO LI 01 0015

* **[Ticket: 1014446 / FISCAL01-699]** Otimização no processo de alteração da máscara de CFOP.

Arquivo: RM.Fis.NaturezaOper.Data.dll

### Rotina: EVENTOS

* **[Ticket: FISCAL01-876]** Ajuste no envio da CC-e para que o XML sejá convertido em byte corretamente sem ignorar os caracteres especiais.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NFS E ATUALIZACAO DE MUNICIPIOS HOMOLOGADOS NF 01 0023

* **[Ticket: 1100588 / FISCAL01-878]** Liberação do município de Batatais - SP.Municipio envia NFS-e, Consulta NFS-e, envia cancelamento de NFS-e e Consulta o cancelamento de NFS-e.Este municipio NÃO permite o envio de substituição.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.Form.dll, RM.Fis.Lib.dll

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 994526 / FISCAL01-886]** Alteração na geração da tag discrdedu, ela não era considerada quando o movimento possuia mais de 1 item.

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.Data.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - ECF LI010032

* **[Ticket: 94774 / FISCAL01-832]** A issue em questão foi implementada na versão Atual (12.1.18). Porém, foi necessário implementar as alterações no contexto da ECF desde a versão 11.80, para manter a compatibilidade do Layout em todas as versões.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES PRINCIPAIS APURACAO ISS LI 01 0043

* **[Ticket: 1024477 / FISCAL01-869]** Ajustado no Processo de Encerramento de Período de Apuração para que a mensagem não seja apresentada.

Arquivo: RM.Fis.ApuracaoTrb.Service.dll

## TOTVS Incorporação

### Rotina: ALUGUEL CONTRATO DE LOCACAO IMB 49 774

* **[Ticket: 1045007 / TINPAD001-606]** Incluindo função de fórmula para retornar a data de contabiização do aluguel além da correta carga do contexto em todas as situações.

Arquivos: RM.Imb.Recursos.dll, RM.Imb.Formula.dll

### Rotina: Desenvolvimento dos parâmetros do Reajuste

* **[Ticket: TINREV001-40]** Melhoria na tela de condições de financiamento do tipo correção monetária.

Arquivo: RM.Imb.Venda.Regra.Form.dll

### Rotina: Problema no calculo do Seguro por emprendimento - Revitalização SGI

* **[Ticket: 1095726 / TINREV001-48]** Melhoria no processo de calculo do seguro por empreendimento, apenas projeto de revitalização TIN.

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: VENDA EFETIVACAO GERACAO PLANO DE FINANCIAMENTO IMB 49 869

* **[Ticket: 1097147 / TINREV001-49]** Melhoria no processo de calculo do seguro por empreendimento, apenas projeto de revitalização TIN.

Arquivo: RM.Imb.Venda.Regra.Intf.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: RELATORIOS GERAL RHU 36 579

* **[Ticket: 1100447 / RHU01-940]** Ajuste realizado ao utilizar SmtBrigadistasAction na criação de novo Formulário em metadados

Arquivo: RM.Smt.EPC.Data.dll

# 12.1.15.169

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 979118 / PONTO01-679]** Ajustes realizados no processo de recálculo para permitir o funcionamento correto do processo.

Arquivo: RM.Pto.Calculo.Service.dll

* **[Ticket: 979118 / PONTO01-679]** Remoção de código desnecessário.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 870285 / PONTO01-609]** Melhoria no código evitando redundância, não tem efeito direto para o usuário.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Business Connect

### Rotina: MNT BAIXA ESTOQUE APLICACAO DIRETA MNT 007

* **[Ticket: 1014867 / MATESTCNTFTOF01-370]** Ajuste nos arquivos de Transformação da mensagem CancelRequest\_1.000 para considerar o correto DataServer de cancelamento.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsMessage.dll

## TOTVS Educacional

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 975654 / EDUCACIONAL01-1257]** Foi realizada otimização do processo de geração de movimentação em regime de competência, permitindo ao sistema, gerar movimentação em regime de caixa para boletos oriundos de parcelas do tipo extra, mesmo quando o sistema estiver parametrizado para gerar movimento em regime de competência.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: GERACAO DE MOVIMENTO EDU 50 229

* **[Ticket: 837119 / EDUCACIONAL01-883]** Foi realizada otimização do processo de geração de movimento, permitindo ao sistema, que o código de serviço do produto no município seja carregado pelo TOTVS Gestão de Estoque, Compras e Faturamento, conforme parametrização do movimento. Se o movimento estiver parametrizado para editar município por item, o sistema buscará o código do serviço com base na tributação do item.

Arquivos: RM.Edu.Consts.dll, RM.Edu.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Financeiro.Server.dll

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 695425 / EDUCACIONAL01-1097]** Ajuste ao filtrar a frequência diária pelo ReadView no webservice do dataserver EduFrequenciaDiariaWSData, para que ao inserir o filtro de data o mesmo seja respeitado e retornando os registros corretos.

Arquivo: RM.Edu.NotaFalta.Data.dll

### Rotina: Project-1072300 Relações Empresariais - Cadastro Project-1072300

* **[Ticket: 1086452 / EDUCACIONAL01-1623]** Ajuste na validação de tipos de documentos duplicados no cadastro de empresas.

Arquivo: RM.Edu.MatrizCurricular.Server.dll

### Rotina: REMATRICULA EDU 50 421

* **[Ticket: 1097933 / EDUCACIONAL01-1729]** Ajuste na visualização da numeração da turma.

Arquivo: RM.Edu.Processos.Data.dll

## TOTVS Folha de Pagamento

### Rotina: EVENTOS PROGRAMADOS LAB 01 139

* **[Ticket: 726970 / FOPCALCULO01-33]** Nº Ficha Reg. agora pega o maior valor entre as coligadas e se "Selecionar por CNPJ" estiver marcado, pega o Reg. por CNPJ

Arquivo: RM.Fop.Parametros.Data.dll

### Rotina: EXPORTACAO DE ARQUIVOS FOP 34 439

* **[Ticket: 796384 / FOPROTINAS01-278]** Correção do Nis e qualificação cadastral, realizada com sucesso.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

### Rotina: FUNCIONARIOS RESCISAO LAB 01 177

* **[Ticket: 990361 / FOPROTINAS01-849]** Feitos ajustes no MANAD para forçar a incidência de INSS em eventos com CC 62 ou 99 lançados na ficha financeira até a data inserida no parâmetro "Forçar incidência de INSS no CC62 e CC99 até a data", encontrado no parametrizador

Arquivos: RM.Fop.Data.Server.dll, RM.Fop.Manad.Data.dll

* **[Ticket: 990361 / FOPROTINAS01-848]** Para A Folha Analítica e o comparativo SEFIP o sistema passa a considerar a incidência de INSS dos eventos de código de cálculo 62 - Aviso Prévio e 99 - Diferença de Aviso Prévio Se: 1) A competência da Folha Analítica seja igual ou superior a informada no parâmetro "Verificar incidência CC 62 e CC 99 a partir" no Parametrizador \ Rescisão \ Aviso Prévio:". E 2) A data de demissão do funcionário esteja anterior à data informada no parâmetro "Forçar incidência de INSS no CC 62 E CC 69 até a data:" no Parametrizador \ Rescisão \ Aviso Prévio:". No comparativo SEFIP o parâmetro "Considera Valor de Aviso Prévio no SEFIP" influencia em considerar ou não o evento de CC 62 na base de INSS. Porém o parâmetro "Forçar incidência de INSS no CC 62 E CC 69 até a data:" tem prioridade.

Arquivo: RM.Fop.Relatorios.Data.dll

## TOTVS Gerador de Relatórios

### Rotina: MATRIZ RPT 00029

* **[Ticket: 1130342 / MFRWBH-2197]** Melhoria na execução de relatórios que contenham matriz.

Arquivo: RM.Rpt.Lib.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS BALANCETE CTB 38 113

* **[Ticket: 801569 / CONTROLADORIA01-214]** Melhoria no relatório Balancete para que gere fazendo a quebra por Filial mesmo em cenários com número excessivo de Contas Contábeis.

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: ANEXOS DO PRODUTO PRD 003

* **[Ticket: 978880 / MATESTCNTFTOF01-325]** Melhoria de performance no cadastro de Tributos do Produto.

Arquivo: RM.Est.Produto.Form.dll

### Rotina: COPIA POR REFERENCIA MOV 014

* **[Ticket: 756228 / MATFATCMPCRM01-658]** No processo de cópia por referência, ao usar um filtro que utilize dados do item de movimento para buscar movimentos, não deve ser mostrados movimentos repetidos.

Arquivo: RM.Mov.Movimento.Data.dll

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: 983598 / MATFATCMPCRM01-733]** Melhorias no processo responsável pela inclusão de movimento através de XML.

Arquivo: RM.Mov.Integracoes.Service.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: ATENDIMENTOS CRM 321443

* **[Ticket: 471255 / MATFATCMPCRM01-845]** Melhorias no processo responsável pelo avanço de etapas do atendimento.

Arquivo: RM.CRM.Atendimento.Form.dll

## TOTVS Gestão Financeira

### Rotina: BORDERO REMESSA DE PAGAMENTO FIN 055

* **[Ticket: 908201 / FINANCEIRO01-838]** Ajuste na busca do tabela de Remessa de Pagamento

Arquivo: RM.Fin.Formula.dll

* **[Ticket: 908201 / FINANCEIRO01-838]** Ajuste na Fórmula DADOSPAGAMENTOBRADESCO('InformacoesComplementares') para pagamentos Cheque Administrativo.

Arquivo: RM.Fin.Formula.dll

### Rotina: CADASTRO DE CLIENTES

* **[Ticket: FINANCEIRO01-1450]** Ajuste no serviço que verifica o preenchimento dos campos definidos como obrigatório pelo usuário supervisor na tela de cadastro de cliente/fornecedor

Arquivo: RM.Fin.CliFor.Service.dll

## TOTVS Gestão Fiscal

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 926457 / MATFATCMPCRM01-629]** Ajuste no serviço que carrega os Defaults dos Tributos dos Itens do Movimento, o campo modalidade da Base cálculo do tributo ICMS-ST foi evoluido para carregar este campo quando destino é Empresa.

Arquivo: RM.Fis.Tributo.Service.dll

### Rotina: PARAMETROS INTEGRACAO LI 01 0056

* **[Ticket: 901453 / FISCAL01-906]** Alteração na geração das informações do DIFAL na Nota Fiscal Eletrônica.O calculo das tags do valor do ICMS do Destinatário e do valor do ICMS do Remetente estavam sendo feitos incorretamente, dando uma diferença de 1 centavo para mais.

Arquivo: RM.Fis.NFe.Service.dll

## TOTVS Gestão Patrimonial

### Rotina: INTEGRACOES INTEGRACAO AQUISICOES COMPRAS RM NUCLEUS PAT 37 64

* **[Ticket: 1084161 / CONTROLADORIA01-341]** Atualização do processo de constituição de patrimônio quando da integração com o RMNucleus referente ao parâmetro “Gerar o código do patrimônio a partir do título do patrimônio definido no produto” que faz com que o sistema passe a buscar titulo amarrado ao patrimônio pelo código do grupo do produto do RMNucleus caso não tenha amarração no grupo de patrimônio.

Arquivos: RM.Pat.Integracao.IService.dll, RM.Pat.Integracao.Intf.dll, RM.Pat.Integracao.Data.dll, RM.Pat.Integracao.Form.dll

## TOTVS Incorporação

### Rotina: Aditivo antecipação de parcelas

* **[Ticket: 987053 / TINPAD001-509]** Melhoria no aditivo de antecipação de parcela em base não revitalizada.

Arquivo: RM.Imb.Aditivos.Form.dll

* **[Ticket: 987053 / TINPAD001-509]** Melhoria no aditivo de antecipação de parcela em base não revitalizada.

Arquivo: RM.Imb.Aditivos.Form.dll

* **[Ticket: 987053 / TINPAD001-509]** Melhoria no aditivo de antecipação de parcela em base não revitalizada.

Arquivo: RM.Imb.Aditivos.Form.dll

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 1107680 / TINPAD001-684]** Cancelar Venda (Data Cancelamento) - Melhoria no processo de cancelamento da venda, a data da venda passa a ser salva na tabela XVENDA e
  apresentada corretamente no relatório de vendas canceladas. A data do cancelamento é a data da execução do processo de cancelamento.

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

# 12.1.15.170

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB ABONAR ANTES DA COMPENSACAO PTO 35 1258

* **[Ticket: 1047874 / PONTO01-848]** 1º incidente: Foi realizado ajuste para que os parâmetros para executar o recálculo seja do funcionário e não do usuário logado (gestor).2º incidente: A atribuição dos valores para preenchimento do paramsProc.CodColigadaResp e paramsProc.ChapaResp está verificando se o usuário logado é um chefe externo ou não, evitando assim erro de referência de objeto, este erro somente ocorre caso o chefe seja externo.3º incidente: Não tem correção no código, trata-se de entendimento.

Arquivos: RM.Pto.Abono.Data.dll, RM.Pto.JustExcecao.Data.dll, RM.Pto.JustExcecao.WebForm.dll

## TOTVS Educacional

### Rotina: GERACAO DE MOVIMENTO EDU 50 229

* **[Ticket: 837119 / EDUCACIONAL01-883]** Criação de mensagem de alerta ao executar o processo de geração de movimento, tanto em regime de caixa quanto em regime de competência, onde o sistema TOTVS Educacional não mais informará o código do serviço do movimento (código do serviço do produto no município). Essa informação será carregada automaticamente desde que o movimento esteja parametrizado para editar município por item.

Arquivos: RM.Edu.Consts.dll, RM.Edu.dll, RM.Edu.Financeiro.Form.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 1148659 / EDUCACIONAL01-1868]** Ajuste na exibição dos itens da modalidade de ensino no cadastro de turmas.

Arquivo: RM.Edu.Consts.dll

### Rotina: Project-1072300 Relações Empresariais - Cadastro Project-1072300

* **[Ticket: 1086452 / EDUCACIONAL01-1623]** Ajuste na validação de duplicidade do cadastro de empresas por tipo de documento.

Arquivo: RM.Edu.MatrizCurricular.Server.dll

## TOTVS Folha de Pagamento

### Rotina: Ajustar comportamento

* **[Ticket: FOPROTINAS01-959]** Para A Folha Analítica e o comparativo SEFIP o sistema passa a forçar a incidência de INSS dos eventos de código de cálculo 62 - Aviso Prévio e 99 - Diferença de Aviso Prévio Se: 1) A competência da Folha Analítica seja igual ou superior a informada no parâmetro "Verificar incidência CC 62 e CC 99 a partir" no Parametrizador \ Rescisão \ Aviso Prévio:". E 2) A data de demissão do funcionário esteja igual ou anterior à data informada no parâmetro "Forçar incidência de INSS no CC 62 E CC 69 até a data:" no Parametrizador \ Rescisão \ Aviso Prévio:". No comparativo SEFIP o parâmetro "Considera Valor de Aviso Prévio no SEFIP" influencia em considerar ou não o evento de CC 62 na base de INSS. Porém o parâmetro "Forçar incidência de INSS no CC 62 E CC 69 até a data:" tem prioridade.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

### Rotina: CAGED LAB 01 48

* **[Ticket: 803596 / FOPROTINAS01-299]** O CAGED passa a informar 5 espaços no registro B das colunas 32 a 36.

Arquivo: RM.Fop.Dominio.dll

### Rotina: Erro na Atualização do AAS e geração do relatório

* **[Ticket: FOPROTINAS01-950]** Correção no processo de Atualização de Bases AAS que não estava sendo executado.

Arquivo: RM.Fop.Rotinas.Data.dll

### Rotina: EVENTOS PROGRAMADOS LAB 01 139

* **[Ticket: 726970 / FOPCALCULO01-33]** Ajuste na rotina de gerar ficha de resitro automaticamente pelo sistema para considerar ficha de registro por coligada.

Arquivo: RM.Fop.Parametros.Data.dll

### Rotina: FERIAS CADASTRO FOP 34 538

* **[Ticket: 285529 / FOPCALCULO01-522]** O log de médias agora é mostrado após gerar o histórico de provisão.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: FUNCIONARIOS CADASTRO LAB 01 128

* **[Ticket: 788843 / FOPCALCULO01-239]** Ajuste na rotina de exibição de pendências demissionais para funcionário com afastamento por acidente de trabalho cadastrado e com data de retorno preenchida, contendo registro de estabilidade.

Arquivos: RM.Fop.Funcionario.Server.dll, RM.Fop.Funcionario.Data.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS RETROSPECTIVA CONTABIL GERENCIAL CTB 38 124

* **[Ticket: 1054290 / CONTROLADORIA01-320]** Ajuste na geração do relatório Retrospectiva para que os dados das Filiais/Departamentos sejam exibidos corretamente no subtítulo do mesmo.

Arquivos: RM.Ctb.Relatorios.Form.dll, RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: REQUISICOES GERAL RHU 36 508

* **[Ticket: 1112618 / RHU01-953]** Realizado ajuste na rotina de Acerto de Tipos de Requisição. Esta rotina é disparada ao logar no Delphi e cria os tipos de requisições no primeiro login em uma nova coligada.

Arquivo: RM.Rhu.Lib.Server.dll

### Rotina: REQUISICOES TRANSFERENCIA COM ALTERACAO DE DADOS FUNCIONAIS RHU 36 507

* **[Ticket: 934840 / RHU01-697]** Modificado a obrigatoriedade do campo de motivo de troca de função e seção somente se houver de fato uma troca de função ou seção.

Arquivos: Portal Corpore.Net

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO BAIXA CREDITOS DEVOLUCOES VINCULADOS FIN 189

* **[Ticket: 940216 / FINANCEIRO01-904]** Ajuste para gerar um novo boleto com o valor que permanece em aberto no lançamento após a baixa utilizando o processo "Baixar Créditos/Devoluções Vinculados".

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: LANCAMENTO CANCELAMENTO DE REMESSA FIN 193

* **[Ticket: 812461 / FINANCEIRO01-598]** Ajuste na validação para os lançamentos a receber do processo de "Cancelamento de Remessa" da visão de lançamentos, onde para os mesmos deve ser feito pela visão de boletos.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: LANCAMENTO MANUTENCAO ENVIAR EMAIL FIN 206

* **[Ticket: 495486 / FINANCEIRO01-359]** Ajustado processo de envio de email, para que os parâmetros dos relatórios delphi, possam ser informados no formulário de processo.

Arquivo: RM.Fin.Lan.Form.dll

### Rotina: SERVICO DE CONTABILIZACAO FIN 323

* **[Ticket: 866976 / FINANCEIRO01-751]** Ajuste no processo de formatação das variáveis da descrição da tabela opcional do complemento do histórico das partidas da contabilização.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: SESSAO DE CAIXA GERENCIAR CAIXAS ABRIR FIN 274

* **[Ticket: 922356 / FINANCEIRO01-867]** Ajuste na carga dos dados de conta caixa global na abertura de sessão.

Arquivo: RM.Fin.SessaoCaixa.Data.dll

## TOTVS Incorporação

### Rotina: ADITIVO PRORROGACAO DE VENCIMENTO IMB 49 783

* **[Ticket: 933348 / TINPAD001-425]** Melhoria no aditivo de alteração de valor em base não revitalizada com parcelas enviadas a banco.

Arquivo: RM.Imb.Aditivos.Server.dll

### Rotina: Aditivo antecipação de parcelas

* **[Ticket: 987053 / TINPAD001-509]** Melhoria no aditivo de antecipação de parcela em base não revitalizada.

Arquivo: RM.Imb.Aditivos.Form.dll

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 1128762 / TINPAD001-726]** Inclusão de Política de Segurança de Comissão de Vendedor para Revitalização

Arquivos: RM.Imb.dll, RM.Imb.Server.dll

### Rotina: DISTRATO OUTROS IMB 49 821

* **[Ticket: 905748 / TINPAD001-407]** Distrato (Cáculo de rescisão com Campo Complementar) - Melhoria no cálculo do valor de distrato, ao salvar o distrato e a fórmula busca o valor do campo complementar para fazer parte do total a ser pago na rescisão. O processo passa a atualizar o valor no salvar.

Arquivos: RM.Imb.Formula.dll, RM.Imb.Venda.Distrato.Data.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 1139600 / TINPAD001-732]** Melhoria no processo de calculo de seguro por empreendimento.

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

* **[Ticket: 1131401 / TINPAD001-720]** Melhoria no processo de calculo de seguro por empreendimento.

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: TABELAS ADICIONAIS IMB 49 861

* **[Ticket: 1130333 / TINPAD001-736]** Melhoria para o conversor de revitalização.

Arquivo: RM.Imb.Venda.Upg.Data.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: CONTROLE DE EXAMES AGENDA DE EXAMES SMT 36 001

* **[Ticket: 719521 / RHU01-938]** correção para permitir troca de valor em tabela dinamica em informações clínicas de um exame

Arquivo: RM.Smt.Lib.Form.dll

### Rotina: Exame Toxicológico - CAGED

* **[Ticket: RHU01-990]** Foi criado um parâmetro para ser informado o exame referente ao Exame Toxicológico. Foi criado também um serviço para ser utilizado pelo RMLabore para retornar os dados referentes ao exame toxicológico de uma determinada pessoa.

Arquivos: RM.Smt.Clinico.Intf.dll, RM.Smt.Parametros.Intf.dll, RM.Smt.Clinico.Data.dll, RM.Smt.Parametros.Form.dll

# 12.1.15.171

## TOTVS Business Connect

### Rotina: RM X FLUIG GED PARAMETROS DE CONFIGURACAO INT 00013

* **[Ticket: 867211 / MFRWBH-2222]** Melhoria no envio de arquivos para o GED ao qual a tabela referênciada possui uma coluna do tipo data

Arquivo: RM.Con.GED.Server.dll

## TOTVS Educacional

### Rotina: GERACAO DE ARQUIVOS ENADE EDU 50 226

* **[Ticket: 1147856 / EDUCACIONAL01-1865]** Ajuste na geração do arquivo do ENADE.

Arquivo: RM.Edu.Academico.Server.dll

## TOTVS Folha de Pagamento

### Rotina: Carga inicial

* **[Ticket: FOPROTINAS01-780]** Ajustes nas Rotinas da integração FieldServices Protheus

Arquivos: RM.Fop.Integracao.Services.dll, RM.Fop.TotvsMessage.Services.dll

### Rotina: Novidades do Caged - Inclusão Novos Campos

* **[Ticket: 323103 / FOPROTINAS01-828]** Contemplado a legislação do CAGED que entra em vigor a patir de 16 de agosto de 2017, referente a Portaria nº 116/2016 do que obriga o empregador que admitir ou desligar motoristas profissionais a declarar os campos: Código Exame Toxicológico, Data Exame Médico (Dia/Mês/Ano), CNPJ do Laboratório, UFCRM e NRCRM, relativos às informações do exame toxicológico de que trata o art. 24 da Lei nº 7.998, de 11 de janeiro 1990, os quais foram incluídos no layout do CadastroVide Especificação no TFS em $/RM/Documentos/Fop-Folha/CAGED/Exame Toxicológico

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Dominio.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Server.dll

* **[Ticket: 323103 / FOPROTINAS01-828]** Uso do servico do SSO para atender a legislação do exame toxicologico

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Utils.Server.dll, RM.Fop.Dominio.dll

## TOTVS Gestão Financeira

### Rotina: BAIXAS REALIZADAS ANEXO CHEQUES DEVOLVIDOS FIN 019

* **[Ticket: 680625 / FINANCEIRO01-10]** Ajuste na leitura dos dados de cheque para baixa com conta caixa de mútuo.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Incorporação

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 1064993 / TINPAD001-721]** Melhoria no aditivo de prorrogação de vencimento em base não revitalizada com parcelas enviadas a banco.

Arquivos: RM.Lib.Params.Wizard.xml, RM.Imb.Aditivos.Server.dll, RM.Imb.CalculoSeguro.Data.dll, RM.Imb.Empreendimento.Data.dll

# 12.1.15.172

## Outros

### Rotina: LOCAL DE PROVA DO CANDIDATO EDUPS 20 1072

* **[Ticket: 751803 / PORTALMOBILE01-217]** Acerto na listagem das áreas afertadas opcionais de um processo seletivo.

Arquivos: FrameHTML

## TOTVS Automação de Ponto

### Rotina: HORARIOS PTO 35 1180

* **[Ticket: 1007002 / PONTO01-716]** Ajustes realizados no cálculo para totalizar de forma correta as horas trabalhadas do funcionário, quando o mesmo possui horário flexível e não insere as batidas de refeição.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: PROCESSO DE CALCULO DE HORAS EXTRAS PTO 35 1238

* **[Ticket: 1034861 / PONTO01-767]** Ajustes realizados no processo de compensação utilizando o parâmetro "Considera por faixas de extras".

Arquivo: RM.Pto.Calculo.Service.dll

## TOTVS Business Connect

### Rotina: SERVICOS WEBSERVICES CON 12

* **[Ticket: 1141565 / MFRWBH-2220]** Melhoria na execução de processos via web service para que o comportamento seja idêntico ao da execução via RM.exe, em que é criada uma pasta com um arquivo separado para cada execução de processo e essa pasta é apagada após o termino da execução.

Arquivo: RM.Con.TotvsMessage.Server.dll

## TOTVS Educacional

### Rotina: PORTAL ALUNO MATRICULA ONLINE EDU 50 356

* **[Ticket: 877100 / PORTALMOBILE01-561]** Otimizado contrato financeiro da matrícula online, para permitir ao sistema substituir todas ocorrências das tags do contrato financeiro parametrizado no sistema.

Arquivo: App\_Web\_edumatriculaonlinecontratofinanceiro.aspx.f55b27f4.dll

### Rotina: PORTAL ALUNO REMATRICULA EDU 50 366

* **[Ticket: 1145894 / PORTALMOBILE01-1151]** Ajuste na rotina de rematrícula online quando o usuário é o responsável.

Arquivo: RM.Edu.Matricula.Data.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR EDU 50 389

* **[Ticket: 1156541 / EDUCACIONAL01-1896]** Alteração na rotina do censo para não limpar os campos de turma ao rodar o processo de preparação.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: RESPONSAVEIS DO ALUNO EDU 50 426

* **[Ticket: 883812 / EDUCACIONAL01-920]** Criação de tag na tela de copia de endereço para copiar ou não o email para o cliente/fornecedor

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.Aluno.Data.dll, RM.Edu.Aluno.Form.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIOS RESCISAO LAB 01 177

* **[Ticket: 990361 / FOPCALCULO01-479]** O cálculo do envelope agora verifica se o ano e mês de competência são menores ou iguais ao ano e mês informados no parâmetro

Arquivo: RM.Fop.Envelope.Data.dll

### Rotina: Novidades do Caged - Inclusão Novos Campos

* **[Ticket: 1084991 / FOPROTINAS01-828]** Contemplado código defensivo para só considerar os campos novos para o CAGED no Registro C, a saber: Código Exame Toxicológico, Data Exame Médico (Dia/Mês/Ano), CNPJ do Laboratório, UFCRM e NRCRM. Quando existir o campo VEXAMESPRONT.CODLAUDOEXAME

Arquivos: RM.Fop.Calc.Interfaces.dll, RM.Fop.Dominio.dll, RM.Fop.Relatorios.Server.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS RAZAO CTB 38 114

* **[Ticket: 680742 / CONTROLADORIA01-189]** Foi feito uma melhoria no relatório Razão para que em casos onde o código reduzido foi cadastrado e no código existe algum espaço gerado pela tecla TAB não cause o espaçamento não calculado, o que gera a quebra de linha e consequentemente a quebra errada de página.

Arquivo: RM.Ctb.Relatorios.Service.dll

* **[Ticket: 988272 / CONTROLADORIA01-273]** O relatório Razão Contábil foi alterado para que o Saldo Anterior das contas seja exibido no subtítulo seja apresentado sem cortes quando é marcado nos parâmetros de sistema a opção (5) para imprimir saldo credor entre parênteses.

Arquivo: RM.Ctb.Relatorios.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CONCLUIR PEDIDO MOV 008

* **[Ticket: 940396 / MATFATCMPCRM01-587]** Ajustamos a rotina responsável por selecionar os itens aptos a serem concluídos.

Arquivos: RM.Mov.Processos.Form.dll, RM.Mov.Processos.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: Check-in das Modificações de AD para o BDMG

* **[Ticket: RHU01-1077]** Modificações para notas aparacerem quando há uma troca de seção.

Arquivo: RM.Rhu.AvalDesemp.Data.dll

## TOTVS Gestão Fiscal

### Rotina: Revisão do Layout da NFS-e TOTVS Colaboração 2.00

* **[Ticket: FISCAL01-950]** Implementação das novas tags para o envio de NFS-e integrada com TOTVS Colaboração 2.0.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

## TOTVS Incorporação

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 1064993 / TINPAD001-721]** Melhoria no aditivo de prorrogação de vencimento em base não revitalizada com parcelas enviadas a banco.

Arquivo: RM.Imb.Empreendimento.Data.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 1162753 / TINPAD001-796]** Melhoria no processo de geração de plano de financiamento.

Arquivo: RM.Imb.Facade.dll

## TOTVS Processo Seletivo

### Rotina: LOCAL DE PROVA DO CANDIDATO EDUPS 20 1072

* **[Ticket: 751803 / PORTALMOBILE01-217]** Melhoria no portal a fim de manter um mesmo comportamento do portal anigo, no qual as opções obrigatórias para a realização da seleção da área de interesse ofertada sejam selecionadas automaticamente quando houver somente uma opção.

Arquivos: FrameHTML

## TOTVS Segurança e Medicina do Trabalho

### Rotina: Exame Toxicológico - CAGED

* **[Ticket: RHU01-990]** Foi criado um parâmetro para ser informado o exame referente ao Exame Toxicológico. Foi criado também um serviço para ser utilizado pelo RMLabore para retornar os dados referentes ao exame toxicológico de uma determinada pessoa.

Arquivos: RM.Smt.Pessoa.Intf.dll, RM.Smt.Clinico.Intf.dll, RM.Smt.Lib.Data.dll, RM.Smt.Lib.Form.dll, RM.Smt.Pessoa.Data.dll, RM.Smt.Parametros.Data.dll, RM.Smt.Parametros.Form.dll, RM.Smt.Clinico.Data.dll, RM.Smt.Clinico.Form.dll, RM.Smt.Lib.Intf.dll, RM.Smt.Parametros.Intf.dll

# 12.1.15.173

## TOTVS Business Connect

### Rotina: FRT CANCELAR ORDEM DE SERVICO PNEUS FRT 004

* **[Ticket: 1140341 / MATESTCNTFTOF01-462]** Ajuste no SourceCode de Cancelamento de Solicitações (CancelRequest) para tratar as duas opções referentes ao parâmetro do Protheus MV\_NGMNTAS - Aglutina Solicitação de Armazém para mesma Ordem de Serviço.

Arquivo: RM.Con.ConfiguraIntegracao.TotvsManutencaoAtivos.dll

## TOTVS Folha de Pagamento

### Rotina: ALTERACOES GLOBAIS ALTERACAO CAMPOS DO CADASTRO LAB 01 1

* **[Ticket: 824727 / FOPCALCULO01-248]** Atualização para inserir branco no histórico de endereço quando executar o processo de Atualizar Campos do Cadastro.

Arquivo: RM.Fop.Rotinas.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: FUNCIONARIOS RHU 36 035

* **[Ticket: 1072365 / RHU01-995]** Corrigido erro ao entrar na avaliação de desempenho no portal.

Arquivo: RM.Rhu.AvalDesemp.Data.dll

## TOTVS Gestão Financeira

### Rotina: CARTAO DE CREDITO TRANSACOES FIN 068

* **[Ticket: 1149895 / FINANCEIRO01-1632]** Disponibilizado permissão para permitir baixar lançamento com transação de cartão de crédito pendente

Arquivos: RM.Fin.Lib.dll, RM.Fin.dll, RM.Fin.Lan.Service.dll, RM.Fin.Server.dll

## TOTVS Gestão Fiscal

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 666031 / FISCAL01-872]** Implementada melhoria na geração da NF-e para que a Tag IEST seja inserida no XML da nota apenas para CFOP's de Substituição tributária e flag "Situação da Retenção ICMS S.T. " igual a "Substituto Tributário"

Arquivos: RM.Fis.Utils.Intf.dll, RM.Fis.NFe.Service.dll

## TOTVS Gestão Patrimonial

### Rotina: INTEGRACOES INTEGRACAO OCORRENCIAS PENDENTES PAT 37 107

* **[Ticket: CONTROLADORIA01-339]** O menu Integração de Ocorrências foi removido do módulo de gestão patrimonial.

Arquivo: RM.Pat.Server.dll

# 12.1.15.174

## TOTVS Educacional

### Rotina: Project-1104971 Mudança de status não esta criticando choque de horario Project-1104971

* **[Ticket: 1128496 / EDUCACIONAL01-1774]** Ajuste no processo de alteração de situação de matrícula da disciplina para efetuar validação de choque de horário ao executar o processo, sendo que será validado o choque para o Ensino Superior se a situação antiga não for "É uma disciplina em curso" e a situação nova for "É uma disciplina em curso" e para o Ensino Básico se a situação antiga não for "Conta como aluno matriculado na turma" e a situação nova for "Conta como aluno matriculado na turma". Os demais casos não será feita validação de choque de horário.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Form.dll, RM.Edu.Matricula.Server.dll, RM.Edu.Matricula.Data.dll

### Rotina: TURMAS EDU 50 453

* **[Ticket: 1111341 / EDUCACIONAL01-1905]** No processo de mudança de turma, apresentava mensagem de erro “Chave duplicada” ao gravar o Log da Digitação de Notas/Freqüência (tabela SLOGNOTA). Somente ocorria se marcasse a opção "Copiar os registros de notas para a turma de destino" e existisse fórmula para cálculo de nota.

Arquivos: RM.Edu.Utils.Intf.dll, RM.Edu.NotaFalta.Server.dll, RM.Edu.Matricula.Server.dll

## TOTVS Folha de Pagamento

### Rotina: Novidades do Caged - Inclusão Novos Campos

* **[Ticket: 323103 / FOPROTINAS01-828]** Mensagem sobre a explicação de novos campos ao entrar no CAGED e inclusão do modulo de consulta médica quem não tem integração com o Vitae.

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Funcionario.Intf.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Funcionario.Data.dll, RM.Fop.Funcionario.Form.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 923217 / CONTROLADORIA01-251]** Para possibilitar a inclusão do arquivo a aba J801 passou a ser exibida durante a realização da ECD substitutiva.

Arquivo: RM.Ctb.Sped.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: FLUIG APROVACAO FATURAMENTO MOVIMENTO FLG 004

* **[Ticket: 990000 / MATESTCNTFTOF01-476]** Alterado a forma como o sistema valida o cancelamento de WorkFlows no Fluig. Se o mesmo estiver aprovado ou cancelado, independente da mensagem de erro retornada, será possível alterar o movimento e será criado um novo WorkFlow no Fluig.

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão Financeira

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 1041887 / FINANCEIRO01-1364]** Otimizado processo de retorno bancário quanto ao valores do arquivo Layout

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS ESTADUAIS LI 01 0027

* **[Ticket: 1173713 / FISCAL01-1057]** Foram criados dois SubTipos no cadastro de Lançamentos de Outros Débitos/Créditos: “Segregação do Crédito Decorrente do Pagamento Antecipado” e “Segregação de outros créditos permitidos para compensar com o débito”. Esses SubTipos estarão disponíveis apenas quando o Tripo escolhido na tela for “Débito”.Foram realizadas alterações no Encerramento do Período de Apuração para que sejam considerados os Lançamentos de Outros Débitos/Créditos com os SubTipos “Segregação do Crédito Decorrente do Pagamento Antecipado” e “Segregação de outros créditos permitidos para compensar com o débito”.

Arquivos: RM.Fis.Lib.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.LancFiscal.Form.dll

## TOTVS Gestão Patrimonial

### Rotina: REVISOES CNTR020

* **[Ticket: CONTROLADORIA01-338]** O processo reponsável por desfazer a revisão de vida útil foi alterado para que seja possível executá-lo com sucesso.

Arquivo: RM.Pat.PatrimonioMoeda.Service.dll

# 12.1.15.175

## Outros

* **[Ticket: Alterações Gerais]** Inclusão Script Especifico CAGED 2017

Arquivos: ExecSql.TOTVSBancodeDados.CAGED.2017.ORA.TotvsScript, ExecSql.TOTVSBancodeDados.CAGED.2017.SQL.Leia-me.txt, ExecSql.TOTVSBancodeDados.CAGED.2017.SQL.TotvsScript, ExecSql.TOTVSBancodeDados.CAGED.2017.ORA.Leia-me.txt

## TOTVS Educacional

### Rotina: GERACAO DE MOVIMENTO EDU 50 229

* **[Ticket: 1118542 / DEDUINTEGRACOES-99]** Ajuste no processo de cancelamento de lançamento financeiro quando temos movimento regime de caixa gerado, pois neste caso não pode permitir o cancelamento.

Arquivo: RM.Edu.Services.Server.dll

## TOTVS Folha de Pagamento

### Rotina: EVENTOS EVENTOS RELACIONADOS REPROGRAMACAO SALARIAL LAB 01 86

* **[Ticket: 801973 / FOPCALCULO01-707]** O numero do salário é gravado e gerado de forma que não gere o erro de "Chapa Dupla" quando feio o Ajuste do Histórico Salarial

Arquivo: RM.Fop.Funcionario.Data.dll

## TOTVS Framework

### Rotina: SMT EMPRESTIMO FORNECIMENTO AUTOMATICO DE EPIS SMT 36 013

* **[Ticket: 467787 / RHU01-966]** Criado mensagem para informar o usuário no caso de um fornecimento de EPI onde o mesmo EPI tem que ser devolvido na mesma operação e o local de devolução diferir do local de empréstimo.

Arquivo: RM.Smt.EPI.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: TOTVS COLAB - INCLUSÃO MOVIMENTO A PARTIR DE XML CLB007

* **[Ticket: MATFATCMPCRM01-871]** Ajuste no processo de "Inclusão de movimento atraves de XML - TOTVS colaboração", agora, os tributos serão carregados corretamente

Arquivo: RM.Mov.Movimento.Form.dll

## TOTVS Gestão Fiscal

### Rotina: Revisão do Layout da NFS-e TOTVS Colaboração 2.00

* **[Ticket: FISCAL01-950]** Reformulação do envio da NFS-e integrada com TOTVS Colaboração 2.0. Implementação das novas tags para o envio de NFS-e integrada com TOTVS Colaboração 2.0.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: FISCAL01-950]** Revisão do Layout da NFS-e TOTVS Colaboração 2.00 Codificação parte 3 Grupos Valores, Fatura, Dedução, Constrciv, Construção,localEntrega

Arquivo: RM.Fis.RotinasFiscais.Intf.dll

* **[Ticket: FISCAL01-950]** Revisão do Layout da NFS-e TOTVS Colaboração 2.00 Codificação parte 3 Grupos Valores, Fatura, Dedução, Constrciv, Construção,localEntrega

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

# 12.1.15.176

## TOTVS Automação de Ponto

### Rotina: PARAMETRIZADOR SINDICATO PTO 35 1249

* **[Ticket: 1018268 / PONTO01-885]** Alteração da validação de horas para permitir o cadastramento de "24:00"

Arquivo: RM.Pto.Parametros.Data.dll

* **[Ticket: 1018268 / PONTO01-885]** Alteração da validação de horas para permitir o cadastramento de "24:00"

Arquivo: RM.Pto.Parametros.Data.dll

## TOTVS Educacional

### Rotina: EDUCAMOBILE ALUNO AVISOS EDU 51018

* **[Ticket: 1180053 / PORTALMOBILE01-1223]** Melhoria de performance na validação de inadimplência do aluno.

Arquivo: RM.Edu.Services.Server.dll

### Rotina: ENADE - Arquivo de concluintes

* **[Ticket: EDUCACIONAL01-1880]** Implementação do leiaute de concluintes do ENADE 2017

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: RESPONSAVEIS DO ALUNO EDU 50 426

* **[Ticket: 883812 / EDUCACIONAL01-920]** Foi alterado o comportamento da cópia de endereço agora possibilitando a opção de copiar e-mail para cliente/fornecedor e pessoa.

Arquivo: RM.Edu.Aluno.Form.dll

## TOTVS Folha de Pagamento

### Rotina: PARAMETROS LOCAIS LAB 01 31

* **[Ticket: 569425 / FOPROTINAS01-664]** Removida referência a action que não existe mais, o que ocasionava a solicitação da atualização.

Arquivo: RM.Fop.Secao.Form.dll

## TOTVS Framework

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 807686 / TINPAD001-962]** Melhoria na atividade Ler Parâmetros do Processo

Arquivo: RM.Lib.Workflow.Activities.dll

### Rotina: FERIAS DIFERENCA FOP 34 405

* **[Ticket: 1153377 / FOPCALCULO01-721]** Tratamento para verificar a existência de evento com CC 88 do tipo Desconto, para acumular as diferenças dos descontos de férias.

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

## TOTVS Gestão Contábil

### Rotina: ESCRITURACAO CONTABIL LOTES CTB 38 86

* **[Ticket: 932163 / CONTROLADORIA01-234]** O cadastro de evento contábil foi modificado para que ao alterar alguma informação no item do evento e avançar para o próximo item (através da seta direcional), o sistema envie avisos pertinentes para que as alterações possam ser salvas ou canceladas.

Arquivo: RM.Ctb.EventosContabeis.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: ITEM DE MOVIMENTO MOV 035

* **[Ticket: 899911 / MATFATCMPCRM01-735]** Melhorias na rotina responsável por expandir estrutura no item de movimento.

Arquivos: RM.Mov.Movimento.Intf.dll, RM.Mov.Movimento.Data.dll, RM.Mov.Movimento.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: REQUISICOES AUMENTO DE QUADRO RHU 36 095

* **[Ticket: 1005046 / RHU01-1022]** Criado validação de nulidade para evitar erro de referência de objeto.

Arquivo: App\_Web\_rhurequsercontrol.ascx.3e26f2e8.dll

### Rotina: REQUISICOES TRANSFERENCIA RHU 36 506

* **[Ticket: 1033403 / RHU01-1021]** correção para que uma requisição de transferência possa ser feita com o campo Data Prevista desabilitada para edição e visualização.

Arquivos: Portal Corpore.Net

## TOTVS Gestão Financeira

### Rotina: SERVICO DE ATUALIZACAO DE CLIENTE FORNECEDOR FIN 314

* **[Ticket: 1110938 / FINANCEIRO01-1440]** Ajustado processo 'Vincular/Desvincular Cli/For' para poder atender a integração com Protheus.

Arquivo: RM.Fin.CliFor.Intf.dll

### Rotina: SESSAO DE CAIXA BAIXA FIN 269

* **[Ticket: 1182401 / FINANCEIRO01-1691]** Otimização no processo de baixa com mais de um lançamento agrupado com a forma de pagamento cheque.

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 1182401 / FINANCEIRO01-1691]** Otimização no processo de baixa com mais de um lançamento agrupado com a forma de pagamento cheque.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: Revisão do Layout da NFS-e TOTVS Colaboração 2.00

* **[Ticket: FISCAL01-950]** Reformulação do envio da NFS-e integrada com TOTVS Colaboração 2.0. Implementação das novas tags para o envio de NFS-e integrada com TOTVS Colaboração 2.0.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Incorporação

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 807686 / TINPAD001-962]** Ajuste no dataSet de venda para funcionar corretamente com formulas visuais.

Arquivos: RM.Imb.Contratos.Intf.dll, RM.Imb.Contratos.Server.dll

# 12.1.15.177

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB ABONAR ATRASOS E FALTAS PTO 35 1257

* **[Ticket: 1177517 / PONTO01-929]** Ajuste realizado para que as solicitações de abonos não sejam duplicadas na visão quando está parametrizado para "Considerar Número de horas para Abono"Parâmetrizador > Cálculo > Parâmetros de cálculo > Considerar abonos por intervalo (Desmarcado)

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Construção e Projetos

### Rotina: BACKUP RESTAURACAO DE PROJETOS PRJ 33 781

* **[Ticket: 1166254 / TOPORCAPLAN001-1000]** Ajuste no restore do projeto para não duplicar cliente/Fornecedor

Arquivos: RM.Prj.Facade.Intf.dll, RM.Prj.BackupRestore.Data.dll

## TOTVS Educacional

### Rotina: Concessão da mesma bolsa futura com percentuais e períodos diferentes

* **[Ticket: DEDUINTEGRACOES-34]** Sistema passou a permitir a inclusão de mais de uma concessão de bolsa futura para uma mesma bolsa, mesmo aluno em períodos de datas (data inicial e data final) diferentes. Para isso, foram alteradas aschaves primárias das tabelas relacionadas com concessão de bolsa, além de alterações em datasets, dataservers, serviços e actions.- Criado o campo IDCONCESSAOBOLSA que passa a compor a chave primária das tabelas relacionadas.- Criado o AUTOINC para IDCONCESSAOBOLSA- Proibição de períodos coincidentes na inclusão de uma concessão para uma mesma bolsa e mesmo aluno no cadastro de concessão de bolsas futuras.- Proibição de períodos coincidentes na inclusão de uma concessão para uma mesma bolsa e mesmo aluno no assistente de concessão de bolsas futuras.- Alteração nas actions de concessões e seus anexos- Reorganização dos datasets de concessão de bolsa, serviços de concessão de bolsas, habilitações de concessão de bolsa (Ensino Básico e Ensino Superior)- Foi alterado também o texto do flag "Inserir bolsa automaticamente" do cadastro de concessão e assistente de concessões de bolsas para "Concessão ativa" a fim de melhorar a usabilidade.- Ajuste no comportamento do ícone exibido ao término do processo do assistente de Concessão de bolsas futuras.

Arquivos: RM.Edu.Utils.Intf.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Interfaces.Intf.dll, RM.Edu.Utils.Server.dll, RM.Edu.Financeiro.Intf.dll, RM.Edu.Services.Server.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Financeiro.Server.dll, RM.Edu.Financeiro.Data.dll

* **[Ticket: DEDUINTEGRACOES-34]** Filtro de matrizes aplicadas vinculadas a matrículas dos alunos selecionados para concessão.Ajuste da chave de campos complementares de concessões de bolsas a fim de considerar o código defensivo ou nova chave (12.1.18).

Arquivos: RM.Edu.Financeiro.Form.dll, RM.Edu.Server.dll

* **[Ticket: DEDUINTEGRACOES-34]** Ajuste na inclusão automática de bolsas nos contratos quando já existe a mesma bolsa nesse contrato e uma nova concessão deve ser inserida em um período diferente.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: EDUCAMOBILE ALUNO AVISOS EDU 51018

* **[Ticket: 1180053 / PORTALMOBILE01-1223]** Melhoria de performance na validação de inadimplência do aluno.

Arquivo: RM.Edu.Services.Server.dll

### Rotina: Erro Exportacao\_de\_usuario\_lookup\_periodo\_letivo

* **[Ticket: EDUCACIONAL01-2031]** Foi corrigido uma validação do campo.

Arquivo: RM.Edu.Lib.Intf.dll

### Rotina: PREPARACAO DO ARQUIVO PARA O CENSO ESCOLAR

* **[Ticket: EDUCACIONAL01-180]** Alteração na rotina do Educacenso para não gerar muitos argumentos na consulta, devido ao limite existente no Oracle.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: TURMAS EDU 50 453

* **[Ticket: 1111341 / EDUCACIONAL01-1905]** Ajustes ao salvar log de notas ao mudar turma que possui fórmula na etapa.

Arquivos: RM.Edu.NotaFalta.Server.dll, RM.Edu.Formula.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIOS PERIODO AQUISITIVO LAB 01 172

* **[Ticket: 1146405 / FOPCALCULO01-742]** O afastamento não será considerado em um período aquisitivo se o inicio e término do afastamento não se encontrarem dentro do período de concessão atual.

Arquivo: RM.Fop.FuFerias.Data.dll

### Rotina: GERACAO DE MOVIMENTO LAB 01 114

* **[Ticket: 432017 / FOPCALCULO01-395]** Ajuste na Restituição de INSS de múltiplos vínculos quando existe INSS de Outro Emprego junto com Férias no mês.

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

### Rotina: INFORME DE RENDIMENTOS FOP 34 431

* **[Ticket: 834004 / FOPROTINAS01-449]** Criado o parâmetro "Imprimir Funcionários sem Movimentação(Informe de Rendimentos)", caso ele esteja marcado o sistema deve gerar o Informe de Rendimentos com todos os funcionários, caso esse parâmetro esteja desmarcado o sistema deve gerar o Informe de Rendimentos apenas para funcionários com movimentação.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Form.dll

## TOTVS Gestão Contábil

### Rotina: GESTAO RM CONECTOR CTB 39 005

* **[Ticket: 1042109 / CONTROLADORIA01-318]** O conceito de importação de lançamentos foi alterado para que o sistema não consista, para coligadas que não acessam contas globais, o reduzido e o código das contas existentes na coligada global.

Arquivo: RM.Ctb.Lan.Data.dll

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 1159719 / CONTROLADORIA01-364]** O campo Conta Anterior passou a permitir a inclusão de pontos, tornando possível informar a máscara contábil.

Arquivo: RM.Ctb.Sped.Form.dll

* **[Ticket: 923217 / CONTROLADORIA01-251]** O processo de geração do SPED Contábil foi modificado para que a aba J801 (Termo de verificação para fins de substituição da ECD) seja exibida para todos os tipos de escrituração quando a opção "Indicador de Finalidade da Escrituração" for Substituta.

Arquivos: RM.Ctb.Sped.Form.dll, RM.Ctb.Sped.Service.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: TOTVS COLAB INCLUSAO MOVIMENTO A PARTIR DE XML CLB 007

* **[Ticket: 531537 / MATFATCMPCRM01-123]** TOTVS Colaboração - Melhoria no processo de Inclusão automática de CT-e.

Arquivo: RM.Mov.Integracoes.Service.dll

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA ENCERRAMENTO DE PERIODO FIN 010

* **[Ticket: 978139 / FINANCEIRO01-1061]** Corrige cálculo saldo real de aplicação financeira, quando aplicação, resgate parcial e encerramento ocorre no mesmo dia.

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

### Rotina: INTEGRACAO FINANCEIRA GERACAO DE LANCAMENTOS IMB 49 836

* **[Ticket: 581584 / TINPAD001-975]** Melhoria no utilitários de lançamentos imobiliários para tratamento do campo valor capitalização e multa.

Arquivo: RM.Fin.Conversor.Service.dll

## TOTVS Gestão Fiscal

### Rotina: CT-e OS - Criação de campos na DFILIAL

* **[Ticket: FISCAL01-957]** Foi implementado os campos "Número do Registro Estadual" e "Termo de Autorização de Fretamento" no Anexo Dados Fiscais do Cadastro da Filial.

Arquivos: RM.Fis.Filial.Intf.dll, RM.Fis.Filial.Form.dll, RM.Fis.Filial.Data.dll

### Rotina: NFS E ENVIO TOTVS COLABORACAO NF 01 0037

* **[Ticket: 1104076 / FISCAL01-962]** Reformulação do envio da NFS-e integrada com TOTVS Colaboração 2.0. Implementação das novas tags para o envio de NFS-e integrada com TOTVS Colaboração 2.0.

Arquivos: RM.Fis.RotinasFiscais.Form.dll, RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Hospitalar

### Rotina: REGISTRO DE INFORMACOES DE CIRURGIA SAU 47 1123

* **[Ticket: 1155333 / MSAU-12372]** Ao acessar o "Registro de Informações Cirúrgicas" e for adicionar um novo "Agente Anestésico" com quantidade
  superior a 100 o sistema voltava a quantidade para 100.O sistema foi ajustado para o componente receber o valor até 1000.15Servidor: POAD040100308\SQLSERVER14SGBD: MSSQL (ODBC)Instância: BURITI16Servidor: poad033SGBD: MSSQL (ODBC)Instância: rmsaude17Servidor: poad033SGBD: MSSQL (ODBC)Instância: rmsaude18Servidor: poad033SGBD: MSSQL (ODBC)Instância: rmsaude

Arquivo: RM.Sau.RegistroInfCirurgia.Form.dll

## TOTVS Incorporação

### Rotina: Desenvolvimento dos parâmetros do Reajuste

* **[Ticket: TINREV001-40]** Melhoria para ficha financeira, apenas para o projeto de revitalização do TIN

Arquivo: RM.Imb.Relatorio.Data.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 951698 / TINPAD001-797]** Melhoria da distribuição do resíduo com a nova engine em base não revitalizada.

Arquivos: RM.Imb.Contratos.IServer.dll, RM.Imb.Reajuste.Calculo.Residuo.dll, RM.Imb.Reajuste.Server.dll

# 12.1.15.178

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO OCORRENCIAS PTO 35 1193

* **[Ticket: 1153458 / PONTO01-905]** Ajustes realizados na compensação diária com a utilização do parâmetro "Considera percentual".

Arquivo: RM.Pto.Calculo.Service.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: BI TAXA GLOBAL POR SITIO PRIMARIO SECUNDARIO SAUIH 55 617

* **[Ticket: 1119205 / MSAU-12356]** Foi alterado o filtro no BI de Taxa Global por Unidade / Especialidade para não exibir a mensagem do campo CODSITIOPRIMARIO.

Arquivo: RM.SauIH.Estatisticos.Form.dll

### Rotina: PROCESSOS SAUIH 55 658

* **[Ticket: 888175 / MSAU-13033]** Alterado o sistema parar ao executar o compilador de antibiograma compilar corretamente os germes e antibiogramas e excluir os germes com antibiograma idênticos para o mesmo dia.

Arquivo: RM.SauIH.Processos.Data.dll

* **[Ticket: 888175 / MSAU-13033]** Alterado o sistema parar ao executar o compilador de antibiograma compilar corretamente os germes e antibiogramas e excluir os germes com antibiograma idênticos para o mesmo dia.

Arquivo: RM.SauIH.Processos.Data.dll

## TOTVS Educacional

### Rotina: Concessão da mesma bolsa futura com percentuais e períodos diferentes

* **[Ticket: DEDUINTEGRACOES-34]** Ajuste na inclusão automática de bolsas nos contratos quando já existe a mesma bolsa nesse contrato e uma nova concessão deve ser inserida em um período diferente.

Arquivo: RM.Edu.Financeiro.Form.dll

### Rotina: EDUCAMOBILE ALUNO AGENDA EDU 51016

* **[Ticket: 753613 / PORTALMOBILE01-254]** Ajuste no contexto do EducaMobile evitando duplicidade de contexto ao acessar o sistema com responsáveis.

Arquivo: RM.Edu.Contexto.Data.dll

### Rotina: MATRICULA EM TURMA MISTA EDU 50 296

* **[Ticket: 1160414 / EDUCACIONAL01-1934]** Acerto no processo de enturmação, a fim de evitar que um mesmo aluno seja matriculado em duas duas turmas/disciplinas de uma mesma disciplina no mesmo periodo letivo.

Arquivo: RM.Edu.Matricula.Server.dll

## TOTVS Folha de Pagamento

### Rotina: CAGED - Acesso sem utilizar o SSO

* **[Ticket: FOPROTINAS01-1018]** Criação de botões para acesso aos cadastros de Profissional de Saúde, Exames, Entidades (Laboratórios), Convênios e Parametrizador do Smt. Esses botões serão habilitados para clientes que não possuem integração com o RM Vitae. Tais cadastros são necessários para contemplar mudanças ocorridas no leiaute do CAGED, que exige preenchimento de novos campos referentes ao exame toxicológico admissional/demissional para motoristas com CBO especifícos.

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Parametros.Intf.dll, RM.Fop.Server.dll, RM.Fop.Utils.Server.dll, RM.FopFolha.dll, RM.Fop.Parametros.Form.dll

### Rotina: Criar serviço para atualização de situação de funcionário

* **[Ticket: FOPROTINAS01-999]** Criação de serviço para atualizar a situação de funcionário retornando de afastamento.

Arquivos: RM.Fop.Lib.Intf.dll, RM.Fop.Lib.Data.dll

### Rotina: FUNCIONARIOS PERIODO AQUISITIVO LAB 01 172

* **[Ticket: 1146405 / FOPCALCULO01-742]** O afastamento não será considerado na data limite de gozo se o afastamento não se encontrar dentro do período aquisitivo atual.

Arquivo: RM.Fop.FuFerias.Data.dll

### Rotina: Réplica do Serviço criado na issue FOPROTINAS01-886

* **[Ticket: FOPROTINAS01-1205]** Criação de serviço que retorna clausula where para pegar as seções das quais um funcionário é chefe

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: Replica Issue - FOPCALCULO01-709

* **[Ticket: FOPCALCULO01-847]** Ajustado processo de Atualizar Saldo de Férias, para atualizar o saldo do período aquisitivo com o saldo do período vencido.

Arquivos: RM.Fop.Calc.Calculos.dll, RM.Fop.FuFerias.Data.dll

## TOTVS Gestão Contábil

### Rotina: ESCRITURACAO CONTABIL FISCAL CTB 38 165

* **[Ticket: 1210228 / CONTROLADORIA01-406]** Melhoria no processo de importação do arquivo da ECD (ano anterior) "Identificar Contas do Plano de Contas Anteriores Automaticamente" para geração do registro I157 de forma que a importação não valide somente as contas que não existem no plano de contas atual e no último período de saldo permitindo que contas que tiveram uma linha do registro I155 (Saldo Periódico) em um período qualquer sejam importadas também.

Arquivo: RM.Ctb.Sped.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: REQUISICOES SUBSTITUICAO RHU 36 504

* **[Ticket: 476871 / RHU01-246]** correção ao enviar e-mail após responder avaliação de desempenho

Arquivo: RM.Rhu.AvalDesemp.Server.dll

## TOTVS Gestão Fiscal

### Rotina: NFS - Implementação do municipio de Uberaba - MG.

* **[Ticket: 1102675 / FISCAL01-889]** Reformulação do envio da NFS-e integrada com TOTVS Colaboração 2.0. Implementação das novas tags para o envio de NFS-e integrada com TOTVS Colaboração 2.0.Retirado as validações integradas com o Mashups, Totvs Colaboração 2.0 não terá trava, desde que a NeoGrid garanta que o envio de NFS-e para o municipio esteja tudo ok.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## TOTVS Gestão Patrimonial

### Rotina: RELATORIOS FICHA DE IMOBILIZADO PAT 37 90

* **[Ticket: 671981 / CONTROLADORIA01-179]** Atualização no cálculo da depreciação de transferência monetária a ser efetuada no patrimônio destino pela taxa de depreciação atual.

Arquivo: RM.Pat.Calculo.Service.dll

## TOTVS Incorporação

### Rotina: ADITIVO ALTERACAO DE VENCIMENTO IMB 49 780

* **[Ticket: 1219394 / TINPAD001-984]** Ajuste para contabilização com rateio de contas gerencias de diferença de aditivo

Arquivo: RM.Imb.Facade.dll

### Rotina: Desenvolvimento dos parâmetros do Reajuste

* **[Ticket: TINREV001-40]** Melhoria para o processo de geração de plano de financimento, apenas clientes revitalizados.

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: Separar Nome e Sobrenome

* **[Ticket: TINPAD001-516]** Ajuste na validação de venda nula, pois gerava erro ao cancelar baixa de aluguel.

Arquivo: RM.Imb.Venda.Financeiro.Server.dll

## TOTVS Processo Seletivo

### Rotina: PORTAL ALUNO MATRICULA ONLINE EDU 50 356

* **[Ticket: 1208122 / PORTALMOBILE01-1328]** Foi realizado um ajuste no preenchimento da Área Ofertada na parte server, do processo seletivo antigo.Isso impedia que o ComboBox de Área Ofertada fosse preenchido no portal.

Arquivo: RM.EduPS.Cadastros.Data.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: CADASTROS TABELAS AUXILIARES TIPOS DE ATESTADOS RHU 36 067

* **[Ticket: 713703 / RHU01-919]** Realizado ajuste em atestados para que ao inserir a data fim em um atestado para o mesmo mês de competência do Labore a situação do funcionário mude para A (ativo).

Arquivos: RM.Smt.Facade.dll, RM.Smt.Pessoa.Intf.dll, RM.Smt.Pessoa.Data.dll, RM.Smt.Pessoa.Form.dll

# 12.1.15.179

## TOTVS Folha de Pagamento

### Rotina: CAGED - Acesso sem utilizar o SSO

* **[Ticket: FOPROTINAS01-1018]** Inclusão da anotação OperationContract que faltava.

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Utils.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: IMPORTACAO DE MOVIMENTO MOV 039

* **[Ticket: 995919 / MATFATCMPCRM01-1016]** Foi acrescentado o campo produto predominante nos seguintes layouts do gerador de saídas:Layout Movimento - V1.TotvsGenLayout Movimento - V2.TotvsGenLayout Movimento - V3.TotvsGenE também nos seguintes conceitos:Movimento - V1.conceptMovimento - V2.conceptMovimento - V3.concept

Arquivo: RM.Mov.Movimento.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NFS E ENVIO NF 01 0052

* **[Ticket: 1113663 / FISCAL01-973]** Geração da tag DocTomadorEstrangeiro para a NFS-e de Campinas-SP.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

## TOTVS Incorporação

### Rotina: Desenvolvimento dos parâmetros do Reajuste

* **[Ticket: TINREV001-40]** Melhoria versão revitalizada.

Arquivo: RM.Imb.Venda.Lib.Intf.dll

# 12.1.15.180

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB ESPELHO DO CARTAO PTO 35 1250

* **[Ticket: 1238867 / PONTO01-1038]** Ajustes realizados no processo de visualização de espelho, ajustando a questão de visualização de funcionários por chefes de diferentes coligadas

Arquivo: App\_Web\_ptoespelhocartaowebform.ascx.1306bbfe.dll

### Rotina: PROCESSO DE CALCULO DE ABONO PTO 35 1300

* **[Ticket: 1231644 / PONTO01-1014]** Ajustes realizados no processo de exclusão de abono para corrigir a mensagem de erro que era apresentada.

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS MEDICAO PRJ 33 941

* **[Ticket: 1179736 / TOPEXECONTROL01-604]** Contrato de InsumoAnalise na validações, em consumos que geram um valor superior ao contratado. Verificado o valor apresentado no campo Saldo disponível.

Arquivos: RM.Prj.Contrato.Data.dll, RM.Prj.Contrato.Form.dll

## TOTVS Educacional

### Rotina: PORTAL ALUNO MATRICULA ONLINE EDU 50 356

* **[Ticket: 1241378 / PORTALMOBILE01-1388]** Ajuste no processo de matrícula online do portal do aluno, evitando que o processo seja paralizado se ao tentar regerar o lançamento o mesmo esteja baixado parcialmente ou remetido/registrado.

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: 1241378 / PORTALMOBILE01-1388]** Melhoria no processo de matrícula online, criado parâmetros para definir se a matrícula onlise será finalizada mesmo que no momento de regerar a parcela definida nos parâmetros a parcela estiver:BaixadaBaixada parcialmenteCom boleto registrado

Arquivos: RM.Edu.Parametros.Intf.dll, RM.Edu.Financeiro.Server.dll, RM.Edu.Parametros.Form.dll

## TOTVS Folha de Pagamento

### Rotina: FOLHA MENSAL ENTRADA DO MOVIMENTO LAB 01 110

* **[Ticket: 1094033 / FOPCALCULO01-722]** Ajuste no cálculo da pensão alimentícia, quando a base de IRRF fica negativa com a dedução do valor da pensão.

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

### Rotina: FUNCIONÁRIOS - HISTÓRICO DE AFASTAMENTO (LAB.01.150)

* **[Ticket: FOPCALCULO01-850]** Ajuste na rotina de exibição de pendências demissionais para funcionário com afastamento por acidente de trabalho cadastrado e com data de retorno preenchida, contendo registro de estabilidade.

Arquivo: RM.Fop.Funcionario.Data.dll

## TOTVS Gestão Contábil

### Rotina: RELATORIOS BALANCETE CTB 38 113

* **[Ticket: 767758 / CONTROLADORIA01-255]** Implementado o recarregamento da configuração do relatório Balancete ao ser alterado a configuração preferencial pelo usuário.

Arquivo: RM.Ctb.Relatorios.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: FLUIG APROVACAO CONTRATO POR CONTRATO FLG 006

* **[Ticket: 1233341 / MATESTCNTFTOF01-574]** Ajuste no cadastro de Tipos de Contrato para configurar os Estados de WorkFlow Fluig corretamente.

Arquivo: RM.Ctr.Cadastros.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: CONTROLE DE EXAMES AGENDA DE EXAMES SMT 36 001

* **[Ticket: 1043954 / RHU01-848]** Modificado lógica de seleção de escalas de uma AD para o cálculo. Agora é considerado apenas as escalas de mesmo tipo da AD. Se a AD avalia só fatores organisacionais apenas as escalas marcadas como fatores organisacionais serão consideradas.

Arquivo: RM.Rhu.AvalDesemp.Server.dll

### Rotina: REQUISICOES AUMENTO DE QUADRO RHU 36 095

* **[Ticket: 1065575 / RHU01-914]** Corrigido o lookup de seção em requisições quando o requisitante era de chefe de diversas seções.

Arquivos: Portal Corpore.Net

# 12.1.15.181

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 1267275 / PONTO01-1098]** Ajustes realizados no processo de recálculo para corrigir o problema da mensagem de inserção do funcionário no Chronus.

Arquivo: RM.Pto.Funcionario.Data.dll

* **[Ticket: 1211833 / PONTO01-1008]** Ajustes realizados no processo de compensação por período para permitir o funcionamento correto do cálculo.

Arquivo: RM.Pto.Calculo.Service.dll

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 1241689 / PONTO01-1046]** Ajustes no processo de geração do relatório do espelho do cartão, para que o relatório seja gerado com sucesso.

Arquivos: RM.Pto.Relatorio.Data.dll, RM.Pto.Funcionario.Data.dll

## TOTVS Educacional

### Rotina: CONTA CORRENTE DO ALUNO EDU 50 138

* **[Ticket: 1196915 / DEDUINTEGRACOES-189]** Realizado uma evolução no processo de transferência interna para que a matriz aplicada dos registros de conta corrente seja atualizada conforme a matriz aplicada de destino.A matiz aplicada no registro de conta corrente será atualizado somente se o contrato de origem estiver sendo cancelado, caso contrário o registro da conta corrente permanecerá com a matriz aplicada do contrato antigo.Habilitamos a opção de edição da conta corrente, possibilitando ao usuário alterar manualmente a matriz aplicada do registro da conta corrente.Será permitido alterar somente a matriz aplicadaSerá listado para a seleção somente matriz aplicada vinculada a um contrato do aluno, contrato que não esteja cancelado .

Arquivos: RM.Edu.dll, RM.Edu.Financeiro.Intf.dll, RM.Edu.Server.dll, RM.Edu.Financeiro.Data.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Matricula.Server.dll

## TOTVS Folha de Pagamento

### Rotina: Caged Conferência em Tela

* **[Ticket: FOPROTINAS01-1015]** Ajustes para adequar o CAGED conferência em tela ao novo layout disponibilizado

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: FOPROTINAS01-1015]** Correção de erro 'índice fora dos limites da matriz'

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: DIFERENCA SALARIAL LAB 01 109

* **[Ticket: 956859 / FOPCALCULO01-785]** Ajuste na função TABFUNC no processo da Diferença Salarial, para considerar a função e a seção da época.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: FERIAS CALCULO FOP 34 402

* **[Ticket: 954386 / FOPCALCULO01-520]** Ajuste no cálculo do INSS na diferença de média das férias partidas, quando calculada no primeiro mês.

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

* **[Ticket: 1206346 / FOPCALCULO01-816]** Ajuste no cálculo do IRRF Férias quando funcionário possui dois recibos no mesmo caixa, um com periodo de gozo e outro com somente pagamento de abono.

Arquivo: RM.Fop.Calc.CalculosBase.dll

## TOTVS Gerador de saídas

### Rotina: OUTROS

* **[Ticket: DFRWTOOLS-7]** Melhoria para adicionar um contexto de aplicação no layout do Gerador de Saída

Arquivo: RM.Gen.Engine.Designer.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CADASTRO DE FORMULA FRM 001

* **[Ticket: 1212510 / MATFATCMPCRM01-1017]** Melhorias nas funções de fórmula do movimento.

Arquivo: RM.Mov.Formula.dll

## TOTVS Gestão de Pessoas

### Rotina: AVALIACAO DE DESEMPENHO

* **[Ticket: 1126974 / RHU01-1007]** A mudança de seção ou função do funcionário enquanto uma avaliação de desempenho na qual ele estava sendo avaliado fazia com que os itens de performance do funcionário sumissem. Modificado pontos do código para considerar a função e a seção original do funcionário.

Arquivos: RM.Rhu.AvalDesemp.Server.dll, RM.Rhu.AvalDesemp.Data.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 1111359 / FINANCEIRO01-2038]** Melhoria no processo de baixa com cheque para permitir que seja efetuado no ambiente três camadas

Arquivos: RM.Fin.Utils.Intf.dll, RM.Fin.Cheque.Form.dll, RM.Fin.Utils.Server.dll, RM.Fin.CliFor.Form.dll

### Rotina: SERVICO DE CONTABILIZACAO FIN 323

* **[Ticket: 962839 / FINANCEIRO01-949]** Ajustado serviço de contabilização de baixa para poder buscar o evento contabil correto.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Patrimonial

### Rotina: CADASTROS PATRIMONIOS PAT 37 39

* **[Ticket: 1052353 / CONTROLADORIA01-324]** Durante a inclusão de um patrimônio, se a data de aquisição for inferior ao período de cálculo, é possível marcar a opção "Informar depreciação acumulada corrigida". Com esta opção selecionada é possível realizar o cálculo automático da depreciação acumulada, clicando no botão que possui a imagem de uma calculadora. Este cálculo foi alterado para que o dia de aquisição seja considerado.

Arquivo: RM.Pat.Patrimonio.Data.dll

### Rotina: RELATORIOS CONTABILIZACAO PAT 37 57

* **[Ticket: 1052666 / CONTROLADORIA01-390]** Implementar na verificação se a geração do relatório de contabilização está sendo por rateio gerencial o reconhecimento da strig rateio na descrição do relatório.

Arquivo: RM.Pat.Relatorio.Data.dll

## TOTVS Incorporação

### Rotina: #REVITALIZADA #SEGURO - Erro ao tentar gerar calculo de seguro - Base Revitalizada.

* **[Ticket: 1270137 / TINREV001-52]** Melhoria no processo de geração de seguro por empreendimento.

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: Desenvolvimento dos parâmetros do Reajuste

* **[Ticket: TINREV001-40]** Melhoria no processo de geração de plano de financiamento.

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 951698 / TINPAD001-797]** Melhoria no cálculo do resíduo anual distribuído com a nova engine.

Arquivo: RM.Imb.Reajuste.Server.dll

* **[Ticket: 951698 / TINPAD001-797]** Melhoria no cálculo da distribuição de resídulo anual.

Arquivo: RM.Imb.Reajuste.Server.dll

## TOTVS Processo Seletivo

### Rotina: Alterar senha do candidato

* **[Ticket: 1235240 / PORTALMOBILE01-1352]** Alteração na consulta SQL que busca o usuário para envio de uma nova senha.

Arquivo: RM.EduPS.Cadastros.Server.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: RELATORIOS PERFIL PROFISSIOGRAFICO PREVIDENCIARIO PPP SMT 36 578

* **[Ticket: 783976 / RHU01-115]** Agrupamento do relatório PPP por período de mudança (sem quebra por ano)

Arquivo: RM.Smt.Relatorio.Data.dll

# 12.1.15.182

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO RECALCULO PTO 35 1187

* **[Ticket: 1267275 / PONTO01-1098]** Ajustes realizados no processo de recálculo para corrigir o problema da mensagem de inserção do funcionário no Chronus.

Arquivo: RM.Pto.Funcionario.Data.dll

## TOTVS Business Connect

### Rotina: RM X FLUIG GED PARAMETROS DE CONFIGURACAO INT 00013

* **[Ticket: 1063585 / DFRWFOUNDATION-109]** Foi ajustado a forma de envio de arquivo para que suporte HTTPS

Arquivo: RM.Con.GED.Server.dll

## TOTVS Construção e Projetos

### Rotina: TIMESHEET APONTAMENTOS EM TAREFAS PRJ 33 993

* **[Ticket: 1092260 / TOPEXECONTROL01-507]** O Sistema passa a considerar a data de demissão ao validar o registro do funcionario em relação a data do apontamento no momento do registro do apontamento. Identifica a chapa ativa na data do apontamento.

Arquivo: RM.Prj.EquipeProjeto.Data.dll

* **[Ticket: 1092260 / TOPEXECONTROL01-507]** O Sistema passa a considerar a data de demissão ao validar o registro do funcionario em relação a data do apontamento no momento do registro do apontamento. Identifica a chapa ativa na data do apontamento.

Arquivo: RM.Prj.EquipeProjeto.Data.dll

## TOTVS Educacional

### Rotina: ALUNOS EDU 50 015

* **[Ticket: 1198209 / EDUCACIONAL01-1996]** A tela de cadastro de alunos foi corrigida para verificar o perfil do usuário antes de permitir alteração nas informações de filiação, responsáveis e na cópia de endereço.

Arquivo: RM.Edu.Aluno.Form.dll

### Rotina: DIGITACAO POR ALUNO NOTAS DE AVALIACOES EDU 50 176

* **[Ticket: 1203056 / EDUCACIONAL01-2138]** Ajuste na gravação de logs no lançamento de notas de alunos, a fim de evitar problemas da validação de chaves, devido a velocidade de processamento de alguns servidores. O alto desempenho de algumas máquinas demandou um melhor tratamento nas datas e horas que são registradas nos logs do sistema.

Arquivo: RM.Edu.NotaFalta.Server.dll

* **[Ticket: 1263036 / EDUCACIONAL01-2220]** Otimização da gravação de logs no lançamento de notas para evitar problemas de validação no seu registro.

Arquivo: RM.Edu.NotaFalta.Server.dll

### Rotina: Geração de Certificado de Participação

* **[Ticket: EDUCACIONAL01-2163]** Ajuste na geração de diplomação e certificação.

Arquivos: RM.Edu.Academico.Data.dll, RM.Edu.Academico.Form.dll

### Rotina: PORTAL LOGIN EDU 50 474

* **[Ticket: 1237723 / PORTALMOBILE01-1374]** Ajuste no retorno do contexto de professores que não são coordenadores.

Arquivo: RM.Edu.Contexto.Data.dll

### Rotina: Project-1258348 Problema ao carregar contexto no portal Project-1258348

* **[Ticket: 1272156 / PORTALMOBILE01-1439]** Realizado ajuste no retorno de informações de contexto de funcionários/professores.

Arquivo: RM.Edu.Contexto.Data.dll

## TOTVS Folha de Pagamento

### Rotina: FOLHA RECALCULO LAB 01 111

* **[Ticket: 1173002 / FOPCALCULO01-803]** Ajuste ao recalcular somente bases para não atualizar movimento de pensão

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

### Rotina: RESCISAO COMPLEMENTAR FOP 34 397

* **[Ticket: 1242408 / FOPCALCULO01-1000]** Ajuste no cálculo de médias na recisão complementar. para considerar eventos de envelopes de competências anteriores. com pagamentos após a data de pagamento da rescisão.

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Framework

### Rotina: PROJETO GERACAO DO PROJETO MTD 00010

* **[Ticket: 945800 / DFRWFOUNDATION-110]** Foi criado um mecanismo para que o host não precise ser reiniciado para que as dlls de metadados sejam geradas no ambiente dos hosts.

Arquivos: RM.Lib.dll, RM.Lib.MetadataProvider.dll, RM.Lib.Server.dll, RM.Lib.WinForms.dll, RM.Glb.Metadata.Form.dll, RM.Lib.MetadataProvider.Server.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 1043221 / CONTROLADORIA01-328]** O rejistro J150 está sendo gerado de acordo a parametrização realizada na DRE, não causando alterações no validador da Receita Federal.

Arquivo: RM.Ctb.Sped.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: CONTROLE DE METAS CONTROLE DE METAS NET RHU 36 011

* **[Ticket: 1196985 / RHU01-1234]** Toda meta criada pela MDI deve possuir o status de aprovação como aprovada ("A"). Modificado o processe de planejamento de metas para criar as metas como aprovadas como feito pelo dataserver correspondente.

Arquivo: RM.Rhu.GestaoMetas.Data.dll

### Rotina: FUNCIONARIOS RHU 36 035

* **[Ticket: 282313 / RHU01-255]** correção para remover os fatore orgnaizacionais quando um candidato é excluído de uma avaliação

Arquivo: RM.Rhu.Lib.Server.dll

### Rotina: REQUISICOES AUMENTO DE QUADRO RHU 36 095

* **[Ticket: 1065575 / RHU01-914]** Corrigido bug introduzido pelo checkin #510702/#510703/#510705/#510706

Arquivo: App\_Web\_rhucoligadafilialsecaofuncao.ascx.6868da05.dll

### Rotina: REQUISICOES TRANSFERENCIA RHU 36 506

* **[Ticket: 1033403 / RHU01-1302]** Correção nas requisições de alteração de dados funcionais e transferência com alterção de dados funcionais.

Arquivos: Portal Corpore.Net

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS ECF LI 01 0032

* **[Ticket: 1094018 / FISCAL01-881]** Foram realizadas alterações ao gerar a ECF, para que o sistema não quebre a linha do Registro M300 quando no campo “7 - Histórico do lançamento no e-Lalur” existir um Lançamento com o caracter “ENTER” no campo Histórico do Lançamento Manual do Evento Tributário:

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 892733 / FISCAL01-682]** Foi realizada uma alteração na geração do SPED Fiscal para que, ao gerar o Registro “G140”, o sistema obedeça a mesma combinação NUM\_ITEM + COD\_ITEM gerada no registro “C170”.

Arquivo: RM.Fis.Sped.Server.dll

### Rotina: OBRIGACOES PRINCIPAIS APURACAO IRPJ E CSLL LI 01 0041

* **[Ticket: 1100975 / FISCAL01-928]** Ajuste no Template da simulação quando é tributo CSLL e forma tributação Lucro Presumido para exibir a Receita de Vendas e serviço corretamente.

Arquivo: RM.Fis.RegrasTributarias.Form.dll

## TOTVS Incorporação

### Rotina: ALUGUEL EVENTO FINANCEIRO IMB 49 776

* **[Ticket: 1171476 / TINPAD001-827]** Melhoria no processo de efetivação da rescisão do contrato de locação com multa rescisória.

Arquivos: RM.Imb.Aluguel.ContratoLoc.Server.dll, RM.Imb.Aluguel.Lancamento.Server.dll

* **[Ticket: 1171476 / TINPAD001-827]** Melhoria ao efetivar a rescisão do contrato de locação.

Arquivo: RM.Imb.Aluguel.Lancamento.Server.dll

### Rotina: ALUGUEL - EVENTO FINANCEIRO IMB49776

* **[Ticket: TINPAD001-816]** Correção para considerar o primeiro dia do contrato de aluguel ao gerar parcelas

Arquivo: RM.Imb.Aluguel.Lancamento.Server.dll

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 807686 / TINPAD001-962]** Ajuste dos tipos de campos para evitar erro na execução de fórmula visual

Arquivo: RM.Imb.Venda.Contrato.Intf.dll

### Rotina: Desenvolvimento dos parâmetros do Reajuste

* **[Ticket: TINREV001-40]** Melhoria no reajuste.

Arquivo: RM.Imb.Venda.Contrato.Intf.dll

* **[Ticket: TINREV001-40]** Melhoria no reajuste.

Arquivo: RM.Imb.Venda.Contrato.Intf.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 1009958 / TINPAD001-568]** Melhoria no cálculo de resíduo anual com parcelas enviadas a banco.

Arquivo: RM.Imb.Reajuste.Server.dll

# 12.1.15.183

## TOTVS Folha de Pagamento

### Rotina: FERIAS ACERTA PERIODO AQUISITIVO FOP 34 407

* **[Ticket: 245711 / FOPCALCULO01-117]** Ajuste no acerto do periodo aquisitivo quando o ano de vencimento das férias é bissexto.

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Incorporação

### Rotina: ALUGUEL GERAR LANCAMENTOS FINANCEIROS IMB 49 777

* **[Ticket: 1259568 / TINPAD001-1077]** Ajustes vencimento apos o fim do contrato

Arquivo: RM.Imb.Aluguel.Imovel.Server.dll

# 12.1.15.184

## TOTVS Construção e Projetos

### Rotina: COPIA DE ITENS PRJ 33 779

* **[Ticket: 1267298 / TOPORCAPLAN001-1180]** PREÇO DE INSUMOS COPIADOS INCORRETAMENTE NA CÓPIA DE SUB-PROJETOS DA CÓPIA DE ITENS

Arquivo: RM.Prj.Projeto.Form.dll

## TOTVS Educacional

### Rotina: BOLETOS EDU 50 069

* **[Ticket: 1045294 / DEDUINTEGRACOES-248]** Foi realizada otimização da visão de boletos, afim de aumentar a performance para carregar os boletos da visão.

Arquivo: RM.Edu.Financeiro.Form.dll

### Rotina: Informações e serviços relacionados aos candidatos

* **[Ticket: PORTALMOBILE01-700]** Ajuste na validação de retorno do Contexto de Professor no portal do Corpore.Net de Pessoas são coordenadoras, e possuem duas chapas. Uma delas demitida.

Arquivo: RM.Edu.Contexto.Data.dll

### Rotina: PORTAL ALUNO SOLICITACOES EDU 50 367

* **[Ticket: 1016552 / PORTALMOBILE01-877]** Ajuste para exibir os parâmetros, na tela de confirmação de abertura de soliticação, de acordo com a configuração de visibilidade nas etapas do tipo de atendimento.

Arquivo: App\_Web\_educonfirmasolicitacao.aspx.2d3da776.dll

## TOTVS Folha de Pagamento

### Rotina: VALIDACAO DA LIBERACAO DE COMPETENCIA LAB 01 124

* **[Ticket: 1237635 / FOPCALCULO01-952]** Ajuste na SEFIP retificadora por tomador que não estava acumulando valores do envelope original na Base de Cálculo da Previdência Social.

Arquivo: RM.Fop.Calc.Calculos.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INT PARAMETRIZACAO TBC WEBSERVICE INT 001

* **[Ticket: 1296474 / MATFATCMPCRM01-1109]** Melhoria na rotina de faturamento via webservice

Arquivos: RM.Mov.CopiaMovimento.Service.dll, RM.Mov.CopiaMovimento.IService.dll

## TOTVS Gestão Financeira

### Rotina: LANCAMENTO BAIXA FIN 185

* **[Ticket: 1237244 / FINANCEIRO01-2212]** Ajustado serviço de baixa de lançamento remetidos.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 892733 / FISCAL01-682]** Ao gerar o SPED Fiscal para determinados lançamentos, o sistema estava emitindo a seguinte mensagem: "O item já foi adicionado. Chave contida no dicionário: "01.01"; chave de acesso sendo adicionada.". Devido à esse problema os lançamentos não estavam sendo gerados.Foi realizada uma alteração para que essa mensagem não seja emitida.

Arquivo: RM.Fis.Sped.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: UTILITARIOS REABERTURA DE COMPETENCIA PAT 37 94

* **[Ticket: 1242994 / CONTROLADORIA01-448]** Não estava sendo possível excluir, através do processo de reabertura de competência, as transferências patrimoniais que foram realizadas com a opção "Unificar mantendo-se as quantidades de origem" marcada. O processo foi alterado para que todas as ocorrências existente no período vigente sejam excluídas com sucesso.

Arquivo: RM.Pat.Ocorrencia.Service.dll

## TOTVS Incorporação

### Rotina: Implementação do Resíduo

* **[Ticket: TINREV001-62]** Implementação da customização de nomes de empreendimento, unidade e subunidade no relatório da FF

Arquivos: RM.Imb.Relatorio.Intf.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Relatorio.Data.dll

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 1009958 / TINPAD001-1162]** Melhoria no resíduo anual ao distribuir o resíduo.

Arquivo: RM.Imb.Reajuste.Server.dll

* **[Ticket: 1009958 / TINPAD001-1162]** Melhoria no resíduo anual ao distribuir o resíduo.

Arquivo: RM.Imb.Reajuste.Server.dll

### Rotina: RELATORIOS INCORPORACAO IMB 49 854

* **[Ticket: 1323502 / TINPAD001-1178]** Melhoria no relatório de ficha financeira FFAPF001.

Arquivos: RM.Imb.Relatorio.Intf.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll, RM.Imb.Relatorio.Data.dll

# 12.1.15.185

## TOTVS Educacional

### Rotina: PORTAL ALUNO SOLICITACOES EDU 50 367

* **[Ticket: 1131370 / PORTALMOBILE01-1150]** Ajustes ao abrir solicitação no portal do Aluno quando o parâmetro para substituir todo o valor atual do serviço pelo valor do tipo de atendimento está marcado.

Arquivos: FrameHTML

## TOTVS Folha de Pagamento

### Rotina: GUIA DE INSS

* **[Ticket: 1329910 / FOPROTINAS01-1406]** Ajuste na importação de arquivos de autonomos na geração de Guia de INSS

Arquivo: RM.Fop.Dominio.dll

## TOTVS Gestão Financeira

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 1041887 / FINANCEIRO01-2248]** Ajuste no processo de retorno bancario para recalcular o valor liquido de acordo com os valores do arquivo.

Arquivo: RM.Fin.Lan.Service.dll

# 12.1.15.186

## TOTVS Automação de Ponto

### Rotina: MOVIMENTO COMPENSACAO LANCAMENTO DO BANCO DE HORAS PTO 35 1195

* **[Ticket: 1242447 / PONTO01-1109]** Ajustes realizados no processo de compensação e lançamento do banco de horas, para que os lançamentos sejam feitos da maneira correta.

Arquivo: RM.Pto.BancoDeHoras.Data.dll

### Rotina: PORTAL WEB EXCLUIR ABONOS CADASTRADOS PTO 35 1259

* **[Ticket: 1241328 / PONTO01-1069]** Correções realizadas no processo de exclusão de abonos através do portal e da MDI

Arquivo: RM.Pto.Abono.Data.dll

## TOTVS Business Connect

### Rotina: Autenticar os usuários para chamadas TBC+ IIS

* **[Ticket: DFRWFOUNDATION-491]** Chamar os processos via web services com login unif.

Arquivo: RM.Con.Conector.WebService.dll

### Rotina: Tradução erronea de tags do XML

* **[Ticket: DFRWTOOLS-230]** Fixado no código as palavras chaves para o envio da mensagem pelo EAI

Arquivo: RM.Con.TotvsMessage.Intf.dll

## TOTVS Educacional

### Rotina: PORTAL ALUNO PLANO DE AULA EDU 50 363

* **[Ticket: 1062262 / PORTALMOBILE01-1050]** Ajuste na visão de planos de aula do Portal do Aluno para não exibir as disciplinas do ensino básico duplicadas

Arquivo: RM.Edu.Matricula.Data.dll

## TOTVS Folha de Pagamento

### Rotina: GUIA DE INSS

* **[Ticket: 1329910 / FOPROTINAS01-1406]** Ajuste na importação de arquivos de autonomos na geração de Guia de INSS

Arquivo: RM.Fop.Dominio.dll

### Rotina: RELATORIO TRCT FOP 34 546

* **[Ticket: 873589 / FOPROTINAS01-1285]** Ajustes no cálculo do TRCT quando o funcionário possui mais de um período de férias perdido

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: VALIDACAO DA LIBERACAO DE COMPETENCIA LAB 01 124

* **[Ticket: 1204061 / FOPCALCULO01-822]** Ajuste para calcular diferença de licença remunerada para em férias coletivas

Arquivos: RM.Fop.Calc.CalculosBase.dll, RM.Fop.Calc.Calculos.dll

## TOTVS Framework

### Rotina: Tradução erronea de tags do XML

* **[Ticket: DFRWTOOLS-230]** Fixado no código as palavras chaves para o envio da mensagem pelo EAI

Arquivo: RM.Lib.dll

## TOTVS Gestão Contábil

### Rotina: ESCRITURACAO CONTABIL LANCAMENTOS CTB 39 006

* **[Ticket: 1132819 / CONTROLADORIA01-415]** Melhoria na tela de edição de partidas para que ao alterar qualquer campo os textos que aparecem nos campos Filial, Centro de Custo e Departamento não se alterem.

Arquivo: RM.Ctb.Lan.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CANCELAR MOVIMENTO MOV 004

* **[Ticket: 893951 / MATESTCNTFTOF01-548]** Ajuste interno na rotina de cancelamento de movimentos que possuem produtos peps/upes repetidos no mesmo movimento.

Arquivo: RM.Est.Baixa.Service.dll

### Rotina: INCLUSAO DE MOVIMENTO MOV 001

* **[Ticket: 1219450 / MATESTCNTFTOF01-648]** Ajuste nos movimentos de entrada para mostrar todos os lotes disponíveis para inclusão, e não apenas os lotes da Filial e Local do movimento.

Arquivo: RM.Est.Produto.Data.dll

### Rotina: INT PARAMETRIZACAO TBC WEBSERVICE INT 001

* **[Ticket: 1296474 / MATFATCMPCRM01-1109]** Melhorias no processo de faturamento automático.

Arquivo: RM.Mov.CopiaMovimento.Service.dll

* **[Ticket: 1296474 / MATFATCMPCRM01-1109]** Melhorias no processo de faturamento quando executado através de WebService.

Arquivo: RM.Mov.CopiaMovimento.Service.dll

## TOTVS Gestão Financeira

### Rotina: CLIENTE FORNECEDOR INCLUSAO ALTERACAO EXCLUSAO FIN 104

* **[Ticket: 1230293 / FINANCEIRO01-1953]** Ajuste no cadastro do cliente/fornecedor para considerar os campos que não devem ser validados como obrigatorio.

Arquivo: RM.Fin.CliFor.Service.dll

### Rotina: SERVICO DE CONTABILIZACAO FIN 323

* **[Ticket: 1323861 / FINANCEIRO01-2384]** Ajuste na baixa ao gerar extrato para outra coligada (mutuo)

Arquivos: RM.Fin.Lan.Form.dll, RM.Fin.Lan.Service.dll

## TOTVS Incorporação

### Rotina: COMPRADOR IMB 49 809

* **[Ticket: 877280 / TINPAD001-1108]** Alteração para permitir visualisar os compradores da venda quando acessada de uma coligada diferente

Arquivo: RM.Imb.Contratos.Form.dll

### Rotina: Implementação das tabelas de Reajuste do legado

* **[Ticket: TINREV001-60]** Melhoria no calculo do numero do documento para o aditivo de troca de comprador, apenas versão revitalizada.

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll

* **[Ticket: TINREV001-60]** Melhoria no processo de geração do plano de financiamento.

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll, RM.Imb.Venda.Calc.Calculos.Proc.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: EXAMES ASSIST IMPORTACAO DE RESULTADO DE EXAMES SMT 36 030

* **[Ticket: 879253 / RHU01-823]** Realizado ajuste no lookup Profissional de Saúde no cadastro de Atestados.

Arquivo: RM.Smt.Pessoa.Form.dll

# 12.1.15.188

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INT PARAMETRIZACAO TBC WEBSERVICE INT 001

* **[Ticket: 1296474 / MATFATCMPCRM01-1109]** Melhorias no processo de faturamento automático.

Arquivo: RM.Mov.CopiaMovimento.Service.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS EFD PIS COFINS LI 01 0033

* **[Ticket: 1099321 / FISCAL01-981]** Ajuste do contexto para importação e execução do Layout EFD Contribuições

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: Teste Sistêmico - NFS-e

* **[Ticket: FISCAL01-1424]** Ajuste no envio de NFS-e modelo TXT

Arquivo: RM.Fis.RotinasFiscais.Service.dll

# 12.1.15.189

## TOTVS Automação de Ponto

### Rotina: HORARIOS PTO 35 1180

* **[Ticket: 1070896 / PONTO01-1119]** Exposição da fórmula NDIASDESC do Chronus como serviço

Arquivos: RM.Pto.Lib.Intf.dll, RM.Pto.Formula.dll

### Rotina: PE - geração extra e atrasos (indevidos)

* **[Ticket: 1354869 / PONTO01-1231]** Correções realizadas no processo de cálculo, para considerar a ausência de refeição de forma correta.

Arquivo: RM.Pto.Calculo.Service.dll

## TOTVS Construção e Projetos

### Rotina: CONTRATOS REAJUSTE PRJ 33 943

* **[Ticket: 1358659 / TOPEXECONTROL01-893]** Ajustes na validação de associação de insumos acima do planejado para permitir itens de contrato sem insumo detalhado.

Arquivo: RM.Prj.Contrato.Data.dll

## TOTVS Folha de Pagamento

### Rotina: PARAMETROS GLOBAIS LAB 01 191

* **[Ticket: 867662 / FOPROTINAS01-508]** Ajuste na cópia entre coligadas de parâmetros de lançamentos financeiros para tratar casos que utilizavam natureza financeira global.

Arquivo: RM.Fop.Cadastros.Data.dll

## TOTVS Gestão Contábil

### Rotina: Relatórios Contábeis - Travamento na Visão de Relatórios

* **[Ticket: 1318075 / CONTROLADORIA01-460]** A tela de parâmetros dos relatórios contábeis estava congelando, travando o sistema, porém elas passaram a ser carregadas em um intervalo de tempo aceitável. Vale ressaltar que na abertura da tela estão sendo milhares de departamentos. Para que a tela seja carregada rapidamente, ao invés de selecionar todos os departamentos e filiais de uma coligada, recomendamos que apenas a coligada seja selecionada.

Arquivos: RM.Ctb.Lib.WinForms.dll, RM.Ctb.Relatorios.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: AVALIACAO DE DESEMPENHO

* **[Ticket: 1288519 / RHU01-1286]** Modificado o comportamento do flag "Ocultar notas para Avaliador/Avaliado" para não ocultar as notas das competências.

Arquivo: App\_Web\_rhuavaliacaodesempenhoexecucao.ascx.246e283e.dll

* **[Ticket: 1206251 / RHU01-1282]** A nota calculada era mostrada errada pois considerava mais de um participante. Adicionado uma condição para considerar apenas o participante atual do portal.

Arquivo: RM.Rhu.AvalDesemp.Data.dll

## TOTVS Gestão Financeira

### Rotina: BOLETO INCLUSAO EXCLUSAO FIN 045

* **[Ticket: 1149867 / FINANCEIRO01-1917]** Ajuste no processo de inclusao de boleto para obedecer a ordem dos lançamentos quando a opção de geração um boleto para cada lançamento.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: GTCP-T4607 (1.0) Validar a exportação e importação de CliFor

* **[Ticket: FINANCEIRO01-2472]** Criando enumerado para os novos tipo primitivos do cadastro de meio de pagamento

Arquivo: RM.Fin.Lib.dll

### Rotina: RETORNO DE COBRANCA ELETRONICA FIN 235

* **[Ticket: 1227077 / FINANCEIRO01-2220]** Melhoria de performance no processo de retorno bancário

Arquivo: RM.Fin.Lan.Service.dll

* **[Ticket: 1182274 / FINANCEIRO01-2231]** Melhoria de performance no processo de retorno bancário

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: NF E ENVIO NF 01 0045

* **[Ticket: 956316 / FISCAL01-1384]** Implementação para alterar os dados do XML para substituir o caractere travessão por hifen na NF-e, pois o TSS não aceita este caractere. Assim evitando que a NF-e inconsistente no sistema devido a esta informação no XML.

Arquivo: RM.Fis.Utils.Server.dll

## TOTVS Incorporação

### Rotina: CONTRATOS IMB 49 813

* **[Ticket: 1372755 / TINREV001-66]** Melhoria no processo de geração de plano de financiamento.

Arquivos: RM.Imb.Cadastros.Data.dll, RM.Imb.Venda.Calc.CalculosBase.dll

### Rotina: Implementação das tabelas de Reajuste do legado

* **[Ticket: TINREV001-60]** Melhoria nos lookups de formula do aditivo global e distrato.

Arquivo: RM.Imb.Venda.Distrato.Form.dll

# 12.1.15.190

## TOTVS Automação de Ponto

### Rotina: CONFIGURACOES PARAMETRIZADOR INICIAIS PTO 35 1216

* **[Ticket: 1213038 / PONTO01-1177]** Ajustes realizados no processo de atualização do espelho.

Arquivo: RM.Pto.Batida.Form.dll

### Rotina: PROCESSO DE CONTROLE DE REFEICOES PTO 35 1247

* **[Ticket: 1308041 / PONTO01-1179]** Alterações na validação do crachá de visitante para corrigir o erro apresentado.

Arquivo: RM.Pto.CadastroDeCracha.Data.dll

### Rotina: Project-1338467 Calculo do Ponto na verão 12.1.17.125, não considerando a jornada trabalhada. Project-1338467

* **[Ticket: 1372524 / PONTO01-1263]** Ajustes realizados na formatação dos valores de carência de atraso.

Arquivo: RM.Pto.Calculo.Service.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: IMP CIRURGIA SAUIH 55 621

* **[Ticket: 1318569 / MSAU-13847]** Ajuste na rotina da importação de cirurgias.

Arquivos: RM.SauIH.Importacao.Intf.dll, RM.SauIH.Importacao.Data.dll

* **[Ticket: 1318569 / MSAU-13847]** Ajuste na rotina da importação de cirurgias.

Arquivo: RM.SauIH.Importacao.Data.dll

## TOTVS Educacional

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 1363702 / EDUCACIONAL01-2435]** Otimização no processo de envio de email via agendamento de job, para avisos de frequência de bolsistas e relatório parcial/final ao coordenador no FLUIG.

Arquivo: RM.Edu.Academico.Server.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: Downgrade 12.1.15

* **[Ticket: MATFATCMPCRM01-678]** Implementação do CT-e OS

Arquivos: RM.Mov.CopiaMovimento.Service.dll, RM.Mov.CTe.Service.dll, RM.Mov.Movimento.Data.dll, RM.Mov.CTe.Data.dll, RM.Mov.Consts.dll, RM.Mov.Cadastros.Intf.dll, RM.Mov.Utils.Intf.dll, RM.Mov.CTe.Intf.dll, RM.Mov.TOTVSColab.IService.dll, RM.Mov.Parametros.Intf.dll, RM.Mov.CTe.IService.dll, RM.Mov.Reports.Server.dll, RM.Mov.CTe.Form.dll, RM.Mov.Movimento.IService.dll, RM.Mov.Movimento.Intf.dll, RM.Mov.Parametros.Form.dll, RM.Mov.Cadastros.Form.dll, RM.Mov.Facade.dll, RM.Mov.Movimento.Form.dll, RM.Mov.Movimento.Service.dll, RM.Mov.Parametros.Data.dll, RM.Mov.TOTVSColab.Service.dll, RM.Mov.Cadastros.Data.dll

* **[Ticket: MATFATCMPCRM01-678]** Implementação CT-e OS

Arquivo: RM.Est.Server.dll

### Rotina: REGERAR SALDOS E CUSTOS EST 013

* **[Ticket: 921451 / MATESTCNTFTOF01-349]** Melhoria de performance no processo de Regeração de Saldos e Custos para produtos que utilizam número de série.

Arquivos: RM.Est.Estoque.Service.dll, RM.Est.Processos.Data.dll

## TOTVS Gestão Financeira

### Rotina: GTCP-T4658 (1.0) Validar todos os processos relacionados a lançamentos provenientes do Totvs Gestão de estoque

* **[Ticket: FINANCEIRO01-2474]** Adicionando imagem para Vale Alimentação, Refeição, Combunstível e Presente

Arquivo: RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

### Rotina: Downgrade 12.1.15

* **[Ticket: MATFATCMPCRM01-678]** Implementação CT-e OS

Arquivos: RM.Fis.Lib.dll, RM.Fis.Utils.Intf.dll, RM.Fis.TSS.IService.dll, RM.Fis.Facade.dll, RM.Fis.TSS.Service.dll

### Rotina: OBRIGACOES ACESSORIAS ESTADUAIS LI 01 0027

* **[Ticket: 1193114 / FISCAL01-1522]** Implementação dos sub tipos ESTCRED5005, ESTDEBI5005 e ICMSDEV5005 nos lançamentos Outros Débitos e Créditos.Estes Subtipos estarão disponíveis na filial do estado "DF" ou para Lançamentos com o Cod ETD igual a "DF".No Encerramento do Período ICMS os novos SubTipos serão considerados.

Arquivos: RM.Fis.Lib.dll, RM.Fis.ApuracaoTrb.Service.dll, RM.Fis.LancFiscal.Form.dll

### Rotina: SPED Fiscal - Erro Registro G140

* **[Ticket: FISCAL01-1618]** Alteração na geração do G140

Arquivo: RM.Fis.Sped.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: PAT - PROCESSOS

* **[Ticket: CONTROLADORIA01-474]** Melhoria no processo de Transferência Monetária marcando as opções "Parcial", “Desmembrar patrimônio de origem" e "Desmembrar por quantidade baseado no patrimônio de origem" para que o mesmo valide se a quantidade informada é maior que a quantidade existente no Patrimônio.

Arquivos: RM.Pat.PatrimonioMoeda.IService.dll, RM.Pat.Ocorrencia.Service.dll, RM.Pat.Patrimonio.Form.dll, RM.Pat.Ocorrencia.Form.dll

* **[Ticket: CONTROLADORIA01-474]** Ao retornar a alocação para o controle atual está sendo gerada uma nova alocação para os dados existentes no controle (filial, departamento, etc).

Arquivo: RM.Pat.Transferencia.Service.dll

## TOTVS Processo Seletivo

### Rotina: QUERO ME INSCREVER PORTAL EDUPS 20 1083

* **[Ticket: 1369570 / PORTALMOBILE01-1664]** Ajuste na exibição do Comprovante de inscrição do Processo Seletivo.

Arquivos: App\_Web\_edupsinscricaoareaofertada.ascx.58ed3fed.dll, App\_Web\_edupsimpressoes.ascx.ca9058f9.dll, RM.EduPS.Lib.Intf.dll, RM.EduPS.Inscricoes.Server.dll, RM.EduPS.Relatorios.WebForm.dll, RM.EduPS.ServicosWeb.Server.dll

# 12.1.15.191

## TOTVS Automação de Ponto

### Rotina: RELATORIOS ESPELHO DO CARTAO PTO 35 1201

* **[Ticket: 1420882 / PONTO01-1372]** Ajustes realizados na compensação por período.

Arquivo: RM.Pto.Calculo.Service.dll

* **[Ticket: 1294464 / PONTO01-1196]** Ajustes realizados no processo de geração do relatório do espelho.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Construção e Projetos

### Rotina: BACKUP RESTAURACAO DE PROJETOS PRJ 33 781

* **[Ticket: 1290542 / TOPORCAPLAN001-1198]** Processo de backup/restore tratado para validar recursos globais e locais

Arquivo: RM.Prj.BackupRestore.Data.dll

## TOTVS Folha de Pagamento

### Rotina: CALCULO PENSAO FOP 34 471

* **[Ticket: 1321944 / FOPCALCULO01-1089]** Ajuste na função de fórmula TI para utilizar o objeto correto na classe proprietária.

Arquivo: RM.Fop.Calc.Formulas.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: Downgrade 12.1.16

* **[Ticket: MATFATCMPCRM01-1241]** Implementação CT-e OS

Arquivos: RM.Lib.Params.Wizard.xml, RM.Est.dll, RM.Mov.CTe.Intf.dll, RM.Mov.CTe.Service.dll, RM.Mov.Reports.Server.dll

## TOTVS Gestão Patrimonial

### Rotina: PAT - RELATÓRIOS

* **[Ticket: CONTROLADORIA01-477]** Não estava sendo possível emitir o relatório "Ficha de imobilizado por filial", porém ele foi alterado para que os dados possam ser exibidos.

Arquivo: RM.Pat.Relatorio.Data.dll

# 12.1.15.192

## TOTVS Automação de Ponto

### Rotina: PORTAL WEB APROVAR ABONOS PTO 35 1268

* **[Ticket: 1159866 / PONTO01-945]** Incluida informação no processo de solicitação de abono através do Portal Web quando o usuário está travado no Chronus.

Arquivos: RM.Pto.Ocorrencia.Data.dll, RM.Pto.Abono.Data.dll

### Rotina: RELATORIOS EXCECOES PTO 35 1204

* **[Ticket: 725798 / PONTO01-83]** Foi realizado o ajuste da geração do relatório de exceções quando o funcionário tem data de admissão posterior a data parametrizada na geração do relatório.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Educacional

### Rotina: Formulário público de cadastro do aluno

* **[Ticket: EDUEDU004-12]** Ajuste na página pública e fluxo do cadastro de aluno para tratar filial ao filtrar os cursos.

Arquivos: Portal Corpore.Net

### Rotina: INTEGRACAO E LEARNING MANAGEMENT SUIT LMS EDU 50 464

* **[Ticket: 1282756 / EDUCACIONAL01-2477]** Alterado validação ao alterar usuário do aluno ou do professor. Não será possível alterar usuário somente se o mesmo já foi integrado ao Fluig LMS e não utiliza integração SAML (identity).

Arquivos: RM.Edu.Aluno.Data.dll, RM.Edu.Professor.Data.dll

### Rotina: MUDAR TURMA EDU 50 314

* **[Ticket: 1281793 / EDUCACIONAL01-2209]** Acerto no sistema para sempre considerar como padrão para consulta à parametrizações o sistema Educacional, pois ao tentar acessar algum processo ou visão, do Educacional, com outro módulo carregado no contexto, as informações de parâmetros não eram recuperadas.

Arquivos: RM.Edu.Matricula.Form.dll, RM.Edu.NotaFalta.Form.dll, RM.Edu.Parametros.Form.dll, RM.Edu.PeriodoLetivo.Form.dll, RM.Edu.Processos.Form.dll, RM.Edu.ProcSel.Form.dll, RM.Edu.Professor.Form.dll, RM.Edu.Solicitacoes.Form.dll, RM.Edu.Lib.WinForms.dll, RM.Edu.Academico.Form.dll, RM.Edu.Aluno.Form.dll, RM.Edu.Financeiro.Form.dll

### Rotina: TURMAS DISCIPLINAS EDU 50 454

* **[Ticket: 1350934 / EDUCACIONAL01-2419]** Gerenciamento de Aula corrigido para não gerar plano de aula duplicado em turmas gerenciadas quando já houver plano de aula gerado para a mesma data que está sendo gerado no momento.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## TOTVS Folha de Pagamento

### Rotina: GERACAO SEFIP

* **[Ticket: 1237635 / FOPCALCULO01-1175]** Ajuste no SEFIP de Retificação para não informar o valor do segurado no caso de único vínculo.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: PARAMETROS GLOBAIS LAB 01 191

* **[Ticket: 867662 / FOPROTINAS01-508]** Ajuste na cópia entre coligadas de parâmetros de lançamentos financeiros para tratar casos que utilizavam natureza financeira global.

Arquivo: RM.Fop.Cadastros.Data.dll

# 12.1.15.193

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E ENVIO DE EVENTO CTE 006

* **[Ticket: 1471141 / MATFATCMPCRM01-1407]** Melhoria para envio do CT-e OS quado o Tomador é Pessoa Física.

Arquivos: RM.Mov.CopiaMovimento.Service.dll, RM.Mov.CTe.Intf.dll, RM.Mov.Parametros.Form.dll, RM.Mov.CTe.Form.dll, RM.Mov.CTe.Service.dll, RM.Mov.Reports.Server.dll

# 12.1.15.194

## TOTVS Construção e Projetos

### Rotina: CONTRATOS MEDICAO PRJ 33 941

* **[Ticket: 1474058 / TOPEXECONTROL01-1147]** TOP - ContratoAnalise do controle de parâmetro, que permite o consumo ou medição acima da quantidade contratada.

Arquivo: RM.Prj.Contrato.Data.dll

* **[Ticket: 1474058 / TOPEXECONTROL01-1147]** TOP - ContratoAnalise do controle de parâmetro, que permite o consumo ou medição acima da quantidade contratada.

Arquivo: RM.Prj.Contrato.Data.dll

### Rotina: MENSAGEM UNICA CADASTRO PROJETO OBRA E TAREFA PRJ 33 918

* **[Ticket: 1388000 / TOPEXECONTROL01-1131]** Ajuste para evitar falha em situações de exclusão de tarefa, sem formula visual com posterior execução do sincronismo, em situação do parametro não enviar valor desativado.

Arquivo: RM.Prj.Integracao.Server.dll

* **[Ticket: 1388000 / TOPEXECONTROL01-1131]** Ajuste para evitar falha em situações de exclusão de tarefa, sem formula visual com posterior execução do sincronismo, em situação do parametro não enviar valor desativado.

Arquivo: RM.Prj.Integracao.Server.dll

## TOTVS Educacional

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 1448766 / DEDUINTEGRACOES-572]** Downgrade de correção que faz com que o as tags de complemento de histórico sejam devidamente resolvidas durante a geração de movimentos em regime de competência.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Facade.dll, RM.Edu.Financeiro.Server.dll

### Rotina: IMPORTADOR CURRICULO LATTES PROFESSOR EDU 50 269

* **[Ticket: 1394098 / EDUCACIONAL01-2672]** Otimização da importação de currículo Lattes do professor, com aumento de campos no banco de dados.Será necessário executar script específico cuja marcação é CN.2017.10\_02.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Professor.Intf.dll, RM.Edu.Professor.Server.dll, RM.Edu.Professor.Data.dll, RM.Edu.Professor.Form.dll

## TOTVS Folha de Pagamento

### Rotina: FUNCIONARIOS CADASTRO LAB 01 128

* **[Ticket: 782674 / FOPROTINAS01-1800]** Ajuste para correção de filtro por perfil utilizando cláusula "LIKE"

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RESCISAO CALCULO DE RESCISAO FOP 34 401

* **[Ticket: 1282204 / FOPCALCULO01-1090]** Ajuste no parâmetro ‘Considera divisor pelo número de dias do mês na remuneração da Admissão e Demissão’ para ser considerado também em eventos do tipo Hora.

Arquivo: RM.Fop.Calc.CalculosBase.dll

## TOTVS Framework

### Rotina: FUNCIONARIOS CADASTRO LAB 01 128

* **[Ticket: 782674 / FOPROTINAS01-1800]** Foi realizada uma alteração para que o filtro de perfil utilizando like funcionasse no select do DataTable.

Arquivo: RM.Lib.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: MOV BAIXA DE ESTOQUE EST 002

* **[Ticket: 1113107 / MATESTCNTFTOF01-802]** Ajuste no processo de regerar saldos e custos para movimentações de transferência de estoque.

Arquivo: RM.Est.Estoque.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: Erro processo de Triagem

* **[Ticket: 1329346 / RHU01-1376]** Correção de erro ao iniciar processo de seleção/executar triagem.

Arquivo: RM.Rhu.Captacao.Data.dll

## TOTVS Gestão Financeira

### Rotina: INTEGRACAO PROTHEUS BACKOFFICE EDU 50 466

* **[Ticket: 1404713 / FINANCEIRO01-3063]** Ajuste na integração Educacional x Backoffice Protheus no envio de mensagem de lançamentos a pagar ao Protheus.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Patrimonial

### Rotina: UTILITARIOS GERACAO DE PATRIMONIOS EM LOTE PAT 37 101

* **[Ticket: 1345702 / CONTROLADORIA01-493]** Implementado a exibição da mensagem correta, conforme já exibido na parametrização, referente à impossibilidade de gerar um código sequencial no processo de geração de patrimônios em lote, para o código do patrimônio quando o mesmo contém letras na máscara

Arquivo: RM.Pat.Patrimonio.Service.dll

# 12.1.15.195

## TOTVS Educacional

### Rotina: HISTORICO ALUNO EDU 50 250

* **[Ticket: 1303327 / EDUCACIONAL01-2792]** Ao emitir o relatório de histórico o sistema apresentava somente os 2 primeiros anos do aluno e não mostrava o terceiro.Foi verificado que o aluno está cursando o mesmo período nos dois últimos anos e relatório fazia a quebra apenas pelo período letivo. Foi incluído o ano na quebra do relatório.

Arquivo: RM.Edu.Lib.Server.dll

### Rotina: IMPORTADOR CURRICULO LATTES PROFESSOR EDU 50 269

* **[Ticket: 1394098 / EDUCACIONAL01-2813]** Otimização da importação de currículo Lattes do professor, com aumento do tamanho de campos no banco de dados, campos: DOI, ISSNISBN, VOLUME, SERIE, FASCICULO, NOMEINSTITUICAO.Será necessário executar script específico cuja marcação é CN.2017.10\_09.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Professor.Intf.dll, RM.Edu.Professor.Server.dll, RM.Edu.Professor.Data.dll, RM.Edu.Professor.Form.dll

### Rotina: INTEGRAÇÃO PROTHEUS (BACKOFFICE) (EDU.50.466)

* **[Ticket: DEDUINTEGRACOES-722]** Integração customizada entre o TOTVS Educacional e Protheus, onde será feita a exportação dos lançamentos contábeis dos Contratos educacionais (RM x Protheus).

Arquivos: RM.Edu.Customizacao.Intf.dll, RM.Edu.Contabil.Server.dll

### Rotina: PORTAL PROFESSOR AVALIACOES EDU 50 371

* **[Ticket: 1084761 / PORTALMOBILE01-1056]** Ajuste na consulta SQL que faz a busca das informações do aluno.

Arquivos: RM.Edu.NotaFalta.Data.dll, App\_Web\_edualunoetapaavaliacoeswebform.ascx.497dfae.dll

### Rotina: Project-1483726 Preenchimento de campo obrigatório Project-1483726

* **[Ticket: 1491726 / EDUCACIONAL01-2782]** Atualização no sistema para acertos na gravação do código de aplicação utilizado na gravação das preferências de usuários.

Arquivos: RM.Edu.Aluno.Data.dll, RM.Edu.Financeiro.Data.dll, RM.Edu.Lib.WinForms.dll, RM.Edu.PeriodoLetivo.Server.dll, RM.Edu.PesquisaExtensao.Data.dll, RM.Edu.Professor.Data.dll, RM.Edu.Academico.Form.dll, RM.Edu.Aluno.Form.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.Matricula.Form.dll, RM.Edu.NotaFalta.Form.dll, RM.Edu.Parametros.Form.dll, RM.Edu.PeriodoLetivo.Form.dll, RM.Edu.Processos.Form.dll, RM.Edu.ProcSel.Form.dll, RM.Edu.Professor.Form.dll, RM.Edu.Solicitacoes.Form.dll, RM.Edu.NotaFalta.Data.dll, RM.Edu.PeriodoLetivo.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E INCONSISTENCIA CTE 002

* **[Ticket: 1496071 / MATFATCMPCRM01-1477]** Melhorias no bloqueio dos campos do movimento para edição quando existir um CTeOS emitido e autorizado pela SEFAZ.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: TOTVS | SMARTCLIENT

* **[Ticket: MATESTCNTFTOF01-879]** Melhoria na consulta de movimento realizada pelo Fluig para executar as querys com NOLOCK.

Arquivo: RM.Mov.Movimento.Data.dll

* **[Ticket: MATESTCNTFTOF01-879]** Ajuste no ReadRecord para realizar o preenchimento da tabela DLAFMOVPROCESSOJUD no dataSet que havia sido retirado no merge.

Arquivo: RM.Mov.Movimento.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: RM: bloqueio de acesso a menus

* **[Ticket: 795311 / RHU01-142]** Ajuste na permissão de menu de tabelas auxiliares de seleção

Arquivos: RM.Rhu.dll, RM.Rhu.Server.dll

## TOTVS Incorporação

### Rotina: VENDEDOR IMB 49 870

* **[Ticket: 1240496 / TINPAD001-1015]** Melhoria na permissão do vendedor do contrato de venda.

Arquivo: RM.Imb.Contratos.Form.dll

# 12.1.15.196

## TOTVS Business Connect

### Rotina: EAI 1.0 - SOURCE CODE SEM (NOLOCK) - JHSF - ERRO

* **[Ticket: DFRWTOOLS-616]** Melhoria na execução dos scripts da integração

Arquivo: RM.Con.ConfiguraIntegracao.Server.dll

## TOTVS Educacional

### Rotina: INTEGRAÇÃO FLUIG (EDU.50.469)

* **[Ticket: EDUCACIONAL01-2889]** Alteração no lançamento a pagar gerado pelos fluxos de Inovação, Pesquisa e Exntesão para que tenham como origem o sistema Educacional.

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

## TOTVS Framework

### Rotina: CURRICULOS QUESTIONARIO CURRICULAR RHU 36 031

* **[Ticket: 1329610 / RHU01-1365]** Ajuste ao clicar no menu Questionario no Banco de Talentos

Arquivos: FrameHTML

## TOTVS Gestão Patrimonial

### Rotina: UTILITARIOS IMPORTACAO DE DADOS CONECTOR PAT 37 66

* **[Ticket: 1424944 / CONTROLADORIA01-626]** O processo de importação passou a alterar a coluna "Reavaliado" da visão de patrimônio. Desta forma é possível identificar que o patrimônio foi avaliado.

Arquivos: RM.Pat.Patrimonio.IService.dll, RM.Pat.Patrimonio.Service.dll, RM.Pat.PatrimonioMoeda.Service.dll, RM.Pat.Ocorrencia.Service.dll

## TOTVS Incorporação

### Rotina: REAJUSTE DE CM IMB 49 851

* **[Ticket: 1487840 / TINPAD001-1693]** Melhoria na distribuição do resíduo em todas as parcelas.

Arquivo: RM.Imb.Reajuste.Server.dll

# 12.1.15.197

## TOTVS Educacional

### Rotina: INTEGRACAO FLUIG EDU 50 469

* **[Ticket: 1474016 / EDUCACIONAL01-2728]** Ajuste no método que notifica coordenador do projeto pesquisa/extensão para o relatório parcial e final para que não ocorra erro de objeto nulo quando não existe uma conta de comunicação na integração com o fluig configurada, pois o mesmo não é necessário para o envio de e-mail, somente sendo necessário para a notificação no fluig.

Arquivos: RM.Edu.Interfaces.Intf.dll, RM.Edu.Academico.Server.dll, RM.Edu.PesquisaExtensao.Server.dll

### Rotina: INTEGRAÇÃO PROTHEUS (BACKOFFICE) (EDU.50.466)

* **[Ticket: EDUCACIONAL01-2969]** Alteração do sistema de origem nos lançamentos a pagar originados dos fluxos de auxílio externo e acompanhamento de bolsista para que registrem o código S do Educacional.

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E INCONSISTENCIA CTE 002

* **[Ticket: 1532112 / MATFATCMPCRM01-1570]** Melhoria para incluir o nome correto do documento eletrônico (CT-e ou CT-e OS) no arquivo XML salvo pelo botão salvar XML.

Arquivo: RM.Mov.CTe.Form.dll

* **[Ticket: 1532112 / MATFATCMPCRM01-1570]** Melhoria para copiar os campos dos Valores da Composição do Frete durante o processo de cópia a partir de outro movimento.

Arquivo: RM.Mov.Movimento.Service.dll

# 12.1.15.198

## TOTVS Construção e Projetos

### Rotina: HTML FRAMEWORK TIMESHEET APONTAMENTOS EM TAREFAS PRJ 33 996

* **[Ticket: 1050745 / TOPORCAPLAN001-1730]** Ajuste nas Permissões da Web para Timesheet, respeitado os campos da tela e tabela.

Arquivos: FrameHTML

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E PARAMETRIZACAO DE MOVIMENTO CTE 001

* **[Ticket: 1562565 / MATFATCMPCRM01-1638]** Melhoria na impressão do DACTEOS onde exitia a TAG ICMS90, mas não exisita Percentual de Redução da Base de Cálculo.

Arquivo: RM.Mov.Reports.Server.dll

### Rotina: CT E REJEICAO CTE 003

* **[Ticket: 1532261 / MATFATCMPCRM01-1564]** Melhorias no processo responsável pelo envio do CT-e OS.

Arquivo: RM.Mov.CTe.Service.dll

## TOTVS Gestão de Pessoas

### Rotina: GESTAO DE METAS

* **[Ticket: 1472717 / RHU01-1748]** Foi ajustado o tamanho dos campos 'nome' e 'quantidade de ocorrência' para respeitar o tamanho das colunas na tabela VGMETA e também ajustado o tamanho da coluna NOME na tabela para que caiba o resultado da concatenação dos campos 'nome', 'nome do funcionário' e 'quantidade de ocorrência' e mais 6 campos.

Arquivo: RM.Rhu.GestaoMetas.Form.dll

# 12.1.15.200

## TOTVS Automação de Ponto

### Rotina: PROCESSO DE CALCULO OCORRENCIA 0043 PTO 35 1280

* **[Ticket: 1281439 / PONTO01-1125]** Correção do cálculo para gerar as ocorrências corretamente

Arquivo: RM.Pto.Calculo.Service.dll

## TOTVS Business Connect

### Rotina: Ajuste na execução dos scripts de criação de base estágio do GoodData

* **[Ticket: FOPROTINAS01-2143]** Ajuste na execução de scripts de criação de base estágio do GoodData

Arquivo: RM.Con.ConfiguraIntegracao.Server.dll

### Rotina: GOODDATA

* **[Ticket: FOPROTINAS01-2107]** Ajustes em NOLOCK quando a tabela possui ALIAS

Arquivos: RM.Con.ConfiguraIntegracao.Server.dll, RM.Con.ConfiguraIntegracao.BackOfficeRMBI.dll

## TOTVS Controle de Infecção Hospitalar

### Rotina: BI TAXA DE CONSUMO DE ANTIBIOTICO SAUIH 55 614

* **[Ticket: 1448313 / RMFIN-361]** Correção no calculo do campo Tempo Total (dias) do BI - Consumo de Antibióticos para desconsiderar as devoluções como tempo de consumo

Arquivo: RM.SauIH.Estatisticos.Form.dll

* **[Ticket: 1435397 / RMFIN-360]** Foi realizado a alteração no formulário para que ao exportar os dados apresentados, seja exibido no arquivo de exportação a mesma relação de informação.

Arquivo: RM.SauIH.Estatisticos.Form.dll

## TOTVS Folha de Pagamento

### Rotina: FOLHA MENSAL ENTRADA DO MOVIMENTO LAB 01 110

* **[Ticket: 862970 / FOPCALCULO01-419]** Ajustes na geração do relatório de orçamento, Quadro de vagas, para considerar todas as seções cadastradas

Arquivo: RM.Fop.Orcamento.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E ENVIO DE EVENTO CTE 006

* **[Ticket: 1592991 / MATFATCMPCRM01-1804]** Alterado a tag "<compl>" (para minusculo) do grupo "grupoObsCont", do evento de carta de correção para o CT-e OS.

Arquivo: RM.Mov.CTe.Form.dll

### Rotina: CT E INCONSISTENCIA CTE 002

* **[Ticket: 1533000 / MATFATCMPCRM01-1567]** Melhorias na rotina responsável por salvar o XML do CT-e OS.

Arquivos: RM.Mov.Utils.Intf.dll, RM.Mov.CTe.Form.dll, RM.Mov.CTe.Service.dll

* **[Ticket: 1498646 / MATFATCMPCRM01-1689]** Melhorias no parametrizador de CT-e OS.

Arquivos: RM.Mov.Parametros.Intf.dll, RM.Mov.Parametros.Form.dll

* **[Ticket: 1532426 / MATFATCMPCRM01-1569]** Implementação do Monitor Sefaz para o CT-e OS

Arquivo: RM.Mov.CTe.Form.dll

### Rotina: CT E RELATORIO CTE 004

* **[Ticket: 1497484 / MATFATCMPCRM01-1481]** Melhoria para buscar corretamente o relatório Default para a impressão do DACTeOS

Arquivos: RM.Mov.CTe.Form.dll, RM.Mov.CTe.Service.dll

### Rotina: CT-E - ENVIO DE EVENTO (CTE.006)

* **[Ticket: MATFATCMPCRM01-1518]** Melhorias no processo de envio do CTeOS.

Arquivos: RM.Mov.CTe.Form.dll, RM.Mov.CTe.Service.dll, RM.Mov.CTe.IService.dll

## TOTVS Gestão de Pessoas

### Rotina: PESSOAS CAMPOS COMPLEMENTARES RHU 36 090

* **[Ticket: 928361 / RHU01-676]** Consertado campos complementares de clientes e fornecedores para aplicar o produto correto.

Arquivo: RM.Rhu.Server.dll

## TOTVS Gestão Fiscal

### Rotina: Análise Escrituração para CT-e OS

* **[Ticket: FISCAL01-1892]** O Lançamento Fiscal e Escrituração passa a reconhecer o documento fiscal modelo 67 CT-e OS como um CT-e modelo 57.

Arquivos: RM.Fis.LancFiscal.Form.dll, RM.Fis.EscrituracaoFiscal.Service.dll, RM.Fis.Utils.Intf.dll

### Rotina: CT E INCONSISTENCIA CTE 002

* **[Ticket: 1532426 / MATFATCMPCRM01-1569]** Implementação do Monitor Sefaz para o CT-e OS

Arquivos: RM.Fis.NFe.Form.dll, RM.Fis.NFe.Service.dll

### Rotina: ESCRITURACAO LI 01 0025

* **[Ticket: 1542735 / FISCAL01-2076]** Gerar os registros D100, D101, D105, D111, D200, D201, D205, D209 da EFD Contribuições para Documento Modelo 67 CT-e OS

Arquivos: RM.Fis.Sped.Server.dll, RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGACOES ACESSORIAS SPED FISCAL LI 01 0036

* **[Ticket: 1491564 / FISCAL01-1863]** Implementação do registro D100 do SPED Fiscal para aceitar o código de modelo de documento 67 - CONHECIMENTO DE TRANSPORTE ELETRÔNICO PARA OUTROS SERVIÇOS - CT-E OS

Arquivo: RM.Fis.Sped.Server.dll

## TOTVS Segurança e Medicina do Trabalho

### Rotina: Downgrade Issue RHU01-1679

* **[Ticket: RHU01-1950]** Downgrade da Issue RHU01-1679

Arquivo: RM.Smt.EPC.Server.dll

# 12.1.15.201

## TOTVS Controle de Infecção Hospitalar

### Rotina: IMP CULTURA FINAL SAUIH 55 622

* **[Ticket: 1374082 / RMFIN-785]** Ajuste realizado na importação de cultura final. O sistema estava passando por um array fora dos limites.

Arquivo: RM.SauIH.Importacao.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: PARAMETRIZACAO TIPO DE MOVIMENTO

* **[Ticket: MATFATCMPCRM01-90]** Acerto para seleção de tributo.

Arquivo: RM.Mov.Parametros.Form.dll

* **[Ticket: MATFATCMPCRM01-90]** Acerto para seleção de tributo.

Arquivo: RM.Mov.Parametros.Form.dll

## TOTVS Gestão de Pessoas

### Rotina: FUNCIONARIOS RHU 36 035

* **[Ticket: 1515737 / RHU01-1844]** Downgrade da issue RHU01-1175

Arquivo: RM.Rhu.Captacao.Data.dll

## TOTVS Processo Seletivo

### Rotina: Erro de E-mail - Local de Prova

* **[Ticket: 1738921 / EDUCACIONAL01-3269]** Ajuste no envio de e-mails para candidatos.

Arquivo: RM.EduPS.Processos.Data.dll

# 12.1.15.202

## TOTVS Construção e Projetos

### Rotina: CONTRATOS LIBERACAO ENVIAR PARA SUPRIMENTOS PRJ 33 995

* **[Ticket: 1831264 / TOPEXECONTROL01-1789]** go-Global - SmartClient - Contrato - Liberar PeríodoAs mensagens trafegadas pelo processo, serão repassadas para o servidor armazenar os valores do campo complementar.

Arquivos: RM.Prj.Utils.Intf.dll, RM.Prj.Contrato.Intf.dll

* **[Ticket: 1574964 / TOPEXECONTROL01-1552]** Ajuste no processo de liberar período para execução no GoGlobo.

Arquivo: RM.Prj.Contrato.Data.dll

## TOTVS Educacional

### Rotina: APURACAO DE RESULTADOS EDU 50 021

* **[Ticket: 756903 / EDUCACIONAL01-235]** Foi realizado um ajuste na fórmula BuscaCampoAvaliacao, para que o erro "Referência de objeto não definida para uma instância de um objeto." não ocorrece mais.

Arquivo: RM.Edu.Formula.dll

### Rotina: MUDAR TURMA EDU 50 314

* **[Ticket: 873943 / EDUCACIONAL01-3225]** Ajuste no processo de mudança de turma para que seja gravado no histórico da matrícula do período letivo do aluno o número do diário quando se retorna para a turma inicial.Foi ajustado também no processo de numeração do ensino básico para a gravação do log do Nº do aluno no histórico de matrícula do período letivo.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Services.Server.dll, RM.Edu.Matricula.Server.dll

* **[Ticket: 873943 / EDUCACIONAL01-3225]** Ajuste no processo de mudança de turma para que seja gravado no histórico da matrícula do período letivo do aluno o número do diário quando se retorna para a turma inicial.Foi ajustado também no processo de numeração do ensino básico para a gravação do log do Nº do aluno no histórico de matrícula do período letivo.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Matricula.Server.dll

### Rotina: PORTAL ALUNO MATRIZ CURRICULAR EDU 50 357

* **[Ticket: 750157 / PORTALMOBILE01-390]** Ao ser exibido o complemento da disciplina no menu Matriz Curricular do Ensino Básico, eram exibidos todos os complementos da disciplina de todos os cursos em que a disciplina fazia parte. Foi realizado o ajuste para exibir apenas o complemento da disciplina referente ao curso do aluno.

Arquivo: App\_Web\_edumatrizcurricularwebform.ascx.9bc05ab5.dll

### Rotina: PROCESSO SELETIVO TERCEIRIZADO EDU 50 394

* **[Ticket: 960662 / EDUCACIONAL01-1517]** Correção do processo de matricula pelo processo seletivo terceirizado, o sistema agora verifica se existe uma pessoa cadastrada no Gestão de Pessoas, de acordo com a regra de unicidade informada nos parâmetros de validação do Gestão Pessoa.

Arquivos: RM.Edu.Facade.Intf.dll, RM.Edu.ProcSel.Data.dll

* **[Ticket: 960662 / EDUCACIONAL01-1517]** Correção do cadastro de filiação pois estava invertendo o nome da mãe com o do pai.

Arquivo: RM.Edu.ProcSel.Data.dll

## TOTVS Gestão Contábil

### Rotina: CADASTRO DE EVENTO CONTABIL EVC 001

* **[Ticket: 1284307 / CONTROLADORIA01-747]** Melhoria no processo de Cópia de Evento Contábil para que caso o usuário marque a coligada corrente e não altere o número do evento seja mostrado mensagem falando que não é possível copiar o evento para mesma coligada sem mudar o número.

Arquivos: RM.Ctb.Processos.Intf.dll, RM.Ctb.Processos.Data.dll, RM.Ctb.Processos.Form.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: CT E REJEICAO CTE 003

* **[Ticket: 1532261 / MATFATCMPCRM01-1998]** Melhorias no processo responsável pelo envio do CT-e OS.

Arquivos: RM.Mov.Facade.dll, RM.Mov.CTe.Service.dll

# 12.1.15.203

## TOTVS Controle de Infecção Hospitalar

### Rotina: IMP CIRURGIA SAUIH 55 621

* **[Ticket: 1785333 / RMFIN-1042]** Ajuste realizado na importação de Cirurgias.

Arquivo: RM.SauIH.Importacao.Data.dll

## TOTVS Educacional

### Rotina: Ajuste de referência da DLL System.Net.Http.dll

* **[Ticket: PORTALMOBILE01-2966]** Ajuste de referência da dll System.Net.Http, conforme solicitado pela equipe de Engenharia.

Arquivo: RM.Edu.Integracoes.Server.dll

### Rotina: ANALISE CURRICULAR EDU 50 016

* **[Ticket: 1337679 / EDUCACIONAL01-2674]** Ajuste no diretório de armazenamento de arquivos de layout de telas.

Arquivos: RM.Edu.Consts.dll, RM.Edu.Aluno.Form.dll, RM.Edu.Matricula.Form.dll

### Rotina: CONTRATOS CONTABILIZACAO EDU 50 141

* **[Ticket: 1690188 / DEDUINTEGRACOES-1010]** Ajustes no preenchimento das tags na geração de lançamentos de parcelas.

Arquivo: RM.Edu.Financeiro.Server.dll

* **[Ticket: 1690188 / DEDUINTEGRACOES-1010]** Ajustes na montagem do histórico/complemento na geração de lançamentos contábeis e financeiros.

Arquivos: RM.Edu.Lib.Intf.dll, RM.Edu.Financeiro.Server.dll, RM.Edu.Contabil.Server.dll

### Rotina: INOVAÇÃO, PESQUISA E EXTENSÃO (EDU.51038)

* **[Ticket: EDUCACIONAL01-2330]** Foi realizado um ajuste no sistema, para que ele só verifique se uma bolsa já foi inserida, quando o usuário tentar realizar uma ação de inclusão.

Arquivo: RM.Edu.PesquisaExtensao.Data.dll

### Rotina: LOG DE MOVIMENTAÇÕES - PROFESSOR (EDU.50.291)

* **[Ticket: EDUCACIONAL01-2998]** Foi realizada uma otimização no processo de exclusão de professor.

Arquivo: RM.Edu.Professor.Data.dll

## TOTVS Framework Web

### Rotina: Ajustes GULP 12.1.15

* **[Ticket: PORTALMOBILE01-3576]** Nesse caso não faz sentido uma descrição para o suporte pois o erro acontece no momento do deploy da aplicação.

Arquivos: FrameHTML

## TOTVS Incorporação

### Rotina: RELATORIOS INCORPORACAO IMB 49 854

* **[Ticket: 1788329 / TINPAD001-1998]** Melhoria na ficha financeira para considerar apenas o último log da subunidade existente quando houver uma troca de subunidade via cadastro de venda, antes de efetivar a venda.

Arquivo: RM.Imb.Relatorio.Data.dll
