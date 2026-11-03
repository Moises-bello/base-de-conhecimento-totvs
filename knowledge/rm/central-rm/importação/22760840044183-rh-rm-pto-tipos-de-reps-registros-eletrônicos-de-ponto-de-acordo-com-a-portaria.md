---
article_id: 22760840044183
category: Importação
content_hash: f702430f5daa341a2d73fedf275b658c5b7f703d4e88e15d2f79d14f4e35148f
fetched_at: '2026-06-28T22:46:33.705770+00:00'
product: rm
section_id: 6045469428631
source: central-rm
title: RH - RM - PTO - Tipos de REPs (Registros Eletrônicos de Ponto) de acordo com
  a Portaria 671
type: support-article
updated_at: '2026-06-25T16:19:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22760840044183-RH-RM-PTO-Tipos-de-REPs-Registros-Eletr%C3%B4nicos-de-Ponto-de-acordo-com-a-Portaria-671
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22760839998871) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quais são os REPs, de acordo com a portaria 671?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.2302.226, 12.1.2306.171 e 12.1.2310.105 ou superiores.  
  
**Solução**

Com base na nova Portaria 671, foram estabelecidos os tipos de Registros Eletrônicos de Ponto (REPs) para realizar a marcação de ponto, os quais são os seguintes:

* **REP-A:** refere-se aos **REPs alternativos** que possibilitam o registro das marcações por meio de **aplicativos** ou **softwares em celulares**, **tablets** e **notebooks**. Para este tipo de REP, não é gerado o arquivo fiscal AEJ e é necessário formalizar em Acordo Coletivo de Trabalho.
* **REP-C:** trata-se dos **REPs físicos** que realizam o registro de ponto por **biometria**.
* **REP-P**: também são **REPs alternativos** que permitem o registro das marcações por meio de **aplicativos ou softwares em celulares, tablets e notebooks**. Para este tipo de REP, é necessário o registro no INPI (Instituto Nacional de Propriedade Industrial) e a certificação digital ICP, portanto, não é exigida a formalização em Acordo Coletivo de Trabalho. **Este tipo de REP emite os arquivos fiscais AFD e AEJ.**

Para esses três tipos de REPs, o layout do arquivo será tratado com base no CPF completo do funcionário + espaço.   
No caso dos **REPs do tipo A e C, o layout é idêntico.** **Conforme estabelecido na portaria, Registro do tipo "3", posição 035-046, será reconhecido por CPF, sendo a leitura****iniciada da esquerda para direita, contendo os 12 dígitos iniciando com o 0 contendo apenas o CPF nas 11 primeiras posições ou na 12ª posição com espaço.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22814640215063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22814640248343)  
**Exemplo:**  
00000049332025-02-09T10:00:00-0300075215950687b722  
Na linha acima há um dígito 'zero' a mais antes do CPF.

Para opção acima, no modulo de automação de ponto, ao realizar o cadastro do layout marque o parâmetro '**Utiliza layout AFD Portaria 671/2021, contém somente CPF'**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22814620106135)  
  
A partir 31/08/2023 o MTE atualizou o layout para importação de batidas, onde permite a possibilidade de preencher o campo CPF possa ser preenchido com o espaço a direita, reservado para o campo tenha tamanho 12(doze). Esta opção deverá ser utilizada quando os registradores de pontos que gerem o AFD apenas com o CPF do funcionário no Registro do tipo "3" (REP-A e REP-C), posição 035-046.

**Exemplo**:

00000049332023-08-31T08:23:00-0300**16661696061** b722

Na linha acima está sem o zero '0' antes do CPF e um espaço após o CPF.

Para opção acima, no modulo de automação de ponto, ao realizar o cadastro do layout marque o parâmetro '**Utiliza layout AFD Portaria 671/2021**'.     
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22814620044311)  
  
  
Para o **REP-P**, o layout segue o exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22814640355607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33832125374231)

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33832125375511)

Para opção acima, no modulo de automação de ponto, ao realizar o cadastro do layout marque o parâmetro **'Utiliza layout AFD Portaria 671/2021**'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35913249605783)

Além dos relógios mencionados, também temos as situações em que os REPs antigos, aprovados pelas antigas portarias 1510 e 373. Esses equipamentos foram divididos em duas categorias com a chegada da nova Portaria:

* **REPs que foram atualizados para atender aos novos layouts conforme a Portaria 671**: nesses casos, a leitura dos dados será feita por meio do dígito 9 + CPF completo do funcionário ou dígito 8 + 10 primeiras posições do CPF do funcionário + dígito verificador (calculado pelo equipamento com base no número do CPF do funcionário).
* **REPs que não foram atualizados:** nesses casos, a leitura permanece da mesma forma, ou seja, por meio do dígito 0 + PIS completo do funcionário ou PIS completo do funcionário + espaço.

O layout para ambos os casos permanece essencialmente o mesmo, sendo a única diferença que, no primeiro cenário, é utilizado o CPF e, no segundo, o PIS.

* O layout será o seguinte ao utilizar o dígito 9 + CPF completo do funcionário:   
  ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22760840009751)
* E desta forma ao utilizar o dígito 8 + 10 primeiras posições do CPF + dígito verificador:   
  ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22760848500247)
* Já para os REPs que não sofreram atualização, o layout permanece o mesmo já utilizado, ou seja: dígito 0 + PIS.  
  ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22760840013591)  
    
  ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22761320115479)  
    
  Para opção acima, no modulo de automação de ponto, ao realizar o cadastro do layout marque o parâmetro **'Utiliza layout AFD Portaria 1510/2009'**  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22815141793559)

Para maiores detalhes sobre o REP adaptado, acesse o link abaixo:

[RH - RM - PTO - Layout AFD portaria 1510 "adaptado" para portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21892016897047)  
  
**Importante**

* **Os tipos de validação '0', '9' e '8' são definidos no software do REP;**
* **O dígito verificador do PIS, com base no número CPF, para empregados que não possuem PIS e o REP faz validação do PIS (tipo '8') é gerado pelo software do REP e inserido ao AFD na posição 34 para posterior importação;**
* **O RM Totvs Automação de Ponto** ***somente*** **efetua a leitura do arquivo AFD no formato .txt gerado pelos REP's, desde que o arquivo gerado pelos REP's estejam conforme exigido pelas portarias 1.510/2009 ou 671/2021.**

**Saiba Mais**  
[RH - RM - PTO - Cadastrar layout do terminal de coleta (relógio) no Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000485588)  
[RH - RM - PTO - Quais são as opções para importar marcações para o Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21824136713367)
