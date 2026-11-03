---
article_id: 360060477354
category: SIGAEST - CUSTOS
content_hash: d56d6731e7b18a6ec34e4fce063ac5db8193c1e9a67fc5e790c0dbca9cd962d0
fetched_at: '2026-06-28T22:39:02.156221+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - EXECAUTO
  (Execução Automática) da rotina
type: support-article
updated_at: '2021-09-29T16:56:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060477354-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-EXECAUTO-Execu%C3%A7%C3%A3o-Autom%C3%A1tica-da-rotina
---

**Dúvida**Como executar a rotina MATA330 de forma automática?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Por meio desta rotina, o Sistema calcula o custo médio ou contábil de forma on-line a cada valorização dos estoques dos produtos com base nas novas entradas de matérias-primas somadas aos saldos existentes.

Essa rotina pode ser executada com o Sistema em uso por todos os usuários. Nesse caso, as movimentações que estão acontecendo simultaneamente ao cálculo podem influir no resultado. Para que a rotina seja executada dessa forma, o parâmetro **MV\_CUSTEXC** deve estar com o conteúdo igual a "**N**".  
Outra forma de execução (mais segura) é com o Sistema em modo exclusivo, sem outros usuários utilizando os arquivos necessários ao cálculo. Para que a rotina seja executada dessa forma, o parâmetro **MV\_CUSTEXC** deve estar com o conteúdo igual a "**S**".  
Se o usuário quiser fazer os lançamentos automáticos somente no final do mês/período, deve definir o parâmetro **MV\_CUSMED** com "**M**". Consulte o manual do módulo Configurador para mais detalhes, assim, o custo médio pode ser refeito através da rotina "Recálculo do Custo Médio" de três formas diferentes:

• **Sequencial**: na ordem em que os movimentos aconteceram.  
• **Diária**: pelos movimentos de cada dia. Contempla todos os dias do período selecionado pelo usuário, sendo o início do período o conteúdo do parâmetro MV\_ULMES+1 e o conteúdo da pergunta “Data inicial”.  
• **Mensal**: pelos movimentos do mês/período. Contempla todos os dias do período selecionado pelo usuário, sendo o início do período o conteúdo do parâmetro MV\_ULMES+1 e o conteúdo da pergunta “Data inicial”.

No reprocessamento do custo médio são eliminados todos os lançamentos contábeis já realizados e gerados novamente.  
No custo diário/mensal, o Sistema considera primeiro as entradas (compras) e depois as saídas, do período. Vale ressaltar que os movimentos internos respeitam seus níveis e processo e, por esta razão, essa regra não se aplica a esses movimentos.

**Para obter o exemplo de uso da Rotina Automática para execução do Custo Médio(MATA330), clique no artigo abaixo:**

**[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Exemplo prático de Execução Automática da Rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010494141)**

**Saiba mais:**

*[MP - SIGAEST - Rotina MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-MP-SIGAEST-Rotina-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
