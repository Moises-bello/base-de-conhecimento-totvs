---
content_hash: 576c85220aa72a45ed8fbc75f0b6c12b592f5338e8ef31d4678393ba9a3de312
fetched_at: '2026-06-29T00:09:35.952478+00:00'
page_id: '425459449'
product: rm
source: tdn-rm
title: Desconto por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459449
version: 42
---

---

Desconto por Antecipação é um recurso disponível no sistema que permite à instituição de ensino cadastrar uma modalidade específica de desconto, válido para determinado período de vigência, composto por uma série de itens (ou faixas) de descontos, com regras específicas de valores e datas para serem concedidos aos alunos que quitarem antecipadamente os boletos referentes às suas mensalidades.

As instituições de ensino podem programar de diversas formas a aplicação dos descontos por antecipação, podendo ter descontos específicos e distintos para cada matriz aplicada, ou para campus/polo da matriz ou ainda para contratos. Basta cadastrá-los e posteriormente associá-los conforme queiram, assim, no momento em que a baixa for registrada, o sistema irá verificar se a baixa foi realizada antecipadamente (antes da data de vencimento) e, tendo desconto por antecipação associado, verificará qual item (ou faixa) de desconto será aplicado conforme quantidade de dias antecipados e então concederá o desconto correspondente.

Na *geração* (inclusão) do lançamento serão sempre considerados os *maiores* descontos cadastrados para compor os valores do lançamento, porém todos os valores de todos os descontos aplicáveis à parcela serão calculados neste momento e armazenados no banco de dados ficando disponíveis para consulta dentro do próprio cadastro da parcela através do Anexo *'Descontos por antecipação da parcela'*. A data de pagamento e valor de pagamento também serão calculados e armazenados no banco. Se o lançamento for *regerado* todos os valores de descontos serão recalculados e regravados no banco de dados.

Tais valores podem ser simulados através do recurso "Calcular valores simulado" presente na visão de parcela do contrato. Na simulação para uma determinada parcela, o sistema irá exibir na forma de coluna o valor para pagamento para cada vencimento cadastrado no desconto por antecipação. Se na simulação o cálculo do valor original - valores de descontos - valores de bolsas for negativo, esse valor negativo calculado será apresentado. O valor líquido na simulação considera o maior valor do desconto por antecipação apresentado.  
   
**Atenção:**  
- O valor para pagamento calculado e armazenado no banco de dados leva em consideração as informações parametrizadas no TOTVS Educacional, tais como descontos de parcela, descontos por antecipação, bolsa e regras da perda da bolsa conforme o desconto por antecipação. Demais valores que serão processados por fórmula no TOTVS Gestão Financeira não irão compor o valor. O cálculo do valor para pagamento é:

* **Valor para pagamento:** Valor da Parcela - Desconto por Parcela - Desconto por Antecipação - Descontos de Bolsa.

Na *baixa*, onde os descontos por antecipação serão efetivamente aplicados, diminuindo o valor líquido do lançamento, nem sempre os maiores descontos serão os considerados, pois neste momento os descontos aplicados serão aqueles diretamente ligados com a quantidade de dias em que a baixa estiver sendo realizada antecipadamente. Se a base de dados estiver parametrizada para , na baixa o sistema poderá ainda fazer um confrontamento entre o maior valor previsto para o desconto (calculado na geração) e o valor realmente concedido de desconto (ligado diretamente à data efetiva da baixa) exibindo-o no respectivo item de baixa.

[Associar os Descontos por Antecipação](https://tdn.totvs.com/pages/viewpage.action?pageId=425458894)  
[Associação Desconto por Antecipação a Bolsa Condicional](https://tdn.totvs.com/pages/viewpage.action?pageId=425458826)  
[Considerar Desconto por Antecipação](https://tdn.totvs.com/pages/viewpage.action?pageId=715145236)  
[Regra de Cálculo do Desconto por Antecipação](https://tdn.totvs.com/pages/viewpage.action?pageId=716345442)  
  
   
  
[Ordem de Aplicação do Desconto por Antecipação](https://tdn.totvs.com/pages/viewpage.action?pageId=716348809)  
[Afeta Base de Cálculo do Desconto por Antecipação](https://tdn.totvs.com/pages/viewpage.action?pageId=716350235)

 Veja Também

---

[Desconto por Antecipação - Mudança de Turma e Transferência Interna](http://tdn.totvs.com/pages/viewpage.action?pageId=329029368)
