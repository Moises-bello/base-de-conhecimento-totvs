---
article_id: 360049722893
category: Controle de Auditorias (SIGAQAD)
content_hash: 4f3ad51867c1533f3a90830d90f9d654e9031e2b491cadb3aec0c982c0847710
fetched_at: '2026-06-28T22:42:30.864207+00:00'
product: protheus
section_id: 360005876634
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQAD - Parâmetro MV_AUDSLID
type: support-article
updated_at: '2022-05-05T20:04:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049722893-Manufatura-Linha-Protheus-SIGAQAD-Par%C3%A2metro-MV-AUDSLID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Qual a função do parâmetro **MV\_AUDSLID - Indica se somente o auditor líder poderá efetuar manutenção na auditoria**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Auditorias (SIGAQAD) - Todas as versões  
  
**Solução**O parâmetro **MV\_AUDSLID**é utilizado no módulo **SIGAQAD - Controle de Auditorias** e define a permissão de visualização e alteração de **Auditorias**, **Agendas**, **Questionários** e **emissão de relatórios de Checklist e de Auditorias**. Os **Auditores Líderes** possuem acesso total de inclusão, alteração, exclusão e visualização de Auditorias, em qualquer fase em que ela esteja, isto é, em aberto ou encerrada.  
Quando o parâmetro **MV\_AUDSLID** está como **T - True - Verdadeiro**, por exemplo, somente o auditor responsável pode alterar a auditoria.   
Caso o parâmetro **MV\_AUDSLID** estiver igual a **F - False - Falso**, os auditores informados na equipe de apoio poderão alterar também. Portanto, outros usuários não poderão alterar mesmo o usuário que cadastrou a auditoria, caso o mesmo não estiver envolvido no processo de auditoria como auditor.  
  
**Saiba mais**  
Para visualizar as permissões se este parâmetro for configurado como**T** ou como **F**, acessar o documento: [Controle de Auditorias](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigaqad.htm)
