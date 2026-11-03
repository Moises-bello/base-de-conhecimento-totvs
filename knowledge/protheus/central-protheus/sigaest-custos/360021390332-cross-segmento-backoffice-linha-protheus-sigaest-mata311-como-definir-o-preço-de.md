---
article_id: 360021390332
category: SIGAEST - CUSTOS
content_hash: 07c2ad7da3e76e2cdbcaa63e62f0ae58fdf6a79b7d68aad8366c6edbe7d94370
fetched_at: '2026-06-28T22:39:00.367744+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA311 - Como definir
  o preço de venda nas transferencias entre filiais?
type: support-article
updated_at: '2026-02-04T18:52:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021390332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA311-Como-definir-o-pre%C3%A7o-de-venda-nas-transferencias-entre-filiais
---

Ao usar a rotina MATA311 para Transferência entre Filiais no TOTVS Protheus, o preço de venda do pedido pode estar incorreto devido ao parâmetro MV\_TPCUSST, que define a origem do preço (Tabela de Preço, Custo Standard, Último Preço de Compra ou Custo Unitário). Se o parâmetro estiver vazio ou com valor 1 sem tabela vinculada, o preço será gerado incorretamente, podendo assumir valor unitário 1 por padrão. É necessário ajustar corretamente esse parâmetro para corrigir o preço.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503340947479)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**

Ao utilizar-se da rotina MATA311 para efetivação de Transferência entre Filiais, preço de venda do Pedido de Vendas do produto é gerado com valor que não é do preço. Como corrigir?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

A inconsistência em questão está relacionada devido ao conteúdo do parâmetro **MV\_TPCUSST**, que define de onde será alocado o preço de venda no registro de transferência

**1=** [**Tabela de Preço**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019193491-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reajuste-de-Valores-na-Tabela-de-Pre%C3%A7o-Pre%C3%A7o-Base-e-Pedidos-em-Aberto)**;**

**2=** [**Custo Standard**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-MATA320-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-B1-CUSTD)**;**

**3=** [**Ultimo Preço de Compra**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412738117399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-atualizar-o-campo-B1-UPRC-com-o-ultimo-pre%C3%A7o-de-Compra-)**;**

**4=** [**Custo Unitário**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013945671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330-Conceito-e-Informa%C3%A7%C3%B5es)**;**

Caso o parâmetro esteja em branco, ou esteja com o conteúdo =1 porém sem a Tabela de Preço devidamente criada e vinculada ao Cadastro de Cliente (neste caso, na filial destino) o respectivo Pedido de Venda será gerado incorretamente)

Se um produto em questão, não estiver sendo informado na tabela de preço e sua condição for para que seja assumido o valor da tabela de preço, **esse produto por padrão terá seu valor unitário = 1.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8442366986775)**

## **Observação Importante:**

O parâmetro MV\_TPCCUST é utilizado **apenas na rotina Solicitação de Transferência (MATA311)** **caso esteja utilizando a rotina Transferência entre filiais (MATA310)** o sistema irá considera o que está no parametro: "**Considera como preço no PV**" conforme imagem abaixo:

![Captura de tela 2025-12-16 104144.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37060437580055)

**Solução**

Conforme descrito, se faz necessário o preenchimento devido do parâmetro destinando o critério a ser considerado para o Pedido de Vendas gerar o preço de venda correto no processo de Transferência dentre as Filiais.

**Saiba mais:**

[*MP - SIGAEST - Transferência entre Filiais - Conceito e Passos Práticos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052)

[*SIGAEST - MATA310 MATA311 - Como configurar tabela de preços para as Transferências?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8552373360023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-tabela-de-pre%C3%A7os-para-as-Transfer%C3%AAncias)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
