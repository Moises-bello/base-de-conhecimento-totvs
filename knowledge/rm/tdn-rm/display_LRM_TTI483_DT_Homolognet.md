---
content_hash: fca05dfebb01617c9ab9b493e77e8aa74b59ca6eca4189908e5a7c29192431f9
fetched_at: '2026-06-29T00:06:10.357398+00:00'
page_id: '203762241'
product: rm
source: tdn-rm
title: TTI483_DT_Homolognet
type: documentation
url: https://tdn.totvs.com/display/LRM/TTI483_DT_Homolognet
version: 1
---

# Homolognet

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Homolognet* |
| **Situação/Requisito:** | Ao consultar rescisão emitida via rotina homolognet, é apresentada a seguinte inconsistência:  181 - A informação referente ao salário líquido foi removida pois a data de afastamento não se encontra entre o primeiro e o sexto dia do mês |
| **Solução/Implementação:** | Otimizada rotina homolognet, implementada regra para que a tag VLSalarioLiquidoMesAnteriorRescisao só vá para o arquivo caso a data de  afastamento esteja entre o primeiro e o sexto dia do mês |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTI483 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
