---
article_id: 360044970173
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 04576bcad7e9c0772e3350ba9ffb4a2cae8519f6985c086908abfbf647279f9b
fetched_at: '2026-06-28T22:42:27.958485+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Help A090DEMITI
type: support-article
updated_at: '2021-05-12T20:57:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044970173-Manufatura-Linha-Protheus-SIGAQNC-Help-A090DEMITI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00 min**  
**Ocorrência**No módulo **SIGAQNC - Controle de Não Conformidades**, ao alterar a **Matrícula** do usuário na rotina **QNCA030 - Cadastro de Plano de Ação** é apresentado o *help* **A090DEMITI - Funcionário está com situação de demitido no cadastro**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Esse *help* é exibido quando o **Código de Matrícula** informado está como inativo na rotina **QAXA010 - Responsáveis/Usuários** ou com **Data fim** preenchido, ou ainda, a **Data fim** ou **Data início** é maior ou igual à data base do Sistema.  
  
**Solução**Para solucionar essa ocorrência, verifique os seguintes campos da rotina **QAXA010** para a **Matrícula** informada:  
1. **Status Usr.** como **1 - Ativo**;  
2. **Data Fim** não preenchido ou data menor do que a data base do Sistema;  
3. **Data Início** menor do que a data base do Sistema.
