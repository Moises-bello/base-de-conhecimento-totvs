---
article_id: 360034574553
category: TAF - REINF
content_hash: c7a7afb77179d24b481442014c01f53d06ccb092829ba6ac601d060a397537c2
fetched_at: '2026-06-28T22:41:34.657665+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Erro de transmissão MS1183
type: support-article
updated_at: '2025-07-07T12:09:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034574553-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-de-transmiss%C3%A3o-MS1183
---

**Dúvida**

Ao realizar a transmissão de um evento ocorre a seguinte rejeição:  
  
<codResp>MS1183</codResp>  
<dscResp>O valor da retenção {vlrRetencao} informado não pode ser maior que 11% da Base de cálculo da retenção da contribuição previdenciária {vlrBaseRet}.</dscResp>

![MS1183.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22338300487575)

**Ambiente**

TAF - SIGATAF  - A partir da versão 12.1.17  
  
**Solução**  
Esse incidente ocorre pois o valor do tributo está sendo arredondado e a Receita não aceita o arredondamento.  
  
Para solucionar essa ocorrência, realize os seguintes passos:

1 - Verificar os parâmetros abaixo, eles precisam estar com os valores a seguir:

**MV\_TAFRND** = 2 **MV\_RNDINS** = .F. - São utilizados somente no Protheus Fiscal **MV\_RNDSOBR** = .F. - São utilizados somente no Protheus Fiscal **MV\_RNDPREC** = 2 - São utilizados somente no Protheus Fiscal  
2 - Após verificar os parâmetros acima, localize a nota no TAF que está com o problema (pelo CNPJ do Participante da nota), altere e digite novamente a alíquota do Tributo, somente para atualizar o valor do tributo. Se a nota possuir mais de um item, realizar o passo para todos os itens.

Caminho para identificar documento no TAF:   
  
Atualizações -> Movimentos Fiscais -> Docs Fiscais/Eletr

3- Exclua a apuração inconsistente pelo menu Atualizações > Eventos Reinf > Periódicos.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente-?source=search)

4 - Apurar e transmitir novamente.
