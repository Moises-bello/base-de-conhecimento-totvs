---
article_id: 360018813571
category: PCO - Bloqueios
content_hash: f4f2ab3255b2b489f052423fd9216daa2a9e5f0c0c9e6883cc086dc8855f8f5b
fetched_at: '2026-06-28T22:37:13.486982+00:00'
product: protheus
section_id: 1500001550782
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA193 - Como configurar
  o aviso/mensagem da ocorrência de bloqueios por % Margem?
type: support-article
updated_at: '2026-03-03T18:34:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018813571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA193-Como-configurar-o-aviso-mensagem-da-ocorr%C3%AAncia-de-bloqueios-por-Margem
---

**Dúvida**

Como configurar o aviso/mensagem da ocorrência de bloqueios por %Margem?

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

Dentro da Rotina Cubos Gerenciais (PCOA193), temos a possibilidade de configurar o envio de mensagem e/ou aviso da ocorrência de bloqueios do Planejamento e Controle Orçamentário (SIGAPCO), configurados por meio do **Tipos de Bloqueios**.

Dentro de **Tipos de Bloqueios** > **Outros** temos o campo: **AKJ\_PRCMRG** que indica a porcentagem da margem para o aviso de bloqueio orçamentário.

**(% Margem Blq.)**

![](http://tdn.totvs.com/download/attachments/269553042/%25MargemBlq.png?version=1&modificationDate=1481723527000&api=v2)

Obs: Esse aviso sobre o atingimento da margem para bloqueio orçamentário poderá ser emitida para o usuário(em tela) e um e-mail para os administradores, ou somente um e-mail será enviado aos administradores (para tanto se faz necessário a configuração do campo: **AKJ\_TIPMSG (Tipo de Mensagem)**

Ao atingir o percentual definido, será apresentado a seguinte tela:

![](http://tdn.totvs.com/download/attachments/269553042/Aviso2.png?version=1&modificationDate=1481731413000&api=v2)
