---
article_id: 360024942253
category: Gestão de Transportes (TMS)
content_hash: 1bbfd677e98f928ed18c9145416d1a7749187082340c314b63b713d70f4e0d56
fetched_at: '2026-06-28T22:45:32.438058+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Principais parâmetros CT-e
type: support-article
updated_at: '2025-06-06T17:19:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024942253-Log%C3%ADstica-Linha-Protheus-TMS-Principais-par%C3%A2metros-CT-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23368118046871)*** Tempo aproximado para leitura: **00:02:10 min****Dúvida**Quais são os principais parâmetros para emissão do **CT-e - Conhecimento de Transporte Eletrônico**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Os principais parâmetros relacionados a geração do **CT-e** são:

* **MV\_TMSCTE -** Habilita o uso do **CT-e;**
* **MV\_CODREG** - Código do Regime de Tributação, que deverá ser preenchido com **1, 2 ou 3 de acordo com regime de tributação da empresa.**
* **MV\_CTECAN -** Habilita validação da exclusão do **CT-e** autorizado pela **SEFAZ - Secretaria da Fazenda**, onde **.T. - Somente autorizado pela SEFAZ e .F. - Não valida.**
* **MV\_CTEEXC -** Prazo em dias para cancelamento do **CT-e** após ser autorizado;
* **MV\_CTEEXCH-** Prazo em horas para cancelamento do **CT-e** após ser autorizado;
* **MV\_CTEVFRE -** Determina qual valor será utilizado no *XML* do **CT-e** referente ao componente de frete na *tag* **<vComp>** - .**T. - Valor Sem Imposto** e **.F. - Valor Com Imposto;**
* **MV\_CTEVPRE -** Determina qual valor será utilizado no *XML* referente a *tag* **Total da Prestação <vTPRest>** -  **.T. - Valor sem impostos** e **.F. - Valor com impostos;**
* **MV\_ESPECIE -** Contém tipos de documentos fiscais utilizados na emissão dos documentos de saídas. O Preenchimento deste parâmetro é **obrigatório** para o correto uso do **CT-e**, exemplo de preenchimento, 001=CTE, onde, 001 é serie do **CT-e** e CTE a espécie. Se a serie e espécie do **CT-e** não estiver contida neste parâmetro, teremos impactos na transmissão do cancelamento;
* **MV\_HORARMT -** Horário gravado na tabela **SF2**, campos **F2\_EMISSAO** e **F2\_HORA,** Exemplo de preenchimento - **1 - Horário do SmartClient*,* 2 - Horário do servidor e 3 - Fuso horário da filial corrente;** Os parâmetros de configuração de data e hora do **CT-e**, devem ser configurados exclusivos por filial;
* **MV\_HVERAO -** Define se o local físico do servidor está em horário de verão;
* **MV\_HVERAOF -** Data de término do horário de verão;
* **MV\_HVERAOI -** Data de início do horário de verão;
* **MV\_TMSHRFL -** Define filiais que não aderiram ao horário de verão e/ou possuem diferença de fuso;
* **MV\_TMSHRVR -** Define se está no período de horário de verão;
* **MV\_TMSUFPG -** Indica o estado que será utilizado na escrituração dos documentos de transporte, sendo que **T - Pagador do Frete** e **F - Destinatário da Mercadoria**;
* **MV\_TMSANTT -** Número do registro na **ANTT - Agência Nacional de Transportes Terrestres** que será utilizado no *XML* do **CT-e** referente a *tag* **<RNTRC>;**
* **MV\_ESTADO -** Sigla do estado de onde a filial emissora do **CT-e** esta localizada. Para efeito de cálculo de **ICMS - Impostos Sobre Circulação de Mercadoria e Serviços,** este parâmetro deve ser exclusivo por filial;
* **MV\_URLQCOD -** Informar a *URL* para pesquisa via *QR Code* do **CT-e**. Este parâmetro deve ser preenchido conforme as orientações do *link* [Logística - Linha Protheus - TMS - Tag infCteSupl no CT-e versão 3.00A.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035596554-Log%C3%ADstica-Linha-Protheus-TMS-Tag-infCteSupl-no-CT-e-vers%C3%A3o-3-00A)
