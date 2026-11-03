---
content_hash: 4a3852b13b000966a5a2de6c34e0c11e2c470691b8c6b000013fc89b4db807b6
fetched_at: '2026-06-29T00:08:19.502928+00:00'
page_id: '267791065'
product: rm
source: tdn-rm
title: TVWIDA_DT_GRRF_Situacao_V
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWIDA_DT_GRRF_Situacao_V
version: 115
---

# GERAÇÃO DA GRRF

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração GRRF* |
| **Situação/Requisito:** | *Cliente informa que ao gerar a GRRF para funcionários que se encontram em situação V - Aviso prévio, os mesmos não estão sendo levados no arquivo.*  *O situação acontece, pois a situação V - Aviso prévio , era utilizada no RMDos, para indicar que o funcionário se encontrava em aviso prévio, porém esta situação não é tratada mais pelo sistema, e hoje existe somente para compatibilidade para atender migrações do RMDos para o RMLabore.* |
| **Solução/Implementação:** | *Foi ajustado o sistema para que não liste mais no campo de código de situação a situação V - Aviso prévio, fazendo com que o usuário informe o funcionário nesta situação, fazendo assim com que ele não seja levado nas rotinas do sistema.* |
| **Chamados relacionados:** | TVWIDA |

divs
