---
article_id: 360062273094
category: ADVPL - Rotina Automática
content_hash: 8cecd008a665dc17278bfa1c95c569d5bc019af0e93fbd90dd71484491cd7add
fetched_at: '2026-06-28T22:40:24.215867+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -   GPEA010 não grava
  todos campos
type: support-article
updated_at: '2021-12-29T13:09:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062273094-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-GPEA010-n%C3%A3o-grava-todos-campos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min****Dúvida**Ao chamar a rotina automática GPEA010 dentro do menu do Protheus ela não esta gravando todos campos informados, como resolver?  
  
**Ambiente**Protheus - ADVPL - A partir da versão 12.  
  
**Solução**Conforme a regras de negócio da rotina alguns campos não tem o módulo selecionado (marcado) no configurador conforme abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003985381/mceclip0.png)  
Nesse caso, é necessário identificar o módulo que está chamando a ExecAuto e desbloquear o campo via configurador na aba Módulos conforme a imagem acima.  
  
Observação:  
A rotina conforme as regras de negócio não está disponível para realizar a chamada dentro do módulo SIGAATF.  
  
**Saiba mais**  
[Exemplo de Rotina Automática - Cadastro de Funcionários - GPEA010](https://tdn.totvs.com/pages/releaseview.action?pageId=6079003)
