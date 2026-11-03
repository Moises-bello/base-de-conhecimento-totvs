---
content_hash: d4533bbce331e9b30b5af5d19d4fb797164edb2d8c7221a0f37142995609ad0f
fetched_at: '2026-06-29T00:06:08.084317+00:00'
page_id: '201744106'
product: rm
source: tdn-rm
title: ER_Avaliar_Competencia_PDI
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Avaliar_Competencia_PDI
version: 17
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Desenvolver Competências através de metas no PDI (Plano de Desenvolvimento Individual).

## Definição da Regra de Negócio

O PDI (Plano de Desenvolvimento Individual) será alterado para possibilitar o desenvolvimento de competências através de metas no processo de PDI. Para isso será disponibilizado no cadastro de PDI que se encontra no caminho **RH > Gestão de Pessoas > Acompanhamento> PDI** uma série de configurações para possibilitar o desenvolvimento de competências através de metas, as quais encontram-se abaixo:

* Utiliza metas para desenvolvimento de competências
* Preenchimento de competência obrigatório
* Habilitar sugestão de competências para o funcionário
* Exibir somente competências definidas na meta
* Exibir somente competências definidas no mapa de conhecimento do funcionário
* Exibir somente competências definidas na meta e que estejam definidas no mapa de conhecimento do funcionário
* Conceder competência automaticamente (Concede a competência automaticamente no final do lançamento de metas do PDI se a meta for aprovada)

Como o desenvolvimento de competências será através de metas também iremos criar um novo anexo chamado **"Competências Vinculadas"** que será somente leitura e somente exibirá as competências vinculadas a meta selecionada. De forma similar ao funcionamento de requisito de acesso vinculados a meta, as competências somente serão vinculadas através de processo, por isso iremos criar um processo chamado **"Vincular/Desvincular Competências a Meta"**. Este processo irá disponibilizar as competências e as metas para o usuário realizar o vínculo. O processo deve funcionar de forma similar ao processo de vinculação de requisitos de acesso, porém realizando a vinculação de competências a meta.

No portal onde se encontram as funcionalidade de PDI, também serão feitas modificações. Teremos na opção de lançamento de ações a opção de preencher também escolhendo competências. Será similar a escolha de requisito de acesso que já existe hoje no sistema, porém funcionará com competências. O Usuário só poderá lançar ações para competências ou para requisitos de acesso, para isso teremos uma opção de escolha no momento de lançamento da ação, se o usuário escolher lançar competências será carregado as opções de competências disponíveis de acordo com as configurações realizadas no PDI anteriormente.

Também será alterado no portal a opção de sugestões da ação. O menu atual irá mudar de nome para **"Carregar Sugestões de Requisito de Acesso"** e irá sugerir somente ações relacionadas com requisitos de acesso, seu comportamento não sofrerá mudanças. Será criado um novo menu chamado **"Carregar Sugestões de Competências"** que deverá sugerir as ações relacionadas com as competências, essa funcionalidade irá funcionar de forma similar ao de sugestão de requisito de acesso.

Caso as opções de competências não estejam marcadas no cadastro de PDI as opções relacionadas a competências do PORTAL não devem ser exibidas. 

Será implementada uma nova funcionalidade para Geração de PDI a partir do Mapa de conhecimento do participante. A funcionalidade consiste em trazer as competências e, ou, requisitos de acesso que estejam definidos no mapa de conhecimento daquele participante. Para isso, será criado um novo processo **"Gerar ações para o PDI a partir do Mapa de conhecimento"**. Este novo processo terá duas opções de escolha para execução: **"Gerar ações do PDI para Competências"** e **"Gerar ações do PDI para Requisitos de Acesso".**Ambos os parâmetros deste processo somente estarão disponíveis se estiverem habilitados no PDI através dos parâmetros: **"Utilizar Requisitos de Acesso"**, **"Utilizar Competências"**. O processo também deve seguir as regras configuradas no PDI relativa a competências e, ou, relativas a requisito de acesso, definido o resultado de ações a serem geradas para o PDI do participante.

Ao final deste processo os participantes do PDI  já terão suas ações (Metas que tenha competências associadas) carregadas automaticamente na parte Web, restando somente a aprovação ou reprovação da ação. Caso a ação for concluída com 100% e o parâmetro **"Conceder competência automaticamente"** esteja marcado no cadastro de PDI, o participante irá receber a competência com a maior graduação exigida definida no mapa de conhecimento. Caso não tenha definição no mapa de conhecimento para a competência definida na Meta, o participante irá receber a competência com a graduação de menor valor cadastrado no sistema.

Será implementado no PDI o conceito de questionários igualmente como utilizado na avaliação de desempenho. Para isso será vinculado no cadastro de PDI o cadastro de questionários e este ficará disponível em **(RH > Gestão de Pessoas > Acompanhamento > PDI > Questionário)**. Os questionários cadastrados no PDI serão exibidos na criação de ações do PDI no portal para preenchimento de informações conforme definição. Os campos não serão obrigatórios. 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de PDI | [Alteração] | [RH -> Gestão de Pessoas -> Acompanhamento -> PDI] | - |
| Cadastro de Metas | [Alteração] | [RH -> Gestão de Pessoas -> Acompanhamento -> Gestão de Metas] | - |
| PDI (Portal) | [Alteração] | [Portal -> Recursos Humanos -> Gestão Por Competências -> PDI] | - |

***Tabelas Utilizadas***

* *VPDI - Tabela de Cadastro de PDI*
* *VGMETAREQACESSO – Tabela de Requisitos de Acesso vinculados a Meta*
* **VGMETACOMPETENCIA - Tabela de Competências vinculadas a Meta**
* **VGMETALANCAMENTO - Tabela de Lançamento de Metas**

## Protótipo de Tela

1 - Processo de vinculação de Competências a Metas

2 - Anexo de Competências na Meta

**- Cadastro de PDI com novas opções de parametrização relacionados a competências**

*4 - Lançamento de Ações*

5 - Sugestão de Ações

6 - Processo para Gerar PDI

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
