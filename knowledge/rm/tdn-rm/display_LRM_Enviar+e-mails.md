---
content_hash: 40177ce11cb1bf79a79063bceda18f302bad4900638bae7a7bd3791248c99a4a
fetched_at: '2026-06-29T00:09:33.876169+00:00'
page_id: '425459071'
product: rm
source: tdn-rm
title: Enviar e-mails
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar+e-mails
version: 15
---

Este processo centraliza a funcionalidade de comunicação com candidatos e profissionais por meio de e-mails.   
No 1º passo do assistente existem três possibilidades para seleção do grupo de destinatários a serem considerados para recebimento do e-mail:

1. Enviar e-mails para candidatos: se não for especificada uma área ofertada ou um candidato, todos os candidatos serão considerados na montagem do filtro de envio.
2. Enviar e-mails para profissionais: se não for especificado um profissional, todos os profissionais serão considerados na montagem do filtro de envio.
3. Enviar e-mails para todos: todos os candidatos e profissionais serão considerados na montagem do filtro de envio.

De acordo com o grupo de destinatários selecionado, no passo seguinte será disponibilizada para o usuário uma lista de opções de "Tipos de emails" possíveis de serem enviados. Cada tipo de e-mail consiste em uma pré-configuração que tem por objetivo auxiliar o usuário a delimitar ainda mais o grupo de destinatários e a definir o conteúdo do e-mail a ser enviado. Os seguintes "Tipos de Emails" estarão disponíveis:

* Para Candidatos: Confirmação de inscrição, Pagamento de inscrição pendente, Local de prova do candidato, Cancelamento de área ofertada, Resultado do processo seletivo, Convocação para matrícula, Documentação pendente e Informações da prova .
* Para Profissionais: Local de trabalho, Confirmação de presença e Confirmação de pagamento.
* Para Todos: Comunicado geral.

**A função dos botões**:

* Tags disponíveis: de acordo com o grupo de destinatários previamente selecionado, apresenta uma lista de tags que poderão ser inseridas no corpo do texto. As tags são marcações inteligentes que serão substituídas por textos específicos durante o processo de montagem do e-mail. Para que possam ser identificadas e "traduzidas", as tags devem ser grafadas totalmente em maiúsculo, por exemplo: PROCESSO\_SELETIVO, NOME\_COLIGADA, NOME\_CANDIDATO, etc. Quando o usuário clicar em uma das tags na lista, ela será adicionada automaticamente na posição em que o cursor se encontrar na caixa de texto.

* Anexar : permite anexar arquivo(s) ao e-mail.
* Remover Anexo: remove o(s) arquivo(s) anexado(s) que está(ão) selecionado(s).

**Observações Importantes sobre o Uso de Tags**:  
A utilização de tags requer cautela por parte do usuário para que o e-mail a ser enviado não apresente informações mal formatadas ou truncadas. O processo de envio apenas tenta "traduzir" tags que foram utilizadas na composição do texto do e-mail. Caso estejam presentes, o processo possui um mecanismo de segurança e não permite que o e-mail seja enviado em caso de impossibilidade de "tradução" das seguintes tags: LOCAL\_PROVA, VALOR\_PAGAMENTO, DATAS\_TRABALHADAS, DATAS\_AUSENTES, TOTAL\_DIAS\_TRABALHADOS e TOTAL\_DIAS\_AUSENTES.

Através da tag "***PROVA\_TESTIS***", ao selecionar o tipo de e-mail "*Informações da prova*", é possível notificar o candidato com informações relacionadas a prova que ele irá executar:

Exemplo da composição da tag:

Etapa: *etapa 1*  
 - Prova: *Redação*  
 - Chave de acesso à prova: *0F01BE6A3F*  
 - Data limite para a realização da prova: *10/09/2020 às 11:37*

Alteração do rótulo 'Inscrição Nº:' na TAG PROVA\_TESTIS

A partir da versão 12.1.2510, o rótulo "Inscrição Nº" da tag "PROVA\_TESTIS" foi substituído por "Chave de acesso à prova".

**Erros que podem impedir o envio de um E-mail**:

1 - As configurações de envio de e-mail não foram corretamente definidas em "Parâmetros Globais";

2 - O e-mail não se encontra corretamente preenchido no "Cadastro de Pessoas" para o candidato ou de "Clientes/fornecedores" para profissionais;

Observação: no caso de candidato, caso o processo seletivo esteja marcado "Utiliza novo portal de inscrições", o e-mail será verificado nos "Dados do usuário do Processo Seletivo";

3 - Impossibilidade de "tradução" uma tag obrigatória presente no corpo do e-mail.

O último passo do assistente permite ao usuário escolher entre realizar uma simulação de envio ou efetivamente enviar os e-mails

**Pré-requisitos do processo**:

a) Correta definição dos parâmetros em "Opções/Parâmetros Globais/Envio de E-Mails".

b) Definição do parâmetro "E-mail de remetente do processo seletivo" em "Opções/Parâmetros/Processo Seletivo/Portal"

**Observações:** :  
Para e-mails do tipo 'Local de prova do candidato', candidatos com a inscrição 'cancelada', 'excedente' ou com o status da opção de 'ausência' ou 'desclassificação' não receberão o e-mail informando o local de prova.

Informações 

A opção de formatação de estilo do texto em formato HTML está disponível à partir das versões **12.1.27.270,** **12.1.28.184 e 12.1.29.109.**

Simulação de envio

O recurso Simulação permite ao usuário ter a real visualização de como o e-mail será enviado. Ao executar o processo é questionado ao usuário se o mesmo deseja salvar o arquivo em formato HTML.

Ao informar que deseja salvar, o usuário deverá escolher em qual local o arquivo será gravado, em seguida clique no botão "Sim" para visualizar o e-mail no navegador.
