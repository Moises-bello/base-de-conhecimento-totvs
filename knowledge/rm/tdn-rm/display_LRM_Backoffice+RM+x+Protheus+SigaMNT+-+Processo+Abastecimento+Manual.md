---
content_hash: 06893ef91fa63a887510860d43be7555d3492bbe4c8d1a224f4487657cf7fdc0
fetched_at: '2026-06-29T00:09:36.801835+00:00'
page_id: '425459523'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo Abastecimento Manual
type: documentation
url: https://tdn.totvs.com/display/LRM/Backoffice+RM+x+Protheus+SigaMNT+-+Processo+Abastecimento+Manual
version: 2
---

**Backoffice RM x Protheus SigaMNT - Processo Abastecimento Manual**

---

A rotina Abastecimento Manual tem a função de permitir o registro manual de notas de Abastecimento que venham a ocorrer  em postos Internos ou Externos. A integração Linha RM x Protheus SigaMNT está preparada para  enviar ao Backoffice RM as notas de Abastecimento manual ou  mante-las  sem enviá-las  com o objetivo de  as utilizar em Conciliação de abastecimentos de acordo com o valor definido para o parâmetro MV\_ESTHOME. Ao efetuar a inclusão de uma nota de Abastecimento Manual no Protheus SigaMNT, se o parâmetro MV\_ESTHOME estiver  com o valor "S" , ela será enviada ao Backoffice RM através  da  mensagem única e para  esta nota será criado um movimento de Baixa de estoque se o posto qual o abastecimento foi feito  for um Posto Interno , ou um movimento  de Pedido de Compra,se o abastecimento for feito  em um posto externo conveniado ou não conveniado.  
    
    
   
    
    
    
 **Pré-Condições:**

1. 1. Ter Sincronizado um Produto.
   2. Ter sincronizado um Local de Estoque
   3. Ter sincronizado uma Unidade de Medida
   4. Ter sincronizado um Fornecedor
   5. Ter sincronizado uma Condição de Pagamento
   6. Ter sincronizado um Centro de Custo
   7. Ter sincronizado um Ativo
   8. Configurar o Parametro MV\_ESTHOME com valor "S". no Protheus SigaMNT
   9. Ter Cadastrado um tipo de combustível no Protheus SigaMNT através de : Atualizações / Controle de Combustíveis / Cadastros Postos / Tipo de Combustíveis.
   10. Classificar um Veículo(Patrimônio) sincronizado através da integração como Ativo Fixo acessando : Atualizações / Controle de Oficina / Bens / Bens
   11. Vincular o tipo de combustível cadastrado ao Veículo acessando : Atualizações / Controle de Oficina / Bens / Bens / Visualizar / Ações Relacionadas/Tanques.
   12. Incluir um Posto Interno informando o combustível cadastrado e relacionando a um produto sincronizado do estoque acessando : Atualizações / Controle de Combustíveis / Cadastros Postos / Postos.
   13. Incluir um Tanque para o posto cadastrado, acessando : Atualizações / Controle de Combustíveis / Cadastros Postos / Posto Interno / Tanques e Bombas.
   14. Incluir uma Bomba e vinculá-la ao tanque cadastrado anteriormente, acessando : Atualizações / Controle de Combustíveis / Cadastros Postos / Posto Interno / Tanques e Bombas.
   15. Vincular o estoque à Bomba acessando : módulo de Estoque e Custos / Atualizações / Estoque / Saldos Iniciais.
   16. Incluir o preço do combustível e uma negociação para a Bomba, acessando : Atualizações / Controle de Combustíveis / Cadastros Postos / Postos/ Ações Relacionadas / Incluir Preço e Incluir Negociação.

**Abastecimento Manual**   
    
 1.  Para incluir um novo Abastecimento Manual acesse : Atualizações / Controle de Combustíveis / Abastecimento / Abast. Manual.  
 2.   Incluir um novo registro.  
 3.   Preencha os campos  e clique em confirmar para salvar o cadastro.Os campos de preenchimento obrigatório são :

* N.Abastec
* Frota
* Cod.posto
* CNPJ / CPF
* Combustível
* Dt.Abastec
* Hora
* Quantidade

4.   No Backoffice RM acesse o caminho a seguir  e informe o código do movimento de baixa de estoque  : RM/Backoffice/Gestão de Estoque, Compras e Faturamento/Estoque/Baixa de Estoque.  
    
 **Observação  :**   
    
 1.   Para efetuar a movimentação de estoque no BackOffice deve ser utilizada a versão 1.002 da mensagem Stockturnover, sendo utilizado o campo Type para diferir entre movimentação de entrada ou saída de estoque.

---

Para mais informações sobre o cadastro do Abastecimento Manual, acesse os boletins técnicos.

**Recursos Adicionais**

TDN - Boletim Técnico : [Processo de Abastecimento Manual](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_ABASTECIMENTO+MANUAL_BR_CON000158.pdf?version=1&modificationDate=1380053409000)
