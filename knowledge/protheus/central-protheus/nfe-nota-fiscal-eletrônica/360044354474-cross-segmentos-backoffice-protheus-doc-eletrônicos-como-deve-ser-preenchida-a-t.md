---
article_id: 360044354474
category: NFe - Nota Fiscal Eletrônica
content_hash: d89cc570167a3c7245972eed56683e7ee96e5d19deec6205bf48d243fbea188e
fetched_at: '2026-06-28T22:40:00.288048+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como deve ser
  preenchida a Tag <dest> para operações relativa à devolução '
type: support-article
updated_at: '2022-05-09T18:11:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044354474--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-deve-ser-preenchida-a-Tag-dest-para-opera%C3%A7%C3%B5es-relativa-%C3%A0-devolu%C3%A7%C3%A3o
---

**Dúvida**

Como deve ser preenchida a tag<dest> relativa à devolução, quando o destinatário mudar de endereço ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Tag <dest> relativa à devolução deve reproduzir todos os elementos constantes da Nota Fiscal anterior.  
  
***Configuração:***  
  
- MV\_HISTTAB igual a True (T).   
Dessa maneira após configurar o parâmetro, cada alteração realizada será gravado um registro na tabela Histórico de Alterações (AIF).  
  
-Deve ser referenciada a nota de origem ao realizar a devolução, para que seja montada a tag finnfe=4.

- F2\_TIPO=D (Devolução)  
  
Dessa maneira será montado os dados com base no xml da nota de origem.
