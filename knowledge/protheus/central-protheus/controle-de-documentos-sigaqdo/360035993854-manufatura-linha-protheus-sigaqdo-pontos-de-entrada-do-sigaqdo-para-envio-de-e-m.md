---
article_id: 360035993854
category: Controle de Documentos (SIGAQDO)
content_hash: e68b522302a3e43ea6fa7bb52ebca6af3b0077866ad5a4df5c5b7a81fd7841e4
fetched_at: '2026-06-28T22:42:29.253828+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Pontos de Entrada do SIGAQDO para envio
  de e-mail
type: support-article
updated_at: '2021-05-26T13:51:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035993854-Manufatura-Linha-Protheus-SIGAQDO-Pontos-de-Entrada-do-SIGAQDO-para-envio-de-e-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Quais os **PE - Ponto de Entrada** do módulo **SIGAQDO - Controle de Documento** referente ao envio de *e-mail*?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Os **PEs** referente ao envio de *e-mail* são:

* [QDOSMAIL - Configuração do Layout de E-Mail](https://tdn.totvs.com/pages/releaseview.action?pageId=6801960)  
  Executado toda vez que for gerada alguma solicitação de alteração de documentos comunicando os usuários envolvidos por *e-mail*.
* [QDOVMAIL - Configuração do Layout de E-Mail](https://tdn.totvs.com/pages/releaseview.action?pageId=6801964)  
  Executado toda vez que algum documento estiver com a  data de validade vencida ou à vencer  comunicando os usuários envolvidos por *e-mail*.
* [Q050LOAD - Funções de Envio de E-mail](https://tdn.totvs.com/pages/releaseview.action?pageId=6801972)  
  Executado no início do módulo **SIGAQDO** para não executar as funções de envio de *e-mail* e verificação de pendências padrões.
* [Q050MAIL - Validação de envio de e-mails na abertura do módulo](https://tdn.totvs.com/pages/releaseview.action?pageId=6801983)  
  Executado no início da função **QDOLOAD** para efetuar a validação do envio de *e-mails* de pendência na abertura do módulo **SIGAQDO**. Para utilizar esse ponto de entrada não poderá existir o ponto de entrada **Q050LOAD** compilado pois o mesmo possui finalidade diferente e tem prioridade maior na execução. Lembrando que, para envio de *e-mails* de pendência também é preciso ativar o parâmetro **MV\_QDOAVEM - Define se haverá envio de e-mail para os usuários que estão com lançamentos pendentes**.
* [QD110PEN - Tratamento de Pendências Antes do Envio de E-mail](https://tdn.totvs.com/pages/releaseview.action?pageId=6801978)  
  Permite que seja efetuado tratamento nas pendências antes do envio de *e-mail*, e é acionado na distribuição de documentos após a gravação das pendências.
* [QDOAMAIL - Configuração de Layout para Ausência Temporária](https://tdn.totvs.com/pages/releaseview.action?pageId=6801902)  
  Executado toda vez que houver uma ausência temporária comunicando os usuários envolvidos por *e-mail*.
* [QDOAVMAIL - Importação do Documento](https://tdn.totvs.com/pages/releaseview.action?pageId=6801939)  
  Permite que seja enviado um *e-mail* ao final da importação do documento.
* [QDOBMAIL - Layout de E-mail para Transferências](https://tdn.totvs.com/pages/releaseview.action?pageId=6801941)  
  Executado toda vez que houver uma transferência comunicando os usuários envolvidos por *e-mail*.
* [QDODMAIL - Distribuição de Documentos](https://tdn.totvs.com/pages/releaseview.action?pageId=6801944)  
  Executado toda vez que houver distribuição de documentos comunicando os usuários envolvidos por *e-mail*.
* [QDOFMAIL - Layout para Documentos Referenciados](https://tdn.totvs.com/display/public/PROT/QDOFMAIL+-+Layout+para+Documentos+Referenciados)  
  Executado toda vez que houver documentos referenciados comunicando os usuários envolvidos por *e-mail.*
* [QDOIMAIL - Layout para solicitação de Novos Documentos](https://tdn.totvs.com/pages/releaseview.action?pageId=6801949)  
  Executado toda vez que houver solicitação de novos documentos comunicando os usuários com acesso a baixa de solicitação envolvidos por *e-mail*.
* [QDORMAIL - Layout de Email para Elaboração de Documentos](https://tdn.totvs.com/pages/releaseview.action?pageId=6801957)  
  Executado toda vez que for gerada alguma etapa de elaboração de documentos comunicando os usuários envolvidos por *e-mail*.
* [QDOTMAIL - Confirmação de email para treinamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=6801961)  
  Executado toda vez que for agendado/cancelado um treinamento comunicando os usuários envolvidos por *e-mail*.
* [QXQAMAIL - Gravação dos Campos](https://tdn.totvs.com/pages/releaseview.action?pageId=6801965)  
  Executado quando existe integração com o módulo **SIGAGPE - Gestão de Pessoas**, onde será executada a função **QA\_QUALITY** de integração somente na alteração de funcionários.
