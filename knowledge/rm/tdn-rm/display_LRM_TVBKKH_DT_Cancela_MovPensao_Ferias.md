---
content_hash: 4c226de7b81cad1c97443a43777a7d9df96d381d2c735f341275b5b8d1e878f5
fetched_at: '2026-06-29T00:08:09.985480+00:00'
page_id: '240298625'
product: rm
source: tdn-rm
title: TVBKKH_DT_Cancela_MovPensao_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBKKH_DT_Cancela_MovPensao_Ferias
version: 4
---

# CANCELAMENTO DE MOVIMENTO ESTÁ EXCLUINDO MOVIMENTO DE PENSÃO FÉRIAS SEM MARCAR PARÂMETRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cancelamento de Movimento* |
| **Situação/Requisito:** | *No processo de Cancelamento de Movimento, quando o funcionário possui eventos de Pensão de Férias e de Folha no mesmo periodo, estão sendo excluídos os* *dois registros no Movimento de Pensão por Dependente, sendo que a opção para "Cancelar Movimento de Férias" está desmarcada.* |
| **Solução/Implementação:** | *Ajuste no processo de Cancelamento de Movimento para somente excluir o registro de movimentação de Pensão de Férias no cadastro do Dependente, quando for* *marcada a opção para "Cancelar Movimento de Férias".* |
| **Chamados   relacionados:** | *TVBKKH, TVBZGZ* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
