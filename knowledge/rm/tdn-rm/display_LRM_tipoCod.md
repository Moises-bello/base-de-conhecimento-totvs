---
content_hash: 1d70588cdce590c034be3a9a4b19606d70d8f2d758ee8025df461eb0703296ef
fetched_at: '2026-06-29T00:11:26.430701+00:00'
page_id: '716369755'
product: rm
source: tdn-rm
title: tipoCod
type: documentation
url: https://tdn.totvs.com/display/LRM/tipoCod
version: 1
---

## Valor Total Da Receita Por Tipo De Código De Atividade Econômica

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| tipoCod | ideEstab | 1-N | - | Registro que apresenta o valor total da receita por tipo de código de atividade econômica | As informações desse Grupo serão originadas da pasta "Contribuição Previdenciária" do Período de Apuração de cada uma das Filiais. |
| codAtivEcon | tipoCod | 0-1 | 8 | Código indicador correspondente à atividade comercial, produto ou serviço sujeito a incidência da Contribuição Previdenciária sobre a Receita Bruta, conforme Tabela 09. | DPERIODOCONTRIBPREV.CODATIVECONOMIC |
| vlrRecBrutaAtiv | tipoCod | 1-1 | 14 | Preencher com o valor total da receita da atividade  Validação: valor igual ao somatório do campo {vlrBruto} do grupo {nfs}. Não pode ser maior que { vlrRecBrutaTotal }. | DPERIODOCONTRIBPREV.VALORRECEITAS |
| vlrExcRecBruta | tipoCod | 1-1 | 14 | Preencher com o Valor total das Exclusões da Receita Bruta previstas em lei.  Validação: deve ser igual a soma dos valores informados no campo {vlrAjuste} cujo {tpAjuste} seja igual a "0". Ajuste de redução. Caso não haja ajuste de redução "0" (zero). Não pode ser maior que {vlrRecBrutaAtiv}. | Não aderência |
| vlrAdicRecBruta | tipoCod | 1-1 | 14 | Preencher com o Valor total das Adições da Receita Bruta previstas em lei.  Validação: deve ser igual a soma dos valores informados no campo {vlrAjuste} cujo {tpAjuste} igual a "1". Ajuste de adição. Caso não haja ajuste de adição preencher com "0" (zero). | Não aderência |
| vlrBcCPRB | tipoCod | 1-1 | 14 | Preencher com o Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta.  Validação: Deve ser igual a {vlrRecBrutaAtiv} + {vlrAdicRecBruta} - {vlrExcRecBruta}. | DPERIODOCONTRIBPREV.BASECALCULO |
| vlrCPRBapur | tipoCod | 0-1 | 14 | Preencher com o Valor Contribuição Previdenciária sobre a Receita Bruta.  Validação: deve ser igual a {vlrBcCPRB} multiplicado pela alíquota do código da atividade{codAtivEcon} da tabela 9 | DPERIODOCONTRIBPREV.VALORCONTRIBUICAO |
