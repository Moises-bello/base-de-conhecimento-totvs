---
article_id: 33631251355799
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1cd11e1c9b715d7ccc499d54ebe65519e892c43b02f046a02516ed1769458bcb
fetched_at: '2026-06-28T22:38:55.613881+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Help: NAORASTRO ao
  tentar incluir Saldo'
type: support-article
updated_at: '2025-07-22T17:09:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33631251355799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-NAORASTRO-ao-tentar-incluir-Saldo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33631265059095) Tempo aproximado para leitura: **00:02:15 min**  
  
**Dúvida**

Ao tentar incluir uma movimetnação de Entrada de Saldo  no Protheus, apresenta o **Help: NAORASTRO**. O que precisa avaliar para concluir a movimentação?

![HELP NAORASTRO.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/33631527077655)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

|  |
| --- |
| **Importante:** **Sempre revisar se realmente utiliza o conceito de Rastreabilidade no Protheus antes de alterar as Configurações destacadas abaixo.** [**Veja nesse link**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus) **as informações sobre o conceito de Rastreabilidade no Protheus.** |

Nas Movimentações de **Entrada de Saldo** no sistema **ao informar o Lote do Produto** no Protheus padrão o **Help NAO RASTRO** é apresentado devido as seguintes situações:

**- 1 -** Verificar no cadastro do Produto se o **campo RASTRO (B1\_RASTRO)** esta igual a Não Utiliza. Nesse caso, realmente não é possível  informar um Lote para a Movimentação de Entrada de Saldo, pois o produto não utiliza controle de Rastro. **Obs.:** ***Veja nesse*** [***link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-ativar-o-controle-de-Lote-Rastro-para-produtos-com-saldo) sobre como iniciar o controle de Rastreabilidade do Produto caso desejar ativar para o produto.

![B1_RASTRO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33633658045847)

**- 2 -**Caso o campo **campo RASTRO (B1\_RASTRO)** esteja marcado como **L - LOTE** ou **S - SUBLOTE** avalie no módulo Configurador se o parâmetro MV\_RASTRO esta marcado com N.

![mv_rastro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33634133147287)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - Como ativar o controle de Lote/Rastro para produtos com saldo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-ativar-o-controle-de-Lote-Rastro-para-produtos-com-saldo)

[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)
