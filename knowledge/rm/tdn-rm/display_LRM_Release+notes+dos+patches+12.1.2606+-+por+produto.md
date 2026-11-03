---
content_hash: 0abc8f58d435997eb4b0cd8d56df6d3ecf354f0ec6929384c2c3277b1551eacc
fetched_at: '2026-06-29T00:05:54.733017+00:00'
page_id: '1082540342'
product: rm
source: tdn-rm
title: Release notes dos patches 12.1.2606 - por produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Release+notes+dos+patches+12.1.2606+-+por+produto
version: 2
---

|  |
| --- |
| Esses são todos os patches gerados, porém nem todos estão disponíveis para todos os clientes. |

---

  
  

1square

---

  
  

# TOTVS Worknow

## 12.1.2606.100

### Rotina: Ãbaris

* **[Ticket: WN-42466]** InclusÃ£o de informaÃ§Ãµes adicionais na geraÃ§Ã£o do json.

Arquivo: Wnw/worknow

* **[Ticket: WN-42466]** InclusÃ£o do id de dados do registro do diploma digital.

Arquivo: Wnw/worknow

* **[Ticket: WN-42466]** Melhorias na geraÃ§Ã£o de informaÃ§Ãµes do json para o Ãbaris.

Arquivo: Wnw/worknow

* **[Ticket: WN-42466]** Melhorias na geraÃ§Ã£o do json enviado para o Ãbaris.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-43241]** Ajuste no processo de integraÃ§Ã£o de professores ao utilizar o parÃ¢metro complementar Email do Moodle.

Arquivo: Wnw/worknow

* **[Ticket: WN-29384]** Nova opÃ§Ã£o para manter a data original da turma disciplina na criaÃ§Ã£o e atualizaÃ§Ã£o de cursos, ignorando os parÃ¢metros de dias antes e depois.

Arquivo: Wnw/worknow

### Rotina: Plataforma A

* **[Ticket: WN-43247]** Ajuste na consulta SQL para validar NULL corretamente.

Arquivo: Wnw/worknow

* **[Ticket: WN-32421]** Ajuste na integraÃ§Ã£o para enviar as datas da Grade Curricular corretamente ou nulas.

Arquivo: Wnw/worknow

### Rotina: MS Teams

* **[Ticket: WN-42908]** Ajuste no processo de atualizaÃ§Ã£o de senha no AD.

Arquivo: Wnw/worknow

### Rotina: Sharepoint

* **[Ticket: WN-42096]** Corrigido vÃ­nculo de anexos em movimentos para validar o mÃ³dulo de origem.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-42723]** Melhoria no log e geraÃ§Ã£o de relatÃ³rios via integraÃ§Ã£o.

Arquivo: Wnw/worknow

* **[Ticket: WN-43193]** CriaÃ§Ã£o das colunas AÃ§Ã£o e Id. AÃ§Ã£o na resposta da FÃ³rmula Visual.

Arquivo: Wnw/worknow

### Rotina: Canvas

* **[Ticket: WN-43083]** Ajuste no processo de remoÃ§Ã£o de alunos.

Arquivo: Wnw/worknow

### Rotina: D2L

* **[Ticket: WN-42683]** Ajuste no processo de integraÃ§Ã£o de notas.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste rotina inativaÃ§Ã£o e ativaÃ§Ã£o de aluno. Vinculo de professor e criaÃ§Ã£o de termos

Arquivo: Wnw/worknow

### Rotina: Sem Rotina Específica

* Adicionado previous\_response\_id OpenIA

Arquivo: Wnw/worknow

# TOTVS Automação de Ponto

## 12.1.2606.100

### Rotina: IMPORTAÇÃO DE BATIDAS

* **[Ticket: DRHJORNRM-9952]** Melhoria no processo de importação de batidas

Arquivos: RM.Pto.Batida.Data.dll; RM.Pto.ImportacaoExportacao.Data.dll

### Rotina: TIPOS DE OCORRÊNCIA

* **[Ticket: 28834300 / DRHJORNRM-9928]** Adequação no totalizador do saldo de banco de horas que estava triplicando o valor do saldo no espelho de ponto quando existe lançamento de ocorrência customizada.

Arquivo: RM.Pto.Ocorrencia.Data.dll

