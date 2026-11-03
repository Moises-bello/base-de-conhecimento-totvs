---
article_id: 1500010281721
category: RH - Cadastros
content_hash: 9be43509854f27aa474fad163ca3a7047bce0b0b4396ae57ebca78d9ab504a18
fetched_at: '2026-06-28T22:43:25.937893+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Local de gravação dos Requisitos das Funções -
  RJ_MEMOREQ
type: support-article
updated_at: '2026-06-25T11:08:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010281721-RH-Linha-Protheus-GPE-Local-de-grava%C3%A7%C3%A3o-dos-Requisitos-das-Fun%C3%A7%C3%B5es-RJ-MEMOREQ
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26496109699351)** Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual o local de gravação dos **Requisitos das Funções - campo RJ\_MEMOREQ?**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O sistema grava o conteúdo do campo **Requisitos da Função** na tabela **RDY - Memos.**  
  
Para identificar o conteúdo, abra a tabela **SRJ - Funções**,  localize o campo **RJ\_DESCREQ** que terá um **código único:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26496109705623)  
  
  
Posteriormente, abra a tabela **RDY - Memos**, e filtre pelo campo **RDY\_CHAVE igual ao código que está gravado na SRJ:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26496109709335)  
  
  
Após clicar em Ok o sistema trará a linha correspondente, e no campo **RDY\_TEXTO** está o que foi digitado no cadastro de Funções - campo Requisitos:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26496105465367)

**Saiba Mais**  
[Artigos Cadastros](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781894-RH-Cadastros)
