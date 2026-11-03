---
article_id: 4412569002647
category: Materiais - Compras (SIGACOM)
content_hash: 17de0f50a7ca9d54af658ac8abf44b3d5c19dc86d481acd689630056ef34788d
fetched_at: '2026-06-28T22:41:12.752770+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGACOM - Integração
  Compras x Ativo Fixo
type: support-article
updated_at: '2024-07-22T12:02:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412569002647-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-Compras-x-Ativo-Fixo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25069900085911) Tempo aproximado para leitura: **00:02:00** **Dúvida**

Como é configurado a Integração do Compras x Ativo Fixo ?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Versão 12  
  
**Solução**

Conforme configuração do TES (Tipo de Entrada) é possível registrar automaticamente a entrada de ativos fixos na empresa. Para isto, basta configurar o campo **Atualiza Ativo** como **Sim** no Cadastro de TES.

Além disso, o Microsiga Protheus® permite desmembrar os itens do documento de entrada pela quantidade unitária, com o objetivo de agilizar a classificação dos bens na integração com o Ambiente Ativo Fixo.

Para tratar esta função, devem ser observados os seguintes procedimentos:

* O campo **Desm. It. ATF** (Desmembra Itens no Ativo), no cadastro de Tipos de Entradas e Saídas (SF4), deve ser configurado com **Sim**(padrão **Não**).
* No cadastro dos produtos, que devem ter a quantidade desmembrada por uma unidade, configurar o campo **Tipo de Entrada** com o código de uma TES que possua o campo **Desm. It. ATF.** definido com **Sim**.
* Ao incluir o documento de entrada, informando para estes produtos quantidades inteiras, quando o item possuir integração com o Ativo Fixo, não é permitido digitar quantidade fracionada (exemplo **123,21**), quando o campo **Atualiza Ativo** do cadastro de Tipos de Entrada e Saída estiver configurado com **Sim**.
* Em um mesmo documento de entrada podem ser incluídos produtos com desmembramento para o ativo fixo ou não (definido pela TES).

***Obs:***

Na integração do Compras com o Ativo Fixo para que o codigo CIAP do item do documento de entrada  (***D1\_CODCIAP***) seja preenchido, o sistema verifica se está ativado o campo da TES ***F4\_CIAP*** para então inserir o bem no CIAP e gravar o campo ***D1\_CODCIAP***.

***Saiba Mais:***

[Integração com o ambiente Ativo Fixo (MATA103 - SIGACOM)](https://tdn.totvs.com/x/iSVKEg)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais campos estão envolvidos na Integração Documento de Entrada x Ativo fixo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23453308774935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-campos-est%C3%A3o-envolvidos-na-integra%C3%A7%C3%A3o-Documento-de-entrada-x-Ativo-fixo?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
