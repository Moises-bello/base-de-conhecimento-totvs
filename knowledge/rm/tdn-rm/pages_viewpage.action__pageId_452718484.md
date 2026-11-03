---
content_hash: a4a899b0155e540d8722ecf5ecde72222b7f3d3e2ef709bc59f9fd2ff848d4ea
fetched_at: '2026-06-29T00:10:00.319566+00:00'
page_id: '452718484'
product: rm
source: tdn-rm
title: Código de Cálculo 71 - 13º Salário Indenizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718484
version: 2
---

Provento do tipo valor, incide no liquido. Este evento somente será utilizado na rescisão.

O cálculo será da seguinte forma:

13º. SALÁRIO / NÚMERO. DE AVOS

Este código de cálculo será utilizado em caso de aviso prévio indenizado. Consulte a tabela de incidências para verificar se deve ser calculado INSS, IRRF e FGTS sobre este valor. Marque, conforme tabela atual, as incidências em IRRF 13º Salário e FGTS.

**Atenção**

Para o perfeito funcionamento do cálculo de 13º rescisão, o usuário deverá deixar os eventos de código de cálculo 48 e 71 sem fórmula, para que o RM Labore calcule o 13º salario e proporcionalize este valor entre o 13º salário rescisão(CC48) e o 13º salário indenizado (CC71). Se for incluída uma fórmula em algum destes eventos o outro evento deverá obrigatoriamente ter fórmula para que o sistema faça os cálculos.  
 Particularidades do cálculo por fórmula

No cálculo de 13º salário indenizado a variável C,valor de evento no movimento atual, não poderá ser usada, porque o envelope não é calculado antes deste evento e portanto não existe o evento com CC48 para ser utilizado em fórmula.

**Exemplo**

CC48 - fórmula = ( (RC + 100.00) / 12 ) \* NROAVOS13

CC71 - fórmula = C('0048') / NROAVOS13 = ERRADO

CC71 - fórmula = ( (RC + 100.00) / 12 ) \* NROAVOS13/NROAVOS13 = CORRETO

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
