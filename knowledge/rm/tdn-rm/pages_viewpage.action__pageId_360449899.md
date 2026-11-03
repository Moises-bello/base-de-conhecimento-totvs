---
content_hash: 761e2a9584935331daa5acc563c7f242b5caad88ae2b8ee335d65f02c0d93177
fetched_at: '2026-06-29T00:08:58.451233+00:00'
page_id: '360449899'
product: rm
source: tdn-rm
title: Orientações eSocial RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=360449899
version: 9
---

# RM eSocial

```

```

**TAF**

O TAF - TOTVS Automação Fiscal é a nova plataforma da TOTVS especializada na consolidação dos movimentos fiscais de forma +compacta para atender as obrigações acessórias impostas pelo Governo, e tem como objetivo suportar o processo tributário permeando as Obrigações Principais e Acessórias pelas Demonstrações, Apurações e Cálculos de Tributos.

Conheça mais em: <http://tdn.totvs.com/display/TAF/Manual+do+TAF>

Veja detalhes de como instalar o TAF:

Instalação <http://tdn.totvs.com.br/pages/releaseview.action?pageId=331868191>

Atualização <http://tdn.totvs.com.br/pages/releaseview.action?pageId=344461282>

**TSS**

O TSS (TOTVS Service SOA) é um software baseado na arquitetura orientada a serviços, em que o objetivo principal é prover os serviços de emissão e manutenção de documentos fiscais eletrônicos.

Conheça mais em: <http://tdn.totvs.com/display/LRM/TSS+%28TOTVS+Service+SOA%29+-+eSocial>

**TOTVS RM**

A solução RM Gestão Folha de Pagamento também atende todas as necessidades da sua empresa na regulamentação com o eSocial.

Veja mais informações em: <http://tdn.totvs.com/display/LRM/eSocial+%7C+RM+-+Entregas+Legais>

Dúvidas do eSocial: <http://tdn.totvs.com/display/public/ConSeg/Perguntas+e+Respostas+eSocial>

FAQ: <http://tdn.totvs.com/display/LRM/01.+FAQ+-+TOTVS+Folha+de+Pagamento>

**PASSO A PASSO PARA CADA FASE DO ESOCIAL NO RM**

**1ª Fase**

Carga Inicial - Envio de dados

Início da obrigatoriedade do carregamento das tabelas iniciais das empresas no sistema de produção do eSocial.  
Sendo os eventos:

S-1000 - Informações do Empregador/Contribuinte/Órgão Público  
S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos  
S-1010 - Tabela de Rubricas  
S-1020 - Tabela de Lotações Tributárias  
S-1030 - Tabela de Cargos/Empregos Públicos \*  
S-1050 - Tabela de Horários/Turnos de Trabalho \*  
S-1070 - Tabela de Processos Administrativos/Judiciais

*\* Eventos excluídos a partir do leiaute S-1.0*

Veja mais detalhes sobre as fases e prazos em: <http://tdn.totvs.com/display/LRM/Faseamento+da+entrega+-+Prazos+e+eventos>

1º Passo - Configurações no RM (Parametrizador | eSocial)

Deverá configurar o “Tipo de Ambiente” e “Datas de Obrigatoriedade”. Clique aqui para ver detalhes (  )

Deverá configurar a integração com o TAF e ou Middleware. Clique aqui para ver detalhes ( ou  )

2º Passo – **eSocial | Software House**

<https://tdn.totvs.com.br/display/LRM/Software+House>

3º Passo – **eSocial | Informações do Empregador**

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718306>

4º Passo – **eSocial | Endereços**

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719564>

5º Passo – **eSocial | Lotação Tributária**

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719593>

6º Passo – **eSocial | Validador da Base de Dados**

Realizar a validação da base de dados dos eventos de tabelas inicial (S-1000 a S-1070), conforme obrigatoriedade definidas no leiaute do eSocial. Clique aqui para ver detalhes <https://tdn.totvs.com.br/display/LRM/Validador+da+Base+de+Dados>

Lembrando que é possível realizar alguns tipos de parametrizações conforme abaixo. Para ter acesso a todos as informações do parametrizador do eSocial, acesse:

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718787>

