---
content_hash: 05b686db1f17cf3fef0192b32fd045fec0fef38b5eb21ae30f711d3f12810530
fetched_at: '2026-06-29T00:06:07.108639+00:00'
page_id: '201735250'
product: rm
source: tdn-rm
title: TTDPX2_DT_Notas_Avaliacao_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDPX2_DT_Notas_Avaliacao_Portal
version: 3
---

# NOTAS DE AVALIAÇÃO DO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Notas de avaliação do portal* |
| **Situação/Requisito:** | *O ícone parecer descritivo da turma/disciplina GR13011-00009 no período letivo 2015, nível de ensino graduação, não é exibido somente para a professora Jessica do Vale Luz (usuário: JESSICALUZ), para as outras professoras desta turma/disciplina o ícone é exibido normalmente. A única diferença entre as professoras é que a professora Jessica possui dois cadastros de professor diferentes mas com o mesmo codigo de pessoa e o mesmo usuário associado. Ao tentarmos desvincular o usuário JESSICALUZ do cadastro de professor 9391809, automaticamente o sistema desvincula o usuário do cadastro de professor 9396175. Esse incidente já foi relatado pelo cliente no chamado TGRNTI.* |
| **Solução/Implementação:** | **Ajuste no método que retorna o código do professor, para que seja retornado o código do professor considerando em qual turma/disciplina ele está associado.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.40.108 e 11.82.41* |
