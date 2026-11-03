---
article_id: 360024994032
category: TAF - REINF
content_hash: 79141dcd9bd3ccb67ce99f99441c25ade34ed42c3f23a4fb1c5b3d7061a86924
fetched_at: '2026-06-28T22:41:34.714414+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Mensagem "Falha no processamento"
  na rotina de Processamentos
type: support-article
updated_at: '2024-07-10T19:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024994032-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Mensagem-Falha-no-processamento-na-rotina-de-Processamentos
---

**Ocorrência**No módulo TAF, após atualização disponibilizada para correção do erro 609 - Código invalido, ocorre o erro "Falha no Processamento"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - À partir da versão 12.1.33 e superiores  
  
**Causa**Esse incidente ocorre, devido alguma falha ou inconsistência na parametrização TAF após atualização dos fontes relacionado a integração e rotinas de negócios ou quando as informações do banco de dados e conexão ODBC/DBAccess são alteradas.  
  
**Solução**Para solucionar essa ocorrência, basta que execute o Wizard de configuração TAF:

1. Acesse o TAF, vá em **atualizações** > **Configs. TAF** > **Wizard Config. TAF**:

Execute o Wizard até o final.

![](https://ci3.googleusercontent.com/proxy/McmJW52SVBH7MAk_RzMd_A0Ytsvc251w5YOPUjcfVdiLgixPIsZBcu7XW9RkM3Ro-yppasuCocGrpbDLguQ5xP4MvNKMjD-m0KcCETDHyyQhdVrbadPCjskEnrFvizDWS9-ArKjL5YhAVjIw5ofpP3fUMoP1FQ6sWBjF5NJm6RcM-eUSNOUAAbkI7PXBiu9E4nmqyQ=s0-d-e1-ft#http://tdn.totvs.com.br/download/attachments/364910096/image2018-5-3_15-10-4.png?version=1&modificationDate=1527214040000&api=v2)

2. No passo abaixo, atente-se a informar corretamente os parâmetros de ambiente, onde está configurado o banco de dados do TAF. Estes dados podem ser obtidos a partir do arquivo appserver.ini do próprio TAF, conforme segue:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023785432)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023785712)**

![](https://ci4.googleusercontent.com/proxy/K43kHSirI09ju6YkGnx8Th3NI8AqnlRudIFcS-S8jEqV1iSucNfZ-PRcXeG_18znwGMbLf6mwyXH9-Mmz-Gph23SoeCqDRLr2Oe-MBxospmLcggobiwn_b5hWUWQHEXDHAykIun07WuOcXCyKowcPWXSMYyWRfClzc7SsiFLM7iRUxKBPMlQsuVQxEusgaP2wMmrMk0=s0-d-e1-ft#http://tdn.totvs.com.br/download/attachments/364910096/image2018-5-3_15-11-54.png?version=1&modificationDate=1527214039000&api=v2)

![](https://ci4.googleusercontent.com/proxy/rcey6iV0d9mQK5-YuFqUCkF9nT2Kd5n4WAmv6zF4uySQtEj6zB__mW1g4LNN19BMpQigKE3ouVkbejgnKBwdiYdBJQf3a-BLxscx2WtAy4YKs8l_whbcF5m0Ip0H83MEVgSUl3wkVbYvV_te3DcvLdlNMnbvT85PXCvrSdDL2uZ9bOX-KEO8diziZH9SO2p7WaeUCAk=s0-d-e1-ft#http://tdn.totvs.com.br/download/attachments/364910096/image2018-5-3_15-49-45.png?version=1&modificationDate=1527214039000&api=v2)

![](https://ci3.googleusercontent.com/proxy/-FMmVCMVj858SLO5bv1egco4z-bZhevsspjuUxACXEYSS_7XnqimXVbcgy9jQ6v3Z95cPUooGyRrRGL-FOwD95upu1IDsONuERy1C7Qk_RCik4ffywO2Upd3JwwQ7W_SffNfhKfy3VA40oLSuFXUh8Xfw8HlkZL6_Oatl3TN3uuNhH8yklGaD0VSA7ENr_ooayWtSxc=s0-d-e1-ft#http://tdn.totvs.com.br/download/attachments/364910096/image2018-5-3_15-50-55.png?version=1&modificationDate=1527214039000&api=v2)

![](https://ci6.googleusercontent.com/proxy/Kn7aNDZ_abNFkdTnQQfGgbovLwGOA-DJRg1XxXfNha0VxfRgOpCscFRnHq3W3dcP4Mx32T1-jnMKe-yOWYIvfgW8TIpBZYEXralDnSukNQgtrL-LSOR2SQ77RvCOyI2dH_xgLAW0x95w3cORCqrqZn3fVrBlPdrxnjmaMiiDWN7LDjkwZRetOOkMURKBreMBllUPgKg=s0-d-e1-ft#http://tdn.totvs.com.br/download/attachments/364910096/image2018-5-3_15-50-46.png?version=1&modificationDate=1527214039000&api=v2)
