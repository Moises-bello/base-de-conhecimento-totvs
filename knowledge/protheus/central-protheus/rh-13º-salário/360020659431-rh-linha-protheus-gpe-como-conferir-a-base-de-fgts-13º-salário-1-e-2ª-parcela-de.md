---
article_id: 360020659431
category: RH - 13º salário
content_hash: bce740c118b7c1552e3cb6178217b2963e7c780149ffc5661a8ada6fd59cc51c
fetched_at: '2026-06-28T22:44:00.567476+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir a Base de FGTS 13º Salário 1° e 2ª
  Parcela de funcionários Afastados por Acidente de Trabalho
type: support-article
updated_at: '2026-01-20T14:05:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020659431-RH-Linha-Protheus-GPE-Como-Conferir-a-Base-de-FGTS-13%C2%BA-Sal%C3%A1rio-1-e-2%C2%AA-Parcela-de-funcion%C3%A1rios-Afastados-por-Acidente-de-Trabalho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18941819814679) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**  
Como conferir a Base de FGTS 13º Salário 2ª Parcela para funcionários Afastados por Acidente de Trabalho?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para o período que o funcionário está afastado por acidente de trabalho, mesmo que ele não tenha direito ao avo do mês, deve ser calculado o FGTS sobre o período de afastamento.

Para que o FGTS seja calculado corretamente, verifique os cadastros abaixo:

**1.** No cadastro do **Tipo de Ausência**, o campo **Depos. FGTS** deve estar selecionado com a opção de cálculo integrale o campo **Cod.Au.SEFIP** selecionado com o código referente a acidente de trabalho.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35014606856855)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37800104836631)

2. No cadastro de Verbas, para o cálculo ser enviado corretamente para o eSocial, deve existir uma verba relacionada ao **ID 1730**, nessa verba será calculado o valor de 13º referente ao período de afastamento que será considerado para o FGTS. Acesse [esta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057407274-RH-Linha-Protheus-GPE-Id-1730-Base-FGTS-13%C2%BA-para-funcion%C3%A1rio-afastado-por-acidente-de-trabalho) para verificar o cadastro da verba de ID 1730.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37800089522967)

**Exemplo de Cálculo:**  
-Funcionário afastado por acidente de trabalho a partir de 01/10/2025.  
-Possui direito a 10 avos de 13º salário, pois os primeiros 15 dias são pagos pela empresa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35014606860439)

**Cálculo da 1ª Parcela**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35014639002007)

1ª Parcela 13º: Salário / 12 x Avos de Direito x 50%  
3.125,00 /12 x 10 x 50% = **1.302,08 (verba 107 - id 0022)**

13º Acidente pago pela previdência: Salário / 12 x Meses de afastamento x 50%  
3.125,00 /12 x 2 x 50% = **260,42 (verba 348 - id 1730)**

Base FGTS: 1ª parcela (verba 107 - id 0022) + FGTS pago pela previdência (verba 348 - id 1730)  
**1.302,08 + 260,42 = 1.562,50 (verba 722 - id 0108)**

**Cálculo da 2º Parcela**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35014639002903)**  
  
2ª Parcela 13º: Salário / 12 x Avos de Direito   
3.125,00 /12 x 10 = **2.604,17 (verba 108 - id 0024)**

13º Acidente pago pela previdência: Salário / 12 x Meses de afastamento - Acidente pago pela previdência da 1ª parcela (id 1730)  
3.125,00 /12 x 2 - 260,42 = **260,42 (verba 348 - id 1730)**

Base FGTS: 2ª parcela (verba 108 - id 0024) + FGTS pago pela previdência (verba 348 - id 1730) - Adiantamento da 1ª parcela (verba 439 - id 0183)  
2.604,17 + 260,42 - 1302,08 = **1.562,51 (verba 722 - id 0108)**

**Saiba Mais**  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409855157399-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionadas-ao-c%C3%A1lculo-da-1%C2%AA-parcela-do-13-Sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409828940055-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionados-ao-c%C3%A1lculo-da-2%C2%AA-parcela-do-13%C2%BA-Sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410720423959-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionadas-ao-c%C3%A1lculo-do-complemento-de-13%C2%BA)
