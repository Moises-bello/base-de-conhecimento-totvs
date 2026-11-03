---
content_hash: 3fa82f066c41e0f9c58479ba8b9a306e10549b319b87cb66650732bab564f587
fetched_at: '2026-06-29T00:06:21.760053+00:00'
page_id: '223180744'
product: rm
source: tdn-rm
title: TTMBMX_DT_VinculoRAIS_Transferencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMBMX_DT_VinculoRAIS_Transferencia
version: 2
---

# VÍNCULO DA RAIS SEM PREENCHER NA RESCISÃO POR TRANSFERÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão por Transferência* |
| **Situação/Requisito:** | *Quando o campo "Vínculo da RAIS" no cadastro do funcionário não está preenchido, a rescisão por transferência está gerando a nova chapa, mas mantém o funcionário antigo como ativo.*  *E assim permanecem 2 chapas do mesmo vínculo com a situação ATIVO.* |
| **Solução/Implementação:** | *Existe uma consistência no processo de rescisão de não permitir demitir funcionário com o campo "Vínculo da RAIS" sem preencher.*  *Nesta situação, deverá ser tratado também de não gerar a nova chapa transferida.* |
| **Chamados   relacionados:** | *TTMBMX* |
| **Versões/Release:** | *12.1.9* |
