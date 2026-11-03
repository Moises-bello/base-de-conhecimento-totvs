---
article_id: 39236701718039
category: Financeiro - Contabilização
content_hash: de67760b8179a508a3dcce94cf2194ce2ba44e848d116d4836ce32456f4546db
fetched_at: '2026-06-28T22:38:05.246240+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como bloquear a pergunta
  de contabilização Online para um ou mais usuários
type: support-article
updated_at: '2026-03-23T22:30:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39236701718039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-bloquear-a-pergunta-de-contabiliza%C3%A7%C3%A3o-Online-para-um-ou-mais-usu%C3%A1rios
---

Para pré-configurar e bloquear a pergunta "Contabiliza On-line" no TOTVS Protheus, deve-se utilizar a rotina de "Configuração de Perguntas" disponível no módulo Configurador.O procedimento consiste em definir uma resposta padrão e desabilitar o campo para usuários ou grupos específicos. Dessa forma, a alteração manual será impedida durante a execução das rotinas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39236701663767) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
Como deixar a pergunta “Contabiliza On-line” pré-configurada e bloqueada, garantindo um único padrão para um grupo usuários e impedindo alterações manuais durante a execução das rotinas?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução:**

Para manter a padronização das perguntas de contabilização, é necessário definir previamente o comportamento desejado e aplicar o bloqueio do grupo de perguntas para os usuários.

Isso pode ser feito por meio da rotina de "**Configuração de Perguntas"**, no módulo Configurador, onde é possível definir uma resposta padrão e impedir a alteração no F12 do grupo de perguntas, onde o campo *“Contabiliza On-line”* está disponivel para ajuste de um usuário ou grupos específicos.

Dessa forma, todos os usuários vinculados ao grupo passam a seguir a mesma regra de configuração.

Para aplicar essa configuração (exemplo utilizando a rotina FIN080, podendo ser adaptado para outras rotinas que possuam esse parâmetro), siga os passos abaixo:

* Acesse o módulo **Configurador**;
* Navegue até **Usuário > Senhas > Config. Perguntas**;
* Clique em **Incluir**;  
  ![Rotina.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39236701664791)
* No campo **Grupo**, informe o grupo de perguntas da rotina desejada (exemplo: FIN080);  
  ![fini080.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39236677328535)
* No campo **Usuário ou Grupo de Usuário**, selecione para quem a regra será aplicada;  
  ![fin080.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39236701669527)

Na parte inferior da tela, serão exibidas as perguntas disponíveis para o grupo informado:

* Localize a pergunta *“Contabiliza On-line”*;
* Clique sobre ela e pressione a tecla **DEL** — a linha ficará em branco, indicando que está bloqueada para edição;
* Na coluna **Conteúdo**, defina o valor padrão desejado;  
  ![sss.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39236677340951)

Por fim, clique em **Confirmar** para salvar a configuração.

Após esse procedimento, os usuários ou grupos vinculados não poderão alterar essa pergunta durante a execução das rotinas, garantindo a padronização do processo.
