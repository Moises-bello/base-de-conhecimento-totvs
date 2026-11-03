---
article_id: 1500004558141
category: SIGAEST - MOVIMENTAÇÕES
content_hash: e6269202839b379ee5b31710a7ac27fcffc775d54b267e31a7c7e2848ada3268
fetched_at: '2026-06-28T22:38:56.979756+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Pontos de
  Entrada da rotina Movimentação Múltipla
type: support-article
updated_at: '2026-03-03T21:07:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004558141-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Pontos-de-Entrada-da-rotina-Movimenta%C3%A7%C3%A3o-M%C3%BAltipla
---

Os Pontos de Entrada da rotina MATA241 - Movimentação Múltipla no TOTVS Backoffice permitem personalizações em diversas fases, como inclusão de campos, validações, atualizações e tratamentos específicos durante movimentações internas (requisições/devoluções). Cada ponto atua em funções específicas, desde a montagem da tela até a gravação e estorno dos movimentos, oferecendo flexibilidade para ajustes conforme necessidade do usuário.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38781961947159) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Quais são os Pontos de Entrada relacionados à rotina MATA241 - Movimentação Múltipla?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Veja abaixo os Pontos de Entrada relacionados à rotina MATA241 - Movimentação Múltipla (clique no nome do Ponto de Entrada para obter maiores detalhes):

