---
article_id: 5243886416151
category: Controle de Documentos (SIGAQDO)
content_hash: 055b4bbfb6bf35dc5e9068f5feb19a086f492e1a4df219deda388d86f340a9dd
fetched_at: '2026-06-28T22:42:29.128058+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QD120USRNE
type: support-article
updated_at: '2022-04-05T18:40:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5243886416151-Manufatura-Linha-Protheus-SIGAQDO-Help-QD120USRNE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:40 min****Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, na rotina **QDOA120 - Manutenção de Distribuição de Documentos**,quando o usuário tenta realizar a distribuição, ocorre o *help* **QD120USRNE- Usuário não encontrado.**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* **QD120USRNE- Usuário não encontrado** é exibido quando a rotina **QDOA120** não encontra o usuário informado como destinatário para o documento em questão. Esta informação fica registrada na tabela **QDG - Destinatário**, relacionada ao documento.  
  
**Solução**Na rotina **QDOA120** a seleção por **Distribuir por Destinatário** irá exibir apenas os usuários que contemplem as condições abaixo:  
  
1. Não tenha data fim preenchida na tabela **QAA - Usuários,** ou seja, que o campo **QAA\_FIM - Data Fim** esteja em branco ou que a data fim seja maior ou igual à data pesquisada.  
2. Que o *status* não seja **2-Inativo**, ou seja, o campo **QAA\_STATUS - Status do Usuário** esteja igual a **1-ativo**;  
3. Que a filial do cadastro do usuário seja igual à filial do cadastro do departamento, ou seja, que os campos **QAA\_FILIAL - Filial** e **QAD\_FILIAL - Filial** tenham o mesmo conteúdo;  
4. Que o departamento do cadastro do usuário seja um departamento válido, ou seja, que os campos **QAA\_CC - Código de Departamento** e  **QAD\_CUSTO - Código de Departamento** tenham o mesmo conteúdo.
