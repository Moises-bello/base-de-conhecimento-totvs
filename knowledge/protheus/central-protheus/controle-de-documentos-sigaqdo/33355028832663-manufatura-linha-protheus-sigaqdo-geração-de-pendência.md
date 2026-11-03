---
article_id: 33355028832663
category: Controle de Documentos (SIGAQDO)
content_hash: 853db7aa4cb298b2e9122895bebf4f737da699b2e842868bfc9b90ed60fc53cf
fetched_at: '2026-06-28T22:42:29.091372+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Geração de Pendência
type: support-article
updated_at: '2025-07-10T19:05:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33355028832663-Manufatura-Linha-Protheus-SIGAQDO-Gera%C3%A7%C3%A3o-de-Pend%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33355035374743) Tempo aproximado para leitura: **00:06:50 min**  
  
**Dúvida**  
No **SIGAQDO - Controle de Documentos**, qual a regra para **gerar pendência** ao usuário?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**  
A **geração de pendência** ocorre para o usuário que está cadastrado na rotina **QDOA050 - Cadastro de Documento** como **Responsáveis**, levando em consideração dois fatores:

* A configuração do **Tipo de Documento** selecionado, previamente cadastrado na rotina **QDOA020 - Tipo de Documentos**, considerando o campo **Baixa Pend** conforme artigo [Manufatura - Linha Protheus - SIGAQDO - Todos usuários cadastrados recebem pendência de baixa](https://totvssuporte.zendesk.com/knowledge/editor/01JZQTSJ3YVN6CA4616GD24G9F/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F13117548771991)
* E a configuração do parâmetro **MV\_QDBXALE - Define se a baixa da Etapa devera ser aleatória quando houver mais de um responsável na etapa** conforme artigo [Manufatura - Linha Protheus - SIGAQDO - Baixa da etapa aleatória quando houver mais de um responsável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025550213-Manufatura-Linha-Protheus-SIGAQDO-Baixa-da-etapa-aleat%C3%B3ria-quando-houver-mais-de-um-respons%C3%A1vel)  
    
  **Seguem cenários como exemplo:**  
    
  1. Cenário 1:
* rotina **QDOA020** o campo **Nr Mínimo** para e etapa de Aprovação tem conteúdo **igual a 01;**
* rotina **QDOA020** o campo **Baixa Pend** com conteúdo **igual a S;**
* e parâmetro **MV\_QDBXALE** igual **a N.**

Em **Responsáveis** na rotina **QDOA050** é cadastrado 03 responsáveis para Etapa de Aprovação:  
APR001  
APR002  
APR003  
Somente o responsável cadastrado na primeira sequência, no caso o usuário APR001 receberá a pendência de baixa.  
  
2. Cenário 2:

* rotina **QDOA020** o campo **Nr Mínimo** para e etapa de Aprovação tem conteúdo **igual a 01**;
* rotina **QDOA020** o campo **Baixa Pend** tem conteúdo **igual a S;**
* e parâmetro **MV\_QDBXALE** igual **a S.**

Em **Responsáveis** na rotina **QDOA050** é cadastrado 03 responsáveis para Etapa de Aprovação:  
APR001  
APR002  
APR003  
Os 03 responsáveis receberão a pendência simultaneamente. Assim que qualquer usuário Aprovador efetuar a baixa da pendência de Aprovação, as demais pendências de Aprovação são baixadas automaticamente.  
  
3. Cenário 3:

* rotina **QDOA020** o campo **Nr Mínimo** para e etapa de Aprovação tem conteúdo **igual a 01**;
* rotina **QDOA020** o campo **Baixa Pend** tem conteúdo **igual a N;**
* e parâmetro **MV\_QDBXALE** igual **a N.**

Em **Responsáveis** na rotina **QDOA050** é cadastrado 03 responsáveis para Etapa de Aprovação:  
APR001  
APR002  
APR003  
Os 03 responsáveis receberão a pendência, seguindo a ordem cadastrada. O usuário APR001 baixa a pendência de Aprovação e a pendência é aberta para usuário APR02, e assim sucessivamente.

4. Cenário 4:

* rotina **QDOA020** o campo **Nr Mínimo** para e etapa de Aprovação tem conteúdo **igual a 01**;
* rotina **QDOA020** o campo **Baixa Pend** tem conteúdo **igual a N;**
* e parâmetro **MV\_QDBXALE** igual **a S**.

Em **Responsáveis** na rotina **QDOA050** é cadastrado 03 responsáveis para Etapa de Aprovação:  
APR001  
APR002  
APR003  
Os 03 responsáveis receberão a pendência simultaneamente, e cada qual deverá efetuar a respectiva baixa.  
  
**Observação**  
O **Nr Mínimo** pode variar conforme necessidade do cliente, assim como a **quantidade de responsáveis**. No exemplo, foi utilizado a etapa de Aprovação, porém todas as etapas, incluindo **Elaboração, Revisão, Aprovação, Homologação** seguem o mesmo fluxo.
