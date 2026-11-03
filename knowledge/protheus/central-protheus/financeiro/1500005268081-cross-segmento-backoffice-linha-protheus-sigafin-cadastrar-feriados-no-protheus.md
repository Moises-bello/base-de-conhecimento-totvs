---
article_id: 1500005268081
category: Financeiro
content_hash: 5f142522af7ef19e6e7532790e0cd1320e42cd9b83cd883956ca8eebefcb136c
fetched_at: '2026-06-28T22:38:00.822303+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Cadastrar  Feriados
  no PROTHEUS  na Tabela 63 - Feriados
type: support-article
updated_at: '2025-08-12T19:27:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005268081-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Cadastrar-Feriados-no-PROTHEUS-na-Tabela-63-Feriados
---

**Dúvida**Como faço para cadastrar Feriados no PROTHEUS na tabela genérica 63 ( Tabelas de Feriados ) ?  
  
**Ambiente**Cross Segmento - BackOffice Linha Protheus – Financeiro  – Contabilidade Gerencial – 12.1.17  
  
**Solução**

Para que o sistema reconheça uma data como feriado e ajuste automaticamente o vencimento do título para o próximo dia útil, é necessário cadastrá-la na Tabela Genérica 63.

**Acesse:**  
`Configurador (SIGACFG) > Base de Dados > Dicionário > Base de Dados`  
Selecione a **Empresa (Grupo)** e clique em **Tabelas Genéricas**.

**Observações importantes:**

* A data deve ser informada no formato **Dia/Mês/Ano** (ex.: `01/01/99`).
* Caso a data deva ser considerada feriado todos os anos, informe **três espaços em branco após o mês** (ex.: `01/01` ) e, em seguida, insira a descrição.

**Exemplo:**  
`01/01 Feriado Nacional – Confraternização Universal`

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007305761)
