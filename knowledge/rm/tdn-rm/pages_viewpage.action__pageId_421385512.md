---
content_hash: d8479d7be171b6e200e4c5e0bfb76c76e7c9e208140268ae05e3ae0519b19848
fetched_at: '2026-06-29T00:09:16.312125+00:00'
page_id: '421385512'
product: rm
source: tdn-rm
title: Tarefa(Visão Avanço Físico)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385512
version: 24
---

---

A  tela Visão de Avanço Físico pode ser acessada:

Pelo anexo "Visão de Avanço físico" na Folha Tarefa.

Ou pela opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra\ Avanço Físico \  Visão de Avanço Fìsico

Apresenta uma visão com informações das tarefas da folha e do avanço físico, onde não será permitido realizar nenhuma alteração, apenas visualização e acompanhamento.

Hoje essa visão exibe as seguintes informações:

* Número da Folha Tarefa
* Descrição da Folha Tarefa
* Etapa
* Código da Tarefa | Item
* Nome da Tarefa | Item
* Unidade da Tarefa |Item
* Quantidade da Tarefa |Item
* % do Apontamento
* Quantidade Programada
* Saldo a Executar
* Tipo de Apontamento
* Data do Apontamento
* Status da Folha Tarefa
* Data da Atualização do PERT
* Criado Por
* Criado Em
* Fator de Produtividade
* Quantidade Planejada
* Descrição da Tarefa |Item
* Percentual

Lembrando que conforme detalhado no parâmetro Planilha para Apontamentos 

Quando o projeto estiver parametrizado para utilizar apontamentos na Planilha Executiva as informações exibidas na visão dos apontamentos de Avanço Físico considerará os itens da Planilha Executiva.

Quando o projeto estiver parametrizado para utilizar apontamentos na Planilha de Atividades as informações exibidas na visão dos apontamentos de Avanço Físico considerará as tarefas na Planilha de Arividades.

Informações Complementares (Anexo)

---

[Históricos do Apontamento de Avanço Físico](https://tdn.totvs.com/pages/viewpage.action?pageId=795922997)

Para detalhes como realizar  Apontamento de Avanço Físico no App acesse :

**Observação:**

O campo "Saldo a executar" é exibido somente quando o projeto está parametrizado para utilizar folha tarefa. O valor apresentado é referente ao saldo que está disponível para planejamento em novas folhas tarefas.

O parâmetro de casas decimais para percentual e quantidade será respeitado pelo TOP Mobile.

Para que a produção real do executado na obra possa ser possível, o TOP Mobile permite que os apontamentos de Avanço Físico possam ser definidos acima de 100% do planejado, pois em muitos casos a quantidade planejada é apenas uma estimativa e não reflete a realidade.

Sendo assim temos dois cenários em que esse apontamento acima de 100% pode refletir no TOTVS Obras e Projetos:

* **Quantidade Planejada do item na Falha Tarefa ser 100% da quantidade definida para a tarefa no projeto:**
  + Tarefa 001.01.01, Quantidade = 100
  + Item da Folha Tarefa, Quantidade Planejada = 100
  + Percentual do Apontamento = 200%
  + Percentual Concluído no PERT = 100%
* **Quantidade Planejada do item na Falha Tarefa ser menos de 100% da quantidade definida para a tarefa no projeto:**
  + Tarefa 001.01.02, Quantidade = 100
  + Item da Folha Tarefa, Quantidade Planejada = 25
  + Percentual do Apontamento = 200%
  + Percentual Concluído no PERT = 50%

No TOP Mobile, nos apontamentos de Avanço Físico, além da foto que pode ser tirada através do próprio aplicativo, é possível selecionar, a partir da galeria do Coletor Móvel, alguma imagem que por ventura foi recebida através de aplicativos de mensagens ou até mesmo um download. Em várias obras, alguns arquivos de imagens são coletador via drone e utilizados para registro de imagens (vídeo/foto) da evolução da obra.

Na tela de apontamento, se a tarefa em questão não tem nenhuma foto associada, são exibidas as opções de "Tirar Foto" e de "Buscar na Galeria do Coletor". Caso já existam fotos associadas, as mesmas serão apresentada ao lado das opções de Tirar Foto e Buscar na Galeria do Coletor.

Ao sincronizar com o TOTVS Obras e Projetos, todas as imagens associadas ao apontamento, serão enviadas e poderão ser visualizadas na "Edição de Apontamentos" no anexo da respectiva Folha Tarefa.

---
