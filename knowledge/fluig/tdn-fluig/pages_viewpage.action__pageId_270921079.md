---
content_hash: ed92ff3bbca5c883b21324479d7b60eb6f212db2783e0c663a29f6c346b73538
fetched_at: '2026-06-28T21:35:24.578840+00:00'
page_id: '270921079'
product: fluig
source: tdn-fluig
title: Mecanismo de atribuição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270921079
version: 18
---

true.\*ndicenone

# Sobre mecanismo de atribuição

---

Os mecanismos de atribuição são instrumentos utilizados durante um processo de *workflow* que permitem criar, segundo um critério estabelecido pelo próprio mecanismo, uma lista de possíveis usuários para uma atividade. Esta lista pode ser utilizada em dois momentos:

1. na inicialização do processo, onde o sistema verifica se o usuário corrente faz parte desta lista e, portanto, pode iniciá-lo;
2. no momento do encaminhamento de uma tarefa, quando esta lista é apresentada ao usuário corrente com opções de encaminhamento da solicitação.

No primeiro caso, a lista é gerada de acordo com o mecanismo de atribuição existente na primeira atividade do processo (que representa a atividade inicial). Nas demais atividades é adotado o segundo procedimento. Quando não houver um mecanismo de atribuição associado a uma atividade (seja ela inicial ou não), todos os usuários são considerados válidos.

O fluig possui alguns mecanismos de atribuição padrão, conforme abaixo:

| Mecanismo de Atribuição | Descrição |
| --- | --- |
| Para um papel (Pool) | Permite atribuir tarefas a um **papel** e não apenas a um usuário. Assim, qualquer um dos usuários neste **papel** pode assumir as tarefas para completá-las. |
| Para um grupo (Pool) | Permite atribuir tarefas a um **grupo** e não apenas a um usuário. Assim, qualquer um dos usuários deste **grupo** pode assumir as tarefas para completá-las. |
| Por associação | Permite compor lógicas complexas de atribuição por intermédio da associação de vários mecanismos. Essa função não aceita mecanismos customizados. |
| Por campo de formulário | Permite atribuir tarefas ao usuário informado em um campo do formulário do processo. |
| Por executor de atividade | Permite selecionar os usuários que executaram uma atividade anterior. |
| Por grupo | Permite selecionar no momento da movimentação da atividade apenas os usuários que façam parte de um determinado **grupo**. |
| Por grupos do usuário | Permite filtrar apenas os usuários que pertençam a um dos grupos do usuário corrente, ou do usuário que iniciou o processo (solicitante). Também permite filtrar apenas os usuários cujo grupo de trabalho seja o mesmo do usuário (corrente ou solicitante). |
| Por papel | Permite selecionar no momento da movimentação da atividade apenas os usuários que possuam um determinado **papel**. |
| Por usuário | Permite atribuir tarefas a um usuário específico. |

Mais informações

Os mecanismos "Por executor de atividade" e "Por usuário", selecionam um usuário específico, seja ele pré-determinado (Por usuário) ou variável conforme o fluxo da solicitação (Por executor). Caso o usuário destino esteja inativo, a atividade vai ser enviada ao gestor do processo.

## Como criar um mecanismo de atribuição

---

A criação de um mecanismo de atribuição é realizada pelo fluig Studio, sendo necessário já existir um projeto fluig.

Mais informações

Para que um usuário que não é administrador da empresa possa criar, importar, editar e remover mecanismos, é necessário que ele possua a permissão "Configurar Mecanismos". Esta permissão pode ser concedida pelo administrador através do item "Permissões" disponível na aba "Gerais" do Painel de Controle do fluig.

Saiba como realizar esse procedimento [clicando aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=269423844).

Utilize o passo-a-passo para conhecer o processo de criação de um mecanismo de atribuição de exemplo:

false0.5falsemecatribfadetrue11º Passo

* Para criar um novo mecanismo de atribuição desenvolvido sob a plataforma, clicar com o botão direito do *mouse* no projeto do fluig, acessar a opção *New* e então a opção *Other*. No assistente aberto, selecionar a opção "Mecanismo customizado fluig" presente na pasta fluig e clicar no botão *Next*:

22º Passo

* O assistente **Novo mecanismo fluig** é aberto. Informar o código e uma descrição e clicar no botão *Finish*:

33º Passo (Implementação)

* O arquivo JavaScript do mecanismo de atribuição é adicionado ao projeto na pasta **mechanisms** e aberto para edição.
* Este *script* deve retornar uma lista dos usuários que podem assumir a tarefa. Abaixo temos um exemplo de implementação:

javascriptEclipse1true

É possível acessar Datasets e Serviços cadastrados no fluig no desenvolvimento do mecanismo de atribuição sob a plataforma.

4Último Passo (Exportação)

* Por fim, o mecanismo de atribuição desenvolvido sob a plataforma deve ser exportado para o servidor do fluig e ao realizar a exportação deve ser informado obrigatoriamente seu código e nome, e opcionalmente uma descrição:

## Exemplo de mecanismo de atribuição Por associação

---

Demonstração de como utilizar um mecanismo de atribuição por Associação com Grupos do Colaborador e Papel, podendo adaptá-lo conforme sua necessidade.

samplesPasso 1

* Nas propriedades da atividade, em **Mecanismo de atribuição**, selecione **Atribuição por Associação** e clique em **Configurar**. Selecione **Atribuição por Grupos do Colaborador** e clique em incluir. Selecione o registro incluído e clique em **Editar**.

* Na tela de **Grupos do colaborador**, no campo **Busca Usuários nos Grupos**informe **do Usuário corrente**  e marque **Apenas Grupos de Trabalho**.
* Logo depois acione **Confirmar**.

Passo 2

* Em sequência inclua um novo mecanismo, agora como **Atribuição por Papel**, pois queremos enviar esta atividade para o papel **Líderes** onde está o líder deste usuário. Selecione o novo registro e clique em **Editar**.

* Selecione o código do papel **Líderes** e logo depois acione **Confirmar**.

Passo 3

* Selecione o tipo de associação como **Somente usuários selecionados em todos os mecanismos**, para que apenas os usuários que estejam presentes tanto no Grupo de trabalho do colaborador quanto no Papel **Líderes** sejam aptos a receber a solicitação.

* Para que no momento de enviar a solicitação seja mostrada a tela de seleção do usuário apenas quando houver mais de uma opção, o que não é o caso agora, pois existe apenas um usuário que está no Grupo de trabalho do usuário corrente e também no Papel **Líderes**, selecione o campo **Quando houver mais de uma opção** nas propriedades da atividade.

Passo 4

* No fluig você pode ter um Papel com os líderes de todas as áreas da empresa e um Grupo onde estão todos os usuários de determinada equipe, inclusive o Líder. Para utilizar o mecanismo de Grupos de trabalho do Colaborador, você precisará adicionar no cadastro do usuário este Grupo em dois locais: **Grupos** e **Grupo de trabalho workflow**.
* No exemplo abaixo o Grupo de trabalho é **suporte**. Desta forma, quando um usuário iniciar uma solicitação, a atividade configurada conforme acima irá ser direcionada diretamente para o Líder do usuário corrente, desde que ele esteja no Papel de líderes e também no Grupo de trabalho do usuário.
