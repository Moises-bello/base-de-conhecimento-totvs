---
article_id: 1500008814261
category: Inspeção de Processos (SIGAQIP)
content_hash: e1d49055a20710791580f21164e84a72e50e704344cfa2aeb3c64a06feb54af4
fetched_at: '2026-06-28T22:42:25.841935+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Mensagem A210WHDE
type: support-article
updated_at: '2021-10-01T13:11:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008814261-Manufatura-Linha-Protheus-SIGAQIP-Mensagem-A210WHDE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min**  
**Ocorrência**Ao acessar a rotina **QIPA215 - Resultados** apresenta mensagem **InterFunctionCall: cannot find function A210WHDE**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Causa**A mensagem indica a falta da **função A210WHDE** durante a utilização da rotina **QIPA215**. E ocorre porque esta função existia no **Protheus 11**, mas foi descontinuada para a **versão 12**.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a tabela **SX3** via **APSDU**;  
2. Filtre e localize os campos **X3\_WHEN** que estejam preenchidos com a informação **A210WhDE()**;  
3. Apague a informação **A210WhDE()** de todos os campos e realizar um novo teste.  
  
**Importante**  
Antes de efetuar procedimento indicado, é recomendado realizar um *backup* da tabela **SX3**.
