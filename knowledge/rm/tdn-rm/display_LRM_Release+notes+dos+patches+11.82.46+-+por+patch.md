---
content_hash: d3c8a6f253d81b470fa01905505034bdc75c0d79b1adc5b20e81e2c7ad89d284
fetched_at: '2026-06-29T00:09:03.487711+00:00'
page_id: '381040952'
product: rm
source: tdn-rm
title: Release notes dos patches 11.82.46 - por patch
type: documentation
url: https://tdn.totvs.com/display/LRM/Release+notes+dos+patches+11.82.46+-+por+patch
version: 3
---

|  |
| --- |
| Esses são todos os patches gerados, porém nem todos estão disponíveis para todos os clientes. |

---

  
  

1square

---

  
  

# 11.82.46.100

## TOTVS Folha de Pagamento

* **[Ticket: 07\TVWHJF]** Ajuste no cálculo do FGTS para tratar o caso de rescisão complementar na mesma competência da rescisão original.

Arquivo: RM.Fop.Calc.CalculosBase.dll

## TOTVS Gestão Hospitalar

* **[Ticket: 07\TVUHZE]** Restaurado o parâmetro “Grau de Participação na guia SP/SADT - exames” nas condições contratuais do convênio.

Arquivos: RM.Sau.Ans.Sever.dll, RM.Sau.CadastrosFat.Form.dll

# 11.82.46.101

## TOTVS Framework

* **[Ticket: 07\TVXIOS]** -Otimização da exibição de filtros pelo acesso rápido ao trocar o contexto do sistema.

Arquivo: RM.MDI.Server.dll

* **[Ticket: 07\TVO630]** Foi realizada uma melhoria para identificar strings literais. Para tal deverá ser inserido um @ antes da string. Por exemplo:SE TABDEP ('INCDEFINIVEIS' ,'S',4) = @' \*\* 'ENTAO 'IGUAL'SENAO 'DIFERENTE'FIMSE

Arquivo: RM.Lib.Formula.dll

## TOTVS Gestão Financeira

* **[Ticket: 07\TVXTZY]** Otimização no processo de retorno bancário de cobrança. Agora o sistema apresenta corretamente o somatório dos valores de baixa dos lançamentos não baixados.

Arquivo: RM.Fin.Lan.Data.dll

* **[Ticket: 07\TWCSJX]** Otimização no processo de filtros customizados na visão de lançamentos/extratos para exibir o número correto de lançamentos/extratos visíveis e quando houver filtro de colunas ativos também.

Arquivos: RM.Fin.Extrato.Form.dll, RM.Fin.Lan.Form.dll

## TOTVS Gestão Fiscal

* **[Ticket: 07\TVZLYB]** Implementação no envio da NF-e. Segundo o manual do consumidor os grupos DI e DetExport somente serão gerados ao mesmo tempo na NF-e, quando a CFOP for a 3.503 (devolução de importação).Alterado a regra de geração destes grupos para atender a legislação descrita no manual da NF-e.

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: 07\TVZLYB]** Implementação no envio da NF-e. Segundo o manual do consumidor os grupos DI e DetExport somente serão gerados ao mesmo tempo na NF-e, quando a CFOP for a 3.503 (devolução de importação).Alterado a regra de geração destes grupos para atender a legislação descrita no manual da NF-e.

Arquivo: RM.Fis.NFe.Service.dll

## TOTVS Gestão Hospitalar

* **[Ticket: 07\TVZAWB]** Ajuste realizado para que a geração do XML possua a tag encoding.

Arquivo: RM.Sau.Ans.Sever.dll

# 11.82.46.102

## TOTVS Gestão de Pessoas

### Rotina: Formação adicional não exibe formação com data termino superior ao ano atual

* **[Ticket: MRH-651]** Ajuste na data de termino no cadastro de formação adicional

Arquivo: App\_Web\_pasta\_form\_adic\_edicao.ascx.abf61458.dll

# 11.82.46.103

## TOTVS Automação de Ponto

### Rotina: ACJEF

* **[Ticket: MRH-2025]** Otimizado a emissão do relatório ACJEF para tratar os casos onde o evento de extra não está no sindicato mas é calculado pelo sistema.

Arquivo: RM.Pto.Relatorio.Data.dll

## TOTVS Educacional

### Rotina: MELHORIA, PARA TROCAR A VALIDAÇÃO DO PROCESSO DE MATRICULA NO PORTAL.

* **[Ticket: MEDU-239]** Foi realizada otimização do processo de matrícula online, de forma que a inadimplência será verificada a partir da data de vencimento do boleto.

Arquivos: RM.Edu.Services.Server.dll, RM.Edu.Matricula.Data.dll, RM.Edu.NotaFalta.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: Incosistencia Sistema Totvs

* **[Ticket: MRH-2378]** Tratada a unicidade de usuário no banco de talentos

Arquivo: App\_Web\_login\_novo.aspx.f661be84.dll

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: GERAÇÃO DE ATENDIMENTO

* **[Ticket: MCP-907]** Ajuste ao repassar atendimentos em base oracle

Arquivo: RM.CRM.Atendimento.Data.dll

## TOTVS Gestão Hospitalar

### Rotina: RÉPLICA para 11.80 - desenvolvimento da versão 3.03.01 da TISS

* **[Ticket: MSAU-2300]** Implementação da versão 3.03.01 da TISS

Arquivos: RM.Sau.Ans.Sever.dll, RM.Sau.Faturamento.Form.dll, RM.Sau.Ans.Form.dll

# 11.82.46.104

## TOTVS Folha de Pagamento

### Rotina: Formula Visual Para Leitura de Parâmetros - T34999

