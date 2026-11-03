---
content_hash: 89dc19bb5d0d3053ad4562f9b2691e09082d21f68c38b9bde45e51a71f55627c
fetched_at: '2026-06-29T00:09:24.675877+00:00'
page_id: '423937991'
product: rm
source: tdn-rm
title: Relatório de Contabilização 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937991
version: 3
---

O relatório de contabilização tem por objetivo apresentar toda movimentação patrimonial já contabilizada e ainda não integrada ao Totvs Gestão Contábil.  Ou seja, através deste relatório é possível apurar dados de contabilizações de aquisições, transferências, ocorrências, depreciações e correções que já tenham sofrido o processo de contabilização, porém não tenham sido integrados ao módulo contábil. Pois a partir do momento que a integração é realizada, não existe a possibilidade de visualização através do relatório de contabilização.

**Regras para Emissão do Relatório**

Como pré-requisitos para composição deste relatório deverão ser importados, no RM Reports, a estrutura do relatório de Contabilização e Contabilização por Filial. A estrutura do relatório de contabilização apresenta as informações de forma agrupada, ou seja, mesmo que filiais especificas sejam previamente selecionadas na primeira etapa de parametrização o relatório será exibido apenas com um totalizador, sem realizar quebra por filial. Diferentemente do que ocorre quando a estrutura utilizada é a do relatório de contabilização por filial. Optando por este layout, os totalizadores serão apresentados repeitando as filiais e contas contábeis selecionadas. Por exemplo, as contabilizações de aquisições do grupo de patrimônio 01 terá um totalizador para a filial 01, depois para a filial 02 e assim sucessivamente.

Os relatórios exibirão apenas as informações contidas dentro do período de cálculo em aberto (definido no fechamento de período). Até mesmo por que, operacionalmente não existe possibilidade de haver contabilizações pendentes para integração, de data anterior e posterior ao período em aberto.

**Emissão do Relatório de Contabilização**

Inicialmente deverão ser informados os meses e anos, respectivamente, iniciais e finais desejados para apuração (seleção do período) e o cenário de cálculo correspondente a estes patrimônios. Lembrando que o cenário de cálculo é definido no grupo de patrimônios que está associado ao patrimônio.

Caso seja necessário pode-se selecionar uma ou mais filiais e/ ou faixa de contas contábeis. Desta forma somente as contabilizações que envolvem esta parametrização serão exibidas.

O relatório de Contabilização permite totalizar cada conjunto de informações definidas, neste caso, como de aquisições, ocorrências, transferências, depreciações e correções. A totalização pode ser realizada para cada um dos conjuntos acima ou para todos. Além da possibilidade de imprimir estas contabilizações por centro de custo.

Como obrigatoriedade, para composição da estrutura das informações, deve ser informado o relatório (Contabilização ou Contabilização por filial).

Depois de realizada a correta parametrização, o relatório poderá ser executado, sendo que ao seu final serão apresentados o próprio relatório e o log contendo todas as informações referentes à execução do processo.

Veja Também
