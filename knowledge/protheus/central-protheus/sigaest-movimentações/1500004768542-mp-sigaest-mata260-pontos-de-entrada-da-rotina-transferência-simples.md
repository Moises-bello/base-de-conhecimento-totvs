---
article_id: 1500004768542
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 080985f5e6649fac1b00396de39b9439bd5e23cf6dd12e75ef651126a632fb42
fetched_at: '2026-06-28T22:38:58.614793+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - MATA260 - Pontos de Entrada da rotina Transferência Simples
type: support-article
updated_at: '2021-04-28T15:44:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004768542-MP-SIGAEST-MATA260-Pontos-de-Entrada-da-rotina-Transfer%C3%AAncia-Simples
---

**Dúvida**Quais são os Pontos de Entrada da rotina MATA260 - Transferência Simples?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Veja abaixo os Pontos de Entrada relacionados à rotina MATA260 - Transferência Simples (clique no nome do Ponto de Entrada para obter maiores detalhes):

|  |  |  |
| --- | --- | --- |
| **Nome:** | **Título:** | **Descrição:** |
| **[MT260FIL](https://tdn.totvs.com/display/public/PROT/MT260FIL+-+Filtra+Mbrowse+do+programa+MATA260)** | Filtra Mbrowse do programa MATA260 | LOCALIZAÇÃO : Function Mata260() - Responsável pela Transferência entre almoxarifados / localizações.  DESCRIÇÃO : Ponto de entrada para filtragem da Mbrowse do programa MATA260 |
| **[M260FILB](https://tdn.totvs.com/pages/releaseview.action?pageId=6087972)** | Verificação de filtros na Mbrowse da Função MATA260 | LOCALIZAÇÃO: Ponto de entrada localizado na rotina Transferência entre almoxarifados / localizações.  EM QUE PONTO: Será executado antes que seja exibida a tela principal da rotina. Este ponto de entrada tem como objetivo permitir que o usuário filtre os dados a serem exibidos. |
| **[MT260BTN](https://tdn.totvs.com/pages/releaseview.action?pageId=6087758)** | Inclui botões de usuário na barra de ferramentas | LOCALIZAÇÃO : Funções A260Visual(), A260Inclui(), A260Estorn(), A260NFOrig()  EM QUE PONTO : Ponto de Entrada para inclusão de botões de usuário na barra de ferramentas. |
| **[MT260BLD](https://tdn.totvs.com/pages/releaseview.action?pageId=6087757)** | Impede a exibição do botão "Seleciona Lote Destino" | LOCALIZAÇÃO : Localizado nas funções A260Inclui() e A260Estorn( ) antes da criação do botão 'Seleciona Lote destino'.  EM QUE PONTO : Este Ponto de Entrada tem o objetivo de impedir a exibição do botão 'Seleciona Lote Destino' localizado na ToolBar da rotina e se encontra antes da criação do botão logo no inicio das funções a260Inclui e a260Estorn. |
| **[MTA260DOC](https://tdn.totvs.com/pages/releaseview.action?pageId=6087811)** | Indica se o usuário pode digitar o documento | LOCALIZAÇÃO : Function A260Inclui() - Responsável pela inclusão de transferências.  EM QUE PONTO : Criação do ponto de entrada MTA260DOC que indica se o usuário pode digitar o documento (retornar .T.) ou não (retornar .F.) |
| **[MA260WMS](https://tdn.totvs.com/pages/releaseview.action?pageId=6783813)** | Indica os armazéns que não são controlados pelo WMS | Implementado ponto de entrada para indicar os armazéns que não são controlados pelo WMS, para não efetuar as validações ref. ao WMS nas rotinas de Transferência Modelos 1 e 2. |
| **[A260INI](https://tdn.totvs.com/pages/releaseview.action?pageId=6087511)** | Valida código já validado de produto destino | LOCALIZAÇÃO : Function A260IniCpo() - Responsável por inicializar campos a partir do código do produto.  EM QUE PONTO : É chamado na validação do código do produto origem e na validação do código do produto destino. Utilizado para validar os códigos já mencionados. |
| **[MT260UM](https://tdn.totvs.com/pages/releaseview.action?pageId=6087762)** | Trata a conversão de Unidades de Medida e validação dos campos | LOCALIZAÇÃO : Localizado na função A260Quant( ) responsável por tratar Conversão de Unidades de Medida e Validação dos campos ( Quantidade e Quantidade Secundária).  EM QUE PONTO : No final da função, antes de retornar a variável que controla o status da validação executado pela função. |
| **[MA260EST](https://tdn.totvs.com/pages/releaseview.action?pageId=6087613)** | Efetua estorno de transferência | LOCALIZAÇÃO: Function MTA260OK() - Responsável pela Confirmação antes de executar o estorno.  EM QUE PONTO: Ponto de entrada para validar se pode efetuar o estorno da transferência ou não. |
| **[A260LOC](https://tdn.totvs.com/pages/releaseview.action?pageId=6087512)** | Cria no SB2 o produto na movimentação | LOCALIZAÇÃO : Function A260Local() - Validação do campo cLocOrig.  EM QUE PONTO : Objetivo desde P.E. é criar no SB2, o produto de origem/local de origem digitados na movimentação |
| **[MA260EXC](https://tdn.totvs.com/pages/releaseview.action?pageId=6087614)** | Atualiza campo ou variável | LOCALIZAÇÃO : Function a260Processa() - Processamento da inclusão  EM QUE PONTO : Este Ponto de Entrada e chamado após o estorno. Pode ser utilizado para atualização de algum campo ou variável. |
| **[MA260NFQ](https://tdn.totvs.com/pages/releaseview.action?pageId=6087615)** | Oculta tela de seleção de materiais para o CQ | LOCALIZAÇÃO : Localizado na função A261Grava( ) antes da geração dos movimentos de origem.  EM QUE PONTO : Este Ponto de Entrada tem o objetivo de não exibir a tela para selecao de materiais a serem transferidos para o CQ, quando houver integracao com o Quality. |
| **[A260GRV](https://tdn.totvs.com/pages/releaseview.action?pageId=6087510)** | Valida movimento e atualiza valor das variáveis | LOCALIZAÇÃO : Function a260Processa() - Responsável pelo Processamento da inclusão.  EM QUE PONTO : Apos confirmada a transferencia, antes de atualizar qualquer arquivo. Pode ser utilizado para validar o movimento ou atualizar o valor de alguma das variáveis disponíveis no momento. |
| **[MT260NLOT](https://tdn.totvs.com/pages/releaseview.action?pageId=6087929)** | Opção para o tipo de SubLote. | LOCALIZAÇÃO: Está localizado na função a260Processa que tem o objetivo de de processar a inclusão.  EM QUE PONTO: É executado no momento que está criando o sublote na transferência. |
| **[MA260D3](https://tdn.totvs.com/display/public/PROT/MA260D3+-+Atualiza+arquivos+e+campos)** | Atualiza arquivos e campos | LOCALIZAÇÃO : Function a260Processa() - Processamento da inclusão  EM QUE PONTO : Após gravação dos registros de movimento na inclusão de uma transferência. Pode ser utilizado para atualizar algum arquivo ou campo. |
| **[MA260D3F](https://tdn.totvs.com/display/public/PROT/MA260D3F+-+Atualiza+arquivo+e+campo)** | Atualiza arquivo e campo | LOCALIZAÇÃO : Function a260Processa() - Processamento da inclusão  EM QUE PONTO : Após gravação dos registros de movimento na inclusão de uma transferência fora do controle de transação. Pode ser utilizado para atualizar algum arquivo ou campo. |
| **[MT260TOK](https://tdn.totvs.com/pages/releaseview.action?pageId=6087761)** | Validar as informações inseridas pelo Usuário | LOCALIZAÇÃO : Ponto de Entrada localizado na confirmação da Dialog na função A260TudoOK.  EM QUE PONTO : É executada ao pressionar o botão da EnchoiceBar. |
| **[MTA260MNU](https://tdn.totvs.com/pages/releaseview.action?pageId=6087760)** | Adiciona opções na rotina da função | LOCALIZAÇÃO : Function MATA260- Função responsável pelas Transferências entre almoxarifados / localizações. |

**Saiba mais:**

*[MP - SIGAEST - MATA241 - Pontos de Entrada da rotina Movimentação Múltipla](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004558141)*

*[MP - SIGAEST - MATA240 - Pontos de Entrada da rotina Movimentação Simples](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004532861)*

*[MP - SIGAEST - MATA175 - Pontos de Entrada da rotina Baixa de CQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004325941)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