7º Passo – **eSocial | Gerar Gatilhos Eventos Iniciais**

Gerar registros da fila de eventos do eSocial, ainda sem as informações do XML. Sua função é sinalizar a necessidade de envio de informações para o Governo para dar início a vida da empresa no eSocial. Serão considerados os eventos de tabelas inicial (S-1000 a S-1070).

Clique aqui para ver detalhes <https://tdn.totvs.com.br/display/LRM/Gerar+Gatilhos+Eventos+Iniciais>

9º Passo – **eSocial | Fila de Eventos:** Possibilita monitorar os registros dos eventos do eSocial gerados pelos gatilhos, bem como seus status. Podendo também verificar os erros de geração e informações da integração com TAF.

Clique aqui para ver detalhes <https://tdn.totvs.com.br/display/LRM/Fila+de+Eventos>

10º Passo – **eSocial | Gerar XML:** Gera a estrutura de XML dos registros existentes na “[Fila de Eventos](https://tdn.totvs.com.br/display/LRM/Fila+de+Eventos)” ou criar os ["Eventos Periódicos"](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719672)  para Integrar com TAF (ou com o TSS via Middleware).

Clique aqui para ver detalhes <https://tdn.totvs.com.br/display/LRM/Gerar+XML>

Para agilizar e facilitar o dia-a-dia do usuário este processo pode ser agendado.

11º Passo – **eSocial | Integrar com TAF** ou **eSocial | Enviar XML**: Envia os arquivos XML existentes na “Fila de Eventos” ou em "Eventos Periódicos" para o TAF (ou para o governo, caso utilize o Middleware), de acordo com o status do evento.

Clique aqui para ver detalhes  /

Para agilizar e facilitar o dia-a-dia do usuário este processo pode ser agendado.

**Caso utilize o Middleware, pule para o passo 15**

12º Passo - **TAF – Processamentos (Transferir registros para tabela de negócio)**

Os eventos do eSocial enviados pelo RM ficarão “pendente” na base do TAF até serem processados, ou seja, após o processamento desses eventos os mesmos serão inseridos nas tabelas de negócio existentes no TAF.

Clique aqui para ver detalhes <http://tdn.totvs.com/display/public/TAF/03.+Processamento+manual>

13º Passo – **TAF – Processamentos (Validar registros importados)**

Após a execução do 12º passo, será necessário executar o processo “Validar Base do TAF” para que seja comparado as informações importadas com o leiaute disponibilizado pelo governo.

Clique aqui para ver detalhes <http://tdn.totvs.com/display/public/TAF/03.+Processamento+manual>

14º Passo – **TAF – Monitoramento**

No menu Monitoramento é possível verificar como se encontra a “vida da empresa” no eSocial, podendo visualizar quais registros foram integrados, rejeitados ou que ainda se encontram pendente para envio.

Clique aqui para ver detalhes <http://tdn.totvs.com/display/public/TAF/Monitor+do+eSocial+-+TAFMONTES+-+TAF+-+P12>

Selecione o status, evento, tipo de visão e qual o período que será consultado para visualização.

Após aplicar o filtro criado acima, será listado um resumo dos eventos. Para transmitir ao governo, basta selecionar os eventos e clicar no botão Transmitir ao Governo.

Caso queira visualizar o retorno do governo referente a um evento especifico, basta selecionar o tipo do evento que será consultado e clicar no botão “Detalhamento”. Na visão que será aberta, selecione o evento que deseja consultar e clique no botão “Inconsistência”.

15º Passo – **eSocial | Atualizar Status Integração TAF**

Atualiza os status dos eventos existentes na Fila de Eventos conforme status atual dos eventos no TAF.

Clique aqui para ver detalhes

Obs: Para agilizar e facilitar o dia-a-dia do usuário este processo pode ser agendado.

16º Passo - **eSocial | Fila de Eventos | Erro de Integração**

Para os eventos rejeitados pelo Governo, o detalhamento da possível inconsistência será visível através do TAF ou através da fila de eventos do RM.

**PONTOS**

Como avaliar as inconsistências retornadas pelo RET <http://tdn.totvs.com/pages/viewpage.action?pageId=337358841>
