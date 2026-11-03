---
content_hash: 26e4d3fc0073e43fde72f84284f4a846dc6ccfc69919ba67efb710f721ef429e
fetched_at: '2026-06-29T00:11:21.100473+00:00'
page_id: '687759347'
product: rm
source: tdn-rm
title: FISCAL01-18059 - DT Processo Envio NF-e - Campos Uso Livre da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18059+-+DT+Processo+Envio+NF-e+-+Campos+Uso+Livre+da+NF-e
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Envio NF-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18059 |

## **02. SITUAÇÃO/REQUISITO**

Alteração no Processo de Envio de NF-e - Campos de Uso Livre

## **03. SOLUÇÃO**

Cadastro:

Preenchimento no Movimento:

Envio da NF-e:

XML

<xml>  
<obsItem>  
<obsCont xCampo="Info Contribuinte">  
<xTexto>Nota de Recolhimento de ICMS Fev/2021</xTexto>  
</obsCont>  
<obsFisco xCampo="IN072009">  
<xTexto>02/2021</xTexto>  
</obsFisco>  
</obsItem>  
<infAdic>  
<infAdFisco>Texto Livre (campo já existe no Movimento)</infAdFisco>  
<infCpl>Texto Livre (campo já existe no Movimento)</infCpl>  
<obsCont xCampo="Info Contribuinte">  
<xTexto>É Gerado por campo complementar e podem existir até 10 campos deste por nota</xTexto>  
</obsCont>  
<obsFisco xCampo="IN072009">  
<xTexto>01/2020</xTexto>  
</obsFisco>  
<obsFisco xCampo="nProtNFeOrigem">  
<xTexto>Protocolo de autorização</xTexto>  
</obsFisco>  
</infAdic>  
</xml>

Disponível a partir da biblioteca 12.1.33
