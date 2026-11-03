---
article_id: 40219160912151
category: Ferrramentas de análise
content_hash: 339481bd882f3bc5ec032c14c0515a5914c77d06a48f1a24f6585235a1ccd367
fetched_at: '2026-06-28T22:46:32.145503+00:00'
product: rm
section_id: 1500000835161
source: central-rm
title: RH - RM - PTO - Coluna PROCESSO da AAFDT e PROCESSOLOG da ABATFUNLOG
type: support-article
updated_at: '2026-05-04T18:51:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40219160912151-RH-RM-PTO-Coluna-PROCESSO-da-AAFDT-e-PROCESSOLOG-da-ABATFUNLOG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40219177627159) Tempo aproximado para leitura: **00:01:10 min**  
  
**Dúvida**  
Quais são as definições e origens registradas nas colunas PROCESSO da tabela AAFDT e PROCESSOLOG da tabela ABATFUNLOG no módulo RM TOTVS Automação de Ponto?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**  
As tabelas AAFDT e ABATFUNLOG armazenam informações sobre a origem e o processo de criação ou alteração das marcações de ponto. Abaixo estão as descrições dos códigos e origens mapeadas:

### **Coluna PROCESSO da tabela AAFDT**

| Código | Descrição |
| --- | --- |
| 0 | Importação manual |
| 1 | Edição individual de batidas |
| 2 | Lançamento global de horário |
| 3 | Inclusão manual |
| 4 | Lançamento global de batidas |
| 5 | Edição de várias batidas do espelho |
| 6 | Aprovação de batidas |
| 7 | Gerada pelo Conversor |
| 8 | Cancelar Movimento |
| 9 | Desaprova batidas |
| 10 | Importação de XML |
| 11 | Customizações |

### **Coluna PROCESSOLOG da tabela ABATFUNLOG**

| Identificador de Processo | Origem/Ação |
| --- | --- |
| RM.Pto.Batida.PtoEntradaBatidaFuncData | RMPortal - Visão de subordinados - Anexo - Entrada de batidas - Botão Incluir batida |
| RM.Pto.Batida.Grid.PtoGridBatidaFuncData | RMPortal - Visão de subordinados - Anexo - Entrada de batidas (digitação direta) |
| PtoProcEntradaBatidas | Entrada de Batidas (Menu Cadastro) |
| RM.Pto.Batida.PtoBatidaData | Inclusão de batidas diretamente no espelho |
| RM.Pto.Batida.Grid.PtoEspelhoCartaoData | Edição de batidas dentro do espelho de ponto |
| RM.Pto.LancamentoDeBatidas.Data.PtoProcLancamentoBatidaPeloPlanejado | Processo de lançamento de batidas pelo horário planejado |
| Microsoft SQL Server Management Studio - Consulta | Insert/Delete diretamente via banco pelo SQL SERVER |
| SqlDbx Personal | Insert/Delete diretamente via banco pelo SQL DBX |
| RM.Pto.Batida.PtoProcExcluirBatidas | Reprovação de Batidas |
| RM.Pto.AprovarBatidas.PtoAprovarBatidasProc | Aprovação de batidas |
| RM.Pto.Batida.PtoBatidaFuncBaseData | Geolocalização |
