---
content_hash: 6adee5cae8e16af2506931497da7dc9256002bb431262e257106890cf67f1727
fetched_at: '2026-06-29T00:09:09.768287+00:00'
page_id: '394201489'
product: rm
source: tdn-rm
title: Descrição do Processo de Industrialização Interna - Transferência entre Filiais
  (SEM Local Transitório - Retorno de outra mercadoria - PI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394201489
version: 13
---

## Visão Geral

**Retornar simbolicamente a Matéria Prima, destacar o Serviço de Industrialização e Enviar o Produto Industrializado**

**Descrição do Processo:**

Neste caso, o retorno da industrialização será lançado em um tipo de movimento também do tipo ***3.1 ‘Industrialização Efetuada para Outra Filial’***, que será criado através de um processo específico **Retorno Simbólico Industrialização Efetuada para outra Filial** na filial que realizar a industrialização. Neste processo serão selecionadas as notas fiscais de ***‘Transferência para Industrialização em Outra Filial’***, emitidas na filial remetente, cujos insumos ainda não retornaram, seja parcial ou total. Após finalizar o processo, será aberta a edição do movimento de ***‘Industrialização Efetuada para Outra Filial’*** com os insumos selecionados anteriormente e as respectivas quantidades pendentes de retorno. Neste momento o usuário poderá alterar a quantidade retornada e preencher os dados fiscais da operação, se estes não estiverem parametrizados no tipo de movimento. Deverá incluir o serviço referente ao processo de industrialização com o respectivo CFOP. Ao finalizar a inclusão desse movimento, o sistema irá **diminuir** o estoque **DE Terceiros** na filial origem da movimentação e **diminuir** o estoque **COM Terceiros** na filial destino da movimentação.

Em seguida, **na filial recebedora**, o sistema irá abrir a edição de um tipo de movimento (pré parametrizado) como ***‘Transferência Produto Industrializado’*** para baixar o estoque do Produto Industrializado na filial origem (que efetuou a industrialização) e aumentar o estoque na filial destino (aquela que solicitou a industrialização). O usuário deverá preencher os dados do movimento, como código do PI dentre outras informações.

Ao confirmar a inclusão desse movimento, o sistema irá, **na filial remetente da remessa**, baixar o estoque físico/financeiro (saldo atual) das mercadorias retornadas simbolicamente, através da criação automática de um movimento do tipo ***‘Baixa Mercadoria utilizada na industrialização interna’*** que terá sido pré parametrizado para baixar o estoque saldo atual.

Se a filial que efetuar a industrialização não utilizar toda a mercadoria ora remetida para o processo, a mesma irá emitir uma nota fiscal de retorno da mercadoria não aplicada na industrialização. Esta operação será realizada em um movimento de transferência do tipo ***3.1 ‘Retorno mercadoria não aplicada na industrialização’*** que será criado através de cópia por referencia do movimento de ***‘Transferência para industrialização em Outra Filial’*** criado na filial solicitante da industrialização, que irá **diminuir** o estoque **DE Terceiros** na filial emitente e **diminuir** o estoque **COM Terceiros** na filial destino.

## Parametrização

**Estoque de Terceiros - Parametrização do Processo de Industrialização Interna - Transferência entre Filiais**

**Filial Remetente:**O tipo de movimento de **Transferência para Industrialização em Outra Filial** terá a seguinte parametrização para que seja possível controlar o estoque **COM Terceiros**:

**Etapa Item - Identificação 1/2:**Tipo dos Itens = Produtos

**Etapa Estoque - Estoque 2/3:**Tipo Controle de Estoque Terceiros = Transferência para Industrialização em Outra Filial

                                                    Efeito Sobre o Saldo com Terceiros = Aumenta

**Integração Contábil:**Parametrizar de acordo com as obrigações contábeis da Empresa

**Integração Fiscal:**Parametrizar de acordo com as obrigações legais da Empresa

**Fis - Natureza:**Edita Cliente/Fornecedor Origem/Destino = Marcado

O tipo de movimento de **Baixa de Mercadoria Utilizada na Industrialização** terá as mesmas parametrizações descritas acima, diferenciando-se o **Tipo Controle de Estoque Terceiros** e o **efeito** sobre o **Saldo Atual**para que seja possível controlar o estoque **COM Terceiros**:

**Etapa Estoque - Estoque 1/3:**Saldo Atual = Diminui

**Etapa Estoque - Estoque 2/3:**Tipo Controle de Estoque Terceiros = Baixa de Mercadoria Utilizada na Industrialização em Outra Filial

**Filial Recebedora:**O tipo de movimento de **Industrialização Efetuada para Outra Filial** terá a seguinte parametrização para que seja possível controlar o estoque **COM terceiros** da Filial Remetente:

**Etapa Item - Identificação 1/2:**Tipo dos Itens = Produtos

**Etapa Estoque - Estoque 2/3:**Tipo Controle de Estoque Terceiros = Industrialização Efetuada para Outra Filial 

                                                    Efeito Sobre o Saldo de Terceiros = Diminui

**Integração Contábil:**Parametrizar de acordo com as obrigações contábeis da Empresa

**Integração Fiscal:**Parametrizar de acordo com as obrigações legais da Empresa

**Fis - Natureza:**Edita Cliente/Fornecedor Origem/Destino = Marcado

                       

O tipo de movimento de **Transferência do Produto Industrializado em Outra Filial**terá a seguinte parametrização para que seja possível controlar o estoque **COM terceiros**da Filial Remetente:

**Etapa Item - Identificação 1/2:**Tipo dos Itens = Produtos

**Etapa Estoque - Estoque 1/3:**Saldo Atual = Diminui

**Etapa Estoque - Estoque 2/3:**Tipo Controle de Estoque Terceiros: Transferência do Produto Industrializado em Outra Filial

**Integração Contábil:**Parametrizar de acordo com as obrigações contábeis da Empresa

**Integração Fiscal:**Parametrizar de acordo com as obrigações legais da Empresa

**Fis - Natureza:**Edita Cliente/Fornecedor Origem/Destino = Marcado

                       

O tipo de movimento para **Retorno de Mercadoria não Aplicada na Industrialização** terá as mesmas parametrizações descritas acima, além de parametrizar o **Motivo de Referência** para que seja estornado o estoque **COM terceiros**da Filial Remetente:

**Etapa Mov - Outros Dados:**Usar Cópia de Movimentos por referência = 11 - Retorno de Mercadoria não Aplicada na Industrialização
