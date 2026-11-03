---
article_id: 360017527772
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a289eaba80e36ac69a520ecb9d13eb71296983c72281938b4ed9f2b7721be0f8
fetched_at: '2026-06-28T22:38:54.208466+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Conceito e controle
  do Número de Série no Estoque de Produtos no Protheus
type: support-article
updated_at: '2026-02-20T16:39:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527772-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-controle-do-N%C3%BAmero-de-S%C3%A9rie-no-Estoque-de-Produtos-no-Protheus
---

O controle de Número de Série no Protheus é aplicado a produtos gerenciados individualmente no estoque, como celulares com IMEI. Para usar, é necessário ativar o parâmetro MV\_LOCALIZ e configurar o produto com Contr. Ende. "Sim". A definição dos números ocorre na rotina MATA265, onde cada número acompanha o produto durante sua permanência no estoque. Produtos serializados têm saldo disponível apenas após identificação dos números de série.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25118980846871) Tempo aproximado para leitura: **00:04:30 min**

**Dúvida:**

O que é a Serialização e em quais casos posso definir Número de Série nos produtos no Estoque? ***Como funciona no Protheus*** o controle de Número de Série para os produtos?

**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução:**

**Conceito para utilização**

O controle de Número de Série deve ser aplicado aos produtos que são gerenciados no estoque de forma serializada, ou seja, com identificação única por cada **unidade** do produto, sendo esta identificação o Número de Série. Um exemplo de aplicação deste controle seria para uma loja de venda de aparelhos celulares, onde cada aparelho é identificado por uma numeração única, o IMEI.

A utilização das funcionalidades do controle de Número de Série dependem da ativação do parâmetro MV\_LOCALIZ. Além disto é necessário que o cadastro de cada produto que deseja-se utilizar o controle seja configurado com o campo Contr. Ende. (B1\_LOCALIZ) como “Sim”.

|  |
| --- |
| **--- Informações Importantes sobre a Serialização de Produtos no Protheus ---** |

**- 1 -** Ao habilitar o controle de Número de Série para um produto que já possui saldo no Estoque, é necessário realizar a distribuição deste saldo em Números de Série. Para isto deve-se utilizar o programa de Criar Sld. no End. (MATA805) através do menu Atualizações -> Movimentações -> Internas -> Endereçamento -> Criar Sld. no End. ([**Veja exemplo aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020663372-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-implantar-o-controle-de-endere%C3%A7o-para-produtos-que-j%C3%A1-tem-saldo))

**- 2 -** No Protheus, **a definição dos Números de Série** para um produto ***somente é possível*** na rotina de Endereçamento de Produtos (MATA265).

**- 3 -** Durante a execução da rotina 'Endereçamento', o usuário atribui os Números de Série aos produtos (através do campo DB\_NUMSERI).

**- 4 -** Uma vez cadastrado, o Número de Série irá acompanhar o produto em todas as movimentações ***durante sua permanência*** **no estoque**. Ou seja, após o CONSUMO/REQUISIÇÃO do item que foi serializado, o Número de Série que foi consumido fica disponível para um novo item.

**- 5 -** Quando o produto possui controle de Número de Série, os saldos das entradas ficarão disponíveis no estoque para movimentação somente após a realização da identificação dos Números de Série.

**- 6 -** Quando o produto utiliza controle de Número de Série, **cada Número de Série poderá ter** **saldo de uma unidade** do produto.

**- 7 -** No cabeçalho desta rotina são exibidas as informações referentes a entrada que originou o saldo a distribuir, apenas para visualização pelo Usuário.

**- 8 -** **Caso não tenha identificado os Números de Séries no momento do Endereçamento, e tenha criado movimentos com o numero de serie ERRADO**, é necessário avaliar as **opções abaixo** para que possa Endereçar novamente com a serie desejada.

**- 8.1 -** Estornar o Endereçamento Origem e Endereçar novamente identificando os Números de Séries desejados;

**- 8.2 -** Utilizar a rotina **TRANSFERÊNCIAS MÚLTIPLAS (MATA261)** e transferir o Saldo do Endereço Origem e ***não informar o Endereço Destino***, dessa forma gera Saldo a Endereçar (B2\_QACLASS) e uma linha de registros na rotina MATA265 (tabela SDA) onde pode agora realizar um novo Endereçamento definindo os Números de Séries desejados;

## **Principais Campos na Tabela Endereçamento:**

* *Produto (DA\_PRODUTO):* código do produto a receber a identificação dos números de série.
* *Qtd Original (DA\_QTDORI):* quantidade movimentada pela entrada que originou a distribuição.
* *Saldo (DA\_SALDO):* saldo para identificação dos números de série.
* *Data (DA\_DATA):* data do movimento de entrada que originou a distribuição.
* *Lote (DA\_LOTECTL)*: número de lote da quantidade a distribuir.
* *Armazém (DA\_LOCAL):* armazém onde se encontra o saldo a distribuir.
* *Documento (DA\_DOC):* número de documento que originou a distribuição.
* *Serie (DA\_SERIE):* série do documento de entrada que originou a distribuição.

Nos itens, o saldo a identificar Números de Série deverá ser distribuído conforme números de série desejados.

## **Principais Campos referente e Movimentações de Endereços:**

* *Estornado (DB\_ESTORNO):* identifica se o endereçamento realizado neste endereço deve ser estornado (preenche-lo somente quando acessada a opção de estorno).
* *Qtd Distribu (DB\_QUANT):* quantidade a endereçar no endereço informado (deve ser obrigatoriamente 1).
* *Num de Série (DB\_NUMSERI):* código do número de série que será criado para o produto em questão

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - Protheus se perde na geração da série dos produtos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403859340951)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao informar o número de série no endereçamento ocorre o Help QUANTSERIE*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24166763856919-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-informar-o-n%C3%BAmero-de-s%C3%A9rie-no-endere%C3%A7amento-ocorre-o-Help-QUANTSERIE)
