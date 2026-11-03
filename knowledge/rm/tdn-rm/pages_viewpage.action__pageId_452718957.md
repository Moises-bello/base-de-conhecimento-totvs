---
content_hash: 042c31b21bb15d5eeeabef9a627461236c8f0509c912e93c179b2521c866add5
fetched_at: '2026-06-29T00:10:02.559429+00:00'
page_id: '452718957'
product: rm
source: tdn-rm
title: Eventos Adicionais Globais - 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718957
version: 2
---

Nesta etapa será configurado os eventos adicionais que irão compor a base de cálculo de 13º Salário. Para inserir, excluir ou editar um evento, use os respectivos ícones na parte superior desta etapa.  
    
 **Campos**

Cod. Evento Recibo   
 Selecione o evento a ser somado para compor a base de 13º salário. Este evento será somado ao valor calculado para 13º salário 1ª parcela, rescisão (parte proporcional e parte indenizada) e será discriminado no pagamento da 2ª parcela de 13º salário.

**Observações**

* Para que este evento seja considerado no pagamento da 1ª parcela de 13º salário é preciso que o parâmetro "Paga eventos adicionais na 1ª parcela de 13º salário" em PARAMETRIZADOR | 13º SALÁRIO | CÁLCULO esteja marcado.
* Os eventos cadastrados devem ter o código de cálculo 102 vinculado para que sejam considerados nas rotinas.

Valor

Digite o valor deste evento, caso o evento tenha fórmula deixe este campo zerado.

**Observação**  
 Este valor não será proporcionalizado para isto o usuário deverá criar uma fórmula de proporcionalização. 

**Exemplo**

Se o usuário quer pagar um evento de Prêmio de 13º salário para todos os funcionários e existem funcionários que receberão 13º proporcional poderá fazer da seguinte forma: 100/12 \* NROAVOS13 (Cem reais dividido por 12 meses multiplicado pelo número de avos de 13º salário que o funcionário tem direito), sendo que deve ser feita todas as considerações nesta fórmula para atender a casos específicos.  
 Fórmula de seleção

É necessário informar uma fórmula (previamente cadastrada) para definir o universo de funcionários a que tais eventos serão aplicáveis.  
    
 Número de Vezes  
 Neste campo será informado número de vezes que o evento deve ser lançado. O evento será lançado toda vez que for processada a rotina de Cálculo de 13º Salário. E a cada vez que for pago o 13º salário (1ª e/ou 2ª parcela), este campo será decrementado de 1 vez.

**Exemplo**  
 Número de vezes = 12  
 Lancei a 2ª parcela de 13º salário  
 Número de vezes = 11  
    
 **Observação**

* Caso queira que o número de vezes seja infinito, basta preencher este campo com 999 e a cada vez que for processada a rotina de pagamento de 13º salário este campo não será decrementado.
* O sistema valida o período, então toda vez que for processada o lançamento de 13º salário no mesmo período, caso já tenha sido lançado o evento adicional, o mesmo não será lançado novamente e não será decrementado.
* Quando é processado o cancelamento da folha no período que foi lançado os eventos adicionais junto com as verbas de 13º Salário, o campo número de vezes é incrementado com +1, caso o valor seja diferente de 999.
* Caso este campo seja 0 (zero), não será lançado o evento adicional na rotina de cálculo de 13º salário.

Provisionar evento?  
 Quando este parâmetro estiver marcado, o evento adicional entrará para o cálculo de provisão de 13º salário, quando a opção 'De forma personalizada' estiver marcada na etapa Cálculo em Configurações | Parâmetro | Parametrizador | 13º Salário.  
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Voltar para tela anterior **13º Salário**
