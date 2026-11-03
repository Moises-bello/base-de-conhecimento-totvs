---
article_id: 360007160131
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 34bd53fdda0de3bdeda910559b7591b0eaeaf33a2c0d9b913daadfc6a7cc123b
fetched_at: '2026-06-28T22:40:48.960256+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: MP - ECF - Error log Index not found. on SALDOPLANREF.
type: support-article
updated_at: '2021-04-28T22:09:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007160131-MP-ECF-Error-log-Index-not-found-on-SALDOPLANREF
---

**Dúvida**

Error log ao executar a escrituração ECF.

CVD260: SetOrder - Index not found. on SALDOPLANREF(CTBS011.PRW) 18/06/2018 15:03:52 line : 5386  
   
 **Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
   
**Solução**Verifique o Índice da tabela CVD conforme padrão abaixo :

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007430432/mceclip1.png)

Certifique-se que realizou o procedimento de atualização conforme abaixo:

1. Acessar o portal do cliente e realize o download do ultimo dicionário completo e diferencial disponibilizado.

Ex.:

* 18-01-12-BRA-DICIONARIOS\_COMPL\_12\_1\_17 - Completo
* 18-01-12-BRA-DICIONARIOS\_DIF\_12\_1\_17 - Diferencial

Obs.: Lembrando que em caso de dicionários para outros países, deve-se realizar o download do pais respectivo.

2. Realizar o backup do seu ambiente (dicionário, RPO e dados)

3. Excluir os arquivos de log abaixo:

Dentro da pasta system:

mpupdlog.log  
mpupdlog.fpt  
mpwizard.hlp  
mpwizardhlp.lck

Dentro da pasta Appserver:

mpupddistri.tsk

4. Copiar os arquivos do dicionário para a sua pasta **systemload**

**5. Realizar a execução do compatibilizador UPDDISTR.**
