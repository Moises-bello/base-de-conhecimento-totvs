---
article_id: 39135324768663
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: d87f9cd21ff80a552ab519fdc89a7e052c3cfcc5732f6dfcaebb4b12a6f80df4
fetched_at: '2026-06-28T22:40:32.592126+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial
  (SIGACTB) - Como padronizar a pergunta de contabilização para todos os usuários
type: support-article
updated_at: '2026-03-18T19:27:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39135324768663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Contabilidade-Gerencial-SIGACTB-Como-padronizar-a-pergunta-de-contabiliza%C3%A7%C3%A3o-para-todos-os-usu%C3%A1rios
---

No TOTVS Protheus, para pré-configurar e bloquear a pergunta "Contabiliza On-line" para usuários, deve-se usar a rotina de Configuração de Perguntas no módulo Configurador, definindo uma resposta padrão e desabilitando o campo para usuários ou grupos específicos. Assim, a alteração manual fica impedida durante o uso das rotinas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39135324749847) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
Como deixar a pergunta "Contabiliza On-line" pré-configurada e bloqueada de uma única forma para os usuários no sistema, impedindo a alteração manual durante o uso das rotinas?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade gerencial - SIGACTB - A partir da versão 12.

**Solução**

Para menter a padronização das perguntas de contabilização, deve ajusta a forma que deve ocorrer a contabilização e utilizar o bloqueio de perguntas.

Através da rotina de Configuração de Perguntas do módulo Configurador, é possível definir uma resposta padrão e desabilitar o campo "Contabiliza On-line" para usuários específicos ou grupos de usuários. Assim, todos os usuários atrelados ao grupo receberão a mesma regra de configuração.

Para desabilitar o campo nas rotinas desejadas (como no exemplo de uma rotina financeira FIN080, que se aplica a qualquer outra que possua o parâmetro), siga o procedimento abaixo:

1. Acesse o módulo **Configurador**.
2. Acesse o menu Usuário > Senhas > Config. Perguntas.
3. Clique em **Incluir**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39135324752663)
4. No campo **Grupo**, informe o código do Grupo de Perguntas da rotina desejada (Exemplo: FIN080).

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39135294793111)
5. No campo **Usuário ou Grupo de Usuário**, selecione para quem a regra de bloqueio será aplicada

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39135294795287)
6. Na seção inferior, serão exibidas as perguntas referentes ao grupo selecionado.
7. Filtre ou localize a linha correspondente à pergunta "Contabiliza On-line".
8. Clique sobre a pergunta e pressione a tecla **DEL** do teclado. A linha ficará marcada em branco, indicando o bloqueio.
9. Para deixar um valor padrão configurado, selecione a opção desejada na coluna Conteúdo.
10. Ao finalizar, clique em **Confirmar**.

    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39135324758039)

Realizado os passos acima o usuário ou grupo de usuário atrelados a configuração não poderão ajustar a pergunta de contabilização.

**Saiba Mais**  
[Bloquear resposta de Perguntas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034770094-Framework-Linha-Protheus-Bloquear-resposta-de-Perguntas)  
[Configuração de Perguntas - Bloquear Parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=271390085)
