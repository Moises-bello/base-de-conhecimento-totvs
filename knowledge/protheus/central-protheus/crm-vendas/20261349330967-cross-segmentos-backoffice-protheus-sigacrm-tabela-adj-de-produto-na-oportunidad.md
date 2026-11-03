---
article_id: 20261349330967
category: CRM - Vendas
content_hash: abcacdeabb6008c64df9d9a78aeab40675df065aca52d5c76a0e5ddb47ddee1f
fetched_at: '2026-06-28T22:40:25.858218+00:00'
product: protheus
section_id: 1500001549102
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Tabela ADJ de Produto na
  Oportunidade de Venda (FATA300)
type: support-article
updated_at: '2024-03-21T16:50:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20261349330967-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Tabela-ADJ-de-Produto-na-Oportunidade-de-Venda-FATA300
---

**Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**  
Qual a finalidade da tabela ADJ de produtos na Oportunidade de Venda (FATA300)?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - Todas as versões  
  
**Solução:**   
A tabela de Produtos (ADJ) na rotina de Oportunidades (FATA300) tem como finalidade a visualização e preenchimento dos produtos relacionados à essa Oportunidade, porém a inclusão manual de produtos torna-se informativa na oportunidade de venda.

Ao preencher um produto dentro dessa tabela a informação fica apenas como histórico, esses são os produtos informados na Oportunidade de venda ao cliente, porém podem não ser os produtos que serão vendidos quando a Oportunidade for ganha.

Ao incluir a Proposta Comercial para a efetiva e geração do pedido de venda, o sistema considera os produtos da Proposta e não os digitados manualmente na Oportunidade, assim o produto informado na tabela ADJ não será incluído no pedido de venda.

Para assegurar a correta exibição do produto na oportunidade, é crucial entender e ajustar o parâmetro MV\_FATMNTP, conforme descrito abaixo:

* Quando o parâmetro **MV\_FATMNTP** é configurado como "1", o produto na proposta comercial irá sobrepor o produto na oportunidade, não mantendo a linha com a informação do produto inicialmente incluído na oportunidade.
* Se configurado como "2", o produto na proposta comercial será incluído junto ao produto da oportunidade, gerando uma linha adicional.

Após a aprovação da Oportunidade e a subsequente geração do pedido de venda os produtos inseridos na Proposta seguem para o Pedido de Vendas, concretizando o processo de venda.

**Saiba mais**: [Criação de Oportunidade de Vendas com Proposta Comercial](https://tdn.totvs.com/x/XjEaDg)
