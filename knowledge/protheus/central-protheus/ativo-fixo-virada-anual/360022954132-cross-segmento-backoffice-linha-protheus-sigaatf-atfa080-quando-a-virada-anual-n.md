---
article_id: 360022954132
category: Ativo Fixo - Virada Anual
content_hash: 22fa9f23bcce12e4b63a36e7bd8ff7a2c8b325290ec7f141393049e9db7ce4e6
fetched_at: '2026-06-28T22:41:54.211865+00:00'
product: protheus
section_id: 1500001547482
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA080 - Quando a virada
  anual não é executada  o saldo anterior do ativo é apresentado errado
type: support-article
updated_at: '2025-03-31T12:52:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022954132-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA080-Quando-a-virada-anual-n%C3%A3o-%C3%A9-executada-o-saldo-anterior-do-ativo-%C3%A9-apresentado-errado
---

**Dúvida**

Quando a virada anual não é executada o saldo anterior do ativo é apresentado errado

**Ambiente**  
Microsiga Protheus  – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

A virada zera no SN3, o valor de depreciação do mês e do exercício anterior, no SN5 deleta todos os registros do exercício e cria um registro com Tipo= 0, com a data do novo exercício, porque o razão só lista os dados que contenham o mesmo ano da data base.

Estando no dia 01 de janeiro do exercício seguinte, execute a rotina Virada de Saldos.

Ex. Vamos iniciar um novo exercício de 2011, então informar a data base como 01/01/2011. O sistema limpa e deleta os dados do exercício anterior e cria o tipo=0 com data de 31/12/2010.

Se o usuário não fizer a Virada Anual e calcular as depreciações do novo exercício, o razão vai ficar com o saldo atual errado, porque não irá encontrar o registro tipo=0 ( saldo anterior ), e não vai conseguir compor o saldo atual. Neste caso a solução é rodar a rotina "Refaz saldo", que deve ser  baseado no Cadastro de Bens ( **SN3)**, o sistema irá colocar saldo = XXXXX, somando todos os valores, ou baseado pela movimentação ( SN4 ) , vai colocar o saldo anterior, mais os movimentos deste novo exercício.

[MP- SIGAATF - ATFA120 - REFAZ SALDOS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007396331-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA120-REFAZ-SALDOS)

•Sintético - os saldos são reconstruídos através do Cadastro de Bens (SN1-Cadastro de Ativo Imobilizado + SN3-Arquivo de Saldos), gerando saldos atualizados (resumido).

•Analítico - os saldos são reconstruídos através do Cadastro de Movimentações (SN4-Movimentações do Ativo Fixo), gerados com valores históricos (baixas, depreciações, etc.).

**SN0 - Dados auxiliares ATF**

Na SN0  existe  a tabela 13 - (viradaativo), que contem  a data da virada.

Após a virada esta data tambem é alterada, porem este processo somente irá ocorrer na tabela se o parâmetro MV\_ ATFRSLD estiver configurado = .T.

[Sobre o parâmetro MV\_ATFRSLD](https://tdn.totvs.com/pages/releaseview.action?pageId=6067591)

Veja mais :

[Virada anual](https://tdn.totvs.com/display/public/PROT/Virada+Anual+--+11330)

[ATF0015 - Como funciona a rotina Virada Anual (ATFA080)](http://tdn.totvs.com/pages/releaseview.action?pageId=271163111)

[MV\_ATFRSLD](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/atfa080_parametros.htm)
