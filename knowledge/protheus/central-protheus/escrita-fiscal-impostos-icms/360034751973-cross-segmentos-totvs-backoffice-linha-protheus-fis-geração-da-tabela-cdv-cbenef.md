---
article_id: 360034751973
category: Escrita Fiscal - Impostos - ICMS
content_hash: 08e1d154a86e87a9fa1d84c36824a10d9fea6f1984a31673da8487f21b318e15
fetched_at: '2026-06-28T22:39:25.909420+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Geração da tabela
  CDV "cBenef" para alimentar a tag cBenef para o estado do RS '
type: support-article
updated_at: '2024-01-24T13:41:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034751973-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-cBenef-para-alimentar-a-tag-cBenef-para-o-estado-do-RS
---

**Dúvida**Como gerar a tabela CDV para alimentar a tag cBenef para o estado do RS?  
  
  
**Ambiente**Protheus - Livros Fiscais - A partir Todas versões 12  
  
  
**Solução**

o tratamento da tag cbenef para o estado de RS devera seguir orientação abaixo:

A TAG **cBenef é** validada pela **UF do emitente**, sendo assim para **UF de transmissão de nota** (por operação)

Para gerar a tabela **CDV** realize os seguintes passos:

1. Configure os parâmetros;

* **MV\_ESTADO = RS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693471827735)

* **MV\_GIAEFD = F**

![](https://totvssuporte.zendesk.com/attachments/token/IyfXFYRoPtEAKNiI1rFhSLgdk/?name=image.png)

**Importante:** Caso o parâmetro **MV\_GIAEFD estiver igual a .T.** a tabela CDV (responsável pela geração da tag cBenef) não será alimentada através do documento fiscal e por isso a tag não será gerada. Este parâmetro foi criado para atender as geração do registro E115 da EFD ICMS/IPI, porém realizando o processo abaixo, o registro também será gerado não sendo mais necessário utilizar o parâmetro MV\_GIAEFD com o conteúdo igual a .T.

2. Importar os códigos de lançamento da tabela 5.2 do estado do **RS** pelo **U\_IMPSPED** ou **cadastrar manualmente na rotina FISA156 - Códigos de Valores Declaratórios;**

Para importar a tabela, siga os passos abaixo:

* Realizar o ***download*****da tabela 5.2** através do portal do SPED na receita federal

<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

 Realizar o *download* da tabela

- Após realizado o *download*, é necessário **renomear** a tabela para o nome **"TABELA52.TXT"**.

- Colocar a tabela dentro da pasta Protheus\_Data

**\***Caso seu servidor for **Linux** o arquivo deve ser em letra minúscula "**tabela52.txt**" e o caminho interno deve ser em minúsculo da pasta por exemplo: protheus\_data/system/...

- Executar o Protheus com a opção "U\_IMPSPED":

- Selecionar a pasta onde está o arquivo e clicar em "Abrir"

- Confirmar a execução para importação das tabelas:

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=ax22ZPjEWIQ>*

![IMPORTAÇ~~AO RS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19034866864023)

**Após concluir será gravado os códigos na sua tabela CDY**

**Importante:** Os códigos da tabela 5.2 que não precisam gerar a tag cBenef, porém precisam ser apresentados no registro E115 da EFD ICMS/IPI devem estar com o campo "Gera NFe" (CDY\_NFE) igual a "Não" para que o código seja ignorado na geração do xml de transmissão. Mesmo com o campo igual a Não será gerado a tabela CDV.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18692678312215)

Agora deve acessar a rotina FISA140

3. Criar a **amarração** na rotina **FISA140 - Prod. x Cod.V.Decl.;**

**Informar:**

* Produto
* CFOP da operação a ser aplicado aquele código
* Cod. Val. Decl (Tabela 5.2 da receita federal)
* CST
* Código de Reflexo conforme a sua necessidade

Exemplo:

**Vídeo didático no canal How To da Totvs no Youtube:** *<https://www.youtube.com/watch?v=WOUvZLBvRUU>*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693471833751)

**Dica:** No portal da nota fiscal eletrônica é possível saber qual código declaratório pode ser usado em correlação ao CST.

Acesse o site da Nota fiscal Eletrônica **<https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=>**

Vai até a  Tabela cBenef e clica no site do Rio Grande do Sul

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693455548311)

Será aberto o site do SEFAZ RS

Em Arquivos da NF-e acessar clicando no "aqui"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693455551255)

