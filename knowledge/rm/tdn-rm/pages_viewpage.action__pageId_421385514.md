---
content_hash: 64152b8a58a70d3f2447cb2035af4568e9b22d4b321f5d131a5dc65149c45c5f
fetched_at: '2026-06-29T00:09:16.328585+00:00'
page_id: '421385514'
product: rm
source: tdn-rm
title: Apontamentos de Avanço Físico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385514
version: 49
---

---

O avanço físico de uma obra é medido em termos de progresso alcançado em relação ao cronograma e ao escopo do projeto.

O responsável pelo acompanhamento do avanço geralmente utiliza ferramentas como gráficos de Gantt, relatórios de progresso, medições de áreas construídas, entre outras métricas, para avaliar o status da obra em cada etapa e garantir que tudo esteja de acordo com o planejado.

Eventuais desvios ou problemas são identificados e tratados ao longo do processo para garantir a conclusão bem-sucedida do projeto.

Dessa forma, o apontamento do avanço físico é uma prática contínua ao longo do projeto, e sua precisão e eficácia dependem de um registro cuidadoso e preciso do progresso de cada atividade.

Os coletores móveis recolhem os apontamentos de Avanço Físico das tarefas e enviam a carga com estes dados para o TOTVS Construção Obras e Projetos.

**App Minha Obra:**

**Para acessar os  Apontamentos de Avanço Físico há duas opções:**

* Acesse a opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra\ Avanço Físico \  Apontamentos de Avanço Físico;
* Ou acesse a opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra\ Avanço Físico \  Visão de Avanço Físico;

 Ou através do Anexo  Folha Tarefa:

* Acessando a opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra\ Folhas Tarefa \ Anexos \ Apontamentos de Avanço Físico;

Parâmetros

Existem alguns parâmetros que podem ser utilizados para uma experiência mais específica nos apontamentos de Avanço Físico: Para mais detalhes acesse:  |

Dentre os parâmetros citados acima é importante destacar que há duas formas de utilizar o apontamento físico: 

Por default o sistema é habilitado para utilizar o parâmetro "Progresso da Tarefa"

O percentual e quantidade apontada irão respeitar o parâmetro de avanço físico "Forma de utilização do apontamento de avanço físico", para mais detalhes, veja a documentação abaixo:  veja também

**[Progresso da Tarefa](https://tdn.totvs.com/display/LRM/Progresso+da+Tarefa)**

**[Trabalho Realizado](https://tdn.totvs.com/display/LRM/Trabalho+Realizado)**

Conforme detalhado no parâmetro Planilha para Apontamentos 

Quando o projeto estiver parametrizado para utilizar apontamentos na Planilha Executiva as informações exibidas na visão dos apontamentos de Avanço Físico considerará os itens da Planilha Executiva.

Quando o projeto estiver parametrizado para utilizar apontamentos na Planilha de Atividades as informações exibidas na visão dos apontamentos de Avanço Físico considerará as tarefas na Planilha de Atividades e não permitirá que sejam desativadas na Planilha de Atividades  por estarem vinculadas a folha tarefa.

Alguns pontos importantes sobre os apontamentos de Avanço Físico

**Atenção:**

* O campo "Saldo a executar" é exibido somente quando o projeto está parametrizado para utilizar folha tarefa. O valor apresentado é referente ao saldo que está disponível para planejamento em novas folhas tarefas.
* As alterações nos apontamentos de Avanço Físico só podem ser feitas antes da atualização do PERT no caso de o parâmetro de projeto "Atualizar o PERT automaticamente ao sincronizar e ao salvar o apontamento de avanço físico" estiver desmarcado, onde os dados somente estarão disponíveis neste anexo para visualização.
* Somente usuários com permissão no perfil podem editar os apontamentos de Avanço Físico.  
  Caso o parâmetro "Atualizar o PERT automaticamente ao sincronizar e ao salvar o apontamento de avanço físico" estar marcado, só será possível realizar alterações em folha tarefa com status apontada.
* A tela de Edição de Apontamentos vem preenchida com os valores coletados e o usuário pode alterar o Percentual ou a Quantidade de Avanço Físico da tarefa que foi recolhido pelo coletor móvel. Após a alteração deve ser informado o Status do Apontamento, que pode ser "Em Validação", para apontamentos que ainda podem ser alterados, ou "Validado" para apontamentos já liberados para atualização do PERT.
* O campo Motivo da Alteração também está presente na Edição de Apontamentos e é de preenchimento obrigatório, nele deve ser informado o motivo pelo qual os dados coletados sobre apontamentos de Avanço Físico foram alterados.
* Todas as alterações feitas serão armazenadas em tabelas de log, informando a data, hora e usuário responsável pela última alteração.
* Para apontamentos retroativos há um parâmetro que determina o número máximo de dias que um usuário pode retroceder .[Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196)
* Quando utilizar folha tarefa e o parâmetro "Atualizar o PERT automaticamente ao sincronizar e ao salvar o apontamento de Avanço Físico" estiver habilitado

  + Ao incluir um apontamento de avanço físico pelo app deve refletir o apontamento no pert .
  + Usando o mesmo apontamento de avanço físico pelo RM e o status do apontamento estiver como validado  esse apontamento será sempre refletido no  cronograma e no pert  independente de ter parametro habilitado ou não.
  + Quando utilizar não utilizar o pert o cockpit deverá buscar o avanço físico do cronograma executado.  
    Neste caso, como temos a informação por período, o cockpit deverá apresentar o avanço dos últimos 4 meses.

 Informações Complementares (Anexo)

[Históricos do Apontamento de Avanço Físico](https://tdn.totvs.com/pages/viewpage.action?pageId=795922997)
