---
content_hash: a4fe173dc9e7e59c6394aa23932536036e87a734c4e9f12b4e005910c478b8f1
fetched_at: '2026-06-29T00:09:16.069691+00:00'
page_id: '421385451'
product: rm
source: tdn-rm
title: Importação de Apontamento de Equipamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385451
version: 3
---

---

O processo de importação de apontamentos de equipamentos é iniciado no coletor móvel, o mesmo envia para o TOP os apontamentos registrados de forma manual ou através de jobs agendados no coletor.

Para a coleta dos apontamentos o usuário pode informar a tarefa através de leitura de códigos de barras ou via digitação manual, caso o usuário não saiba em qual tarefa o equipamento está trabalhando e saiba o centro de custo, então poderá informar esse centro de custo.  
 Os dados que serão trafegados durante a importação de apontamentos serão os seguintes:  
 Coligada; Projeto; Identificador do Coletor (IMEI); Tarefa (Código de Barras); Centro de Custo; Equipamento (Código de Barras); Horímetro; Código de motivo de improdutividade; Tipo de apontamento (check-in ou check-out); Data/hora de início da atividade; Data/hora de término da atividade; Usuário que apontou/registrou.  
 O TOP após receber os apontamentos do coletor móvel vai gerar um log contendo os seguintes dados:  
 Identificação do equipamento; Identificação do processo; Data e Hora de Transmissão; Status da transmissão (Caso seja mal-sucedida poderá ser enviado um e-mail de notificação, conforme parametrização de envio de e-mails de erros).

**Importante:**

* Caso o TOP esteja integrado com o módulo Manutenção de Ativos (Protheus) o apontamento será enviado diretamente ao Protheus e seu status será definido como enviado. Para isso duas condições devem ser atendidas:
  + A fórmula visual "PRJWKF0001 - Appointment" deve ser importada para a base;
  + Deverá ser agendado um job no TOTVS Business Connector para quando receber mensagens do tipo "APPOINTMENT" processá-la automaticamente.
* Foi criado um parâmetro MV\_NGTURNL que controla o uso do calendário do bem.
* Quando habilitada a opção 1 o parâmetro rejeita a utilização do calendário do bem quando fora do Turno de trabalho
* Ou seja quando a tag TurnCalendar do xml enviado ao Protheus através da mensagem APPOINTMENT estiver vazio e o paramento MV\_NGTURNL habilitado com a opção 1 o mesmo rejeita a utilização do calendário do bem exibindo a seguinte mensagem :**" A Tag TurnCalendar não foi preenchida. Favor verificar o parâmetro MV\_NGTURNL ou enviar um turno no apontamento."**
* Quando habilitada a opção 2 o parâmetro utiliza o calendário do bem.
* Ou seja quando a tag TurnCalendar do xml enviado ao Protheus através da mensagem APPOINTMENT estiver com o valor preenchido o mesmo o parâmetro utiliza o calendário do bem.

**Passos para Importar para o TOP Apontamentos de Equipamentos:**

1. Acessar o TOP Mobile (Coletor Móvel);
2. Fazer logon;
3. Iniciar o processo de sincronização de dados (ou através de jobs agendados no coletor móvel);
4. Os apontamentos são validados e enviados ao TOP;
5. O TOP envia um arquivo contendo os dados de apontamentos para enviar ao Manutenção de Ativos (Protheus).
