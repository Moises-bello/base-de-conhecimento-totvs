---
article_id: 360018569392
category: Financeiro - Baixas a Receber
content_hash: 7454e9db0a809d5c525a39a01c0657e8e32e90a1c22fa39cd8fb8f3a2efafca8
fetched_at: '2026-06-28T22:37:43.820146+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - SIGAFIN - FINA070 / FINA080 -
  Qual a diferença entre o cancelamento e a exclusão nas baixa de titulo
type: support-article
updated_at: '2026-03-19T11:37:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018569392-Cross-Segmentos-Linha-BackOffice-Protheus-SIGAFIN-FINA070-FINA080-Qual-a-diferen%C3%A7a-entre-o-cancelamento-e-a-exclus%C3%A3o-nas-baixa-de-titulo
---

**Dúvida**  
Qual é a diferença entre cancelar e excluir uma baixa de título?  
  
**Ambiente**  
Microsiga protheus – Financeiro – A partir da versão 11.80  
  
  
**Solução**  
Há duas formas de reverter as baixas efetuadas:  
  
**Cancelar:** O cancelamento gera um registro de estorno na movimentação bancária **SE5**, para que posteriormente o extrato bancário mostre o histórico de operações efetuadas.  
Nesta operação, o sistema permite a informação de um histórico. Neste caso, a **Consulta Posição de Clientes** e **Consulta Posição Fornecedores** destacam como informação histórica das movimentações.

**Excluir:** Não é gerado movimento na tabela **SE5** referente à exclusão, e o registro do movimento é deletado. Dessa forma, no extrato não é evidenciada a movimentação de baixa nem a respectiva exclusão.

Entretanto, foi realizada uma reestruturação no processo de movimentação, na qual os movimentos excluídos passaram a ser registrados na **FK5**, sendo essa a tabela utilizada para exibição de dados no**SmartView (novo relatório) e novo conciliador backoffice.**

No sistema de conciliação anterior, os registros eram validados com base na tabela **SE5**, motivo pelo qual as exclusões de baixa não eram refletidas no relatório de extrato bancário (**FINR470**). Por essa razão, é fundamental verificar se as divergências entre os relatórios não estão relacionadas as exclusões previamente efetuadas.

No novo conciliador foi implementado um filtro com a opção de **remover registros estornados**, o que impede a exibição de dados referentes a exclusões e cancelamentos.

**Documentação relacionada à nova reestruturação**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Diferença entre Extrato bancário FINR470 x Smart View FINSV014](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32576681343127-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Diferen%C3%A7a-entre-Extrato-banc%C3%A1rio-FINR470-x-Smart-View-FINSV014)

**Saiba mais**  
[Baixas Pagar Manual - FINA080 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12)  
[FINA070 - Baixas a Receber - Protheus 12](https://tdn.totvs.com/display/public/PROT/FINA070+-++Baixas+a+Receber+-+Protheus+12)  
[MP - SIGAFIN - Descrições dos tipos de movimentações do campo E5\_TIPODOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022538171-MP-SIGAFIN-Descri%C3%A7%C3%B5es-dos-tipos-de-movimenta%C3%A7%C3%B5es-do-campo-E5-TIPODOC-)
