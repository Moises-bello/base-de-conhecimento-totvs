---
content_hash: 2917abe6dcff487f5f5ec88678673b6f240eaf8a3efef86898a9f86223e3557f
fetched_at: '2026-06-29T00:10:51.400430+00:00'
page_id: '567745592'
product: rm
source: tdn-rm
title: 9612871 FISCAL01-13918 DT NFS-e Aparecida de Goiânia/GO - L030 - Valor do ISS
  não informado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=567745592
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Enviar NFS-e |
| Ticket: | 9612871 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13918 |

## **02. SITUAÇÃO/REQUISITO**

Quando é enviada a NFS-e para Aparecida de Goiânia/GO, na situação dos clientes eles tem retenção de ISS (tag issRetido =1) e somente a tag ValorISSRetido deve ser gerada.

Prefeituras que trabalham com o provedor IssNetOnline estão apresentando a rejeição L030, pois o provedor alterou a validação do xml e será necessário um ajuste para não enviar as tags ValorISS e ValorISSRetido na mesma nota.

<tc:IssRetido>1</tc:IssRetido>  
<tc:ValorIss>5.00</tc:ValorIss>  
<tc:ValorIssRetido>5.00</tc:ValorIssRetido>

## **03. SOLUÇÃO**

Na geração do XML de NFS-e para Aparecida de Goiânia/GO que utiliza o IssNetOnline, foi alterado a geração das tags ValorISS e ValorISSRetido. Caso:  
- a tag ISSRetido seja gerada com valor 1 a tag ValorISSRetido será preenchida e a tag ValorISS não será gerada.  
- a tag ISSRetido seja gerada com valor 2 a tag ValorISS será preenchida e a tag ValorISSRetido não será gerada.
