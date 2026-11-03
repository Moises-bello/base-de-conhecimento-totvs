---
article_id: 360024979111
category: ADVPL - Classe e Função
content_hash: ffa2a661c6252972e42df70f32bd348ea6f5e7835066f308cfb4f2fc6b72cf49
fetched_at: '2026-06-28T22:40:20.495797+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Manipulações em
  SX's em customizações no versão P12.1.23
type: support-article
updated_at: '2022-03-16T15:31:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024979111-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Manipula%C3%A7%C3%B5es-em-SX-s-em-customiza%C3%A7%C3%B5es-no-vers%C3%A3o-P12-1-23
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Gostaria de saber como fazer o acesso direto utilizando a função Posicione ou DbSeek em SX's em Customizações no versão P12.1.23, pois o Dicionário de Dados do Protheus será inicializado diretamente no Banco de Dados.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão P12.1.23  
  
**Solução**A partir da Release abaixo ao invés de ser utilizado na pasta System, as SXs estarão centralizadas dos dados no SGBD essa alteração visa proporcionar maior agilidade na leitura do dicionário  
**Release:** 12.1.23  
**LIB:** versão 20180820  
**Binário:** Build 7.00.131227A - Jul 27 2018   
**DBAccess:** Build 20171117-20180412  
  
Para acessar essas tabelas foram criadas alguma classes genérica para leitura das tabelas

**[Classes](http://tdn.totvs.com/display/PROT/Classes)**

Para tabela Sx5 temos a função

**[X5Descri - Descrição da tabela](http://tdn.totvs.com/pages/releaseview.action?pageId=6815022)**

**Saiba mais**

* É proibido abrir o arquivo de Empresa(SIGAMAT) com DBUseArea, deve-se utilizar OpenSm0 ou OpenSm0Excl;
* É proibido abrir os arquivos de dicionário com DBUseArea.

**[Migração do Dicionário de Dados para o Banco de Dados](http://tdn.totvs.com/pages/releaseview.action?pageId=360450442)**

* O dicionário de dados pode ser alterado diretamente por SQL?  
  Não pode ser alterado nem pelo banco e nem pelo fonte; apenas pelo configurador do Protheus.

**[Release 12.1.23 - Expedição em Fevereiro/2019 - FAQs](http://tdn.totvs.com/pages/viewpage.action?pageId=461919278)**
