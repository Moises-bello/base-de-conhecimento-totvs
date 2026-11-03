---
content_hash: 80e07934209767d94d1e5164ffbe06e7a4db07126597ae199b9dc56528625a9c
fetched_at: '2026-06-29T00:08:25.016615+00:00'
page_id: '270909788'
product: rm
source: tdn-rm
title: RPT00009.5.1 - Propriedade Arredondar Valor
type: documentation
url: https://tdn.totvs.com/display/LRM/RPT00009.5.1+-+Propriedade+Arredondar+Valor
version: 23
---

# Índice:

---

.\*ndice:

# Introdução

---

A propriedade **Arredondar Valor** faz com que valores formatados sejam ou não arredondados. Essa propriedade está presente nos seguintes **controles** do relatório:

falseITextoExpressãoFórmulaTotalizador

Um relatório foi criado para demonstrar a diferença entre a propriedade **Arredondar Valor** **marcada** e **desmarcada**.

Esse relatório contém todos os quatros controles citados acima. Os controles **Expressao1**, **Texto1** e **Formula1** trazem como resultado o valor **4,0190**.

O formato utilizado é o **{0:n2}**.

FORMATAÇÂO

Para saber mais sobre **formatação** veja: [Formatação (Passo a Passo)](http://tdn.totvs.com/x/NNaFDg).

**Demonstração:**

falseIPropriedade Arredondar Valor marcada.

Podemos perceber que o relatório gerado trouxe os quatro campos com o valor **4,02,**que é exatamente o valor 4,0190 formatado com duas casas decimais e devidamente arredondado.

Propriedade Arredondar Valor desmarcada.

O valor gerado agora para os quatro controles é **4,01,**que é o valor **4,0190** formatado com duas casas decimais, porém seu valor não foi arredondado, foi simplesmente truncado, ou seja, anda-se com a virgula, sem qualquer outra alteração.

VERSIONAMENTOA propriedade **Arredondar Valor** está disponível a partir das versões **12.1.15** ou superiores.falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Propriedade Arredondar Valor

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
