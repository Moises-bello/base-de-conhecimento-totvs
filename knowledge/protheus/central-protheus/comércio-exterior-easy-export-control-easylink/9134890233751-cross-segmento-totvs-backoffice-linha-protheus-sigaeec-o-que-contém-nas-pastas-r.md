---
article_id: 9134890233751
category: Comércio Exterior - Easy Export Control - Easylink
content_hash: 6a24be880396e4944eb1185fa9ddd4b1355e0d3ee266c0aaa7cf0e9acea88350
fetched_at: '2026-06-28T22:36:38.202273+00:00'
product: protheus
section_id: 1500001538261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEEC- O que contém nas
  pastas Report.zip, Rdmakes.zip e Config.zip do pacote acumulado do Comex, qual a
  sua finalidade?
type: support-article
updated_at: '2024-05-29T11:57:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9134890233751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-O-que-cont%C3%A9m-nas-pastas-Report-zip-Rdmakes-zip-e-Config-zip-do-pacote-acumulado-do-Comex-qual-a-sua-finalidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23808986942231)Tempo aproximado para leitura:**00:05:00 min** **Dúvida**No pacote acumulado do Comex contém as pastas Report.zip, Rdmakes.zip e Config.zip, qual a sua finalidade?   
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus) -*Easy Export Control*- Todas as versões  
  
**Solução****Report.zip -** Arquivos para impressão de documentos, para compilação de impressão ou customização de relatórios.   
***Rdmakes* Padrão -** Para atualização dos modelos de customização (*rdmakes* padrão) utilizados para impressão de documentos e complemento de algumas funcionalidades dos módulos de Importação e Exportação, extraia o arquivo "***rdmakes.zip***" no diretório de customizações do ambiente.  
**Config.zip -**Contém os arquivos Avlinks, arquivos .RPTs, integrador DUE (*Siscomex web*) e instalador AVGXML2DBF.  
**Arquivos .RPT -** são artefatos para impressão de documentos - Pasta Crystal  
  
**Layouts de Integração Easylink- *Avlinks***Para clientes que utilizam o módulo de Exportação ou o módulo Siscoserv integrado ao módulo financeiro do Protheus é imprescindível a atualização dos arquivos .XML contidos no pacote "config.zip".  
Esses arquivos possuem configurações atualizadas para as integrações e devem ser atualizados para contemplar as últimas atualizações.  
  
**Aviso**Os arquivos devem ser atualizados no diretório do Easylink, definido pelo parâmetro "MV\_AVG0135", cuja definição padrão é: \comex\easylink.  
  
**Aplicativos Complementares**No arquivo "config.zip" estão contidos os programas de integração com os Sistemas do Governo, cujos arquivos devem ser atualizados no diretório do SmartClient.  
São eles:  
**tr-sw-web-solution-due.jar:** Programa de integração com o Portal Único para registro de DUE (Declaração Única de Exportação).  
**tr-sw-web-solution-siscomexweb.jar:** Programa de integração com o Siscomex Importação WEB para registro de DI (Declaração de Importação) e LI (Licença de Importação).

* **AVGXML2DBF** - Instalador para impressão de documentos do Crystal.
* **Crystal DLLs**- DLLs de impressão do Crystal.

**Saiba mais**  
[EEC0006\_Documento\_de\_Instalação\_AVGXML2DBF\_e\_DLLs\_Crystal](https://tdn.totvs.com/pages/releaseview.action?pageId=271413885)  
[Pacotes de Atualizações - Comércio Exterior - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=526987588)
