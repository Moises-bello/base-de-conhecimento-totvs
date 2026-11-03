---
content_hash: f8190cf77571d063a9addff8b2d4cf7d2b75a7e34a32d54e668ae8c71d717c0e
fetched_at: '2026-06-29T00:09:29.241236+00:00'
page_id: '423938847'
product: rm
source: tdn-rm
title: Processo de Pedido de Compra (Integração ERP TOTVS X Portal de Compras Paradigma)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938847
version: 5
---

**Objetivo**

Permitir que o usuário integre os pedidos de compra originados no TOTVS Gestão de Estoque, Compras e Faturamento para o Portal de Compras Paradigma (WBC – Web Business Center).  
  
**Sobre o Processo**

A entidade "Pedido de Compra" no Portal de Compras é equivalente à entidade "Ordem de Compra" no ERP RM. O processo de seleção e envio de ordens de compra ao Portal de Compras não será automático, devendo ser executado o processo de integração dos pedidos de compra.  
O pedido de compras pode ser inserido no BackOffice RM através de diversos processos, sendo oriundo de cotação ou não. Após a inclusão do pedido, fica a cargo do profissional responsável selecionar os que devem ser integrados ao Portal de Compras Paradigma e executar o processo de integração, obtendo neste momento o retorno de integração que informará o status da integração de cada pedido.  
Os pedidos de compra integrados passarão pelo processo padrão do Portal de Compras, sendo que os mesmos não poderão ser faturados no BackOffice enquanto não obtiverem aceite do fornecedor.  
  
**Parametrização**

Para que a integração possa ser utilizada, a mesma deverá estar ativa dentro do ERP TOTVS.   
Para parametrizar a integração é necessário:

1. Acessar o módulo **TOTVS Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Paradigma** , e marcar a flag "Integrado com Paradigma" e configurar o caminho do WebService onde se encontra o servidor do paradigma.
2. Acessar **TOTVS Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas,** ao acessar a tela vá em Classificação e no campo "Tipo de Produto fornecido pelo fornecedor", marcar como "Tipo".
3. Parametrizar o tipo de movimento que será utilizado como pedido de compra. Acessando o módulo **TOTVS Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | "Tipo de movimento escolhido para pedido de compra"**

Etapa "Compra/Venda – Outros", Tipo de movimento de compras, marcar "Pedido de Compras".  
Etapa "Integração Paradigma", deverá ser marcado "Integrado com o Portal de Compras Paradigma".  
  
**Carga Inicial**

Para que o processo funcione é necessário que os cadastros utilizados na geração do movimento de pedido de compra, como moeda, filial, condição de pagamento, fornecedor, produto etc, estejam sincronizados com o portal paradigma.   
Utilizando a carga inicial o usuário tem a opção de sincronizar os registros que já estão na base de dados do ERP TOTVS, ele poderá sincronizar todos os registros, somente os não enviados ou selecionar quais registros deseja sincronizar.   
A carga inicial pode ser acessada no módulo **TOTVS Gestão de Estoque, Compras e Faturamento | Utilitários | Carga inicial**  
  
**Processo de Pedido de compras – Integração**

* **Inclusão de Pedido de compras**

**1. Criação da ordem de compras no ERP TOTVS**  
O comprador deverá gerar uma ordem de compra no ERP, até então sem integração com o portal de compras, utilizando o movimento que foi previamente parametrizado. Esta ordem de compra pode ou não ter sua origem pelo processo de cotação. Ao criar esse pedido de compra o mesmo assume o "Status Paradigma" como "Não integrado".  
  
**2. Comprador seleciona Ordens de Compra para tratamento no Portal de Compras**  
Comprador seleciona as ordens de compra que deseja integrar e executa processo responsável por enviar as mesmas, como "pedidos de compra", para o Portal de Compras Paradigma.   
Esta ação é efetuada pelo processo "Integrar Pedido com Portal de Compras Paradigma" que se encontra na visão do movimento de pedido de compra no menu Processos". O portal fará o processamento da mensagem de integração e o status da execução será apresentado no log de execução do processo. O retorno do processamento pelo Portal de Compras será validado e caso haja erro a operação será totalmente desfeita, caso contrário o pedido de compras assume o "Status Paradigma" como "Aguardando Aceite Fornecedor" e permanecerá com esse status até que o fornecedor dê o aceite do pedido.   
  
**3. Alteração da ordem de compra no ERP**  
Caso haja alteração em uma ordem de compra já integrada ao Portal de Compras Paradigma será enviada automaticamente a mensagem de atualização, não necessitando interação do usuário. A alteração será integrada independente do pedido de compra ter sido cancelado ou aceito pelo fornecedor no Portal de Compras

***Importante!***  
Toda Ordem de Compra será inserida com o status de integração "Não integrado", oriundo de cotação ou não.  
O processo de integração somente poderá ser efetuado para Ordens de Compra com status "Pendente".  
Ordens de compra não poderão ser faturadas enquanto tiverem o status de integração "Aguardando aceite de Fornecedor" ou "Recusado pelo Fornecedor".  
Caso uma ordem de compra integrada sofra alterações, seu status de integração será alterado para "Aguardando aceite de Fornecedor" independente do status atual.  
O fluxo de integração de Pedido de Compra ocorre somente originando no BackOffice RM. Assim sendo, caso seja feita qualquer alteração no Pedido de Compra a partir do Paradigma a mesma não será refletida no BackOffice.  
O usuário comprador enviado para o paradigma corresponde ao comprador no RM (TMOV.VEN1), desde que o comprador esteja vinculado a uma pessoa que possua um usuário informado, caso contrário, será enviado o usuário responsável pela criação do pedido no RM (TMOV.CODUSUARIO).
