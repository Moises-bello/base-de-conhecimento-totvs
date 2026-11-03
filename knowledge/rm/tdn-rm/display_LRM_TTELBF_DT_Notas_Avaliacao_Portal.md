---
content_hash: cc7aa9502939985b79dfe1abd0e1700199b0caec13021002b5fe3004ec55c10a
fetched_at: '2026-06-29T00:06:07.796347+00:00'
page_id: '201738051'
product: rm
source: tdn-rm
title: TTELBF_DT_Notas_Avaliacao_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TTELBF_DT_Notas_Avaliacao_Portal
version: 1
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
| **Versões/Release:** | *12.1.7 e 12.1.8* |
