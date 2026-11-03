---
content_hash: 0aa2f411dea48a260b405e0a7c09c7eda09e78f9dd43bdcb0915e45de30dd8f0
fetched_at: '2026-06-29T00:09:48.559837+00:00'
page_id: '435105189'
product: rm
source: tdn-rm
title: Gestão Financeira - Rateio - Valor Fixo por M²
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105189
version: 3
---

Nesse rateio o valor da despesa definido em metro quadrado será aplicado diretamente para a subunidade conforme a sua área.    Como exemplo, podemos citar o Fundo de Reserva de um Empreendimento, onde todas as Subunidades precisam pagar o mesmo valor da metro quadrado. Dessa forma basta cadastrar essa cobrança utilizando como Tipo de Rateio o Valor Fixo por metro quadrado e associar ao empreendimento.

|  |
| --- |
| Valor Rateio = Valor fixo M² **Área da subunidade** |

Para obter a  Área da subunidade, o sistema possui 2 formas. Para definir qual a forma será utilizada, é verificado o parâmetro do Empreendimento **"Gestão de Condomínio integrado à Gestão de Aluguel"**. Sendo assim essa forma de busca do valor será aplicado para o empreendimento e suas unidades e subunidades. Segue o comportamento do sistema conforme o estado do parâmetro:

* **Parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" MARCADO:** A busca da área de uma subunidade será realizada pelo somatório das áreas do imóvel, associada a subunidade, que possua tipo de locação Áreas Fracionadas ou Unificadas;
* **Parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" DESMARCADO:** A busca da área de uma subunidade será realizada pelo o valor do campo "Área m²" do cadastro da subunidade.

Quando o Empreendimento estiver com o parâmetro citado marcado, o rateio será feito para cada contrato de locação, gerando assim posteriormente lançamentos diferentes para contratos de locação diferentes.  
 Em caso de vacância, o sistema irá verificar a área que não está locada e então calculará também o seu rateio. Posteriormente este rateio também terá o seu lançamento financeiro gerado.   
 Quando o parâmetro estiver desmarcado, será observado o ocupante que seja responsável financeiro da subunidade, e que sua data inicial seja anterior e a data final posterior à competência do fechamento, para que possa ser gerado o lançamento financeiro.

* **Um empreendimento:** Rateio será realizado para todas as subunidades do empreendimento definido;
* **Uma ou mais unidades:** Rateio será realizado para todas as subunidades da unidade ou de um conjunto de unidades;
* **Uma ou mais subunidades:** Rateio será realizado diretamente na subunidade definida ou no conjunto de subunidades.

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Valor fixo por M² | X | X | X |

**Observações:**

* Quando o Parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" estiver **MARCADO** e a subunidade estiver associada a um imóvel com tipo de locação igual à "Imóvel", o sistema não permitirá que o rateio seja realizado;
* Quando o Parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" estiver **MARCADO** e a subunidade não estiver associada a nenhum imóvel, será exibido um erro no cálculo do fechamento, pois não foi encontrada o imóvel para que fosse extraída o valor da área;
