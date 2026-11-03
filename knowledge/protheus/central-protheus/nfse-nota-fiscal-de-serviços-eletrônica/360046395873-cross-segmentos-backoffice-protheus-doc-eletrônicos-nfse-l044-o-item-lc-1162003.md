---
article_id: 360046395873
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6b2d2aeaa57b64131ca6c63b6071847c1bf534bd4d589749993e1fd4ac55d37b
fetched_at: '2026-06-28T22:39:57.530429+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - L044 - O
  item LC 116/2003 informado não corresponde ao CNAE informado
type: support-article
updated_at: '2025-07-02T14:12:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046395873-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-L044-O-item-LC-116-2003-informado-n%C3%A3o-corresponde-ao-CNAE-informado
---

**Ocorrência**Ao realizar a transmissão de um RPS é apresentado a seguinte rejeição: **L044 - O item LC 116/2003 informado não corresponde ao CNAE informado.**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Este erro está relacionado ao uso incorreto dos conteúdos de uma relação de Código de Serviço x Atividade (CNAE) que a própria prefeitura disponibiliza. Exemplo abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065596633/mceclip1.png)  
  
Onde no caso foi rejeitada a nota pelo fato dos conteúdos não terem relação.  
Lembrando que eles são informados nos campos: B1\_CODISS (Código de Serviço) e B1\_CNAE (CNAE - Atividade) no Cadastro de Produtos.  
*Obs.: Caso seja utilizado a rotina MATA018 (Indicador de Produtos) deverão ser informados nos campos BZ\_CODISS e BZ\_CNAE.*  
  
**Solução**Caso no próprio portal da prefeitura não disponibilize essa relação, deverá entrar em contato para entender essa combinação e quais códigos que deverão ser utilizados.
