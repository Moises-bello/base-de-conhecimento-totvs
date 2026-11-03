---
content_hash: fe25af9cb026fe486e747be63a8083bac51f2e172168e32d027cc639b1f8e2af
fetched_at: '2026-06-29T00:09:58.782006+00:00'
page_id: '452706390'
product: rm
source: tdn-rm
title: 12.1.12 (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452706390
version: 9
---

Criação da etapa Definições Gerais 5/5 nos parâmetros de [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220) para que o usuário possa selecionar quais informações sobre o item de orçamento deseja visualizar.

Disponibilizado o Status "Indisponível" para produtos no registro de orçamento da [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220) . Permitindo que sejam diferenciadas situações em que o produto não se encontra disponível no momento da Cotação das situações que o produto não é fornecido pelo Fornecedor. O Status "Indisponível" também pode ser informado na [Cotação Web](http://tdn.totvs.com/pages/viewpage.action?pageId=423938016) e [Importação de Cotação via planilha Excel](http://tdn.totvs.com/pages/viewpage.action?pageId=423938009).

Disponibilizada possibilidade de acesso ao cadastro do [Fornecedor](http://tdn.totvs.com/pages/viewpage.action?pageId=425459224) através da [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220), permitindo inclusão de fornecedor, edição ou consulta de dados do mesmo no momento da escolha dos fornecedores que vão participar da Cotação.

Padronizada a exibição da aba de Orçamentos na [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220), sendo possível agora associar recursos e customizar a mesma, como por exemplo, a associação da action de [Filial](http://tdn.totvs.com/pages/viewpage.action?pageId=422545738) para permitir acesso ao cadastro da Filial a partir da visão de Orçamento.

Melhorias no processo de cálculo da Data de Entrega na [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220). Foi criado o campo Prazo de Entrega na tela de Registro de Orçamento na [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220), [Cotação Web](http://tdn.totvs.com/pages/viewpage.action?pageId=423938016) e [Importação de Cotação via planilha Excel](http://tdn.totvs.com/pages/viewpage.action?pageId=423938009), para que o usuário decida qual modelo trabalhar: Data de Entrega ou Prazo de Entrega(dias).

Criação de link de acesso as informações dos produtos que participam do processo de cotação quando forem utilizadas as rotinas: Registrar Orçamento, Registrar Negociação, Itens de Movimento e Assistente de Inclusão de Cotação.

Melhoria no processo de Interferência sobre todos os Itens na [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220). Foi disponibilizada a possibilidade de realizar tal interferência por Fornecedor e por Produto.

Implementado o campo "Descrição" no processo Cancelar [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220) e exclusão de itens da Cotação. Desta forma, além de informar o motivo de cancelamento (previamente cadastrado) é possível informar uma descrição por texto específica para cada cancelamento/exclusão realizada.  
Essa informação pode ser extraída posteriormente via relatório (campo DESCMOTIVO da tabela TCCOTACAOITMMOV).

Melhoria no processo de alteração de preço cotado/negociado no [Registro de Orçamento/Negociação na Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220), permitindo a possibilidade de se informar valores positivos ou negativos para alteração do preço.

Melhoria para possibilitar a edição de Cotações a partir da tela de [Rastreamento de Movimentos](http://tdn.totvs.com/display/LRM/Rastreamento).

Implementada possibilidade de edição de solicitações de compra a partir da [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220). Na edição da Cotação na aba Itens de Movimento, assim como na visão de Cotações no anexo Itens de Movimento, agora é possível selecionar uma solicitação participante da Cotação e com um duplo clique abrir a edição do Movimento.

Melhoria na exibição de campos não editáveis no registro de [Orçamento e Negociação na Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220), agora esses campos são apresentados na cor cinza.

Criação do parâmetro [Condição de Pagamento obrigatória na Inclusão da Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938121).

O campo CNPJ/CPF passou a ser o campo default para filtrar fornecedores no Assistente de Inclusão de [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220).

Restruturação do processo de [Enviar e-mail para Cliente/Fornecedor](http://tdn.totvs.com/pages/viewpage.action?pageId=423938104). Foi criada a opção o "envio do e-mail apenas para os contatos do fornecedor". Será permitido enviar e-mail individualmente para todas as opções de destinatários, a única opção que será enviada como cópia será "Cópia de e-mail para Usuário Logado".

Criação do campo [Status de Envio de E-mail](http://tdn.totvs.com/pages/viewpage.action?pageId=423938104)na visão do movimento de ordem de compras e no anexo de [Pedidos Gerados](http://tdn.totvs.com/pages/viewpage.action?pageId=423938102) da [Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938220).
