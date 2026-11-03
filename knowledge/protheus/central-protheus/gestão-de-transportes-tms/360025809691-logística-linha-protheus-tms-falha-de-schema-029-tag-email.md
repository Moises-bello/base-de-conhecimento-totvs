---
article_id: 360025809691
category: Gestão de Transportes (TMS)
content_hash: ac5fd7bff6d05bd8c914819586169c7447ada0a195e299723727ddd48e0a808a
fetched_at: '2026-06-28T22:45:27.765738+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Falha de SCHEMA 029 tag <email>
type: support-article
updated_at: '2022-05-02T12:47:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025809691-Log%C3%ADstica-Linha-Protheus-TMS-Falha-de-SCHEMA-029-tag-email
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:51 min****Ocorrência**  
Falha de *schema* **029** *tag***<email>**.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024634391/Capturar.PNG)

**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**   
Esse incidente ocorre, pois a parametrização do Sistema está incorreta.  
  
**Solução**Para solucionar o erro de *schema* em questão é necessário a verificação de dois pontos:

1. É necessário adicionar no arquivo **appserver.ini** do seu **TSS** a seguinte informação:  
   **SPED\_DELMAIL -** Define se deverá ser apagada a informação **e-mail** do **XML**do **CT-e**.  
   Os valores possíveis para essa *tag* são **0 - Não** e **1 - Sim**
2. Verifique como está preenchido o campo **Email - A1\_EMAIL**do cliente destinatário do **CT-e**. Não pode conter nenhum carácter especial ou espaços.

**Glossário  
CT-e -**Conhecimento de Transporte eletrônico **TSS** - TOTVS SPED Service  
**XML -** Extensible Markup Language
