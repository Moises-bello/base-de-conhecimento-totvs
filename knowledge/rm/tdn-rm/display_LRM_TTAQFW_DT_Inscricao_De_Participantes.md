---
content_hash: 8878ada82f7423cddfbec80b9d0d79f98e18481290cd4fa26c28c66abef7b250
fetched_at: '2026-06-29T00:06:05.466121+00:00'
page_id: '201722495'
product: rm
source: tdn-rm
title: TTAQFW_DT_Inscricao_De_Participantes
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAQFW_DT_Inscricao_De_Participantes
version: 3
---

# INSCRIÇÃO DE PARTICIPANTES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Turmas* |
| **Situação/Requisito:** | *Não há possibilidade de incluir participantes do centro de custo 01. Sistema apresenta a mensagem: A turma "Turma teste Denise 27/08" não possui mais vagas disponíveis para inscrição de novos participantes.*  *Neste caso a mensagem está incorreta. Pois são participantes do centro de custo 01 que estou querendo incluir na turma. E há reserva de vagas para eles. E ainda estou marcando que estou consumindo reservas de vagas automaticamente. Ele só permite que os participante do centro de custo 01 sejam incluídos, se além das vagas reservadas, tiver vagas disponíveis.* |
| **Solução/Implementação:** | *Otimização no processo "Inscrição de Participantes". Quando são inseridos participantes em reservas de vagas, as reservas são atualizadas, exibindo qual participante está utilizando aquela reserva. Quando todas as vagas estão reservadas, o sistema permite a inserção de um participante nas vagas, desde que esse participante atenda aos requisitos da reserva. Quando a reserva não está disponível, ela não pode ser editada nem excluída. Quando é marcado o checkbox "Não inscrever as pessoas que estejam repetindo o treinamento.", não é permitido a inserção de participantes em turmas cujo curso já tenha sido realizado ou esteja sendo realizado pelo mesmo.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTAQFW* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
