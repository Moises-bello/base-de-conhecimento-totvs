---
content_hash: 1f680c6957f165af74e4b2caf35ad306303a7c268a4afaf5b9a644b38ea43469
fetched_at: '2026-06-29T00:09:30.288061+00:00'
page_id: '425458417'
product: rm
source: tdn-rm
title: Motivo de Repasse - TOTVS Aprovações e Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458417
version: 8
---

---

Nesta opção cadastra-se a tabela de motivo de repasse.

Através do cadastro é possível controlar:  
   
**Identificação**

Nesta pasta, serão informados os dados que identificarão o motivo de repasse cadastrado.  
   
Código  
Código identificador do motivo de repasse. Este código é único e é criado automaticamente pelo sistema.   
   
Descrição  
Neste campo deve ser informado o nome (descrição) do motivo pelo qual a ocorrência está sendo repassada. Ex.: Agendamento, Conclusão, Dúvida, etc.

Tipo  
 Neste campo, devemos selecionar qual o tipo do motivo de repasse.   
   
Repasse   
 Devemos selecionar essa opção quando estamos repassando simplesmente uma ocorrência por diversos motivos, que não seja agendamento ou conclusão da mesma.   
   
Agendamento  
Devemos selecionar essa opção quando estamos repassando a ocorrência porque estamos agendando-a ou concluindo-a.

Fluxo de Tarefas  
Devemos selecionar essa opção quando estamos repassando a ocorrência dentro do fluxo de tarefas.  
Fórmula a ser executada no momento de repasse com este motivoPara que o sistema execute uma fórmula ao repassar a ocorrência apenas quando o motivo que está sendo cadastrado é selecionado no repasse, basta selecionar a fórmula neste campo.

**Exemplo**

Estou repassando uma ocorrência para solicitar autorização em concluir a mesma.

Uma fórmula pode ser criada em Cadastros | Fórmulas. Esta fórmula tem a função de alterar o status do atendimento que está sendo repassado para concluído a responder automaticamente.

É necessário que seja cadastrado o motivo de repasse com o nome, por exemplo, Concluir (a responder) e que seja associada a este motivo à fórmula cadastrada.

Neste caso, quando uma ocorrência é repassada e for selecionado o motivo de repasse "Concluir (a responder)", o sistema vai executar a fórmula e alterar o status da ocorrência para Concluído a Responder.

**Observação**

O campo "Fórmula a ser executada no momento de repasse com este motivo" é habilitado apenas quando o Tipo selecionado é "Repasse".
