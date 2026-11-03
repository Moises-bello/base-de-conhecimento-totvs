---
article_id: 360028071034
category: NFe - Nota Fiscal Eletrônica
content_hash: fe6e82d774414846ba0d77c4b4301be8576bab7b305b84656d20b3e2c81d347b
fetched_at: '2026-06-28T22:40:03.698693+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Qual o conteúdo
  é levado para a TAG vUnCom e vUnTrib
type: support-article
updated_at: '2025-02-03T19:33:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028071034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Qual-o-conte%C3%BAdo-%C3%A9-levado-para-a-TAG-vUnCom-e-vUnTrib
---

**Dúvida**Qual o conteúdo é levado para a TAG vUnCom ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

No Protheus é incluído **quantidade** vezes **valor unitário** e chegando no **valor total.**

A Sefaz conforme o **Manual do Contribuinte\_v\_6.00** página 184 a TAG **vUnCom e vUnTrib**  
  
![](https://totvssuporte.zendesk.com/attachments/token/i1LyHZxDPsT6jXVWNcWcxeUA5/?name=inline968043967.png)

***Informar o valor unitário de comercialização do produto, campo meramente informativo, o contribuinte pode utilizar a precisão desejada (0-10 decimais). Para efeitos de cálculo, o valor unitário será obtido pela divisão do valor do produto pela quantidade comercial. (v2.0)***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14501763397271)​

***Informar o valor unitário de tributação do produto, campo* meramente informativo, o contribuinte pode utilizar a precisão desejada (0-10 decimais). Para efeitos de cálculo, o valor unitário será obtido pela divisão do valor do produto pela quantidade tributável (NT 2013/003).**  
  
  
Sendo assim, o cálculo é feito pelo fonte:  
  
A **divisão** que gera é do **valor do produto,** dividido pela **quantidade.**  
  
**<vProd>** divido **<qCom>** igual **<vUnCom>**  
  
**Exemplo:**  
  
**<vProd>5807.80</vProd> / <qCom>1,79222</qCom>**  
  
  
**= <vUnCom>**3240,56194577786**<UnCom>**

A **divisão** que gera é do **valor do produto,** dividido pela **quantidade.**  
  
**<vProd>** divido **<qTrib>** igual **<vUnTrib>**  
  
**Exemplo:**  
  
**<vProd>286.00</vProd> / <qTrib>130.0000</qTrib>**  
  
  
**= <vUnTrib>2.2000000000</vUnTrib>**

Se houver, ***duas unidades de medida buscamos da tabela SB5.***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar Segunda unidade de medida no XML ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044212253)

Se for levado o valor da SD2 gera as rejeições 629 e 630.   
  
**O nosso fonte hoje por padrão:**  
  
Quantidade são 4 casas decimais. **<qCom>**  
Valor unitário são 8 casas decimais. **<vUnCom>**  
Valor total são 2 casas decimais. **<vProd>**

**O nosso fonte hoje por padrão:**  
  
Quantidade são 4 casas decimais. **<qTrib>**  
Valor unitário são 8 casas decimais. **<uTrib>**  
Valor total são 2 casas decimais. **<vProd>**

* **Saiba mais:**

**Para alterar a forma atendida pela legislação hoje:**

Há opção de ajustar os campos com as **casas decimais.**

*[Clique Aqui](https://tdn.totvs.com/display/public/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)*

*[Clique Aqui](https://tdn.totvs.com/display/public/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)*

**Após alterar o ERP** para que o XML e o Danfe atenda sua necessidade há**três opções de processos** a ser seguido:  
  
1- Primeira opção pode ser customizado o **NFESEFAZ .**  
  
[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)  
  
**Rdmake disponível no link acima.**  
  
2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**  
  
  
3- Terceira opção para que seja atendido no padrão é necessário que a empresa tenha alguma **legislação na qual informe a obrigatoriedade** de gerar conforme deseja.  
  
Havendo a legislação abra um ticket no suporte e nos encaminhe que será compartilhado junto a consultoria tributária da TOTVS e posteriormente ao produto.

* ***Saiba mais:***

Caso haja um **valor unitário bruto no campo da SD2 "D2\_PRUNIT"** e outro valor no campo do preço **de lista "D2\_PRCVEN"** será levada na TAG **vUnCom** o valor bruto e gerado desconto com a diferença dos dois campos:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017119662)

**Na impressão do Danfe,** será apresento do valor unitário Bruto e no campo desconto a diferença dos dois campos da **SD2.**

* Temos um parecer da **consultoria tributária da TOTVS** referente a isso, no link abaixo:

***[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=353292106)***
