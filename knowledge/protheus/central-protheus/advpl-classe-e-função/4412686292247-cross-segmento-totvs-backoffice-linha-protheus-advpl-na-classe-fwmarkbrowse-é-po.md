---
article_id: 4412686292247
category: ADVPL - Classe e Função
content_hash: edaf77ccfc00890e81c58a6305a961c70f7918d7d0218d33bf5901a749a6b9ed
fetched_at: '2026-06-28T22:40:20.761766+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Na classe FwMarkBrowse
  é possível habilitar edição de uma célula específica
type: support-article
updated_at: '2021-11-10T16:56:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412686292247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Na-classe-FwMarkBrowse-%C3%A9-poss%C3%ADvel-habilitar-edi%C3%A7%C3%A3o-de-uma-c%C3%A9lula-espec%C3%ADfica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Na classe **FwMarkBrowse** é possível habilitar para edição uma célula específica?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**A classe **FwMarkBrowse** não foi construída com o intuito de edição de dados. Alguns métodos por motivos de herança de outras classes possuem propriedades para edição, porém na classe **FwMarkBrowse**, por padrão a edição não é suportada.  
Para editar dados na grid e marcar ou desmarcar uma linha, é indicado que você utilize a **MsNewGetdados** ou **MsBrGetDBase**onde você possui um controle maior das propriedades do objeto.   
Outra opção seria fazer um controle manual da edição, utilizando uma tecla de atalho.   
Por exemplo,  definir com a função **SetKey** que ao usuário apertar a tecla F2 vai chamar uma outra função e nessa função você cria uma nova tela para edição dos dados da linha posicionada.  
  
**Saiba mais**[FWMarkBrowse](https://tdn.totvs.com/display/public/PROT/FWMarkBrowse)   
[MsNewGetDados](https://tdn.totvs.com/display/framework/MsNewGetDados)   
[MsBrGetDBase](https://tdn.totvs.com/display/tec/MsBrGetDBase)   
[SetKey](https://tdn.totvs.com/display/tec/SetKey)
