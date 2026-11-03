---
article_id: 360022073332
category: SIGAACD - Automação e Coleta de Dados
content_hash: ab796f3f7e14ccd60af3b2abaab4002eb1f23434e286048a74e91b27786cd104
fetched_at: '2026-06-28T22:39:12.574543+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como funciona o Controle
  de Tarefas - ACDA180
type: support-article
updated_at: '2025-03-12T12:47:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022073332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-funciona-o-Controle-de-Tarefas-ACDA180
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24762949735447) Tempo aproximado para leitura: **00:02:00 min*****Dúvida**  
Como funciona o Controle de Tarefas - ACDA180?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 11.80.

**Solução**

O processo Controle de tarefas permite enviar mensagens com tarefas, para um operador, solicitando esta execução no sistema. O operador pode receber uma mensagem via Coletor RF e executar automaticamente uma rotina, sem ter a necessidade de percorrer as opções do menu. Para que este processo ocorra é necessário que o responsável inclua uma tarefa por esta rotina, informando o código do operador que receberá mensagem, o corpo da mensagem, o status, rotina a executar e o buffer do teclado. O operador tem acesso às mensagens no Coletor RF pela rotina Mensagens.

O processo também possibilita que qualquer operador existente e ocioso no sistema possa executar uma tarefa não lida, eliminando a necessidade de vinculá-la a um determinado operador, basta que o responsável pelo cadastro deixe o campo CBF\_PARA em branco. Ao verificar a mensagem o operador fica responsável pela execução da tarefa e esta pode voltar a ficar pendente para qualquer outro operador se o responsável pelo controle de tarefa limpar o conteúdo do campo CBF\_PARA na alteração.

**Procedimentos**Para incluir controle de tarefas:

1. Em Controle de Tarefas, acesse a opção Incluir.

2. Informe os valores para os campos conforme detalhes:

* Para (CBF\_PARA): Código do operador responsável pela tarefa. Para que todos os operadores tenham acesso à tarefa, o campo pode ser deixado vazio.
* Assunto (CBF\_MSG): Conteúdo da mensagem visualizado pelo operador.
* Status (CBF\_STATUS): Status da mensagem.
* Rotina (CBF\_ROTINA): Nome da rotina chamada quando o operador confirmar a execução da tarefa.
* Keyboard (CBF\_KEYB): Uma cadeia de caracteres contendo as informações que ficam em buffer para execução da rotina indicada.

3. Confira os dados e confirme a inclusão.  
  
**Saiba mais**

<http://tdn.totvs.com/display/PROT/Controle+de+Tarefas+-+ACDA180>

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)
