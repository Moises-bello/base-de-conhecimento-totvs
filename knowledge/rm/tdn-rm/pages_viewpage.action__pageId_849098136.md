---
content_hash: beef4d70b6d6ca6c2aa66659b3b531f8d1e67089ad510da93eabc29b98e4892a
fetched_at: '2026-06-29T00:11:51.566309+00:00'
page_id: '849098136'
product: rm
source: tdn-rm
title: Prioriza Código de Dez Dígitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849098136
version: 1
---

## **03. Regras de Código do MatMed**

As regras de preenchimento do código de procedimento para MatMed seguem uma ordem de prioridade no XML da TISS.

**Nota:** **Lembrando que o mesmo seguirá a ordem de prioridade e receberá o código procedimento independente dos outros parâmetros marcados.   
Ex.: Caso entre na primeira condição, ignore o resto.**

1. Codificação especifica: Esta tela se encontra em RM Saúde > Cadastros > Outros Cadastros > Padrões de Faturamento e Codificação. (Normalmente apenas utilizado pela UNIMED, de acordo com o Alberto)
3. Código de 10 dígitos (Código TISS): Caso o parâmetro “Prioriza código de dez dígitos” (RM Saúde > Cadastros > Outros Cadastros > Tabela de MATMED usadas) esteja marcado, o código procedimento receberá o valor do campo “Código TISS” referente à tabela de preço utilizada pelo produto.
4. Obs.: A tela acima pode ser encontrada em: (RM Saúde > Cadastros > Produto > Anexo Informações – TOTVS Saúde > Anexo Tabela de preço).
5. Código Item Brasindice: Será utilizado caso o parâmetro abaixo esteja marcado.
7. Código TUSS ou Código Específico: Por fim, ele irá validar o preenchimento do novo campo “Código TUSS” se o mesmo estiver preenchido, irá utiliza-lo. Senão irá receber o código de 8 dígitos (Código Específico) que já utilizava anteriormente.
