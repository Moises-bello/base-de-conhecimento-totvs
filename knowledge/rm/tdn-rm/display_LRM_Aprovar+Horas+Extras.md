---
content_hash: 50449fc761c01077546d7171b727a81d1a36875a35f5952c132bf67282d9695d
fetched_at: '2026-06-29T00:10:08.544421+00:00'
page_id: '452719534'
product: rm
source: tdn-rm
title: Aprovar Horas Extras
type: documentation
url: https://tdn.totvs.com/display/LRM/Aprovar+Horas+Extras
version: 7
---

**Aprovar Horas Extras -** Nesta janela serão exibidas as ocorrências de Hora Extra para aprovação. Este processo consiste em aprovar as extras já executadas ou aprovar um valor diferente das extras executadas. Esta aprovação pode ser feita por Intervalo ou Número de Horas, de acordo com a configuração do Parâmetro 'Considera extra autorizada por intervalo', disponível na 'Etapa 1 - Cálculo' do Parametrizador Iniciais.

**Observação:**

Na tela de Aprovação, as horas extras já parametrizadas para o funcionário serão exibidas conforme parãmetro ["Extra aprovada sobrepõe as extras parametrizadas para o funcionário"](https://tdn.totvs.com/pages/viewpage.action?pageId=452719522) , e será definido pelo usuário.

**Importante**

* Caso seja necessário autorizar essas extras, o parâmetro *Parametrizar Funcionário >> Extras >> Autorização de extras* deve estar zerado (00:00).
* Caso no Parametrizador do Funcionário, na 'Etapa 9 - Extras', o campo 'Número de horas extras autorizadas' estiver configurado com valor inferior a 24:00, ao realizar a Aprovação de Extras pelo Portal RH, serão aprovadas o valor informado neste campo + o valor aprovado pelo portal.

**Exemplo:**

Número de horas extras autorizadas: 00:15

Horário Planejado: 08:00 12:00 14:00 18:00

Horário Executado: 08:00 12:00 14:00 19:00

Extra Executada: 01:00 Extra Autorizada: 00:15 (Conforme parametrização do funcionário)

Com base neste cenário, o funcionário teria 00:15 de Extra Autorizada e 00:45 de Extra Não Autorizada. Realizando a Aprovação de Extras no Portal RH no total de 00:45 o cálculo passará a ser:

**Extra Executado:** 01:00

**Extra Autorizada:** 01:00 (00:15 de Extra Autorizada pela Parametrização do Funcionário + 00:45 de Extra Aprovada pelo Portal RH)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

|  |  |
| --- | --- |
|  | Como Fazer |

---

|  |  |
| --- | --- |
|  | Recursos Adicionais |

---

|  |  |
| --- | --- |
|  | Veja Também |

---