* **[Ticket: 190356 / MRH-2481]** Adição de parâmetro "Alterar Rúbrica" na classe de parâmetros da geração do TRCT para utilização em fórmulas visuais

Arquivos: RM.Fop.Lib.Intf.dll, RM.Fop.Relatorios.Form.dll

### Rotina: Project-192442 Virada de Competência Project-192442

* **[Ticket: 195695 / MRH-2431]** Na liberação de competência no processo para estender a vigência da Alíquota do FAP por Estabelecimento foi otimizado para estender a vigência automaticamente

Arquivo: RM.Fop.Data.Server.dll

# 11.82.46.105

## TOTVS Framework

### Rotina: Ajustes da fórmula visual para a equipe do Labore

* **[Ticket: MFRWBH-814]** Ajustes da fórmula visual para a equipe do Labore

Arquivo: RM.Lib.Workflow.Activities.dll

## TOTVS Gestão Fiscal

### Rotina: NFS-e - Porto Alegre - Dados do intermediario - L44 - Tomador de serviço não possui inscrição municipal válida no município e não pode efetuar a retenção do ISSQN na fonte.

* **[Ticket: 96571 / MEDU-304]** Implementação dos dados do Intermediário.Realizado a montagem do grupo Intermediário da NFS-e para o município de Porto Alegre - RS.Sendo montado em cima da seguinte regra:O município do Tomador é diferente do município da Filial Emitente;O Tipo do Recolhimento do ISS é Retido;O município de prestação do serviço é o mesmo da Filial Emitente; eO código do serviço federal cadastrado no serviço é 7.02, 7.04, 7.05, 7.09, 7.10, 7.11, 7.12, 7.16, 7.17, 7.18 ou 7.19.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.RotinasFiscais.Service.dll

# 11.82.46.106

## TOTVS Framework

### Rotina: Exportação de cubo

* **[Ticket: 280399 / MFRWBH-815]** Ajustes da fórmula visual para a equipe do Labore

Arquivo: RM.Lib.Workflow.Activities.dll

### Rotina: Project-203293 PROBLEMAS PLANILHA.NET Project-203293

* **[Ticket: 263715 / MFRWBH-777]** Melhoria na execução de procedures em planilha RM

Arquivo: RM.Glb.PlanilhaNet.Form.dll

# 11.82.46.107

## TOTVS Automação de Ponto

### Rotina: [PROCESSO] LANCAMENTO EXTRA AUTORIZADA SINTETICA

* **[Ticket: MRH-1250]** Ajuste referente a data na rotina de extra sintética autorizada.

Arquivos: RM.Pto.Extra.dll, RM.Pto.Extras.Form.dll, RM.Pto.Extra.Intf.dll

## TOTVS Gestão Financeira

### Rotina: #INSS #MULTA - Valor de Multa do lançamento referente a INSS considera feriado municipal e SINTEGRA não considera.

* **[Ticket: 98583 / MEDU-349]** Cálculo de multa de IRRF e INSS passa a considerar como feriados apenas os nacionais.

Arquivo: RM.Fin.Facade.dll

### Rotina: Liberar o campo histórico do processo de retorno de pagamento para ser utilizado pela customização

* **[Ticket: MEDU-1806]** Apenas disponibilizar o campo histórico no processo de retorno de pagamento para ser utilizado pela customização

Arquivo: RM.Fin.Banco.Data.dll

# 11.82.46.108

## TOTVS Automação de Ponto

### Rotina: Project-152197 Erro ao aprovar horas extras Project-152197

* **[Ticket: 171980 / MRH-2042]** Acertada a rotina de aprovação de extras, para usuário externo.

Arquivo: RM.Pto.AprovaHorasExtras.Data.dll

## TOTVS Gestão de Pessoas

### Rotina: Project-226402 Falha ao salvar campos complementares Project-226402

* **[Ticket: 299295 / MRH-3702]**

Arquivo: RM.Rhu.Pessoa.Data.dll

# 11.82.46.109

## TOTVS Gestão de Pessoas

### Rotina: VITAE/SSO

* **[Ticket: MRH-4359]** Realizado ajuste no cadastro de entidades para a DIRF.

Arquivo: RM.Rhu.Cadastros.Form.dll

# 11.82.46.110

## TOTVS Automação de Ponto

### Rotina: Project-369530 Ao Prime: RM Chronus- Indisponibilidade relatórios da Portaria 1510/ 2009. Project-369530

* **[Ticket: MRH-5023]** Ajustada a data limite para acerto de AFDT e CRC.

Arquivo: RM.Pto.Batida.Data.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF - Implementação Previdência Complementar

* **[Ticket: MRH-3260]** Liberação dos cadastros iniciais da DIRF 2017

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3260]** Liberação dos cadastros iniciais da DIRF 2017

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3260]** Liberação dos cadastros iniciais da DIRF 2017

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3260]** Liberação dos cadastros iniciais da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: Modulos necessários para Reembolso de titular e seus dependentes

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivos: RM.Fop.Dominio.dll, RM.Fop.Funcionario.Intf.dll, RM.Fop.Lib.WinForms.dll, RM.Fop.Lib.Extensions.dll, RM.Fop.Utils.Intf.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Utils.Server.dll, RM.Fop.Cadastros.Form.dll, RM.Fop.Infraestrutura.Repositorios.dll, RM.Fop.Cadastros.Intf.dll, RM.Fop.Funcionario.Data.dll, RM.FopFolha.dll, RM.Fop.Funcionario.Form.dll, RM.Fop.Cadastros.Data.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivos: RM.Fop.Utils.Intf.dll, RM.Fop.Utils.Server.dll

