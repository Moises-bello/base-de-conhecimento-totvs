---
content_hash: 3f24afb1a70fcd1e8030cd86f3311cea54f38163160792d29a7e4781e03f4295
fetched_at: '2026-06-29T00:09:33.466385+00:00'
page_id: '425459039'
product: rm
source: tdn-rm
title: Associação de desconto por antecipação à bolsas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459039
version: 2
---

---

Este processo visa facilitar a associação de descontos por antecipação à bolsas condicionais a fim de que essas bolsas sejam validadas até um vencimento especifico conforme descrito previamente em .  
Acessar Financeiro / Contábil | *Formação de preço | Bolsas | Processos | Associação de desconto por antecipação à bolsas.*  
 **Importante** Somente bolsas "**Condicionais**" poderão ser selecionadas para processamento. Caso seja selecionada alguma bolsa "**Incondicional**", o sistema exibirá uma mensagem para o usuário e não permitirá prosseguir com o processo.  
  
 O processo também só estará visível, se o parâmetro de sistema "*Parâmetros \ Integração \ Financeiro \ Educacional \ Fin - Vlrs. Opcionais/Integração 3/3 \ **Mantem fórmula default para valor opcional / integração de bolsas condicionais"*** estiver marcado.  
  
 São três status possíveis para os registros de associação do processo:  
  
 **Banco de dados:** Indica que a associação entre o desconto por antecipação e a bolsa já existe no banco de dados. Esse registro permanecerá inalterado na execução do processo.  
  
 **Inclusão:** Indica que a associação entre o desconto por antecipação e a bolsa será incluída no banco de dados após execução do processo. Somente terão esse status, os registros que não existiam no banco de dados. Caso a associação do desconto já exista para alguma bolsa, o sistema não adicionará nenhuma linha no grid de associação.  
  
Para associar desconto por antecipação à bolsas basta selecionar o ***Id. do desconto por antecipação*** e em seguida o ***item desconto por Antecipação*** e clicar em adicionar. Sendo possível adicionar um ou mais descontos para execução.  
  
 **Exclusão:** Indica que a associação entre o desconto por antecipação e a bolsa será excluída no banco de dados após execução do processo. Somente os registros carregados do banco de dados terão esse status. Caso o usuário tenha incluído no processo uma associação que não existia previamente no banco de dados, o respectivo registro será excluído da grid de associações.

Para excluir um desconto que foi adicionado basta selecionar no grid quais os descontos que deseja excluir e clicar no botão ***Remover.***É possível também desfazer as alterações de associações de desconto por antecipação à bolsas feitas anteriormente e carregar os registros de associações existentes, clicando no botão ***Carregar associações existentes****.*  
 Após a execução do processo, o sistema exibirá um log com todas as inclusões e exclusões feitas.