# TOTVS Business Connect

## 12.1.2606.100

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-5188]** Corrigido filtro do Sync para o ForceReload e Carga Inicial

Arquivo: RM.Con.SmartLink.Service.dll

# TOTVS Construção e Projetos

## 12.1.2606.100

### Rotina: ANÁLISE DE VALOR AGREGADO

* **[Ticket: 28170188 / TOPEXECONTROL01-31121]** Ajuste no processo de gerar Análise do Valor Agregado

Arquivo: RM.Prj.AnaliseDeValorAgregado.Data.dll

### Rotina: APP MINHA OBRA

* **[Ticket: TOPEXECONTROL01-30763]** Sincronismo dos Dados do funcionário.

Arquivos: RM.Prj.Mobilidade.Intf.dll; RM.Prj.Api.dll; RM.Prj.Mobilidade.Server.dll

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: TOPORCAPLAN001-30691]** Ajuste no realinhamento de itens de contrato para salvar o valor realinhado que deve ser considerado no cálculo.

Arquivos: RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.Contrato.IServer.dll

### Rotina: MINHAS INSPEÇÕES

* **[Ticket: TOPORCAPLAN001-30653]** melhorias rotemaento e testes no TS 12.1.2606

Arquivo: Prj/portaldaobra

### Rotina: REVISÃO MÚLTIPLA

* **[Ticket: TOPORCAPLAN001-30059]** Nova opção de calculo por saldo de tarefas considerando apenas apropriado travado e previsto liberado.

Arquivos: RM.Prj.Parametros.Intf.dll; RM.Prj.Calculo.Server.dll; RM.Prj.Cronograma.Data.dll; RM.Prj.Parametros.Form.dll; RM.Prj.Cronograma.Intf.dll; RM.Prj.Cronograma.Server.dll; RM.Prj.Parametros.Data.dll

# TOTVS Educacional

## 12.1.2606.100

### Rotina: Sem Rotina Específica

* **[Ticket: DEDUSAGA-10732]** alteração no metodo que valida o usuario no hub

Arquivo: RM.Edu.API.dll

* **[Ticket: DEDUSAGA-10732]** Remoção de propriedade defensiva referente a tag EnableRealtime.

Arquivo: RM.Edu.API.dll

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: 29058691 / DEDUBOPE-12019]** Refatorado campo 180 do Registro 10 do Censo Básico para permitir a seleção de valores corretos

Arquivos: RM.Edu.Consts.dll; RM.Edu.Cadastros.Form.dll; RM.Edu.Cadastros.Intf.dll

* **[Ticket: 28865558 / DEDUBOPE-12040]** Otimização nas rotinas do Censo Básico

Arquivos: RM.Edu.Academico.Server.dll; RM.Edu.PeriodoLetivo.Intf.dll; RM.Edu.Consts.dll; RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.PeriodoLetivo.Server.dll

### Rotina: CENTRAL DE COMUNICAÇÕES

* **[Ticket: 27892812 / DEDUCAPCOM-10584]** Ajuste na exibição de categorias do eduCONNECT no Perfil de UsuárioCorrigido o componente de exibição das categorias do eduCONNECT, localizado nas parametrizações do Educacional (cadastro do perfil de usuário, aba "Central de Comunicação"). O ajuste garante que a listagem não seja cortada para clientes que possuem mais de 20 categorias cadastradas.

Arquivo: RM.Edu.Parametros.Form.dll

* **[Ticket: 26835583 / DEDUCAPCOM-10513]** Ajustes para evitar emails duplicados durante a rotina de notificação de boleto proximo ao vencimento

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUBOPE-12059]** Melhorias de performance e segurança

Arquivos: RM.Edu.RDStation.Marketing.SmartLink.Server.dll; RM.Edu.RDStation.Marketing.SmartLink.Intf.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Matricula.Server.dll

### Rotina: DESCONTO POR ANTECIPAÇÃO

* **[Ticket: 28350849 / DEDUPACMEN-9023]** Ajuste no web server de cadastro de bolsa do aluno para recuperar o valor da ordem do desconto por antecipação da bolsa caso não seja informado. Ajuste para adicionar os campos Aplica desconto por antecipação e Afeta base de cálculo na fórmula visual de inclusão de bolsa do aluno

