---
article_id: 360021107672
category: Controle de Documentos (SIGAQDO)
content_hash: 62051a2f2c396a7429731f4fd9368f746e05e3e7a8228b3342fdc20483519129
fetched_at: '2026-06-28T22:42:29.055137+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Este documento possui revisão, não
  poderá ser cancelado
type: support-article
updated_at: '2024-06-18T19:11:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021107672-Manufatura-Linha-Protheus-SIGAQDO-Este-documento-possui-revis%C3%A3o-n%C3%A3o-poder%C3%A1-ser-cancelado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar cancelar um documento é apresentada a mensagem **Este documento possui revisão, não poderá ser cancelado!**  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
 **Causa**Esta mensagem é apresentada quando existe alguma revisão ou pendência para o documento. O Sistema permitirá o cancelamento apenas quando todas as pendências estiverem baixadas, inclusive as pendências de distribuição e leitura.  
  
 **Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **QDOA050 -** **Cadastro de Documentos**;  
2. Selecione o documento em questão e clique no botão **Outras Ações** > **Detalhe**;  
3. Verifique se existe alguma pendência com o status **Vermelho**. Estas pendências precisarão ser baixadas para que o Sistema permita o cancelamento do documento.
