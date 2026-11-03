---
content_hash: 0d63f6045f95ab240360afd912ec77eb43c0cc8ee20f2413d740fb677b99d143
fetched_at: '2026-06-29T00:10:07.255692+00:00'
page_id: '452719385'
product: rm
source: tdn-rm
title: Gestão por Quadrantes no Totvs Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719385
version: 3
---

**Gestão por Quadrantes no Totvs Portal**

Acessar Totvs Portal| Recursos Humanos| Gestão por Quadrantes.

A visão é composta por cabeçalho com filtros, o grid de acompanhamento e os quadrantes com os participantes. Quando no cadastro da Gestão por Quadrantes está marcado o campo "Utiliza participantes de Avaliações de Desempenho", os participantes da gestão estarão distribuídos nos quadrantes de acordo com a nota obtida na avaliação de desempenho e o valor do intervalo do quadrante, conforme descrito no processo de inicialização. E somente serão exibidos nos quadrantes os participantes que o avaliador for gerir, ou seja, avaliados diretos e/ou indiretos.  
   
Quando no cadastro da Gestão por Quadrantes está desmarcado o campo "Utiliza participantes de Avaliações de Desempenho", os participantes da gestão estarão obrigatoriamente no quadrante padrão, conforme descrito no processo de inicialização. E somente serão exibidos nos quadrantes os participantes que o avaliador for gerir, ou seja, avaliados diretos e/ou indiretos.

As **opções de filtros** são:

- Responsável pela Fase: Campo que indica o nome do funcionário avaliador da gestão em questão. Caso o usuário seja um avaliador, o lookup ficará desabilitado, mostrando o nome do mesmo. Caso o usuário logado não seja um avaliador, mas tenha permissão para revisão, o lookup ficará habilitado, onde será permitido selecionar o responsável pela gestão;

- Filtro de Avaliação: Campo que listará as entidades existentes, de acordo com a configuração da Gestão por Quadrante. As entidades poderão ser Função, Cargo ou Grupo Ocupacional. Se a gestão por quadrante foi configurada por função, no lookup serão listadas as funções dos avaliados por exemplo;

- Filtro de Pessoas por Gestor: Campo com os avaliados que são avaliadores (diretos e/ou indiretos) do responsável pela fase selecionado. Ao selecionar uma pessoa por gestor, será exibido os avaliados da gestão a partir da visão deste avaliador selecionado;

- Filtro customizado: campo que irá listar os filtros do RM Portal configurados para a gestão por quadrantes. Para configurar estes filtros acessar Configurações| Filtros do RM Portal e editar a opção Gestão por Quadrantes;

- Exibir avaliados diretos: campo que irá restringir a exibição para somente avaliados diretos;

- Exibir avaliados indiretos: campo que irá restringir a exibição para somente avaliados indiretos.  
   
**Visão geral:**

Gerenciar – Contém link de acesso para gerenciar quadrantes;

Código – Código da gestão por quadrantes;

Status – Indica o status da gestão que pode ser: Pendente ou Finalizada;

Descrição – contém a descrição da gestão;

Seleção de Avaliados – informa se a gestão será feita em função de avaliados diretos e/ou indiretos;

Data da abertura – data da abertura da gestão;

Data limite execução – data de limite de execução da gestão;

Data de fechamento – data de fechamento da gestão;

**Tela de gerenciamento:**

O quadro de Acompanhamento terá as seguintes informações:

- Total de Participantes: quantidade de avaliados do avaliador, de acordo com os filtros realizados;

- Análise: coluna com o nome dos quadrantes definidos na configuração da gestão por quadrante;

- Percentual Exigido: percentual de avaliados que espera-se que esteja alocado no respectivo quadrante, definido na configuração da gestão por quadrante;

- Exigido: quantidade de avaliados que espera-se que estejam alocados no respectivo quadrante, considerando a quantidade de avaliados e o percentual do quadrante;

- Atual: quantidade atual de participantes em um quadrante;

- Percentual Atual: percentual atual de avaliados no quadrante, considerando o total de participantes e a quantidade atual.

- Ajuste: quantidade de participantes que deverão sofrer alterações de quadrante, de modo que seja respeitada a quantidade máxima/percentual;

- Percentual de Ajuste: diferença entre o percentual exigido e o percentual atual.

**Operações:**

- Por meio do recurso arrastar e soltar poderão ser movimentados os participantes entre quadrantes, atualizando automaticamente o quadro de acompanhamento para o determinado avaliador;

- Se o avaliado for alterado para um quadrante de avaliação superior, passará a ter seu nome destacado na cor azul.

- Se o avaliado for alterado para um quadrante de avaliação inferior, passará a ter seu nome destacado na cor vermelha.

- Visualização de informações complementares do avaliado, ao posicionar o mouse sobre o mesmo, e a possibilidade de realizar a inserção de comentários;

- Para destacar um quadrante deve clicar no ícone "Destacar quadrante". Ao destacar um determinado quadrante, o "quadrante padrão" (quando houver) ocupará temporariamente a posição do quadrante que irá receber o destaque. Sendo assim, o quadrante padrão irá retornar à posição original no momento em que o quadrante em destaque for restaurado.

- Finalização da gestão feita pelo avaliador. Este recurso encontra-se presente no botão "Finalizar", onde cada avaliador após realizar os seus ajustes, fecha a gestão para que o avaliador hierarquicamente acima dele possa efetuar uma gestão sem interferências. Uma vez que um avaliador finaliza a sua gestão, todos os seus avaliados que são avaliadores terão a sua gestão finalizada, ou seja, não poderão realizar nenhuma alteração.  Ao acessar o recurso de finalização serão apresentadas algumas informações sobre os avaliados, como Nome, Quadrante Anterior, Quadrante Atual, e um botão para inserir comentário rapidamente.
