---
article_id: 360022574811
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 1e21e58cc1a5cff0e0d6c05216b13428d5ca1b9ab968d4d9a3f22bdb714b961f
fetched_at: '2026-06-28T22:40:45.757916+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'MP - SIGACTB : CTBS001 invalid field name in Alias CS0->CS0_IDBLK on MSMGET:MONTAARRAY(MSMGETPR.PRW)'
type: support-article
updated_at: '2021-04-28T22:08:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022574811-MP-SIGACTB-CTBS001-invalid-field-name-in-Alias-CS0-CS0-IDBLK-on-MSMGET-MONTAARRAY-MSMGETPR-PRW
---

**Ocorrência**

Ao acessar a rotina de Escrituração o sistema gera error log

THREAD ERROR ([11587], Admin,xxxtr) 21/12/2018 11:14:04   
invalid field name in Alias CS0->CS0\_IDBLK on MSMGET:MONTAARRAY(MSMGETPR.PRW) 15/05/2018 17:39:45 line : 489   
   
 **Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão P12  
   
 **Causa**

Situação é apresentada devido ao  campo CS0\_IDBLK

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019730152/mceclip1.png)  
   
 **Solução**

**Baixar o Pacote e Dicionário através do link**[Pacote de Atualização / Correção - ECD 2018 - Exercício 2017](http://tdn.totvs.com/pages/releaseview.action?pageId=331864819)

**Passo 1** - Baixar os artefatos de atualização ao lado

**Passo 2** - Copiar os arquivo SDFBRA.TXT para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e copia do arquivo novo)

Importante

Você deve baixar tanto o arquivo de dicionário completo (SXSBRA.TXT, por exemplo) quanto o dicionário diferencial (SDFBRA.TXT, por exemplo), e descompactá-los na pasta Systemload. Embora a atualização de release utilize apenas o arquivo diferencial, o arquivo completo também deve ser baixado para a pasta, pois futuramente, quando for criar uma nova empresa ou filial, por exemplo, o arquivo que será utilizado será o COMPLETO.

Maiores informações para download dos arquivos no link: [Atualizar o Dicionário de Dados do Protheus 12](http://tdn.totvs.com/pages/releaseview.action?pageId=271415266)

**Passo 3** – Aplicar  pacote referente ao ECD no RPO

**Passo 4** - Excluir os arquivos de log abaixo:

Dentro da pasta system:

* mpupdlog.log
* mpupdlog.fpt
* mpwizard.hlp
* mpwizardhlp.lck

Dentro da pasta Appserver:

* mpupddistri.tsk

**Passo 5** - Realizar a execução do UPDDISTR em seu ambiente: Atualizador de dicionário e base de dados - UPDDISTR

**Passo 6** - Proceder com o processo de cheklist descrito no link: CheckList - ECD / ECF

**Passo 7** - Proceder com o processo do layout 6.0 conforme link: ECD - Notas Explicativas - Layout 6.0

Saiba mais :

[ECD\_SPED\_CONTABIL Bloco K](http://tdn.totvs.com/display/public/PROT/ECD_SPED_CONTABIL+Bloco+K)
