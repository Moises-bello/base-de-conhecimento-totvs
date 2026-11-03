---
article_id: 6847223461911
category: Escrita Fiscal - Impostos - IR
content_hash: bfae9a741e86de7b758f8c166d83311beeb785722cdc1bdcbbaf300e156f1eea
fetched_at: '2026-06-28T22:39:31.908148+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como considerar dependentes
  no cálculo de IRRF Pessoa Física?
type: support-article
updated_at: '2022-06-17T14:03:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6847223461911-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-considerar-dependentes-no-c%C3%A1lculo-de-IRRF-Pessoa-F%C3%ADsica
---

**Dúvida**

Como considerar dependentes no cálculo de IRRF Pessoa Física?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Livros Fiscais - a partir da versão 12.  
  
**Solução**

Para utilizar a retenção do IRRF (pessoa física com dependentes) devemos considerar :

Cadastro de Fornecedor

Campo **A2\_NUMDEP**= Que deverá informar a quantidade de dependentes.

 Parâmetro SX6

**MV\_TMSVDEP** = Que deverá informar o valor por dependente (**Obs.: Valores fracionários devem ser gravados com ponto decimal. Ex.: 99999.99**)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6846897090711/mceclip0.png)

**MV\_RNDIRF** = Informe o critério de arredondamento do IRRF. As opções validas são: .T. arredonda, .F. trunca.   

**Calculo do Imposto de Renda - Pessoa Física**

01 - Verificar seu salário bruto total (com a inclusão de todos adicionais, se você receber).  
02 - Subtrair deste salário bruto total o valor do desconto do INSS.  
03 - Subtrair do montante restante o valor referente ao número de dependentes.

\* Em 2022, o valor a ser deduzido por cada dependente é de **R$  2.275,08**  
Para consultar valores históricos e atualizados, recomendamos o acesso direto ao site da Receita Federal.

04 - Subtrair do montante restante o valor pago a título de pensão alimentícia, quando em cumprimento de decisão judicial.  
05 - Subtrair do montante restante o valor pago em previdência privada.  
  
Mais uma vez recomendamos aqui consultar o site da Receita Federal para verificar as condições necessárias para utilizar este outro tipo de dedução.

06 - Após estas deduções (INSS, dependentes, pensão alimentícia e previdência privada), o contribuinte terá o valor-base para o cálculo do desconto mensal do IR.

07 - Existem outras deduções que podem ser abatidas, apesar de não serem tão comuns:  
- Funpresp.  
- FAPI e parcela isenta de aposentadoria.  
- Reserva remunerada, reforma e pensão para declarantes acima de 65 anos.  
Se você se enquadrar em uma dessas deduções, também poderá utilizá-las para encontrar o seu valor-base.

08 - Consultar a tabela do IR mensal para verificar em qual faixa se enquadra o seu valor-base e qual a alíquota a ser paga.

Repare que, assim como o INSS, a alíquota do IR é progressiva, ou seja, quanto maior o seu salário, maior será o desconto do imposto de renda.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6846995682071/mceclip1.png)

Obs.: O valores desta tabela IR se referem ao exercício de 2022. Para atualizações ou consulta de valores históricos dos anos anteriores, recomendamos o acesso direto ao site da Receita Federal.

09 - Aplicar a alíquota do IR sobre o valor-base.  
10 - Subtrair a parcela a deduzir do valor encontrado no item 09.

| Exemplo | |
| --- | --- |
| a - Valor Bruto | R$ 10.000,00 |
| b - Deduções: 02 Dependentes a R$ 2.275,08 cada | R$ 4.550,16 |
| **c - SubTotal (a - b)** | **R$ 5.449,84** |
| d - Aplicar alíquota tabela progressiva, neste caso 27,5% | R$ 1.498,70 |
| e - Aplicar dedução conforme tabela progressiva | R$ 869,36 |
| **f - SubTotal Imposto Apurado (d - e)** | **R$ 629,35** |
|  |  |
| **Valor líquido após deduções e IR (a - f)** | **R$ 9.370,65** |

Exemplo considerando **A2\_NUMDEP=2**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6847144517783/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6847176394391/mceclip3.png)

**Assuntos relacionados:**

[MP - FIS - Como fazer o Cálculo de IRRF - Tabela Progressiva](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062163014-MP-FIS-Como-fazer-o-C%C3%A1lculo-de-IRRF-Tabela-Progressiva-?source=search)

[MP - FIS - Como efetuar a retenção do IRRF no Contas a Pagar do Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003545201-MP-FIS-Como-efetuar-a-reten%C3%A7%C3%A3o-do-IRRF-no-Contas-a-Pagar-do-Protheus-?source=search)

Simulador IRPF

<https://www27.receita.fazenda.gov.br/simulador-irpf/>
