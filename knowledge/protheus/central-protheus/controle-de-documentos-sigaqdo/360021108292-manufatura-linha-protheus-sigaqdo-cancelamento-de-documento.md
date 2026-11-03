---
article_id: 360021108292
category: Controle de Documentos (SIGAQDO)
content_hash: 2b8dff8204732ea8377bba31919e42416dd8d6f7c28e2f454ecd4919a3df7333
fetched_at: '2026-06-28T22:42:28.970036+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Cancelamento de documento
type: support-article
updated_at: '2024-08-14T19:28:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021108292-Manufatura-Linha-Protheus-SIGAQDO-Cancelamento-de-documento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25652356297623)**Tempo aproximado para leitura:**00:01:30 min  
  
Dúvida**Como cancelar um documento cadastrado na rotina **QDOA050 - Cadastro de Documentos**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Na rotina **QDOA050**, selecione o documento que deseja cancelar e acesse o botão **Outras Ações**/**Cancelar**.   
  
É possível cancelar apenas a **última revisão** do documento que esteja com *status* de **leitura** e apenas os usuários com a permissão para **gerar revisões** poderão realizar o cancelamento.  
Para verificar quais usuários possuem a permissão para **Gera revisão**, acesse a rotina **QDOA020 - Tipos de Documento**, selecione o tipo de documento em questão, clique no botão **Visualizar** e em seguida no botão **Outras Ações**/**Niv. Resp**.  
  
Ao cancelar o documento, será gerada uma nova revisão informando que o documento em questão será cancelado. O documento passará por todas as fases de revisão previamente configuradas: **Elaboração**, **Revisão**, **Aprovação**, **Distribuição**, etc, para que todos os leitores estejam cientes de que o documento foi cancelado. O cancelamento será efetivado apenas após todos os usuários baixarem as pendências de leitura.  
A revisão na qual o documento foi cancelado, terão os campos **QDH\_CANCEL - Cancelado** e **QDH\_OBSOL - Obsoleto** alterados para **S**, e a revisão atual gerada, após passar por todos as fases de revisão, terá o campo **QDH\_CANCEL** como **S** e o campo **QDH\_OSBOL** como **N**.  
  
**Importante**  
Caso necessário, o documento cancelado poderá ser reativado, impresso ou visualizado através da rotina **QDOA120 - Manutenção de Distribuição**por meio do botão **Documentos cancelados**.  
  
**Observação**  
O cancelamento, independente da revisão, irá cancelar todas as revisões do documento.  
  
**Saiba mais**  
Para identificar qual o usuário que fez o cancelamento do documento, consulte o artigo [Manufatura - Linha Protheus - SIGAQDO - Como identificar o usuário que fez o cancelamento de um documento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050499433)
