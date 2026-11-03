---
article_id: 6224866527383
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 0900adac5edad637641ea7e80bbc24c6c5f1bc143f152c4c91711cff46f9f947
fetched_at: '2026-06-28T22:39:31.038226+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Geração da tabela
  CDV "cBenef" para alimentar a tag cBenef para o estado do GO
type: support-article
updated_at: '2024-01-24T13:38:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6224866527383-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-cBenef-para-alimentar-a-tag-cBenef-para-o-estado-do-GO
---

**Dúvida**Geração da tabela CDV "cBenef" para alimentar a tag cBenef para o estado do GO  
**Ambiente**Protheus a partir 12.1.25  
  
**Solução**

O tratamento da tag cbenef para o estado de GO devera seguir orientação abaixo:

A TAG **cBenef é** validada pela **UF do emitente**, sendo assim para **UF de transmissão de nota**

Para gerar a tabela **CDV** realize os seguintes passos:

1. Configure os parâmetros;

* **MV\_ESTADO = GO**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15127975663639)

* **MV\_GIAEFD = F**

![](https://totvssuporte.zendesk.com/attachments/token/IyfXFYRoPtEAKNiI1rFhSLgdk/?name=image.png)

I

2. Importar os códigos de lançamento da tabela 5.2 do estado do **GO** pelo **U\_IMPSPED** ou **cadastrar manualmente na rotina FISA156 - Códigos de Valores Declaratórios;**

Para importar a tabela, siga os passos abaixo:

* Realizar o ***download*****da tabela 5.2** através do portal do SPED na receita federal

<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=ax22ZPjEWIQ>*

**IMPORTANTE**

* Após realizado o***download***, é necessário renomear a tabela para o nome **TABELA52.TXT**
* **\***Caso seu servidor for **Linux** o arquivo deve ser em letra minúscula "tabela52.txt" e o caminho interno deve ser em minúsculo da pasta por exemplo: protheus\_data/system/...
* Colocar a tabela dentro da pasta **System** do Protheus
* Executar o Protheus com a opção**U\_IMPSPED**
* Selecionar a pasta onde está o arquivo e **clicar em "Abrir"**
* **Confirmar** a execução para **importação das tabelas**

**Após concluir será gravado os códigos na sua tabela CDY**

**![GO GIFT 52.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18989487655831)\*\*\*ATENÇÃO\*\*\***

**Sobre o questionamento onde na tabela 5.2 do SPED não existe determinados códigos, porem no portal da nota fiscal existe, isso ocorre porque o SEFAZ de GO "Secretária da Fazenda do estado de Goiás" ainda não atualizou os códigos no portal do SPED.**

**Este questionamento devera ser realizado pelo contribuinte junto ao seu postos fiscal "SEFAZ GO" porque ainda não consta na tabela 5.2 do SPED.**

**Existe a possibilidade de efetuar o cadastro** **manualmente pela rotina FISA156 com o código desejado, no entanto deve se atentar que o código deve ter Data Início informada e Data Final em branco.**

![GO INCLUINDO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18989503696279)

É possível avaliar os códigos exigidos no portal da NFE para cBenef no link

<https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=>

Clique no estado de Goiás para fazer download  do arquivo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18679941209495)

Agora deve acessar a rotina FISA140

3. Criar a **amarração** na rotina **FISA140 - Prod. x Cod.V.Decl.;**

**Informar:**

* Produto
* CFOP da operação a ser aplicado aquele código
* Cod. Val. Decl (Tabela 5.2 da receita federal)
* CST
* Código de Reflexo conforme a sua necessidade

![GO GIFT amarraçao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18989487662999)

Na rotina Código de Reflexo "FISA072" do exemplo

* Base p/ calc. = Base ICMS
* Alíquota = Alíquota de ICMS
* Valor = valor do ICMS

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6224838893719)

**Configurar a TES:**

**Exemplo:**

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=WOUvZLBvRUU>*

* Calcula ICMS = Sim
* Livro Fiscal ICMS = Isento ou Outros
* CFOP da operação a ser utilizado
* Sit Trib ICM = da operação a ser utilizado

      4 . Pedido de Venda MATA410

Para verificar se os valores serão gravados na CDV acessar na planilha do pedido de venda na aba Lançamento da apuração ->Val Declaratório.

![GO PEDIDO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18989487665431)

Após gera a nota fiscal é gerado a tabela CDV com as informações gravadas.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6224916988055)

**ATENÇÃO**

Somente será gravada a tabela CDV após emissão da nota fiscal.

É desta tabela que a montagem do XML vai buscar para gerar a tabela para gerar a tag cBenef

## **Caso a tes esteja como:**

Calcula ICMS=Não e o Livro de ICMS estiver como OUTROS ou ISENTO, o código reflexo deve estar desta forma:

**Vídeo didático no canal How To da Totvs no Youtube:**

*<https://www.youtube.com/watch?v=1NGqosady-4&t=9s>*

*<https://www.youtube.com/watch?v=_frSFU_mm2A&t=26s>*

* Para Calcula ICMS= Não e Livro de ICMS = ISENTO

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12657458796183)

* Para Calcula ICMS= Não e Livro de ICMS = OUTROS

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12657479858583)

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

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18613528315031)

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=J_2XSvhVe5I>*

**Para os casos de ICMS Diferido**

Diferimento

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS?source=search>

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=0rYNnvJTgCc>*

Deixe seu código de reflexo desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18613520545559)

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

![GO GRUPOI TRB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18989503707415)

**IMPORTANTE:**

Se a informação estiver gerada CDV e mesmo assim não gera as informações no XML ou causando rejeição de transmissão,  orientamos abrir um chamado com a equipe do **TSS "Nota fiscal eletrônica" para maiores esclarecimentos**.
