---
article_id: 360035994374
category: Inspeção de Entradas (SIGAQIE)
content_hash: ed874250b2bacac38a374586669c4a4ed1ef59ac3a609a58bdb3c0d38424f18c
fetched_at: '2026-06-28T22:42:27.018538+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help Q215046
type: support-article
updated_at: '2021-08-09T12:37:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035994374-Manufatura-Linha-Protheus-SIGAQIE-Help-Q215046
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao salvar a inspeção de resultados é exibido o *help* **Q215046 - Existem laboratórios sem Laudos Informados**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *help* ocorre na rotina **QIEA215  - Cadastro de Resultados** devido o parâmetro **MV\_QBLQSLA - Determina se a pasta de Laudo Geral será bloqueada caso existam laboratórios sem laudo definido** estar com conteúdo igual à **T - True**, indicando o bloqueio quando não foi informado no campo **Laudo** da aba **Laudo do Laboratório**.  
  
**Solução**Para que a rotina **QIEA215** permita a liberação do resultado sem ter laudo informado, o parâmetro **MV\_QBLQSLA** deve ter conteúdo igual à **F - False**.
