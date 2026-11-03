---
content_hash: 1e3dcc502f00b4432e2ea9b1fb04612eb6a0a6d435d41373e280bb8ed0043ad8
fetched_at: '2026-06-29T00:10:19.027370+00:00'
page_id: '4813028'
product: rm
source: tdn-rm
title: Grupo de Relatório para Impressão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813028
version: 6
---

BLOCK

Grupo de Relatório para Impressão

FAQ: **Grupo de Relatório para Impressão**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema de forma que possa determinar os layouts de relatório que o usuário terá acesso?

* ***Definição do Processo***

A parametrização tem por finalidade determinar os usuários que poderão acessar e utilizar determinados layouts de relatórios na base. Esta consistência poderá ser feita “apenas” para os usuários que não estiverem parametrizados como “supervisor”.

Solução

* ***Parametrizações Necessárias***

Acessar **| Cadastro | Segurança |** e selecionar o usuário a ser parametrizado. A seguir editá-lo e acessar aba | **Configuração de Segurança |** onde o campo “supervisor” deve estar desabilitado. Ainda nesta aba verificar a qual perfil este usuário está associado em **| Perfis Associados |**.

Acessar **| Cadastro | Segurança | Perfil |** e editar o perfil associado ao usuário consultado. A seguir acessar a aba **| Acesso á Relatórios / Planilhas |** e clicar no ícone **| Incluir |** onde será aberta tela com o campo **| Grupo |**. A direita deste campo deverá clicar no ícone | [![clip_image002](http://lh6.ggpht.com/_G7KXZLoZDsY/TKUX4zgdAaI/AAAAAAAABVU/Nbtrtrp43Z0/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKUX4JmpbuI/AAAAAAAABVQ/wDI-_xSaTUQ/s1600-h/clip_image002%5B3%5D.jpg) | para que seja aberta tela **| Grupo de Relatórios |** para inclusão dos mesmos.

Depois de inclusos grupos de relatórios deverá preencher as informações abaixo na aba | **Acesso á Relatórios / Planilhas |:**

- Grupo: informar grupo de relatório a ser associado a este perfil. Serão apresentados apenas os grupos já criados previamente.

- Nível Alteração: Informe um número para o nível de alteração dos relatórios/planilhas.

- Nível Emissão: Informe um número para o nível de emissão dos relatórios/planilhas.

Acessar **| Relatórios | Gerador |** selecionar o layout desejado e clicar no ícone **| [![clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TKUX6hTJphI/AAAAAAAABVc/4uVmt0g4294/clip_image004_thumb.jpg?imgmax=800 "clip_image004")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKUX5oaiCHI/AAAAAAAABVY/5QcwzyJ6n8M/s1600-h/clip_image004%5B3%5D.jpg) - Editar |** onde o usuário deve preencher a informação do campo **| Nível de Acesso |** e **| Grupo de Relatórios |**.

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

- **Etapa Mov Impressão**

- Acessar **| Relatórios – Do Movimento |** e informar | Ação ao Cadastrar Movimento: escolher uma das opções que permita edição do layout a ser impresso |

* ***Descrição do Processo***

A inclusão do movimento será feita como de costume, porém ao selecionar o movimento através da visão e clicar no ícone **| [![clip_image006](http://lh3.ggpht.com/_G7KXZLoZDsY/TKUX8CMBJpI/AAAAAAAABVk/YgpF3u8r588/clip_image006_thumb.jpg?imgmax=800 "clip_image006")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKUX7ScI4DI/AAAAAAAABVg/EI1qS2UK1pk/s1600-h/clip_image006%5B3%5D.jpg) - Imprimir Documentos |** serão apresentados apenas os layouts que o usuário tem permissão de acessar. Estes layouts também não serão visualizados em **| Relatório | Gerador |** por falta de permissão.

* ***Informações Adicionais***

- Ao deixar o campo Grupo de Relatório “vazio” em **| Relatório | Gerador |** significa que não haverá nenhum impedimento para visualização ou utilização do mesmo.

- Usuários parametrizados como “supervisor” não farão consistência de Grupo de Relatório

- O usuário só poderá alterar/emitir um relatório/planilha que estiver configurado com nível de acesso menor ou igual ao nível do grupo correspondente no perfil do usuário. Não é possível inserir um valor para o nível de emissão menor que o nível de alteração.

- Os layouts serão visualizados e poderão ser utilizados obedecendo nível de alteração e nível de emissão configurados no “perfil” vinculado ao usuário. Desta forma, ao informar | Nível Alteração e Nível Emissão: 3 | significa que todos os relatórios que possuírem “Nível de Acesso” menor ou igual a 3 serão visualizados e poderão ser utilizados.