* **[Ticket: MRH-3763]** dirf

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivos: RM.Fop.Cadastros.Form.dll, RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivo: RM.Fop.Funcionario.Form.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivos: RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivos: RM.Fop.Cadastros.Form.dll, RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivo: RM.Fop.Cadastros.Form.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivo: RM.Fop.Funcionario.Form.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivo: RM.Fop.Funcionario.Form.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivo: RM.FopFolha.dll

* **[Ticket: MRH-3763]** Inclusão de Cadastros para DIRF 2017

Arquivo: RM.Fop.Utils.Server.dll

### Rotina: Permissão Acesso RAIS 11.82

* **[Ticket: MRH-5239]** Permissão Acesso RAIS 11.82

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: Processo para preencher os dados do Advogado na DIRF

* **[Ticket: MRH-3557]** Incluindo cadastros iniciais da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Incluindo cadastros iniciais da DIRF 2017

Arquivo: RM.Fop.Funcionario.Form.dll

* **[Ticket: MRH-3557]** Incluindo cadastros iniciais da DIRF 2017

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3557]** Incluindo cadastros iniciais da DIRF 2017

Arquivo: RM.Fop.Utils.Server.dll

* **[Ticket: MRH-3557]** Incluindo cadastros iniciais da DIRF 2017

Arquivo: RM.Fop.Relatorios.Form.dll

### Rotina: Rotina DIRF 2016/2017

* **[Ticket: 183323 / MRH-2344]** Liberação dos cadastros iniciais da DIRF 2017

Arquivos: RM.Fop.Funcionario.Intf.dll, RM.Fop.Funcionario.Form.dll, RM.Fop.Funcionario.Data.dll

## TOTVS Gestão Fiscal

### Rotina: Implementação dos Registros Referentes aos Rendimentos dos Socios por Mês na DIRF (Versão 11.80)

* **[Ticket: MEDU-1974]** Implementação dos Registros Referentes aos Rendimentos dos Socios por Mês na DIRF

Arquivos: RM.Fis.Filial.Intf.dll, RM.Fis.Filial.Data.dll, RM.Fis.Filial.Form.dll

# 11.82.46.112

## TOTVS Folha de Pagamento

### Rotina: DIRF - Implementação Previdência Complementar

* **[Ticket: MRH-3260]** Liberado DIRF para Conferência na DIRF Cadastral 2017.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Relatorios.Data.dll

### Rotina: Modulos necessários para Reembolso de titular e seus dependentes

* **[Ticket: MRH-3763]** Inclusão de cadastro para DIRF

Arquivo: RM.Fop.Relatorios.Data.dll

## TOTVS Gestão Financeira

* **[Ticket: Alterações Gerais]**

Arquivos: WSTotvs.RegrasECommerceMaster.dll, RM.Glb.Live.SSO.Auth.dll, WSTotvs.RegrasECommerce.dll

## TOTVS Gestão Fiscal

### Rotina: NF-e - Totvs Colaboração - Método errado para monitoramento.

* **[Ticket: 382378 / MEDU-2193]**

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: Valor incorreto no campo: "Valor ICMS Interestadual"

* **[Ticket: 370407 / MEDU-2158]** Implementada melhoria para sistema conseguir calcular corretamente o Valor do ICMS Interestadual mesmo com redução de base de cálculo do ICMSem lançamentos fiscais de entrada com diferencial de alíquota.

Arquivos: RM.Fis.LancFiscal.Intf.dll, RM.Fis.LancFiscal.Service.dll, RM.Fis.LancFiscal.Form.dll

## TOTVS Incorporação

* **[Ticket: Alterações Gerais]**

Arquivo: RM.Imb.Aditivos.Server.dll

# 11.82.46.113

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Informe.Data.dll

### Rotina: DIRF - Implementação Previdência Complementar

* **[Ticket: MRH-3260]** Liberação DIRF 2017 - Informe de Rendimentos e DIRF em Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: Erro ao gerar Encargo

* **[Ticket: 319708 / MRH-4360]**

Arquivo: RM.Fop.Dominio.dll

### Rotina: Processo para preencher os dados do Advogado na DIRF

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivos: RM.Fop.Funcionario.Form.dll, RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Informe.Data.dll

### Rotina: RAIS

* **[Ticket: MRH-5725]** \* Ajuste em rotina rais para verificação de seção de pagamento de adiantamento de 13º salário que era registrado com o mesmo valor em várias seções segundo o histórico de seções do funcionário.\* Retirado caracteres especiis para nome do funcionário\* Validação para o campo "valor de dissídio" quando negativo sendo enviado para RAIS com valor positivo\* Verificação de contagem dias de afastamento quando retorna à situação de afastamento na mesma data que do fim do afastamento anterior. O sistema contava esse dia duas vezes.\* Ajuste em rotina RAIS para informar valor 1 no campo Tipo RAIS quando registro de Seção não possuir funcionários vinculados.

Arquivos: RM.Fop.Dominio.dll, RM.Fop.Relatorios.Server.dll

* **[Ticket: MRH-5725]** Ajuste em Rotina RAIS para forçar valor de R$0,01 ao mesmo mês de remuneração que o mês de rescisão quando não houver remuneração nos meses do ano base.

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-5725]** Ajuste para informar valor de remuneração que não estava sendo levado.

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-5725]** Ajuste em rotina rais para verificação de seção de pagamento de adiantamento de 13º salário que era registrado com o mesmo valor em várias seções segundo o histórico de seções do funcionário.

Arquivo: RM.Fop.Dominio.dll

### Rotina: RAIS 2017

* **[Ticket: MRH-6149]**

Arquivo: RM.Fop.Dominio.dll

## TOTVS Gestão Financeira

### Rotina: Ao realizar o processo de baixa de lançamento, tanto automática ou manual, o sistema apresenta a inconsistência:

