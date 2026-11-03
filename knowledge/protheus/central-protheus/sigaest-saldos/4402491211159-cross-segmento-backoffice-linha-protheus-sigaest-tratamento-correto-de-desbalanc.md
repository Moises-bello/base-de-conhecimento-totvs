---
article_id: 4402491211159
category: SIGAEST - SALDOS
content_hash: 211691be40996ada72684596b993baf1ecf491bdf4d5d01863234122e7773463
fetched_at: '2026-06-28T22:39:14.952065+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Tratamento correto
  de desbalanceamento de tabelas de Lote e Endereço em todos os cenários
type: support-article
updated_at: '2026-06-02T16:11:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402491211159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Tratamento-correto-de-desbalanceamento-de-tabelas-de-Lote-e-Endere%C3%A7o-em-todos-os-cen%C3%A1rios
---

O desbalanceamento entre as tabelas SB2, SB8 e SBF no módulo SIGAEST ocorre quando os saldos físico/financeiro não coincidem com os registros de lote ou endereço. A correção varia conforme o cenário: ajuste de lotes via MATA390, endereçamento via MATA265 ou uso da rotina Refaz Saldos (MATA300). Divergências complexas exigem analista especializado. O parâmetro MV\_LOGMOV permite rastreamento para prevenção.

**Dúvida**

Como realizar a correção de desbalanceamento de saldos entre as tabelas SB2 (Saldos Físico e Financeiro), SB8 (Saldos por Lote) e SBF (Saldos por Endereço) no módulo SIGAEST?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
O desbalanceamento entre as tabelas de estoque ocorre quando os saldos físico/financeiro não coincidem com os registros de rastreabilidade (lote) ou localização (endereço). A correção deve ser aplicada de acordo com a origem da divergência, utilizando rotinas de manutenção ou recalculo de saldos para equalização dos dados.

Nesta documentação **vamos abordar os principais cenários e o que fazer em cada um deles**:

1. **Cenário: Saldo da SB2 maior que SB8**

Este cenário ocorre quando existem saldos que ainda não foram loteados.

* Acesse a rotina Manutenção de Lotes (MATA390) através do caminho: Atualizações -> Movimentações -> Internas -> Rastreabilidade -> Manutenção.
* Clique em Incluir e preencha os campos Produto, Armazém, Data de Movimento, Quantidade e Validade do Lote.
* A rotina realizará o ajuste entre SB2 e SB8, gerando uma movimentação de acerto na tabela SD5.

Alternativamente, execute a rotina Refaz Saldos (MATA300) para verificar se o sistema equaliza os registros.

**2. Cenário: Saldo da SB2 maior que SBF**

Ocorre quando há saldos físicos pendentes de endereçamento.

* Acesse a rotina Endereçamento (MATA265) através do caminho: Atualizações -> Movimentações -> Internas -> Endereçamento -> Endereçar.
* Selecione o produto com a legenda verde (pendente) e clique em Endereçar.
* Preencha obrigatoriamente os campos "Endereço" e "Qtd Distribu" e confirme para alimentar a tabela SBF.

O uso da rotina Refaz Saldos (MATA300) também é uma alternativa para tentativa de equalização.

**3. Cenário: Saldo na SBF ou SB8 maior que na SB2**

Divergências onde os saldos de lote ou endereço superam o saldo físico/financeiro possuem diagnóstico complexo e podem ser causadas por manipulação de banco de dados, reaberturas incorretas, customizações ou parâmetros ([MV\_A280GRV e MV\_A330GRV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062164934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-A330GRV-e-MV-A280GRV-para-produtos-obsoletos)) divergentes.

**Oque costuma ocasionar isso fora customizações ou manipulações?**

* Desativação do conceito de endereçamento ou rastreabilidade no produto ou parametros MV\_RASTRO e MV\_LOCALIZ para um item que ja teve saldos movimentados, uma vez produto controla rastro ou localização "Não se deve mexer nesses parametros", sem que todos os saldos estejam Devidamente "Zerados".

Tente a execução da rotina **Refaz Saldos (MATA300)**.

Caso não haja sucesso, não existem rotinas padrão para correção automática; recomenda-se a visita de um analista especialista para evitar efeitos colaterais no faturamento, contabilidade, fiscal (Bloco K) ou novas divergências de custo.  
  
**4. Monitoramento e Prevenção**  
Utilize o parâmetro MV\_LOGMOV com conteúdo "S" para rastrear divergências em movimentações internas, transferências, notas de entrada e pedidos de venda.

O sistema gerará arquivos de log (CM??????.LOG) na pasta System detalhando diferenças de quantidade ou lote entre as tabelas SB2, SB8, SBF, SD5, SDA e SDB

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)
