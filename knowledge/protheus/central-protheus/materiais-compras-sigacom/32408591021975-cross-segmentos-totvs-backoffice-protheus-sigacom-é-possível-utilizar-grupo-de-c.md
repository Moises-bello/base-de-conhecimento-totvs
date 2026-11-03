---
article_id: 32408591021975
category: Materiais - Compras (SIGACOM)
content_hash: 18cd3d367658e7c4cd27a6c2c3e9b35c51b47897602508694efcd624fa2eb71b
fetched_at: '2026-06-28T22:41:17.569593+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível utilizar
  Grupo de Compras na Rotina de Análise de Cotação?
type: support-article
updated_at: '2025-05-28T17:54:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32408591021975-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-utilizar-Grupo-de-Compras-na-Rotina-de-An%C3%A1lise-de-Cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32408577027735) Tempo aproximado para leitura: **00:05:00min** **Dúvida**É possível utilizar Grupo de Compras na Rotina de Análise de Cotação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus compras - Todas as versões

**Solução**

|  |  |
| --- | --- |
| **Produto:** | Protheus. |
| **Ocorrência:** | Para que o Análise da Cotação respeite o Cadastro de Grupo de Compras, quando o Campo Análise da Cotação estiver marcado como Não, é importante os seguintes procedimentos preliminares antes de iniciar o processo de Solicitação de Compras. |
| **Passo a passo:** | - Ativar o parâmetro: MV\_RESTCOM para S - No Cadastro de Produtos, definir o Grupo de Compras padrão (B1\_GRUPCOM) para o Produto ou no Cadastro de Solicitantes, definir o Grupo de Materiais, Produtos e qual o Grupo de Compras que está amarrado a este processo.  Desta forma, ao gerar a solicitação de compras (SC1), o campo: C1\_GRUPCOM será gravado conforme a amarração que foi efetuada. Após efetuar a Geração e Atualização da Cotação a solicitação de compras aprovada (SC8) também estará com o campo:  C8\_GRUPCOM gravado inicialmente na tabela SC1 e carregado para a tabela SC8.  Em seguida, ao entrar no Programa de Análise da Cotação e clicar em Analisar, o sistema não deverá permitir a análise da cotação que estiver nesta condição. Porém, se o parâmetro MV\_RESTCOM estiver = "N" a análise irá funcionar normalmente.  Caso seja incluído o Solicitante (Adm Compras - Solicitantes), poderá ser amarrado junto ao solicitante, o Grupo de Compras para o mesmo, caso não seja amarrado o Grupo de Compras no produto, conforme exemplo:  Grupo = \* / Produto= \* / Domínio= I(Inclui) / Grupo de Compras="nro. do Grupo de Compras. |
| **Observações:** | Via Configurador, também é possível travar o botão de “Analise de Cotação”, acessar o cadastro do usuário que não pode Analisar Cotações, acessar Detalhes - Acessos - desmarcar a opção "Analisar Cotações", desta maneira o botão ficará desabilitado para o comprador. |

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido cadastro de Grupo de Compras ( MATA086 ) no Módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9016158177175-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-definido-cadastro-de-Grupo-de-Compras-MATA086-no-M%C3%B3dulo-de-Compras)

[PCOM10006 - Analise de Cotação - Grupos de compras](https://tdn.totvs.com/pages/releaseview.action?pageId=285642623)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Restrição de Solicitantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11491127349911)

[PCOM09005 - Solicitantes (MATA084)](http://tdn.totvs.com/pages/releaseview.action?pageId=274630904)

[PCOM06003 - Como funciona o bloqueio de solicitação de compras?](https://tdn.totvs.com.br/pages/releaseview.action?pageId=233754768)

[PCOM06006 - Cadastro de Solicitante e Solicitação de Compra](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=286735615)

[5967493 DMANMAT02-19255 DT Asterisco no campo DBK\_CC](https://tdn.totvs.com/display/public/PROT/5967493+DMANMAT02-19255+DT+Asterisco+no+campo+DBK_CC)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