* **[Ticket: 430598 / MEDU-2313]** Ajustado update dos rateios de departamento do item de baixa para não apresentar erro de syntax.

Arquivo: RM.Fin.Lan.Service.dll

## TOTVS Gestão Fiscal

### Rotina: DIRF 2017 - Criação de validação para clientes que não aplicaram scripts da ECF

* **[Ticket: MEDU-2332]** Foi realizada uma implementação na geração da DIRF na versão 11.82.46 para que, caso o usuário proceda com a geração da DIRF 2017 e não tenha executado em sua Base de Dados os Scripts referente às implementações da ECF (será verificado o campo “RENDPORMES” da tabela “DSOCIOECF”), o sistema emita a seguinte mensagem: "Prezado Cliente, A DIRF 2017 está disponível para todos os clientes em patchs específicos a partir do release 12.1.12. A utilização desta rotina no release 11.82 depende de liberação comercial por parte da TOTVS. Para maiores informações, contate o Suporte Técnico Totvs através do 4003-0015.".

Arquivo: RM.Fis.RotinasFiscais.Form.dll

### Rotina: Implementação dos Registros Referentes aos Rendimentos dos Socios por Mês na DIRF

* **[Ticket: MEDU-2255]** Merge das Implementações dos Registros Referentes aos Rendimentos dos Socios por Mês na DIRF

Arquivos: RM.Fis.RotinasFiscais.Service.dll, RM.Fis.RotinasFiscais.Intf.dll

### Rotina: SPED Fiscal - Registro 0200 - Campo 13

* **[Ticket: 415568 / MEDU-2265]** Implementação do campo 13\_CEST do registro 0200 da rotina Sped Fiscal. De acordo com o guia prático, layout 11, válido a partir de 01 de janeiro de 2017, o campo CEST é válido a partir de 01/01/2017.Manual disponível em: http://sped.rfb.gov.br/estatico/81/01339D2ACB30B5E6162E014631262CBDD1A372/GUIA%20PR%c3%81TICO%20DA%20EFD%20-%20Vers%c3%a3o%202.0.19.pdf

Arquivos: RM.Fis.Sped.Engine.dll, RM.Fis.Sped.Form.dll, RM.Fis.Sped.Server.dll

* **[Ticket: 415568 / MEDU-2265]** Implementação do campo 13\_CEST do registro 0200 da rotina Sped Fiscal. De acordo com o guia prático, layout 11, válido a partir de 01 de janeiro de 2017, o campo CEST é válido a partir de 01/01/2017.Manual disponível em: http://sped.rfb.gov.br/estatico/81/01339D2ACB30B5E6162E014631262CBDD1A372/GUIA%20PR%c3%81TICO%20DA%20EFD%20-%20Vers%c3%a3o%202.0.19.pdf

Arquivos: RM.Fis.Sped.Server.dll, RM.Fis.Sped.Engine.dll

# 11.82.46.114

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3260]** Liberação DIRF 2017.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da dirf 2017

Arquivo: RM.Fop.Cadastros.Data.dll

* **[Ticket: MRH-3260]** Implementação DIRF 2017.

Arquivos: RM.Fop.Informe.Data.dll, RM.Fop.Informe.Intf.dll

* **[Ticket: MRH-3557]** Realizando liberação da dirf 2017

Arquivo: RM.Fop.Informe.Data.dll

* **[Ticket: MRH-3260]**

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: Processo para preencher os dados do Advogado na DIRF

* **[Ticket: MRH-3557]**

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da dirf em arquivo.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivos: RM.Fop.Cadastros.Intf.dll, RM.Fop.Infraestrutura.Repositorios.dll, RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Form.dll, RM.Fop.Cadastros.Data.dll

### Rotina: RELATÓRIO TRCT FOP34546

* **[Ticket: 96211 / MRH-102]** Alterar o tratamento de arredondamento do valores gravados na tabela PFFERRESCTRCT, para evitar diferenças entre o relatório e os valores lançados no envelope de rescisão.

Arquivo: RM.Fop.Calc.Calculos.dll

# 11.82.46.115

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Legislação DIRF: No Informe tct foi implementado a Quebra do nome do advogado no campo 7 conforme é feito no portal e pdf

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** DIRF 2017 - Otimizado informações de previdência complementar referente ao décimo terceiro.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivos: RM.Fop.Relatorios.Data.dll, RM.Fop.Relatorios.Intf.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]**

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3260]** DIRF 2017 - Otimizado informações de previdência complementar referente ao décimo terceiro.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3260]** Liberação DIRF 2017.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 - Alteração Informe de Rendimentos e DIRF Arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

## TOTVS Gestão Hospitalar

### Rotina: Erro na rotina de cópia de diárias

* **[Ticket: 207253 / MSAU-4143]** Ajuste realizado para que o sistema faça a cópia das diárias de um convênio para outro corretamente.

Arquivos: RM.Sau.CadastrosFat.Form.dll, RM.Sau.CadastrosFat.Server.dll

# 11.82.46.117

## TOTVS Automação de Ponto

### Rotina: Project-495293 Erro autorização de extras Project-495293

* **[Ticket: 495657 / MRH-6805]** Foi alterada o nome da coluna para INICIO no sistema, pois a coluna INICIO1 não está presente na tabela EXTRASINTETICO

Arquivo: RM.Pto.Extra.dll

## TOTVS Folha de Pagamento

### Rotina: DIRF

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivos: RM.Fop.Relatorios.Data.dll, RM.Fop.Informe.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3557]** Realizando liberação da DIRF 2017

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: MRH-3260]** DIRF 2017: Ajuste na previdência complementar que estava abatendo indevidamente no rendimento tributável.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: INFORME DE RENDIMENTOS FOP 34 431

