---
content_hash: 3c00cb2ee913c5f5a70124591351e5a7d94c014a726b55174dfbcb3566be0821
fetched_at: '2026-06-29T00:08:20.222068+00:00'
page_id: '268572320'
product: rm
source: tdn-rm
title: TVZPOQ_DT_Parametrizador
type: documentation
url: https://tdn.totvs.com/display/LRM/TVZPOQ_DT_Parametrizador
version: 109
---

# PARAMETRIZADOR - RM PORTAL - DEMONSTRATIVO DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parametrizador* |
| **Situação/Requisito:** | Ao informar um número de período inicio maior que um número de período final, o sistema apresenta mensagem informando que está incorreto. Porém no Delphi não era realizado dessa forma. |
| **Solução/Implementação:** | Ajustar o sistema para não validar o número do período. Pois somente deve apresentar a mensagem quando o mês/ano inicio for igual ao mês/ano final. |
| **Chamados relacionados:** | TVZPOQ |

divs
