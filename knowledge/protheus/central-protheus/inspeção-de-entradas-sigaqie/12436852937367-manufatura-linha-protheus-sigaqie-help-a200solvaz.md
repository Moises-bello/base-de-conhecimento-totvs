---
article_id: 12436852937367
category: Inspeção de Entradas (SIGAQIE)
content_hash: 5b148b225c009baab541d569fab991253d89d80c5320c06b897f3806063fbd0b
fetched_at: '2026-06-28T22:42:27.002677+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help A200SOLVAZ
type: support-article
updated_at: '2023-02-15T18:28:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12436852937367-Manufatura-Linha-Protheus-SIGAQIE-Help-A200SOLVAZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:25 min****Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao tentar incluir ou alterar uma entrada na rotina **QIEA200 - Entradas** é apresentado o *help* **A200SOLVAZ**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *help* **A200SOLVAZ** ocorre quando na rotina **MATA061 - Atualização Produto x Fornecedor** a situação do produto x fornecedor é **Pré-Qualificada**, ou seja, quando o campo **Situação - A5\_SITU** contém o conteúdo igual a **C**.  
  
**Solução**Para que o *help* **A200SOLVAZ**não seja exibido, altere na rotina **MATA061** a situação do fornecedor no campo **Situação** para **A - Assegurado**, ou altere o conteúdo do parâmetro **MV\_QSOLPQU - Exige o nome do Solicitante quando a Situacao do Produto/Fornecedor tiver categoria Sem Skip-Lote** para **N - Não**.
