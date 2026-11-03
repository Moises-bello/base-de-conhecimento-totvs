---
content_hash: 0db9c0bd09f93f642ffb77f29dea9280d9f890803552ef37a55041fd04c6f97d
fetched_at: '2026-06-29T00:09:10.477219+00:00'
page_id: '398753796'
product: rm
source: tdn-rm
title: S-2245 - Treinamentos e Capacitações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=398753796
version: 4
---

O envio do evento S-2245, tem a finalidade de prestar informações sobre os treinamentos, capacitações e exercícios simulados realizados, obrigatórios de acordo com as NRs. As informações referentes aos cursos estão disponibilizadas na tabela 29.

Com o intuito de facilitar a identificação da norma à qual o registro da tabela 29 se refere, os dois primeiros registros correspondem à NR que dispõe sobre a realização do treinamento, capacitação ou exercício simulado.

O prazo de envio do evento é até o dia 07 (sete) do mês subsequente ao da finalização do treinamento, capacitação ou exercícios simulados. Porém, o correto envio do evento S-2245 ao eSocial, só será possível após o envio dos eventos “S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador” e “S-2300 - Trabalhadores Sem Vínculo Emprego/Estatutário – Início”.

A partir da data de obrigatoriedade, todos os participantes que estejam nas turmas em que os cursos estejam vinculados a um curso da tabela 29, terão o gatilho do evento gerado após a finalização de avaliação de conhecimento da turma. Caso a turma tenha início anterior e ainda esteja em andamento na data de obrigatoriedade, a data que será enviada será a data de início da obrigatoriedade.

**Procedimentos para a geração dos cursos eSocial, turmas e gatilho.**

**Cursos.**

Totvs Gestão de Pessoas | Desenvolvimento | Cursos.

Para que o curso seja considerado no envio do eSocial, ele deve ser vinculado a um código da tabela 29 e para que a opção seja habilitada é preciso marcar a opção “Curso eSocial”.

Após habilitar a opção, os campos referentes ao curso eSocial, passam a ser obrigatórios para a geração do XML.

O código do curso da tabela 29 será informada no campo “Código do treinamento eSocial.”

**Turmas**

Desenvolvimento | Turmas

Na criação da turma, o campo professor passa a ser obrigatório **para a geração do XML** mas não para o cadastro da turma. Deve-se, então, observar se a turma que será cadastrada refere-se a um curso do eSocial.

*Inclusão de participantes:*

A inclusão do participante na turma pode ser feita através do Anexos | Participantes ou através de Processos | Inserir Participantes. Após inserir os participante da turma, deve-se observar se eles também foram inseridos na avaliação de conhecimento, pois somente os participantes que estiverem vinculados a uma avaliação de conhecimento finalizada terão o gatilho para o evento gerado.

Anexos | Inserir Participantes.

Processos | Inserir Participantes.

A inserção de participantes é feito através do cadastro de pessoas, porém somente será gerado gatilho para as pessoas que possuírem vínculos no cadastro de funcionários.

Para que o gatilho seja gerado é necessário finalizar a avaliação de conhecimento antes de finalizar a turma.

Após finalizar a avaliação de conhecimento, os gatilhos são gerados **SOMENTE** para as pessoas que forem funcionários.

Veja mapeamento dos campos que serão informados: Evento [S-2245](http://tdn.totvs.com/display/LRM/Evento+S-2245).
