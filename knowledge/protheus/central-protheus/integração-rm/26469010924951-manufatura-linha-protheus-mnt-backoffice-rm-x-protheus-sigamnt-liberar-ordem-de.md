---
article_id: 26469010924951
category: Integração RM
content_hash: d1c4ab42932fa869a140718eb4936232bbab275901a92af3b628bb60941d91ba
fetched_at: '2026-06-28T22:42:36.854975+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Backoffice RM x Protheus SigaMNT - Liberar
  Ordem de Serviço
type: support-article
updated_at: '2024-10-11T20:10:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26469010924951-Manufatura-Linha-Protheus-MNT-Backoffice-RM-x-Protheus-SigaMNT-Liberar-Ordem-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26469017730967)*** Tempo aproximado para leitura: **00:01:50 min** **Dúvida**Como é realizado o processo de **Liberar Ordem de Serviço - O.S - MNTA490** integrado ao **Backoffice RM x Protheus Manutenção de Ativos - SIGAMNT**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Todas as versões  
  
**Solução**A funcionalidade liberar **Ordem de Serviço - O.S** é executada através do **Protheus Manutenção de Ativos - SIGAMNT** e tem o objetivo de alterar o *Status* de uma **O.S** que esteja **Pendente**. Quando uma **O.S** é incluída, um dos seus campos é responsável por informar seu *status* inicial podendo ser alterado para **Liberado** e fazendo com que a **Ordem de Manutenção** seja criada no **Backoffice RM**. Serão enviados ao **Backoffice RM** somente as **O.S** que forem alteradas do *Status* **Pendente** para **Liberado** ficando a cargo do usuário a decisão de criá-lo ou não como **Liberada**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26958247748887)

Executando o processo:1 - Cadastrar manualmente o **DExPARA de Coligada e Filial RM x Empresas e Filiais Protheus**;  
2 - Inclusão de **Ordem de serviço Manual Preventiva** ou **Corretiva** com insumos previstos;  
3 - Acessar o **Protheus SIGAMNT - Atualizações - Ordem de Serviço - Liberar O.S. - MNTA490**;4 - Selecione uma **O.S.** com *status* **Pendente** e execute o processo de **Liberação**;5 - Serão enviadas as mensagens abaixo ao **Backoffice RM** para incluir:

* **MAINTENANCEORDER** - **Ordem de Manutenção**;
* **REQUEST - S.A. - Solicitação de Armazém** ou **SC - Solicitação de compra** dos insumos previstos.

**Saiba mais**- Para gerar **S.A.**, veja o artigo do *link* [Manufatura - Linha Protheus - MNT - Procedimento para gerar a Solicitação de Armazém](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026182131)  
- Para gerar **S.C.** veja o artigo do *link* [Manufatura - Linha Protheus - MNT - Procedimento para gerar empenho e S.C para O.S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025671132)  
- Para informações dos campos do **XML** das duas mensagens geradas, veja os *links*:  
[Mapeamento MaintenanceOrder](https://tdn.totvs.com/display/INT/MNT0019_BackOfficeRMxSigaMNT_Mapeamento_MaintenanceOrder)  
[Mapeamento Request](https://tdn.totvs.com/display/INT/MNT0017_BackOfficeRMxSigaMNT_Mapeamento_Request)
