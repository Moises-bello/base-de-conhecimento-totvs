---
article_id: 360023788792
category: SIGAEST - CUSTOS
content_hash: aaee1ea656245e470f36378d0896c9f6953f090643143ef80ab221e66aa79278
fetched_at: '2026-06-28T22:39:00.322899+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Custo zerado em movimentos
  no Protheus. Por quê?
type: support-article
updated_at: '2026-04-06T14:44:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023788792-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-zerado-em-movimentos-no-Protheus-Por-qu%C3%AA
---

O parâmetro MV\_CUSZERO no TOTVS Protheus permite zerar o custo de movimentos quando o saldo final for zero, evitando custo em produtos sem quantidade ou valor. Configurado como "S", o custo do movimento será zero; como "N", usa o custo médio histórico. Esse parâmetro não afeta movimentações valorizadas e é considerado no recálculo do custo médio.

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33452845727127)***Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Existe a possibilidade de zerar o custo de um movimento, quando o saldo final calculado for zero? **Ou mesmo não calcular custo**, se iniciarem o periodo com Saldo de quantidade Zerado e Valor Zerado?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Sim, é possível utiizar esse conceito de zerar os movimentos, bem como o custo historico a ser levado para o fechamento do periodo, através do comportamento gerado com a particularidade de utilização do **parâmetro MV\_CUSZERO**.

**Resumo do parametro, conforme segue no HELP do mesmo:**

**Se a quantidade no final do Periodo for igual a Zero**, devera Zerar Custo dos próximos Movimentos?

**Sim ("S")** ou **Nao ("N")**

***Atenção:*** *Esse parametro **NÃO** tem o conceito de **zerar o custo final caso seu estoque, caso ele finalize sem quantidade**, se o seu problema é ter custo final e não possuir quantidade, Deve-se primeiro entender como foi calculadas as movimentações, para isso avalie o Kardex por período (MATR900) como indicado no link abaixo:*

[Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)

**CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**
4. **Informações adicionais**

**01. VISÃO GERAL**

O parâmetro **MV\_CUSZERO**tem como finalidade definir se as movimentações não valorizadas (custeadas com base no custo médio atual) terão seu custo zerado caso o produto não tenha saldo em valor (B2\_VATU1) ou quantidade (B2\_QATU) no armazém.

**Abaixo segue as duas configurações disponíveis:**

S = O custo do movimento será 0 caso não tenha quantidade ou custo no armazém.

N = Será considerado o custo médio histórico (B2\_CM1) para custear o movimento que não tenha quantidade ou custo no armazém.

Padrão do sistema: conteudo N

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16892504367383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16892480815767)

**02. EXEMPLO DE UTILIZAÇÃO**

**MV\_CUSZERO = S (Sim)**

Produto com **quantidade 0**, **custo total 50** e **custo médio 10**;  
Incluída uma movimentação interna **não valorizada** de entrada (DE0) com quantidade 1;  
**O custo da movimentação (D3\_CUSTO1) será 0 (Zero)**;  
Em estoque, o saldo do produto será 1 e custo total 50.

**MV\_CUSZERO = N (Não)**

Produto com **quantidade 0**, **custo total 50** e **custo médio 10**;  
Incluída uma movimentação interna não valorizada de entrada (DE0) com quantidade 1;  
**O custo da movimentação será Quantidade \* Custo médio histórico (B2\_CM1) = 10;**  
Em estoque, o saldo do produto será 1, custo total 60 e novo custo médio 60.

**03. TABELAS UTILIZADAS**

* SB2 (Saldos Físico e Financeiro)
* SD2 (Itens de Venda da NF)
* SD3 (Movimentações Internas)

**04. INFORMAÇÕES ADICIONAIS**

* O parâmetro também será considerado na rotina Recálculo do Custo Médio (MATA330) para recalcular o custo das movimentações. Nesse caso, são utilizados os campos B2\_QFIM, B2\_VFIM1 e B2\_CFIM1 como referência.
* O parâmetro não será considerado por movimentações valorizadas, como por exemplo, notas fiscal de compra e movimentação interna valorizada (RE6/DE6).
* Este parâmetro, com o conteúdo S, utiliza a função interna 'PegaCMFim', e zera (ou não) o custo médio do movimento interno, se a quantidade do movimento for zero ou o custo for zero exceto para as movimentações dos tipo: "DE4, RE4, DE6, RE6, RE7, DE7, RE8, DE8, RE5, DE5".

**Resumo do parametro, conforme segue no HELP do mesmo:**

Se a quantidade final do Periodo for igual a Zero, devera Zerar Custo do Movimento?

Sim ("S") ou Nao ("N")

**Saiba mais:**

[*Clique aqui e saiba mais sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
