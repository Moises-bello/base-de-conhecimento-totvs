---
content_hash: 35c2b9513572c21912f7e8703c287bba97cbf147fe464ce2ab03f6d0cc1ddffe
fetched_at: '2026-06-29T00:09:49.663264+00:00'
page_id: '435105342'
product: rm
source: tdn-rm
title: Condomínio - Fechamento do Condomínio - Cobrança Direta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105342
version: 9
---

O cadastro de cobrança direta permite ao administrador de condomínios cadastrar cobranças fixas ou esporádicas que irão incidir no condomínio como, por exemplo, taxa de condomínio fixa, fundo de reserva e multas por infrações no empreendimento. As cobranças podem ser associadas a empreendimentos, ou a unidades ou a subunidades. Essa associação é considerada depois no fechamento do condomínio.

**Aba Identificação:** 

* **Cód. Cobrança Direta:** Código identificador definido pelo sistema para o cadastro de Cobrança Direta.
* **Item de cobrança:** Informe o item de cobrança que será utilizado para o fechamento das despesas.
* **Descrição**: Informe a descrição desta cobrança direta.
* **Modelo de rateio:** permite indicar o modelo de cálculo que será utilizado no rateio.
* Os tipos de Rateio são:

* + [Rateio por Fração Ideal](http://tdn.totvs.com/pages/viewpage.action?pageId=435105183)

* **Data inicial**: A data inicial da cobrança. Esta informação é obrigatória.
* **Data final**: A data final da cobrança. Esta informação não é obrigatória dado que uma cobrança pode ser recorrente sem data final definida.
* **Valor**: O valor da cobrança que será apurado no fechamento do condomínio. Caso o valor for definido, o campo Fórmula será desativado. Não serão possíveis cadastros de valores negativos neste campo.
* **Fórmula**: Informe a fórmula que será utilizada para calcular o valor a ser apurado. Caso a fórmula for definida, então o campo Valor será desativado. Para mais informações referentes a utilização de formulas acesse:

Tipos de associações das cobrançasTambém é possível definir se a cobrança será associada a empreendimento, unidade ou subunidade. O sistema não permite associação em níveis diferentes. Após a escolha do tipo de associação então o usuário deve definir os empreendimentos/unidades/subunidades.  
No caso de associação de um conjunto de unidades, o sistema permite unidades de diferentes empreendimentos. No caso de associação de um conjunto de subunidades, o sistema permite subunidades de diferentes unidades e empreendimentos.Visualização das associações

Na visão de Empreendimento / Unidade / Subunidade foi criado o anexo "Cobranças Diretas associadas" para a visualização das associações feitas. Neste anexo é possível realizar a exclusão de uma determinada associação. Nesta visão não é possível incluir ou editar.

Regra para ser considerada no cálculo do fechamentoA cobrança será considerada no cálculo de um fechamento quando ela se iniciar ou finalizar dentro da competência do fechamento, ou se começar antes e terminar depois da competência.Travamento da edição de informações da cobrançaQuando a cobrança já estiver sido calculada em algum fechamento de condomínio, então o sistema não irá permitir a sua edição ou exclusão. Apenas o campo de data final e as associações poderão ser alteradas. Quando a data final for alterada não poderá ser menor do que a data do último período fechado.
