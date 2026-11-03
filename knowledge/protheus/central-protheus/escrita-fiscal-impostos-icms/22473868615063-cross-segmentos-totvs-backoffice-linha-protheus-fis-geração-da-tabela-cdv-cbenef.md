---
article_id: 22473868615063
category: Escrita Fiscal - Impostos - ICMS
content_hash: 35b8dfa34b0fd3a4a6c32af6f3c11db90d0bd4f9f8cb2fec85655ac3176ff002
fetched_at: '2026-06-28T22:39:25.884221+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Geração da tabela
  CDV "cBenef" para alimentar a tag cBenef para o estado do ES
type: support-article
updated_at: '2024-06-27T14:22:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22473868615063-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-cBenef-para-alimentar-a-tag-cBenef-para-o-estado-do-ES
---

**Dúvida**

Geração da Tabela CDV "cBenef" para alimentar a tag cbenef do estado de ES

**Ambiente**Protheus todas as versões  
  
**Solução**

O tratamento da tag cbenef para o estado de SC devera seguir orientação abaixo:

A TAG cBenef é validada pela UF do emitente, sendo assim para UF de transmissão de nota

Para gerar a tabela CDV realize os seguintes passos:

1. Configure os parâmetros;

* **MV\_ESTADO = ES**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22473868539031)**

* **MV\_GIAEFD = .F.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22473877407895)**

2. Importar os códigos de lançamento da tabela 5.2 do estado do **ES** pelo **U\_IMPSPED** ou **cadastrar manualmente na rotina FISA156 - Códigos de Valores Declaratórios**;

Para importar a tabela, siga os passos abaixo:

**Vídeo didático no canal How To da Totvs no Youtube:** *<https://www.youtube.com/watch?v=ax22ZPjEWIQ>*

Realizar o **download da tabela 5.2** através do portal do SPED na receita federal  
[*http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal*](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22473868548887)

**IMPORTANTE**

* Após realizado o **download**, é necessário renomear a tabela para o nome **TABELA52.TXT**
* **\***Caso seu servidor for **Linux** o arquivo deve ser em **letra minúscula "tabela52.txt"** e o caminho interno deve ser em minúsculo da pasta por exemplo: protheus\_data/system/...
* Colocar a tabela dentro da pasta System do Protheus
* Executar o Protheus com a opção U\_IMPSPED
* Selecionar a pasta onde está o arquivo e clicar em "Abrir"
* Confirmar a execução para importação das tabelas

![Importar tabela 52 ES.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22473868556439)

**Após concluir será gravado os códigos na sua tabela CDY**

Para fazer amarração na rotina "Itens X Cod.val.declaratórios" (FISA140)

Agora deve acessar a rotina FISA140

3. Criar a amarração na rotina **FISA140 - Prod. x Cod.V.Decl.;**

Informar:

* Produto
* CFOP da operação a ser aplicado aquele código
* Cod. Val. Decl (Tabela 5.2 da receita federal)
* CST
* Código de Reflexo conforme a sua necessidade

Exemplo:

**Vídeo didático no canal How To da Totvs no Youtube:** *<https://www.youtube.com/watch?v=WOUvZLBvRUU>*

Após concluir, ir no MATA410 Pedido de venda e realizar inclusão do pedido de venda.

Depois que colocar o cliente, produto, quantidade e valor unitário e total, coloque a tes devidamente configurada e ir em Outras ações, Planilha, Aba lançamento de apuração e clicar em valor declaratório.

Neste momento vai aparecer as informações para tag cbenef

![Geraçao pedido com cbenef ES.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22473868560023)

**ATENÇÃO**

Somente será gravada a tabela CDV após emissão da nota fiscal.

É desta tabela que a montagem do XML vai buscar para gerar a tabela para gerar a tag cBenef

**Caso a tes esteja como:**  
**Calcula ICMS=Não** e o **Livro de ICMS** estiver como**OUTROS** ou **ISENTO**, o código reflexo deve estar desta forma:

Vídeo didático no canal How To da Totvs no Youtube:

*<https://www.youtube.com/watch?v=1NGqosady-4&t=9s>*

*<https://www.youtube.com/watch?v=_frSFU_mm2A&t=26s>*

**Para Calcula ICMS= Não e Livro de ICMS = ISENTO**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22473877420183)

**Para Calcula ICMS= Não e Livro de ICMS = OUTROS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22473877424279)

**Nos casos de redução de base de ICMS como fazer a amarração do código de reflexo:**

Documentação para configurar a redução de base do ICMS:

[*https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342473--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-de-ICMS*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342473--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-de-ICMS)

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

**Vídeo didático no canal How To da Totvs no Youtube:** *<https://www.youtube.com/watch?v=J_2XSvhVe5I>*

O código de reflexo deixe desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22473868570775)

**Nos casos de ICMS Diferido**

Diferimento

*<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS?source=search>*

Vídeo didático no canal How To da Totvs no Youtube: *<https://www.youtube.com/watch?v=0rYNnvJTgCc>*

Deixe seu código de reflexo desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22473868573591)

**DICA**

Existe uma forma de tratar a FISA140 em vez de código de produto, poderá tratar via grupo de tributação.

Para tratar por grupo de tributação existe o parametro MV\_MTCLF3K

MV\_MTCLF3K= 0 tratará por código de produto  
MV\_MTCLF3K= 1 tratará por grupo de tributação  
Segue documentação:

*<https://tdn.totvs.com/pages/releaseview.action?pageId=520651465>*

**Exemplo:**

Se seu produto tem o grupo tributário amarrado como 001

E seu cliente o grupo tributário estiver em branco

A regra da FISA140 deve ter somente o grupo de produto informado = 001 e grupo de cliente em branco

Agora se seu produto tem o grupo tributário amarrado como 001

E seu cliente o grupo tributário estiver AAA

A regra da FISA140 deve ter somente o grupo de produto informado = 001 e grupo de cliente= AAA

![FISA140 por grupo tributario ES.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22473877436311)

**IMPORTANTE:**

Se a informação estiver gerada CDV e mesmo assim não gera as informações no XML ou causando rejeição de transmissão, **orientamos abrir um chamado com a equipe do TSS (nota fiscal eletrônica) para auxiliar.**
