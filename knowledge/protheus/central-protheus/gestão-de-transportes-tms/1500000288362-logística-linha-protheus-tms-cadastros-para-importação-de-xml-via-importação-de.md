---
article_id: 1500000288362
category: Gestão de Transportes (TMS)
content_hash: da67a856558a80dbd557f9c0f8a95a4f3fe472fe32f6c89349312691ae7203b5
fetched_at: '2026-06-28T22:45:27.355937+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastros para importação de XML via Importação
  de Notas Fiscais - TMSAE80
type: support-article
updated_at: '2025-02-26T16:57:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000288362-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-para-importa%C3%A7%C3%A3o-de-XML-via-Importa%C3%A7%C3%A3o-de-Notas-Fiscais-TMSAE80
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24853050856855)** Tempo aproximado para leitura: **00:10:00 min****Dúvida**Quais os cadastros necessários para que o Sistema efetue a importação do **XML** de Nota Fiscal via **Importação de Notas Fiscais - TMSAE80?**   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões.  
  
**Solução**Os dados da **transportadora, emitente, destinatário e produtos do XML** para serem importados na leitura do XML devem estar cadastrados no **TMS** da seguinte forma:

* O **CNPJ** da Transportadora do **XML,** referente a *tag* **transporta,** deve ser o mesmo do **SIGAMAT** - **Filial em uso**. No exemplo, utilizamos **CNPJ:** 22372432000166 e **IE:** 574114556.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9776729569303)

* Parâmetro **MV\_CGCTRAN preenchido.** Caso ele esteja em branco, o Sistema **não** importará o **XML** para as tabelas do **TMS**. Este parâmetro é utilizado para importar notas fiscais cujo **XML** não possui a *tag* **<transporta>** preenchida, então, deve-se habilitar ou desabilitar conforme necessidade.
* Cadastrar o emitente do **XML,** referente a *tag* **emit,** como **Cliente - MATA030.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9776971436055)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777031624343)

* Cadastrar o destinatário do **XML, r**eferente a *tag* **dest,** como **Cliente - MATA030.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777228187415)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777326198679)

* Mas, não é necessário incluir os cadastros de emitente e destinatário, o Sistema pode inclui-los de forma automática, para isso, para importar automaticamente o emitente do **XML**, basta habilitar o parâmetro **MV\_IMPEMIT**.   
  Para que o emitente e destinatário do **XML** sejam cadastrados automaticamente como **Cliente - MATA030,** o código do município informado na *tag* **cMun** deve estar cadastrado no **Grupo de Região - TMSA115,** campo **DUY\_CODMUN,** e, no dicionário de dados, os campos **Código - A1\_COD** e **Loja - A1\_LOJA** devem possuir inicializador padrão conforme exemplo abaixo.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9774230751639)**

* Para que o produto do **XML** seja lido e incluído no campo **Código do Produto - DE5\_CODPRO**, então, cadastrar o código do produto do **XML,** *tag* **cProd** e sua unidade de medida na rotina **Produtos - MATA010.**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777336035223)**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777419546263)

* Mas, não é necessário realizar o cadastro deste produto do **XML**, basta utilizar um produto genérico na importação do **XML**, para isso, cadastre um produto no **MATA010** e informe o código deste produto genérico no parâmetro **MV\_PROGEN**, desta forma, o produto deste parâmetro será gravado no campo **DE5\_CODPRO**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255176536087)

