---
content_hash: 5c0119423a71e8684a153b6b5431ecd8d49b9d9b274ede0b04897097e03b3f16
fetched_at: '2026-06-29T00:09:34.457204+00:00'
page_id: '425459158'
product: rm
source: tdn-rm
title: Valor simulado da Parcela
type: documentation
url: https://tdn.totvs.com/display/LRM/Valor+simulado+da+Parcela
version: 12
---

---

Antes de gerar a  é possível realizar o cálculo simulado do valor da parcela.

Esta funcionalidade retorna informações relacionadas aos valores utilizados para o cálculo de uma ou várias parcelas, respeitando as regras parametrizadas no sistema, por exemplo:

* Valor calculado por créditos;
* Bolsa válida após o vencimento e etc.

**Importante:**  
O processo de calcular os valores simulados é apenas visual, não sendo possível recuperar essa informação via banco de dados. O intuito dessa funcionalidade é permitir que o usuário visualize os valores sem ter a necessidade de gerar a parcela, projetando no momento vigente a geração dos valores de forma independente dos lançamentos em aberto.

Para que o usuário consiga simular o valor das parcelas é necessário seleciona-las e então clicar no botão 'Simular cálculo' (canto inferior direito da tela).  
O uso desta funcionalidade possibilita que o usuário visualize os valores que serão gerados para o aluno.  
Após a execução, os valores simulados serão retornados em colunas especificas na visão de parcelas, tais como:

* Valor original do lançamento
* Valor bolsa condicional
* Valor bolsa incondicional
* Valor do desconto
* Valor líquido (= Valor original – descontos – bolsas)
* Valor simulado (disponível para o nível superior = valor calculado conforme o número de créditos)
* Valor Crédito Retroativo (utilizado apenas para o Segundo modelo de Bolsa Retroativa: Criando lançamentos de devolução / Movimentando a Conta Corrente, quando configurado para gerar lançamentos de devolução)
* Descontos por Antecipação (caso o aluno tenha direito a algum , os valores dos descontos serão apresentados separadamente em colunas específicas para cada vencimento, conforme definido em cada item de desconto. Ao posicionar o cursor do mouse sobre o valor do desconto apresentado na tela, o sistema mostrará a data limite à qual o aluno terá direito ao desconto. Se na simulação o cálculo do valor original - valores de descontos - valores de bolsas for negativo, esse valor negativo calculado será apresentado. O valor líquido na simulação considera o maior valor do desconto por antecipação apresentado)

**Importante:**  
O sis476pxtema irá simular os valores dos lançamentos conforme parametrização realizada na base, assim o valor líquido da parcela, assim como os valores de bolsas e descontos poderão ser simulados com diversos resultados. Para saber mais detalhes, consulte o help sobre os  e sobre os .

Se por algum motivo a simulação não retornar valores, o sistema deve apresentar na tela uma mensagem alegando o motivo da não geração.   
 

   Como Fazer 

---

[Simulação de parcelas de contratos via webservice](http://tdn.totvs.com/pages/viewpage.action?pageId=392496907)[Simulação de parcelas de contratos utilizando plano de pagamento via webservice](http://tdn.totvs.com/x/ChkwGg)
