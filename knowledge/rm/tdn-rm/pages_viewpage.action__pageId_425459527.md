---
content_hash: 7feff19599ccd036031f018d7a15db01e56eb790d3c6838c678e9962519afee6
fetched_at: '2026-06-29T00:09:36.816891+00:00'
page_id: '425459527'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Conciliação de Abastecimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459527
version: 3
---

**Conciliação de Abastecimento**

---

A conciliação de abastecimentos permite comparar os abastecimentos realizados nos postos que não são conveniados, com as notas fiscais referentes aos abastecimentos efetuados durante a viagem. O valor informado na tela dos parâmetros, será cruzado com o valor total dos abastecimentos que serão conciliados.

   
 Existem três tipos de conciliação no SigaMNT, são elas:

**1. Conciliação Manual:** esta rotina é utilizada em situações, em que devido à necessidade, o motorista se obrigue a abastecer em postos que não sejam conveniados, ou nos casos em que a empresa não mantenha convênio com os postos.

**2. Conciliação Manual de Posto Interno**: permite comparar os abastecimentos realizados nos postos internos que são de propriedade da empresa. Feito o abastecimento, é necessário realizar um controle interno dos gastos dos combustíveis utilizados pela frota da empresa, que pode gerar movimentações de estoque no BackOffice (baixa e/ou acréscimo).

**3. Conciliação Automática:** tem por objetivo confrontar os abastecimentos importados que foram realizados em postos conveniados, com as informações da nota fiscal enviada pelo posto que realizou estes abastecimentos. Fica a cargo das regras de negócio do SigaMNT Gestão de Frotas a definição das movimentações de estoque (baixa e/ou acréscimo) necessárias em cada conciliação.

Para efetuar a movimentação de estoque no BackOffice o mesmo lançará a mensagem **Stockturnover**, sendo utilizado o campo *"Type"* para diferir entre movimentação de entrada ou saída de estoque.   
 Para gerar o Pedido de Compra no BackOffice o mesmo lançará a mensagem **Order**, sendo utilizado o campo *"Type"* também para diferir entre os movimentos de pagamento e de compra.

**Ficando assim:**   
    
 **Mensagem Stockturnover**  
 'Type' = '000' será gerado um movimento de Baixa de Estoque  
 'type' =  '001'  será gerado um movimento de Entrada de Estoque  
    
 **Mensagem** **Order**  
 'Type' = '000' Pedido de Pagamento 'Type' = '001' Pedido de Compras   
    
 Após a Conciliação de Abastecimento ser finalizada no Protheus SigaMNT o usuário deverá acessar o TOTVS Gestão de Estoque, Compras e Faturamento, acessar o movimento e dar continuidade no processo. Desse ponto em diante o processo seguirá todo o fluxo interno do TOTVS Gestão de Estoque, Compras e Faturamento. Para maiores informações acesse o help de movimentos do TOTVS Gestão de Estoque, Compras e Faturamento

---

Para mais informações sobre o processo de Conciliação de Abastecimento, acesse os boletins técnicos.

**Recursos Adicionais**

---

TDN - Boletim Técnico : [Processo de Conciliação de Abastecimentos](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_CONCILIA%c3%87%c3%83O+DE+ABASTECIMENTO_BR_CON000158.pdf.pdf?version=1&modificationDate=1380053410000)
