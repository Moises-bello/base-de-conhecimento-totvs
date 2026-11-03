---
article_id: 1500004532861
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 23ef2dcc72830a120f775d8eef9d26723c9d12c8db83042655dd4333aa69ee14
fetched_at: '2026-06-28T22:38:58.602763+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - MATA240 - Pontos de Entrada da rotina Movimentação Simples
type: support-article
updated_at: '2021-07-05T13:07:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004532861-MP-SIGAEST-MATA240-Pontos-de-Entrada-da-rotina-Movimenta%C3%A7%C3%A3o-Simples
---

**Dúvida**Quais os Pontos de Entrada relacionados à rotina MATA240?  
  
**Ambiente**Microsiga Protheus - Estoque/Custos - A partir da versão 11.80

**Solução**

Veja abaixo os Pontos de Entrada relacionados à rotina MATA240 - Movimentação Simples:

|  |  |  |
| --- | --- | --- |
| **Nome:** | **Título:** | **Descrição:** |
| **[MT240MEM](https://tdn.totvs.com/display/public/PROT/MT240MEM)** | Adiciona campos Memos virtuais de usuários | LOCALIZAÇÃO : Function Mata240- Função de Movimentacoes Internas (Requisicoes/Devolucoes).  EM QUE PONTO : No momento em que o sistema carrega o Array Principal (aMemos), onde é possível adicionar os campos Memos virtuais de usuários. |
| **[M240FILB](https://tdn.totvs.com/pages/releaseview.action?pageId=6087980)** | Verificação de filtros na Mbrowse da Função MATA240 | LOCALIZAÇÃO: Ponto de entrada localizado na rotina Internos.  EM QUE PONTO: Será executado antes que seja exibida a tela principal da rotina. Este ponto de entrada tem como objetivo permitir que o usuário filtre os dados a serem exibidos. |
| **[M240BUT](https://tdn.totvs.com/pages/viewpage.action?pageId=236593343)** | Ponto de Entrada para criação de botões do usuário | Localização: Localizado nas funções:   * A240Inclui (Inclusão de Movimentos Internos: Requisições e Devoluções) * A240Estorn (Estorno de Movimentos Internos: Requisições e Devoluções) * A240Visual (Visualização de Movimentos Internos: Requisições e Devoluções)   Em que ponto: Antes da montagem da tela das funções citadas; deve ser utilizado para incluir botões na EnchoiceBar para chamadas de rotinas específicas do usuário. |
| **[MT240INC](https://tdn.totvs.com/pages/releaseview.action?pageId=6087857)** | Inclusão de registros na tabela SD3 | Localização: Este ponto de entrada está localizado na função "A240Inclui" e será executado somente após a inclusão completa do registro na tabela SD3.Ao ser executado possibilitará ao usuário, obter os dados do registro que acabou de ser incluído na tabela SD3. |
| **[MT240CAN](https://tdn.totvs.com/pages/releaseview.action?pageId=6087735)** | Tratamento de arquivo e campos do usuário | LOCALIZAÇÃO : Function A240Inclui - Função para inclusão de movimentos internos (Requisições e Devoluções internas)  EM QUE PONTO: No final da Função, no CANCELAMENTO da inclusão; deve ser utilizado para tratamentos específicos de arquivos/campos do usuário. |
| **[SD3240I](https://tdn.totvs.com/pages/releaseview.action?pageId=6087848)** | Gravação de movimentos no SD3 | LOCALIZAÇÃO : É chamado pela função A240ATU (função que grava movimentos no SD3 para os programas MATA240 e MATA241)  EM QUE PONTO : após a inclusão do registro no SD3. |
| **[SD3240E](https://tdn.totvs.com/display/public/PROT/SD3240E+-+Estorno+de+valores+dos+arquivos)** | Estorno de valores dos arquivos | LOCALIZAÇÃO : Function a240DesAtu() - Responsável por estornar os valores dos arquivos.EM QUE PONTO : Após a atualização do registro de movimento interno (SD3) no estorno do mesmo.Pode ser utilizado para atualizar algum campo ou arquivo criado pelo usuário. |
| **[MT240TOK](https://tdn.totvs.com/pages/releaseview.action?pageId=6087738)** | Valida inclusão do movimento | LOCALIZAÇÃO : Na função A240TudoOK (rotina de validação da inclusão do movimento).  EM QUE PONTO : Encontra-se no FINAL da função de validação da inclusão e pode ser usado para validar a inclusão do movimento pelo usuário. |
| **[SD3VESR](https://tdn.totvs.com/pages/releaseview.action?pageId=6087853)** | Validação do componente na requisição | LOCALIZAÇÃO : Function A240Alert() - Responsável por verificar se o produto digitado não faz parte da estrutura do produto da OP.  EM QUE PONTO : Ponto de entrada foi criado para permitir que a validação do componente na requisição para ordem de produção não se |
| **[SD3NSDV](https://tdn.totvs.com/pages/releaseview.action?pageId=6087852)** | Número de série no movimento de devolução | LOCALIZAÇÃO : Funções A240Locali() e A240NumSer ()  DESCRIÇÃO : Criado ponto de entrada SD3NSDV para permitir que seja informado o número de série dos produtos que utilizam localização física em um movimento de devolução. |
| **[MT240EST](https://tdn.totvs.com/display/public/PROT/MT240EST+-+Valida+estorno+do+movimento)** | Valida estorno do movimento | LOCALIZAÇÃO : Function A240EstrOk() - Responsável por validar se pode ser efetuado o estorno.  EM QUE PONTO : Na validacao da inclusao do estorno do movimento. Valida se pode ser incluido o estorno do movimento ou nao. Após confirmação do estorno. |
| **[MT240DVL](https://tdn.totvs.com/pages/viewpage.action?pageId=455807265)** | Validação das Informações do Movimento quando a quantidade informada é maior que a requisição | O ponto de entrada localizado no Movimento Interno (MATA240), função A240VldeOP(), utilizado para validar a apresentação da mensagem "A quantidade de devolução é maior que o saldo requisitado do produto para Ordem de Produção". |
| **[A240WMSO](https://tdn.totvs.com/pages/releaseview.action?pageId=6087492)** | Permite passagem de Endereço e estrutura de Origem | LOCALIZAÇÃO : Function a240Atu() - Responsável por atualizar arquivos.  EM QUE PONTO : Ponto de Entrada A240WMSO utilizado para permitir que a informacao do Endereco e da Estrutura de Origem seja passado via ponto de entrada. Os parametros deste Ponto de Entrada são : Produto /Quantidade e NumSeq |
| **[M240BROW](https://tdn.totvs.com/pages/releaseview.action?pageId=6087563)** | Tratamentos de exibição dos dados no browse | LOCALIZAÇÃO : Funcções Mata240() e Mata241()  EM QUE PONTO : Executado antes da execução do browse, serve para tratamentos de exibição dos dados no browse (filtro, por exemplo). Este ponto de entrada e chamado pelos programas MATA240 (Internos) e MATA241 (Internos Mod.2). |

**Saiba mais:**

*[MP - SIGAEST - MATA175 - Pontos de Entrada da rotina Baixa de CQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004325941)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
