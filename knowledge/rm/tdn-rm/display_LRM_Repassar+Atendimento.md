---
content_hash: e3e00ce23a2821ef0a9e41b965a3d495cbdd687e43c46b7fbfad5cf94d23a825
fetched_at: '2026-06-29T00:09:30.244351+00:00'
page_id: '425458386'
product: rm
source: tdn-rm
title: Repassar Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Repassar+Atendimento
version: 1
---

**Repassar Atendimento**   
Este processo repassa um atendimento para um atendente pré-definido ou para um grupo de atendentes (um atendente de um grupo) de acordo com os parâmetros que são passados para o processo. Pode ser utilizado quando outro atendente auxiliará no andamento ou na conclusão do atendimento. O repasse para um grupo de atendentes  possui prioridade, isto é, se informado o código do grupo e o código do atendente então o atendimento será repassado para o grupo de atendentes.   
Quando o processo é executado, é possível visualizar a lista de atendentes disponíveis para realizar o repasse através do lookup.  Deve ser indicado (ou não) se o novo atendente responsável (atendente que receberá o atendimento) será também o responsável pelo contato com o cliente, além de definir se o repasse pode ser executado mesmo que o atendente de destino esteja fora do período de trabalho.  
Veja maiores informações sobre a parametrização nos **Parâmetros Gerais** do Sistema: Clique aqui.  
 Caso a flag "Repassar o atendimento mesmo se o atendente destino estiver fora do seu período de trabalho" não seja marcada, o sistema apresentará uma mensagem de alerta solicitando confirmação para efetuar o repasse (Mensagem de Alerta:"Atenção: Você está repassando uma ocorrência fora do horário de trabalho. É possível que o atendente de destino não esteja disponível para atuar na mesma. Deseja efetuar o repasse? ").   
O motivo do repasse é de caráter obrigatório, mas a justificativa e o endereço de e-mail, para cópias, são opcionais. Caso o atendimento que está sendo repassado possua mensagens pendentes na caixa postal, o sistema não permitirá o repasse, sendo necessário verificá-las. Quando o processo é executado com sucesso, o histórico de repasses do atendimento é atualizado e se endereços de e-mail foram preenchidos no campo de cópia de e-mails, o sistema registra no campo discussão do atendimento para aumentar o controle das informações.  
**Observação**  
   
Vale ressaltar  que o sistema permite o repasse de atendimentos com o status de agendado a responder e ao executar o processo de Agendado Respondido, o atendimento é encaminhado para quem executou o processo de Agendar Atendimento.
