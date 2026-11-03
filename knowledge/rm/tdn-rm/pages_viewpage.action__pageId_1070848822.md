---
content_hash: 41550dec856e8103f45d1c540b023af021049b1c599fc4a556018966c88813f1
fetched_at: '2026-06-29T00:05:53.795299+00:00'
page_id: '1070848822'
product: rm
source: tdn-rm
title: Cadastro de disciplina (c)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1070848822
version: 9
---

---

Disciplina é uma funcionalidade do TOTVS Obras e Projetos que tem a finalidade de caracterizar e classificar tarefas para ter-se uma melhor visualização, usabilidade e operação do sistema.

De forma técnica, "Disciplinas" são as áreas de atuação da engenharia, por exemplo: Elétrica, Civil, Processo, Segurança, Caldeiraria, etc.

Assim, as Disciplinas serão utilizadas no sistema para agrupar tarefas que são de responsabilidade de cada área de atuação da engenharia para, por exemplo, saber quanto se está gastando com a Engenharia Elétrica, por exemplo.

Não haverá o conceito de "Disciplinas Globais" no sistema, ou seja, a definição da Disciplina será por projeto.

Quanto às Disciplinas o TOP apresenta as seguintes características:

* Uma disciplina poderá estar associada a várias tarefas;
* Mesmo que o usuário não possa cadastrar uma disciplina, ele poderá agrupá-las na visão de tarefas (Utilizando o Filtro de Disciplinas);
* As colunas de disciplinas não aparecerão na visão do PERT;
* Não poderão ser associadas disciplinas à tarefas de obra ou etapa.

**Filtro por Disciplina**

Através da funcionalidade Filtro por Disciplina é possível exibir para o usuário apenas as tarefas relacionadas às disciplinas permitidas a ele, e as tarefas que não foram classificadas com nenhuma disciplina. O filtro é aplicado automaticamente ao abrir as telas, sendo necessário apenas associar previamente as disciplinas cadastradas aos usuários. Veja em [Usuários Associados](https://tdn.totvs.com/pages/viewpage.action?pageId=421385593).  
A associação das disciplinas aos usuários pode ser feita através dos processos "Permissão por Usuário" ou "Permissão por Disciplina", disponíveis dentro do cadastro da Disciplina. O usuário que não tiver uma disciplina relacionada a ele conseguirá ver todas as tarefas (as que tem disciplina vinculada e as que não tem nenhuma disciplina vinculada). O usuário que tiver uma ou mais disciplinas vinculadas poderá visualizar as tarefas que foram associadas a essas disciplinas, bem como as que não tem nenhuma disciplina.  
No cadastro da disciplina está disponível o anexo "Usuários Associados", que permite visualizar os usuários vinculados à disciplina selecionada.  
As telas, anexos e processos nos quais o filtro é aplicado são:

* Planilha:
  + Planilha de Atividades e Serviços;
  + Serviço(s) Associado(s);
  + Associar Tarefa Percentual;
  + Fórmula de Cálculo.
* Composição:
  + Impactos em Tarefas.
* Cronograma:
  + Cronograma como Planilha;
  + Cronograma Desembolso.
* Insumos:
  + Impactos em Tarefas.
* Projeto:
  + Cópia dos Itens;
  + Comparador de Projetos.
* Tarefas:
  + Alterar Hierarquia de Tarefa;
  + Transformar Tarefa em Etapa (Limpar campo disciplina);
  + Alterar BDI diferenciado;
  + Copiar tarefa;
  + Trocar código tarefa;
  + PERT;
  + Alteração de recurso da tarefa;
  + Altera serviço indireto – direto;
  + Altera nome descrição da tarefa;
  + Calcular peso.
* Geração de Pedidos:
  + Filtro de Seleção das Tarefas;
  + Item de Pedido de Material;
  + Histograma Discriminado;
  + Histograma Agrupado;
  + Histograma Resumo;
  + Processos do anexo 'Item de Pedido de Material'.
* Geração de Pedido Extra:
  + Item de Pedido de Material Extra;
  + Processos do anexo "Item de Pedido de Material Extra"

---

**Informações Complementares - Anexos**

---

Usuários Associados

Permite visualizar todos os usuários que foram vinculados à disciplina selecionada, através dos processos "Associação por Usuário" ou "Associação por Disciplina".  
   
[Atualizacao Múltipla de Registros](https://tdn.totvs.com/pages/viewpage.action?pageId=421385084)

Para facilitar a associação entre disciplinas e tarefas, no processo de "Atualização Múltipla de Registros" existe a opção de atualizar disciplinas para tarefas.

Quando o usuário escolher o campo Disciplina na lista deste processo, serão mostrados dois campos: um para escolher a disciplina a ser associada às tarefas e outro para remover a associação das tarefas com disciplinas.

Se o segundo for marcado, o primeiro ficará desabilitado. Caso o usuário marque o segundo campo e mande executar o processo, todas as tarefas ficarão sem associação com disciplinas.  
   
[Cópia de Disciplinas](https://tdn.totvs.com/pages/viewpage.action?pageId=421385362)

Como as disciplinas serão cadastradas por coligada e projeto, há a opção de utilizar o processo de "Cópia de Itens", uma aba para copiar disciplinas entre projetos.

Ao copiar uma tarefa e essa já estiver vinculada a alguma disciplina, a disciplina também será copiada para o projeto de destino do processo.

Se ao copiar disciplinas e no projeto de destino já existir um código de disciplina igual à origem, o processo irá respeitar a escolha do usuário de ignorar ou sobrepor do campo "Item Existente" do formulário.

---

**Processos**

---

[Associação por Usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=421385073)  
   
[Associação por Disciplina](https://tdn.totvs.com/display/LRM/Cadastro+de+Disciplinas)  
   
[Atualização Múltipla de Disciplinas](https://tdn.totvs.com/pages/viewpage.action?pageId=421385084)
