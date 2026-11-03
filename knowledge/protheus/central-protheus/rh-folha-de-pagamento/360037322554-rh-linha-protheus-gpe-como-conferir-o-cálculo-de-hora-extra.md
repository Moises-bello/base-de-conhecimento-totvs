---
article_id: 360037322554
category: RH - Folha de Pagamento
content_hash: 12eb2c25c04c35827a45e535484ee1c259d1897abd8ad5876b72e2acad39e75b
fetched_at: '2026-06-28T22:44:13.256047+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o cálculo de hora extra
type: support-article
updated_at: '2025-08-11T21:56:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037322554-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-de-hora-extra
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26327939866391) Tempo ap****roximado para leitura: 00:03:00 min**

**Dúvida**Ao calcular folha de pagamento, como deve ser conferido o cálculo das horas extras e adicional noturno?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O sistema considera para compor a carga horária mensal, para o cálculo de horas extras e adicional noturno o cadastro de períodos e a carga horária diária, desta forma o sistema monta a carga horária mensal e assim calcula os valores de horas extras e adicional noturno.  
  
Abaixo como deve ser feita a conferência, usaremos como exemplo o período 08/2019:  
**Exemplo 1 - Cálculo apenas sobre salário base:**  
**1.** Verificar no cadastro do período em aberto a quantidade de dias considerados para cálculo na aba Cadastro Calendário:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049807593)  
  
**2.** Verificar no cadastro do funcionário em questão o campo Hora Dia:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048909534)  
  
**3.** O sistema fará o seguinte cálculo para chegar na carga horária mensal: horas do campo Hora Dia X Dias preenchido no campo Dias Cálculo, que conforme *prints* acima será 7,3333 X 30 = 220 horas.  
Chegando na carga horária mensal, sistema fará o cálculo abaixo para calcular as horas extras e/ou adicional noturno:  
Salário Base = 1550,00  
Carga horária mensal = 220  
Salário hora = Salário Base / Carga horária mensal = 7,0454  
  
**4.** Ao chegar no salário hora, sistema fará o cálculo da verba de acordo com as horas lançadas e percentual da mesma, no exemplo abaixo temos uma verba de HE 100% lançada com 7 horas, o cálculo será da seguinte forma:  
Salário Hora \* horas lançadas = 7,0454 \* 7 = 49,3178  
49,3178 \* 100% = 49,3178  
HE final = 98,64 (pois foi arredondada a segunda casa decimal)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048922374)  
  
**Exemplo 2 - Cálculo com cadastro de períodos considerando 31 dias de cálculo:**  
**1.** A fórmula de cálculo para chegar no salário hora é a mesma, mas neste caso será sobre 31 dias conforme parametrizado no cadastro de Períodos:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049820833)  
  
Carga horária mensal = Campo Horas Dias X Dias preenchido no campo Dias Cálculo = 227,33  
Salário Base = 1550,00  
Carga horária mensal = 227,33  
Salário hora = Salário Base / Carga horária mensal = 6,8182   
  
**2.** Ao chegar no salário hora, sistema fará o cálculo da verba de acordo com as horas lançadas e percentual da mesma, no exemplo abaixo temos uma verba de HE 100% lançada com 7 horas, o cálculo será da seguinte forma:  
Salário Hora \* horas lançadas = 6,8182 \* 7 = 47,7274  
47,7274 \* 100% = 47,7274  
HE final = 95,45  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048924214)

**OBS.:** Caso o funcionário trabalhe apenas parte do mês por conta de férias ou demais ausências, o cálculo será o mesmo, pois sempre é considerada a carga horária mensal completa, independente da quantidade de dias que o funcionário trabalhou.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
