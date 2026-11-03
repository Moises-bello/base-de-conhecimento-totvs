---
content_hash: 1ec5df36cdd256418294cbc072b9e727130d93f4aadc2685702cf8ed38379904
fetched_at: '2026-06-29T00:10:04.662114+00:00'
page_id: '452719229'
product: rm
source: tdn-rm
title: Exclusão de Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719229
version: 7
---

O cadastro de funcionários é o primeiro procedimento realizado no momento da admissão. Por ser uma etapa inicial, sujeita a possíveis erros, o sistema permite a exclusão do cadastro do funcionário dentro de determinados critérios.

### Critérios para Exclusão

O processo de exclusão de funcionários possibilita que o usuário exclua um funcionário do cadastro, desde que:

* O funcionário tenha sido admitido no **mês atual**;
* Não possua nenhuma movimentação lançada na **Ficha Financeira**;
* A situação do funcionário seja:

  + **"A - Ativo"** com data de admissão dentro da competência atual; ou
  + **"Z - Admissão próximo mês"** com data de admissão maior ou igual à competência atual.

### Impacto da Exclusão

Ao processar a exclusão, o sistema irá remover os dados relacionados ao funcionário nas seguintes tabelas:

|  |  |  |
| --- | --- | --- |
| **TABELA** | **DESCRIÇÃO** | **PRODUTO** |
| AABONFUN | Cadastro de Abonos Lançados para os Funcionários | TOTVS Automação de Ponto |
| AABONFUNAM | Cadastro de Abonos em Períodos Anteriores | TOTVS Automação de Ponto |
| AABONFUTURO | Cadastro de Abonos em Períodos Futuros | TOTVS Automação de Ponto |
| AABONOFUNCIONARIO | Cadastro de Abonos Lançados para os Funcionários | TOTVS Automação de Ponto |
| ABATFUN | Batidas no Espelho de Ponto dos Funcionários | TOTVS Automação de Ponto |
| ABATFUNAM | Batidas de Pontos em Períodos Anteriores | TOTVS Automação de Ponto |
| ACRELFUN | Associação de Crachá (PFunc) e Grupo | TOTVS Automação de Ponto |
| AEAUTFUN | Autorização de Horas Extras | TOTVS Automação de Ponto |
| AEXCECAOCALCULO | Exceção do Cálculo | TOTVS Automação de Ponto |
| AEXPORTPONTOAPROVACAO | Exportação de Folhas de Ponto para Aprovação | TOTVS Automação de Ponto |
| AFLUXOSOBREAV | Justificativa para a solicitação do sobreaviso | TOTVS Automação de Ponto |
| AHISTPARCOLFUNC | Histórico de parâmetros coletivos do Funcionário | TOTVS Automação de Ponto |
| AHSTUTILIZAPONTO | Histórico de utilização de ponto do Funcionário | TOTVS Automação de Ponto |
| APARFUN | Parâmetros do Funcionário | TOTVS Automação de Ponto |
| ARECALCULOFUNCMEURH | Dados da execução do recálculo Meu RH | TOTVS Automação de Ponto |
| ASECVIS | Seções Visitadas | TOTVS Automação de Ponto |
| ATROCAFERIADO | Troca de feriado por funcionário | TOTVS Automação de Ponto |
| AVISITA | Visitantes | TOTVS Automação de Ponto |
| EPROFES | Cadastro de Professores | TOTVS Educacional |
| HATENDENTE | Cadastro de Atendentes | TOTVS Aprovação e Atendimento |
| IALOCACAOFUNCIONARIO | Alocação Funcionário | TOTVS Gestão Patrimonial |
| IINTEGRAAQUISICAO | Integra aquisição | TOTVS Gestão Patrimonial |
| IINVENTARIO | Inventário | TOTVS Gestão Patrimonial |
| ILOCAL | Localizações | TOTVS Gestão Patrimonial |
| IPATRIMONIO | Patrimônio | TOTVS Gestão Patrimonial |
| IPATRIMONIOALOCACAO | Patrimônio Alocação | TOTVS Gestão Patrimonial |
| IPATRIMONIOFUNCIONARIO | Patrimônio funcionário | TOTVS Gestão Patrimonial |
| IPATRIMONIOTRANSFERENCIA | Patrimônio transferência | TOTVS Gestão Patrimonial |
| MCNT | Contratos | TOTVS Obras e Projetos |
| MCNTSTATUSLOG | Log de Status de Contratos | TOTVS Obras e Projetos |
| MFOLHATAREFAMEMBRO | Membros da Folha Tarefa | TOTVS Obras e Projetos |
| MISMAPROP | Insumos Apropriados | TOTVS Obras e Projetos |
| MMAOOBRAPDO | Mão de obra alocada por período | TOTVS Obras e Projetos |
| MPRJ | Projetos | TOTVS Obras e Projetos |
| MPRJSTATUSLOG | Log de Status do Projeto | TOTVS Obras e Projetos |
| MPRODUTIVIDADEPAGAMENTOITEM | Dados do arquivo de pagamento por produtividade | TOTVS Obras e Projetos |
| OFATENDENTE | Atendentes | TOTVS Hospitais e Clínicas |
| OFATENDIMENTO | Atendimento | TOTVS Hospitais e Clínicas |
| OFATENDIMENTOEXTOS | Atendimentos do TOTVS Aprovação e Atendimento para Manutenção | TOTVS Hospitais e Clínicas |
| OFITMAPROPRIACAOPRD | Itens da apropriação direta de produtos | TOTVS Hospitais e Clínicas |
| PCHEFEEXTERNO | Chefe Externo | TOTVS Folha de Pagamento |
| PCOMISSAO | Comissão de Funcionários | TOTVS Folha de Pagamento |
| PCOMMUNICATECOLLABORATOR | Dados do comunicado Comunica RH por colaborador | TOTVS Folha de Pagamento |
| PCOMMUNICATEPUSH | Comunicados do Comunica RH | TOTVS Folha de Pagamento |
| PCONDICAODIFERENCIADATRABALHO | Condições Diferenciadas de Trabalho | TOTVS Folha de Pagamento |
| PDADOSRESCISAO | Dados de Rescisão | TOTVS Folha de Pagamento |
| PDADQUIOSQUE | Solicitação de Alteração de Dados Cadastro | TOTVS Folha de Pagamento |
| PDIRF | Tabela para geração do Informe de Rendimento | TOTVS Folha de Pagamento |
| PDIRFCOMPLEMENTO | Tabela para geração do Informe de Rendimento | TOTVS Folha de Pagamento |
| PDIRSPT | Tabela de declaração IRS (Portugal) | TOTVS Folha de Pagamento |
| PESTABILIDADE | Estabilidade do Funcionário | TOTVS Folha de Pagamento |
| PEVTRELACSALCMPCC | Eventos relacionados a Salário Composto por Centro de Custo | TOTVS Folha de Pagamento |
| PFAAS | Tabela Aas do Funcionário | TOTVS Folha de Pagamento |
| PFADICFER | Eventos Adicionais de Férias | TOTVS Folha de Pagamento |
| PFATIVREMUNERADA | Atividades Remuneradas | TOTVS Folha de Pagamento |
| PFATIVREMUNERADACC | Atividades Remuneradas por Centro de Custo | TOTVS Folha de Pagamento |
| PFAVISO | Avisos do Funcionário | TOTVS Folha de Pagamento |
| PFBENEFICIO | Benefícios do Funcionário | TOTVS Folha de Pagamento |
| PFBENEFICIOSUSPENSAO | Suspensão/Término dos Benefícios do Funcionário | TOTVS Folha de Pagamento |
| PFCODFIX | Código Fixo do Funcionário | TOTVS Folha de Pagamento |
| PFCOMPL | Campos complementares do Funcionário | TOTVS Folha de Pagamento |
| PFCONSIGNADODISTMARGEM | Anexo de distribuição de margem consignável do funcionário | TOTVS Folha de Pagamento |
| PFCONVOCACAO | Convocação de Funcionário | TOTVS Folha de Pagamento |
| PFDEPEND | Dependentes do Funcionário | TOTVS Folha de Pagamento |
| PFDEPENDCOMPL | Campos Complementares de Dependentes | TOTVS Folha de Pagamento |
| PFDEPEVENTOS | Eventos que não Entram Pensão por Dependente | TOTVS Folha de Pagamento |
| PFEMPRT | Empréstimos do Funcionário | TOTVS Folha de Pagamento |
| PFENCARGO | Histórico de Encargos | TOTVS Folha de Pagamento |
| PFENCCC | Histórico Encargos por Centro de Custo | TOTVS Folha de Pagamento |
| PFESOCIALCPF | Tabela de Alteração CPF para eSocial | TOTVS Folha de Pagamento |
| PFEVENTOSPROG | Eventos Programados para o Funcionário | TOTVS Folha de Pagamento |
| PFFERPROG | Férias Programadas | TOTVS Folha de Pagamento |
| PFFERRESCTRCT | Valores de férias na rescisão | TOTVS Folha de Pagamento |
| PFHSTAFT | Histórico de Afastamento do Funcionário | TOTVS Folha de Pagamento |
| PFHSTASSMED | Histórico assist. médica dos dependentes | TOTVS Folha de Pagamento |
| PFHSTASSMEDCOPART | Detalhamento do Pagamento referente a coparticipação | TOTVS Folha de Pagamento |
| PFHSTBEM | Histórico da Adesão ao Benefício Extraordinário Mensal B.E.M | TOTVS Folha de Pagamento |
| PFHSTCATEGORIAESOCIAL | Histórico da Categoria eSocial | TOTVS Folha de Pagamento |
| PFHSTCODRECEBIMENTO | Histórico de Tipo de Recebimento | TOTVS Folha de Pagamento |
| PFHSTCODTIPOFUNCIONARIO | Histórico de Tipo de Funcionário | TOTVS Folha de Pagamento |
| PFHSTCOMPRAVT | Histórico de Compra de Vale Transporte | TOTVS Folha de Pagamento |
| PFHSTCPGTO | Dados bancários do funcionário | TOTVS Folha de Pagamento |
| PFHSTCSD | Histórico de contribuição sindical | TOTVS Folha de Pagamento |
| PFHSTESTATUTARIO | Histórico do Estatutário | TOTVS Folha de Pagamento |
| PFHSTFALTA | Histórico de Faltas | TOTVS Folha de Pagamento |
| PFHSTFCO | Histórico de Função | TOTVS Folha de Pagamento |
| PFHSTFER\_OLD | Usuário criador do registro | TOTVS Folha de Pagamento |
| PFHSTHOR | Histórico de Horários | TOTVS Folha de Pagamento |
| PFHSTINDSIMPLES | Histórico de Indicador de Contribuição Substituída | TOTVS Folha de Pagamento |
| PFHSTNDP | Histórico do Nº de Dependentes | TOTVS Folha de Pagamento |
| PFHSTOCORRENCIATRABRURAL | Histórico de Ocorrências do trabalhador Rural | TOTVS Folha de Pagamento |
| PFHSTPROV | Histórico de Provisões | TOTVS Folha de Pagamento |
| PFHSTPROVABAT | Histórico Provisão Abatimento | TOTVS Folha de Pagamento |
| PFHSTPROVABATMESCC | Histórico Provisão Abatimento Por Centro de Custo | TOTVS Folha de Pagamento |
| PFHSTPROVFORMULA | Histórico Provisão Fórmula | TOTVS Folha de Pagamento |
| PFHSTPROVFORMULAMESCC | Histórico Provisão Fórmula Por Centro de Custo / Mês | TOTVS Folha de Pagamento |
| PFHSTPROVMESCC | Histórico Provisão Centro de Custo Por Mês | TOTVS Folha de Pagamento |
| PFHSTRATEIOTOMADOR | Histórico do Rateio de Tomador | TOTVS Folha de Pagamento |
| PFHSTRRA | Histórico Rendimentos Recebidos Acumuladamente | TOTVS Folha de Pagamento |
| PFHSTRRAADVOGADOS | Histórico Rendimentos Recebidos Acumuladamente Advogados | TOTVS Folha de Pagamento |
| PFHSTSAL | Histórico de Salários | TOTVS Folha de Pagamento |
| PFHSTSALFUT | Histórico Salarial Futuro | TOTVS Folha de Pagamento |
| PFHSTSEC | Histórico de Seção | TOTVS Folha de Pagamento |
| PFHSTSIT | Histórico de Situação | TOTVS Folha de Pagamento |
| PFHSTTIPOREGIMEJORNADA | Histórico do Tipo de Regime da Jornada | TOTVS Folha de Pagamento |
| PFHSTUTILIZAPONTOAHGORA | Controla qual funcionário usa ou usou ponto Ahgora | TOTVS Folha de Pagamento |
| PFITEMLAN | Itens Lançamentos Financeiros por Funcionário | TOTVS Folha de Pagamento |
| PFMEDCALCEVT | Valor da média por evento | TOTVS Folha de Pagamento |
| PFMEDCALCEVTMES | Valor por mês da Ficha Financeira por evento | TOTVS Folha de Pagamento |
| PFMEDCALCGRUPO | Valor da média por grupo | TOTVS Folha de Pagamento |
| PFMEDIACALCULO | Valor total da média | TOTVS Folha de Pagamento |
| PFMOVCONVENIO | Movimentação do Convênio | TOTVS Folha de Pagamento |
| PFMOVENSINO | Movimento de Ensino | TOTVS Folha de Pagamento |
| PFMOVENSINOIMP | Imp. Movimento de Ensino de Terceiros | TOTVS Folha de Pagamento |
| PFMOVENSINOIMPRESILICAO | Movimento de Ensino Importado da Resilição | TOTVS Folha de Pagamento |
| PFMOVFGTS | Movimentação FGTS | TOTVS Folha de Pagamento |
| PFMOVTEMP | Movimentação temp. da folha de pagamento | TOTVS Folha de Pagamento |
| PFMOVTOMADOR | Movimentação por Tomador de Serviço | TOTVS Folha de Pagamento |
| PFMULTVINCULOSEXTERNO | Informação de Múltiplos Vínculo | TOTVS Folha de Pagamento |
| PFPERFER\_OLD | Usuário criador do registro | TOTVS Folha de Pagamento |
| PFPERFF | Ficha Financeira - Períodos | TOTVS Folha de Pagamento |
| PFPERFFCOMPL | Ficha Financeira - Períodos (Compl.) | TOTVS Folha de Pagamento |
| PFPRECISARECALCULOMV | Pendências de Recálculo para funcionários Múltiplos Vínculos | TOTVS Folha de Pagamento |
| PFPROCESSOSJUDICIAIS | Processos judiciais do trabalhador quanto à não incidência de contribuição previdenciária e/ou Imposto de Renda | TOTVS Folha de Pagamento |
| PFRATEIOFIXO | Rateio Fixo por Funcionário | TOTVS Folha de Pagamento |
| PFRATEIOTOMADOR | Rateio do Funcionário por Tomador de Serviço | TOTVS Folha de Pagamento |
| PFREEMBOLSOOPERADORA | Reembolso da Operadora de Saúde | TOTVS Folha de Pagamento |
| PFREEMBOLSOOPERADORAMENSAL | Valores do reembolso da Operadora de Saúde mensal | TOTVS Folha de Pagamento |
| PFREMBASE | Cálculo da remuneração base de Professor | TOTVS Folha de Pagamento |
| PFREMCREDTRAB | Eventos da remuneração do funcionário para margem consignável do crédito ao trabalhador | TOTVS Folha de Pagamento |
| PFRESCDESBLOQUEADA | Rescisão Desbloqueada | TOTVS Folha de Pagamento |
| PFRESILICAO | Dados da Resilição | TOTVS Folha de Pagamento |
| PFSALCMP | Salários Compostos | TOTVS Folha de Pagamento |
| PFSALCMPCC | Salários Compostos por Centro de Custo | TOTVS Folha de Pagamento |
| PFSUBSTITUICAO | Controle de Substituição do Funcionário | TOTVS Folha de Pagamento |
| PFUFERIAS | Períodos Aquisitivos de Férias | TOTVS Folha de Pagamento |
| PFUFERIASPER | Dados dos períodos de gozo das férias | TOTVS Folha de Pagamento |
| PFUNCOBSERVACAO | Tabela de Observações Contratuais do Funcionário | TOTVS Folha de Pagamento |
| PFUNCPRELIMINAR | Tabela de registro preliminar de Funcionário | TOTVS Folha de Pagamento |
| PFUNCPT | Funcionários (Portugal) | TOTVS Folha de Pagamento |
| PFUNCVAL | Valores associados | TOTVS Folha de Pagamento |
| PFVALETR | Vale Transporte - Funcionários | TOTVS Folha de Pagamento |
| PFVALORFORCADO | Valor Forçado da Ficha Financeira | TOTVS Folha de Pagamento |
| PGPSLIMINAR | Informações para gerar GPS Liminar | TOTVS Folha de Pagamento |
| PGPSLOGCALCDETALHE | Memória de Cálculo da GPS - Detalhamento | TOTVS Folha de Pagamento |
| PHSTOCORRENCIA | Histórico de Alteração de Ocorrências | TOTVS Folha de Pagamento |
| PHSTPRODUCAOAGRARIA | Histórico de de produção Agrária | TOTVS Folha de Pagamento |
| PINTEGRACAOENVIOAHGORA | Registra requisições que serão ou foram enviadas para Ahgora | TOTVS Folha de Pagamento |
| PITEMPARTIDA | Tabela de Itens da Partida | TOTVS Folha de Pagamento |
| PITEMRATEIOLC | Tabela de Itens do Rateio da Partida | TOTVS Folha de Pagamento |
| PLOGFUNCIONARIO | Log de Cálculo do funcionário | TOTVS Folha de Pagamento |
| PORCAMENTOLOTACAOFUNC | Funcionários da lotação | TOTVS Folha de Pagamento |
| PPRODUCAOAGRARIA | Produção Agrária | TOTVS Folha de Pagamento |
| PSIMULADEMISSAO | Simulação Demissão Passivo Trabalhista | TOTVS Folha de Pagamento |
| PSUBSTCHEFE | Cadastro de Chefe/Supervisores | TOTVS Folha de Pagamento |
| PSUBSTSUP | Cadastro de Chefe/Supervisores | TOTVS Folha de Pagamento |
| PSUPERVEXTERNO | Cadastro de Chefe/Supervisores | TOTVS Folha de Pagamento |
| PTMOVFUNC | Movimentação Gerada - Funcionário 2 | TOTVS Folha de Pagamento |
| SBOLSAALUNO | Bolsas do Aluno | TOTVS Educacional |
| SPROFESSOR | Professor | TOTVS Educacional |
| SPROFESSORFILIAL | Filiais do professor | TOTVS Educacional |
| SPSINSCRICAOANONIMA | Inscrição anônima | TOTVS Educacional |
| SPSINSCRICAOAREAOFERTADA | Inscrição | TOTVS Educacional |
| SPSPROFISSIONAL | Profissional | TOTVS Educacional |
| TITMMOV | Itens de Movimento | TOTVS Gestão Estoque, Compras e Faturamento |
| TMOV | Movimentos | TOTVS Gestão Estoque, Compras e Faturamento |
| VACOMPANHAMENTOMETA | Acompanhamento das metas por funcionário/seção | TOTVS Gestão de Pessoas |
| VADFATORORGAVALIADO | Fatores organizacionais avaliados | TOTVS Gestão de Pessoas |
| VADFEEDBACK | Feedback da Avaliação de Desempenho | TOTVS Gestão de Pessoas |
| VADGESTAOMETASAVALIADAS | Metas avaliadas da avaliação de desempenho | TOTVS Gestão de Pessoas |
| VADMETAS | Tabela de Metas avaliadas | TOTVS Gestão de Pessoas |
| VADNOTATOTAL | Nota total da Avaliação de Desempenho | TOTVS Gestão de Pessoas |
| VADPARTICIPANTES | Cadastro avaliados e avaliadores | TOTVS Gestão de Pessoas |
| VADPESOTIPOAVALIADOR | Tabela de pesos por tipo de avaliador | TOTVS Gestão de Pessoas |
| VADVERTENCIA | Advertências | TOTVS Gestão de Pessoas |
| VAGENDAEXAM | Agenda de Exames | TOTVS Gestão de Pessoas |
| VALTDADFUNCPROG | Tabela com os dados de uma requisição de Alteração de Dados Funcionais Progressivo | TOTVS Gestão de Pessoas |
| VATRIBUICOESMETAS | Atribuições das Metas | TOTVS Gestão de Pessoas |
| VBENEFCARTAO | Cartão de identificação do benefício para o Funcionário e seus dependentes | TOTVS Gestão de Pessoas |
| VBENEFDEPEND | Benefício por dependente | TOTVS Gestão de Pessoas |
| VBENEFFUNC | Benefícios dos Funcionários | TOTVS Gestão de Pessoas |
| VBENEFVINCDEPEND | Benefícios p/ os dependente do Funcionário | TOTVS Gestão de Pessoas |
| VBENEFVINCFUNC | Histórico do Benefício por cargo | TOTVS Gestão de Pessoas |
| VBIBRIGADISTA | Brigadista da brigada de incêndio | TOTVS Gestão de Pessoas |
| VCANDIDATOSCIPA | Candidatos de Eleições da Cipa | TOTVS Gestão de Pessoas |
| VCHAPAATESTADO | Funcionários Beneficiados com Atestado | TOTVS Gestão de Pessoas |
| VCONSULTASPRONT | Consultas Clínicas | TOTVS Gestão de Pessoas |
| VCONTROLESISTEMA | Controle do Sistema | TOTVS Gestão de Pessoas |
| VCURSOSPESSOAIS | Cursos de Interesses dos Funcionários | TOTVS Gestão de Pessoas |
| VDISTRVERBATREINA | Distribuição Gerenciamento Verbas Treinamento | TOTVS Gestão de Pessoas |
| VEXAMESPEND | Exames pendentes da pessoa | TOTVS Gestão de Pessoas |
| VFECHAMENTOMETA | Fechamento do plano de metas | TOTVS Gestão de Pessoas |
| VFLUXOREQPROMOCAO | Fluxo da Requisição de Promoção | TOTVS Gestão de Pessoas |
| VFUNCIONARIO | Funcionário | TOTVS Gestão de Pessoas |
| VFUNCNVINC | Vínculo de Funcionário a Tomadores de Serviço | TOTVS Gestão de Pessoas |
| VGMETAATRIBUICAO | Tabela de atribuição de Metas | TOTVS Gestão de Pessoas |
| VGRUPOAVALIACAO | Grupo de Avaliação | TOTVS Gestão de Pessoas |
| VHIERARQUIACOLIGADAEXTERNA | Pessoa externa vinculada a Hierarquia | TOTVS Gestão de Pessoas |
| VHISTBENEFDEPEND | Histórico do Benefício por dependente | TOTVS Gestão de Pessoas |
| VHISTBENEFFUNC | Histórico do Benefício por funcionário | TOTVS Gestão de Pessoas |
| VHISTBENEFVINCDEPEND | Histórico Benefícios para os dependentes do Funcionário | TOTVS Gestão de Pessoas |
| VHISTBENEFVINCFUNC | Histórico do Benefício por cargo | TOTVS Gestão de Pessoas |
| VHISTPOSICAO | Histórico da Posição | TOTVS Gestão de Pessoas |
| VHISTPOSTOPFUNC | Histórico das funções do posto | TOTVS Gestão de Pessoas |
| VHLIDER | Líderes de posição de gestões de Hierarquia | TOTVS Gestão de Pessoas |
| VHTIMEPARTICIPANTE | Participantes de times de gestões de Hierarquia | TOTVS Gestão de Pessoas |
| VINFOEXPRISCOOBS | Observações complementares referentes a registros ambientais | TOTVS Gestão de Pessoas |
| VLNTPESSOASCOMP | Guarda o resultado da LNT por Competência | TOTVS Gestão de Pessoas |
| VLNTPESSOASREQACESSO | Tabela com resultado de LNT por requisito de acesso | TOTVS Gestão de Pessoas |
| VMAPACONHECIMENTOCOMPETENCIA | Tabela que armazena as definições de mapa de conhecimento por Competência | TOTVS Gestão de Pessoas |
| VMAPACONHECIMENTOREQACESSO | Tabela que armazenará as definições de mapa de conhecimento por requisito de acesso | TOTVS Gestão de Pessoas |
| VMAPAFUNCAOFUNC | Mapas da Função associados ao Funcionário | TOTVS Gestão de Pessoas |
| VMEDICAMENTOMOVIMENTO | Movimento de Medicamento | TOTVS Gestão de Pessoas |
| VMEMBROSGRUPOAVALIACAO | Membros do Grupo de Avaliação | TOTVS Gestão de Pessoas |
| VMETASVINCULADAS | Metas vinculadas | TOTVS Gestão de Pessoas |
| VMOVFUNC | Movimento/Eventos Funcionários | TOTVS Gestão de Pessoas |
| VOCORRENCIA | Ocorrência | TOTVS Gestão de Pessoas |
| VPARTICIPANTES | Participantes da Cipa | TOTVS Gestão de Pessoas |
| VPDIPARTICIPANTE | Guarda os participantes de um PDI | TOTVS Gestão de Pessoas |
| VPDISUGESTAO | Armazena as sugestões de ação em um PDI | TOTVS Gestão de Pessoas |
| VPERFILEXAMEFUNC | Código da coligada | TOTVS Gestão de Pessoas |
| VPESSOASINSCTURMA | Pessoas inscritas na turma | TOTVS Gestão de Pessoas |
| VPFUNCPRESTSERVTERCEIROS | Criação da tabela VPFUNCPRESTSERVTERCEIROS. | TOTVS Gestão de Pessoas |
| VPLANOMETAS | Plano de metas | TOTVS Gestão de Pessoas |
| VPOSICAO | Tabela VPOSICAO. Posição da Hierarquia | TOTVS Gestão de Pessoas |
| VPOSTOSFUNC | Posto de Trabalho por Funcionário | TOTVS Gestão de Pessoas |
| VPPRAMEDICOES | Medições do risco | TOTVS Gestão de Pessoas |
| VQUADHIERARQUIA | Hierarquia dos Quadrantes | TOTVS Gestão de Pessoas |
| VQUADRANTEREVISOR | Revisores | TOTVS Gestão de Pessoas |
| VQUADRESPOSTA | Respostas | TOTVS Gestão de Pessoas |
| VQUADRESULTADO | Resultados | TOTVS Gestão de Pessoas |
| VRANKFUNCIONAL | Rank Funcional | TOTVS Gestão de Pessoas |
| VRECRUTAMENTO | Pessoas em Processo de Recrutamento | TOTVS Gestão de Pessoas |
| VREPRESENTANTEEMPREGADO | Tabela de representantes de empregado | TOTVS Gestão de Pessoas |
| VREQABERTTURMA | Requisição Abertura de Turma | TOTVS Gestão de Pessoas |
| VREQABERTTURMAPARECER | Pareceres de Requisições abertura | TOTVS Gestão de Pessoas |
| VREQAUMENTOQUADRO | Requisição de aumento de quadro | TOTVS Gestão de Pessoas |
| VREQAUMENTOQUADROPARECER | Pareceres da requisição de aumento de quadro | TOTVS Gestão de Pessoas |
| VREQBENEFICIO | Requisição de Benefícios | TOTVS Gestão de Pessoas |
| VREQCARGAREQUISITOS | Requisição de Carga de Requisitos | TOTVS Gestão de Pessoas |
| VREQDESLIGAMENTO | Tabela de Desligamento | TOTVS Gestão de Pessoas |
| VREQGERAL | Requisição Geral | TOTVS Gestão de Pessoas |
| VREQPROMOCAO | Tabela de Requisição de Promoção | TOTVS Gestão de Pessoas |
| VREQSUBSTITUICAO | Tabela de substituição | TOTVS Gestão de Pessoas |
| VREQTRANSFERENCIA | Tabela de Requisição de transferência | TOTVS Gestão de Pessoas |
| VREQTRANSFLOTE | Requisição de Transferência em Lote | TOTVS Gestão de Pessoas |
| VREQTRANSFLOTEFUNC | Funcionários (itens) da requisição de transferência em Lote | TOTVS Gestão de Pessoas |
| VREQTRANSFLOTEPARECER | Pareceres da requisição de transferência em Lote | TOTVS Gestão de Pessoas |
| VREQTRANSFPROMOCAO | Requisição de Transferência com Promoção | TOTVS Gestão de Pessoas |
| VREQTRANSFPROMOCAOPARECER | Pareceres da Requisição de transferência com  promoção | TOTVS Gestão de Pessoas |
| VREQTREINAMENTO | Requisição de Treinamento | TOTVS Gestão de Pessoas |
| VREQTREINAMENTOFUNCIND | Participantes Indicados para Treinamento | TOTVS Gestão de Pessoas |
| VRSSOLICITACOES | Tabela de solicitações | TOTVS Gestão de Pessoas |
| VSUBSTITUICAO | Define um substituto para uma hierarquia ou posição. | TOTVS Gestão de Pessoas |
| VTAREFAPESSOAL | Tarefas Pessoais | TOTVS Gestão de Pessoas |
| VTOMADORSERVICOVINC | Vínculo de Funcionário a Tomadores de Serviço | TOTVS Gestão de Pessoas |
| VTRANSFALTDADFUNCPROG | Tabela com os dados de uma requisição de Transferência com Alteração de Dados Funcionais Progressivo | TOTVS Gestão de Pessoas |
| VVOTACAOCIPA | Histórico de funcionários que votaram. | TOTVS Gestão de Pessoas |
| XCOMISSOESITEM | Tabela dos itens das Comissões Geradas | TOTVS Gestão de Imóveis |
| XVENDEDOR | Campo para definição do vendedor principal da venda. | TOTVS Gestão de Imóveis |

### ⚠️ ATENÇÃO I:

Caso exista alguma outra tabela relacionada ao funcionário a ser excluído, o sistema apresentará uma mensagem no log e **interromperá o processo**, para que o usuário realize a **exclusão manual do relacionamento**.

Ao processar a exclusão, o sistema armazenará alguns dados do funcionário excluído. Isso é necessário porque a **ficha de registro é sequencial**, e, para que **não haja lacunas** na numeração — o que poderia gerar questionamentos por parte da fiscalização trabalhista —, os dados excluídos serão mantidos em uma tabela de controle.

Essas informações serão armazenadas na tabela **PFUNCEXCLUIDO**.

### ⚠️ ATENÇÃO II:

Ao excluir um funcionário, será automaticamente gerado o **Evento de Exclusão (S-3000)** para o **eSocial**. Link Evento de Exclusão (S-3000).  
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
