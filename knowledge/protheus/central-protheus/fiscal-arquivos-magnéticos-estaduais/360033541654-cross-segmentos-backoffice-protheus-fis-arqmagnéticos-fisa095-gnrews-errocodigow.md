---
article_id: 360033541654
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 0f8a89445b32d982ee41c36e442fdc0bb06ae7aecbaed65c970ee54d378d2c0c
fetched_at: '2026-06-28T22:42:10.905067+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - FISA095 - GNREWS
  <Erro><Codigo>WSCERR048</Codigo> NA TRANSMISSÃO DA GUIA
type: support-article
updated_at: '2022-08-17T20:30:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033541654-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-FISA095-GNREWS-Erro-Codigo-WSCERR048-Codigo-NA-TRANSMISS%C3%83O-DA-GUIA
---

**Dúvida**Como corrigir o erro GNREWS <Erro><Codigo>WSCERR048</Codigo> na transmissão da guia?  
  
 **Ambiente**Protheus  – A partir da versão 11.80  
   
**Ocorrência**ERRO: Foram transmitidas 0 GNRE(s) em 00:01

A(s) GNRe(s) abaixo foram recusadas, verifique a rotina 'Monitor' para saber os motivos.

PRICM000000061 - <Erro><Codigo>WSCERR048</Codigo><Descricao>WSCERR048 / SOAP FAULT ( POST in <https://www.testegnre.pe.gov.br/gnreWS/services/GnreConfigUF> ) : [java.rmi.RemoteException: Erro ao gerar XML de resposta [DETAIL] ]   
ADVPL WSDL Client 1.120703 / TOTVS MSSQL Sped on 20190719 09:28:01   
</Descricao></Erro>

**Solução**O erro acontece porque o campo **F6\_CODREC** está vazio na tabela **SF6** (guia de recolhimento) .  
Esse campo é obrigatório para a transmissão.   
  
O código tem que ser preenchido conforme lista de códigos por UF disponíveis no portal da GNRE:  
<http://www.testegnre.pe.gov.br/gnre/portal/automacao.jsp#>

![](https://ci4.googleusercontent.com/proxy/Lekf-_otFXvLRr0gdFlT5jS6Kkjc9vAst8-XDVBRDLIY91W8psCCddQhZIRni3OQ--0sJCuwaPyDPV6aHwhTyTdugdQygajRoRIWkbrVhuPHS7zj9xVlUPYVnVBOt9lwsvqv6C3XixqRsXBVB3xCeLt5CcFu7IE_je0=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/eFP2u2KV2iLqy6IXVgq8EI6QB/?name=inline-534129716.png)

 Preencha o campo na Guia e faça novamente a transmissão.
