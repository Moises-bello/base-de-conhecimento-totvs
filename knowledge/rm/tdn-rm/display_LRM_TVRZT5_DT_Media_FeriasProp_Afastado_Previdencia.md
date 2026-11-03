---
content_hash: 01869f13f3a7f0774fcde9f7a110d60eb904f62e7ae4d0460796423bb78d35b9
fetched_at: '2026-06-29T00:08:19.238391+00:00'
page_id: '266981227'
product: rm
source: tdn-rm
title: TVRZT5_DT_Media_FeriasProp_Afastado_Previdencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TVRZT5_DT_Media_FeriasProp_Afastado_Previdencia
version: 109
---

# PERIODO DE MÉDIA DE FÉRIAS PROPORCIONAIS PARA AFASTADO PELA PREVIDÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | Cálculo da média de férias proporcionais na rescisão não estava considerando o periodo correto quando funcionário teve um longo periodo de afastamento pela previdência, pegando dois periodos aquisitivos de férias, sendo um vencido e outro proporcional.  O erro só ocorria quando o total de dias de afastamento dava mais de 180 dias, mas quando considerado por periodo aquisitivo não somava 180 em nenhum dos dois. Ou seja, não causava perda de nenhum periodo aquisitivo de férias. |
| **Solução/Implementação:** | Ajuste na media de férias proporcionais na rescisão para pegar o periodo correto de apuração, quando funcionário tem um longo periodo de afastamento pela Previdência. |
| **Chamados relacionados:** | *TVRZT5* |

divs
