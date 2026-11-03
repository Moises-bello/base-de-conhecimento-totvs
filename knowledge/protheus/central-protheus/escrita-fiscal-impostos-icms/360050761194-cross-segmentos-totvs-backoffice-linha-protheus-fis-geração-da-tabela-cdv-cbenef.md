---
article_id: 360050761194
category: Escrita Fiscal - Impostos - ICMS
content_hash: 394a25d303c4a59af5aa99d69b7ca8e7ee9e324f259a387bfe5c08fe0ce91f22
fetched_at: '2026-06-28T22:39:25.873083+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Geração da tabela
  CDV "cBenef" para alimentar a tag cBenef para o estado do DF "Distrito Federal"
type: support-article
updated_at: '2024-01-24T13:40:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050761194-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-cBenef-para-alimentar-a-tag-cBenef-para-o-estado-do-DF-Distrito-Federal
---

**Dúvida**Como tratar a cBenef para o estado do Distrito Federal - DF  
  
**Ambiente**Protheus – Escrita Fiscal – A partir da versão 12 "Todas versões"

**Solução**

O tratamento da tag cbenef para o estado de DF devera seguir orientação abaixo:

A TAG **cBenef é** validada pela **UF do emitente**, sendo assim para **UF de transmissão de nota**

Para gerar a tabela **CDV** realize os seguintes passos:

1. Configure os parâmetros;

* **MV\_ESTADO = DF**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17479645494679)**

* **MV\_GIAEFD = .F.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17479591530519)**

2. Importar os códigos de lançamento da tabela 5.2 do estado do **DF** pelo **U\_IMPSPED** ou **cadastrar manualmente na rotina FISA156 - Códigos de Valores Declaratórios;**

Para importar a tabela, siga os passos abaixo:

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=ax22ZPjEWIQ>*

* Realizar o ***download*****da tabela 5.2** através do portal do SPED na receita federal

<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

**Pacote**: Tabelas do Distrito Federal

**Tabela**: 5.2 - Ajuste e Informações de Valores Provenientes de Documentos Fiscais - DF

Clique em Baixar.

**IMPORTANTE**

* Após realizado o***download***, é necessário renomear a tabela para o nome **TABELA52.TXT**
* **\***Caso seu servidor for **Linux** o arquivo deve ser em letra minúscula "tabela52.txt" e o caminho interno deve ser em minúsculo da pasta por exemplo: protheus\_data/system/...
* Colocar a tabela dentro da pasta **System** do Protheus
* Executar o Protheus com a opção**U\_IMPSPED**
* Selecionar a pasta onde está o arquivo e **clicar em "Abrir"**
* **Confirmar** a execução para **importação das tabelas**

![DF inportaç~~ao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19034394347671)

**Após concluir será gravado os códigos na sua tabela CDY**

Agora deve acessar a rotina FISA140

3. Criar a **amarração** na rotina **FISA140 - Prod. x Cod.V.Decl.;**

**Informar:**

* Produto
* CFOP da operação a ser aplicado aquele código
* Cod. Val. Decl (Tabela 5.2 da receita federal)
* CST
* Código de Reflexo conforme a sua necessidade

Para validar qual codigo declaratório vs CST pode ser utilizado, acessar o site do portal da NFE e seguir a orientação abaixo:

No site portal da NFE <http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=>

Ir na parte da cBenef x CST e selecionar Distrito Federal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17479840779543)

Ao clicar no link será encaminhado para esta pagina <https://ww1.receita.fazenda.df.gov.br/legislacao/visualizar-legislacao?txtNumero=4&txtAno=2023&txtTipo=734&txtParte=.&identificacao=Ato%20Declarat%C3%B3rio%20-%20Assuntos%20Econ%C3%B4micos%20n%C2%BA%204%2F2023>

Nela consta as informações dos códigos pertinentes para amarra vs CST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17479900520215)

Tendo estas informações devera realizar a amarração pela rotina FISA140 "Produto vs Valor declaratório"

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17480154700951)

Rotina FISA072 "Código de reflexo" link da documentação <https://centraldeatendimento.totvs.com/hc/pt-br/articles/6224866527383-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-cBenef-para-alimentar-a-tag-cBenef-para-o-estado-do-GO?source=search>

- Configuração Códigos de Reflexo

Base p/ calc. = Base ICMS

Alíquota = Alíquota de ICMS

Valor = valor do ICMS

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17480229050519)

**Configurar a TES:**

**Exemplo:**

**Vídeo didático no canal How To da Totvs no Youtube:** *<https://www.youtube.com/watch?v=WOUvZLBvRUU>*

Calcula ICMS = Sim

Livro Fiscal ICMS = Isento

CFOP da operação a ser utilizado

Sit Trib ICM = da operação a ser utilizado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17480182550679)

4 . Pedido de Venda MATA410

Para verificar se os valores serão gravados na CDV acessar na planilha do pedido de venda na aba Lançamento da apuração ->Val Declaratório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17480130024343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17480203532823)

**ATENÇÃO**

Somente será gravada a tabela CDV após emissão da nota fiscal.

É desta tabela que a montagem do XML vai buscar para gerar a tabela para gerar a tag cBenef

## **Caso a tes esteja como:**

Calcula ICMS=Não e o Livro de ICMS estiver como OUTROS ou ISENTO, o código reflexo deve estar desta forma:

**Vídeo didático no canal How To da Totvs no Youtube:**

*<https://www.youtube.com/watch?v=1NGqosady-4&t=9s>*

*<https://www.youtube.com/watch?v=_frSFU_mm2A&t=26s>*

* Para Calcula ICMS= Não e Livro de ICMS = ISENTO

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17480273838231)

* Para Calcula ICMS= Não e Livro de ICMS = OUTROS

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17480229066391)

**Nos casos de redução de base de ICMS como fazer a amarração do código de reflexo:**

Documentação para configurar a redução de base do ICMS:

[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342473--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-de-ICMS](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/360027342473--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-de-ICMS)

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

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=J_2XSvhVe5I>*

O código de reflexo deixe desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17480229078423)

**Para os casos de ICMS Diferido**

Diferimento

[https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS?source=search](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS?source=search)

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=0rYNnvJTgCc>*

Deixe seu código de reflexo desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17480229083543)

**DICA**

Existe uma forma de tratar a FISA140 em vez de código de produto, poderá tratar via grupo de tributação.

Para tratar por grupo de tributação existe o parâmetro MV\_MTCLF3K

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

![GO GRUPOI TRB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19034407562007)

**IMPORTANTE:**

Se a informação estiver gerada CDV e mesmo assim não gera as informações no XML ou causando rejeição de transmissão,  orientamos abrir um chamado com a equipe do **TSS "Nota fiscal eletrônica" para maiores esclarecimentos**.
