---
article_id: 1500004530301
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 54aa54c38db0ac46104c75a80882f11db84ef9b978eb87048c610016a7bdf56e
fetched_at: '2026-06-28T22:38:56.902429+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Pontos de
  Entrada da rotina Baixa de Pré-Requisição ao Armazém
type: support-article
updated_at: '2025-12-12T20:14:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004530301-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Pontos-de-Entrada-da-rotina-Baixa-de-Pr%C3%A9-Requisi%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

**Dúvida**

Quais são os Pontos de Entrada da rotina Baixa de Pré-Requisição ao Armazém - MATA185?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Veja abaixo os pontos de entrada relacionados à rotina MATA185 - Baixa de Pré-Requisição ao Armazém:

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada:** | **Título:** | **Descrição:** |
| [**MT185COR**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087714) | Manipulação de ítens na legenda | Descrição: LOCALIZAÇÃO: Na rotina de Baixa Pré-Requisições  EM QUE PONTO: Após a definição do array de cores da legenda padrão. |
| [**MT185FIL**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087715) | Adiciona Filtro na solicitação ao armazém | Descrição: LOCALIZAÇÃO: Function MatA185() - Responsável por baixar as Pre-requisicoes gerando as requisições.  EM QUE PONTO : Ponto de entrada utilizado para adicionar Filtro no Menu da mBrowse das solicitações ao armazém (SCP) |
| [**M185FILB**](https://tdn.totvs.com/pages/releaseview.action?pageId=651920289) | Verificação de filtros na Mbrowse da Função MATA185 | Ponto de entrada localizado na rotina Baixa as Pre-requisicoes gerando as requisições  EM QUE PONTO: Será executado antes que seja exibida a tela principal da rotina. Este ponto de entrada tem como objetivo permitir que o usuário filtre os dados a serem exibidos. |
| [**M185BAIX**](https://tdn.totvs.com/pages/viewpage.action?pageId=236592014) | Customiza baixa de pré-requisição | Descrição: LOCALIZAÇÃO: Function A185Baixar() - Responsável pela chamada da função para o tipo de baixa.  EM QUE PONTO : Logo no inicio da rotina A185Baixar. O Ponto de Entrada M185BAIX possibilita customizar a execução da baixa da pre-requisição. |
| [**M185GRV**](https://tdn.totvs.com/display/public/PROT/M185GRV) | Ponto após a gravação do registro na tabela SD3 | Localização: Function A185Gera(Gera requisicoes.) e A185GeraAut(Gera as requisicoes usando o Movimentos Modelo 2).  Em que ponto: E chamado apos a gravação de todos os dados, inclusive apos gerar a requisição no arquivo de movimentos internos (SD3). |
| [**MT185BUT**](https://tdn.totvs.com/pages/releaseview.action?pageId=311633965) | Adiciona opções no menu da rotina | Ponto de entrada MT185BUT  permite adicionar botões customizados |
| [**M185MOD1**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087555) | Validação da baixa da pré-requisição mod1 | Descrição:  LOCALIZAÇÃO : Function A185Manual() - Responsável pelas baixas das Pre-requisicoes.  EM QUE PONTO : Ponto de entrada utilizado na validação da baixa da pre-requisição modelo 1 (manual). |
| [**MT185SD3**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087718) | Atualiza informações na SD3 | LOCALIZAÇÃO : Function A185AtuSD3 - Função responsável pela atualização das variáveis de memoria para Inclusão no SD3.  EM QUE PONTO : No final da Função, após já ter executado as atualizações dos demais campos da tabela SD3.. Neste ponto de entrada poderão ser atualizadas informações da tabela SD3 com informações da tabela SCP, conforme exemplo abaixo, ondo é atualizado o campo ('D3\_DOC') com o conteúdo do ('CP\_NUM'). |
| [**M185VLDEXC**](https://tdn.totvs.com/pages/releaseview.action?pageId=651919975) | Responsável pela exclusão das pré-requisições | LOCALIZAÇÃO : Function A185Exclui() - Responsável pela exclusão das Pre-Requisicoes.  EM QUE PONTO : Ponto de entrada localizado antes da validação e exclusão do registro no SC1 e atualização do campo B2\_QEMPSA. |
| [**M185EXCL**](https://tdn.totvs.com/pages/releaseview.action?pageId=651920399) | Exclusão das pré-requisições | LOCALIZAÇÃO : Function A185Exclui() - Responsável pela exclusão das Pre-Requisicoes.    EM QUE PONTO : É chamado antes da exclusao da pre-requisicao. Neste momento da chamada do ponto de entrada, o registro estara posicionado nos arquivos SCP, SCQ, SC1 e SB2. |
| [**MT185EST**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087996) | Validação de Estorno | Ponto de entrada localizado na função A185MovSD3, responsável por atualizar os dados do estorno das pré-requisições.EM QUE PONTO: Antes da execução do estorno, permitindo validar sua realização. |
| [**MT106CQ**](https://tdn.totvs.com/pages/releaseview.action?pageId=6085432) | Fornece informações relacionadas ao produto | LOCALIZAÇÃO : Function MaSAPreReq - Função responsável por avaliar solicitação ao armazém e gerar solicitações de compra ou autorizações de entrega para atender as necessidades  EM QUE PONTO : O ponto se encontra após a gravação do arquivo SCQ. Caso o produto tenha gerado autorização de entrega no processo de geração da pre-requisicao ira receber como parametro informacoes relacionadas num array |
| [**MT185LEG**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087717) | Manipulação de itens na legenda | LOCALIZAÇÃO: Na rotina de Baixa Pré-Requisições  EM QUE PONTO: Após a definição do array de textos da legenda padrão. |
| [**MA185ENC**](https://tdn.totvs.com/display/public/PROT/MA185ENC) | Encerramento de Pré-Requisições | Descrição:  LOCALIZAÇÃO : Function A185Encer() - Responsável pelo Encerramento de Pre-Requisicoes.  EM QUE PONTO : Este ponto de entrada está localizado após todas as atualizações dos arquivos relacionados ao encerramento da pré-requisição. |
| [**MT185BX**](https://tdn.totvs.com/display/public/PROT/MT185BX) | Montagem dos dados para a baixa da Pré-Requisição | LOCALIZAÇÃO : Function A185Automa( ) função responsável pela montagem dos dados para baixa da pre-requisição.  EM QUE PONTO : O ponto se encontra antes da montagem do array aCols onde se encontra o conteúdo dos campos a serem mostrados na baixa da pre-requisição Modelo 2. |
| [**M185MOD2**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087556) | Baixa de Pré-requisição Mod2 | LOCALIZAÇÃO : Function A185Automa() - Responsável pela baixa Total das Pre-requisicoes.  EM QUE PONTO : Ponto de entrada utilizado na validação da baixa da pre-requisição modelo 2 (automatica) |
| [**MT185DAD**](https://tdn.totvs.com/display/PROT/TSVMZY_DT_PONTO_DE_ENTRADA_MT185DAD) | Validação dos itens da baixa ou manipulação dos itens que serão baixados. | Validação dos itens da baixa ou manipulação dos itens que serão baixados. |
| [**MT185GERA**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087716) | Verifica estoque disponível | LOCALIZAÇÃO : Function A185GeraAut( ) função responsável pela montagem dos dados para baixa da pre-requisição.  EM QUE PONTO : O ponto se encontra antes da validação da quantidade da baixa para verificar se existe estoque disponível para realização da baixa da pre-requisição. |
| [**M185FGR**](https://tdn.totvs.com/display/public/PROT/M185FGR) | Responsável por gerar as requisições usando o Movimentos Modelo 2 | LOCALIZAÇÃO : Function A185GeraAut() - Responsável por gerar as requisições usando o Movimentos Modelo 2.  EM QUE PONTO : Ponto de Entrada no final do processo de baixa total das pre-requisicoes, após o controle de transação. |
| [**M185CAMP**](https://tdn.totvs.com/display/public/PROT/M185CAMP++-+Carga+de+Movimentos+no+aCols) | Carga de Movimentos no aCols | LOCALIZAÇÃO : Function A185Atu2SD3( ) - Função responsável por realizar a carga dos movimentos no aCols da rotina de movimentação interna modelo 2.  EM QUE PONTO : O ponto de entrada se encontra após a carga de linha do aCols. |
| [**MTA185MNU**](https://tdn.totvs.com/pages/viewpage.action?pageId=469438744) | Manipulação do menu funcional do processo de Baixa de Pre-Requisição | O ponto de entrada para permitir manipular o menu funcional da tela de baixa de pré-requisição(MATA185). Permitindo incluir novas funções ou retiradas para as disponibilizadas no produto padrão. Para sua implementação, é obrigatório a utilização da variável aRotina que possui o escopo Private derivado da sua implementação na função MenuDef(). |
| [**MT185OK**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087935) | Validar os dados da baixa de Pré-Requisição | Localização: Está localizado na função A185Manual que tem o Objetivo de Baixa das Pre-requisicoesQuando: O Ponto de Entrada é chamado após clicar no botão OK da tela  Finalidade: O Ponto de Entrada tem o Objetivo de validar os dados após clicar no OK da Enchoicebar |

**Saiba mais:**

[*MP - SIGAEST - MATA310/MATA311 - Pontos de entrada da rotina Transferência entre Filiais*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082)

[*MP - SIGAEST - MATA175 - Pontos de Entrada da rotina Baixa de CQ*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004325941)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
