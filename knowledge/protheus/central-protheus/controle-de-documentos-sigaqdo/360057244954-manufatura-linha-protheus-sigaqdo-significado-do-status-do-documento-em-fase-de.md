---
article_id: 360057244954
category: Controle de Documentos (SIGAQDO)
content_hash: 8fb4c979a8aafcfc0da5e97c23e251a1a090c11e1758b0981fdbedc987c01c1e
fetched_at: '2026-06-28T22:42:29.925141+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Significado do status do documento
  Em Fase de Implantação
type: support-article
updated_at: '2022-08-01T17:47:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057244954-Manufatura-Linha-Protheus-SIGAQDO-Significado-do-status-do-documento-Em-Fase-de-Implanta%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:42 min**  
**Dúvida**O que significa o status **Em Fase de Implantação** que é apresenta para alguns documentos ao clicar em **Detalhes** na rotina **QDOA050 - Cadastro de Documentos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Um documento é apresentado com o status **Em Fase de Implantação** quando já foi distribuído, mas o início da vigência é uma data futura. Isto é, o campo **QDH\_STATUS - Status** está com o conteúdo **L** e o conteúdo do campo **QDH\_DTVIG - Dat Vigência** é posterior a data atual.  
  
**Observação**  
No **Protheus** padrão os documentos com o status **Em Fase de Implantação** deixam de ser exibidos para os usuários na rotina **QDOA050** até que a **data de vigência** seja igual à **data atual**. Caso queira visualizar os documentos, existem os pontos de entrada **[QD050FIL](https://tdn.totvs.com/pages/releaseview.action?pageId=6801967)**ou **[QDOFILBR](https://tdn.totvs.com/pages/releaseview.action?pageId=6801945)**.
