---
content_hash: b00a608e1ebdef9c1d057ecc75d7dbcbc149a93ed76c1311de472793eec2e436
fetched_at: '2026-06-29T00:10:03.078113+00:00'
page_id: '452718996'
product: rm
source: tdn-rm
title: Gráfico de Absenteísmo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718996
version: 81
---

Por este gráfico, o usuário poderá verificar facilmente a relação entre a quantidade de horas negativas (abonos, atrasos e/ou faltas) e o número de horas previsto de trabalho.  
O usuário poderá gerar considerando as opções Considera Atrasos, Considera Faltas e Considera abonos de faltas/atrasos.  
**Observação**  
Para visualizar o gráfico de Absenteísmo, o parâmetro Considera Atrasos e/ou Considera Faltas deve estar habilitado.

Por seção:  
Na geração do relatório do gráfico de absenteísmo por seção, somamos todas as horas negativas (atrasos, faltas e abonos) dos funcionários daquela seção e dividimos pela soma total das horas previstas de trabalho de todos da mesma seção. Isso gera uma média ponderada, ou seja, considerando o peso (as horas previstas) de cada funcionário.  
Em outras palavras: tratamos a seção como um único índividuo, somando todas as horas negativas e tudo o que ela deveria trabalhar.

Exemplo prático:

Na mesma seção:  
• Mário: 2h de atraso e 4h previstas.  
• Carla: 2h de atraso e 8h previstas.

Mas a real média ponderada é:  
• Total horas negativas: 4h (2h + 2h)  
• Total horas previstas: 12h (4h + 8h)  
Média ponderada: (4 / 12) × 100 = 33,33%

A média ponderada é mais precisa, pois leva em conta o total de horas previstas de trabalho, demonstrando o cenário real mesmo quando os funcionários têm cargas horárias diferentes.

|  |  |
| --- | --- |
|  | Como Fazer |

---

[Como Fazer - Gráfico de Absenteísmo](http://tdn.totvs.com/x/8wUWBw)
