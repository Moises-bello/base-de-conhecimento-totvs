---
article_id: 360028377912
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 896ff94160394e39702d411917e8adf63543fea3ee230e39eac8ab3b0b540afd
fetched_at: '2026-06-28T22:39:47.722708+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Cadastro de condição
  de pagamento '
type: support-article
updated_at: '2022-05-02T14:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028377912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Cadastro-de-condi%C3%A7%C3%A3o-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como cadastrar a condição de  Pagamento no módulo SIGAEIC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução** As condições inseridas neste cadastro identificam a forma de pagamento das importações. Elas serão baseadas na Data de Embarque dos processos ou campo informado no parâmetro MV\_DTB\_APD.   
  
O sistema apresenta três tipos de condições de pagamento, são elas:

* **À Vista:** Pagamento único do valor FOB com vencimento na data de embarque.
* **Normal:** Pagamento único do valor FOB, com data de vencimento de 1 a 899 dias a contar da data do embarque.
* **Parcelado:** Destinado ao parcelamento do valor FOB em até 10 parcelas, inclusive parcelas antecipadas. Os vencimentos desses pagamentos são calculados á partir da data de embarque.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029102911/mceclip0.png)

Exemplo - Como cadastrar Condições de Pagamento:   
  
**Condição de pagamento Normal:**  
1. Selecione o menu “Atualizações\Tabelas\Condições de Pag”.

2. Clique na opção “Incluir” e na pasta Cadastrais, informe os seguintes dados: ![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029103552/mceclip12.png)

3. Para condições de pagamento do tipo normal, os campos da pasta “Parcelas” estarão desabilitados.

4. Clique sobre o botão “Confirmar” para gravar.   
  
**Condição de pagamento a vista:**  
1. Clique novamente na opção “Incluir” e na pasta Cadastrais, informe os seguintes dados:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029101492/mceclip2.png)

2. Para condições de pagamento do tipo a vista, o campo “No. de Dias” será preenchido automaticamente pelo sistema com o valor -1 e os campos da pasta “Parcelas” estarão desabilitados. 3. Clique sobre o botão “Confirmar” para gravar.  
 **Condição de pagamento parcelado:**  
1. Clique novamente na opção “Incluir” e na pasta Cadastrais, informe os seguintes dados:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029103591/mceclip3.png)

2. Para condições de pagamento do tipo parcelado, o campo “No. de Dias” será preenchido automaticamente pelo sistema com o valor 901. Para que este conteúdo não seja considerado para pagamento ou vencimento. Será usado neste exemplo, os percentuais de cada parcela e os prazos de vencimento foram definidos nos campos da pasta “Parcelas”, conforme demonstrado a seguir:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029101912/mceclip4.png)

3. Confira os dados e clique sobre o botão “Confirmar” para gravar.   
  
**Condição de pagamento antecipado:**  
1. Clique novamente na opção “Incluir” e na pasta Cadastrais, informe os seguintes dados:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029101972/mceclip5.png)

2. Condições de pagamento antecipado são do tipo “Parcelado”. No exemplo que foi usado na pasta “Parcelas” foi preenchido o percentual a ser pago e o número de dias negativo para o vencimento, conforme demonstrado a seguir:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029103931/mceclip6.png)

3. Confira os dados e clique sobre o botão “Confirmar” para gravar.   
  
4. É possível configurar condições de pagamento mesclando parcelas com vencimento antes e depois da data de embarque, conforme exemplo abaixo:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029102712/mceclip9.png)

Os tipos de Cobertura "Cambial" determinam os campos a serem informados:   
Cobertura

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029104451/mceclip10.png)

**Obs.:** Quando integrado com SIGAFIN deve-se preencher o campo **C.Pagto SIGA** informando uma condição de pagamento existente no SIGAFIN, esta servira apenas para integrar os dados ao SIGAFIN, no entanto os vencimento e parcelas serão sempre calculado pelo SIGAEIC, independente da configuração da condição de pagamento do SIGAFIN.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029104531/mceclip11.png)
