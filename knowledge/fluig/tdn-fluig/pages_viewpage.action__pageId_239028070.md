---
content_hash: 16d44e051bdce246d38bce22fa5b5552deeacee43eaaf2f96d8a9056c21b0db6
fetched_at: '2026-06-28T21:35:22.727126+00:00'
page_id: '239028070'
product: fluig
source: tdn-fluig
title: BPM 039 - Por que o prazo da atividade fica com a data "31/12/1969" ?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239028070
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

O prazo da atividade fica com a data "31/12/1969"

# Causa

Foi criado um evento para calcular uma data para o prazo da atividade. Ao gerar uma data para o prazo, é provável que essa data seja inválida e o sistema envia a primeira data válida que seria essa "31/12/1969".

# Solução

Verificar o código fonte desse evento e corrigir o calculo da data.

# Observações

Datas enviadas via mobile são convertidas para o formato (YYYY-MM-DD), datas enviadas através do Chrome já estão nesse mesmo formato (YYYY-MM-DD) e datas enviadas via IE e Firefox são no formato (DD/MM/YYYY).

A maneira correta de tratar diferentes formatos de data é convertendo todas para um único formato, conforme a documentação [Desenvolvimento de Formulários](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#DesenvolvimentodeFormulários-InputFields).
