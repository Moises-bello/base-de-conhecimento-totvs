---
content_hash: 93d85fb9c95e578feccd1c0316f88a1de5bfe02a5017ddd7208d12f05a729845
fetched_at: '2026-06-29T00:09:36.760457+00:00'
page_id: '425459517'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo Abastecimento em Lote
type: documentation
url: https://tdn.totvs.com/display/LRM/Backoffice+RM+x+Protheus+SigaMNT+-+Processo+Abastecimento+em+Lote
version: 2
---

**Backoffice RM x Protheus SigaMNT - Processo Abastecimento em Lote**

---

A rotina de Abastecimento em Lote permite realizar vários lançamentos simultâneos de abastecimentos e outros serviços como troca de óleo, obtendo agilidade no processo de abastecimento no Protheus SigaMNT. Para cada  abastecimento  informado na nota de Abastecimento  em Lote é gerada uma mensagem de Consulta de saldo (StockLevel)  e após  a confirmação é feita a Baixa de Estoque (StockTurnOver). Esta rotina também permite registrar outras saídas de combutstíveis, que não sejam por consumo dos veículos, como por exemplo: vazamentos, retirada para aferição, etc. Para que o Abastecimento em Lote seja efetuado e  enviado ao Backoffice  através  da integração  LinhaRM x Protheus SigaMNT é necessário que o parâmetro MV\_ESTHOME  no módulo SigaCFG do Protheus esteja  configurado com o valor "S".  
 O Abastecimento em lote é  permitido apenas para lançamentos informando Postos Internos.  
    
    
      
    
    
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

**Abastecimento  em Lote.**  
    
 1.   Para incluir um Abastecimento em Lote  acesse  : Atualizações / Controle de Combustíveis / Abastecimento / Abast. Lote Posto Int  
 2.   Incluir um novo registro  
 3.   Preencher os campos e  clicar em Confirmar para salvar o registro. Os campos de preenchimento obrigatório são  :

* Data
* Hora
* Tipo Lançamento
* Folha
* Posto
* Loja
* Atual
* Tanque
* Bomba
* Data Abast.
* Hora Abast.
* Veiculo
* Placa
* Contador
* Quantidade
* Lubrificante
* Qtde.Lub
* Almoxarifado

4.   No Backoffice RM acesse o caminho a seguir e informe o código do movimento de baixa de estoque : RM/Backoffice/Gestão de Estoque, Compras e Faturamento/Estoque/Baixa de Estoque.  
    
 **Observações**  
    
 Para incluir um Abastecimento em Lote  é necessário  selecionar o  Tipo de Lançamento  que contém as  opções abaixo:

·         Abastecimento;  
 ·         Abastecimento + Lubrificante: nesta opção quando confirmado o abastecimento é aberto automaticamente uma ordem de serviço corretiva para o bem e serviço definido no campo lubrificante.   
 ·         Lubrificante.

---

Para mais informações  sobre  o cadastro do Abastecimento  em Lote, acesse  os boletins técnicos

**Recursos Adicionais**

TDN - Boletim Técnico :   [Processo de Abastecimento em Lote](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_ABASTECIMENTO+EM+LOTE_BR_CON000158.pdf?version=1&modificationDate=1380053408000)
