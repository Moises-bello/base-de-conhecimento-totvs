---
content_hash: 024fbf6f6dcb9ca44a244c434543d096b141f36470ff7e36b3d8ab75166cb701
fetched_at: '2026-06-29T00:09:31.359626+00:00'
page_id: '425458652'
product: rm
source: tdn-rm
title: Matrícula em regime de dependência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458652
version: 5
---

---

Matricula em regime de dependência, consiste na situação em que acontece no **Ensino Básico**, onde um aluno pode fazer uma disciplina de uma série anterior de forma isolada, quando foi reprovado no ano anterior. Desta forma, o aluno fica apto a cursar a série seguinte e cumprir a disciplina pendente.

Este parâmetro marcado irá influenciar na , para mais informações do impacto na geração do histórico .

**Montando um cenário para exemplificar...**

Um aluno do ENSINO MÉDIO, em 2010 Cursou 1º. Ano e foi reprovado na disciplina de MATEMÁTICA. No modelo normal, este aluno, em 2011 deveria repetir o primeiro ano (cursar novamente).

Já no conceito de Dependência, o aluno em questão se matriculará normalmente no 2º. Ano do Ensino Médio e, paralelamente a isso ele vai se matricular também no 1º. Ano, só que Cursando apenas a disciplina de MATEMÁTICA. Respeitando, obviamente, as regras normais, como choque de horário, etc.

No Aplicativo, essa possibilidade se dará da seguinte forma:

1º. No Cadastro de Tipo de Matrícula, existe agora um check-box, para indicar Dependência. Portando, deve se criar um Tipo de matricula para tal situação;

2º. Ao se matricular o aluno pelo processo "Matricular aluno", deve-se informar o tipo de matrícula em questão para a série e para a disciplina que o mesmo foi reprovado no período/ano anterior.

**Obs.**: A Matrícula da Série seguinte dele é feita NORMALMENTE.