* **[Ticket: 431090 / MRH-5945]** DIRF 2017: Otimizado dedução de dependente quando há diferente de férias.

Arquivo: RM.Fop.Relatorios.Data.dll

# 11.82.46.118

## TOTVS Folha de Pagamento

### Rotina: Comprovante de Rendimentos 2017

* **[Ticket: 323103 / MRH-4134]** DIRF 2017 - Ajuste na previdência complementar de décimo terceiro no Informe de Rendimentos.DIRF 2017 - Ajuste na restituição de décimo terceiro no Informe de Rendimentos e DIRF para Conferência.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: DIRF

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-3763]** Liberação DIRF 2017 Informe de Rendimentos e DIRF em arquivo

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: DIRF LAB 01 11

* **[Ticket: 471314 / MRH-6552]** DIRF 2017 - Ajuste na previdência complementar de décimo terceiro no Informe de Rendimentos.DIRF 2017 - Ajuste na restituição de décimo terceiro no Informe de Rendimentos e DIRF para Conferência.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 501166 / MRH-7021]** DIRF 2017 - Informe de Rendimentos: Ajuste na dedução da Previdência de Décimo Terceiro.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 488749 / MRH-6846]** Para os graus de parentesco abaixo o sistema não irá gerar log de erro e sim de informação ao validar a data de nascimento na DIRF, a saber: Mãe: 7; Pai: 6; Sogra: 8, S; Companheiro: C, P; Outros: 9.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 482495 / MRH-7014]** DIRF 2017: Ajuste no desconto do plano de saúde quando a dedução referente a férias para o dependente e titular.

Arquivo: RM.Fop.Relatorios.Data.dll

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: INT FISCAL ESCRITURACAO FIS 001

* **[Ticket: 422469 / MCP-1715]** O campo que indica se usa rateio de valores financeiros, estava presente na regra de inclusão, mas não na de alteração, isso fazia com que esse valor se perdesse em uma alteração, agora esse valor foi incluído na regra de alteração resolvendo esse problema.

Arquivo: RM.Mov.Movimento.IService.dll

# 11.82.46.119

## TOTVS Folha de Pagamento

### Rotina: DIRF LAB 01 11

* **[Ticket: 514895 / MRH-7202]** DIRF 2017: Ajustado opção Subtrair na geração da DIRF/Informe de Rendimentos.

Arquivo: RM.Fop.Relatorios.Intf.dll

# 11.82.46.120

## TOTVS Folha de Pagamento

### Rotina: DIRF LAB 01 11

* **[Ticket: 529275 / MRH-7352]** DIRF 2017: Ajuste unificação de dados da pensão alimentícia quando há movimentação referente a PLR.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 501718 / MRH-7434]** DIRF 2017: Otimizado ajuste na DIRF referente aos dados do plano de saúde.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 514983 / MRH-7233]** Quando o parâmetro "Calcular IRRF/INSS de múltiplos vínculos sem chapa centralizadora" estiver desmarcado o sistema irá obter o valor da dedução de 13º salário dos dependentes somente da chapa centralizadora evitando duplicar os valores de dedução.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 501718 / MRH-7434]** DIRF 2017: Otimizado ajuste na DIRF referente aos dados do plano de saúde.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 524112 / MRH-7263]** O nome do dependente passa a ser informado de forma alinhada no informe de rendimento PDF nas "Despesas Médico-Odonto-Hospitalares" para o "Valor pago no ano referente aos dependentes".

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: INFORME DE RENDIMENTOS FOP 34 431

* **[Ticket: 534377 / MRH-7429]** Realizando ajuste no campo de informações complementares para não somar a base de 13º salário.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RAIS

* **[Ticket: MRH-5725]**

Arquivos: RM.Fop.Infraestrutura.Repositorios.dll, RM.Fop.Dominio.dll

* **[Ticket: MRH-5725]**

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: MRH-5725]**

Arquivo: RM.Fop.Infraestrutura.Repositorios.dll

### Rotina: RECLASSIFICAR

* **[Ticket: MRH-1353]** Ajuste na seleção de funcionários do fracionamento de jobs na geração de encargos

Arquivo: RM.Fop.Lib.Server.dll

## TOTVS Framework

* **[Ticket: Alterações Gerais]**

Arquivo: RM.Lib.Server.dll

# 11.82.46.121

## TOTVS Folha de Pagamento

### Rotina: Comprovante de Rendimentos 2017

* **[Ticket: 323103 / MRH-4134]** DIRF 2017: Ajuste na unificação de dados da pensão alimnetícia.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 323103 / MRH-4134]** DIRF 2017: Otimizado ajuste na DIRF referente aos dados do plano de saúde.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 323103 / MRH-4134]** DIRF 2017: Otimizado ajuste na DIRF referente aos dados do plano de saúde.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: DIRF LAB 01 11

* **[Ticket: 523112 / MRH-7531]** DIRF 2017: Alterado para permitir evento do tipo provento marcar a opção Subtrair.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 535472 / MRH-7473]** O nome do dependente passa a ser informado de forma alinhada no informe de rendimento PDF nas "Despesas Médico-Odonto-Hospitalares" para o "Valor pago no ano referente aos dependentes".

Arquivo: RM.Fop.Relatorios.Data.dll

# 11.82.46.122

## TOTVS Folha de Pagamento

### Rotina: DIRF LAB 01 11

* **[Ticket: MRH-7747]** DIRF: Ajustado pensão sobre PLR no Informe de Rendimentos.

Arquivos: RM.Fop.Relatorios.Intf.dll, RM.Fop.Relatorios.Data.dll

