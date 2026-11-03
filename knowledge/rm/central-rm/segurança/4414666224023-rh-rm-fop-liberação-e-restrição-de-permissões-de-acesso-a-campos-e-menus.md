---
article_id: 4414666224023
category: Segurança
content_hash: 825b3e8ca2cd30977726d916106487a8e1941d474a55a691503d85fa7b8939da
fetched_at: '2026-06-28T22:46:46.823933+00:00'
product: rm
section_id: 1500000834641
source: central-rm
title: RH - RM - FOP - Liberação e restrição de permissões de acesso a campos e menus
type: support-article
updated_at: '2024-10-09T19:07:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414666224023-RH-RM-FOP-Libera%C3%A7%C3%A3o-e-restri%C3%A7%C3%A3o-de-permiss%C3%B5es-de-acesso-a-campos-e-menus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21486566479127) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como liberar ou restringir permissões a usuários no acesso a campos e menus do módulo Folha de Pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Primeiramente, deve atentar-se ao perfil associado ao usuário. Caso não saiba qual perfil está associado ao usuário em questão, verifique em: **Serviços Globais | Segurança | Usuários | Segurança** e selecione o perfil desejado. Certifique-se de que o Sistema visualizado seja o Folha de Pagamento, conforme demonstrado e destacado na imagem abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414663642007)  
  
Para liberar ou restringir o acesso a campos e menus, acesse o módulo: **Serviços Globais | Segurança | Perfis | Sistema: Folha de Pagamento**. Devem serem levadas em consideração as seguintes abas: **Identificação, Acesso a Campos e Acesso a Menus.**  
1. Acesso a Campos: Acesse a tabela e o campo desejado, liberando ou restringindo as permissões nas flags: **Pode Consultar**; **Pode Alterar**. Segue o exemplo da Tabela PFUNC na imagem abaixo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414675547031)  
  
Entende-se como **campo** todos os itens do sistema que permitem ao usuário preencher com algum dado, ou que pelo menos o dado seja apresentado para consulta ao visualizar uma tela. São os dados que preenchem e populam uma tabela. Por exemplo, o campo NOME na tabela PPESSOA:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414744827159)  
  
Note que para visualizar o nome da tabela e campo conforme demonstrado acima, basta clicar com o botão direito do mouse em qualquer área cinza da tela e selecionar **Visualizar nome dos campos**. Feito isso, basta passar o mouse sobre o campo para visualiza-lo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414751623575)  
  
3. Acesso a Menus: Ao escolher o Menu desejado clicar em **Permitir Acesso** ou **Proibir Acesso**:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414663918359)  
  
Entende-se como **menus** todos os itens do sistema que permitem ao usuário clicar para acessar uma tela ou rotina. Isso vale para os ícones distribuídos nas abas do sistema, os anexos de determinada tela, etc:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414744937751)  
  
**Importante**  
Vale ressaltar que o processo deve ser realizado para todos os perfis vinculados ao usuário e a todos os módulos que possuem. Existem tabelas que são compartilhadas entre outros módulos, como por exemplo a tabela PFUNC. Se, por exemplo, o usuário tiver restrição de acesso aos campos da tabela PFUNC no perfil do módulo Folha de Pagamento mas tiver acesso à mesma no perfil do módulo Gestão de Pessoas, pode haver conflito das permissões e o usuário acabar com uma permissão que não deveria. Deve-se verificar também se há mais de um perfil vinculado ao usuário para que a restrição seja aplicada em todos eles, para também evitar conflito de permissões.
