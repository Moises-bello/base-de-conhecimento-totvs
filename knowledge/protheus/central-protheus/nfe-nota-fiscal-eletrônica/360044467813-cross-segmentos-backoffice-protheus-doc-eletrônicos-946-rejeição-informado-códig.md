---
article_id: 360044467813
category: NFe - Nota Fiscal Eletrônica
content_hash: 9d59ab36e737af986b92086944dc3dc2009b2457ddf0193be9f3da865922d1dd
fetched_at: '2026-06-28T22:40:03.434599+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  946 Rejeição :
  Informado código de benefício fiscal incorreto ou inexistente na UF'
type: support-article
updated_at: '2025-08-12T00:11:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044467813-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-946-Rejei%C3%A7%C3%A3o-Informado-c%C3%B3digo-de-benef%C3%ADcio-fiscal-incorreto-ou-inexistente-na-UF
---

**Dúvida**

Como corrigir a rejeição abaixo:

946 Rejeição : Informado código de benefício fiscal incorreto ou inexistente na UF ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Importante:**

O ambiente deve estar atualizado com os pacotes do link abaixo:

[MP-NFE-Nota técnica 2019.001](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027935371)

1 - Verificar se o código gerado na TAG ***cBenef***  está de acordo com a tabela que consta no site da Sefaz nacional.

* As listas disponíveis são para as UFs de **RS, RJ, PR** e **DF**nos links abaixo:

Tabela cBenef x CST - Relacionada à Nota Técnica 2019.001  
  
        Estado do Paraná  
        <http://www.sped.fazenda.pr.gov.br/modules/conteudo/conteudo.php?conteudo=146>  
  
        Estado do Rio Grande do Sul  
        <https://receita.fazenda.rs.gov.br/lista/2933>  
  
        Estado do Rio de Janeiro  
        <http://www.fazenda.rj.gov.br/dfe>

        Distrito Federal  
        [http://www.fazenda.df.gov.br/aplicacoes/legislacao/legislacao/](http://www.fazenda.df.gov.br/aplicacoes/legislacao/legislacao/TelaSaidaDocumento.cfm?txtNumero=1&txtAno=2020&txtTipo=734&txtParte=.)

* **Saiba mais:**

Conforme o parecer da consultoria através dos link abaixo, haverá código da **tabela 5.2 para UF de DF:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=555856158>

Para utilizar a **tabela 5.2 para UF de DF** é necessário que o **NFESEFAZ** esteja com **data igual ou superior** 22/07/2020

Nesse Excel caso exista o código de benefício utilizado e na coluna do **CST esteja como SIM** é possível verificar também as duas colunas  **DT INÍCIO e DT FINAL**, com isso verifique se o mesmo ainda está vigente.

* **Exemplo :**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060467173)

2 - Lembrando que a*TAG **cBenef é** validada pela **UF do emitente**, ou seja a **UF de transmissão de nota.***

* **Caso seja emitente dos Estados de PR / RJ / RS / DF que utilizam a tabela 5.2 e**haja dúvidas de como **alterar o código** de benefício gerado na nota consultar o link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG cBenef na versão 4.00](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017974352)

3 - Além disso, caso tenha gerado na *TAG **cBenef o literal SEM CBENEF é importante verificar as informações abaixo:***

O literal **SEM CBENEF** só é gerado para as UFs de **PR** e **RS.**

Para o **Paraná** pode ser gerado para o CST abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34111865094551)

Para o **Rio Grande do Sul** pode ser gerado para os CSTs abaixo:

​![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34111849523351)

* **Importante após 10/08/2020:**

Será aceito para **CST 10 e 90.**

4 - No qual houve correção  para os **emitentes do Estado do RS**,  para o CST 10 e 90.

Caso não tenha no configurador crie o parâmetro **MV\_CODCST** conforme abaixo:

**1.** Criando o parâmetro.

**a)**Acessar o módulo**SIGACFG;**

**b)** Acessar a rotina **Base de Dados** \ **Dicionário** \ **Base de Dados** ou **Ambiente** \ **Cadastros** \ **Parâmetros;**

Vamos utilizar a rotina **Ambiente** \ **Cadastros** \ **Parâmetros:**

![](https://tdn.totvs.com/download/attachments/559504153/image2020-8-10_10-49-48.png?version=1&modificationDate=1597953883447&api=v2)

**c)** Selecionar **Parâmetros**, e em seguida, clicar na opção **Incluir**.

![](https://tdn.totvs.com/download/attachments/559504153/image2020-8-10_10-51-57.png?version=1&modificationDate=1597953883477&api=v2)

**d)** Informar os dados da criação do parâmetro.

Na aba **Informações**, para os campos:

**Filial:** pode ser específico por filial ou em branco (genérico para todas as filiais).

**Nome da Var.:** nome do parâmetro: **MV\_CODCST**.

**Tipo:**deve ser **Caracter**.

**Cont. Por**: Preencher conforme orientações do tópico **02. Exemplo de Utilização**

**Cont. Ing**:

**Cont. Esp**:

![](https://tdn.totvs.com/download/attachments/559504153/image2020-8-20_17-48-28.png?version=1&modificationDate=1597956508270&api=v2)

**e)** Na aba **Descrição**, para os campos:

**Descrição**: Resp. por configurar o conteúdo da tag cBenef

**Cont. Descriç**: Informar UF=CST para SEM CBENEF

**Cont. Descriç**: Informar apenas UF para tabela 5.2

Caso necessário, informar a descrição em outros idiomas, possuem os mesmos campos para inglês e espanhol.

![](https://tdn.totvs.com/download/attachments/559504153/image2020-8-20_17-48-56.png?version=1&modificationDate=1597956536547&api=v2)

## **EXEMPLO DE UTILIZAÇÃO**

O preenchimento do parâmetro funciona das seguintes formas:

* Para uma ou mais UFs, preenchendo o código da UF acompanhada do CST para que o conteúdo da tag **cBenef seja alimentado com o literal "SEM CBENEF"**:
* Ex.: RS=10,90;PR=10

* Para uma ou mais UFs, preenchendo apenas a UF, caso a**informação da tag seja originada da tabela 5.2 - Informações Adicionais da Apuração - Valores Declaratórios****- V**
* EX.: DF;RJ

* De forma mista, onde algumas UF's venham acompanhadas do CST e outras não;
* Ex.: RS=10,90;DF;PR=10;RJ

Aviso

* Para informar o CST, o formato deve ser UF=CST, entre a UF e CST deve existir o símbolo que representa igualdade ( **=** );
* As UFs **devem** ser separadas por **ponto e vírgula** ( **;** );
* **Não pode haver espaço em branco** entre o conteúdo;
* Caso exista mais de um CST para a mesma UF, **separar os CSTs por vírgula**( **,** ) no formato **UF=CST,CST**.

* **Saiba mais:**

<https://tdn.totvs.com/display/public/PROT/Preencher+a+tag+cBenef+no+XML+da+NF-e>

[Clique aqui](https://tdn.totvs.com/display/public/PROT/9502079+DSERTSS1-15450+DT+Literal+SEM+CBENEF+para+UF+do+RS+para+CST+10)

* **Saiba mais:**

Há algumas exceções para essa rejeição conforme o print que consta abaixo, porém a maioria é a ***critério da UF.***

E foi acrescentado que essa validação ***não se aplica a emitentes do Simples Nacional*** que utilizam ***CSOSN.***

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077573614)

* **Cronograma de Validação:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060389153)**
