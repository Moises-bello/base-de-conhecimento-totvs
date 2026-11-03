---
article_id: 29540366968727
category: Financeiro
content_hash: 61d8bb7114284812a7d9199e07ccc8d922cb10697035f99f27dbf77838046766
fetched_at: '2026-06-28T22:38:00.997391+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - O que fazer quando
  ocorre lentidão no sistema
type: support-article
updated_at: '2025-10-10T20:58:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29540366968727-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-O-que-fazer-quando-ocorre-lentid%C3%A3o-no-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29540366951063) Tempo aproximado para leitura: **00****:010 min**

**Dúvida**O que fazer quando ocorre lentidão no sistema?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33  
  
**Solução**

A lentidão pode ser causada por diversos fatores. No entanto, para iniciarmos a análise de forma adequada, é imprescindível que o sistema esteja atualizado, a fim de validar se houve alguma correção relacionada à lentidão reportada.

* Caso o ambiente esteja desatualizado, por favor, efetuar atualização conforme artefatos disponibilizados no portal do cliente:

[**Pacote Acumulado**](https://suporte.totvs.com/portal/p/10098/download?e=1123867)

[**Pacotes LIB**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)  
[**Pacotes DBAccess**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)  
[**Binário AppServer**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
[**Binário SmartClient / WebApp**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)

* **Qual o tempo de processando até a finalização da rotina?**
* **O problema ocorreu após alguma atualização, se sim, qual?**
* **Quantos registros aproximados estão sendo processados?**

---

#### Além das informações referente ao processo, necessitamos de algumas informações técnicas para análise.

* **Efetue os procedimentos abaixo para geração dos Logs para análise:**  
  + Adicione a chave **FWTRACELOG=1** no **AppServer.ini** no ambiente utilizado pelo serviço;
  + Renomeie o **Console.log** dos serviços;
  + Insira na seção **[GENERAL]** as chaves:
    - TLPP\_REST\_LOG=1
    - REST\_LOG\_LEVEL=7
    - REST\_LOG\_STRINGSIZE=0
    - LOGHTTPFUNCS=1
    - TLPP\_REST\_LOG=1
    - CONSOLEMAXSIZE=300888999
    - CONSOLELOG=1
  + Na seção **[HTTPV11]** insira a chave:
    - LOGPROFILE=1
  + Na seção do ambiente **[ENVIROMENT]** insira a chave:
    - FWLOGMSG\_DEBUG=1
    - FWTRACELOG=1
* **Favor executar o MallocIO e nos encaminhar** ***Print*** **da tela conforme documentação abaixo.**
  + <https://tdn.totvs.com/display/public/PROT/MallocIO>
* **Nota:**  
  Será gerado também Log no diretório do **AppServer,** exemplo:  
  **appserver\_[data hora].log ou appsrvlinux\_[data hora].log**
* **Reproduza o erro e encaminhe os logs e o console.log do serviço, para análise.**  
    
  **LogProfiler do processo:** <https://tdn.totvs.com/pages/releaseview.action?pageId=243638663>   
  **DBTrace do processo:** [https://tdn.totvs.com/pages/releaseview.action?pageId=274851061](https://tdn.totvs.com/pages/releaseview.action?pageId=274851061%28esse)   
  **Extrato de versão:** [RH - Linha Protheus - GPE - Como gerar extrato de versão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410028522135-RH-Linha-Protheus-GPE-Como-gerar-extrato-de-vers%C3%A3o?source=search)

Caso a lentidão persista após as atualizações, solicitamos que seja realizado o levantamento das informações descritas no artigo e que estas sejam encaminhadas ao suporte para análise.

**Saiba mais**

[Framework - Linha Protheus - Lentidão no Protheus 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515552-Framework-Linha-Protheus-Lentid%C3%A3o-no-Protheus-12)
