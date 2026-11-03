---
article_id: 1500007816962
category: Controle de Auditorias (SIGAQAD)
content_hash: e11e44bb5676ca79cb05db534987da7386e7025f0e3981b44f31c51d4115762c
fetched_at: '2026-06-28T22:42:30.885872+00:00'
product: protheus
section_id: 360005876634
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQAD - QADA100 Não atualiza áreas auditadas
  no QADA150
type: support-article
updated_at: '2021-08-16T14:05:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007816962-Manufatura-Linha-Protheus-SIGAQAD-QADA100-N%C3%A3o-atualiza-%C3%A1reas-auditadas-no-QADA150
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Por que a área auditada informada no **QADA100 - Auditorias** não é atualizada na rotina **QADA150 - Agenda de Auditorias**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Auditorias (SIGAQAD) - Todas as versões  
  
**Solução**A agenda de auditorias tem a função de pré-cadastro da auditoria. Isto é, as informações cadastradas na rotina **QADA150** serão apresentadas na rotina **QADA100**. No entanto, esta integração não ocorre de forma inversa, da **Auditoria** para a **Agenda de Auditorias**. Todas as validações e ajustes devem ser realizados por meio da rotina **QADA100** e em caso de alterações, estas informações não serão replicadas para a rotina **QADA150**.  
Lembrando também que o cadastro de uma agenda de auditoria não é obrigatório para a inclusão da auditoria.
