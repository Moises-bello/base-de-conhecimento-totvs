---
article_id: 360033521654
category: NFe - Nota Fiscal Eletrônica
content_hash: 8f8d2f6552a3d13d34a093a93d68c29a22d51ac811323d5c0eb0a4cb7276039f
fetched_at: '2026-06-28T22:40:07.162388+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 930: CST
  com benefício fiscal e não informado o código de benefício fiscal'
type: support-article
updated_at: '2026-05-12T20:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033521654-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-930-CST-com-benef%C3%ADcio-fiscal-e-n%C3%A3o-informado-o-c%C3%B3digo-de-benef%C3%ADcio-fiscal
---

**Dúvida**  
Como corrigir a rejeição 930 - CST com benefício fiscal e não informado o código de benefício fiscal ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

 No site da Sefaz nacional é possível consultar a lista de **código de beneficio** que podem ser utilizados por **CST.**

* **Acessar o site**

[**https://www.nfe.fazenda.gov.br/portal/principal.aspx**](https://www.nfe.fazenda.gov.br/portal/principal.aspx)

Aba documentos -> Diversos, pesquisar ***CBENEF***

Para gerar a tag **cBenef** com o código do beneficio é preciso informar apena a UF do emitente no parâmetro ***MV\_CODCST.***

***Ex: MV\_CODCST  = GO;SC;DF;RJ;PR;RS;ES;SP;***

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

Estado de São Paulo

<https://portal.fazenda.sp.gov.br/servicos/nfe/Paginas/cBenef.aspx>

Obs: Os demais Estados não utilizam a tabela cBenef.

**Saiba mais:**

* **Caso seja emitente dos Estados de****PR / RJ / RS / DF/ SC/ GO/** **tabela 5.2.**

**Para o estado de SP a tabela52 ainda não foi disponibilizada**

Para gerar a tabela **CDV** realize os seguintes passos:

 1. Configure os parâmetros;

De acordo com a sua **UF de transmissão** da nota

* **MV\_ESTADO = RS**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027264919)

Ou

* **MV\_ESTADO = PR**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027265559)

 Ou

* **MV\_ESTADO = RJ**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027267351)

 Ou

* **MV\_ESTADO = DF**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194036984215)**

**ou**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38793258889367)

* **MV\_GIAEFD = F**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194036988823)

**Importante:** 

Caso o parâmetro **MV\_GIAEFD** estiver igual a **.T.** a tabela CDV (responsável pela geração da tag cBenef) não será alimentada através do documento fiscal e por isso a tag não será gerada.

Este parâmetro foi criado para atender as geração do registro **E115 da EFD ICMS/IPI,** porém realizando o processo abaixo, o registro também será gerado **não sendo mais necessário** utilizar o parâmetro **MV\_GIAEFD com o conteúdo igual a .T.**

2. Importar os códigos de lançamento da tabela 5.2 do estado do **PR, RS, RJ**pelo **U\_IMPSPED** ou **cadastrar manualmente na rotina FISA156 - Códigos de Valores Declaratórios;**

Para importar a tabela, siga os passos abaixo:

* Realizar o ***download*****da tabela 5.2** através do portal do SPED na receita federal

[CLIQUE AQUI](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)

**Exemplo:**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027273751)

* Após realizado o***download***, é necessário renomear a tabela para o nome **TABELA52.TXT**
* Colocar a tabela dentro da pasta **Protheus\_Data**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194036995479)

* Executar o Protheus com a **opção U\_IMPSPED**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194036999191)

* Selecionar a pasta onde está o arquivo e **clicar em "Abrir"**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194037003927)

* **Confirmar** a execução para **importação das tabelas**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027286039)

**Importante:**

**Os códigos da tabela 5.2 que não precisam gerar a tag cBenef**, porém precisam ser apresentados no registro **E115 da EFD ICMS/IPI devem estar com o campo "Gera NFe" (CDY\_NFE) igual a "Não"** para que o código seja ignorado na geração do xml de transmissão.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027287959)

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

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027289495)

Dentro da rotina **FISA140 está disponível um facilitador** que permite **importar os produtos**.

Após preencher o **CFOP, CST e Código de reflexo**, a rotina irá incluir automaticamente todos os produtos com as regras cadastradas.

**Exemplo:**

Preencha as perguntas com os **filtros desejados**:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194037011095)

Na tela apresentada a seguir, preencha os campos apresentados para que o sistema faça a **inclusão destes códigos para todos os produtos encontrados.**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027292823)

**Importante:**

O código de reflexo utilizado deverá retornar algum valor para que as informações sejam gravadas na **CDV.**

Se o campo Valor **(CE0\_NFVALO) retornar zero** as informações não serão gravadas.

4. Para verificar se os valores serão gravados **na CDV acessar na planilha do pedido de venda** na aba **Lançamento da apuração ->Val Declaratório;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194027294999)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194037018263)

**Importante:**

Na rotina **FISA156** existe o campo **CDY\_NFE**  **"Gera NFE"** de acordo com o código de ajuste deve definir o campo como **1**- Sim ou **2-** Não.

Para levar a TAG **Cbenef** no XML o campo **CDY\_NFE** deve estar configurado **igual 1, ou em branco.**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043083554)**

Caso precise gerar a tag **cBenef** com o literal ***SEM CBENEF*****,**acessar o módulo **Configurador (SIGACFG)**, em seguida em ***Ambiente /** **Cadastros / Parâmetros*** clicar em ***editar , exemplo:***

***MV\_CODCST******PR=90,41;RS=10,90; são apenas exemplos, tem que preencher com a UF do seu estado e o CST da sua operação.***

![20220321_113222.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18671340453015)

[Clique Aqui](https://tdn.totvs.com/display/public/PROT/Preencher+a+tag+cBenef+no+XML+da+NF-e)

Para estados que possuem necessidade do destaque do grupo **gCred** e tenham necessidade de preencher o código presumido no xml veja as informações abaixo:

* **Atender as novas regras do Fisco Catarinense  ATO DIAT nº 35/2024, que informa os novos campos de preenchimento obrigatório relacionados ao crédito presumido.**

* Caso isenção, redução de base de calculo, diferimento e não incidência ou suspenção da exigibilidade do imposto, será realizado o preenchimento de acordo com o campo da TES (F4\_SITTRIB), caso (40, 51, 41, 50) será gerado o tag cBenef.

* Caso tenha credito presumido, informar TES (F4\_SITTRIB =00), (MV\_CODCST = SC) e (CDY\_TPLANC =1) sendo assim as tags geradas serão cCredPresumido, vCredPresumido e pCredPresumido e não será gerado cBenef.

* Para gerar as duas tags: cBenef e grupo gCred com as tags cCredPresumido, vCredPresumido e pCredPresumido é necessario que tenha dois cadastros para o mesmo código de beneficio na rotina FISA156, sendo um cadastro com campo CDY\_TPLANC em branco para gerar o cBenef e o outro cadastro com CDY\_TPLANC = 1 para gera o grupo gCred.

* Para gerar a tag cBenef com literal SEM CBENEF deve preencher o parâmetro MV\_CODCST igual UF=CST; lembrando que é apenas um exemplo, deve ser inserido a UF do seu estado e o CST do ICMS da sua operação, como exemplo coloquei a UF de Santa Catarina e o CST da minha operação.

EX: MV\_CODCST = SC=00

Abaixo documentações para configuração no Protheus:  
  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar os Códigos de Valores Declaratórios de São Paulo no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38006107103639-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-os-C%C3%B3digos-de-Valores-Declarat%C3%B3rios-de-S%C3%A3o-Paulo-no-Protheus)  
  
TES - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - FIS - Como configurar o cBenef por grupo cliente / produto para o estado de SP?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38585621995287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-configurar-o-cBenef-por-grupo-cliente-produto-para-o-estado-de-SP)  
  
TES - [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Geração da tabela CDV "cBenef" para alimentar a tag cBenef para o estado do SP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38988101281815-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-cBenef-para-alimentar-a-tag-cBenef-para-o-estado-do-SP)  
  
FISA170 - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS Como configurar o ICMS diferido 100% e gerar cBenef para SP?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38777174413463-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-ICMS-diferido-100-e-gerar-cBenef-para-SP)  
  
FISA170 - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar o cBenef operação isenta CST41 no fisa170?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35880226492183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-cBenef-opera%C3%A7%C3%A3o-isenta-CST41-no-fisa170)  
  
FISA170 - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - FIS Como gerar cBenef com redução de base de calculo no fisa170?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38986562919447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-gerar-cBenef-com-redu%C3%A7%C3%A3o-de-base-de-calculo-no-fisa170)

Obs: Se emitir a nota com dois itens para o mesmo CST e no parâmetro MV\_CODCST = UF=CST;  Ex: SP=40;

O item que não gerar registro na tabela CDV ira gerar com a tag cBenef = sem cbenef.

O item que gerar o registro na tabela CDV, vai gerar a tag cBenef com o código informado no campo CDV\_CODAJU.