|  |  |  |
| --- | --- | --- |
| **Nome:** | **Título:** | **Descrição:** |
| [**MT241MEM**](https://tdn.totvs.com/display/public/PROT/MT241MEM) | Retorna um array sendo que cada elemento é um campo memo a ser tratado pelo cadastro. | LOCALIZAÇÃO : Function Mata241- Função de Movimentações Internas (Requisições/Devoluções).  EM QUE PONTO : No momento em que o sistema carrega o Array Principal (aMemos), onde é possível adicionar os campos Memos virtuais de usuários. |
| [**MTA241CPO**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087797) | Inclui campos do usuário na getdados | LOCALIZAÇÃO : Localiza-se nas seguintes rotinas de Movimentos Internos Modelo 2:  a) A241Inclui (função para Inclusão de movimentação interna)  b) A241Visual (função para Visualização de movimentação interna)  c) A241Estorn (função para Estorno de movimentação interna)  EM QUE PONTO: Após a montagem do aHeader e aCols nas rotinas acima; Pode ser utilizado para incluir campos do usuário na getdados. |
| [**A241BUT**](https://tdn.totvs.com/pages/releaseview.action?pageId=235599354) | Movimentações Internas | LOCALIZAÇÃO: Na rotina de movimentações internas (modalidade II).  EM QUE PONTO: Será executado na montagem da tela nas funções de visualização, inclusão e estorno. |
| [**MT241CAB**](https://tdn.totvs.com/pages/releaseview.action?pageId=6085553) | Inclusão de campos no cabeçalho da rotina Movimentos Internos Mod2 | O Ponto de entrada MT241CAB permite a inclusão de campos no cabeçalho da rotina "Movimentos Internos - Modelo 2". |
| [**MTA241DOC**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087798) | Permite ou não a digitação do campo "Número do Documento" | LOCALIZAÇÃO : Function a241Inclui() - Responsável pela inclusão de movimentação interna.  EM QUE PONTO : antes da digitação dos dados e seu objetivo é permitir ou não a digitação do campo 'Numero do Documento'. O retorno do ponto de entrada MTA241DOC indica se o usuário pode digitar o documento (retorno = .T.) ou não (retorno = .F.). |
| [**MTA241PCO**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087800) | Rotina de baixa da pré-requisição | LOCALIZAÇÃO : Function A241Inclui - Função para inclusão de movimentos internos (Requisições e Devoluções internas) Modelo 2  EM QUE PONTO : Apos a montagem do aCols, vale ressaltar que este ponto de entrada e somente utilizado quando utilizada a rotina de baixa da pre-requisição. ('MATA185') |
| [**MT241SD3**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087745) | Atualização de Arquivo ou campo | LOCALIZAÇÃO : Função A241Inclui (Inclusão de Movimentação Interna).  EM QUE PONTO : É executado logo após a gravação dos movimentos internos (SD3), na inclusão e tem como finalidade a atualização de algum arquivo ou campo. |
| [**MT241CAN**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087739) | Tratamento específicos de campos do usuário | LOCALIZAÇÃO : Function A241Inclui - Função para inclusão de movimentos internos (Requisições e Devoluções internas) Modelo 2  EM QUE PONTO : No final da Função, no CANCELAMENTO da inclusão; deve ser utilizado para tratamentos específicos de arquivos/campos do usuário. |
| [**MT241EST**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087740) | Atualização de arquivo ou campo | LOCALIZAÇÃO: Função A241Estorn (Estorno de Movimentação Interna)  EM QUE PONTO : Após a atualização do registro de movimentos internos (SD3) no estorno do movimento e tem como finalidade a atualização de algum arquivo ou campo. |
| [**MT241TOK**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087747) | Valida inclusão de movimento | LOCALIZAÇÃO : Função A241TudOk (Validação da Inclusão do Movimento - Critica se todo o documento esta' Ok)  EM QUE PONTO : Tem a finalidade de ser utilizado como validação da inclusão do movimento pelo usuário. |
| [**MT241GRV**](https://tdn.totvs.com/display/public/PROT/MT241GRV+-+Atualiza+arquivo+ou+campo) | Atualiza arquivo ou campo | LOCALIZAÇÃO : função A241GRAVA (Gravação do movimento)  EM QUE PONTO : Após a gravação dos dados (aCols) no SD3, e tem a finalidade de atualizar algum arquivo ou campo. |
| [**MTA241I**](https://tdn.totvs.com/display/public/PROT/MTA241I+-+Valida+a+data+do+movimento) | Valida a data do movimento | LOCALIZAÇÃO : Este Ponto de Entrada está localizado na função A241Data (valida a data em relação a data do último fechamento)  EM QUE PONTO: Após a validação da data do movimento, no cabeçalho da rotina e tem a finalidade de validar esta mesma data. |
| [**MT241EXT**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087741) | Valida campos específicos de usuário | LOCALIZAÇÃO : função MTA241ESTOK (Confirmação antes de executar o estorno)  EM QUE PONTO : Antes do Estorno e sua finalidade é permitir validar campos específicos do usuário no momento do estorno. |
| [**MT241SE**](https://tdn.totvs.com/display/public/PROT/MT241SE+-+Adiciona+itens+no+aCols) | Adiciona itens no aCols | LOCALIZAÇÃO : Está localizado na função M241SeleEs (Seleciona estrutura como base para preenchimento automático de produtos a serem requisitados - utilizada para explodir o 1° nível da estrutura).  EM QUE PONTO: No final da função M241SeleEs, deve ser utilizada para adicionar itens no aCols. |
| [**MTA241MNU**](https://tdn.totvs.com/display/public/PROT/MTA241MNU+-+Altera+o+Menu) | Altera o Menu | O ponto de entrada MTA241MNU permite a inclusão de novas rotinas ao Menu Padrão da rotina de Movimentos Internos (Modelo 2) |
| [**M240BROW**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087563) | Tratamentos de exibição dos dados no browse | LOCALIZAÇÃO : Funções Mata240() e Mata241()  EM QUE PONTO : Executado antes da execução do browse, serve para tratamentos de exibição dos dados no browse (filtro, por exemplo). Este ponto de entrada e chamado pelos programas MATA240 (Internos) e MATA241 (Internos Mod.2). |
| [**MT240DVL**](https://tdn.totvs.com/pages/viewpage.action?pageId=455807265) | Validação das Informações do Movimento quando a quantidade informada é maior que a requisição | O ponto de entrada localizado no Movimento Interno (MATA240), função A240VldeOP(), utilizado para validar a apresentação da mensagem "A quantidade de devolução é maior que o saldo requisitado do produto para Ordem de Produção". |

**Saiba mais:**

[*MP - SIGAEST - MATA240 - Pontos de Entrada da rotina Movimentação Simples*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004532861)

[*MP - SIGAEST - MATA185 - Pontos de Entrada da rotina Baixa de Pré-Requisição ao Armazém*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004530301)

[*MP - SIGAEST - MATA175 - Pontos de Entrada da rotina Baixa de CQ*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004325941)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