Arquivos: RM.Edu.Financeiro.Server.dll; RM.Edu.Financeiro.Data.dll; RM.Edu.WFCore.Runtime.dll; RM.Edu.Workflow.Activities.dll

### Rotina: ESTRUTURA CURRICULAR/ESTRUTURA DE OFERTA

* **[Ticket: 29318320 / DEDUBOPE-12092]** Inclusão da opção de não enviar carga horária para o Censo.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: MATRICULAR PROCESSO SELETIVO RM

* **[Ticket: DEDUCAPCOM-10882]** Realizado ajuste para considerar apenas registros válidos, evitando inconsistências durante a gravação das habilitações dos alunos.

Arquivo: RM.Edu.Facade.dll

### Rotina: NOTAS E FALTAS DE AVALIAÇÃO

* **[Ticket: 29097450 / DEDUSAGA-11052]** Ajuste para manter as permissões do usuário logado atualizadas.

Arquivo: Edu/portaldoprofessor

### Rotina: OCORRÊNCIAS

* **[Ticket: 29098225 / DEDUSAGA-11053]** Ajuste de responsividade na tabela de ocorrências de alunos

Arquivo: Edu/portaldoprofessor

### Rotina: PAGAMENTO TOTVS TPC

* **[Ticket: DEDUPACMEN-8961]** Criação de permissão de acesso para usuários de serviço utilizarem a API de criação de recorrência.

Arquivos: RM.Edu.API.dll; RM.Edu.Menu.dll

### Rotina: PAINEL DO ALUNO

* **[Ticket: 29201140 / DEDUSAGA-11082]** Ajuste para apresentar notas com 'Vírgula' e não com 'Ponto' no gráfico de notas.

Arquivo: Edu/portalgestaoeducacional

### Rotina: TABELA DE PREÇO

* **[Ticket: DEDUPACMEN-9048]** Ajuste para funcionamento da gestão de fiador após atualização para angular 21

Arquivo: Edu/portalgestaoeducacional

# TOTVS Folha de Pagamento

## 12.1.2606.100

### Rotina: COMPLEMENTAR

* **[Ticket: 28936250 / DRHCALCRM-12436]** Na retificação da rescisão o provento obrigatório pago na rescisão original está sendo consdirado duas vezes na insuficiência de saldo

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: FILA DE EVENTOS

* **[Ticket: DRHROTRM-18400]** Ajuste na validação de eventos com de/para para eventos com código de cálculo 420

Arquivos: RM.Fop.Evento.Data.dll; RM.Fop.Esocial.Form.dll

### Rotina: S-1010 - RUBRICAS

* **[Ticket: 26023454 / DRHROTRM-16904]** Liberação do processo para converter os evento do de/para de férias do parametrizador

Arquivos: RM.FopFolha.dll; RM.Fop.Esocial.Form.dll

# TOTVS Framework

## 12.1.2606.100

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWFOUNDATION-30890]** Ajuste para que a flag OIDC\_ENABLED não seja setada no processamento da mensagem ErpUserEvent

Arquivos: RM.Lib.Server.dll; RM.Lib.SmartLink.Service.dll; RM.Lib.SmartX.Cadastros.dll

* **[Ticket: DFRWFOUNDATION-30890]** Ocultando menu de Contexto

Arquivo: RM.Lib.SmartX.Cadastros.dll

### Rotina: ACESSO A MENUS

* **[Ticket: DFRWFOUNDATION-30747]** Voltando Permissão em item de Menu

Arquivo: RM.Lib.Client.dll

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-30852]** Realizado ajuste em mensagem enviada para o Snowdem sobre execuções no WFCore.

Arquivo: RM.Glb.Workflow.Server.dll

# TOTVS Gestão Compras e Faturamento

## 12.1.2606.100

### Rotina: CONCLUIR CONTRATO

* **[Ticket: DRMMATERIAIS-8293]** Ajuste na geração de contrato a partir de um movimento com campos opcionais vazios.

Arquivo: RM.Ctr.Processos.Data.dll

### Rotina: INCLUSÃO

* **[Ticket: 29020485 / DRMMATERIAIS-10286]** Ajuste na parametrização de cache

