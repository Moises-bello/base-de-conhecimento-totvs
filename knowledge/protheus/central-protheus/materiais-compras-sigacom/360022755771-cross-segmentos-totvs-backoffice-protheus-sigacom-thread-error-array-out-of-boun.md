---
article_id: 360022755771
category: Materiais - Compras (SIGACOM)
content_hash: 49fe0bb2a2a6869a2729509b1eccf4a00a548e45ed22c1961f14f18977d3f5df
fetched_at: '2026-06-28T22:41:10.457038+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - THREAD ERROR array
  out of bounds ( 11 of 9 ) on A103GRAVA(MATA103.PRW) 02/01/2019 09:38:34 line : 12901'
type: support-article
updated_at: '2022-05-16T20:58:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022755771-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-THREAD-ERROR-array-out-of-bounds-11-of-9-on-A103GRAVA-MATA103-PRW-02-01-2019-09-38-34-line-12901
---

**Dúvida**THREAD ERROR array out of bounds ( 11 of 9 ) on A103GRAVA(MATA103.PRW) 02/01/2019 09:38:34 line : 12901  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**O erro ocorre devido a falta dos campos relacionados a região da tabela SF1.

Disponibilizados os campos **UF Origem Transporte (F1\_UFORITR)**, **Município Origem Transporte (F1\_MUORITR)**, **UF Destino Transporte (F1\_UFDESTR)** e **Município Destino Transporte (F1\_MUDESTR)**na aba **Informações Adicionais**do documento de entrada(MATA103) para que sejam fornecidas as informações referentes ao transporte.

Mais informações sobre os campos veja no link: **<http://tdn.totvs.com/display/public/PROT/DOC0055+Tratamento+dos+Campos+F1_UFORITR%2C+F1_UFDESTR%2C+F1_MUORITR+e+F1_MUDESTR>**

**Atenção**

Para criar os campos em releases anteriores ao 12.1.20 será necessário executar o compatibilizador UPDDISTR ([Atualizador de dicionário e base de dados - UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468)) com o dicionário diferencial (SDFBRA), para isso [clique aqui](http://suporte.totvs.com/totvs-tdi-files-maps/mapeamentos/portal-anexos/anexos/zendesk/20190204/TTVFLGP1J004-1549308127899-639825.zip)

Por gentileza, em ambiente de homologação, salve os arquivos anexos na pasta \systemload e siga os procedimentos abaixo para executar o UPDDISTR, afim de verificar se os campos serão criados corretamente.  
  
Antes de rodar o UPDDISTR, crie backup dos arquivos de LOG. (Caso não tenha algum dos arquivos, apenas ignore e apague os que tiver).  
  
1) Dentro da pasta system:  
  
mpupdlog.log  
mpupdlog.fpt  
mpwizard.hlp  
mpwizardhlp.lck  
  
2) Dentro da pasta Appserver:  
  
mpupddistri.tsk  
mppatch.exe   
  
Após efetuar criar o backup dos arquivos, execute o compatibilizador e veja se os campos foram criados.

Todo o processo deve ser executado com backup dos registros e primeiramente em ambiente de **HOMOLOGAÇÃO**.

Após a atualização e execução do UPDDISTR os campos serão criados conforme abaixo:

**F1\_UFORITR**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020107732/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019967851/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019967871/mceclip2.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020107952/mceclip3.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020107972/mceclip4.png)

**F1\_UFDESTR**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020108192/mceclip5.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020108332/mceclip6.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019968371/mceclip7.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019968391/mceclip8.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020108412/mceclip9.png)

F1\_MUORITR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019968511/mceclip10.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020108552/mceclip11.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019968571/mceclip12.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020108592/mceclip13.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019968671/mceclip14.png)

**F1\_MUDESTR**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020108692/mceclip15.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020108732/mceclip16.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019968791/mceclip17.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019968811/mceclip18.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020108852/mceclip19.png)

***Saiba Mais:***

**<http://tdn.totvs.com/display/public/PROT/DOC0055+Tratamento+dos+Campos+F1_UFORITR%2C+F1_UFDESTR%2C+F1_MUORITR+e+F1_MUDESTR>**
