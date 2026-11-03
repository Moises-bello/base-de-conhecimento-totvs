---
content_hash: f0128019e684985e52f741d460dfa613f549969a21ff889239c4d77b35325881
fetched_at: '2026-06-29T00:11:32.083292+00:00'
page_id: '744469090'
product: rm
source: tdn-rm
title: Empreendimento - Aba - Portal de Imóvel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=744469090
version: 3
---

Ao acessar a aba de **Portal de Imóvel** na edição do Empreendimento são exibidos os campos abaixo:

Agrupador **Comissão:**  Neste agrupador são exibidos os campos abaixo que são utilizados para gerar a Comissão (no modelo antigo), pelo Portal de Imóveis:

* **% Pago pela Empresa:** É o percentual da comissão que será pago pela Empresa quando na proposta a comissão for paga por esta entidade;
* **% Pago pelo Cliente:** É o percentual da comissão que será pago pela Cliente quando na proposta a comissão for paga por esta entidade;

Agrupador **Proposta de Venda**:

* **% de Perda VPL**: Define o percentual de VPL aceitável, quando o Plano de Financiamento da proposta é trazido a valor presente. Este cálculo é realizado para validar as alterações nos valores das parcelas e datas de vencimento, que são realizadas pelo corretor ao montar a proposta. O sistema considera o Percentual de Perda VPL, que estiver parametrizado na entidade mais específica, ou seja, na que for mais detalhada em relação à proposta.

Ou outras palavras, o sistema respeitará  a seguinte ordem de verificação, partido da entidade mais específica, para a mais genérica, caso aquela não tenha esta informação parametrizada:

1° - [Alçada de Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=641678463), localizado no Portal do Imóvel;

2º - [Modalidade](https://tdn.totvs.com/display/LRM/Plano+-+Modalidades), localizado no TCGI; ou

3º - Empreendimento, localizado no TCGI.

Assim, por exemplo, caso haja uma Alçada de Aprovação parametrizada no Portal de Imóvel, ela irá prevalecer sobre o percentual de perda VPL parametrizado na Modalidade, que por sua vez, prevalece sobre este mesmo percentual parametrizado no Empreendimento.

Para maiores informações sobre o Portal de Imóveis, consulte esta documentação: [TOTVS Construção Gestão de Imóveis - Web - Portal de Imóveis](https://tdn.totvs.com/pages/viewpage.action?pageId=435105077)
