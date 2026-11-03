---
content_hash: d62b929411e7ed501564cb553a542a95e8070f5bae2974ae7228b765370da2ed
fetched_at: '2026-06-29T00:11:11.500162+00:00'
page_id: '647457680'
product: rm
source: tdn-rm
title: Validação de assinatura de Assemblies
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=647457680
version: 9
---

Para ativar a **validação de assinatura de assemblies**, consulte: 

Caso a tag **ALLOWASSEMBLYSIGNCHECK** esteja ativa no Host.config, o RM passará a realizar a validação da assinatura dos **assemblies** carregados em tempo de execução. Caso algum desses **assemblies** não esteja assinado corretamente, o Host irá parar de responder, como medida de segurança contra injeção direta.

Uma mensagem similar a seguinte será exibida caso ocorra a tentativa de carregamento de algum **assembly** não assinado no Host:

Obs.: A partir da versão **12.1.2606**, a mensagem passa a ser exibida no host, conforme ilustrado na imagem abaixo.

Vale ressaltar que as APIs também estão realizando a mesma validação e não irão responder caso algum assembly não esteja assinado.

Deve ser reforçado que essa é uma regra de negócio e ***NÃO*** um bug. Assim sendo, é aconselhável não realizar alterações, como decompilações nas DLL's do RM, pois estas irão bloquear o acesso ao Host.
