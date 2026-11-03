---
content_hash: b11dbbc86a186c53bf6bcdedce177ba34a04edb0fac27bf088f694ec31fc2ae6
fetched_at: '2026-06-29T00:09:49.194816+00:00'
page_id: '435105252'
product: rm
source: tdn-rm
title: Gestão Financeira - Rateio - Rateio por M² Ocupado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105252
version: 6
---

O cálculo de rateio por M² ocupado irá obter inicialmente a soma de todas as áreas da subunidade que possuem associado algum ocupante que seja responsável financeiro.   
 Com este valor, o sistema realiza o cálculo do fator que será utilizado para calcular posteriormente o valor do rateio.

|  |
| --- |
| Fator M² Ocupado = Valor Total da Despesa / M² Total áreas ocupadas |

* **Observação:** Em caso da despesa estiver associada a uma unidade, o cálculo do fator irá utilizar o total das áreas dessa unidade. Em caso da despesa estiver associada a um conjunto de subunidades, o cálculo irá utilizar o total dessas subunidades.

Com o fator calculado, o sistema irá realizar o rateio somente para as subunidades que possuem o ocupante válido.

|  |
| --- |
| Valor Rateio = Fator M² Ocupado \*  Área da subunidade |

A busca da área de uma subunidade será realizada pelo o valor do campo "Área m²" do cadastro da subunidade que possua um ocupante válido.

Será observado o ocupante que seja responsável financeiro da subunidade, e que sua data inicial seja anterior e a data final posterior à competência do fechamento, para que possa ser gerado o lançamento financeiro.

**Exemplo de aplicação do rateio:**

* Empreendimento X
  + Unidade A
    - Subunidade 101 - 100 m² (ocupado)
    - Subunidade 102 - 50 m² (ocupado)
    - Subunidade 103 - 200 m²
* Despesa = R$ 1.000,00 associada ao empreendimento X

|  |
| --- |
| Fator M² Ocupado = Valor Total da Despesa / M² Total áreas ocupadas |

|  |
| --- |
| Fator M² Ocupado = 1.000,00 / 150 = 6,666 |

|  |
| --- |
| **Valor Rateio Subunidade 101 = 6,66 \* 100 = 666,66** |

|  |
| --- |
| **Valor Rateio Subunidade 102 = 6,66 \* 50 = 333,33** |

* **Um empreendimento:** Rateio será realizado para todas as subunidades do empreendimento definido;
* **Uma ou mais unidades:** Rateio será realizado para todas as subunidades da unidade ou de um conjunto de unidades;
* **Uma ou mais subunidades:** Rateio será realizado diretamente na subunidade definida ou no conjunto de subunidades.

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Valor fixo por M² | X | X | X |

**Observações:**

* Esse rateio somente é válido para Empreendimento que tenha o parâmetro "Gestão de Condomínio integrado à Gestão de Aluguel" **DESMARCADO**. Caso seja utilizado em um empreendimento que esteja com o parâmetro **MARCADO,** o sistema irá impedir a execução do rateio, exibindo uma mensagem de erro.
