---
article_id: 360046709113
category: NFe - Nota Fiscal Eletrônica
content_hash: 32e6d221b3cde2d993b591c1c3002000bc235acb6148fa3dc8f0e31cb6fc90d1
fetched_at: '2026-06-28T22:40:03.145724+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  029 : Falha de
  schema na Tag NCM'
type: support-article
updated_at: '2025-06-12T18:23:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046709113-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-NCM
---

**Dúvida**Como solucionar a falha de Schema referente a TAG NCM ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Ao gerar falha de Schema referente ao ***NCM*** verifique se o seu XML gerou conforme o exemplo abaixo em branco ou com pontos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065496794)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076857033)

2. Conforme o XML acima não foi preenchido o ***NCM***que é ***obrigatório***

3. Preencher o NCM no cadastro de Produto o campo ***Pos.IPI/NCM** **B1\_POSIPI***

![20220411_141510.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17174903899031)

 4. Após isso, transmita novamente a ***Nota fiscal eletrônica.***

**Se necessário a Manutenção para o cadastro de NCM ( Clientes que não utilizam o SIGAEIC)**

1. Cadastre os ***NCMs conforme o link*** abaixo:

[MP - SIGACOM - Manutenção no cadastro NCM (Clientes que não utilizam o SIGAEIC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007540511)

Conforme a nota técnica 2016.001 será validado a **TAG Utrib** de acordo com o seu NCM essa alteração pode ser realizada no cadastro de produto no campo de unidade de medida, para as empresas que utilizarem em seu XML a mercadoria com unidade comercial **ucom** diferente da unidade tributada **utrib** pode ser cadastrada a segunda unidade de medida.

* **Importante:**

Tabela de NCM e respectiva Utrib, no Portal Nacional da NF-e <www.nfe.fazenda.gov.br>, **aba “Documentos”, opção “Diversos”.**

Os 8 (cinco) códigos incluídos na tabela de NCM publicada no Portal Nacional da NF-e estão realçados em verde com a informação de início ***de vigência***. Os 4 (quatro) códigos excluídos da tabela de NCM publicada no Portal Nacional da NF-e estão realçados em vermelho com a informação de ***fim de vigência.***
