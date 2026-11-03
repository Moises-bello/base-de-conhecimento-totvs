---
article_id: 360060446574
category: RH - Folha de Pagamento
content_hash: 44ad284ed66b70b994138275df8af2002934d7780ecd05c7923ba9a0770af13b
fetched_at: '2026-06-28T22:44:17.136924+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Contribuição previdenciária patronal sobre o salário-maternidade
  NT 20/2020.
type: support-article
updated_at: '2024-09-12T19:31:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060446574-RH-Linha-Protheus-GPE-Contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-patronal-sobre-o-sal%C3%A1rio-maternidade-NT-20-2020
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26333507518359) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como calcular Contribuição Previdenciária sobre salário maternidade NT 20/2020?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que as verbas referentes a Maternidade nos roteiros FOL (folha), RES (rescisão) e 132 (segunda parcela do 13º) não entrem na composição da base dos encargos patronais. É necessário a aplicação do pacote desta atualização: [https://tdn.totvs.com/pages/releaseview.action?pageId=576982919.](https://tdn.totvs.com/pages/releaseview.action?pageId=576982919)  
  
Para esse calculo foram criados dois mnemônicos, sendo eles:  
1. Mnemônico: **P\_DEDMAT**

Definição: Define quais verbas de maternidade serão desprezadas para formação da base dos encargos patronais.

As opções do mnemônico são:

* 1ª OPÇÃO: Para que automaticamente **todas as verbas de maternidade** sejam **desprezadas** na composição da base de cálculo do encargo patronal, deve permanecer com **conteúdo "1"** (opção **padrão** do produto);

**IMPORTANTE**: O tratamento de carga automática das verbas - opção "1" do mnemônico P\_DEDMAT - é válido apenas para verbas que compõem **a base de INSS (RV\_INSS = 'S'), com RV\_INCCP igual a 21 ou 22 e cujo campo no cadastro de verbas "Cd. Inc. CP." (RV\_NATUREZ) esteja preenchido**, ou seja, é **restrita às verbas configuradas como pagamento de auxílio-maternidade**.

* 2ª OPÇÃO: Informar o código de cada verba que deseja-se desprezar individualmente , ex.: "001002003" (no caso, 001 por exemplo, é a verba de identificador de cálculo 0040 - Aux. Maternidade) - somente necessária para casos em que a 1ª opção não atender à necessidade;
* 3ª OPÇÃO: Em branco para que todas as verbas referentes a maternidade continuem somando na base de cálculo do encargo patronal.

2. Mnemônico: **P\_ENCEMP**

Definição: Define quais encargos patronais serão calculados utilizando essa nova composição de base.

As opções do mnemônico são:

* 1ª OPÇÃO: Para que o critério se aplique a **todos os encargos patronais**, deve permanecer com **conteúdo "1"** (opção **padrão** do produto);
* 2ª OPÇÃO: **Somente** para os casos em que deseja-se desprezar a maternidade apenas para alguns **encargos específicos**, deve-se **informar o código da verba** vinculada a cada identificador de cálculo do encargo patronal desejado. Ex.: "X01X02X03" (no caso, X01 por exemplo, é a verba de identificador de cálculo 0148 - % Empresa)

**Exemplo:** Calculo com conteúdo "opção padrão" para ambos mnemônicos:  
**Mnemônicos:**

**P\_DEDMAT = conteúdo "1"**

**P\_ENCEMP = conteúdo "1"**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102868453)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001856581)

**Cadastro das Verbas Salario Maternidade:**

INSS (RV\_INSS), Natureza (RV\_NATUREZA), Cd.Inc. CP (RV\_INCCP):

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102853213)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102853273)**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001841261)**

**Calculo Licença maternidade:**Calculo folha de pagamento 12/2020 matricula 000016 com calculo dos Encargos abatendo as verbas de Maternidade.  
  
Afastamento Maternidade a partir de 15/12/2020 por 120 dias:  
  
101 – Salario Mensalista = 1430,00  
131 – Auxilio Maternidade = 1870,00  
721 – Base de INSS = 3.300,00

Base INSS com abatimento = 3.300,00  – 1.870,00 = 1.430,00

% Empresa = 1.430,00 \* 20% é 286,00  
% Terceiros = 1.430,00 \* 5,8% é 82,94  
% Acid.Trabalho = 1.430,00 \* 1,5% é 21,45

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102868073)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
