---
content_hash: 584a0ba1f9e94dfad0286c4a361ea09bde989b1677b652fa65a7074852123236
fetched_at: '2026-06-29T00:09:49.420077+00:00'
page_id: '435105286'
product: rm
source: tdn-rm
title: Condomínio - Fechamento do Condomínio - Tarifa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105286
version: 10
---

O cadastro de tarifa permite o usuário informar o valor que será cobrado pelo fornecimento de determinado insumo, por exemplo água e luz. Este preço deve ser estabelecido pelo condomínio conforme gestão interna. Neste cadastro será informado um valor unitário da unidade de medida configurada no medidor e sem a possibilidade de indicação de valores variados por faixa de consumo.

**Figura 1 - Tela de cadastro da Tarifa**

* **Cód. Tarifa:** código identificador do cadastro de Tarifa;
* **Descrição:** campo livre onde o usuário poderá descrever a identificação da Tarifa. Ex: período de bandeira vermelha;
* **Data inicial:** data no formato (mês/ano) a partir da qual a tarifa deve ser utilizada no cálculo. Campo obrigatório;
* **Data final:** data final no formato (mês/ano) que a tarifa deve ser utilizada no cálculo;
* **Valor da tarifa:** permite indicar manualmente o valor da tarifa, neste campo poderá ser informado até quatro casas decimais caso seja necessário.
* **Fórmula**: indica a fórmula que será utilizada para calcular o valor da tarifa. Esta fórmula será executada no fechamento do condomínio. Caso a fórmula não for definida, então o sistema utiliza o valor da tarifa.
  + Para auxiliar no desenvolvimento desta fórmula, foi disponibilizado a função de fórmula TABMEDIDOR, que obtém os valores de determinados campos do medidor e seus anexos de medições e tarifas.  
    Para mais informações da função acesse:

O sistema não permite incluir tarifas com as datas em interseção para o mesmo medidor.  
A tarifa pode ser associada a um ou mais medidores. Essa associação pode ser realizada em cada medidor ou através do processo "Associar Tarifa". Para base mais sobre o processo "Associar Tarifa", clique aqui

Informações Complementares

---



Como Fazer

---
