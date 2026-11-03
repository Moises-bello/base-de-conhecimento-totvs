---
article_id: 360047771974
category: Escrita Fiscal - Impostos - ICMS
content_hash: ef54bbbfa2591ed50e21c7653bd3dcd12cf2d886d1a0aa6e0e156200556ab9dc
fetched_at: '2026-06-28T22:39:24.209979+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importa a TABELA52
  no Protheus para tratamento da tag cBenef
type: support-article
updated_at: '2024-01-24T13:36:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047771974-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importa-a-TABELA52-no-Protheus-para-tratamento-da-tag-cBenef
---

**Dúvida**Como importa a TABELA 52 no Protheus para tratamento da tag cBenef?  
  
**Ambiente**Protheus – Fiscal  – Todas versão 12 do Protheus

**Solução**Para realizar este procedimento deve acessar o site do SPED, entrar em tabelas, segue link: <http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

Ao acessar o site, existe duas opções de escolhas  "Pacote" e "Tabela".

* Na opção de escolha "**Pacote**" **escolha o estado desejado**
* Na opção de escolha "**Tabela**" selecione a TABELA5.2

Segue video Ho

**Vídeo didático no canal How To da Totvs no Youtube:***<https://www.youtube.com/watch?v=ax22ZPjEWIQ>*

Segue print **demonstrativo**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070113874)

Para importar a tabela, siga os passos abaixo:

- Realizar o *download* da tabela 5.2 através do portal do SPED na receita federal (<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>):

- Após realizado o *download*, é necessário renomear a tabela para o nome **"TABELA52.TXT"**.

**\***Caso seu servidor for **Linux** o arquivo deve ser em letra minúscula **"tabela52.txt"** e o caminho interno      deve ser em minúsculo da pasta por exemplo: **protheus\_data/system/...**

- Colocar a tabela dentro da pasta Protheus\_Data

- Executar o Protheus com a opção "U\_IMPSPED":

* Selecionar a pasta onde está o arquivo e **clicar em "Abrir"**
* **Confirmar** a execução para **importação das tabelas**

**Segue exemplo abaixo**

![PR IMPORTAÇ~~AO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19035455420055)

**Após concluir será gravado os códigos na sua tabela CDY**
