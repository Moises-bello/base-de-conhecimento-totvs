---
article_id: 360046238394
category: Controle de Documentos (SIGAQDO)
content_hash: a52974c582cd95ee61cf7f5b1a6c7a274bd6fae4acdba8c1b11f3f254a9e728e
fetched_at: '2026-06-28T22:42:29.151264+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDO50NE
type: support-article
updated_at: '2021-05-24T17:15:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046238394-Manufatura-Linha-Protheus-SIGAQDO-Help-QDO50NE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**Ao tentar finalizar a inclusão de documentos na rotina **QDOA050 - Cadastro de Documentos** aparece o *help* **QDO50NE**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* **QDO50NE** é exibido quando a estrutura do diretório para gravação do **Documento** não existe conforme o parâmetro **MV\_QPATHW - Define o diretório onde contem os arquivos dos Documentos**. O parâmetro **MV\_QPATHW** define o diretório que contém os arquivos dos documentos. Deve-se criar o diretório **DOCS** dentro do diretório **SYSTEM**, à partir do diretório de instalação do Sistema.  
  
**Solução**Para solucionar essa ocorrência, crie o diretório **DOCS** dentro do diretório **SYSTEM**, à partir do diretório de instalação do Sistema, conforme parâmetro **MV\_QPATHW**.
