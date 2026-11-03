---
content_hash: 3578f43699c46d2dc8f8f31d1e8cc0b3e54e4388982617220026650cc01197bd
fetched_at: '2026-06-29T00:09:36.354066+00:00'
page_id: '425459502'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo de Sinistros e Multas
type: documentation
url: https://tdn.totvs.com/display/LRM/Backoffice+RM+x+Protheus+SigaMNT+-+Processo+de+Sinistros+e+Multas
version: 4
---

**Backoffice RM x Protheus SigaMNT - Processo de Sinistros e Multas**

---

O Processo de  Sinistros e Multas  permite cadastrar as informações relacionadas às multas recebidas por veículos da empresa ou terceiros, registrar o acompanhamento dos processos, e também registrar e controlar o pagamento destas multas.  
   
 O ponto de integração é iniciado ao efetuar a entrada de uma multa no sistema de manutenção de frotas, gerada diretamente ou a partir de notificação. Neste momento o mesmo encaminha uma mensagem de pedido de pagamento para o BackOffice RM, que ficará responsável por gerir o fluxo do pedido de pagamento até sua baixa efetiva, conforme processo definido pela empresa. Qualquer alteração (cancelamento ou exclusão) no pedido de pagamento, deve ser originada no SigaMNT Frotas e seguirá as regras normais do BackOffice.  
   
 Após seguir todo o fluxo parametrizado para o pedido de pagamento, iniciará o fluxo de pagamento das parcelas definidas. Ao efetivar a baixa ou estorno do pagamento de títulos (lançamentos financeiros) no módulo de gestão financeira, o BackOffice se encarregará de reportar este evento ao sistema de manutenção de frotas através da mensagem InfoOfParcelValues.  
   
   
   
   
   
 **Fluxo da Integração**  
   
   
 **1.**  **Cadastramento da multa**  
    
 **vO cadastramento da multa é efetuado por geração por notificação ou por geração direta. A geração da multa dispara o gatilho de integração do pedido de pagamento, conforme descrito no item seguinte.**  
   
 **2.**  **Integração do pedido de pagamento**  
   
 **Inclusão:** Na inclusão de uma multa o SigaMNT Frotas envia a mensagem "Order" a fim de incluir o pedido de compras no módulo de compras do BackOffice RM, informando o parcelamento selecionado.  
            
 **Alteração:** A alteração de uma multa no SigaMNT Frotas pode gerar a integração da mensagem "Order" a fim de atualizar os dados do pedido de compras no módulo de compras do BackOffice RM, caso os dados alterados façam parte do escopo do pedido. A alteração passará por todas as validações do BackOffice, que retornará se é possível alterar o pedido na sua situação atual.  
    
 **Exclusão:** A exclusão de uma multa no SigaMNT Frotas pode gerar a integração da mensagem "Order" com evento de exclusão, a fim de excluir o pedido de compras no módulo de compras do BackOffice RM. A exclusão passará por todas as validações do BackOffice, que retornará se é possível efetuar a exclusão ou não, como por exemplo, caso o pedido já tenha sido faturado.  
    
 **3.**  **Evolução do pedido de pagamento**  
    
 O pedido de pagamento deve passar pelo processo normal do BackOffice definido de acordo com a necessidade do cliente, salvo devidas configurações obrigatórias para a regra de negócio da integração.  
    
 **4.**  **Informe de pagamento ou estorno de pagamento de parcelas**  
    
 Seguindo o processo normal do pedido de pagamento, serão gerados lançamentos financeiros referentes a cada parcela do pedido. O pagamento das parcelas é efetuado a partir da baixa destes títulos.   
    
 Ao efetuar pagamento total ou parcial de uma parcela, será enviada uma mensagem de atualização dos dados ao SigaMNT informando, dentre outras informações, o valor pago, data de pagamento e situação da parcela. O estorno de pagamentos segue o mesmo fluxo citado anteriormente.  
    
 **Pré-Condições :**   
 1.   Sincronizar uma Condição de Pagamento.  
 2.   Sincronizar um Fornecedor  
 3.   Cadastrar infração de transito  no  Protheus SigaMNT.  
 4.   Cadastrar os Orgãos Auturadores no Protheus SigaMNT  
 5.   Configurar o parâmetro TMVPedido Pagamento, que deve referênciar o Tipo de Movimento cadastrado para gerar Pedido de Pagamento .  
 6.   Sincronizar um Produto.  
 7.   Ter importado a Fórmula Visual  para pagamento de parcelas no Backoffice RM.  
   
 O processo de Sinistros e multas é executado  conforme exibido abaixo :   
 **Orgão Autuador**  
 1.   Para incluir um Orgão Autuador de Infrações acesse : Atualizações / Controle de Riscos / Multas / Org. Autuadores.  
 2.   Incluir um novo  registro  
 3.   Preencher os campos  e clicar em Confirmar para salvar o registro.  
 4.   Os campos de preenchimento obrigatório  são :