Depois vai até o bloco NF-e Nota Fiscal Eletrônica e clique na Tabela cBenef\_x\_CST onde será feito o Download da tabela em Excel, neste excel pode verificar qual Código Declaratório pode ser usado para o CST desejado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693471842967)

Após concluir, ir no MATA410 Pedido de venda e realizar inclusão do pedido de venda.

Depois que colocar o cliente, produto, quantidade e valor unitário e total, coloque a tes devidamente configurada e ir em Outras ações, Planilha, Aba lançamento de apuração e clicar em valor Declaratório.

Neste momento vai aparecer as informações para tag cbenef

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693471846039)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693455559063)

**ATENÇÃO**

Somente será gravada a tabela CDV após emissão da nota fiscal.

É desta tabela que a montagem do XML vai buscar para gerar a tabela para gerar a tag cBenef

## **Caso a tes esteja como:**

Calcula ICMS= NÃO e o Livro de ICMS estiver como OUTROS ou ISENTO, o código reflexo deve estar desta forma:

**Vídeo didático no canal How To da Totvs no Youtube:**

*<https://www.youtube.com/watch?v=1NGqosady-4&t=9s>*

*<https://www.youtube.com/watch?v=_frSFU_mm2A&t=26s>*

* Para Calcula ICMS= NÃO e Livro de ICMS = ISENTO

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18693455563415)

* Para Calcula ICMS= NÃO e Livro de ICMS = OUTROS

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18693455566871)

**Nos casos de redução de base de ICMS como fazer a amarração do código de reflexo:**

Documentação para configurar a redução de base do ICMS:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342473--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-de-ICMS>

Cadastro TES:

Calc. ICMS (F4\_ICM) = S

%Red.do ICMS (F4\_BASEICM) "TES" ou %Red.do ICMS (F7\_BASEICM) "Exceção fiscal" = Informe o valor a ser calculado do ICMS próprio. No padrão, este valor é apresentado na coluna Tributada do Livro Fiscal.

Livro Fiscal ICMS (F4\_LFICM) = ISENTO/ OUTROS. Selecione uma das opções para informar onde será destacado o restante da operação Valor total da NF menos percentual informado no campo F4\_BASEICM.

Material de Consumo (F4\_CONSUMO)=NÃO

Exemplo:

%Red.do ICMS (F4\_BASEICM) ou %Red.do ICMS (F7\_BASEICM)= 60;

Livro Fiscal ICMS (F4\_LFICM) = ISENTO

Material de Consumo (F4\_CONSUMO) = NÃO

O valor do ICMS será dividido entre as colunas Tributado(60%) e Isento(40%)

%Red.do ICMS (F4\_BASEICM) ou %Red.do ICMS (F7\_BASEICM)= 60;

Livro Fiscal ICMS (F4\_LFICM) = OUTROS

Material de Consumo (F4\_CONSUMO) = NÃO

O valor do ICMS será dividido entre as colunas Tributado(60%) e Outros(40%)

O código de reflexo deixe desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693455567895)

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=J_2XSvhVe5I>*

**Nos casos de ICMS Diferido**

Diferimento

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS?source=search>

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=0rYNnvJTgCc>*

Deixe seu código de reflexo desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18693455570455)

**DICA**

Existe uma forma de tratar a FISA140 em vez de código de produto, poderá tratar via grupo de tributação.

Para tratar por grupo de tributação existe o parametro MV\_MTCLF3K

* MV\_MTCLF3K= 0 tratará por código de produto
* MV\_MTCLF3K= 1 tratará por grupo de tributação

Segue documentação:

<https://tdn.totvs.com/pages/releaseview.action?pageId=520651465>

**Exemplo:**

Se seu produto tem o grupo tributário amarrado como 001

E seu cliente o grupo tributário estiver em branco

A regra da FISA140 deve ter somente o grupo de produto informado = 001 e grupo de cliente em branco

Agora se seu produto tem o grupo tributário amarrado como 001

E seu cliente o grupo tributário estiver AAA

A regra da FISA140 deve ter somente o grupo de produto informado = 001 e grupo de cliente= AAA

![GO GRUPOI TRB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19034895724183)

**IMPORTANTE:**

Se a informação estiver gerada CDV e mesmo assim não gera as informações no XML ou causando rejeição de transmissão,  orientamos abrir um chamado com a equipe do **TSS "Nota fiscal eletrônica" para maiores esclarecimentos**.
