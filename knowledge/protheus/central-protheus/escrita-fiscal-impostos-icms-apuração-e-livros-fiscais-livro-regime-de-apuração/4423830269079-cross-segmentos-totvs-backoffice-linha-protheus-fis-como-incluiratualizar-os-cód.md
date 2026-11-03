---
article_id: 4423830269079
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 0585753b8eef746c5f93293ffe769c054627bdf2316ef2c1cb0ccbd3793e64fa
fetched_at: '2026-06-28T22:39:22.162386+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como incluir/Atualizar
  os códigos da tabela: 5.5- Tabela de Tipos de Utilização dos Créditos Fiscais -
  ICMS - Tabela CE7?'
type: support-article
updated_at: '2022-02-11T20:34:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4423830269079-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-incluir-Atualizar-os-c%C3%B3digos-da-tabela-5-5-Tabela-de-Tipos-de-Utiliza%C3%A7%C3%A3o-dos-Cr%C3%A9ditos-Fiscais-ICMS-Tabela-CE7
---

**Dúvida**

Como incluir/Atualizar os códigos da tabela: 5.5- Tabela de Tipos de Utilização dos Créditos Fiscais - ICMS - Tabela CE7?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

Para alimentar ou atualizar a tabela 5.5- Tabela de Tipos de Utilização dos Créditos Fiscais é necessário seguir os seguintes passos.

1. Acesse site da receita:  
[http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscalhttp://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)

2. Selecionar a tabela 5.5 e Unidade Federativa desejada

3. Baixar a Tabela de Tipos de Utilização dos Créditos Fiscais (Arquivo TXT)

4. Coloque o Arquivo TXT dentro da pasta System

5. Execute o compatilibilizador U\_IMPSPED

6. Durante o processo será feita pergunta (deseja efetuar a importação das informações cadastrais do SPED?) selecione botão SIM

7. selecione a pasta que esta o arquivo TXT (System)

Após continuar processo será exibido relatório com a tabela CE7 será atualizada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4423829370007/mceclip0.png)

A informação com os respectivos códigos pode ser visualizada através da rotina Tipos de Utilização de Créditos (FISA35)

***Atualizações // Sped // Tipos de Utilização de Créditos***

**Assuntos relacionados:**

**SPEDFISCAL - Registro 1200/1210 ( Controle de Crédito Físcais - ICMS )**

<https://tdn.totvs.com/pages/viewpage.action?pageId=338381972>
