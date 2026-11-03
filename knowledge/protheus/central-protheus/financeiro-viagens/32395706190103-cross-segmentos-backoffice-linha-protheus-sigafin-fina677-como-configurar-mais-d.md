---
article_id: 32395706190103
category: Financeiro - Viagens
content_hash: 93b968b7e38c30315c7cfae900ec42387e292b1a020becc2438ba0160ced4347
fetched_at: '2026-06-28T22:38:21.421187+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA677 - Como configurar
  mais de um aprovador para aprovação no processo de prestação de contas
type: support-article
updated_at: '2025-05-27T16:55:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32395706190103-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Como-configurar-mais-de-um-aprovador-para-aprova%C3%A7%C3%A3o-no-processo-de-presta%C3%A7%C3%A3o-de-contas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32395702435223) Tempo aproximado para leitura: **00****:04:00 min** **Dúvida**Como configurar mais de um aprovador para aprovação no processo de prestação de contas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**Neste caso é necessário utilizar o ponto de entrada F677GERAPR, desta forma será possível incluir mais de um aprovador no fluxo de aprovações das prestações de contas.

Documentação do ponto de entrada:

F677GERAPR - [Alteração do Fluxo de Aprovadores (Prestação de Contas)](https://tdn.totvs.com/pages/releaseview.action?pageId=198956516)

**OBS:** O código inserido no ponto de entrada, deve ser o código do campo **RD0\_CODIGO**.

Na rotina **FINA691** ou via parâmetro **MV\_RESGVIA** deve adicionar o código **SIGA** dos usuários que serão aprovadores de viagens e separa-los por ponto e virgula **";"**, o campo seria o **USR\_ID** ou pode acessar o cadastro de usuários no módulo **SIGACFG** e validar o código**.**

Após localizar o código dos usuários envolvidos, deve inserir no parâmetro **MV\_RESGVIA** ou no campo da **FINA691 "Assistente de configuração".**
