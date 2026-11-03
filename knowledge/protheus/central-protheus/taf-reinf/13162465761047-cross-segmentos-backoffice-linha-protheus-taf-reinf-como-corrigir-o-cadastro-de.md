---
article_id: 13162465761047
category: TAF - REINF
content_hash: 068842738e462145b13ec09994e8ef65e38e42f5f98655a411d8632e44e50ca5
fetched_at: '2026-06-28T22:41:33.412723+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos - Backoffice Linha Protheus - TAF - REINF - Como corrigir o
  cadastro de Fornecedor que foi integrado para o TAF com atividade = Produtor Rural?
type: support-article
updated_at: '2023-03-30T16:48:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13162465761047-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Como-corrigir-o-cadastro-de-Fornecedor-que-foi-integrado-para-o-TAF-com-atividade-Produtor-Rural
---

**Dúvida**Efetuei a integração dos Fornecedores para o TAF, porém foram integrados com o campo C1H\_RAMO = 4 - Produtor Rural. Como corrigir o cadastro?

**Ambiente**  
TAF – SIGATAF – A partir da versão 12.1.25  
  
**Solução**

Ao efetuar a integração de um cadastro com a opção Produtor Rural, pode ocorrer do evento R-2055 ser habilitado incorretamente para apuração.

Para correção, deve-se deixar o campo A2\_TIPORUR no cadastro de Fornecedor **vazio:**

**![C1H_RAMO_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13162426291095)**

Caso este campo esteja preenchido, por ele ser reservado para Produtor Rural, mesmo que na aba Outros, campo A2\_INDRUR esteja como 0 - não, o registro será levado para o TAF com a Atividade = Produtor Rural.

Este campo deve permanecer vazio e após, reintegrar o cadastro para o TAF, caso necessário.