* Caso o **XML** possua mais de um produto informado, então, para que seja importado somente um produto, basta desabilitar o parâmetro **MV\_PRDDIV**, desta forma, o Sistema utilizará o produto do parâmetro **MV\_PROGEN** para preencher o campo **DE5\_CODPRO**. Caso deseje importar todos os produtos do **XML,** onde o valor total da nota será a soma do valor dos produtos, então, habilite o parâmetro **MV\_PRDDIV.**
* Com o parâmetro **MV\_PRDDIV** habilitado, podemos associar os produtos do **XML** relacionado a *tag* **cProd** com produto cadastrado no **MATA010**, para isso, podemos utilizar os cadastros de **Produtos x Embarcadora - TMSAE40** ou **Produto x Cliente - MATA370.**
* Com o parâmetro **MV\_PRDDIV** habilitado, no cadastro de **Produtos x Embarcadora - TMSAE40,** informe o cliente emitente, o Código do Produto relacionado ao cadastro do **MATA010,** e, no campo **Produto Embarcado** informe o código referente a *tag* **cProd.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255176539799)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255176542231)**Exemplo de nota importada **![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255176543639)**

* Com o parâmetro **MV\_PRDDIV** habilitado, no cadastro de **Produto x Cliente - MATA370,** informe o cliente emitente, o Código do Produto relacionado ao cadastro do **MATA010**, e, no campo Código Produto Cliente informe o código referente a *tag* **cProd**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255161870359)**Exemplo de nota importada **![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255176547863)**

* Caso o Sistema não encontre os cadastros de **Produtos x Embarcadora - TMSAE40** ou **Produto x Cliente - MATA370**, ou se **MV\_PRDDIV** desabilitado**,** então, o campo **DE5\_CODPRO** será gravado com o conteúdo do parâmetro **MV\_PROGEN**.
* Cadastrar a unidade de medida relacionado a *tag* **uCom** do **XML** na tabela genérica **MG** no **SIGACFG**.

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001391002)

* Cadastrar o emitente do **XML** como **Solicitante - TMSA440.**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777636768151)

* Cadastrar o **Contrato de Cliente - TECA250** para o emitente. No campo **EDI TMS - DDA\_EDITMS** do serviço que será utilizado na importação do **XML**, informar **Sim**. Podemos cadastrar o contrato para o cliente genérico informado no parâmetro **MV\_CLIGEN.** Este parâmetro deve ser configurado com filial em branco, ou seja, compartilhado entre as filiais.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404659146903)

* Cadastrar o **Perfil do Cliente - TMSA480** para o cliente tomador de serviço. **Dica**: somente o Contrato do Cliente é possível utilizar com cliente genérico.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777714703255)

* Necessário preencher a aba **EDI** da seguinte maneira.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001447421)

* Caso deseje habilitar a busca da nota pela Inscrição Estadual do **EDI**, habilite o parâmetro **MV\_INSCEDI.**
* Para considerar o valor total da nota fiscal na importação do **XML**, habilite o parâmetro **MV\_PRDITEM.****Processamento do TMSAE80**
* Incluir o **XML** da **NFe** na pasta **NEW.**

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001449941)

* Caso deseje, pode-se observar no *AppServer* a execução do *Schedule*.

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100285394)

* Após a execução do **EDI**, o **XML** será movido para a pasta **OLD** se a importação ocorreu com sucesso e então, o registro será gravado na tabela **DE5**.
* Caso não seja importado por algum erro, então, o **XML** será movido para a pasta **ERR** e o registro gravado na tabela **DEV.** Se o **XML** foi movido para a pasta **ERR**, basta verificar o movido do erro na rotina **Atualizações/ EDI/ NFEs Não importadas - TMSAE85.**
* Para esta nota que foi importada com erros, então, após os devidos ajustes, basta selecionar a nota desejada e clicar em **Reprocessar.**

**Saiba mais**Para mais informações acesse: [Logística - Linha Protheus - TMS - TMSAE80 Importação de Notas Fiscais - XML.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026949131)  
  
**Glossário  
CNPJ** - Cadastro Nacional da Pessoa Jurídica**ERR** - Pasta que contém os XML não importados por erro  
**IE** - Inscrição Estadual**NEW** - Pasta para adicionar os XML a ser importados **NFe** - Nota Fiscal Eletrônica  
**OLD** - Pasta que contém os XML já importados  
**XML** - *Extensible Markup Language*
