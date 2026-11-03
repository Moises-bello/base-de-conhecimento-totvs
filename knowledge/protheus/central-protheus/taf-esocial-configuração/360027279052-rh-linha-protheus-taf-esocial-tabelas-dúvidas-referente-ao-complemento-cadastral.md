---
article_id: 360027279052
category: TAF - eSocial - Configuração
content_hash: 5a30049b4b9a16ff1c3e11e0933826dcf7aee6a68e78e233bdfe181af7e2f4a5
fetched_at: '2026-06-28T22:45:14.522304+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Tabelas - Dúvidas referente ao Complemento
  Cadastral no TAF (S-1000)
type: support-article
updated_at: '2024-06-25T21:12:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027279052-RH-Linha-Protheus-TAF-eSocial-Tabelas-D%C3%BAvidas-referente-ao-Complemento-Cadastral-no-TAF-S-1000
---

**Dúvida**Qual a configuração correta para o Complemento Cadastral (TAFA050) deverá ser 1X1 ou 1XN?  
  
**Ambiente**RH - Linha Protheus - TAF - eSocial - Release à partir da 12.1.33

**Solução**

**O cliente pode utilizar o TAF para realizar a integração de diversas obrigações ao governo, como por exemplo eSocial e Reinf. No caso do eSocial ele pode optar por centralizar dados de diversas filiais em uma centralizadora (N:1), já no caso do Reinf os registros devem ser integrados cada um em sua devida filial (1:1).**

Para atender a obrigação da REINF deverá ser 1X1, caso use a configuração do eSocial 1X1, deverá seguir conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030027352)

Deixar o campo Outras Filiais a filial que destina este 1X1:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052339514)

Para os casos que utilizem o eSocial como 1xN deverá seguir a configuração abaixo:

Criar o parâmetro MV\_TAFCFGE e deixa-lo como .T., segue link de como cria-lo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=455804537>

Deverá selecionar a empresa Matriz e flegar a opção Matriz:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027048611)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027048391)

Na Matriz amarre as filiais, na aba Outras Filiais:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027049231)

Nas empresas filiais deverá deixar a Aba Outras Filiais em branco.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056375793)
