---
article_id: 22593559917207
category: SIGAEST - MOVIMENTAÇÕES
content_hash: d64a7bcbd0dfe7388c8ca2ac17dd67f878749ec3897a0cb9da94b287ccf61f98
fetched_at: '2026-06-28T22:38:57.304547+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Solicitação de Compra
  originada da Solicitação ao Armazém vem com a descrição do Produto cortada
type: support-article
updated_at: '2024-04-05T14:26:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22593559917207-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Solicita%C3%A7%C3%A3o-de-Compra-originada-da-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m-vem-com-a-descri%C3%A7%C3%A3o-do-Produto-cortada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22593585076887) Tempo aproximado para leitura: **00:01:10min****Ocorrência**Ao realizar o aumento do campo de descrição do produto, quando se realiza uma solicitação ao armazém que gera uma solicitação de compras a Descrição fica cortada na SC1, porém não tem corte na SCP.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**No caso o Cadastro de Produto é utilizado em todo o ERP, dessa maneira, ao realizar o aumento do tamanho o campo descrição é necessário muito critério, pois não existe grupo de campo para a descrição, dessa maneira, o ajuste é realizado manualmente em todos os campos de todas as tabelas de todos os módulos utilizados, e no cenário de tabelas que se relacionam não estarem equalizadas pode ocorrer problema de descrição cortada.   
  
**Solução**No cenário apresentado acima a Solicitação ao Armazém (MATA105) a tabela utilizada é a SCP, já a Solicitação de Compras (MATA110) utiliza a tabela SC1, porém a rotina que de fato gera a Solicitação de Compras é a gerar pré requisição (MATA106) que utiliza a tabela SCQ, dessa maneira, para que a integração da Solicitação ao Armazém gere a Solicitação de Compras com a descrição correta, as tabelas envolvidas devem estar equalizadas:

- **C1\_DESCRI;**

- **CP\_DESCRI;**

- **CQ\_DESCRI;**

Importante: esse tipo de alteração é ideal que seja realizada com apoio de um analista in loco, para analise dos processos praticados na empresa, visando equalizar todos os campos que se comunicam, evitando colaterais.

**S****aiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
