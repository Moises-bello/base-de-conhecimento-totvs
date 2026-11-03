---
content_hash: 257d200a384b5e317e3a0eed240e2d0e9934d8957363dda4694c40236b4b351b
fetched_at: '2026-06-29T00:09:28.720485+00:00'
page_id: '423938768'
product: rm
source: tdn-rm
title: Paradigma (Requisição) 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938768
version: 5
---

Permite que o usuário faça o envio de requisições originados no TOTVS Gestão de Estoque, Compras e Faturamento para o Portal de Compras Paradigma (WBC – Web Business Center).   
A entidade "Requisição" no Portal de Compras é equivalente à entidade "Solicitação de Compra" no ERP RM.   
O processo de seleção e envio de solicitações de compra ao Portal de Compras não será automático, ficando a cargo do comprador esta tarefa (podendo ser agendado para execução futura via JobServer).   
A inclusão de Requisição será incluída somente no TOTVS RM, ou seja, deve-se desabilitar a inclusão de Requisição no Portal de Compras Paradigma.

**1. Solicitação de Compra**

**1.1.  Inclusão de Solicitação de Compras:**O comprador gera uma solicitação de compra no ERP, até então sem integração com o portal de compras Paradigma. É gerado um movimento do tipo 1.1XX onde são solicitados os produtos que a empresa precisa comprar.

**1.2. Alteração de Solicitação de Compras:**Não será permitido alterar/excluir itens que estão incluídos na Cotação, esta regra será respeitada para as solicitações de compra que possuem cotação integrada com paradigma.

**2. Cotação no RM**

**2.1.** **Inclusão da Cotação no Sistema:**A integração com o Portal de Compras Paradigma irá ocorrer através do processo de Geração da Cotação. Ao incluir uma nova Cotação no TOTVS Gestão de Estoque, Compras e Faturamento, se a opção "Integrar com Portal Paradigma" estiver marcada e o usuário marcar a opção Integrar com Paradigma, serão realizadas as seguintes ações:

* Não será permitido escolher Fornecedores, ou seja, a cotação será criada sem fornecedor;
* O status paradigma da cotação ficará como "Pendente de envio";
* Será permitido somente incluir Itens na cotação. As demais funcionalidades ficarão desabilitadas, ou seja, **não será permitido;**
* Comunicar fornecedores;
* Incluir Fornecedores;
* Copiar Mensagem para Todos Fornecedores;
* Consultar Pontuações Detalhadas por Produto para o Fornecedor selecionado.

Será disponibilizada no cadastro da Cotação a coluna Status Paradigma que tem o objetivo de informar qual a situação da cotação em relação à integração com Paradigma. Este campo ficará disponível somente se a parametrização da integração estiver habilitada. As opções para o status paradigma são:

* Não Integrado: cotação não foi integrada com o Paradigma. Este será o valor default.
* Pendente de Envio: cotação será integrada e ainda não sincronizada com o portal paradigma.
* Parcialmente Integrado: cotação já foi sincronizada, porém existem itens que não foram integrados.
* Integrado: cotação já foi sincronizada com o portal paradigma.

Serão disponibilizados no cadastro de Itens da Cotação as colunas Código da Cotação Paradigma e Código do Item de Cotação Paradigma. Estas colunas ficarão visíveis somente se a parametrização da integração estiver habilitada.

**2.2. Alteração na Cotação:**Quando a cotação estiver integrada com o  paradigma será permitido incluir novos itens e excluir itens da cotação. Caso sejam incluídos ou excluídos novos itens, o status da cotação obedecerá ao fluxo abaixo:

* Caso sejam incluídos novos itens, o status da cotação obedecerá ao fluxo que existe hoje e o status paradigma será alterado para "Parcialmente Integrado" se o status paradigma anterior for "Integrado".
* Caso seja excluído um Item da Cotação e ele for o único item que não está integrado, se o status do Paradigma for "Parcialmente Integrado" ele será alterado para "Integrado".
* Caso sejam excluídos todos os Itens da Cotação que estejam integrados, se o status do Paradigma for "Parcialmente Integrado" ele será alterado para "Pendente de Envio Paradigma".
* Caso sejam excluídos todos os Itens da Cotação, se o status do Paradigma for "Integrado "ele será alterado para "Cancelado".
* Caso o item que esteja sendo excluído no ERP esteja em cotação não será permitido a exclusão.

Caso o item que esteja sendo excluído no ERP tenha sido cotado e retornado pelo Paradigma, a exclusão será efetuada no ERP mas não será enviado para cancelamento no Paradigma, pois uma vez que o item de requisição já consta como cotado no Paradigma este não poderá ser cancelado. Neste caso o registro correspondente ao item de requisição na tabela TINTEGRACAOID, que armazena a chave DE/PARA, não será excluído, portanto não estará disponível para a seleção do item para uma nova cotação e não será possível a integração com o Paradigma.

**3. Integrar Requisição no Portal de Compras Paradigma:**

Será disponibilizado na visão/edição de Cotação o processo "Integrar Requisição no Portal de Compras Paradigma".   
Ao executar este processo é enviada uma mensagem de integração para criação da(s) requisição(ões) no portal.   
O número da requisição do portal será o mesmo que o número da solicitação no ERP, para permitir a rastreabilidade entre os sistemas.   
Serão enviados todos os itens que não estão integrados com o Portal e cujo status paradigma da Cotação seja "Pendente de envio" ou "Parcialmente Integrado".

**Informações Adicionais:**Para realizar a Requisição de Itens de Cotação é necessário realizar o cadastro e/ou carga inicial dos seguintes cadastros: Envio de empresa (coligada e filial) Envio de unidade de medida Envio de categoria de produto Envio de produto Envio de usuário Envio de Centro de Custo Envio de Departamento.

---
