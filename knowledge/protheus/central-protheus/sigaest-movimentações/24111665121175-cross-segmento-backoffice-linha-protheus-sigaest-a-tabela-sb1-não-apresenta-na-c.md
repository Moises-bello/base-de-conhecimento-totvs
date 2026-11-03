---
article_id: 24111665121175
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 910ae7c4012795ed3710bf7399dd7e471b0f73b906ab7586ac98b6af167ac102
fetched_at: '2026-06-28T22:38:54.265158+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - A tabela SB1 não apresenta
  na Consulta Genérica
type: support-article
updated_at: '2024-06-11T18:59:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24111665121175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-A-tabela-SB1-n%C3%A3o-apresenta-na-Consulta-Gen%C3%A9rica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24111697520919) Tempo aproximado para leitura: **00:02:00 min****Dúvida**O que fazer quando, ao pesquisar a tabela SB1 na Consulta Generica, não aparece a tabela?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Para apresentar a tabela SB1 na rotina Consulta Genérica é necessário avaliar as hipoteses abaixo:

**Hipotese 1 - Privilégios customizados que tiram a possibilidade dos usuários visualizarem o SB1 na Consulta Genérica. Siga as etapas para validar essa possibilidade:**

1. Acessar no SmartClient o **SIGACFG**.

2. No configurador, acessar a opção do **Menu Usuário - Senhas - Privilégios**.

3. No Cadastro do Privilégio, clicar em incluir, informa uma Regra e um Comentário por obrigátorio, configurar conforme o Print,  e avaliar se a coluna Rotina do menu está conforme o nativo do Protheus.![](https://centraldeatendimento.totvs.com/hc/article_attachments/24111665083543)![](https://centraldeatendimento.totvs.com/hc/article_attachments/24111697525527)

4. Caso tenha alguma função customizada na opção Rotina do menu, esse é o motivo da tabela SB1 não estar aparecendo na Consulta Genérica, todas as funções do Cadastro do Produto devem estar conforme o padrão (print da etapa 3)

5 . Depois de ter cadastrado o Privilégio é necessário verificar se esse Privilégio está amarrado ao Grupo, no caminho a seguir **Usuário - Senhas - Grupos**. Selecione o seu usuário, clique em "Outras Ações" -> "Privilégio".![](https://centraldeatendimento.totvs.com/hc/article_attachments/24111665089687)

6. Clicando em **Privilégio,** observe que a coluna **Regra** terá a amarração do privilégio informado anteriormente.![](https://centraldeatendimento.totvs.com/hc/article_attachments/24111665093015)

7. Esse mesmo Privilégio temos também para usuário no seguinte caminho: **Usuáro - Senhas - Usuários**, clicando em "Outras Ações" -> "Privilégio".![](https://centraldeatendimento.totvs.com/hc/article_attachments/24111697534743)

8. Nessa opção terá o privilégio também amarrado ao usuário, conforme o Print.![](https://centraldeatendimento.totvs.com/hc/article_attachments/24111665103383)

9. É necessário avaliar se o usuário ou grupo tem o privilégio do cadastro do produto e ter a opção permitida do privilégio para aquele determinado usuário, dessa forma todos os acessos serão liberados para aquele usuário em específico e o mesmo terá acesso a tabela SB1 na rotina Consulta Genérica.

**Hipotese 2 - SB1 desmarcada na rotina do Menu. Valide essa hipotese por meio das etapas abaixo:**

1. Acessar no SmartClient o **SIGACFG**.

2. No configurador, acessar a opção do **Menu Ambiente - Cadastros - Menus**

3. Marque apenas o check-box do menu Estoque/Custos e clique em OK

4. Após carregar o menu, clique no ícone "Adicionar", conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24112684902935)

5. Selecione a rotina da Consulta Genérica e clique em Detalhes. Em seguida marque o check-box SB1![Exibindo image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEWB5qOI7s5mUJOLWD%2FDE8AowQhAOljGYCCGScLlTkvzMNM0EXgMd5rjRePBmMrWFqg%2F3N6OSn9M%2FY2pu0cvlOk%2FzteMrpr34pfeJBMgbbyBKFP8ovb2vKMF8kikDpuoEJkM2dxcqEBzgDWKHwYDgGV%2B9kgvctCZ8RIVJ1llDMR7sxDiP5%2BIbjRO1yiINhv1pCZV0zDws6T527OdC88agRkJxUoiMLfMKNlE%2FuAgAfUYQs07pYX2l%2FtE6LRyIqOy3SmmAYkpdpZtKxPGiFGNW%2B9ldxtRj1Cs7u6fAut3zxdGj5ICTnnhNEkDSFUWyOIlV5NB%2BUpsFpAB2Oj2ra%2BG0Wu0cl94DRQg0C9zbAygA5T%2FkDeee4WQO7zQHaW69Bxp9BTd1QpNyV%2BfziMG%2FcWCRePxbysK7pV5dSougvz6Cskfo2plbFKMhtIx4ZRS%2FLfKWweTk1lmfhAhemt8feLKYTcNC94%2BCpPIJdeY6TgxSwTix8UepFZHD2v8MwuT5R%2Fxcebxn%2B0Iin59lQtBOyudjKsAPwxF%2FBz85bI1edHuZ2VhbgUe819b95BeG7wfBqA%3D&sz=w1503-h955)

6. Clique para Gerar o Menu, podendo dar o mesmo nome original para substituir (SIGAEST)![](https://centraldeatendimento.totvs.com/hc/article_attachments/24112513108119)

Essas são as 2 hipoteses comuns onde o arquivo SB1 não exibe na Consulta Genérica.

**Saiba Mais:**

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