Arquivo: RM.Mov.Movimento.Data.dll

# TOTVS Gestão Financeira

## 12.1.2606.100

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 27406908 / FINANCEIRO01-27738]** Buscar Nome Fantasia de Coligada e informar no Merchant Descriptor

Arquivo: RM.Fin.Integracoes.Service.dll

### Rotina: EXTRATO DE CAIXA - VISÃO

* **[Ticket: 28320758 / DRMGR-5090]** Ajuste na escolha de convênio da conta caixa no processo de Extrato de Caixa

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: POSIÇÃO FINANCEIRA

* **[Ticket: 28858426 / FINANCEIRO01-27981]** Evolução na visão da Posição Financeira para tratar os casos com e sem IBS e CBS informado no histórico de lançamentos.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO

* **[Ticket: 27668510 / FINANCEIRO01-27757]** Melhoria no processo de Retorno de Pagamento

Arquivo: RM.Fin.Contrato.Service.dll

# TOTVS Gestão Fiscal

## 12.1.2606.100

### Rotina: EMISSÃO

* **[Ticket: DMOTORFISCALRM-808]** Ajustado processo para permitir o Envio de Cancelamento de Eventos Autorizados [110001].

Arquivo: RM.Fis.NFe.Data.dll

### Rotina: INVENTÁRIO OBJETOS GERENCIAIS (BSO)

* **[Ticket: DMONTRIBRM-4394]** DANFSE - Inclusão do projeto RM.Doc.NativeProvider.TesteUnitario

Arquivo: RM.Doc.NativeProvider.Service.dll

# TOTVS Gestão Hospitalar

## 12.1.2606.100

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUPEPCONV-23755]** Descrição de prescrição médica campo complementar

Arquivo: Sau/pep

### Rotina: MOVIMENTAÇÃO DE ESTOQUE

* **[Ticket: DSAUCLINICA-14876]** Ajuste na tela de itens da movimentação de estoque. Ao alterar o produto por meio da seta de seleção, as informações de lote do item anteriormente selecionado permaneciam preenchidas indevidamente. Foi realizado um ajuste para recarregar os lotes de acordo com o novo produto selecionado, garantindo a exibição das informações corretas.

Arquivo: RM.Sau.Stock.Form.dll

### Rotina: PEDIDO DE EXAMES

* **[Ticket: DSAUGHASSIST-22632]** Alterado parametro Utiliza Status Liberação na Recepção da unidade diagnóstico para não permitir digitação do campo

Arquivo: RM.Sau.Parametrizador.Form.dll

# TOTVS Gestão Hospitalar Prontuário Eletrônico

## 12.1.2606.100

### Rotina: Sem Rotina Específica

* **[Ticket: 28624148 / DSAUPEPCONV-24029]** Ajuste na exibição do anexo

Arquivo: RM.Pep.Documents.Server.dll

# TOTVS Incorporação

## 12.1.2606.100

### Rotina: USO EXTERNO DE API / WEBSERVICE

* **[Ticket: TINPAD001-22659]** RD Marketing - Ajuste no parametro do conversor de integração

Arquivo: RM.Imb.RDStation.Marketing.SmartLink.Server.dll

# TOTVS Manutenção

## 12.1.2606.100

### Rotina: OBJETO DE MANUTENÇÃO

* **[Ticket: 28049753 / TOPORCAPLAN001-30652]** Obras e projetos - manutenção - OS integração com patrimônio.

Arquivos: RM.Mnt.ApropriacaoDireta.Form.dll; RM.Mnt.ObjOficina.Service.dll

# TOTVS Processo Seletivo

## 12.1.2606.100

### Rotina: ANEXOS - AREA DE INTERESSE OFERTADA

* **[Ticket: 27646209 / DEDUCAPCOM-10542]** Ajuste na identificação de PS de venda on line na área ofertada

Arquivo: RM.EduPS.Cadastros.Data.dll

# TOTVS Segurança e Medicina do Trabalho

## 12.1.2606.100

### Rotina: FONTES GERADORAS

* **[Ticket: 27192804 / DRHSSTPT-2059]** Ajuste no PPP para a não impressão de riscos ergonômicos e mecânicos

Arquivo: RM.Smt.Relatorio.Data.dll
