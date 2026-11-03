---
article_id: 360028868432
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: c931e61b1cb69fd42120269c61b785d40a8e7a839ae798c38c9e40e5dae2b48a
fetched_at: '2026-06-28T22:40:47.724129+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - ERRO CheckList
  ECF : CONTAS SUPERIORES (C1O_CTASUP) '
type: support-article
updated_at: '2021-11-12T15:22:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028868432-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-ERRO-CheckList-ECF-CONTAS-SUPERIORES-C1O-CTASUP
---

**Dúvida**

4. AS CONTAS SUPERIORES (C1O\_CTASUP) ABAIXO NAO EXISTEM NO PLANO  
DE CONTAS UTILIZADO (TABELA CT1). POR FAVOR, VERIFIQUE.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030285432/mceclip0.png)  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 11.80

**Causa**

O sistema esta buscando da " CONTA: 11"  a "CONTA SUPERIOR: 94DB57CB-57CA-48CC-818C-84A2094AD6CA" na tabela C1O

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030252471/mceclip2.png)

Diante disse veja o exemplo abaixo TABELA C1O como sistema grava os dados

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030285652/mceclip3.png)

* C1O\_CTASUP  da conta 23601001 existe C1O\_ID (conta anterior)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030252711/mceclip4.png)

* O sistema gravou :
* conta 23601 (Sintética) com o C1O\_ID : a6c0b938-f09b-a273-eca3-63880f059925
* conta 23601001(Analitica)  com o C1O\_ID : c2ed4be2-89f4-b026-2f93-804308554179 e C1O\_CTASUP : a6c0b938-f09b-a273-eca3-63880f059925

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030252811/mceclip5.png)

**Solução**

Diante disso necessário  verificar  se durante a integração da Rotina de Escrituração(CTBS001) com o TAF é apresentado algum erro ou advertência impedindo que a todas as contas (Sintéticas e analíticas ) sejam integradas para tabela do TAF C1O

Exemplo de erro  que pode ser apresentado ao realizar a integração da rotina de escrituração(CTBS001) com o TAF

[MP - SIGACTB - ECF - O valor '110101' informado no campo Conta Superior (C1O\_CTASUP) não existe na base de dados.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008352587-MP-SIGACTB-ECF-O-valor-110101-informado-no-campo-Conta-Superior-C1O-CTASUP-n%C3%A3o-existe-na-base-de-dados-?source=search)
