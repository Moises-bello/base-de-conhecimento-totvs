---
content_hash: 3b4bb916ad10c690269b39532f9d6c8e78e8b0d4ff654e3ac33c51b5c13b7b81
fetched_at: '2026-06-29T00:09:35.502290+00:00'
page_id: '425459371'
product: rm
source: tdn-rm
title: Integração TOTVS Folha de Pagamento x Gestor AVB (Tools)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459371
version: 6
---

**TOTVS Folha de Pagamento x Gestor AVB (Tools)**

---

A integração TOTVS Folha de Pagamento x Gestor AVB (TOOLS) visa a disponibilização de um BPO (Business Process Outsourcing) onde os funcionários das empresas que utilizam o módulo de RH dos ERPs da organização: Protheus, Datasul, RM e Logix, possam solicitar empréstimos de averbação em folha com o mínimo de envolvimento do RH.    
    
 **Arquitetura**

Nessa integração para que a comunicação entre os dois sistemas (de origem e destino) aconteça é utilizado um repositório de mensagens, chamado MessageQueue, que fica armazenado em um servidor Java (JBOSS). O TOOLS envia mensagens de solicitação de informações para o MessageQueue. O Conector, por sua vez,  vai até o repositório de tempo em tempo, conforme agendamento de serviço (recomendamos de 1 em 1 minuto), e verifica se existem novas informações para serem processadas. Caso exista ele processa, caso contrário deve ser verificado o motivo pelo qual a menssagem não foi processada.

Todas as mensagens que são processadas serão gravadas no Monitor da Fila de Integração do Conector. Caso nenhuma mensagem tenha sido gravada no Monitor da Fila de Integração, é por que não existiam mensagens para serem processadas. Nesse caso deve ser verificado o Monitor de Jobs do segmento Serviços Globais.

Com essa comunicação são integradas as funcionalidades: Consulta Funcionários, Consultar Status Folha de Pagamento, Cadastrar Empréstimos, Cancelar Empréstimos (Quitação antecipada).

Outras funcionalidades são integradas através de um Web Service. O TOTVS Folha de Pagamento chama um evento no TOTVS Business Conector e entrega todos os funcionários que tenham empréstimos consignado pelo TOOLS, como se fosse um 'pacote'. Ao liberar a Competência o sistema gera uma mensagem, e através do WS (Web Service) o 'pacote' é entregue para o TOOLS com todas as informações.

Quando o envio dessas mensagens é processado pelo WS o TOOLS, por sua vez, retorna uma mensagem de confirmação (gravando-a no Monitor da Fila de Integração) informando se tudo chegou com sucesso ou não. Veja abaixo os status:

1 - Processado com Sucesso

99 - Erro Para cada registro enviado que o retorno for diferente de 'Processado com Sucesso' o TOTVS Business Conector deverá gerar um Log deste erro no Monitor da Fila de Integração e continuar enviando os registros até finalizar todo o processo (não parando assim o envio do 'pacote' quando existir um erro). Com essa comunicação são integradas as funcionalidades: Baixar Parcelas, Demissão de Funcionários.

---

**Clique nos links abaixo para mais informações desta integração.**
