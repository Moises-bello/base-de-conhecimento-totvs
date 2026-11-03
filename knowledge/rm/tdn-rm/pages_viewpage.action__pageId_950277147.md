---
content_hash: fabb6b57606a202d73dd9cdcb2aa0c468bb128f0ffd54676871bd9426bc3d68e
fetched_at: '2026-06-29T00:12:10.098355+00:00'
page_id: '950277147'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Base Aceleradora
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=950277147
version: 3
---

### Introdução

---

Facilitando a cópia de parâmetros entre coligadas ou bases externas, estamos disponibilizando as tabelas abaixo para que possam ser importadas em novas coligadas, de forma a agilizar o processo de implantação de uma nova coligada com dados que sejam comuns a todas.

### Procedimento para Utilização

---

As tabelas e *actions* abaixo estão prontas para serem utilizadas no processo de  dos Serviços Globais.

Lembrando que todas as tabelas abaixo podem ser associadas a um [Template único](https://tdn.totvs.com/pages/viewpage.action?pageId=592067102#C%C3%B3piadeDados-03.CADASTRODETEMPLATE), possibilitando uma importação mais simples de todos os parâmetros necessários.

| Parâmetros | Cadastro para cópia de dados |
| --- | --- |
| Cópia dos [Parâmetros de Integração Financeira.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105050) | Action Name: ImbCopyParamIntegracaoFinanceiraAction Wizard Parâmetro: GlbActionProcCopyColig Server Name: ImbCopyParamIntegracaoFinanceiraProc Tabela Principal: XALGPARAM Cód. Sistema: X (TOTVS Incorporação) |
| Cópia dos [Modelos de Contrato de Aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105135). | Action Name: ImbCopyContratoLocModeloAction Wizard Parâmetro: GlbParamsProcFormCopyColig Server Name: ImbCopyContratoLocModeloProc Tabela Principal: XALGCONTRATOLOCMODELO Cód. Sistema: X (TOTVS Incorporação) |
| Cópia dos [Tipos de Evento Financeiro.](https://tdn.totvs.com/display/LRM/Cadastros+-+Tipo+Evento+Financeiro) | Action Name: ImbCopyTipoEventoFinanceiroAction Wizard Parâmetro: GlbActionProcCopyColig Server Name: ImbCopyTipoEventoFinanceiroProc Tabela Principal: XALGTIPOEVENTOFINANCEIRO Cód. Sistema: X (TOTVS Incorporação) |
| Cópia dos [Tipos de Escalonamento.](https://tdn.totvs.com/pages/viewpage.action?pageId=520659202) | Action Name: ImbCopyTipoEscalonamentoAction Wizard Parâmetro: GlbActionProcCopyColig Server Name: ImbCopyTipoEscalonamentoProc Tabela Principal: XALGTIPOESCALONAMENTO Cód. Sistema: X (TOTVS Incorporação) |
| Cópia das [Regras de Vencimento de Contrato.](https://tdn.totvs.com/display/LRM/Cadastros+-+Regra+de+Vencimento) | Action Name: ImbCopyRegraVencimentoAction Wizard Parâmetro: GlbActionProcCopyColig Server Name: ImbCopyRegraVencimentoProc Tabela Principal: XALGVENCIMENTO Cód. Sistema: X (TOTVS Incorporação) |
| Cópia dos [Tipos de Locação.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105420) | Action Name: ImbCopyTipoContratoLocacaoAction  Wizard Parâmetro: GlbActionProcCopyColig Server Name: ImbCopyTipoContratoLocacaoProc  Tabela Principal: XALGCONTRATOLOCTIPOLOC  Cód. Sistema: X (TOTVS Incorporação) |
| Cópia dos [Motivos de Aditivo.](https://tdn.totvs.com/display/LRM/Cadastros+-+Motivo+de+Aditivo) | Action Name: ImbCopyMotivoAditivoRenovacaoAction Wizard Parâmetro: GlbParamsProcFormCopyColig Server Name: ImbCopyMotivoAditivoRenovacaoProc Tabela Principal: XALGMOTADIT Cód. Sistema: X (TOTVS Incorporação) |
| Cópia dos [Tipos de Consumo dos Medidores.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105201) | Action Name: ImbCopyCondTipoConsumoMedidorAction Wizard Parâmetro: GlbActionProcCopyColig Server Name: ImbCopyCondTipoConsumoMedidorProc Tabela Principal: XCONDTIPCONSMED Cód. Sistema: X (TOTVS Incorporação) |
| Cópia [dos Itens de Cobrança.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105029) | Action Name: ImbCopyItemCobrancaAction Wizard Parâmetro: GlbActionProcCopyColig Server Name: ImbCopyItemCobrancaProc Tabela Principal: XCONDITEMCOBR Cód. Sistema: X (TOTVS Incorporação) |
|  |  |
