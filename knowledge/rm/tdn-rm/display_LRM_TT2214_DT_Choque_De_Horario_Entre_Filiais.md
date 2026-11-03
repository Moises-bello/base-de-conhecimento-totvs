---
content_hash: 37ed0a636b06c7bf36c4ca237db4c93a9449af5e4ab9642595719017eecfa1d2
fetched_at: '2026-06-29T00:06:05.427094+00:00'
page_id: '201721579'
product: rm
source: tdn-rm
title: TT2214_DT_Choque_De_Horario_Entre_Filiais
type: documentation
url: https://tdn.totvs.com/display/LRM/TT2214_DT_Choque_De_Horario_Entre_Filiais
version: 4
---

# CHOQUE DE HORÁRIO ENTRE FILIAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | *Educacional* |
| **Função:** | *Choque de horário entre Filiais* |
| **Situação/Requisito:** | *Ao tentar realizar o processo de matricula em disciplinas o sistema está validando o choque de horário, mas em alguns momentos não valida. Caso o horário esteja com a mesma data da turma disciplina o sistema está permitindo o choque de horário mesmo não possuindo permissão. Se estiver sem data, exibe o choque.* |
| **Solução/Implementação:** | *A validação do componente responsável pela exibição dos horários selecionados, estava considerando a coluna CODHORARIO, enquanto que para validar o choque de horário entre Filiais, é necessário que seja utilizado as datas e horário início e fim.* |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | *NA* |
| **Versões/Release:** | *11.82.41* |
