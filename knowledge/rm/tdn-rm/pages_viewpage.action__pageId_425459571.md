---
content_hash: 9a28cb767889bb170acb6270f049da9e227b9b20d9e74047397476bae109e94c
fetched_at: '2026-06-29T00:09:37.173405+00:00'
page_id: '425459571'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x Backoffice Protheus - Processos - Medição de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459571
version: 4
---

**Medição de Contrato**

---

A inclusão, alteração e exclusão da Medição de Contrato são realizadas no TOP. No Protheus são gerados os pedidos de compra e venda. É utilizada a tecnologia Web Service para sincronizar os dados entre o TOP e o Protheus.  
    
   
    
 Durante o acompanhamento do projeto são geradas diversas medições ao longo dos períodos. O processo de Medição de Contrato gera um movimento no TOP e um pedido de compra ou venda no Protheus conforme o tipo do contrato. Para cadastrar um contrato no TOP acesse: Cadastros | Contratos  
    
 1. É necessário associar itens do projeto ao contrato. Para isso selecione o contrato e acesse: Processos | Associação de Itens ao Contrato  
    
 ***Observações:***

* Selecione uma tarefa que tenha preço.
* O cliente/Fornecedor selecionado deve existir no Protheus.

2. Informe o período do contrato e o valor previsto. Para isso acesse: Anexos | Períodos do Contrato  
    
 3. A execução do processo de medição de contrato deve ser realizado através da versão Delphi do Solum. Selecione o projeto no Solum.exe, e acesse: Cadastros | Contratos   
    
 Selecione o contrato desejado, e no Anexo Períodos de Contrato, selecione o período desejado. Dentro do anexo, execute o Processo Medição de Item de Contrato. Após a execução do processo, o movimento é gerado no TOP. No momento em que o movimento é gerado, um pedido de venda ou de compra é gerado no Protheus.  
    
 ***Observação:***

Os pedidos são gerados de acordo com o tipo de contrato. Contrato a Receber será gerado Pedido venda , Contrato a Pagar será gerado Pedido de compra.   
    
 Para visualizar o Pedido de Venda acesse: Protheus | Módulo | Atualizações | Geren. de Vendas | Pedido de Venda  
 Para visualizar o Pedido de Compra acesse: Protheus | Módulo | Atualizações | Geren. de Compras | Pedido de Compra  
    
 Para realizar a medição do contrato utilizando rateio e centro de custo, antes de executar o Processo Medição de Item de Contrato, associe o centro de custo através do Anexo Centros de Custo do Contrato. Informe o centro de custo (este deve existir no Protheus) e o percentual. Após é só executar o processo de medição normalmente.  
    
 No Protheus o centro de custo e o percentual são visualizados através do ícone Rateio, dentro do pedido de compra/venda gerado através da medição de contrato.   
    
 ***Observações:***

* No momento da liberação de medição o valor do adiantamento (total ou parcial) pode ser abatido no valor medido.
* As seguintes funcionalidades serão desabilitadas no TOP:

                           - Opções relacionadas à integração financeira na tela de Liberação de período do contrato. Pois a integração financeira não está contemplada.

                          - Escolher os tipos de movimento. Eles serão definidos automaticamente pela integração.

                         - Tabelas opcionais no envio de medição para faturamento. As tabelas opcionais não estão contempladas na integração.

                         - Campo "observação", se período de estorno. Por que o Título a Pagar do Protheus não possui este campo.
