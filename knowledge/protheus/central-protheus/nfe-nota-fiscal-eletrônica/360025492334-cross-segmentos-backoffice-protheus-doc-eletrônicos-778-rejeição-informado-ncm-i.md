---
article_id: 360025492334
category: NFe - Nota Fiscal Eletrônica
content_hash: 8aef049348e8fd5bcb2df0730a1e6ee30d8f86bd8bc988457cc0bf79ad617ac5
fetched_at: '2026-06-28T22:40:03.270305+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  778 Rejeição :
  Informado NCM inexistente'
type: support-article
updated_at: '2025-06-12T18:26:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025492334-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-778-Rejei%C3%A7%C3%A3o-Informado-NCM-inexistente
---

**Dúvida**Como resolver a rejeição abaixo:

778 Rejeição : Informado NCM inexistente ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Conforme a nota técnica 2016.001 será validado a **TAG Utrib** de acordo com o seu NCM essa alteração pode ser realizada no cadastro de produto no campo de unidade de medida, para as empresas que utilizarem em seu XML a mercadoria com unidade comercial **ucom** diferente da unidade tributada **utrib** pode ser cadastrada a segunda unidade de medida.

* **Importante:**

Tabela de NCM e respectiva Utrib, no Portal Nacional da NF-e <www.nfe.fazenda.gov.br>, **aba “Documentos”, opção “Diversos”.**

Os 8 (cinco) códigos incluídos na tabela de NCM publicada no Portal Nacional da NF-e estão realçados em verde com a informação de início ***de vigência***. Os 4 (quatro) códigos excluídos da tabela de NCM publicada no Portal Nacional da NF-e estão realçados em vermelho com a informação de ***fim de vigência.***

Para correção consulte as tabelas acima após isso se o NCM não for válido:

1. Preencha no campo do cadastro de produto ***Pos.IPI/NCM** "**B1\_POSIPI". para um NCM válido pela Sefaz.***

![20220411_141510.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5375552696215)

 2. Após isso, transmita novamente a ***Nota fiscal eletrônica.***

**Se necessário a Manutenção para o cadastro de NCM ( Clientes que não utilizam o SIGAEIC)**

1. Cadastre os ***NCMs conforme o link*** abaixo:

[MP - SIGACOM - Manutenção no cadastro NCM (Clientes que não utilizam o SIGAEIC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007540511)

* **Validação da Sefaz:**  
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039529934)
