---
article_id: 360025543594
category: NFe - Nota Fiscal Eletrônica
content_hash: 50864d03a2acf815a7cc15d9a78aca4281d641bc26ef5ad6895e5fcb216061b7
fetched_at: '2026-06-28T22:40:01.592628+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 928 Rejeição :
  Informado código de benefício fiscal para CST sem benefício fiscal'
type: support-article
updated_at: '2024-06-10T17:31:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025543594--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-928-Rejei%C3%A7%C3%A3o-Informado-c%C3%B3digo-de-benef%C3%ADcio-fiscal-para-CST-sem-benef%C3%ADcio-fiscal
---

**Dúvida**Como solucionar a rejeição abaixo:

928 Rejeição : Informado código de benefício fiscal para CST sem benefício fiscal

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

No site da Sefaz nacional é possível consultar a lista de **código de beneficio** que podem ser utilizados por **CST**

* As listas disponíveis são para as UFs de **GO**, **RS, RJ, PR** e **DF**nos links abaixo:

Tabela cBenef x CST - Relacionada à Nota Técnica 2019.001

Distrito Federal (Atualizada em 12/05/2023)

[https://ww1.receita.fazenda.df.gov.br/legislacao/visualizar-legislacao?txtNumero=4&txtAno=2023&txtTipo=734&txtParte=.&identificacao=Ato Declaratório - Assuntos Econômicos nº 4/2023](https://ww1.receita.fazenda.df.gov.br/legislacao/visualizar-legislacao?txtNumero=4&txtAno=2023&txtTipo=734&txtParte=.&identificacao=Ato%20Declarat%C3%B3rio%20-%20Assuntos%20Econ%C3%B4micos%20n%C2%BA%204/2023)

 

Estado de Goiás

<https://www.economia.go.gov.br/files/Documentos_Fiscais/IN.docx>

Estado do Paraná

<https://sped.fazenda.pr.gov.br/NFe/Pagina/CODIGO-DE-BENEFICIO-FISCAL>

Estado do Rio Grande do Sul

<https://atendimento.receita.rs.gov.br/nf-e-nota-fiscal-eletronica>

Estado do Rio de Janeiro

<http://www.fazenda.rj.gov.br/dfe>

Obs: Os demais Estados não utilizam a tabela cBenef.

Se necessário gerar o literal **SEM CBENEF.**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **incluir** **MV\_CODCST** conforme abaixo:

**Nome da Var.:** nome do parâmetro: **MV\_CODCST**.

**Tipo:**deve ser **Caracter**.

**Cont. Por**: Preencher conforme orientações do tópico **02. Exemplo de Utilização**

**Cont. Ing**:

**Cont. Esp**:

**e)** Na aba **Descrição**, para os campos:

**Descrição**: Resp. por configurar o conteúdo da tag cBenef

**Cont. Descriç**: Informar UF=CST para SEM CBENEF

**Cont. Descriç**: Informar apenas UF para tabela 5.2

Caso necessário, informar a descrição em outros idiomas, possuem os mesmos campos para inglês e espanhol.

## **EXEMPLO DE UTILIZAÇÃO**

O preenchimento do parâmetro funciona das seguintes formas:

* Para uma ou mais UFs, preenchendo o código da UF mais o código do CST será gerado conteúdo da tag **cBenef  com o literal "SEM CBENEF"**:
* Ex.: RS=10,90;PR=10

* Para uma ou mais UFs, preenchendo apenas a UF, caso a**informação da tag seja originada da tabela 5.2 - Informações Adicionais da Apuração - Valores Declaratórios**
* EX.: DF;RJ;PR.RS;GO

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

*A TAG **cBenef é** validada pela **UF do emitente**, sendo assim para **UF de transmissão de nota***

* **Caso seja emitente dos Estados de PR / RJ / RS / DF tabela 5.2.**

Para gerar a tabela **CDV** realize os seguintes passos:

1. Configure os parâmetros;

De acordo com a sua **UF de transmissão** da nota

* **MV\_ESTADO = RS**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444432901399)

Ou

* **MV\_ESTADO = PR**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444416787223)

Ou

* **MV\_ESTADO = RJ**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444432926615)

Ou

* **MV\_ESTADO = DF**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444416802071)**

* **MV\_GIAEFD = F**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444432943127)

**Importante:** 

Caso o parâmetro **MV\_GIAEFD** estiver igual a **.T.** a tabela CDV (responsável pela geração da tag cBenef) não será alimentada através do documento fiscal e por isso a tag não será gerada.

