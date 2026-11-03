---
content_hash: 2addc652e65c53404b28c9d784a75b16ffb5369bd3a66b201f65dab6f6189273
fetched_at: '2026-06-29T00:09:47.926008+00:00'
page_id: '435105104'
product: rm
source: tdn-rm
title: Cobrança por Orçamento - Modelo de Cálculo de Rateio - Valor Fixo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105104
version: 5
---

Nesse rateio o valor da despesa será aplicado diretamente para a subunidade.    
 Como exemplo, podemos citar o Fundo de Reserva de um Empreendimento, onde todas as Subunidades precisam pagar o mesmo valor. Dessa forma basta cadastrar essa Despesa, utilizando como Tipo de Rateio o Valor Fixo, e associar ao Empreendimento.    
 Nesse modelo o usuário poderá definir as seguintes associações:

* **Um empreendimento:** O valor da despesa será replicado para todas as subunidades do empreendimento definido;
* **Uma ou mais unidades:** O valor da despesa será replicado para todas as subunidades da unidade ou de um conjunto de unidades;
* **Uma ou mais subunidades:** O valor da despesa será aplicado diretamente na subunidade definida ou no conjunto de subunidades. Neste caso todas as subunidade devem ser da mesma unidade;

Dessa forma esse rateio pode ser aplicado para todas as despesas associadas aos seguintes níveis:

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Valor fixo | X | X | X |

**Observações:**

* Caso pelo menos uma das subunidades estiver associada a um imóvel do módulo de Aluguel, tendo como Tipo de Locação "Áreas Fracionadas", a apuração não será executada para a despesa relacionada.
* Caso a(s) subunidade(s) esteja(m) associada(s) a imóvel(is) do módulo de Aluguel, tendo como Tipo de Locação "Áreas Unificadas", a apuração será executada normalmente, pois não existe rateio para este tipo de locação.

Veja Também

---

* # [Manutenção de Empreendimentos - Condomínio](http://tdn.totvs.com/pages/viewpage.action?pageId=435105121)
