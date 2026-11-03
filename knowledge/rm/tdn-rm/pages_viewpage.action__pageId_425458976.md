---
content_hash: db9c86079e134392db36385ea6a0aee05a38646c339275a61132872a361ef141
fetched_at: '2026-06-29T00:09:33.327863+00:00'
page_id: '425458976'
product: rm
source: tdn-rm
title: Importação de dados do Urânia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458976
version: 6
---

---

Este processo importa as alocações de salas e professores do Urânia, exportados pelo menu "Integração/Exportar horário", para o TOTVS Educacional.

**Importante**

O processo de importação não atualiza os dados da turma/disciplina, as informações importadas são armazenadas em um estrutura temporária que possibilita a conferência das informações antes da efetivação na base de dados. O processo respeitará o contexto corrente do usuário.  
   
Na execução do processo é informado o período letivo, o perídio do turno e o arquivo que foi gerado no Urânia.   
   
Durante a importação algumas validações são realizadas:

* Existência da turma referenciada no arquivo de importação;
* Existência da turma/disciplina referenciada no arquivo de importação;
* Existência do professor referenciado no arquivo de importação;
* Existência da sala (ambiente) referenciado no arquivo caso o parâmetro "Utiliza "Ambiente" do Urânia como "Sala" do TOTVS Educacional"l estiver habilitado;
* Existência da relação entre aula e o horário do TOTVS Educacional;
* Parâmetro "Permitir atualização de turma/disciplina com conteúdo previsto preenchido no plano de aula" desabilitado;
* Parâmetro "Permite atualização dos horários da turma/disciplina que possua professor com folha de pagamento aprovada" desabilitado;
* Existência de alunos matriculados.

Ao concluir a execução, será informado no log:

* Quantidade de turmas/disciplinas sugeridas apagadas: Número de turmas/disciplinas que foram importadas na execução anterior do processo para o período letivo e turno
* Quantidades de turmas/disciplinas: Número de turmas/disciplinas que será importadas
* Quantidade de turmas/disciplinas sugeridas com pendência/aviso no log: Número de turmas/disciplinas que possuem algum tipo de inconsistência, podem ser do tipo pendência: log que precisa de alguma ação do usuário ou aviso: log para o qual existem permissões no processo de importação definitiva e dependendo da escolha do usuário poderá impedir ou permitir a atualização da turma/disciplina.
* Quantidade de turmas/disciplinas sugeridas sem pendência/aviso no log: Número de turmas/disciplinas que foram importadas e não ocorreu nenhuma inconsistência.
* Detalhes da importação de cada turma/disciplina.

 Como Fazer

---

[INTEGRAÇÃO TOTVS Educacional X Urânia](http://tdn.totvs.com/display/INT/DI_MANUAL_TOTVS_Educacional_Urania)