Este parâmetro foi criado para atender as geração do registro **E115 da EFD ICMS/IPI,** porém realizando o processo abaixo, o registro também será gerado **não sendo mais necessário** utilizar o parâmetro **MV\_GIAEFD com o conteúdo igual a .T.**

2. Importar os códigos de lançamento da tabela 5.2 do estado do **PR, RS, RJ** pelo **U\_IMPSPED** ou **cadastrar manualmente na rotina FISA156 - Códigos de Valores Declaratórios;**

Para importar a tabela, siga os passos abaixo:

* Realizar o ***download* da tabela 5.2** através do portal do SPED na receita federal

[CLIQUE AQUI](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)

**Exemplo:**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444432949911)

* Após realizado o***download***, é necessário renomear a tabela para o nome **TABELA52.TXT**

* Colocar a tabela dentro da pasta **Protheus\_Data**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444432957463)

* Executar o Protheus com a **opção U\_IMPSPED**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444432959127)

* Selecionar a pasta onde está o arquivo e **clicar em "Abrir"**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444432966807)

* **Confirmar** a execução para **importação das tabelas**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444416851991)

**Importante:**

**Os códigos da tabela 5.2 que não precisam gerar a tag cBenef**, porém precisam ser apresentados no registro **E115 da EFD ICMS/IPI devem estar com o campo "Gera NFe" (CDY\_NFE) igual a "Não"** para que o código seja ignorado na geração do xml de transmissão.

Lembrando que mesmo com o campo igual a **Não** será gerado a tabela **CDV.**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444416859799)

3. Criar a **amarração** na rotina **FISA140 - Prod. x Cod.V.Decl.;**

**Informar:**

* Produto
* CFOP da operação a ser aplicado aquele código
* Cod. Val. Decl (Tabela 5.2 da receita federal)
* CST
* Código de Reflexo conforme a sua necessidade

* Base p/ calc. = Base ICMS
* Alíquota = Alíquota de ICMS
* Valor = valor do ICMS

**Configurar a TES:**

* Calcula ICMS = Sim
* L. Fiscal ICMS = Isento
* CFOP da operação a ser utilizado
* Sit Trib ICM = da operação a ser utilizado

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444432998167)

Dentro da rotina **FISA140 está disponível um facilitador** que permite **importar os produtos**.

Após preencher o **CFOP, CST e Código de reflexo**, a rotina irá incluir automaticamente todos os produtos com as regras cadastradas.

* **Exemplo:**

Preencha as perguntas com os **filtros desejados**:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444505027991)

Na tela apresentada a seguir, preencha os campos apresentados para que o sistema faça a **inclusão destes códigos para todos os produtos encontrados.**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444467346327)

**Importante:**

O código de reflexo utilizado deverá retornar algum valor para que as informações sejam gravadas na **CDV.**

Se o campo Valor **(CE0\_NFVALO) retornar zero** as informações não serão gravadas.

4. Para verificar se os valores serão gravados **na CDV acessar na planilha do pedido de venda** na aba **Lançamento da apuração ->Val Declaratório;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444505056919)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17444505063703)

**Importante:**

Na rotina **FISA156** existe o campo **CDY\_NFE**  **"Gera NFE"** de acordo com o código de ajuste deve definir o campo como **1**- Sim ou **2-** Não.

Para levar a TAG **Cbenef** no XML o campo deve estar configurado **diferente de 2 -Não, ou seja com 1 ou em branco**

* **Caso esteja gravando na CDV, mas não esteja levando para o XML:**

O fonte do NFESEFAZ verifica se a tabela CDV possui os **4 índices**, por isso será necessário verificar a **SIX.**

* **O campo no Sigamat.emp:**

**M0\_ESTENT ==** "PR" ou "RJ" ou "RS"

* **E o campo:**

**CDV\_CODAJU =** Preenchido corretamente.

* **Após isso realizamos a comparação do tamanho dos campos na SX3:**

CDV\_DOC e D2\_DOC

CDV\_SERIE e D2\_SERIE

CDV\_CLIFOR e D2\_CLIENTE

CDV\_LOJA e D2\_LOJA

* **Saiba mais:**

Conforme o parecer da consultoria através dos link abaixo, haverá código da **tabela 5.2 para UF de DF:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=555856158>

Para utilizar a **tabela 5.2 para UF de DF** é necessário que o **NFESEFAZ** esteja com **data igual ou superior** 22/07/2020

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095010493)
