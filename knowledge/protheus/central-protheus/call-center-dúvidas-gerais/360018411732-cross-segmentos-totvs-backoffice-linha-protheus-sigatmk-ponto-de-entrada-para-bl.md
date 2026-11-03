---
article_id: 360018411732
category: Call Center - Dúvidas Gerais
content_hash: a5c2a274b30ce2668acf7d74b62d1085c9cd6f8cc234ae053ad1f2e4be4d6804
fetched_at: '2026-06-28T22:41:26.879958+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice -(Linha Protheus-)SIGATMK-Ponto de entrada
  para bloqueio da edição dos dados dos contatos na tela de Seleção de Entidades
type: support-article
updated_at: '2022-06-17T18:10:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018411732-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ponto-de-entrada-para-bloqueio-da-edi%C3%A7%C3%A3o-dos-dados-dos-contatos-na-tela-de-Sele%C3%A7%C3%A3o-de-Entidades
---

**Dúvida**

Como desligar /bloquear a edição dos dados do Contato ao selecionar a entidade no atendimento Telemarketing?

**Ambiente**

Cross Segmentos-TOTVS Backoffice -(Linha Protheus-)SIGATMK - a partir da versão 11.  
  
**Solução**

Ao configurar o parâmetro **MV\_TMKF3** o sistema passa a apresentar uma tela diferenciada para seleção de entidades no Atendimento Telemarketing, nesta tela o sistema permite que o Operador inclua novos contatos vinculados à entidade selecionada, além de permitir a alteração dos dados dos Contatos já cadastrados.

Algumas empresas não permitem que o Operador tenha acesso ao cadastro ou alteração destes dados e para esta necessidade foi criado o ponto de entrada TMKXCTET - Retorno em array.

Utilize o ponto de entrada **TMKXCTET** - Retorno em array

<http://tdn.totvs.com/display/public/PROT/TMKXCTET+-+Retorno+em+array>

 O mesmo define a permissão de alteração/inclusão de contatos e os campos que o usuário poderá alterar dos contatos.
