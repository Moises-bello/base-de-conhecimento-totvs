---
article_id: 360016177632
category: SIGAEST - RELATORIOS
content_hash: 3dc05a661da3f92b510bac89bcec1473f25a6eb596ba3a5cc17b5c3940aaf046
fetched_at: '2026-06-28T22:39:06.020007+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como extrair o MATR260
  para verificação de saldos comparando com outros relatórios?
type: support-article
updated_at: '2023-07-10T19:02:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016177632-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-extrair-o-MATR260-para-verifica%C3%A7%C3%A3o-de-saldos-comparando-com-outros-relat%C3%B3rios
---

**Dúvida**Qual a importância da pergunta "**Saldo do Produto a Considerar?**" na extração do MATR260 - Relatório Posição de Estoque - para verificação de saldos comparando com outros relatórios?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O objetivo do relatório "Posição de Estoques" não é detalhar as Reservas e  Empenhos de cada produto e sim demonstrar o Saldo em Estoque e os Empenhos Aglutinados, para que o usuário possa visualizar o Saldo Disponível em Estoque.

Partindo da premissa que perguntas como "Produto De/Até", "Data de Referência", "Armazém De/Até" estejam pareados com o outro relatório que for comparar, olharemos para uma pergunta de extrema importância para exibição dos dados, que é o pergunte "**Saldo do Produto a Considerar?**"

Nesta pergunta, temos algumas opções e iremos explicá-las para que consigas parametrizar de forma que o resultado seja satisfatório:

1 - **Parâmetro Saldo atual:** Se baseia no B2\_QATU / B2\_VATU. Não se baseia na data de referência

2 -  **Parâmetro: Saldo do fechamento:**  Se baseia no B2\_QFIM / B2\_VFIM. Não se baseia na data de referência

3 - **Parâmetro Saldo por movimento:** Utiliza a função calcest() para calcular o saldo do movimento até a data

presente (pela data do último fechamento do B9) descontando todas as movimentações do SD1,

SD2, SD3. Neste caso a pergunta "Data de referência" deve ser preenchida.

**OBS**: Este parâmetro tem como objetivo a comparação de saldos com o Kardex (MATR900) do período.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012224673-SIGAEST-RELATORIOS)*
