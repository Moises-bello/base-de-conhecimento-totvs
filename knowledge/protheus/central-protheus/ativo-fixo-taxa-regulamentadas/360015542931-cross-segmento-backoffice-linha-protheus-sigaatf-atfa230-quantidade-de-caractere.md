---
article_id: 360015542931
category: Ativo Fixo - Taxa Regulamentadas
content_hash: e17f7a591f51ce64a040bc4de31867ed5323aacbbab80394b7b3521817966143
fetched_at: '2026-06-28T22:41:51.484617+00:00'
product: protheus
section_id: 1500001536121
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA230 - Quantidade
  de caracteres para a nova taxa
type: support-article
updated_at: '2023-12-04T19:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015542931-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA230-Quantidade-de-caracteres-para-a-nova-taxa
---

**Ocorrência**Na alteração da **taxa de depreciação** - rotina **ATFA230**, não há a possibilidade de informar valor superior a 999,9999%.  
   
 **Ambiente**Microsiga Protheus - Ativo Fixo - A partir da versão 12  
   
 **Causa**Devido a **configuração da picture**, na pergunta 5 do grupo AFA230, o campo possui limitação de 3 dígitos com 4 decimais.  
  
 **Solução**O campo poderá tratar valores superiores a 999,9999%, somente quando houver a alteração nas **configurações**da **picture** no grupo de perguntas da rotina.  
  
![AFA230_1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360010563671)  
  
Na **imagem**acima, temos um exemplo de configuração da pergunta, para que tenhamos o tratamento abaixo:  
  
![AFA230_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360010547872)
