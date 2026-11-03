---
article_id: 360057227834
category: RH - Folha de Pagamento
content_hash: 62dcbf40542bc0a09bfe80fcfdd5cac616786fcfafefb959f1206863622bb602
fetched_at: '2026-06-28T22:44:13.384719+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como é calculado o valor na verba de ID 1432 -
  Valor de afastamento por acidente pago pela Previdência
type: support-article
updated_at: '2025-09-15T14:40:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057227834-RH-Linha-Protheus-GPE-Como-%C3%A9-calculado-o-valor-na-verba-de-ID-1432-Valor-de-afastamento-por-acidente-pago-pela-Previd%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26182771509783) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como é calculado o valor na verba de ID 1432 - Valor de afastamento por acidente pago pela Previdência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**A verba com o **ID 1432** apresentará o valor referente ao período de afastamento que ultrapasse os 15 primeiros dias pagos pela empresa.   
No caso, a empresa arca com o pagamento dos 15 primeiros de afastamento, o valor será calculado na verba relacionada no campo **Verba Sup** no cadastro de **Tipo de Ausências**, o que ultrapassar os 15 primeiros dias é calculado na verba de **ID 1432**-**Valor de afastamento por acidente pago pela Previdência**.  
  
Exemplo  
  
Cadastro verba ID 1432  
​![](https://totvssuporte.zendesk.com/attachments/token/wfvnlrn4JrH2DgzxHwEqixaZr/?name=inline-421536054.png)​

Ausência do funcionário

![](https://totvssuporte.zendesk.com/attachments/token/7ZVM1qbXg0BvDF0b954FRcQLZ/?name=inline1882592685.png)  
 **Salário base - 3356,00**  
Afastamento a partir do dia 10/10  
  
Memória de cálculo:  
9 dias trabalhados = 3356,00 / 30 \* 9 = 1006,80  
15 dias Aux. Acidente pago pela empresa = 3356,00/30 \* 15 = 1678,00  
6 dias Afastamento pago pela Previdência = 3356,00 / 30 \* 6 = **671,20**  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/tdhmzFPcXludIMZe9VXXoN4tP/?name=inline-1665436728.png)

**Saiba mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Separação de remuneração de funcionários afastados (Criação Ids de cálculo 1432 e 1433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029356611)
