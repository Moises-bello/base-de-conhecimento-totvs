---
content_hash: 617ac5eaf5b42d79e7e7154aa34a59a4c05896e8fed0f12a6b7f34571f069517
fetched_at: '2026-06-29T00:06:27.383048+00:00'
page_id: '232821095'
product: rm
source: tdn-rm
title: TUFB65_DT_LibCompetencia_Descricao_Periodo_Maior32
type: documentation
url: https://tdn.totvs.com/display/LRM/TUFB65_DT_LibCompetencia_Descricao_Periodo_Maior32
version: 2
---

# LIBERAÇÃO DE COMPETÊNCIA COM DESCRIÇÃO DO PERIODO MAIOR QUE 32 CARACTERES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Liberação de Competência* |
| **Situação/Requisito:** | *Ao tentar liberar competência informando nos campos de "Descrição do Período" um texto com mais de 32 caracteres utilizados é apresentado a mensagem "String or binary data would be truncated".* |
| **Solução/Implementação:** | *Ajuste no módulo de Liberação de Competência para não permitir nos campos de "Descrição do Período" texto com mais de 32 caracteres..* |
| **Chamados   relacionados:** | *TUFB65, TUJH51* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
