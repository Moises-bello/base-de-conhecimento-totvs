---
article_id: 30310769450391
category: Financeiro - Contas a Pagar
content_hash: a7c711e8ccbe0322af9b845e59aef675877136cfeaa1e605c274acb32e674466
fetched_at: '2026-06-28T22:38:06.988620+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA340 - Uso de variáveis
  na contabilização
type: support-article
updated_at: '2025-02-28T20:05:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30310769450391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Uso-de-vari%C3%A1veis-na-contabiliza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30310753905815) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais variáveis posso utilizar para contabilizar no modo online ou offline

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA340 - Todas as versões  
  
**Solução**A lista de variáveis que podem ser utilizadas na configuração do Lançamento Padrão 597 (Compensação Contas a pagar) para contabilização **online** da Compensação a pagar (FINA340):

**VALOR** - Armazena o valor compensado  
**VALOR2** - Valor de Acréscimo  
**VALOR3** - Valor de Decréscimo  
**VALOR4** - Variação da correção monetária  
**VLRINSTR** - Armazena o valor compensado  
**nSldReal** - Armazena o valor compensado na moeda correspondente do título  
**ABATIMENTO** - Valores de abatimentos  
**REGVALOR** - Recno do registro atual  
**STRLCTPAD** - Chave do título principal+número do documento

Essas variáveis são alimentadas com os dados do registro posicionado de onde **partiu a compensação**. Enquanto que para os registros selecionados para compensar, é feita a contabilização pela SE5.

Na contabilização on-line, não é possível alterar a filial de contabilização, sendo contabilizado na filial do processo de compensação (filial do título de partida da compensação).

**Exemplo:**

Selecionar a **NF1** e clicado em Compensar.

Na tela de seleção dos títulos a compensar, selecionar a **PA1** e **PA2**.

Ao contabilizar on-line, as informações da **NF1** estarão nas variáveis de contabilização. Já as informações da compensação de cada PA, terão seus respectivos registros da SE5 posicionados.

**Variáveis Estorno**:

**VALOR** - Armazena o valor compensado  
**VLRINSTR** - Armazena o valor compensado

Ao forçarmos o posicionamento dos títulos a serem compensados, a contabilização trará os dois títulos (ex: NF x PA), contabilizando o valor dos dois títulos, podendo gerar duplicidade na contabilização.

As variáveis disponíveis para a **contabilização off-line** (CTBAFIN):

**VALOR** - Armazena o valor compensado  
**VALOR2** - Valor de Acréscimo  
**VALOR3** - Valor de Decréscimo  
**REGVALOR** - RECNO do registro atual  
**STRLCTPAD** - Chave do título principal+número do documento

**Obs**.: Estas variáveis estão disponíveis tanto para a compensação quanto para o estorno.

Essas variáveis são alimentadas com os dados do registro posicionado de onde **partiu a compensação**. Enquanto para os registros selecionados para compensar, é feita a contabilização pela SE5.

**Saiba mais**

[Compensação contas a pagar - FINA340 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=504794483)