* + Orgão
  + Nome do Orgão
  + Fornecedor
  + Loja
  + Condição de Pagamento

**Infrações de Transito**  
 1.    Para incluir uma nova infração de Trânsito  acesse: Atualizações / Controle de Riscos / Multas / Infrações Trans.  
 2.   Incluir um novo registro  
 3.   Preencher os campos e clicar em Confirmar para salvar o cadastro.  
 4.   Os campos de preenchimento  obrigatório são  :

* + Infração
  + Valor Multa
  + Pontos
  + Responsabili
  + Tp Infração

**Multas**  
 1.   Para incluir uma nova Multa acesse :  Atualizações / Controle de Riscos / Multas / Multas.  
 2.   Incluir um novo registro .  
 3.   Preencher os campos e   confirmar as parcelas.  
 4.   clicar em Confirmar  
 5.   Os campos de preenchimento obrigatório são  :   
 Aba Cadastro de Multa

* Multa
* Dta. Infração
* Hra. Infração
* Nro. Infração
* Infração
* Local Infrac.
* UF Infrac.
* Orgão Autuad.
* Placa Veicu.
* Status Multa
* Origem Multa
* Rec Auto Inf.
* Rec. Notifica.

Aba Pagamento

* Emissao

6.   Acessar o sistema RM e verificar que foi  criado um  movimento do tipo Pedido de Pagamento para  a  multa criada. O sistema RM permite através da execução de Processos, integral ou parcial , o  pagamento  ou estorno do das parcelas do pedido de pagamento gerado  ao cadastrar a multa. O número de parcelas varia de acordo com a condição de pagamento selecionada no momento do cadastro.  
 **Observações :**

1. Para que o sistema Protheus SigaMNT consiga enviar as Multas  ao Backoffice RM é necessario que seja feita  no  sistema RM  a **Mensagens Order com o campo 'ordertypecode' igual a '000' geram movimentos do  tipo Pedido de Pagamento.**
2. Para o funcionamento  do processo de sinistros e multas, é necessário que os parâmetros "  Integrado com SigaMNT " e "Integrado com Multas, Documentos e Honorários de Despachante"  Tenham sido selecionados na configuração do Tipo de Movimento.
3. Não será possível alterar o fornecedor, data de emissão ou valor do movimento internamente ao BackOffice.
4. As informações de parcelamento não poderão ser alteradas via BackOffice, sendo desabilitada a inclusão, alteração e exclusão de parcelas.
5. Será desabilitada a inclusão e exclusão de itens de movimento, visto que os serviços a serem pagos não devem ser alterados via BackOffice.
6. Os dados de produto, quantidade, unidade de medida, preço unitário e descontos dos itens de movimento não poderão ser alterados via BackOffice.
7. Pedidos de Pagamento  criados á partir do recebimento de Mensagens ORDER, enviada ao cadastrar uma  multa,  não poderão  ser cancelados ou excluídos no Backoffice RM.
8. Ao gerar uma multa direta ou por notificação no SigaMNT, é disparado a mensagem "*Order"*  com o campo "ordertypecode"  igual a '000' gerando assim um pedido de pagamento no BackOffice RM que ficará responsável por gerir o fluxo do pedido de pagamento até sua baixa efetiva.
9. Ao efetivar a baixa ou estorno do pagamento de títulos (lançamentos financeiros) no módulo de gestão financeira, o BackOffice se encarregará de reportar este evento ao sistema de manutenção de frotas através da mensagem "InfoOfParcelValues".

---

**Para mais informações sobre o processo de Sinistros e Multas, acesse os boletins técnicos.**

Recursos Adicionais

---

**TDN - Boletim Técnico :** [**Processo de Sinistros e Multas**](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_SINISTROS+E+MULTAS_BR_CON000158.pdf?version=1&modificationDate=1380053414000)
