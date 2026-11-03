---
article_id: 360017974352
category: NFe - Nota Fiscal Eletrônica
content_hash: 803d6f68116dc06137862f6709a9b6cfe7f337ef24e562c3d775707c433e217a
fetched_at: '2026-06-28T22:40:06.664366+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG
  cBenef
type: support-article
updated_at: '2026-03-23T13:49:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017974352-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-cBenef
---

**Dúvida**  
MP-NFE- Como gerar a TAG cBenef na versão 4.00 ?   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

*A TAG **cBenef é** validada pela **UF do emitente**, sendo assim para **UF de transmissão de nota***

* **Caso seja emitente dos Estados de** **PR / RJ / RS / DF/ SC/ GO/ SC****tabela 5.2.**

No site da Sefaz nacional é possível consultar a lista de **código de beneficio** que podem ser utilizados por **CST.**

* **Acessar o site**

[**https://www.nfe.fazenda.gov.br/portal/principal.aspx**](https://www.nfe.fazenda.gov.br/portal/principal.aspx)

Aba documentos -> Diversos, pesquisar ***CBENEF***

Se necessário gerar o literal ***SEM CBENEF*****,**acessar o módulo **Configurador (SIGACFG)**, em seguida em ***Ambiente /** **Cadastros / Parâmetros*** clicar em ***editar , exemplo MV\_CODCST******PR=90;41;RS=10,90;GO;SC;***

![20220321_113222.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18673812526103)

[Clique Aqui](https://tdn.totvs.com/display/public/PROT/Preencher+a+tag+cBenef+no+XML+da+NF-e)

Para gerar a tabela **CDV** realize os seguintes passos:

 1. Configure os parâmetros;

De acordo com a sua **UF de transmissão** da nota

* **MV\_ESTADO = RS**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044818834)

Ou

* **MV\_ESTADO = PR**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045680953)

 Ou

* **MV\_ESTADO = RJ**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045681033)

 Ou

* **MV\_ESTADO = DF**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082920273)**

* **MV\_GIAEFD = F**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045681173)

**Importante:** 

Caso o parâmetro **MV\_GIAEFD** estiver igual a **.T.** a tabela CDV (responsável pela geração da tag cBenef) não será alimentada através do documento fiscal e por isso a tag não será gerada.

Este parâmetro foi criado para atender as geração do registro **E115 da EFD ICMS/IPI,** porém realizando o processo abaixo, o registro também será gerado **não sendo mais necessário** utilizar o parâmetro **MV\_GIAEFD com o conteúdo igual a .T.**

2. Importar os códigos de lançamento da tabela 5.2 do estado do **PR, RS, RJ**pelo **U\_IMPSPED** ou **cadastrar manualmente na rotina FISA156 - Códigos de Valores Declaratórios;**

Para importar a tabela, siga os passos abaixo:

* Realizar o ***download*****da tabela 5.2** através do portal do SPED na receita federal

[CLIQUE AQUI](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)

**Exemplo:**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044819814)

* Após realizado o***download***, é necessário renomear a tabela para o nome **TABELA52.TXT**
* Colocar a tabela dentro da pasta **Protheus\_Data**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045682233)

* Executar o Protheus com a **opção U\_IMPSPED**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044820094)

* Selecionar a pasta onde está o arquivo e **clicar em "Abrir"**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044820254)

* **Confirmar** a execução para **importação das tabelas**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044820434)

**Importante:**

**Os códigos da tabela 5.2 que não precisam gerar a tag cBenef**, porém precisam ser apresentados no registro **E115 da EFD ICMS/IPI devem estar com o campo "Gera NFe" (CDY\_NFE) igual a "Não"** para que o código seja ignorado na geração do xml de transmissão.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044820514)

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

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045683193)

Dentro da rotina **FISA140 está disponível um facilitador** que permite **importar os produtos**.

Após preencher o **CFOP, CST e Código de reflexo**, a rotina irá incluir automaticamente todos os produtos com as regras cadastradas.

**Exemplo:**

Preencha as perguntas com os **filtros desejados**:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18402550878615)

Na tela apresentada a seguir, preencha os campos apresentados para que o sistema faça a **inclusão destes códigos para todos os produtos encontrados.**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18402526007703)

**Importante:**

O código de reflexo utilizado deverá retornar algum valor para que as informações sejam gravadas na **CDV.**

Se o campo Valor **(CE0\_NFVALO) retornar zero** as informações não serão gravadas.

4. Para verificar se os valores serão gravados **na CDV acessar na planilha do pedido de venda** na aba **Lançamento da apuração ->Val Declaratório;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18402526009879)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18402526018071)

**Importante:**

Na rotina **FISA156** existe o campo **CDY\_NFE**  **"Gera NFE"** de acordo com o código de ajuste deve definir o campo como **1**- Sim ou **2-** Não.

Para levar a TAG **Cbenef** no XML o campo deve estar configurado **diferente de 2 -Não, ou seja com 1 ou em branco**

* **Saiba mais:**

* Conforme o parecer da consultoria através dos link abaixo, haverá código da **tabela 5.2 para UF de DF:**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=555856158)

* Parecer da Consultoria referente as ***UFs da TAG cBenef:***

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=394221312)

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=676044859)

**Para as demais UFs:**

Para a TAG cBenef deve ser preenchido na TES em **Lançamento de Apuração do ICMS:**

* CC7\_CODLAN = 10 caracteres **(Tabela 5.3).** Será levado para o XML o conteúdo do campo **CDA\_CODLAN**

Abaixo documentações para configuração no Protheus:  
  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar os Códigos de Valores Declaratórios de São Paulo no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38006107103639-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-os-C%C3%B3digos-de-Valores-Declarat%C3%B3rios-de-S%C3%A3o-Paulo-no-Protheus)  
  
TES - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - FIS - Como configurar o cBenef por grupo cliente / produto para o estado de SP?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38585621995287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-configurar-o-cBenef-por-grupo-cliente-produto-para-o-estado-de-SP)  
  
TES - [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Geração da tabela CDV "cBenef" para alimentar a tag cBenef para o estado do SP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38988101281815-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-cBenef-para-alimentar-a-tag-cBenef-para-o-estado-do-SP)  
  
FISA170 - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS Como configurar o ICMS diferido 100% e gerar cBenef para SP?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38777174413463-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-ICMS-diferido-100-e-gerar-cBenef-para-SP)  
  
FISA170 - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar o cBenef operação isenta CST41 no fisa170?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35880226492183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-cBenef-opera%C3%A7%C3%A3o-isenta-CST41-no-fisa170)  
  
FISA170 - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - FIS Como gerar cBenef com redução de base de calculo no fisa170?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38986562919447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-gerar-cBenef-com-redu%C3%A7%C3%A3o-de-base-de-calculo-no-fisa170)