* **[Ticket: 521406 / MRH-7232]**

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: MRH-7747]** Acerto na distribuição de assistencia médica entre titular e dependnete.Informe portal para emitir o pdf do usuario de chapa corrente.

Arquivos: RM.Fop.Informe.Data.dll, RM.Fop.Relatorios.Data.dll

### Rotina: Project-551992 Ajuda de Custo no Informe Project-551992

* **[Ticket: 552678 / MRH-7751]**

Arquivo: RM.Fop.Relatorios.Data.dll

## TOTVS Gestão Financeira

### Rotina: Project-525553 Desvincular borderô de pgto Project-525553

* **[Ticket: 527448 / MEDU-2730]** Ajustado processo de desvincular lançamentos do borderô para cancelar a retenção acumulada relacionada ao item de baixa cancelado durante o processo.

Arquivo: RM.Fin.Lan.Service.dll

# 11.82.46.123

## TOTVS Folha de Pagamento

### Rotina: DIRF LAB 01 11

* **[Ticket: 557313 / MRH-7806]** Ajuste na Rotina da DIRF para verificar o código de receita de PLR afim de evitar o somatório de valores de RRA e valores de folha.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RAIS LAB 01 12

* **[Ticket: 559790 / MRH-7817]** Ajuste na rotina RAIS para chamada de construtor do da classe com parâmetros já preenchidos.

Arquivo: RM.Fop.Relatorios.Server.dll

* **[Ticket: 559790 / MRH-7817]** Ajuste em rotina rais para verificação de valor de cnpj vazio em cadastros.

Arquivo: RM.Fop.Dominio.dll

# 11.82.46.124

## TOTVS Folha de Pagamento

### Rotina: RAIS LAB 01 12

* **[Ticket: 573676 / FOPROTINAS01-382]** Ajuste em rotina RAIS para não deduzir valor de diferença de aviso prévio (cc 99) que influenciava diretamente no valor de diferença salarial (cc 96 ou cc 37).

Arquivo: RM.Fop.Dominio.dll

# 11.82.46.125

## TOTVS Folha de Pagamento

### Rotina: DIRF LAB 01 11

* **[Ticket: 577484 / MRH-7992]** Otimizado geração da DIRF para considerar a dedução de dependente de IRRF décimo terceiro somente uma vez

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: MAQUINA DE CALCULO FOP 1 4 1 91

* **[Ticket: 592074 / MRH-8146]** Ajuste no cálculo de média da provisão de férias para considerar a perda do periodo aquisitivo somente quando o funcionário ficar 31 dias ou mais com afastamento tipo R - Licença Remunerada.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: PORTAL WEB GESTAO DE FERIAS LAB 01 208

* **[Ticket: 521382 / MRH-7229]** Tratar na apuração das faltas do cadastro de férias do executável, para subtrair a referência do CC 128 somente quando o evento for do tipo Provento.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: RAIS LAB 01 12

* **[Ticket: 573676 / FOPROTINAS01-382]** Ajuste na rotina RAIS para não considerar data de pagamento do evento para códigos de cálculo 96 e 37 e sim mês e ano de competência para comparação com data de desligamento.

Arquivos: RM.Fop.BaseDados.Data.dll, RM.Fop.Dominio.dll

# 11.82.46.126

## TOTVS Folha de Pagamento

### Rotina: Project-590048 Assistência Médica Dependente Project-590048

* **[Ticket: 598448 / MRH-8238]** O campo de valor do registro TPSE para DIRF em arquivo permanecendo zerado mesmo que os registros DTPSE tenha valores.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RAIS LAB 01 12

* **[Ticket: 504006 / MRH-8164]** Ajuste no processo de geração da RAIS quando a opção “Gera registro para alteração de CEI” está marcada.

Arquivo: RM.Fop.Dominio.dll

# 11.82.46.127

## TOTVS Folha de Pagamento

### Rotina: Project-584475 Informe de Rendimento - Previdência Project-584475

* **[Ticket: 590625 / MRH-8133]** Realizando ajuste no valor dos rendimentos isentos que estavam sendo levados incorretamente quando o funcionário possuia mais de uma previdência privada.

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RAIS LAB 01 12

* **[Ticket: 612758 / FOPROTINAS01-310]**

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 607699 / FOPROTINAS01-311]**

Arquivo: RM.Fop.Dominio.dll

## TOTVS Gestão Financeira

### Rotina: A DELIC

* **[Ticket: MEDU-2773]** Registro Q100 - ECF

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Lan.IService.dll

* **[Ticket: MEDU-2773]** Registro Q100 - ECF

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Lan.IService.dll

* **[Ticket: MEDU-2773]** Registro Q100 - ECF

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Lan.IService.dll

* **[Ticket: MEDU-2773]** Registro Q100 - ECF

Arquivos: RM.Fin.Lan.Service.dll, RM.Fin.Lan.IService.dll

# 11.82.46.128

## TOTVS Gestão de Pessoas

### Rotina: PESSOAS RHU 36 050

* **[Ticket: 631243 / MRH-8618]** Realizado ajuste no cadastro de Funcionário de forma a evitar inconsistências quando o funcionário a ser cadastrado estiver vinculado a uma requisição de substituição gerada por uma requisição de outra coligada.

Arquivo: RM.Rhu.Requisicao.Server.dll

# 11.82.46.130

## TOTVS Folha de Pagamento

### Rotina: FOLHA

* **[Ticket: MRH-9228]**

Arquivo: RM.FopFolha.dll

## TOTVS Gestão Contábil

### Rotina: OBRIGACOES ACESSORIAS GERAR SPED CONTABIL CTB 38 133

