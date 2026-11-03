---
article_id: 40104142750615
category: Inspeção de Processos (SIGAQIP)
content_hash: cc1cecd3c9e47bc66ce21d20050ce52a08cd8ef8fe63d91ab4948ccfcc4f1680
fetched_at: '2026-06-28T22:42:25.866487+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Numeração Automática de Ensaios
type: support-article
updated_at: '2026-04-30T11:48:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40104142750615-Manufatura-Linha-Protheus-SIGAQIP-Numera%C3%A7%C3%A3o-Autom%C3%A1tica-de-Ensaios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40104142726935) Tempo aproximado para leitura: **00:00:40 min**  
  
**Dúvida**  
Na rotina **QIPA010 - Ensaios** o campo **Ensaio - QP1\_ENSAIO** possui n**umeração automática** ou **inicializador padrão**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**  
No Produto Padrão, a rotina **QIPA010** não prevê numeração automática ou inicializador para o campo **QP1\_ENSAIO**. O preenchimento deste campo deve ser realizado manualmente pelo usuário no momento do cadastro do ensaio.

Conforme a política de atendimento do Suporte Técnico TOTVS, o escopo de atuação é restrito a situações relacionadas ao comportamento do **Produto Padrão**.

**Importante**  
Caso haja necessidade de automatizar este preenchimento, a implementação deverá ser realizada através de uma **customização** (como a criação de um gatilho ou inicializador de dicionário via Configurador), visto que tal funcionalidade não está nativamente disponível na rotina. Para este tipo de demanda, recomendamos o contato com o seu AR (Agente de Relacionamento) ou **Consultoria** ***In-Loco**.*
