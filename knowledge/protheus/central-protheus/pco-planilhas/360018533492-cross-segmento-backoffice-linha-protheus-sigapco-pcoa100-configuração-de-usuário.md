---
article_id: 360018533492
category: PCO - Planilhas
content_hash: d548e6389b2259c41740e2561996b6f9d8031253f085a5826b26371a8b5afb71
fetched_at: '2026-06-28T22:37:05.375438+00:00'
product: protheus
section_id: 1500001539901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA100  Configuração
  de usuário para alteração da Fase da Planilha Orçamentária
type: support-article
updated_at: '2022-06-07T20:34:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018533492-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA100-Configura%C3%A7%C3%A3o-de-usu%C3%A1rio-para-altera%C3%A7%C3%A3o-da-Fase-da-Planilha-Or%C3%A7ament%C3%A1ria
---

**Dúvida**Como configurar o usuário para realizar a alteração da Fase da Planilha Orçamentária (Rotina: PCOA100 )?

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

Para que seja possível configurar um usuário com acesso a função > **Altera Fase** (Fase orçamentária) será necessário incluir o **ID** deste **user** dentro do parâmetro:

**MV\_PCOUNI**

***Help do Parâmetro:****Contém o código de usuários que terão autorização de gerenciar o cadastro de Unidades Orçamentarias.*

*Exemplo:*

![](http://tdn.totvs.com/download/attachments/244939055/MV_PCOUNI.png?version=2&modificationDate=1472655209000&api=v2)

Neste caso somente os usuários de ID:   
**000000;000006;000009;000010** poderão alterar a Fase da Planilha Orçamentária
