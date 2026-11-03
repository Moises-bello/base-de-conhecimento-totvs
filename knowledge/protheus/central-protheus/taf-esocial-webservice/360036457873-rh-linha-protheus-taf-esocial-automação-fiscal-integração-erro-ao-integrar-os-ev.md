---
article_id: 360036457873
category: TAF - eSocial - WebService
content_hash: c88636b3e38a4223064dbe31667e1bf87e8c344d284c7b2835fc7d5f61d6992c
fetched_at: '2026-06-28T22:45:15.200817+00:00'
product: protheus
section_id: 1500001536741
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Automação Fiscal- INTEGRAÇÃO - Erro ao
  integrar os eventos com o TAF (401 - Not Authorized)
type: support-article
updated_at: '2026-06-26T11:51:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036457873-RH-Linha-Protheus-TAF-eSocial-Automa%C3%A7%C3%A3o-Fiscal-INTEGRA%C3%87%C3%83O-Erro-ao-integrar-os-eventos-com-o-TAF-401-Not-Authorized
---

**Ocorrência**No TAF, ao integrar eventos vindos do RM ocorre um erro:  
  
Ocorreu erro que impediu a execução do processo. System.Exception: O servidor remoto retornou um erro: **(401) Não Autorizado.**em RM.Fop.Esocial.JSONHelper.Get(String url, String user, String password, String registryKey, String sourceBranch, Boolean queryElements)  
em RM.Fop.Esocial.FopEsocialIntegrarTafMod.Consultar(Int16 codColigada, String codUsuario, List`1 eventosList, RMSServerLog log, Int32& numErros, Int32& totalAtualizados, Int32& totalProcessados).  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Causa**  
O erro ocorre quando existe a senha do administrador que possui um parâmetro configurado para a troca de senha a cada n dias definido pelo sistema.  
  
  
**Solução**

1 - Acesse o TAF;

2 - Menu: Miscelânea -> Usuários:

![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360047870053)

3 - Selecione o usuário administrador e clique em alterar;

4 - Altere a senha ou se quiser pode deixar a senha com o campo vazio:

![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360047870073)

5 - Abaixo em "Troca periódica de senha a cada n dias" deixe o valor igual a 0:

![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360046996934)

6 - Clique em confirmar para salvar;

7 - Faça a troca de senha no seu ERP (RM) e refaça a integração.
