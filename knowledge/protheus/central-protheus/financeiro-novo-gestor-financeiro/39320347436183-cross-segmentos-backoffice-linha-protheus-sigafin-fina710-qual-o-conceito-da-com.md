---
article_id: 39320347436183
category: Financeiro - Novo Gestor Financeiro
content_hash: b7ebef51008e09e05775880f9132a303b94cf99cc8dd0c587cb9f2e31caaca1b
fetched_at: '2026-06-28T22:37:41.507599+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Qual o conceito
  da composição do saldo final apresentado no card Saldos bancários
type: support-article
updated_at: '2026-03-26T20:00:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39320347436183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Qual-o-conceito-da-composi%C3%A7%C3%A3o-do-saldo-final-apresentado-no-card-Saldos-banc%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39320347406359) Tempo aproximado para leitura: 00**:05:00 min**  
  
**Dúvida**  
Qual o conceito da composição do saldo final apresentado no card saldos bancários?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**  
No Protheus, diversas rotinas de consulta e relatórios financeiros possuem parâmetros que definem a visão do saldo. Quando a consulta é posicionada pelo Ambiente/Filial, o sistema considera todos os títulos em aberto e baixados, que compõem a carteira daquela unidade, independentemente de estarem vinculados a um banco específico no caso do **novo gestor Financeiro.**

Títulos em Aberto: Compõem o saldo previsto/posicionado por representarem uma expectativa de direito/obrigação.

Títulos Baixados: Deixam de compor o saldo previsto de títulos, pois o valor já foi realizado e passou a compor o saldo bancário (Realizado).

Desta forma, o conceito atual do card, é apresentar o saldo total, esteja em determinada conta bancária ou não.

Exemplo:

Existe no ambiente 1 titulo no valor de 10 mil a receber, este está baixado/recebido, e existem mais 3 títulos em aberto, veja como é apresentado o saldo, selecionando a conta bancária onde o titulo baixado foi inserido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39320306360983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39320347410327)

Caso remova a conta bancária do filtro no caminho a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39320347411607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39320347413143)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39320347413911)

O saldo apresentado é somente dos títulos em aberto, sem considerar a baixa do titulo no valor de 10 mil.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39320306364951)

Saiba mais: [Indicadores Painel de Controle - FINA710](https://tdn.totvs.com/display/public/PROT/Indicadores+Painel+de+Controle++-+FINA710)
