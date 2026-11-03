---
article_id: 360060708833
category: NFe - Nota Fiscal Eletrônica
content_hash: 85b6fb52b688942b00025382c29e45db5431617a509e93212667969f94034cc8
fetched_at: '2026-06-28T22:40:00.373164+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 - Falha de
  Schema referente a TAG tpIntermedio'
type: support-article
updated_at: '2021-10-08T19:25:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060708833--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-Schema-referente-a-TAG-tpIntermedio
---

**Dúvida**Como solucionar a falha de Schema abaixo:

029 - Falha de Schema referente a TAG tpIntermedio  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Conforme a **documentação abaixo:**

[Manual de Orientação do Contribuinte - versão 6.00](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)

* **Página 186:**

![](https://totvssuporte.zendesk.com/attachments/token/iNLsPSm6Q0O9bi9bN8l7Qr5v8/?name=inline832416246.png)​

Esta TAG **tpIntermedio** é obrigatória.

**1-** Quando**não usa integração**com o**módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N**

**![20201201_145829.gif](https://totvssuporte.zendesk.com/hc/article_attachments/360101037393/20201201_145829.gif)**

**2-**Acesse a rotina **Livros Fiscais-> Atualizações->Movimentos->NF manual de Saída->Outras ações->Complementos->Importação:**

**![20201201_145142.gif](https://totvssuporte.zendesk.com/hc/article_attachments/360101036933/20201201_145142.gif)**

3 - Quando é informado a TAG **tpIntermedio=2 ou 3** informação  preenchida no campo **CD5\_INTERM.**

4 - É necessário ser preenchida a TAG **CNPJ** o campo que leva o conteúdo dessa TAG é  **CD5\_CNPJAE podendo ser preenchida uma das opções abaixo:**

**1=**Importação por conta própria;

**2=**Importação por conta e ordem;

**3=**Importação por encomenda;

5- Se informar tpIntermedio  **CD5\_INTERM= 1** o campo **CD5\_CNPJAE** poderá ficar em branco.

6- Exclua a nota e gere novamente preenchendo os **Livros fiscais corretamente.**
