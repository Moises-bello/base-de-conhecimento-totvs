---
content_hash: 99c0f377017e5e29d9d103adb4edd39ca1996e9379798ef3375dad2c68f3484c
fetched_at: '2026-06-29T00:08:52.671435+00:00'
page_id: '342299079'
product: rm
source: tdn-rm
title: 1725910 FISCAL01-2553 DT Envio NF-e tag vAFRMM
type: documentation
url: https://tdn.totvs.com/display/LRM/1725910+FISCAL01-2553+DT+Envio+NF-e+tag+vAFRMM
version: 2
---

# Envio da NF-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio da NF-e |
| **Situação/Requisito:** | Ao efetuar o envio de uma NF-e importação , onde a via de transporte é 1=Marítima a mesma está sendo rejeitada:  330/Rejeicao: Informar o Valor da AFRMM na importacao por via maritima  Foi verificado que o problema está ocorrendo pois não foi montado a tag <vAFRMM>0</vAFRMM> no XML |
| **Solução/Implementação:** | Envio da NF-e  Quando a via de transporte for 1 - Marítima e o campo vAFRMM não estiver preenchido então no envio  da NF-e a tag "vAFRMM" será preenchida com valor "0". |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | FIS000071 |
| **Documento de Referência:** | Não se Aplica |
