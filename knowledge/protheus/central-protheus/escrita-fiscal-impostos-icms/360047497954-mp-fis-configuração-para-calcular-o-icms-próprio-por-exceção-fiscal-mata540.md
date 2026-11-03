---
article_id: 360047497954
category: Escrita Fiscal - Impostos - ICMS
content_hash: 661ab4ba8d697e018c1d069ccc49d990fcca92fcb61f9500445cb50f8dbb8086
fetched_at: '2026-06-28T22:39:26.073617+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: MP FIS - Configuração para calcular o ICMS próprio por Exceção Fiscal (MATA540)
type: support-article
updated_at: '2021-04-28T20:51:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047497954-MP-FIS-Configura%C3%A7%C3%A3o-para-calcular-o-ICMS-pr%C3%B3prio-por-Exce%C3%A7%C3%A3o-Fiscal-MATA540
---

**Dúvida**Como configurar o cadastro de Exceções Fiscais para o tratamento das alíquotas de ICMS Próprio?

**Ambiente**Protheus - Todas as versões.

**Solução**

**Grupo Trib (F7\_GRTRIB)**: Código do grupo de tributação cadastrado. O código preenchido nesse campo obrigatoriamente deverá ser vinculado no campo Grupo Trib. (B1\_GRTRIB) no cadastro do Produto.

**Sequência (F7\_SEQUEN)**: Código sequencial do registro. Esse código é preenchido automaticamente, porém não necessita seguir uma ordem específica.

**Estado (F7\_EST)**: Para exceções fiscais utilizadas em notas de saída (venda/remessa), esse campo representa o Estado do Cliente para o qual o produto está sendo enviado.

Caso seja uma exceção para notas de entrada (compra/aquisição), esse campo representa o Estado do Fornecedor do qual a empresa está recebendo os produtos.

**Tipo (F7\_TIPOCLI)**: Nesse campo deverá ser informado o tipo do Cliente. O conteúdo desse campo deverá ser o mesmo utilizado no campo Tipo Cliente (C5\_TIPOCLI) no momento de lançar o pedido de venda.

Para as notas de entrada orientamos preencher esse campo com \* (todos) ou Consumidor Final.

**Aliq.Interna (F7\_ALIQINT)**: Informar a alíquota do ICMS para as operações internas. Caso esse campo não seja preenchido o sistema irá utilizar a alíquota preechida no cadastro do produto (B1\_PICM) e caso esse campo também esteja vazio será considerada a alíquota do parâmetro MV\_ICMPAD.

**Aliq.Externa (F7\_ALIQEXT)**: Informar a alíquota do ICMS para as operações interestaduais. Caso o campo não seja preenchido, o sistema utilizará a alíquota interestadual padrão (12% calculada pela MATXFIS ou nos casos em que a UF de destino estiver no parâmetro MV\_NORTE será aplicado 7%).

**Grp.Cli/For (F7\_GRPCLI)**: Esse campo não é de preenchimento obrigatório para validar a exceção fiscal, porém caso ele seja preenchido o mesmo conteúdo deverá ser informado no cadastro do fornecedor através do campo Grp. Tribut (A2\_GRPTRIB) ou no cadastro o cliente através do campo Grp. Clientes (A1\_GRPTRIB).

**UF Busca (F7\_UFBUSCA)**: Apenas para as notas fiscais de entrada, esse campo irá indicar como o sistema deve se comportar no momento de selecionar a exceção fiscal. O padrão do sistema é buscar a exceção pela UF de destino da mercadoria (no caso das entradas, a UF a ser cadastrada deve ser a mesma do contribuinte, ou seja, a mesma informada no MV\_ESTADO). Esse campo poderá mudar a lógica de composição da exceção, considerando a UF do remetente da mercadoria, ou seja, a UF do fornecedor. Portanto, utilize: 1=Destino, para que a UF a ser selecionada na exceção fiscal das notas de entrada seja a do destino da mercadoria (MV\_ESTADO) 2=Origem, para que a UF a ser selecionada na exceção fiscal das notas de entrada seja a da origem da mercadoria (cadastro do fornecedor).

É importante que o tamanho dos campos abaixo estejam corretos para que a exceção fiscal possa funcionar.

F7\_GRTRIB = CARACTER, 6

F7\_GRPCLI = CARACTER, 3

A1\_GRPTRIB = CARACTER, 3

A2\_GRPTRIB = CARACTER, 3

B1\_GRTRIB = CARACTER, 6
