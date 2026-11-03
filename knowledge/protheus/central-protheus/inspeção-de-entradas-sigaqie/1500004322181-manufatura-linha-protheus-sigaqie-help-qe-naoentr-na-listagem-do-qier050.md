---
article_id: 1500004322181
category: Inspeção de Entradas (SIGAQIE)
content_hash: 1c831be9279a60a5d16a662d2493462dfa9d8d893725735d50de888dc5a902d1
fetched_at: '2026-06-28T22:42:27.031471+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help QE_NAOENTR na listagem do QIER050
type: support-article
updated_at: '2022-04-26T20:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004322181-Manufatura-Linha-Protheus-SIGAQIE-Help-QE-NAOENTR-na-listagem-do-QIER050
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min**  
**Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao tentar listar o certificado de qualidade pela rotina **QIER050 - Certificado de Qualidade** é apresentado o *help* **QE\_NAOENTR**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *help* **QE\_NAOENTR** ocorre quando a rotina não encontra dados para listagem, levando em consideração os dados informados pelo usuário nos parâmetros da rotina **QIER050**.  
  
**Solução**Para listagem, quando selecionado o fornecedor por meio do *zoom* do campo **Fornecedor?** os demais dados necessários para a listagem são carregados automaticamente porém, se o fornecedor for digitado, os demais dados devem ser informados manualmente pelo usuário na rotina **QIER050**.  
A listagem é feita de acordo com o resultado da inspeção realizado na rotina **QIEA215 - Cadastro de Resultado**, utilizando como base a tabela **QEK - Entradas**.  
Cada parâmetro informado na tela, corresponde à um campo da tabela **QEK**, que segue:

* **Fornecedor? - QEK\_FORNEC - Forn/Cliente**
* **Loja Fornecedor? - QEK\_LOJFOR - Loja**
* **Produto?- QEK\_PRODUT - Produto**
* **Data Entrega? - QEK\_DTENTR - Data Entrega**
* **Lote? - QEK\_LOTE - Lote**
* **Nota Fiscal? - QEK\_NTFISC - Nota Fiscal**
* **Série NF? - QEK\_SERINF - Série NF**
* **Item? - QEK\_ITEMNF - Item da NF**
* **Num.Sequenc.? - QEK\_NUMSEQ - Num. Sequenc.**
