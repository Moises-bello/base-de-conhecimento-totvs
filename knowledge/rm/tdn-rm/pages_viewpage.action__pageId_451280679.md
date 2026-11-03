---
content_hash: 650092852fd53f95100b5cc30f9d5a24e3c025fbdb1d3f3d4f765c2c20104b62
fetched_at: '2026-06-29T00:09:58.248142+00:00'
page_id: '451280679'
product: rm
source: tdn-rm
title: 4710548 FISCAL01-7542 DT Ativar/Desativar o cadastro de Natureza de Operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451280679
version: 3
---

# Ativar/Desativar cadastro de Natureza da Operação

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Cadastro de Natureza de Operação |
| **Situação/Requisito:** | Ajuste nas consistências do campo Ativo no cadastro de natureza de operação. |
| **Solução/Implementação:** | Ajustes conforme a regra:   * O sistema não permitirá marcar este campo se o CFOP de nível superior estiver inativo. * O sistema não permitirá desmarcar este campo se existirem CFOPs de níveis inferiores ativos. * Não será permitido desativar um CFOP associado a Lançamento Fiscal ou Lançamento de Ativo Imobilizado cujo Período de Apuração (do ICMS ou do ISSQN, dependendo do tipo de livro da Filial) encontra-se em aberto. * Nos Lançamentos Fiscais ou Lançamentos de ativo imobilizado, não será possível selecionar um CFOP inativo. * Na importação de Lançamentos Fiscais, o sistema estará buscando o CFOP correspondente, conforme arquivo de importação, se e somente se ele estiver Ativo. Se a Natureza está cadastrada no sistema mas encontra-se inativa, o lançamento fiscal não será importado. * Caso a natureza possua vínculo com o Lançamento Fiscal ou Movimento, o sistema não permitirá alterar as informações referentes a: origem/destino, tipo da natureza e código. |
