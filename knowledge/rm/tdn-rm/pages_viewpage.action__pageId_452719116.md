---
content_hash: 884167de95001a4670e3445748d2d443f313d85e2408987accbe58083d7c8a37
fetched_at: '2026-06-29T00:10:03.654539+00:00'
page_id: '452719116'
product: rm
source: tdn-rm
title: Escala de horário e Descanso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719116
version: 11
---

Este módulo permite realizar a alteração do horário por escada dos funcionários.  
 

**Importante:**

Para atender ao eSocial, quando for realizado o processo de alteração por Escala-Horário e Descanso será gerado um Gatilho na fila de eventos  S-2206 – Alteração de Contrato de Trabalho para o horário que for atualizado no cadastro do funcionário (PFUNC).

**Observação:** Para o eSocial é considerado somente o horário contratual, ou seja, somente será gerado gatilho quando alterar o horário no cadastro do funcionário (PFUNC), não olhará histórico de horário.

A alteração por escala não refere-se à uma mudança contratual. Sendo assim, somente o último horário informado na escala será registrado no cadastro do funcionário (PFUNC), gerando então um único gatilho do S-2206.

**Exemplo:**

Processada a alteração de escala de horário para o funcionário alterando o horário nas datas 06/01/2018, 07/01/2018, 12/01/2018 e 16/01/2018.

Sistema cadastrou o histórico das alterações corretamente, porém somente o ultimo horário foi alterado no cadastrado do funcionário.

Neste caso será gerado somente um gatilho S-2206 com a informação do horário do cadastro do funcionário (PFUNC).
