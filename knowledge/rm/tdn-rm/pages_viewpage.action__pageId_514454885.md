---
content_hash: 86d6a809829bfc25807d268682566f901dda0efaf9b38f407936809b4ddcd43a
fetched_at: '2026-06-29T00:10:26.719928+00:00'
page_id: '514454885'
product: rm
source: tdn-rm
title: Qual o funcionamento do evento com o código de cálculo 181 e o código de cálculo
  72?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514454885
version: 5
---

# Objetivo:

---

O objetivo deste documento é informar o funcionamento dos códigos de cálculo 181 e 72.

---

**Código de cálculo 72 - Base INSS Outro Emprego**

Este evento deverá ser lançado manualmente (no envelope, via grupo de eventos, via código fixo etc.) para funcionários que tenham mais de um emprego. Informando o CC72, o CC29 correspondente ao valor descontado no outro emprego, também deverá ser lançado para o funcionário e será recalculado conforme a alíquota do total da base de INSS.

**Exemplos**

1) (Base abaixo do Teto)  
Base de Cálculo INSS na Outra Empresa (CC72): 1000,00  
INSS Descontado na Outra Empresa (CC29): 80,00 (8%) - **Após o recalculo o valor passará a ser 90,00 (9%)**  
Base de Cálculo INSS na Empresa Atual: 1500,00  
Base Total do INSS na Competência: 2500,00  
Alíquota devida do Mês de Competência: 9%  
Valor devido para desconto do INSS na Competência: 225,00  
Valor INSS desconta na Empresa Atual (CC03): 135,00 (225,00 – 90,00)

Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC72 com o valor da base de cálculo da outra empresa (1000,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência, realizará o cálculo do valor correto do desconto e deduzirá o valor informado no evento de CC29 (90,00) para o desconto do INSS na empresa (CC03).  
  
2) (Base acima do Teto)  
Base de Cálculo INSS na Outra Empresa (CC72): 4000,00  
INSS Descontado na Outra Empresa (CC29): 440,00 (11%)  
Base de Cálculo INSS na Empresa Atual: 2000,00  
Base Total do INSS na Competência: 6000,00 (ultrapassou limite para desconto do teto)  
Valor devido para desconto do INSS na Competência: 642,34  
Valor INSS desconta na Empresa Atual (CC03): 202,34 (642,34 – 440,00)

Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC72 com o valor da base de cálculo da outra empresa (4000,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência e deduzirá o valor informado no evento de CC29 (440,00) para o desconto do INSS na empresa (CC03). Como a alíquota na outra empresa já atingiu a última faixa, mesmo efetuando o recálculo o valor do CC29 não é alterado.

**Código de cálculo 181 - Base INSS Outro Emprego Desconto Complementar**

Informar neste evento a base de cálculo utilizada na outra empresa para o cálculo do desconto do INSS. Este evento deve ser lançado quando houver necessidade de desconto do total descontado no outro emprego e não calculado o valor proporcionalizado, portanto na movimentação deve existir apenas os eventos com CC 181 – Base INSS Outro Emprego Desconto Complementar e CC29 - INSS Outro Emprego.   
   
**Exemplos**  
  
1) (Base abaixo do Teto)  
Base de Cálculo INSS na Outra Empresa (CC72): 1000,00  
INSS Descontado na Outra Empresa (CC29): 80,00 (8%)   
Base de Cálculo INSS na Empresa Atual: 1500,00  
Base Total do INSS na Competência: 2500,00  
Alíquota devida do Mês de Competência: 9%  
Valor devido para desconto do INSS na Competência: 225,00  
Valor INSS desconta na Empresa Atual (CC03): 145,00 (225,00 – 80,00)

Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC181 com o valor da base de cálculo da outra empresa (1000,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência e deduzirá o valor informado no evento de CC29 (80,00) para o desconto do INSS na empresa (CC03) sem recalcular o CC29.  
  
2) (Base acima do Teto)  
Base de Cálculo INSS na Outra Empresa (CC72): 4000,00  
INSS Descontado na Outra Empresa (CC29): 440,00 (11%)  
Base de Cálculo INSS na Empresa Atual: 2000,00  
Base Total do INSS na Competência: 6000,00 (ultrapassou limite para desconto do teto)  
Valor devido para desconto do INSS na Competência: 642,34  
Valor INSS desconta na Empresa Atual (CC03): 202,34 (642,34 – 440,00)

Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC181 com o valor da base de cálculo da outra empresa (4000,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência e deduzirá o valor informado no evento de CC29 (440,00) para o desconto do INSS na empresa (CC03) sem recalcular o CC29.
