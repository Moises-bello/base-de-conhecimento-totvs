---
content_hash: 07ba52ef36d655030a7f9e2514bcf6fe87dd49ffee2cbaf1a2071fc63de1130f
fetched_at: '2026-06-29T00:09:36.404580+00:00'
page_id: '425459513'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo de Geração de Documentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459513
version: 3
---

**Backoffice RM x Protheus SigaMNT - Processo  de Geração de Documentos**

---

O Processo de Geração de Documentos  permite que  diversos  tipos de documentos (taxas,multas e etc.) sejam gerados  e  enviados ao Backoffice RM , com o objetivo de gerenciar   os Bens enviados do Backoffice RM. Através do processo  são gerados movimentos de Pedido de Pagamento no Backoffice que  podem ser faturados  e estornados , tanto parcialmente , quanto  totalmente , além de permitir que descontos e acréscimos sejam adicionados aos documentos  integrados.  
    
   
    
 **Inclusão:** Na inclusão de um documento o SigaMNT Frotas envia a mensagem "Order" a fim de incluir o pedido de compras no módulo de compras do BackOffice RM, informando o parcelamento selecionado.  
    
 **Alteração:** A alteração de um documento no SigaMNT Frotas pode gerar a integração da mensagem "Order" a fim de atualizar os dados do pedido de compras no módulo de compras do BackOffice RM, caso os dados alterados façam parte do escopo do pedido. A alteração passará por todas as validações do BackOffice, que retornará se é possível alterar o pedido na sua situação atual.  
    
 **Exclusão:** A exclusão de um documento no SigaMNT Frotas pode gerar a integração da mensagem "Order" com evento de exclusão, a fim de excluir o pedido de compras no módulo de compras do BackOffice RM. A exclusão passará por todas as validações do BackOffice, que retornará se é possível efetuar a exclusão ou não, como por exemplo, caso o pedido já tenha sido faturado.  
    
 Dentre várias funcionalidades oferecidas pelo módulo de gestão de documentos do SigaMNT Frotas, destacamos as seguintes:  
    
 ·         Permitir o gerenciamento da documentação referente à Frota de Bens.  
 ·         Permitir aos usuários a geração de documentos a vencer mensalmente ou manualmente.  
 ·         Permitir uma efetiva gestão de forma centralizada através de consultas e relatórios apontando os serviços utilizados e seus custos, gerenciar a documentação necessária para cada frota.   
    
 O processo de inclusão de Documentos no Protheus SigaMNT segue o  fluxo abaixo.

1. Incluir um documento no Protheus SigaMNT, referenciando um produto, um bem  e uma condição de pagamento previamente integrada do Backoffice RM.
2. É enviada uma mensagem de Pedido de pagamento ao Backoffice RM , contendo o número de parcelas   informado no cadastro do documento.
3. É criado no Backoffice RM um  movimento de Pedido de Pagamento com as  parcelas referentes à Condição de Pagamento informada no cadastro
4. As parcelas do movimento criado  podem ser Baixadas ou estornadas  de acordo com a necessidade.

---

Para mais informações sobre o  processo de Geração de Documentos, acesse os boletins técnicos.

**Recursos Adicionais**

TDN - Boletim Técnico :  [Processo de Geração de Documentos](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_GERA%c3%87%c3%83O+DE+DOCUMENTOS_BR_CON000158.pdf?version=1&modificationDate=1380053410000)
