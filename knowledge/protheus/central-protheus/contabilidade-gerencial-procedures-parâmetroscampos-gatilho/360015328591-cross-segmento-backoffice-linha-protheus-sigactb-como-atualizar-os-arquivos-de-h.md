---
article_id: 360015328591
category: Contabilidade Gerencial - Procedures, Parâmetros,Campos, Gatilho
content_hash: d6938bbbb84b1934dba8b64a4aa9d653576a759195059cffdd9bb72dda1b6d0c
fetched_at: '2026-06-28T22:41:01.425612+00:00'
product: protheus
section_id: 1500001537361
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB Como atualizar os arquivos
  de Help dos Campos
type: support-article
updated_at: '2022-07-18T20:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015328591-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-atualizar-os-arquivos-de-Help-dos-Campos
---

**Dúvida**

Como atualizar os arquivos de Help dos Campos  
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus  – Contabilidade – A partir da versão 11.80 **Solução**

Segue abaixo procedimento para atualizar ou recriar os Helps de Campos do Protheus:

Primeiramente faça o download do arquivo.

* [Clique aqui](http://tdn.totvs.com/display/public/PROT/Atualizar+Help+de+Campos)

Após baixar o pacote, descompacte os arquivos .txt para dentro da pasta **Systemload** do Protheus.

Para atualizar, pare o serviço do Protheus, acesse a pasta **System** e:

- Para o help de campos em português, apague o arquivo **sigahlp.hlp**.

- Para o help de campos em inglês, apague o arquivo **sigahle.hle**.

- Para o help de campos em espanhol, apague o arquivo **sigahls.hls**.

Reinicie o serviço do Protheus. Ao acessar o sistema, o **help** será recriado a partir do **.txt** descompactado. Uma imagem de alerta será exibida durante a atualização dos arquivos:

![](http://tdn.totvs.com/download/attachments/271414846/Help_Campos.png?version=1&modificationDate=1486573706000&api=v2)
