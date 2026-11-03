---
content_hash: c7e54ed3a344f407bfc1c2a362b5c83e1fe3f9ac03d1153059ed5748b25dd3d8
fetched_at: '2026-06-29T00:08:32.518598+00:00'
page_id: '273989178'
product: rm
source: tdn-rm
title: ER_TOPORCAPLAN001-154_Melhorias_TOP_Mobile
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_TOPORCAPLAN001-154_Melhorias_TOP_Mobile
version: 13
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Mobilidade |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | TOPORCAPLAN001 | **IRM/EPIC1** | TOPORCAPLAN001-154 |
| **Requisito/Story/Issue1** | TOPORCAPLAN001-165  TOPORCAPLAN001-166  TOPORCAPLAN001-167  TOPORCAPLAN001-168  TOPORCAPLAN001-169  TOPORCAPLAN001-170 | **Subtarefa1** | TOPORCAPLAN001-191  TOPORCAPLAN001-194  TOPORCAPLAN001-211 |
| **Chamado/Ticket2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Apresentar as melhoria desenvolvidas no TOTVS Obras e Projetos e no TOP Mobile expedido na versão 12.1.17

## Definição da Regra de Negócio

Algumas melhorias e novidades estão disponíveis no TOTVS Obras e Projetos que envolvem as funcionalidades do TOP Mobile.

A seguir o detalhamento de cada uma delas. 

**1) Motivo de Improdutividade Vinculado**

* No cadastro de Motivos de Improdutividade, é possível vincular um motivo de Mão de Obra a um motivo de Equipamento;
* **Improdutividade de Mão de Obra Associada**: Esse campo somente estará disponível para motivos do tipo Equipamento e somente poderão ser associados os motivos do tipo Mão de Obra. Essa amarração permite com que, no coletor, ao incluir apontamentos do equipamento, que seja improdutivos, o apontamento do operador (se o usuário do coletor estiver marcado como operador) do equipamento, isto é, de mão de obra, possa ser incluído também como improdutivo. Não existindo amarração, o apontamento do operador não será incluído automaticamente.

**2) Equipamentos Associados ao Projeto**

* Possibilidade de associar equipamentos à um determinado projeto para que os mesmos possam ser sincronizados com o coletor;
* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Equipamentos \ Equipamentos Associados ao Projeto;
* Essa opção estará disponível apenas em projetos abertos;
* Os equipamentos listados para serem adicionados, são originários no cadastro de patrimônio do TOTVS Gestão Patrimonial ou do SIGAMNT;
* Após realizar a associação, os mesmos estarão disponíveis para a vinculação ao usuário operador do coletor;
* **Validações:**
  + Inclusão e Alteração: 
    - Valida se o equipamento corrente já está associado ao projeto.
  + Exclusão:
    - Valida se o equipamento está associado a algum usuário de coletor.
* **Processo de Associar Equipamentos ao Projeto**

  + Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Usuários de Coletores Móveis\ Anexos \ Equipamentos Associados\\ Processos \ Associar Equipamentos ao Projeto;
  + Através deste processo, é possível realizar a associação de vários equipamentos de uma só vez;
  + Por padrão os equipamentos carregados serão os que pertencem à filial do Projeto, porém, para visualizar todos, basta desmarcar a opção "Somente Equipamento da Filial do Projeto";
  + São exibidos apenas os equipamentos que não estão associados ao projeto;
  + As validações são as mesmas da inclusão unitária.

**3) Usuário do coletor como Operador de Equipamentos**

* O usuário de coletor pode ser definido como "Operador de Equipamentos";
* **Operador de Equipamentos**: Este campo, por default, é desmarcado. Essa informação é utilizada no coletor afim de identificar o usuário como um operador dos equipamentos associados ao mesmo e como consequência, no coletor, inserir, após o apontamento do equipamento, também, um apontamento de mão de obra para o operador.
  + Este campo somente estará habilitado se a permissão de “Apontamento de Equipamentos” estiver selecionada;
  + Para que seja possível definir o usuário como Operador de Equipamentos, é obrigatório que o mesmo seja membro de uma Equipe de Mobilidade, pois o apontamento de mão de obra necessita dessa informação.

**4) Equipamentos Associados a Usuários**

