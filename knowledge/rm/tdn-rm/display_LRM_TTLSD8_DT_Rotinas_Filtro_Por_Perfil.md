---
content_hash: c8a702dc6140bb51059baa858ad10d7e24b08d90330732f79bf3c92d46c32260
fetched_at: '2026-06-29T00:06:15.391601+00:00'
page_id: '210054819'
product: rm
source: tdn-rm
title: TTLSD8_DT_Rotinas_Filtro_Por_Perfil
type: documentation
url: https://tdn.totvs.com/display/LRM/TTLSD8_DT_Rotinas_Filtro_Por_Perfil
version: 2
---

# PERFIL - FILTRO POR PERFIL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Seleção de funcionários* |
| **Situação/Requisito:** | *Em algumas rotinas, como “Alteração Global de Campos”, “Distribuição da Sefip”, “Liberação de Flags”, o filtro aplicado ao perfil do usuário para restrição de acesso não estava sendo respeitado, fazendo a seleção de funcionários normalmente sem o filtro cadastrado.* |
| **Solução/Implementação:** | *Alterado a execução das rotinas descritas acima para que verifiquem adequadamente a restrição do perfil.* |
| **Chamados relacionados:** | TTLSD8 |
| **Versões/Release:** | *11.82.42* |