* **[Ticket: 481525 / MEDU-3360]** Com objetivo de atender aos clientes que querem entregar o SPED Contábil e não precisam entregar o bloco K por se tratar de um registro facultativo para o ano base 2016, iremos liberar uma versão do SPED Contábil 5.0 sem contemplar algumas evoluções:- Bloco K: Conglomerados Econômicos (Facultativo para o ano-calendário 2016)Em função do nível de complexidade dos recursos acima os mesmos serão disponibilizados em versões posteriores.

Arquivos: RM.Ctb.Sped.Service.dll, RM.Ctb.Sped.Data.dll, RM.Ctb.Sped.Form.dll, RM.Ctb.Parametros.Intf.dll, RM.Ctb.Sped.Intf.dll

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS ECF LI 01 0032

* **[Ticket: 623082 / MEDU-3091]** Será implementado a ECF versão 0003 na versão de biblioteca 11.82.46

Arquivos: RM.Fis.Lib.dll, RM.Fis.Facade.dll, RM.Fis.Filial.Intf.dll, RM.Fis.RotinasFiscais.Intf.dll, RM.Fis.Sped.Server.dll, RM.Fis.Filial.Data.dll, RM.Fis.Filial.Form.dll, RM.Fis.RotinasFiscais.Service.dll

# 11.82.46.133

## TOTVS Educacional

### Rotina: CONTRATOS EDU 50 139

* **[Ticket: 724360 / EDUCACIONAL01-120]**

Arquivos: RM.Edu.Lib.Server.dll, RM.Edu.Lib.WinForms.dll, RM.Edu.Financeiro.Form.dll, RM.Edu.PeriodoLetivo.Form.dll

* **[Ticket: 724360 / EDUCACIONAL01-120]** Alguns processos no educacional permitem que os usuários utilizem consultas SQL previamente cadastradas no RM para carregar informações que serão processadas.Realizamos um ajuste para que as variáveis documentadas no link abaixo sejam interpretadas caso sejam utilizadas em uma das consultas SQL.http://tdn.totvs.com/pages/viewpage.action?pageId=63275590

Arquivo: RM.Edu.Lib.Server.dll

# 11.82.46.134

## TOTVS Gestão Fiscal

### Rotina: OBRIGACOES ACESSORIAS FEDERAIS EFD PIS COFINS LI 01 0033

* **[Ticket: 637128 / FISCAL01-117]** Ao gerar a EFD Contribuições, o sistema não estava contemplando determinado lançamento Financeiro (Id. Lan. 1600), gerado no registro “F525”, ao somar os valores a serem gerados no campo “VL\_TOT\_REC” do registro “1900”.Foi constatado que o Lançamento Financeiro não estava sendo contemplado no somatório do campo no registro “1900” pelo fato de não ter um CFOP válido. Foi analisado que essa situação pode acontecer, pois se trata de um recibo de Aluguel.Foi realizada uma alteração na geração do campo “VL\_TOT\_REC” do registro “1900” para que sejam contemplados no somatório do campo Lançamentos Financeiros que não possuam CFOP.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

# 11.82.46.136

## TOTVS Gestão Fiscal

### Rotina: (11.82) Erro na autorização de NFSe em Juiz de Fora Project-806618

* **[Ticket: 807094 / FISCAL01-321]** Alteração no layout do XML para o município de Juiz de Fora - MG, conforme solicitação do TSS.

Arquivo: RM.Fis.RotinasFiscais.Data.dll

# 11.82.46.137

## TOTVS Gestão de Estoques, Compras e Faturamento

### Rotina: MOV BAIXA DE ESTOQUE EST 002

* **[Ticket: 290560 / MATESTCNTFTOF01-34]** Melhoria no processo de regerar saldos e custos para movimentação de transferência de estoque

Arquivo: RM.Est.Estoque.Service.dll

# 11.82.46.138

## TOTVS Gestão do Relacionamento com o Cliente

### Rotina: GRUPO DE ATENDIMENTOS CRM 321415

* **[Ticket: 654557 / MATFATCMPCRM01-449]** Melhorias no processo responsável por gerar atendimento através de grupo de e-mail.

Arquivos: RM.CRM.Atendimento.Data.dll, RM.CRM.Servicos.Server.dll

# 11.82.46.139

## TOTVS Automação de Ponto

### Rotina: CADASTRO HORARIO POR JORNADA PTO 35 1295

* **[Ticket: 856184 / PONTO01-190]** Foi realizado o ajuste de modo que somente sejam somadas as horas trabalhadas as horas oriundas das ocorrências de trabalho e de horas extras.

Arquivo: RM.Pto.Calculo.Service.dll

# 11.82.46.142

## TOTVS Gerador de Relatórios

### Rotina: Project-1045805 Erro ao importar relatório Project-1045805

* **[Ticket: 1047504 / MFRWBH-2073]** Melhoria na importação de relatórios que seja alterado o código da sentença SQL vinculada

Arquivo: RM.Rpt.Reports.Server.dll

# 11.82.46.143

## TOTVS Gestão Fiscal

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - ECF LI010032

* **[Ticket: 94774 / FISCAL01-832]** A issue em questão foi implementada na versão Atual (12.1.18). Porém, foi necessário implementar as alterações no contexto da ECF desde a versão 11.80, para manter a compatibilidade do Layout em todas as versões.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

# 11.82.46.145

## TOTVS Educacional

### Rotina: BOLSAS EDU 50 082

* **[Ticket: DEDUINTEGRACOES-109]** - Criado o campo IDCONCESSAOBOLSA que passa a compor a chave primária das tabelas relacionadas.- Criado o AUTOINC para IDCONCESSAOBOLSA- Código defensivo para que o sistema continue funcionando em bases de clientes que rodaram e não rodaram o script de alteração das PKs ('CN.2017.07\_03')- Alteração em estruturas de tabelas do banco de dados- Alteração nos datasets tipados- Alteração nos dataservers- Alteração no assistente de concessão de bolsas futuras- Alteração nas actions de concessões e seus anexos- Alteração em serviços que consideram JOINs com a chave antiga da tabela- Reorganização dos datasets de concessão de bolsa, serviços de concessão de bolsas, habilitações de concessão de bolsa (Ensino Básico e Ensino Superior)

