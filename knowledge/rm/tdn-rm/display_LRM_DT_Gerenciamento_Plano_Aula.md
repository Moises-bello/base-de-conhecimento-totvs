---
content_hash: a545237362f4c39f3a316b468023fab00d63be86f709fb98ffdf78f4ee436628
fetched_at: '2026-06-29T00:06:27.475468+00:00'
page_id: '232822553'
product: rm
source: tdn-rm
title: DT_Gerenciamento_Plano_Aula
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Gerenciamento_Plano_Aula
version: 126
---

# Gerenciamento de aula

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Gerenciamento de aula* | *Gerenciamento de plano de aula* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Plano de aula da turma/disciplina* |  | | *Professores da turma/disciplina* |  | | *Horários da turma/disciplina* |  | | *Professores do horário na turma/disciplina* |  | |
| **Cadastros Iniciais:** | *Período letivo, turma, turma/disciplina, turno, horário do turno, etc* |
| **Requisito (ISSUE):** | PCREQ-8586 |
| **País(es):** | *Brasil* |
| **Versões/Release:** | *12.1.10* |

## Descrição

Foi disponibilizado uma nova interface para "Gerenciamento de aula" (plano de aula) para a turma/disciplina. Com essa nova funcionalidade, nossos clientes irão ganhar mais agilidade e facilidade ao realizar o gerenciamento das aulas, professores e horários de suas turma/disciplinas. Através dessa nova funcionalidade, o usuário poderá incluir/alterar/excluir uma aula, bem como alterar a disciplina, data da aula e horário entre turmas/disciplinas de mesma turma e período letivo, facilitando assim o ajuste de aulas geradas. Em resumo, nosso cliente poderá realizar a manutenção de 4 cadastros (Horário da turma/disciplina, Professor da Turma/Disciplina, Professor do horário e Plano de aula) em uma única funcionalidade.

## Procedimento para Utilização

       1.            Acessar o registro de perfil no módulo de Globais para conceder acesso as funcionalidades em "RM | Serviços Globais | Segurança | Acesso | Perfis | Sistema Educacional":

1. 1. Conceder permissão de acesso na funcionalidade "Gerenciamento de aula", em "Educacional > [01] Currículo e Oferta > [01.03] Oferta > [01.03.06] Mais ... > **[01.03.06.07] Gerenciamento de aula**";
   2. Conceder permissão de acesso para o plano de aula em "Educacional > [01] Currículo e Oferta > [01.03] Oferta > [01.03.05] Turmas/Disciplinas > **[01.03.05.25] Planos de aula**";
   3. Conceder permissão de acesso para professores da turma/disciplina em "Educacional > [01] Currículo e Oferta > [01.03] Oferta > [01.03.05] Turmas/Disciplinas >**[01.03.05.04] Professores da turma/disciplina**";

       2.            No TOTVS Educacional, acesse a funcionalidade de gerenciamento de aula em "TOTVS Educacional | Currículo e Oferta | Oferta | Mais ... | Gerenciamento de aula";

Ao acessar a funcionalidade, o sistema irá abrir a tela com o período letivo corrente já preenchido, caso esteja parametrizado no sistema. O filtro de "**Turma**" é **obrigatório** e deverá ser informado, mas o filtro de "**Turma/Disciplina**" é **opcional** para selecionar os registros. Depois de informar os filtros, basta clicar no botão "**selecionar**" que a funcionalidade irá exibir os dados conforme os filtros informados.

       3.            Caso exista alguma aula (plano de aula) para a(s) turma/disciplina(s), a funcionalidade irá exibir uma "grade" com as informações da aula e embaixo de cada aula, os dados do professor da turma/disciplina e do horário, baseado na data da aula e as datas de início/término do professor na turma/disciplina.

Algumas colunas são apenas para visualização e não permitem alteração, tais como "Nome da disciplina", "Aula", "Término" e "Nome" (para professor).

As demais colunas permitem alteração, permitindo a manutenção dos cadastros que envolvem a aula, horário da turma/disciplina e professor da turma/disciplina (em conjunto com professor do horário).

**Importante:** Ao alterar os campos "Cód. Disciplina", "Data", "Inicio (horário)" e/ou "Nome (professor)", o sistema poderá excluir o registro anterior para incluir novo registro com as novas definições.

       4.            Descrição dos parâmetros disponibilizados na funcionalidade (checkbox):

* + **Não verificar data de validade do período letivo:** Este parâmetro marcado, permite ao usuário salvar uma data no plano de aula que não esteja contemplada nas datas de início/término do período letivo.
  + **Não ultrapassar carga horária da disciplina:** Este parâmetro marcado, não permite ao usuário salvar um plano de aula quando o limite de carga horária da disciplina for atingido.
  + **Ordenar aula ao salvar:** Este parâmetro marcado, permite a funcionalidade realizar a ordenação do campo "aula" do plano de aula, sempre que algum plano de aula for salvo. Essa opção poderá estar desabilitada, caso não tenha permissão, conforme "item 1" e "subitem b" descrito acima;

       5.            Descrição dos botões disponibilizados na funcionalidade:

* + **Incluir aula:** Através desse botão, será possível incluir um novo registro de plano de aula informando os campos obrigatórios. Esse botão poderá estar desabilitado caso não tenha permissão, conforme "item 1" e "subitem b" descrito acima;
  + **Excluir aula:** Através desse botão, será possível excluir um ou mais registro(s) de plano de aula marcando os registros na grade ([X]). Esse botão poderá estar desabilitado caso não tenha permissão, conforme "item 1" e "subitem b" descrito acima;
  + **Incluir professor:** Através desse botão, será possível incluir um novo registro de professor da turma/disciplina e do horário informando os campos obrigatórios. Esse botão poderá estar desabilitado caso não tenha permissão, conforme "item 1" e "subitem c" descrito acima;
  + **Excluir professor:** Através desse botão, será possível excluir um ou mais registro(s) de professor da turma/disciplina e horário marcando os registros na grade ([X]). Esse botão poderá estar desabilitado caso não tenha permissão, conforme "item 1" e "subitem c" descrito acima;
  + **Ordenar aula:** Através desse botão, será possível executar a ordenação dos registros do plano de aula, pois dependendo da manutenção no cadastro, poderemos ter plano de aula com o "número" da aula desordenado. Esse botão poderá estar desabilitado caso não tenha permissão, conforme "item 1" e "subitem b" descrito acima ou o parâmetro "Ordenar aula ao salvar" esteja marcado;
  + **Salvar**: Através desse botão, será possível aplicar todas alterações (mudanças) realizadas na grade da funcionalidade que estejam pendentes. Esse botão estará visível apenas quando existir alguma alteração pendente para salvar.
  + **Cancelar**: Através desse botão, será possível "descartar" todas alterações (mudanças) realizadas na grade da funcionalidade que estejam pendentes. Esse botão estará visível apenas quando existir alguma alteração pendente para salvar.
  + **Fechar**: Através desse botão, será possível fechar a tela da funcionalidade.

divs
