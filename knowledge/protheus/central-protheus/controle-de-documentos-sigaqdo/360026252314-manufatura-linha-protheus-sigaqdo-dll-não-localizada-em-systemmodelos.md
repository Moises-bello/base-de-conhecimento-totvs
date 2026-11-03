---
article_id: 360026252314
category: Controle de Documentos (SIGAQDO)
content_hash: 1b124507a76b093cf78c37d81c0e6df0fe97077962807e64ba60b6949dc3d801
fetched_at: '2026-06-28T22:42:29.006056+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - DLL não localizada em \SYSTEM\MODELOS\
type: support-article
updated_at: '2021-05-12T13:39:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026252314-Manufatura-Linha-Protheus-SIGAQDO-DLL-n%C3%A3o-localizada-em-SYSTEM-MODELOS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar visualizar um documento ocorre a mensagem **DLL não localizada em \SYSTEM\MODELOS\**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Essa mensagem ocorre devido a descontinuação do componente disponibilizado pela **Microsoft**, a ferramenta **TOTVS OFFICE VIEWER** está descontinuada e não sofrerá mais manutenções.  
  
**Solução**Recomendamos a utilização do **SIGAQDO** com **Word View** ou **Word**.  
Para que esta mensagem não seja mais exibida, o parâmetro **MV\_QDPRVW - Determina se será utilizado o 'Preview' na visualização dos documentos** deve ser alterado para **1 - Não**.  
O aplicativo **TOTVS Office Viewer** não possui suporte para abertura de documentos com senha, apenas o **Word View** e o **Word**. Dessa forma, na abertura de documentos que utilizem senha deve ser utilizada a opção **Somente Leitura**.
