---
article_id: 360049572774
category: Controle de Documentos (SIGAQDO)
content_hash: f6a7642b7958d1536780867da80b5cdd83d1f923529080addd85bdd78eb1f91d
fetched_at: '2026-06-28T22:42:29.141927+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDNEDISTR
type: support-article
updated_at: '2022-03-31T17:52:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049572774-Manufatura-Linha-Protheus-SIGAQDO-Help-QDNEDISTR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:44 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, na rotina **QDOA110 - Distribuição de Documentos**,quando o usuário tenta baixar a **Pendência de Distribuição**, ocorre o *help* **QDNEDISTR - Não existe distribuição pendente / Solução: Verifique o cadastro de pendência.****Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esse incidente ocorre porque a rotina não está encontrando pendências de distribuição para o usuário em questão. O Sistema valida também os demais usuários que estão com a pendência, pois a mesma é baixada para todos os usuários com esta responsabilidade.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

* Acesse a tabela **QD1 - Distribuição por Usuários** e filtre pelo documento em questão.
* Verifique se para este usuário e os demais que estão com a pendência na tabela **QD1** com a responsabilidade de distribuição **QD1\_TPPEND=I** estão ativos e com o mesmo departamento **QD1\_DEPTO - Depto Usr**e função **QD1\_CARGO - Cargo Usr** que constam na tabela **QAA - Usuários**.

**Importante**  
O departamento e função que constam para estes usuários na tabela **QAA**, precisam ser os mesmos departamentos e funções que constam na tabela **QD1**.  
Caso houver divergência entre cargo e função entre as tabelas **QAA** e **QD1**, também é necessário ajustar para o Sistema permitir a baixa da pendência.Caso um dos usuários que possuir esta pendência de distribuição estiver inativo, é necessário transferir a pendência para um usuário ativo.   
  
**Saiba mais**  
Para mais informações referente a transferência das pendências entre usuário, consulte o artigo: [Manufatura - Linha Protheus - SIGAQDO - Transferência de pendências para um novo usuário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021357911-MP-QUA-Transfer%C3%AAncia-de-pend%C3%AAncias-para-um-novo-usu%C3%A1rio)
