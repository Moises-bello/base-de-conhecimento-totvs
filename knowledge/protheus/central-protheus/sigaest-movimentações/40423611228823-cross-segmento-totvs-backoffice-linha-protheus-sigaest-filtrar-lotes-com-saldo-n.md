---
article_id: 40423611228823
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 15d76603d472065479ffd7159a77d750d6ed317ed30cf878e8946595e54356c4
fetched_at: '2026-06-28T22:38:58.493117+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Filtrar lotes
  com saldo na consulta F4 da rotina MATA270
type: support-article
updated_at: '2026-05-14T12:24:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40423611228823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Filtrar-lotes-com-saldo-na-consulta-F4-da-rotina-MATA270
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40423611180567) Tempo aproximado para leitura: 00:01:00 **min**  
  
**Dúvida**  
Como filtrar para que sejam exibidos apenas lotes com saldo maior que zero no campo B7\_LOTECTL (Consulta F4) durante o processo de inventário na rotina MATA270?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A tela de consulta de lotes padrão do sistema (função F4LOTE) não possui um filtro nativo configurável pelo usuário para exibir apenas registros com saldo positivo. Para atender a essa necessidade, é necessária a implementação de uma customização utilizando pontos de entrada que permitem manipular a exibição dos dados na consulta de lotes.

**Passos**

Para implementar essa funcionalidade, deve-se utilizar um dos seguintes pontos de entrada:

1. [**F4LOTEHEADER**](https://tdn.totvs.com/pages/releaseview.action?pageId=651921829): Utilizado para manipular o cabeçalho na seleção de lotes.

2. [**MTF4LOTE**](https://tdn.totvs.com/display/public/PROT/MTF4LOTE+-+Consulta+saldos+de+lotes+da+rastreabilidade+via+F4): Utilizado para a consulta de saldos de lotes da rastreabilidade via F4.

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
