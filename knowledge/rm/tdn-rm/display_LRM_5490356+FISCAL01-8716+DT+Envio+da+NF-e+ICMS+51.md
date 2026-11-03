---
content_hash: b55609bf283e0b650df416cb9963d4e3068e447b70ceefb8788ca86a625edeb8
fetched_at: '2026-06-29T00:10:20.225857+00:00'
page_id: '490311221'
product: rm
source: tdn-rm
title: 5490356 FISCAL01-8716 DT Envio da NF-e ICMS 51
type: documentation
url: https://tdn.totvs.com/display/LRM/5490356+FISCAL01-8716+DT+Envio+da+NF-e+ICMS+51
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Envio da NF-e |
| Ticket: | 5490356 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000071 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar uma operação com Diferimento de ICMS de 100% , as tags referente a base, alíquota, valor do ICMS e valor do ICMS diferido estão sendo levados com valor 0 no XML da NF-e.

## **03. SOLUÇÃO**

Para o Rio de Janeiro no Diferimento 100%, todos campos do ICMS 51 serão preenchidos.

Exemplo de Diferimento 100%

<ICMS51>  
<orig>0</orig>  
<CST>51</CST>  
<modBC>3</modBC>  
<pRedBC>0.00</pRedBC>  
<vBC>100.00</vBC>  
<pICMS>18.00</pICMS>  
<vICMSOp>18.00</vICMSOp>  
<pDif>100.0000</pDif>  
<vICMSDif>18.00</vICMSDif>  
<vICMS>0.00</vICMS>  
<vBCFCP>100.00</vBCFCP>  
<pFCP>2.00</pFCP>  
<vFCP>2.00</vFCP>  
</ICMS51>
