---
article_id: 360026060394
category: RH - Folha de Pagamento
content_hash: 2ddb8fd8e73de4544d00078fad577b25afb498259f78c2caaa0fb7442030895e
fetched_at: '2026-06-28T22:44:11.924888+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  Prorrogação da Licença Maternidade - Programa Empresa
  Cidadã
type: support-article
updated_at: '2025-07-25T11:55:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026060394-RH-Linha-Protheus-GPE-Prorroga%C3%A7%C3%A3o-da-Licen%C3%A7a-Maternidade-Programa-Empresa-Cidad%C3%A3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23979648696471) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como executar o Lançamento e o Pagamento da prorrogação da Licença Maternidade.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O programa **Empresa Cidadã**, instituído pela Lei 11.770/2008 (antiga 8.212/91), é destinado a prorrogar por 60 (sessenta) dias a duração da licença-maternidade prevista no inciso XVlll do caput art. 7º da Constituição Federal.

Durante o período de prorrogação da licença-maternidade, a empregada terá direito à sua remuneração integral, nos mesmos moldes devidos no período de percepção do salário-maternidade pago pelo regime geral de previdência social.

O pagamento do salário-maternidade para a empregada do empregador que optar pela prorrogação do prazo será da seguinte forma:

· Os 120 (cento e vinte) primeiros dias continuarão sendo pagos pelo Instituto Nacional do Seguro Social (INSS);  
· Os 60 (sessenta) dias restantes serão pagos pelo empregador.

**Importante:**  
Recomendamos a leitura integral das referencias legais mencionadas para maiores detalhes.  
Para atender as necessidades exigidas com a legislação, deve ser feitas os seguintes passos:  
  
Gestão de Pessoal:  
**1)** Acesse **Atualizações > Cadastros > Verbas (GPEA040).**

* Inclua uma verba de provento para conter o resultado do cálculo referente à prorrogação do auxílio maternidade.

**0927 – Prorrogação Auxílio Maternidade**  
Na pasta **Incidências**, o campo **Ded. G. INSS** (RV\_DEDINSS) deve ser configurado como **Não**.  
![](http://tdn.totvs.com/download/attachments/269429641/image2016-12-3%2017%3A40%3A25.png?version=1&modificationDate=1480796830000&api=v2)  
![](http://tdn.totvs.com/download/attachments/269429641/image2016-12-3%2017%3A43%3A46.png?version=1&modificationDate=1480796831000&api=v2)

* Inclua uma verba de provento para conter as médias do cálculo referente à prorrogação do auxílio maternidade.

**0928 – Pagto. de Médias Prorrogação do Aux. Maternidade**  
Na pasta **Incidências**, o campo **Ded. G. INSS** (RV\_DEDINSS) deve ser configurado como **Não**.  
  
![](http://tdn.totvs.com/download/attachments/269429641/image2016-12-3%2017%3A41%3A44.png?version=1&modificationDate=1480796831000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/269429641/image2016-12-3%2017%3A43%3A52.png?version=1&modificationDate=1480796831000&api=v2)  
  
**2)** **Atualizações > Definições de Cálculo > Tipos de Ausências (GPEA430)**, relacionar a verba de 651 - Prorrogação Auxílio Maternidade (ID 0927):  
![](http://tdn.totvs.com/download/attachments/269429641/image2016-12-3%2018%3A21%3A51.png?version=1&modificationDate=1480796831000&api=v2)  
![](http://tdn.totvs.com/download/attachments/269429641/image2016-12-3%2017%3A48%3A48.png?version=1&modificationDate=1480796831000&api=v2)

**3)** Acesse **Atualizações >Lançamentos > Ausências (GPEA240)**

O sistema já terá um afastamento de licença maternidade com uma duração de 120 dias. Deverá ser criada a prorrogação informando os seguintes itens:

Tipo de afastamento será igual ao afastamento anterior

Data do afastamento iniciará no dia seguinte a data fim do anterior

Segue exemplo:  
![](http://tdn.totvs.com/download/attachments/269429641/image2016-12-3%2018%3A23%3A26.png?version=1&modificationDate=1480796831000&api=v2)  
**4)** Cálculo correto da Prorrogação da Licença Maternidade e da base de INSS:  
![](http://tdn.totvs.com/download/attachments/269429641/image2016-12-3%2018%3A24%3A59.png?version=1&modificationDate=1480796831000&api=v2)

**Saber Mais:**

[RH - Linha Protheus - GPE - Sequência de afastamento Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050439054-RH-Linha-Protheus-GPE-Sequ%C3%AAncia-de-afastamento-Licen%C3%A7a-Maternidade?source=search)

[RH - Linha Protheus - GPE - Como lançar ausência por Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053399713-RH-Linha-Protheus-GPE-Como-lan%C3%A7ar-aus%C3%AAncia-por-Licen%C3%A7a-Maternidade-?source=search)

[RH - Linha Protheus - GPE - Como configurar Licença Maternidade por Adoção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051079813-RH-Linha-Protheus-GPE-Como-configurar-Licen%C3%A7a-Maternidade-por-Ado%C3%A7%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Licença Maternidade quando há óbito da Mãe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052191733-RH-Linha-Protheus-GPE-Licen%C3%A7a-Maternidade-quando-h%C3%A1-%C3%B3bito-da-M%C3%A3e?source=search)
