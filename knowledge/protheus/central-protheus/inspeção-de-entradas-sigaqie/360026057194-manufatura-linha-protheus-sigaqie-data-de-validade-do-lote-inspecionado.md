---
article_id: 360026057194
category: Inspeção de Entradas (SIGAQIE)
content_hash: d5f32b7066d0a7cb82d3f8923dfbf363e987560becbadc1e0a3bccbe9889ef2a
fetched_at: '2026-06-28T22:42:26.938402+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Data de validade do lote inspecionado
type: support-article
updated_at: '2021-09-08T12:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026057194-Manufatura-Linha-Protheus-SIGAQIE-Data-de-validade-do-lote-inspecionado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:15 min**  
**Dúvida**Na rotina de **Resultados - QIEA215**, na aba **Laudo Geral**, é informada uma data de validade. Qual é a regra utilizada para definir esta data?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**A data de validade do lote será considerada conforme o conteúdo informado no parâmetro **MV\_QVALLOT - Define o criterio para a Validade do Lote Lib/Rej**, seguindo as seguintes condições:  
  
**• MV\_QVALLOT  = 1** -Será mantida a **validade do lote** informado no **Documento de entrada**, alterando a validade do lote informada no módulo **Inspeção de Entradas**.  
• **MV\_QVALLOT = 2.**Será considerada a **validade do lote** informada no **Resultado da Inspeção de entrada**, alterando a validade no módulo de **Estoque**.  
• **MV\_QVALLOT = 3.**O Protheus irá considerar a **maior validade para o lote**, considerando a validade do lote informado no **documento de entrada** e o informado no **resultado da inspeção de entrada**, sendo que as informações dos campos também serão alteradas de acordo com a validade assumida pelo sistema.
