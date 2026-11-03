---
article_id: 1500007497542
category: Controle de Documentos (SIGAQDO)
content_hash: a4f582c80a441f3df1c2168f7b95866b598331b8aedaec81c94816dcb21fb688
fetched_at: '2026-06-28T22:42:29.112012+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - HELP QACEQPATH
type: support-article
updated_at: '2021-05-06T13:01:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007497542-Manufatura-Linha-Protheus-SIGAQDO-HELP-QACEQPATH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min**  
**Ocorrência**Na rotina de **Cadastro de Documentos -** **QDOA050** ao tentar acessar um documento ocorre o Help **QACQPATH - Acesso aos diretórios de arquivo dos documentos negado!**.  
**Ambiente**Totvs Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O help **QACEQPATH** é apresentado quando existe inconsistência na localização do documento através do parâmetro **MV\_QPATHW - Define o diretório onde contem os arquivos dos Documentos.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Validar se o conteúdo do parâmetro **MV\_QPATHW** corresponde ao diretório onde está localizado o documento. No padrão o conteúdo do parâmetro é **/SYSTEM/DOCS**;  
2. Confirmar se o documento em questão está gravado na pasta **DOCS**;  
3. Verificar se o campo **QDH\_NOMDOC** está preenchido com o nome correto do arquivo gerado.