Arquivos: RM.Edu.Financeiro.Form.dll, RM.Edu.Financeiro.Server.dll, RM.Edu.Financeiro.Data.dll, RM.Edu.Utils.Server.dll, RM.Edu.Financeiro.Intf.dll, RM.Edu.Services.Server.dll, RM.Edu.Utils.Intf.dll, RM.Edu.Lib.Intf.dll, RM.Edu.Interfaces.Intf.dll

* **[Ticket: DEDUINTEGRACOES-109]** Ajuste para inclusão de mais de uma bolsa no contrato de períodos distintos para duas concessões de uma mesma bolsa

Arquivo: RM.Edu.Financeiro.Server.dll

# 11.82.46.152

## TOTVS Gestão de Custos

### Rotina: Erro ao abrir relatórios da PUC

* **[Ticket: MSAU-6058]** Corrigida falha ao tentar excluir registro na tela de Insumo

Arquivos: RM.Gch.Cadastros.Intf.dll, RM.Gch.dll, RM.Gch.Cadastros.Data.dll, RM.Gch.Processos.Data.dll, RM.Gch.Processos.Form.dll, RM.Gch.Utils.Intf.dll, RM.Gch.Hospitalar.Intf.dll, RM.Gch.Lancamentos.Intf.dll, RM.Gch.Processos.Intf.dll, RM.Gch.Utils.Server.dll, RM.Gch.Lancamentos.Data.dll, RM.Gch.Processos.Server.dll, RM.Gch.Cadastros.Form.dll, RM.Gch.Hospitalar.Data.dll, RM.Gch.Hospitalar.Form.dll, RM.Gch.Lancamentos.Form.dll

### Rotina: Implantação HCOR

* **[Ticket: SAUGCH01-46]** Ajustes no AssemblyInfo

Arquivos: RM.Gch.Cadastros.Intf.dll, RM.Gch.Cadastros.Data.dll, RM.Gch.Cadastros.Form.dll, RM.Gch.Processos.Form.dll, RM.Gch.Lancamentos.Data.dll, RM.Gch.Utils.Intf.dll, RM.Gch.Hospitalar.Intf.dll, RM.Gch.Lancamentos.Intf.dll, RM.Gch.Processos.Intf.dll, RM.Gch.Utils.Server.dll, RM.Gch.Processos.Server.dll, RM.Gch.Hospitalar.Data.dll, RM.Gch.Hospitalar.Form.dll, RM.Gch.Lancamentos.Form.dll, RM.Gch.Processos.Data.dll

# 11.82.46.158

## TOTVS Gestão de Custos

### Rotina: Ajustes no relatórios para 12.1.18

* **[Ticket: RMFIN-326]** Ajuste para calcular o custo fixo mesmo que não haja lançamento em conta (mas que tenha rateio recebido)

Arquivo: RM.Gch.Processos.Server.dll

### Rotina: Erro de violação de chave primária no Consumo Hospitalar

* **[Ticket: RMFIN-440]** Corrigido problema de violação de chave primária no processamento Esquema de Apuração - Consumo Hospitalar

Arquivo: RM.Gch.Processos.Server.dll

### Rotina: RATEIO

* **[Ticket: RMFIN-445]** Cálculo do custo unitário não estava considerando o peso do insumo.

Arquivo: RM.Gch.Processos.Server.dll

# 11.82.46.162

## TOTVS Gestão de Custos

### Rotina: RELATORIOS

* **[Ticket: 1678969 / RMFIN-807]** Ajuste no cálculo do custo unitário do paciente

Arquivo: RM.Gch.Processos.Server.dll

# 11.82.46.163

## TOTVS Gestão de Custos

### Rotina: Erro no cálculo das Diárias

* **[Ticket: 1675396 / RMFIN-808]** Ajuste no cálculo do tempo das diárias

Arquivo: RM.Gch.Processos.Server.dll

# 11.82.46.164

## TOTVS Gestão de Custos

### Rotina: Consumo Pacote (Esquema de Apuração)

* **[Ticket: RMFIN-805]** Ajuste para atualizar o tempo somente dos registros com quantidade utilizada maior que zero.

Arquivo: RM.Gch.Processos.Server.dll

# 11.82.46.165

## TOTVS Gestão Financeira

### Rotina: APLICACAO FINANCEIRA RESGATE FIN 017

* **[Ticket: 1155752 / FINANCEIRO01-1798]** Método Aplicacao.Encerrada() foi modificado.

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

# 11.82.46.171

## TOTVS Gestão de Custos

### Rotina: ESQUEMA DE APURAÇÃO

* **[Ticket: RMFIN-1580]** Ajustado cálculo do tempo do bloco para utilizar a coluna QTUTILIZADA.

Arquivo: RM.Gch.Processos.Server.dll

# 11.82.46.182

## TOTVS Gestão de Custos

### Rotina: RATEIO

* **[Ticket: 2917569 / DSAUGCH-77]** Corrigido cálculo do rateio que não estava considerando a vigência do critério de rateio pré-definido.

Arquivo: RM.Gch.Processos.Server.dll

# 11.82.46.183

## TOTVS Gestão de Custos

### Rotina: Ajustes no projeto 1180

* **[Ticket: DSAUGCH-419]** Removido arquivos que não são utilizados mais no projeto.

Arquivo: RM.Gch.Cadastros.Intf.dll
