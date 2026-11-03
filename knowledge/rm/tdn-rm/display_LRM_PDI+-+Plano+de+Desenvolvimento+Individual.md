---
content_hash: 768ceaef7f4878d8841fc4e82ccd7db2443dbbb95781e12b40c1743dd400a32c
fetched_at: '2026-06-29T00:10:04.773360+00:00'
page_id: '452719248'
product: rm
source: tdn-rm
title: PDI - Plano de Desenvolvimento Individual
type: documentation
url: https://tdn.totvs.com/display/LRM/PDI+-+Plano+de+Desenvolvimento+Individual
version: 3
---

**PDI - Plano de Desenvolvimento Individual**

---

O Plano de Desenvolvimento Individual (PDI) tem como objetivo planejar, executar e acompanhar o desenvolvimento individual de cada profissional, visando atender as necessidades estratégicas internas, de sua função/cargo e do desenvolvimento pessoal/profissional.

Pontos de impacto do PDI:

1) Gestão de Metas: Utiliza a estrutura de metas e seu acompanhamento para criar as ações e lançamentos de completude.

2) Requisitos de Acesso: Realiza a concessão de requisitos de acesso, ao realizar o cumprimento de ações.

3) Levantamento das necessidades de treinamento e desenvolvimento: Utiliza o resultado de uma LNTD para gerar plano de sugestões de ações.

4) Mapa de conhecimento: Utiliza o mapa de conhecimento do funcionário para gerar plano de sugestões de ações.

5) Avaliação de desempenho: Utiliza a estrutura de participantes de uma AD no gerenciamento do PDI.

6) Questionários da Avaliação de Desempenho: Exibe os questionários respondidos na AD no gerenciamento do PDI.

7) E-mail Customizado: Utilizado para enviar e-mail para os avaliadores.

**1 – Cadastro**

Acessar Acompanhamento| PDI para criar um novo registro.

Cód. PDI: campo descritivo que contém identificador único;

Descrição: campo descritivo para nomear o PDI;

Data Início/Data Fim: campo que controla a data de início e data limite para execução;

Permitir visualizar próprio PDI: campo que determina se um colaborador pode visualizar o seu próprio PDI na tela de gerenciamento no Totvs Portal;

Permitir ao próprio avaliado definir seu PDI: campo que determina se um colaborador pode definir/gerenciar o seu próprio PDI na tela de gerenciamento no Totvs Portal. Este campo somente será habilitado se o campo "Permitir visualizar próprio PDI" estiver marcado;

Utiliza metas para o desenvolvimento de requisitos de acesso: campo que determina se o PDI em questão possuirá suporte à utilização de requisitos de acesso nas ações (metas) do PDI, ou seja, se o colaborador avaliado pode receber requisitos de acesso a partir do cumprimento das ações definidas em seu plano de desenvolvimento;

Preenchimento de requisito de acesso obrigatório: campo que determina se o preenchimento do requisito de acesso ao criar ação no Totvs Portal é obrigatório. Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de requisitos de acesso" esteja marcado;

Habilitar sugestões de ações para o funcionário: campo que determina que no Totvs Portal o usuário terá acesso a funcionalidade Sugestão de Ação. Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de requisitos de acesso" esteja marcado;

Tipos de restrição para associação de requisitos às metas: campo que determina o tipo de restrição que o sistema irá realizar nas competências que estarão disponíveis no PDI. Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de competências" esteja marcado.

**Observação:**

Essas restrições são aplicadas somente sobre as Novas Ações que poderão ser criadas no portal. Ao realizar o processo de "Carregar sugestões de competências" serão exibidas as competências que estejam associadas à metas.

Exibir somente competências definidas na meta: Serão disponibilizadas no Portal ao criar uma nova ação as competências vinculadas à meta (Meta|Anexo|Competências).

Exibir somente competências definidas no mapa de conhecimento do funcionário: Serão disponibilizadas no Portal ao criar uma nova ação as competências com status "Não possui a competência" no Mapa de conhecimento por competências do funcionário.

Exibir somente competências definidas na meta e que estejam definidas no mapa de conhecimento do funcionário: Serão disponibilizadas no Portal ao criar uma nova ação as competências que estiverem associadas à meta e simultaneamente vinculadas ao mapa de conhecimento por competência do funcionário.

Sem Restrição: Será disponibilizada no Portal ao criar uma nova ação todas as competências cadastradas no sistema. ;

Utiliza metas para o desenvolvimento de competências: campo que determina se o PDI em questão possuirá suporte à utilização de competências nas matas do PDI, ou seja, se o colaborador avaliado pode receber competências a partir do cumprimento das ações definidas em seu plano de desenvolvimento.

Preenchimento de competência obrigatório: campo que determina se o preenchimento da competência ao criar ação no Totvs Portal é obrigatório. Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de competências" esteja marcado.

Habilitar sugestões de competência para o funcionário: campo que determina que no Totvs Portal o usuário terá acesso a funcionalidade Sugestão de Ação. Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de competências" esteja marcado.

Tipos de restrição para associação de requisitos à metas: campo que determina o tipo de restrição que o sistema irá realizar nas competências que estarão disponíveis no PDI. Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de competências" esteja marcado.

Uma vez definido que um PDI possuirá suporte à gestão de Requisitos de Acesso, será necessário definir os tipos de requisitos que poderão ser utilizados no processo. Para isso o campo "Tipos de restrição para associação de requisitos à Metas" possuirá as opções que restringem à utilização dos requisitos, que são:

- Exibir somente requisitos definidos na meta

- Exibir somente requisitos definidos no mapa de conhecimento do funcionário

- Exibir somente requisitos definidos na meta e que estejam definidos no mapa de conhecimento do funcionário

- Sem restrição

Observações:  Campo descritivo que contém observações gerais sobre o PDI em questão;

Instruções: campo de texto livre que deve conter informações sobre o PDI e que serão exibidas ao usuário na tela de gerenciamento de PDI no Totvs Portal;

Gestão de Metas: campo que deve conter uma meta base do tipo "agrupadora" que contém metas associadas para serem a base da criação das ações no PDI para os avaliados; Ao acionar o botão "Incluir todas as metas associadas", serão adicionadas neste campo todas as metas associadas à meta Pai e estas serão a base para criação das ações dos avaliados do PDI pelo Totvs Portal.

Questionário: será possível associar um questionário a um PDI. Após responder as questões, o questionário não poderá ser removido do PDI.

Avaliação de Desempenho: campo que contém o código de uma Avaliação de Desempenho e realiza o vínculo da mesma com o PDI em questão. Uma vez definido este vínculo, o PDI utilizará a estrutura de participantes existente na Avaliação de Desempenho e criará uma estrutura de participantes idêntica. Contudo, para que esta estrutura seja gerada, o usuário deverá executar o processo "Gerar PDI a partir da AD associada". Liberar PDI

somente após encerramento da AD: campo que determina que o PDI somente ficará disponível para utilização, no Totvs Portal, após o encerramento da AD vinculada.  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Participantes

|  |  |
| --- | --- |
|  | Como Fazer |

---

Configurar Participantes   
Gerar PDI a partir da avaliação desempenho associada   
Carregar sugestão de ação por LNTD   
Enviar e-mail para os Avaliadores do PDI  
Gerar ações para o PDI a partir do Mapa de Conhecimento  
PDI no Totvs Portal
