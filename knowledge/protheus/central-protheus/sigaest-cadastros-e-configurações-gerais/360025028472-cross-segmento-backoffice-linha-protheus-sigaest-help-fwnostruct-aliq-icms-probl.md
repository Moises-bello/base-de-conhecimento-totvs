---
article_id: 360025028472
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 5df5178d9254aa7bad4519ff8bf6f9c568183cef1b89dae7355efa1dd142fd5c
fetched_at: '2026-06-28T22:39:07.898109+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Help FWNOSTRUCT:
  Aliq. ICMS Problema: Valor atribuído difere da estrutura do campo (Aliq. ICMS)'
type: support-article
updated_at: '2022-09-05T13:50:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025028472-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-FWNOSTRUCT-Aliq-ICMS-Problema-Valor-atribu%C3%ADdo-difere-da-estrutura-do-campo-Aliq-ICMS
---

**Ocorrência**Na rotina MATA010 - Cadastro de Produtos, quando incluído/alterado NCM (**B1\_POSIPI**) ocorre o seguinte HELP abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023792432/mceclip0.png)

Como resolvê-lo?  
**Ambiente**Protheus – Estoque/Custos – A partir da 12.1.17  
  
**Causa**Este Help ocorre, pois a ordem padrão do campo foi alterada, este campo é bloqueado pois há aCols e Arrays em fontes que precisam da posição padrão.  
  
**Solução**Para solucionar essa ocorrência, primeiro aplique o pacote acumulado do módulo de Estoque/Custos (**[clique aqui e faça o download conforme a sua release](https://tdn.totvs.com/pages/viewpage.action?pageId=522000602)**). Após aplicação do pacote, caso persistir com o problema, **realize os passos detalhados abaixo** criando a consulta padrão da tabela SYD4 utilizada para o campo B1\_POSIPI**:**

**1.** Acessar o módulo Configurador (SIGACFG)  
Menu Base de Dados-> Dicionários -> Base de Dados;

![](https://tdn.totvs.com/download/attachments/528468928/cfg01.png?version=1&modificationDate=1578426505480&api=v2)

**2.** Ao expandir a árvore de componentes, selecione a opção "Consulta Padrão";

![](https://tdn.totvs.com/download/attachments/528468928/cfg02.png?version=1&modificationDate=1578426715747&api=v2)

Para incluir uma nova consulta, clique no ícone ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_15-53-7.png?version=1&modificationDate=1578426787747&api=v2).  
Informe:  
Em Tipo da Consulta:  
- Consulta Específica;  
Em Informações:  
- Consulta: SYD4;  
- Descrição: TEC4;

![](https://tdn.totvs.com/download/attachments/528468928/image2020-1-7_15-57-6.png?version=1&modificationDate=1578427027123&api=v2)

Clique em "Avançar";

**3**. Em Tabela, selecione: SYD - Nomenclatura Comum do Mercosul;  
Em Expressão: IF( FindFunction( 'M010GetNCM' ), M010GetNCM(), .T. )    
Em Retorno, clique no botão incluir ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_15-53-7.png?version=1&modificationDate=1578423187745&api=v2) e inclua a fórmula: IF( FindFunction( 'M010GetNCM' ), SYD->YD\_TEC, CriaVar( 'B1\_POSIPI', .F.) )

![](https://tdn.totvs.com/download/attachments/528468928/image2020-1-7_16-2-41.png?version=1&modificationDate=1578427362153&api=v2)

Clique em "Finalizar";

**4.** Clique em ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_16-8-23.png?version=1&modificationDate=1578427704257&api=v2)para retornar a árvore de componentes e selecione a opção "Base de Dados";

![](https://tdn.totvs.com/download/attachments/528468928/image2020-1-7_16-11-11.png?version=1&modificationDate=1578427872047&api=v2)

**5.** Clique em "Pesquisar" ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_16-12-10.png?version=1&modificationDate=1578427931127&api=v2), em Procurar Por: digite SB1 e clique em "Buscar";

![](https://tdn.totvs.com/download/attachments/528468928/cfg03.png?version=1&modificationDate=1578428178127&api=v2)

**6.** Clique em "Editar" ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_16-17-21.png?version=1&modificationDate=1578428241497&api=v2)para alterar as configurações da tabela. Ao expandir a árvore de componentes, selecione o componente "Campos", clique em "Pesquisar" ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_16-12-10.png?version=1&modificationDate=1578424331126&api=v2), no campo "Procurar Por" informe o campo B1\_POSIPI e clique em "Buscar";

![cfg04.png](https://tdn.totvs.com/download/attachments/528468928/cfg04.png?version=1&modificationDate=1578428553307&api=v2)

**7.** Clique em "Editar" ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_16-17-21.png?version=1&modificationDate=1578428241497&api=v2)para acessar as configurações do campo B1\_POSIPI. Ao abrir a tela com as informações do campo, clique na Aba "Opções" e no campo Cons. Padrão: informe a consulta padrão SYD4;

![](https://tdn.totvs.com/download/attachments/528468928/image2020-1-7_16-25-15.png?version=1&modificationDate=1578428715560&api=v2)

**8.** Clique em "Salvar" e depois Confirme a alteração ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_16-26-19.png?version=1&modificationDate=1578428780110&api=v2). O sistema vai apresentar uma tela informando que a tabela SB1 possui relacionamento de compartilhamento entre outras tabelas, clique em "Ok" para que ele retorne ao browser inicial de Dicionário de Dados.  
Clique em "Salvar" ![](https://tdn.totvs.com/download/thumbnails/528468928/image2020-1-7_16-29-19.png?version=1&modificationDate=1578428959767&api=v2)para que o sistema efetive o processo de alteração do Dicionário de Dados;

Após esse processo acima não apresentará mais o help FWNOSTRUCT

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
