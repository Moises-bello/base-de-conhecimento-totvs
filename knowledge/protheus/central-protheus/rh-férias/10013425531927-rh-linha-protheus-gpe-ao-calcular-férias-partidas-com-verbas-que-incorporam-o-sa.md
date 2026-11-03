---
article_id: 10013425531927
category: RH - Férias
content_hash: eca00ccf4388c171962718cd33ae7f67bd6771365a6e53c263f614996e12f15f
fetched_at: '2026-06-28T22:43:57.938998+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Ao calcular Férias partidas com verbas que incorporam
  o Salário o valor de Adicional Tempo de Serviço e 1/3 não são gerados corretamente
type: support-article
updated_at: '2025-09-02T17:05:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10013425531927-RH-Linha-Protheus-GPE-Ao-calcular-F%C3%A9rias-partidas-com-verbas-que-incorporam-o-Sal%C3%A1rio-o-valor-de-Adicional-Tempo-de-Servi%C3%A7o-e-1-3-n%C3%A3o-s%C3%A3o-gerados-corretamente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31453088793239)** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Por que ao calcular **Férias partidas com verbas que incorporam o Salário**, o valor de **ATS e 1/3 não são gerados corretamente?**

**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.33

**Solução**Para que o sistema entenda que as verbas fazem parte do cálculo de ATS, é necessário que o campo **Incorp. Salário** esteja configurado com **Sim**, para as verbas que incorporam o salário no cálculo de férias.

O exemplo abaixo é da verba de **Férias Adicional** **de Montagem** Mês Seguinte:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10007697516695)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10007699381655)

No cálculo do valor de ATS em férias partidas, o sistema depende da configuração do parâmetro **MV\_DIASPER** antes do cadastro do período.

**Parâmetro com 1**- Divisor será a quantidade de dias do mês: O sistema irá considerar para a regra de calculo a divisão sobre os dias do mês. Será validado no cadastro de períodos a quantidade de dias do período que consta no campo **Dias Cálculo/Dias Mês.**

**Parâmetro com 2-** Divisor será sempre 30: O divisor para calculo será considerado sempre 30 dias, independente da quantidade de dias do mês.

**Exemplo:**

No cálculo de férias partidas entre Novembro (30 dias) e Dezembro (31 dias), um funcionário que terá 30 dias de gozo de férias (07/11/2022 até 06/12/2022) e o valor de ATS é R$120,96.

Cálculo com o **MV\_DIASPER =1**

**Novembro:** R$120,96/30 = 4,03\*24 = R$96,77

**Dezembro:** R$120,96/31 = 3,90\*6 = R$23,41

Cálculo com o **MV\_DIASPER =2**

**Novembro:** R$120,96/30 = 4,03\*24 = R$96,77

**Dezembro:** R$120,96/30 = 4,03\*6 = R$24,19

Para o cálculo de férias onde o funcionário é mensalista e tem Adicionais, ATS e valor de Salário, o sistema soma o total desses valores, e divide por 3, para gerar o valor total de 1/3 das férias.

Após esse cálculo, o sistema divide o valor total de 1/3 de férias dependendo da configuração do parâmetro **MV\_DIASPER** , divide por 30 dias e multiplica pela quantidade de dias no cálculo de férias e férias mês seguinte.

**Exemplo:**

Conforme a imagem abaixo foi realizado o cálculo de férias de um funcionário com 30 dias de gozados (07/11/2022 à 06/12/2022), o sistema **soma** todos os valores de provento referente ao funcionário (ATS, Férias pagas no mês, média hora extra mês, média valores mês, Adicional de montagem, Férias pagas mês seguinte, média hora extra mês seguinte e média valores mês seguinte), que terá como valor total R$3.132,60.

Deste valor total será gerado o valor de 1/3 das férias: R$3.132,60/3 = R$1.044,20.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10012903453463)

Após o cálculo do valor de 1/3 das férias, o sistema verifica a quantidade de dias do mês, e a configuração do parâmetro **MV\_DIASPER** referente ao período do cálculo gerado, e dependendo da configuração realiza a divisão do valor de 1/3 para os dias do mês de férias.

Nesse exemplo o parâmetro **MV\_DIASPER** está configurado **"2",** porém como o cálculo foi realizado no mês de Novembro será dividido por 30 dias.

**1/3 Férias Novembro**

R$1.044,20/30 \*24 = R$835,36

**1/3 Férias Dezembro**

R$1.044,20/30 \*6 = R$208,84

**Para Saber Mais:**

[RH - Linha Protheus - GPE - Como calcular férias na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015658231-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-na-vers%C3%A3o-12?source=search)  
[RH - Linha Protheus - GPE - Como excluir o calculo das férias conforme origem de cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051158134-RH-Linha-Protheus-GPE-Como-excluir-o-calculo-das-f%C3%A9rias-conforme-origem-de-c%C3%A1lculo?source=search)  
[RH - Linha Protheus - GPE - Salário nas provisões soma o valor de ATS nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034822654-RH-Linha-Protheus-GPE-Sal%C3%A1rio-nas-provis%C3%B5es-soma-o-valor-de-ATS-nas-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Como conferir 1/3 de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024833993-RH-Linha-Protheus-GPE-Como-conferir-1-3-de-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Valor de 1/3 de abono de férias não está correto o que verificar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024602612-RH-Linha-Protheus-GPE-Valor-de-1-3-de-abono-de-f%C3%A9rias-n%C3%A3o-est%C3%A1-correto-o-que-verificar)  
[RH - Linha Protheus - GPE - Férias Proporcionais dividindo por 31 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003366622-RH-Linha-Protheus-GPE-F%C3%A9rias-Proporcionais-dividindo-por-31-dias-?source=search)
