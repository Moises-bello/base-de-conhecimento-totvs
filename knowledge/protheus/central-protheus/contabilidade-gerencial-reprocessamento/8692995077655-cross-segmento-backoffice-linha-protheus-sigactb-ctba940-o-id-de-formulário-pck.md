---
article_id: 8692995077655
category: Contabilidade Gerencial - Reprocessamento
content_hash: 5c448621e92da6deb4c93c2892b3a9c01fe8e81b4643e9e0fc104532afc3512b
fetched_at: '2026-06-28T22:40:41.941525+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: CROSS SEGMENTO - BACKOFFICE LINHA PROTHEUS - SIGACTB - CTBA940 - O id de formulário
  PCK_ACCESS não é válido
type: support-article
updated_at: '2023-11-14T15:13:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8692995077655-CROSS-SEGMENTO-BACKOFFICE-LINHA-PROTHEUS-SIGACTB-CTBA940-O-id-de-formul%C3%A1rio-PCK-ACCESS-n%C3%A3o-%C3%A9-v%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00**:01:00 min** **Dúvida**O que fazer quando ocorrer o erro O id de formulário PCK\_ACCESS não é válido ao executar o WIZARDUUID da rotina CTBA940?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Contabilidade Gerencial - a partir da versão 12  
  
**Solução**

1. Verifique se existe algum projeto em aberto, para isso acesse o **Configurador** do Protheus conforme abaixo:  
   ![](https://tdn.totvs.com.br/download/thumbnails/706149401/image2022-8-29_9-29-53.png?version=1&modificationDate=1661776595113&api=v2)  
   Verifique se existe algum projeto aberto com a descrição "**Inclusão de Campos UUID"**. Se existir, clique em **Outras Ações -> A Encerrar Projeto**.  
   Caso ocorra algum problema nesta etapa, atualize via ferramenta de banco de dados.
2. A tabela que grava estas informações é a **SYS\_BCAST\_PACKAGE\_XX**, onde **XX** é o código da empresa. Caso a tabela contenha informações, faça um **update** alterando o campo **PCK\_STATUS** para "**2**" filtrando o campo **PCK\_CODIGO,** com o código do projeto que esta em aberto.
3. Caso a tabela **SYS\_BCAST\_PACKAGE\_XX** **não** contenha informações (esteja em branco ou vazia) e a mensagem de erro continue a ser apresentada, será necessário **dropar** a tabela **SYS\_BCAST\_PACKAGE\_XX,** onde **XX** é o código da empresa (toda e qualquer manutenção de banco de dados, sugerimos analisa *in loco* para acompanhamento).

Após realizar qualquer um dos procedimentos acima, acesse novamente o **WIZARDUUID** e prossiga com a execução.

![wizard.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8693623488535/wizard.PNG)

Saiba mais:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=648811255>
