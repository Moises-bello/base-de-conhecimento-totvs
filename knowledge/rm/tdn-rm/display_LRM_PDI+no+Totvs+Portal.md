---
content_hash: 5148960fccd6d288d99297fe769cad67937deece47791f058f926f9963aff334
fetched_at: '2026-06-29T00:10:08.629022+00:00'
page_id: '452719549'
product: rm
source: tdn-rm
title: PDI no Totvs Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/PDI+no+Totvs+Portal
version: 3
---

**PDI no Totvs Portal**

Acessar Totvs Portal| Recursos Humanos| Gestão por competências| PDI. Respeitando os parâmetros de definição no cadastro do PDI, os usuários avaliadores/avaliados poderão gerenciar o PDI pelo  Totvs Portal.

O funcionamento da gerência de PDI consiste basicamente na definição de ações que o avaliado deve executar para se desenvolver individualmente em um prazo determinado, assim como o lançamento do percentual de completude de cada ação definida. Sendo assim, tanto a definição das ações quanto a atualização da completude, podem ser realizados pelo avaliador ou pelo avaliado. Contudo, toda alteração realizada por um avaliado é submetida à aprovação de seu avaliador.

**Visão geral:**

**Gerenciar** – Contém link de acesso para gerenciar o PDI do avaliado

**Status** – iIndica o status do PDI, que pode ser: Pendente (PDI que ainda não foi definido), Iniciado (PDI definido mas as ações não foram cumpridas) e Concluído (Quando as ações definidas foram todas cumpridas)

**Pendências** – Indica se o PDI possui pendência de aprovação pelo avaliador de uma nova ação ou lançamento

**Descrição** – Contém a descrição do PDI

**Chapa** – Chapa do funcionário avaliado

**Nome** – Nome do funcionário avaliado

**Avaliação de Desempenho** – Indica o nome da Avaliação de Desempenho vinculada ao PDI, caso exista

**Data Início** – Data inicial do período para execução

**Data Fim** – Data final do período para execução.

**Tela de gerenciamento**

Excluir – Botão para **exclusão da ação** (Somente poderão ser excluídas ações que não tiveram lançamento e também se o PDI estiver dentro do período de execução)

Editar – Botão para **editar dados da ação** (Somente podem ser editados os campos de objetivo da ação e prazo de cumprimento)

Lançar atualização – Botão para efetuar um **novo lançamento** de percentual de completude da ação, com possibilidade de incluir um comentário

Status – Informa qual o **status da ação**, que pode ser:

* Inclusão aguardando aprovação do avaliador,
* Ação sem pendências,
* Sugestões de PDI reprovadas pelo avaliador,
* Atualização aguardando aprovação do avaliador
* Ação aguardando complemento

**Tipo de Ação** – Informa o tipo de ação a ser desenvolvida pelo avaliado

**Objetivo da Ação** – Descreve o objetivo da ação a ser desenvolvida pelo avaliado

**Requisito de Acesso** – Informa o requisito de acesso associado à ação, ou seja, qual requisito será concedido ao funcionário caso ele cumpra a ação (100% de completude)

**Prazo para cumprimento** – Contém a data limite para cumprimento da ação

**Valor** – É o valor percentual de completude da ação. Também é um link de acesso ao histórico de lançamento de completude da ação.

**Nova Ação** - Botão para **inclusão de uma ação**, onde é necessário informar os seguintes dados:

* Objetivo da ação - Devem ser descritos os objetivos do avaliado para cumprimento da ação;
* Tipo de ação – Deve ser descrito o tipo de ação que o usuário deve desenvolver.
* Neste campo serão listadas todas as metas filhas cadastradas na tela de definição do PDI

**Requisito de Acesso** – Caso o parâmetro "Utiliza metas para o desenvolvimento de requisitos de acesso" esteja marcado no cadastro de PDI, esta opção estará disponível na criação da ação. Ao informar o Requisito de Acesso associado à ação, caso avaliado atinja 100% nessa ação, o requisito de acesso será concedido ao avaliado. Os requisitos de acesso disponíveis para ação respeitarão o parâmetro "Tipos de restrição para associação de requisitos à Metas". Se estiver marcado o parâmetro "Preenchimento de requisito de acesso obrigatório", este campo se torna obrigatório;

