---
article_id: 360044371774
category: Inspeção de Entradas (SIGAQIE)
content_hash: 967dc78361ec5b6268370ec71716a6474fab13c62c8f2e0096930e66516094a2
fetched_at: '2026-06-28T22:42:26.905759+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Campo Data Valid do QIEA215
type: support-article
updated_at: '2024-05-15T17:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044371774-Manufatura-Linha-Protheus-SIGAQIE-Campo-Data-Valid-do-QIEA215
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23508958044951)**Tempo aproximado para leitura:**00:00:45 min**  
**Dúvida**Como é calculado o campo **Data Valid** da rotina **QIEA215 - Cadastro de Resultados**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**O campo **QEL\_DTVAL - Data Valid** da rotina **QIEA215** é gravado com base no conteúdo do parâmetro **MV\_QVALLOT - Define o critério para a Validade do Lote Lib/Rej**, onde tem as seguintes opções:  
  
**1** - Mantém a validade do lote cadastrado na nota fiscal;  
**2** - Assume a validade calculada no resultado, alterando também o campo **B8\_DTVALID - Data Validad.** Esta data é calculada levando em consideração a informação contida nos campos ***Shelf Life*** e ***Un.Sh.Life*** da rotina **QIEA010 - Especificação de Produto**;  
**3** - Assume a maior validade entre os campos **B8\_DTVALID** e **QEL\_DTVAL**.  
  
**Importante**  
Além desta parametrização acima, não existe **PE - Ponto de Entrada** que altere o valor deste campo.
