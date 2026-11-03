---
article_id: 360046374334
category: Controle de Documentos (SIGAQDO)
content_hash: 233158b067fe7d67131e6daaacb7e0a53943b98f3dbfe7391a019e8cf170289c
fetched_at: '2026-06-28T22:42:29.165571+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QD_DOCNEXT ao gerar revisão
type: support-article
updated_at: '2021-05-24T17:41:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046374334-Manufatura-Linha-Protheus-SIGAQDO-Help-QD-DOCNEXT-ao-gerar-revis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**O Sistema apresenta o *help* **QD\_DOCNEXT** ao tentar gerar a revisão do documento na rotina **QDOA050 - Cadastro de Documentos**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* **QD\_DOCNEXT** ocorre quando não foi encontrado o documento texto no caminho especificado. Quando um documento é gerado, é criado um arquivo com extensão **.CEL** no servidor.  
Para cada documento criado é gerado um arquivo com nome diferente e para saber qual é o código do arquivo criado é necessário verificar o conteúdo do campo **QDH\_NOMDOC - Nome Arquivo**.   
Também é preciso verificar se o arquivo que consta no campo **QDH\_NOMDOC** está no diretório informado no diretório **MV\_QPATHW - Define o diretório onde contem os arquivos dos Documentos** ou **MV\_QPATHWT - Define o diretório do Client onde ficarão os Documentos gerados pelo Sistema**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verificar o código do arquivo criado analisando o conteúdo do campo **QDH\_NOMDOC**;  
2. Validar se o arquivo que consta no campo **QDH\_NOMDOC** está no diretório informado no diretório **MV\_QPATHW** ou **MV\_QPATHWT**.
