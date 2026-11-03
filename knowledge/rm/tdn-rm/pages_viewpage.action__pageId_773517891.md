---
content_hash: f2b0dfeb5cb39938ea1c60b730ed58caefc1eac6b40de1a79543a1cd9d1873e4
fetched_at: '2026-06-29T00:11:36.779809+00:00'
page_id: '773517891'
product: rm
source: tdn-rm
title: TCGI - Comissão - Regras de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773517891
version: 7
---

### **Cadastro de Regras de Pagamento Comissão.**

Este cadastro , tem o objetivo de determinar a regra de cálculo de cada "vendedor" ou "entidade comissionada", independente se o pagamento da comissão for realizado pela empresa ou pelo próprio cliente. 

Primeiro é preciso habilitar o Perfil para usar o novo modulo Comissões

Para utilizar o Cadastro de Regras Pagamento Comissão , é preciso primeiro liberar acesso para o Perfil do usuário em:  
clique na aba "Acesso a Menus" em 'Gestão de Imóveis >> Venda >> Contratos >> Comissões >> [01.01.04.01] Regras de Pagamento'

Os tipos de parâmetros que são definidos para o pagamento pela empresa e pelo cliente são diferentes e são eles:

Por empresa:

* Valor fixo não vinculado ao recebimento das parcelas
  + Número de parcelas (caso o tipo "Valor fixo" seja selecionado)
* Percentual Máximo vinculado ao recebimento das parcelas
  + Percentual máximo vinculado ao recebimento (caso o tipo "Percentual máximo seja selecionado)
  + Fórmula para definir o % máximo vinculado ao recebimento (caso o tipo "Percentual máximo seja selecionado)
* Valor Parcela Fórmula **\*12.1.2310**
  + Fórmula para definir o valor da parcela (com esta regra, o valor das parcelas de um comissionado pode ser diferente em cada parcela)

Por Cliente:

* Decrescente: Determina a prioridade dos componentes geradores de parcelas para realizar o pagamento da comissão;
* Parcelas Iguais: Determinar que o valor da comissão será rateado de forma igualitária entres todos os componentes utilizados na proposta;
* Proporcional: Determina que valor da comissão será descontado na forma proporcional de cada componente sobre o valor total.

Se marcar a opção 'Utilizar Componentes Específicos' é possível selecionar componentes/Valores de Integração específicos para o cálculo da comissão e definir a prioridade de uso cada um.

Se desmarcado, serão utilizados todos os componentes/Valores de Integração da proposta do cliente/Plano de Financiamento

Ao inserir um novo Componente da Regra de Pagamento da Comissão, o usuário deverá preencher os campos:

* **Prioridade:** este campo é utilizado para definir a ordem de prioridade de desconto da Comissão e deve ser preenchido com valores entre 1 e 100, Sendo que um componente com o valor de Prioridade 1 prevalece sobre um componente de prioridade 2 ou superior.
* **% Máximo Desconto Comissão Cliente:** este campo serve para limitar o desconto máximo deste componente na hora de calcular a Comissão paga pelo Cliente na Mesa e deve ser preenchido com valores numéricos entre 1 e 100%.
* Se o tipo de Contrato for Venda  deve-se selecionar os componentes geradores de parcelas dos tipos Entrada, Principal para utilização no cálculo da comissão.
* Se o tipo de Contrato for Aluguel o campo Código de Integração será habilitado e para se informar o código de integração com o módulo de Aluguel que será utilizado no calculo da comissão.
