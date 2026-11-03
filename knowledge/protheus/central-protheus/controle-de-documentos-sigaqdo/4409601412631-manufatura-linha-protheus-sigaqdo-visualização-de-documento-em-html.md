---
article_id: 4409601412631
category: Controle de Documentos (SIGAQDO)
content_hash: 301a6b146247afc3969f980db34fb873454869e9742f125dd64f72f99262e70f
fetched_at: '2026-06-28T22:42:29.972474+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Visualização de documento em HTML
type: support-article
updated_at: '2021-09-28T15:00:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409601412631-Manufatura-Linha-Protheus-SIGAQDO-Visualiza%C3%A7%C3%A3o-de-documento-em-HTML
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min** **Dúvida**No módulo **SIGAQDO - Controle de Documentos**, como visualizar um documento em **fase de leitura** no **formato HTML**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para visualizar um documento em **formato HTML** em fase de leitura, deverá validar os seguintes passos:  
  
1. Na rotina **QAXA010 - Usuários**, o campo **Tipo Word -** **QAA\_TPWORD** deve estar igual a **1 - HTML**;  
2. Definir um diretório dentro de **\Protheus\_Data\system** no parâmetro **MV\_QPATHWH - Define o diretório onde contém os arquivos dos Documentos gerados como HTML**;  
3. O parâmetro **MV\_QDCHTM - Define se na etapa de leitura, o usuário consulta o Documento em html** deve estar igual a **S - Sim**;  
4. O parâmetro **MV\_QDHTML - Define se grava o documento em html. 1 = Sim / 2 = Não**, deve estar igual a **1 - Sim**.
