---
article_id: 11126102423831
category: Comércio Exterior - Easy Export Control - Relatórios
content_hash: 163c34175ef35e7cc4958bcff7eb9999afb4b7b1b2b569b2ae6f9b371a693f3f
fetched_at: '2026-06-28T22:36:59.924812+00:00'
product: protheus
section_id: 1500001538161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Erro na criação
  do VBScript 516
type: support-article
updated_at: '2024-10-24T18:04:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11126102423831-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Erro-na-cria%C3%A7%C3%A3o-do-VBScript-516
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao tentar emitir o "**Documento Commercial Invoice**" no **Embarque do SIGAEEC** é apresentada a seguinte mensagem: **Erro na criação do VBScript 516**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11120905617431)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – a partir da versão 12.1.27  
  
**Solução**Para a solução do ocorrido, é necessário desinstalar o programa "**Warsaw**" da máquina local do colaborador.  
Este programa impede a geração dos arquivos necessários para geração dos documentos no diretório **%TEMP%** do **Windows**.

Após remoção o documento pode ser gerado.

**Imagem do programa a ser removido**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11128250822167)
