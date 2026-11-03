---
article_id: 1500003318501
category: Controle de Documentos (SIGAQDO)
content_hash: 161d7201934083691b54338d45b12d0ec454ff5b8604e71f36d0795deaa5c396
fetched_at: '2026-06-28T22:42:29.173092+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QD_DOTNEXT ao incluir um tipo
  de documento
type: support-article
updated_at: '2021-05-24T19:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003318501-Manufatura-Linha-Protheus-SIGAQDO-Help-QD-DOTNEXT-ao-incluir-um-tipo-de-documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao incluir um tipo de documento na rotina **QDOA020 - Tipo de Documento**, apresenta o *help* **QD\_DOTNEXT**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
  
**Causa**Esse *help* ocorre nas seguintes situações:

* Não foi informado o diretório no parâmetro **MV\_QPATHWD - Define o diretório onde contém os arquivos dos Documentos gerados como Padrão**;
* O diretório informado no parâmetro **MV\_QPATHWD** é inválido;
* Não existe o arquivo modelo no diretório indicado no parâmetro **MV\_QPATHWD**;
* Quando o arquivo informado no campo **Modelo** da rotina **QDOA020** não possui a extensão **.DOT**.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Informe um diretório válido no parâmetro **MV\_QPATHWD**;
2. Verifique se o arquivo modelo consta no diretório informado no parâmetro **MV\_QPATHWD**;
3. Verifique se no campo **Modelo** foi informado o nome do arquivo que consta no diretório informado com a extensão **.DOT**.
