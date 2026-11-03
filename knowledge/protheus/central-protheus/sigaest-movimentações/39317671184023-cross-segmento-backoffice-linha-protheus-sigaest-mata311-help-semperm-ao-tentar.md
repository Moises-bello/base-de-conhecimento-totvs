---
article_id: 39317671184023
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 89a1be625d78d420bc384328e1bb74334003b52b068957f152bfe296ec9eb3bf
fetched_at: '2026-06-28T22:38:57.153750+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA311 - Help SEMPERM
  ao tentar excluir Solicitação de Transferência
type: support-article
updated_at: '2026-03-26T19:05:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39317671184023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA311-Help-SEMPERM-ao-tentar-excluir-Solicita%C3%A7%C3%A3o-de-Transfer%C3%AAncia
---

Ao tentar excluir uma Solicitação de Transferência na rotina MATA311 do Protheus, pode ocorrer erro por falta de permissão específica. Para resolver, no módulo Configurador (SIGACFG), acesse Usuário Senhas Usuários, selecione o usuário, vá em Restrições de acesso Acessos e marque a opção "3 - Excluir Cadastros". Salve e peça para o usuário reiniciar a sessão.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39317646997271) Tempo aproximado para leitura:**01:00 min**  
  
**Dúvida**  
Ao tentar realizar a exclusão de uma Solicitação de Transferência através da rotina MATA311, o sistema apresenta o help de erro abaixo, impedindo a conclusão da ação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39317671163543)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Este incidente ocorre porque, além do acesso à rotina no menu, o usuário precisa de uma permissão específica no cadastro de acessos do Configurador para realizar operações de exclusão em cadastros.

Para resolver, siga os passos abaixo:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Usuário > Senhas > Usuários**;
3. Selecione o usuário que apresenta o erro e clique em **Alterar**;
4. Clique na aba **Restrições de acesso**;
5. Na sub-aba **Acessos**, localize e marque a opção **3 - Excluir Cadastros**;
6. Clique em **Confirmar** para salvar as alterações e peça ao usuário para reiniciar a sessão no Protheus.

![Screenshot_26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39317671165079)

***Saiba Mais:***

[***Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV\_RESTARM - Validação do HELP SEMPERM ou RESTPRD***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012695422-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-RESTARM-Valida%C3%A7%C3%A3o-do-HELP-SEMPERM-ou-RESTPRD)

[***SIGAEST - MOVIMENTAÇÕES***](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