* Possibilidade de associar equipamentos à um determinado usuário para que os mesmos possam ser sincronizados com o coletor;
* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Usuários de Coletores Móveis\ Anexos \ Equipamentos Associados ao Usuário;
* No cadastro de usuário de coletores móveis pode ser realizado a associação de equipamentos que serão utilizados pelo usuário, este como Operador de Equipamentos, no coletor;
* Os equipamentos que estarão disponíveis para a associação ao usuário são os que foram associados aos projetos (Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Equipamentos \ Equipamentos Associados ao Projeto) que estão relacionados ao coletor no qual o usuário utilizará;
* Somente será possível associar equipamentos, se existirem coletores associados ao usuário;
* Ao realizar o sincronismo no coletor, essas informações serão enviadas. Ao solicitar a inclusão de entrada de apontamento de equipamento, a tela de equipamentos associados será exibida para que o equipamento seja selecionado;
* **Validações:**
  + Inclusão e Alteração: 
    - Valida se existe coletor associado ao usuário, pois os equipamentos são originários dos projetos associados ao coletor;
    - Valida se o usuário do coletor é Operador de Equipamentos.
* **Processo de Associar Equipamentos ao Usuário**

  + Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Usuários de Coletores Móveis\ Processos \ Associar Equipamentos ao Usuário;
  + Através deste processo, é possível realizar a associação de vários equipamentos de uma só vez;
  + São exibidos apenas os equipamentos que não estão associados ao usuário;
  + As validações são as mesmas da inclusão unitária.

**5) Parâmetro de Sincronismo de Equipamentos**

* O parâmetro “Tratamento para sincronismo de equipamentos associados” define como será o envio de equipamentos para o coletor, somente os associados ao usuário, este como operador, ou todos os equipamentos de todos os projetos associados ao coletor.

**6) Equipamentos no Coletor**

* Se o usuário do coletor estiver definido como Operador de Equipamentos e existirem equipamentos associados, após selecionar a Entrada Manual ou Saída Manual, a tela de pré-seleção de equipamentos será exibida para que o equipamento seja selecionado. Em caso de somente um único equipamento associado, essa tela não será exibida e o equipamento sugerido no apontamento será este único. Na entrada de apontamentos de equipamento, não se torna obrigatório apenas equipamentos associados. Ao incluir ou encerrar um apontamento, o mesmo acontecerá com o apontamento de mão de obra do operador de forma automática, porém para apontamentos improdutivos, somente será automático se os motivos estiverem associados;
* Na tela de apontamento, caso seja necessário realizar uma busca de equipamentos, é possível utilizar a tela de busca:
* Ao iniciar a entrada de um determinado equipamento, caso exista um apontamento pendente de encerramento para o mesmo, o anterior será encerrado automaticamente com a data do próximo apontamento a ser incluído. A hora terá o minuto subtraído em menos um. Essa regra não depende de o usuário ser um operador.

**7) Versionamento**

* O TOP Mobile a partir de junho de 2017, passa a ter versões especificas de forma independente. Com esta alteração passa a ter um controle interno para fornecer informações das alterações envolvendo o coletor.

  O controle de versão nos app’s são feitas em no máximo três níveis (Maior.Menor.Pacote):

  + Maior: Quando é realizado uma mudança incompatível na API.
  + Menor: Quando adicionado funcionalidade mantendo a compatibilidade.
  + Pacote: Quando é liberado um novo pacote de correção, mantendo a compatibilidade.

Iremos iniciar a versão do TOP Mobile como 12, fazendo referência a versão do RM iniciamos o novo aplicativo.

* A versão do aplicativo faz referência aos serviços Rest que o usuário pode acessar. O serviço de cada frente poderá exigir uma versão do coletor diferente. Esse recurso faz com que serviços não utilizados, não necessitam de atualização do coletor. Exemplo:

1. 1. Cliente possui a versão do coletor 12.0.0.
   2. Totvs cria uma nova funcionalidade para a frente de Mão de Obra, obrigando o uso da versão 12.1.0.
   3. Apenas clientes que utilizam o serviço de apontamento de Mão de Obra deverão atualizar o coletor. Os outros clientes poderão continuar na versão 12.0.0.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Motivos de Improdutividade | [Envolvida] | Opção de Menu: Projetos \ Construção e Projetos \ Cad. Gerais \ Básicos \ Motivos de Improdutividade | - |
| Equipamentos Associados ao Projeto | [Criação] | Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Equipamentos \ Equipamentos Associados ao Projeto; | - |
| Usuários de Coletores Móveis | [Envolvida] | Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Usuários de Coletores Móveis | - |
| Equipamentos Associados ao Usuário | [Criação] | Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Usuários de Coletores Móveis\ Anexos \ Equipamentos Associados ao Usuário | - |
| Parâmetros Projetos | [Envolvida] | Opção de Menu: Projetos \ Construção e Projetos \ Projetos \ Parâmetros \ Construção e Projetos \ Parâmetros Projetos |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