**Prazo para cumprimento** - Deve ser informado o período para execução e cumprimento da ação.

**"Aprovar/Reprovar Ações" e "Aprovar/Reprovar Atualizações"**- Botões para **aprovar/reprovar ações ou atualizações**. Contudo estes botões somente são exibidos para avaliadores. Caso seja aprovado um lançamento de 100% e ação criada possua Requisito de Acesso vinculado, este requisito será concedido ao perfil do avaliado no momento da aprovação; Para **visualizar o histórico de lançamentos** (% completude) de cada ação, na listagem existe a coluna "Valor" que armazena um link de acesso ao histórico; Caso o avaliado não necessite da definição de ações, o avaliador pode marcar o checkbox "**Não será necessária nenhuma ação**", que seu PDI será considerado como concluído.

**Carregar sugestões de ação** - Se no cadastro do PDI foi marcado o campo "Habilitar sugestões de ações para o funcionário", no Totvs Portal será habilitado a opção "**Carregar sugestões de ação**".  
A sugestão de ação é uma rotina baseada nos requisitos a desenvolver dos avaliados do PDI apontadas por meio do mapa de conhecimento por requisito de acesso e por competências. Quando acionada a opção "Carregar sugestões de ação", será visualizada uma listagem com os requisitos a desenvolver do colaborador, conforme a regra de exibição de requisitos definidos no cadastro de PDI, campo "Tipos de restrição para associação de requisitos à metas". Deve ser selecionado um requisito e o tipo de ação para que seja lançado uma ação no PDI. As ações serão criadas com o status "aguardando complemento", sendo necessário editar a ação criada e preencher as informações obrigatórias faltantes da ação, como objetivo e prazo de conclusão. Após o preenchimento completo das ações o sistema irá disponibilizá-las para uso com a possíveis situações:

* "Ação sem pendências" caso seja o gestor que esteja preenchendo o PDI
* "Inclusão de PDI aguardando aprovação de Gestor", caso seja o próprio funcionário (avaliado) a preencher as informações.

**Observação:**

Na tela de sugestões de ações, serão listados separadamente os requisitos que deveriam ser sugeridos, mas que não possuem metas definidas para desenvolvimento no PDI. Caso o funcionário já possua ações criadas a partir de requisitos sugeridos, o sistema irá marcar estes requisitos com o caractere \* (asterisco).A rotina de sugestões de ações possui ainda uma funcionalidade onde o sistema provê sugestões de ação para os colaboradores baseadas nos resultados de um LNTD (Levantamento de Necessidades de Treinamento e Desenvolvimento). Desta forma, ao invés de serem carregadas sugestões baseadas nos itens a se desenvolver do mapa de conhecimento do funcionário, serão apresentadas sugestões baseadas nos resultados de uma LNTD em que o funcionário for indicado. Para que as sugestões por LNTD fiquem disponíveis, deve ser executado o processo "**Carregar sugestão de ação por LNTD**" disponível em Acompanhamento| PDI. Neste processo deve ser informado o LNTD desejado, para que sejam carregadas as sugestões para todos os participantes do PDI.

**Atenção:**

Um aspecto importante que deve ser entendido sobre a tela de gerência de PDI é que todo seu funcionamento é integrado ao módulo de gestão de metas, ou seja, toda ação criada é uma meta do tipo "valor" que é gerada a partir das metas associadas ao PDI. Sendo assim, toda atualização de completude da ação, nada mais é que a atualização dos resultados para cumprimento de uma meta. Apesar da relação entre PDI e Metas funcionarem de forma transparente, as metas geradas pelo PDI podem ser visualizadas nos cadastros de metas, contudo estas mesmas metas não podem ser manipuladas ou visualizadas através do Painel de Metas (Totvs Portal).
