---
article_id: 1500004342342
category: Controle de Documentos (SIGAQDO)
content_hash: 19be907243de026181574b390d3c70560f652e1c6083cf9605eaa182d081f7ff
fetched_at: '2026-06-28T22:42:29.106503+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help ACESS_ROT na opção Documentos
  Cancelados/Reativa do QDOA120
type: support-article
updated_at: '2021-05-21T20:30:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004342342-Manufatura-Linha-Protheus-SIGAQDO-Help-ACESS-ROT-na-op%C3%A7%C3%A3o-Documentos-Cancelados-Reativa-do-QDOA120
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar reativar um documento cancelado na opção **Documentos Cancelados/Reativa** da rotina **QDOA120 - Manutenção de Distribuição** é exibido o *help* **ACESS\_ROT**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Este *help* é exibido ao reativar um documento cancelado na rotina **QDOA120** quando o usuário que está realizando a ação não possui permissão para reativar documentos cancelados.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o **SIGACFG - Configurador**;
2. Acesse o **Menu Usuário/Senhas/Usuários**;
3. Pesquise pelo usuário em questão;
4. Na rotina **CFGA510 - Cadastro de Usuários**, clique em **Alterar**;
5. Na aba **Restrições de Acesso/Acessos**, marque a opção **95 - Reativa Doctos Cancelados**;
6. Acesse novamente a rotina **QDOA120** e execute novamente a reativação do documento.
