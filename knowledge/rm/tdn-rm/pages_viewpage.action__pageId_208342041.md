---
content_hash: 9e6d1de3dcab2e914297dcca453def35359bcb280b89e173490d34de429677ca
fetched_at: '2026-06-29T00:06:13.472312+00:00'
page_id: '208342041'
product: rm
source: tdn-rm
title: Modelo de utilização da integração do Vitae e Nucleus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208342041
version: 1
---

# Modelo de utilização da integração do Vitae e Nucleus

|  |  |
| --- | --- |
| **Produto:** | Vitae |
| **Versões:** | 11.82.41 |
| **Passo a passo:** | Foi criado o flag **‘Considerar todos os movimentos de entrada’**, onde o vitae, ira visualizar os movimentos de entrada que estejam parametrizados para ser integrado com o vitae e possuir lote, será visualizado os lotes a serem gerados no vitae.    Exemplo de utilização:    Possui o movimento 1.2.64      E o movimento 1.2.65:      Quando for gerado movimento de compra para um EPI, no vitae, em lotes a serem lançados serão exibidos os dois lotes:        **Atenção!**  **Para a quantidade de itens disponíveis no saldo de EPI e considerado a seguinte regra:**  **O saldo total do EPI no Nucleus, menos o total de itens dos lotes a serem gerados no vitae.**  Exemplo:  No Nucleus possui 3 movimentos criados:  1º Possui **10 itens** – já está gerado – para o movimento 1.2.64  2º Possui **15 itens** – já gerado – para o movimento 1.2.65  3º Possui **8 itens** – **não gerado** – para o movimento 1.2.65  **Total no Nucleus = 10+15+8 = 33**  Parametrizador selecionado apenas para utilizar o **movimento 1.2.64**:    Saldo disponível no Vitae = 15 + 10 + 8 = 33 (sistema olha o saldo total de EPIs no Nucleus menos os não gerados no vitae, como está parametrizado para apenas o movimento 64 não diminui os do movimento 65)    Parametrizador selecionado apenas para utilizar o **movimento 1.2.65**:    Saldo disponível no Vitae = 15 + 10 – 8 = 25 como possui 8 itens ainda não gerados no Vitae para o movimento 1.2.65 é diminuído do saldo:    Parametrizador selecionado apenas para **utilizar todos movimentos**:    Saldo disponível no Vitae = 25 como possui 8 itens ainda não lançados no Vitae para o movimento 1.2.65 é diminuído do saldo: |
| **Observações:** |  |

divs
