---
article_id: 360037123134
category: Call Center - Dúvidas Gerais
content_hash: e381245a47dec2db71d9d69716e785ae0f3b345bcc34e65334a0faa64240e00c
fetched_at: '2026-06-28T22:41:26.828785+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- Executar atendimentos
  com data futura na Agenda do Operador
type: support-article
updated_at: '2022-06-17T14:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037123134-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Executar-atendimentos-com-data-futura-na-Agenda-do-Operador
---

**Dúvida**

Ao efetuar a ligação com a data antecipada na **Agenda do Operador (TMKA380), a**parece a seguinte mensagem: "**Data Inválida - Listas com datas futuras não podem ser executadas antes".**Existe algum procedimento que permita efetuar atendimento antes do horário da agendado?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063570413/mceclip0.png)  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK – todas as versões.  
  
**Solução**

A rotina **Agenda do Operador (TMKA380)** possui uma validação que verifica se a **data da lista** / **atendimento** é **posterior**e emite o aviso indicando que:

"**Listas com datas futuras não podem ser executadas antes**","**Data inválida**"

Por padrão **não há como executar** estes contatos ou  **parâmetros** para desabilitar a validação do sistema.

Há um **Ponto de Entrada** para determinar data limite de execução de listas:  
  
**TK380DAT** - Definição de data limite: **<https://tdn.totvs.com/pages/viewpage.action?pageId=6787827>**
