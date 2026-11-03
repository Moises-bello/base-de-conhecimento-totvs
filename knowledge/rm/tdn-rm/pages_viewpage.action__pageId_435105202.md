---
content_hash: d6b4489f35105941bf217ba44d10b24a7ce2344203077b06b3b933366278feb5
fetched_at: '2026-06-29T00:09:48.603603+00:00'
page_id: '435105202'
product: rm
source: tdn-rm
title: Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio por M² Locado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105202
version: 7
---

O cálculo de rateio por M² Locado irá obter inicial o metro quadrado locado do empreendimento. Para obter então o valor total locado do empreendimento, o sistema percorre todos os contratos de locação de todos os imóveis/subunidades do empreendimento e soma a área locada.

|  |
| --- |
| \*Fator M² Locado = Valor Total da Despesa / M² Locado Empreendimento\* |

Com o fator calculado, o sistema irá realizar o rateio para cada subunidade do empreendimento considerando o M² locado do imóvel/subunidade.

|  |
| --- |
| \*Valor Rateio = Fator M² Locado \* M² Locado Subunidade\* |

Para obter o M² locado do imóvel/subunidade, o sistema carrega todos os seus contratos de locação ativos e obtém a área locada pela tabela XALGCONTRATOLOCIMOVELAREA. Esta tabela armazena o histórico das locações das áreas, portanto o sistema obtém a área locada de acordo com a competência do fechamento.   
O rateio será feito para cada contrato de locação, gerando assim posteriormente lançamentos diferentes para contratos de locação diferentes.  
Em caso de vacância, o sistema irá verificar a área que não está locada e então calculará também o seu rateio. Posteriormente este rateio também terá o seu lançamento financeiro gerado.  
Neste modelo o usuário pode definir as seguintes associações:

* **Um empreendimento:** Rateio será realizado para todas as subunidades do empreendimento definido;
* **Uma ou mais unidades:** Rateio será realizado para todas as subunidades da unidade ou de um conjunto de unidades;
* **Uma ou mais subunidades:** Rateio será realizado diretamente na subunidade definida ou no conjunto de subunidades.

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Rateio por M² Locado | X | X | X |

* **Observação:**
  + Caso pelo menos uma das subunidades **não** estiver associada a um imóvel do módulo de Aluguel , tendo como Tipo de Locação "Áreas Fracionadas" ou "Áreas Unificadas", a apuração não será executada para a despesa relacionada.

Veja Também

---
