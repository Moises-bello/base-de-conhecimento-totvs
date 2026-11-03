---
article_id: 40131128571415
category: Funcionários
content_hash: 79ba33aa46e0fd2819cffa7d69120e662da40b97bf0a1b1bc395d18089a8b67c
fetched_at: '2026-06-28T22:47:03.124300+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Histórico de salário visão duplicado SmartUI
type: support-article
updated_at: '2026-05-05T17:07:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40131128571415-RH-RM-FOP-Hist%C3%B3rico-de-sal%C3%A1rio-vis%C3%A3o-duplicado-SmartUI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40131113168535) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como resolver o problema de visão duplicada no histórico de salários da Smart UI?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - 12.1.2506 ou superiores.  
  
**Solução**  
Atualmente devido a**transição e coexistência** da tela do Histórico Salarial e a nova tela em Smart UI, foi identificado o comportamento onde o menu de anexos associado ao registro do colaborador está sendo renderizado em duplicidade.

Após a avaliação do cenário, confirmamos que a duplicação do menu será corrigida através do procedimento abaixo.

**1 - Acesso ao Sistema:** Inicie o sistema (`RM.exe`).

**2 - Menu Serviços Globais:** Selecione o menu **Serviços Globais**.

![](https://tdn.totvs.com/download/attachments/1015576361/image-2025-11-19_9-7-3.png?version=1&modificationDate=1763554025113&api=v2)

**3 - Aba Serviços:** Acesse a aba **Serviços**.

**4 - Ações Anexas:** Clique na opção **Actions Anexas**.

![](https://tdn.totvs.com/download/attachments/1015576361/image-2025-11-19_9-8-37.png?version=1&modificationDate=1763554119627&api=v2)

**5 - Filtro:** Filtre pela *Action* Principal: `FopFuncAction`

**6 - Exclusão:** **Exclua** a *Action* Anexo com o nome: `FopActionHistoricoSalarialWinForm`**.**

**![](https://tdn.totvs.com/download/attachments/1015576361/image-2025-11-19_9-18-30.png?version=1&modificationDate=1763554712560&api=v2)**

**7 - Reinicialização:** Efetue **Logout** e **Login** no sistema.

Após a conclusão do procedimento, acesse o **Cadastro de Funcionários** e **valide** se os anexos do Histórico Salarial estão aparecendo corretamente (sem duplicidade).

**Saiba mais**

[**DT - Smart UI - Visão duplicada**](https://tdn.totvs.com/pages/releaseview.action?pageId=1015576361)
