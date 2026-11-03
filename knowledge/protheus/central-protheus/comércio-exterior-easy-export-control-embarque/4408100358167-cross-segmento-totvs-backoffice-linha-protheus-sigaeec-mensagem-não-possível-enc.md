---
article_id: 4408100358167
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 5ef4db24520f6107173ba1c92f1efae276eb928b54601c842a458bac689596a9
fetched_at: '2026-06-28T22:36:56.476738+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC-  Mensagem: Não
  possível encontrar o arquivo de retorno do pacote DUE'
type: support-article
updated_at: '2021-09-08T20:18:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408100358167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Mensagem-N%C3%A3o-poss%C3%ADvel-encontrar-o-arquivo-de-retorno-do-pacote-DUE
---

**Dúvida**Como faço para que a mensagem abaixo não seja exibida ao transmitir a DUE?  
"Não possível encontrar o arquivo de retorno do pacote DUE. Tente novamente. "

![ARQUIVO_DE_RETORNO_DUE.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408088475543/ARQUIVO_DE_RETORNO_DUE.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Export Control – Todas versões  
  
**Solução**Este erro de retorno da integração da DUE ocorre porque o executável do **java.exe** não foi informado corretamente no diretório Segue abaixo um exemplo de como deve ser exibido o diretório local onde é informado o executável do java: 

![CONFIGURA__O_PARA_USU_RIO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408090239383/CONFIGURA__O_PARA_USU_RIO.PNG)

Informado o diretório do executável a mensagem não será mais exibida e a tela de autenticação do certificado para transmissão da DUE será apresentada.  
  
**Saiba mais**  
[Declaração Única de Exportação (DUE) no SIGAEEC](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=455802907)
