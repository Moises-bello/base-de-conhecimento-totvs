---
content_hash: b54e0a161b34681efa1998dafc7559839b59c7a9b7be858e632199d6e1aec015
fetched_at: '2026-06-29T00:11:02.521790+00:00'
page_id: '619146888'
product: rm
source: tdn-rm
title: 11555718 FISCAL01-15628 - SPED Fiscal (EFD ICMS/IPI) - BP-e de Substituição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=619146888
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 11555718 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15628 |

## **02. SITUAÇÃO/REQUISITO**

Conforme manual da rotina (página 168 [http://sped.rfb.gov.br/estatico/30/5EC21565F41BC9D392045D71E5706429186705/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.6.pdf](http://sped.rfb.gov.br/estatico/30/5EC21565F41BC9D392045D71E5706429186705/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.6.pdf "Follow link"))  
Campo 14 (CHV\_CTE\_REF) -

Preenchimento: Quando o campo TP\_CT-e ou BP-e se referir a “BP-e Substituição”,  
informar a chave do BP-e substituído. Nas demais situações o Campo não deve ser preenchido.

## **03. SOLUÇÃO**

Ajuste no campo 14 do Registro D100 para que seja gerado a chave de acesso do BP-e que foi substituído.

Para que seja gerado a chave de acesso do lançamento  de origem é necessário preencher o motivo de referência nos parâmetros do tipo de movimento na etapa Fis - Escrituração 1/2 que irá substituir.

É necessário marcar na CFOP do movimento de substituição na etapa Outros Dados "Possui Documentos Relacionados":

É necessário também selecionar o tipo BP-e "BP-e Substituição"

Caso contrário será apresentado o seguinte erro de validação:
