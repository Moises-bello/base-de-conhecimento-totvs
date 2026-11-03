---
content_hash: e76e8a21ec3eff98e7ee68477e8464e11ec7c5fc98016f4c0504f1335e17dbc2
fetched_at: '2026-06-29T00:09:49.485127+00:00'
page_id: '435105299'
product: rm
source: tdn-rm
title: Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio por M² Construído
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105299
version: 9
---

O cálculo de rateio por M² construído irá obter inicialmente o metro quadrado construído do empreendimento no seu cadastro. No exemplo abaixo, o valor a ser considerado é o campo "Área construída (m²)".

Com este valor, o sistema realiza o cálculo do fator que será utilizado para calcular posteriormente o valor do rateio.

|  |
| --- |
| \*Fator M² Construído = Valor Total da Despesa / M² Construído Empreendimento\* |

Com o fator calculado, o sistema irá realizar o rateio para cada subunidade do empreendimento considerando a Área da subunidade.

|  |
| --- |
| \*Valor Rateio = Fator M² Construído \* Área da subunidade\* |

Para obter a  Área da subunidade, o sistema possui 2 formas. Para definir qual a forma será utilizada, é verificado o parâmetro do Empreendimento "Gestão de Condomínio integrado à Gestão de Aluguel". Sendo assim essa forma de busca do valor será aplicado para o empreendimento e suas unidades e subunidades. Segue o comportamento do sistema conforme o estado do parâmetro:

* **Parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" MARCADO:** A busca da área de uma subunidade será realizada pelo somatório das áreas do imóvel, associada a subunidade, que possua tipo de locação Áreas Fracionadas ou Unificadas;
* **Parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" DESMARCADO:** A busca da área de uma subunidade será realizada pelo o valor do campo "Área m²" do cadastro da subunidade

Quando o Empreendimento estiver com o parâmetro citado marcado, o rateio será feito para cada contrato de locação, gerando assim posteriormente lançamentos diferentes para contratos de locação diferentes.  
Em caso de vacância, o sistema irá verificar a área que não está locada e então calculará também o seu rateio. Posteriormente este rateio também terá o seu lançamento financeiro gerado.  
Quando o parâmetro estiver desmarcado, será observado o ocupante que seja responsável financeiro da subunidade, e que sua data inicial seja anterior e a data final posterior à competência do fechamento, para que possa ser gerado o lançamento financeiro.

* **Um empreendimento:** Rateio será realizado para todas as subunidades do empreendimento definido;
* **Uma ou mais unidades:** Rateio será realizado para todas as subunidades da unidade ou de um conjunto de unidades;
* **Uma ou mais subunidades:** Rateio será realizado diretamente na subunidade definida ou no conjunto de subunidades.

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Rateio por M² Construído | X | X | X |

**Observações:**

* Quando o Parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" estiver MARCADO e a subunidade estiver associada a um imóvel com tipo de locação igual à "Imóvel", o sistema não permitirá que o rateio seja realizado;
* **O comportamento acima foi alterado a partir da versão 12.1.2306 do sistema. Agora quando um imóvel não possuir áreas fracionadas, ou seja, for do tipo "Imóvel", o cálculo do rateio levará em consideração o total da área em metros quadrados locada ou ocupada, considerando-a como 100% para esse imóvel.**
* Quando o Parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" estiver MARCADO e a subunidade não estiver associada a nenhum imóvel, será exibido um erro no cálculo do fechamento, pois não foi encontrada o imóvel para que fosse extraída o valor da área.

Veja Também

---

* [Condomínio](http://tdn.totvs.com/pages/viewpage.action?pageId=435105121)
