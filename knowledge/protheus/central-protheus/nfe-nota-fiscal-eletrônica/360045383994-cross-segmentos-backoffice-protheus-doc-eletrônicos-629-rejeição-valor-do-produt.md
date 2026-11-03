---
article_id: 360045383994
category: NFe - Nota Fiscal Eletrônica
content_hash: 5a0ecc9350b848c297dc5a79a0841ed501955d492ed9b988c17038b857d76839
fetched_at: '2026-06-28T22:40:03.257670+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  629 Rejeição :
  Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade
  Comercial'
type: support-article
updated_at: '2025-06-17T12:24:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045383994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-629-Rejei%C3%A7%C3%A3o-Valor-do-Produto-difere-do-produto-Valor-Unit%C3%A1rio-de-Comercializa%C3%A7%C3%A3o-e-Quantidade-Comercial
---

**Dúvida**Como solucionar a  629 Rejeição : Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Quando é feito nota do tipo normal a Sefaz valida se a  *vProd*  **é o resutado da** *vUnCom*  **vezes**  *qCom*.

A TAG **vUnCom o valor é gerado pelo fonte**conforme detalhado abaixo:

No Protheus é incluído **quantidade** vezes **valor unitário** e chegando no **valor total.**

* A Sefaz conforme o **Manual do Contribuinte\_v\_6.00** página 184 a TAG **vUnCom**  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/i1LyHZxDPsT6jXVWNcWcxeUA5/?name=inline968043967.png)​  
    
  **Informar o valor unitário de comercialização do produto, campo meramente informativo, o contribuinte pode utilizar a precisão desejada (0-10 decimais). Para efeitos de cálculo, o valor unitário será obtido pela divisão do valor do produto pela quantidade comercial. (v2.0)**  
    
  Sendo assim, o ***cálculo é feito*** pelo fonte:  
    
  A **divisão** que gera é do **valor do produto** dividido pela **quantidade.**  
    
  **<vProd>** divido **<qCom>**igual **<vUnCom>**  
    
  **Exemplo:**  
    
  **<vProd>5807.80</vProd> / <qCom>1,79222</qCom>**  
    
    
  **= <vUnCom>**3240,56194577786**<UnCom>**  
    
    
    
  **O nosso fonte hoje por padrão:**  
    
  Quantidade são 4 casas decimais. **<qCom>**  
  Valor unitário são 8 casas decimais.**<vUnCom>**  
  Valor total são 2 casas decimais. **<vProd>**

1- Verifique ***se nota de saída*** se o cálculo na tabela SD2 está correto:

D2\_PRCVEN \*  D2\_QUANT  = D2\_TOTAL

2- Verifique ***se nota de entrada*** se o cálculo na tabela SD1 está correto:

D1\_VUNIT \* D1\_QUANT = D1\_TOTAL

3 - Se sim, o fonte fará o calculo nesse caso será necessário realizar ***um teste com os fontes padrões do link***  abaixo aplicar a ***patch e compilar o RDMAKE da NFe:***

[MP - NFE - Documentos Eletrônicos NFe / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

4 - Caso a empresa tenha alterado as ***casas decimais do valor unitário na SD1 ou na SD2*** será necessário customizar o NFESEFAZ para facilitar **segue o trecho** do fonte onde deve ser alterado:

cString += '<vUnCom>'+ConvType(aProd[16],21,8)+'</vUnCom>'   
Else   
cString += '<vUnCom>'+ConvType(aProd[16],16,4)+'</vUnCom>'   
Endif

cString += '<vUnTrib>'+ConvType(aProd[10]/aProd[12],21,8)+'</vUnTrib>'   
Else  
cString += '<vUnTrib>'+ConvType(aProd[10]/aProd[12],16,4)+'</vUnTrib>'   
Endif

5 - Após isso, exclua a nota e gere novamente.

6 - Caso seja ***nota de Complemento*** realizar o procedimento do link abaixo:

[MP - NFE - Rejeição 629 Para NFe Complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036585153)

* **Saiba mais:**

**Para alterar a forma atendida pela legislação hoje:**

Há opção de ajustar os campos com as **casas decimais.**

[https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427308-MP-FAT-Casas-decimais-no-Faturamento](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427308-MP-FAT-Casas-decimais-no-Faturamento&sa=D&source=hangouts&ust=1588340897285000&usg=AFQjCNGiVrfbmYelMPQiZxtV0-Z2LikuWQ)

[https://tdn.totvs.com/display/public/PROT/FAT0068\_Aumento\_de\_Casas\_Decimais\_no\_ambiente\_Faturamento\_SIGAFAT](https://www.google.com/url?q=https://tdn.totvs.com/display/public/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT&sa=D&source=hangouts&ust=1588340897285000&usg=AFQjCNG8kgkrTDy50ajlpT2vk6QJbn8ckw)

**Após alterar o ERP** para que o XML e o Danfe atenda sua necessidade há**três opções de processos** a ser seguido:  
  
1- Primeira opção pode ser customizado o **NFESEFAZ .**  
  
**[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download?e=1152113)  
  
**Rdmake disponível no link acima.****  
  
2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**  
  
  
3- Terceira opção para que seja atendido no padrão é necessário que a empresa tenha alguma **legislação na qual informe a obrigatoriedade** de gerar conforme deseja.  
  
Havendo a legislação abra um ticket no suporte e nos encaminhe que será compartilhado junto a consultoria tributária da TOTVS e posteriormente ao produto.

* **Importante:**

Caso haja um **valor unitário bruto no campo da SD2 "D2\_PRUNIT"** e outro valor no campo do preço **de lista "D2\_PRCVEN"** será levada na TAG **vUnCom** o valor bruto e gerado desconto com a diferença dos dois campos:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15337120711063)

**Na impressão do Danfe,** será apresento do valor unitário Bruto e no campo desconto a diferença dos dois campos da **SD2.**

* Temos um parecer da **consultoria tributária da TOTVS** referente a isso, no link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=353292106>

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063317454)
