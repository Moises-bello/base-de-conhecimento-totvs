---
article_id: 360059005874
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1478790888251a65b4ae8d5d48a7900968bc11dbcb5fdfbb85c3abf881bfc986
fetched_at: '2026-06-28T22:39:57.578579+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - NENHUMA NOTA
  FOI CANCELADA
type: support-article
updated_at: '2025-06-25T21:17:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059005874-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-NENHUMA-NOTA-FOI-CANCELADA
---

**Ocorrência**Ao tentar realizar a transmissão de um Cancelamento de RPS ocorre a mensagem: "NENHUMA NOTA FOI CANCELADA".  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101662513/mceclip0.png)  
 **Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Esse problema geralmente ocorre por alguns principais motivos:  
  
I. RPS não foi previamente monitorado, não atualizando a tabela SF3 com os dados de autorização.  
II. Campos na SF3 como F3\_DTCANC não está preenchido com a data de exclusão do documento.  
III. Duplicidade de registro para o mesmo RPS na SF3.  
  
**Solução**O primeiro passo é verificar se a nota autorizada foi monitorada, uma vez que **uma das premissas para transmissão de cancelamento é somente ser possível para notas previamente autorizadas.**  
  
Segundo é verificar se o F3\_DTCANC foi preenchido após excluir o Documento de Saída.  
  
E por último verificar se não possui duplicidade na tabela SF3 filtrando por (F3\_NFISCAL, F3\_SERIE e F3\_ESPECIE = RPS).  
  
*Obs.: Os dois últimos pontos citados é de responsabilidade da equipe Fiscal.*Por padrão os campos da SF3 precisam estar da seguinte maneira para a rotina FISA022 acatar o cancelamento:  
  
F3\_CODRSEF = 'S'  
F3\_CODRET = '111'  
F3\_OBSERV = 'NF CANCELADA'  
F3\_DTCANC = 'AAAAMMDD'
