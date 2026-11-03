---
content_hash: 5f76755543eac17dcdf8006333459d3ff832ee1628135665c742edb285ca90ea
fetched_at: '2026-06-29T00:10:30.537021+00:00'
page_id: '520106530'
product: rm
source: tdn-rm
title: RMPAT00004_Relatório de Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520106530
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.14 Ou superior |
| **Ocorrência:** | Relatório de Contabilização |
| **Ambiente:** |  |
| **Passo a passo:** | O relatório de contabilização tem por objetivo apresentar toda movimentação patrimonial já contabilizada e integrada ou não ao Totvs Gestão Contábil.  Ou seja, através deste relatório é possível apurar dados de contabilizações de aquisições, transferências, ocorrências, depreciações e correções que já tenham sofrido o processo de contabilização, que não tenham sido integrados ao módulo contábil e também as contabilizações já integradas ao módulo Contábil.  **Regras para Emissão do Relatório** Como pré-requisitos para composição deste relatório deverão ser importados, no [RM Report](https://tdn.totvs.com/pages/viewpage.action?pageId=286747760)s, a estrutura do relatório de Contabilização e Contabilização por Filial. A estrutura do relatório de contabilização apresenta as informações de forma agrupada, ou seja, mesmo que filiais especificas sejam previamente selecionadas na primeira etapa de parametrização o relatório será exibido apenas com um totalizador, sem realizar quebra por filial. Diferentemente do que ocorre quando a estrutura utilizada é a do relatório de contabilização por filial. Optando por este layout (contabilização por filial) , os totalizadores serão apresentados repeitando as filiais e contas contábeis selecionadas. Por exemplo, as contabilizações de aquisições do grupo de patrimônio  01 terá um totalizador para a filial 01, depois para a filial 02 e assim sucessivamente.  Os relatórios exibirão apenas as informações contidas dentro do período de cálculo em aberto (definido no fechamento de período), e períodos liberados pela Liberação de Competência. Até mesmo por que, operacionalmente não existe possibilidade de haver contabilizações pendentes para integração, de data anterior e posterior ao período em aberto.  **Emissão do Relatório de Contabilização** Deverão ser informados os meses e anos, respectivamente, iniciais e finais desejados para apuração (seleção do período) e o cenário de cálculo correspondente a estes patrimônios.        Caso seja necessário pode-se selecionar uma ou mais filiais e/ou faixa de contas contábeis. Desta forma somente as contabilizações que envolvem esta parametrização serão exibidas. O relatório de Contabilização permite totalizar cada conjunto de informações definidas, neste caso, como de aquisições, ocorrências, transferências, depreciações e correções.  A totalização pode ser realizada para cada um dos conjuntos acima ou para todos. Além da possibilidade de imprimir estas contabilizações por centro de custo. Como obrigatoriedade, para composição da estrutura das informações, deve ser informado o relatório (Contabilização ou Contabilização por filial).  Depois de realizada a correta parametrização, o relatório poderá ser executado, sendo que ao seu final serão apresentados o próprio relatório e o log contendo todas as informações referentes à execução do processo. |
| **Observações:** |  |
