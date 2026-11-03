---
article_id: 4405233895959
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 62476625fb01d601993ce8a9b1bf9e34bbd46850ff71d36d594cab1989cc60f7
fetched_at: '2026-06-28T22:39:47.757288+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Help: Obrigatórios
  - Vias de Transporte '
type: support-article
updated_at: '2021-07-29T15:01:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405233895959-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Help-Obrigat%C3%B3rios-Vias-de-Transporte
---

**Dúvida**Ao tentar realizar o cadastro de uma nova rota nas vias de transporte *(*EICCV100*)* o sistema apresenta mensagem solicitando a revisão de todos os campos preenchidos. Como faço para salvar a rota sem que esta mensagem seja apresentada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403966143767/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Esta mensagem esta sendo exibida pois os campos da tabela de taxas de Frete não foram preenchidas.  
1. Dê um duplo clique na coluna **Frete p/Kg**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403966330519/mceclip1.png)

2. Será aberto a janela de frete por KG . O campo **Moeda** (YR\_MOEDA) já estará preenchida com a moeda internacional informada no rota nova será necessário informar os campos obrigatório *Até (YR\_KILO1)* e **Valor p/ Kg1** (YR\_VALOR1)*.*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403966414743/mceclip2.png)

3. Após o preenchimento destas informações é só clicar no botão salvar para salvar o frete por kg informado e clicar novamente no botão para salvar a nova rota. Feito isso a mensagem impeditiva do sistema não será mais exibida.
