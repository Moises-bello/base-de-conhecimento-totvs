---
article_id: 1500002287981
category: Escrita Fiscal - Impostos - Cálculos
content_hash: cb33cc7d37076a162c3dc64733e9b9f81757a7ffb42a2e8163df268dc8ede968
fetched_at: '2026-06-28T22:39:31.166916+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: MP - FIS - Como incluir / Emitir Nota Fiscal de Importação pelo Documento de
  Entrada - MATA103?
type: support-article
updated_at: '2024-10-02T20:30:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002287981-MP-FIS-Como-incluir-Emitir-Nota-Fiscal-de-Importa%C3%A7%C3%A3o-pelo-Documento-de-Entrada-MATA103
---

**Dúvida**Como incluir / Emitir Nota Fiscal de Importação pelo MATA103?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Está disponível nas rotinas **Nota Fiscal Manual de Entrada (MATA910)** e **Documento de Entrada (MATA103)**, um tratamento para inclusão de notas fiscais de importação para clientes que não utilizam o módulo SIGAEIC.

Para o tratamento correto do sistema é necessário observar a configuração:

**Cadastro de Fornecedor**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012509012/mceclip5.png)

**Cadastro de TES - Tipo de Entrada ou Saída**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012508652/mceclip4.png)**

**Despesas Acessórias**

Em relação ao valor das despesas (Siscomex, Frete, Despesas, Seguro e AFRMM - Adicional ao Frete para Renovação da Marinha Mercante) compor ou não a base de cálculo dos impostos, observar a configuração:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012518731/mceclip9.png)

**PIS Majorado e COFINS Majorado**

Para o cálculo do Pis Majorado e Cofins Majorado, informar o percentual de acréscimo a ser aplicado na alíquota, nos campos correspondentes, localizados na aba “Outros” da TES:

Ao lançar a nota fiscal, observar a descrição dos impostos calculados. Se a configuração foi efetuada conforme indicação, os impostos serão demonstrados da seguinte maneira:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012509152/mceclip8.png)

**Importante:**Caso a nota tenha sido lançada incorretamente é necessário realizar a **exclusão**e incluir novamente após o ajuste das configurações. A rotina de reprocessamento (MATA930) **não refaz os cálculos dos tributos**.

**O parâmetro abaixo deverá ser criado manualmente:**

MV\_EIC0064

Tipo: Lógico

Descrição: Permite a subtração do valor do II (D1\_II) do valor total do item (D1\_TOTAL). Habilitado (.T.), Desabilitado (.F.)

Valor: .T. ou .F. conforme necessidade da empresa.

Atenção: Com este parâmetro habilitado, significa que o valor informado no item da NF de importação não estará com o Valor de II. Com o parâmetro desabilitado, significa que o valor informado no item da NF de importação estará com o Valor de II. Cabe ao usuário informar ou não o Valor dos Produtos com o Valor de II, lembrando sempre considerando a definição do parâmetro citado.

*Este parâmetro deve ser criado manualmente.*

**Procedimento para lançamento da nota de importação:**

**1º** Acesse a rotina MATA103 e preencha o cabeçalho da nota;

**2º** Some o valor Aduaneiro e o Imposto de Importação e informe o resultado nos campos: Valor do item (D1\_VUNIT) e Valor total (D1\_TOTAL);

**3º** Insira a TES com a configuração específica;

**4º** Informe a alíquota do Imposto de Importação e o valor do Imposto de Importação nos campos Aliq Import (D1\_ALIQII) e  Vlr. I.I. (D1\_II);

**5º** Informe as despesas acessórias, na aba “Descontos/Frete/Despesas”.

Exemplo Prático:

**Declaração de Importação - DI**

Valor da mercadoria = 2.000,00  
Valor do II = 300,00  
Base de cálculo do IPI = 2300,00 \*10% = 230,00  
Base do pis / cofins = 2000,00  
Pis = 2,10 % = 42,00

Cofins  = 9,65% = 193,00  
taxa Siscomex = 215,00

**Parametro MV\_EIC0064= .F.**  
**![(estrela vermelha)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/star_red.png) É necessário somar o valor aduaneiro e o valor do imposto de importação (R$ 2000,00 + R$300,00 = R$2.300,00).**

TES configurada de acordo com o exemplo  
  
Base de cálculo do icms = 2000,00+300,00+230,00+42,00+193,00+215,00 = 2980,00  
2980,00/0,82 = 3634,15 ( 0,82 icms fictício , cálculo por dentro )  
3634,15\* 18% = 654,15

**Preencha os campos Aliq Import (D1\_ALIQII) e  Vlr. I.I. (D1\_II) com os valores****correspondentes:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6066488928151/mceclip0.png)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6067344028311/mceclip3.png)**

**Informe as despesas acessórias:**

no exemplo = 215,00

**Conferir os valores:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6067313838615/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6067329622551/mceclip2.png)

#### Valores de forma correta.
