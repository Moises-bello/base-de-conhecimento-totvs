---
content_hash: eb4c048531cd91aed2f9920b615c596036b37f894f4d8e3b7b3a7fe782cfd8af
fetched_at: '2026-06-29T00:11:39.707576+00:00'
page_id: '789399301'
product: rm
source: tdn-rm
title: Envio de mensagens básico - automática, manual ou agendada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789399301
version: 5
---

O envio de mensagens do TOTVS Educacional para o Meu eduCONNECT pode ser realizado de duas formas: básica e [avançada](http://tdn.totvs.com/x/UbmcEw).

Nessa documentação será possível encontrar informações sobre como enviar mensagens de forma manual ou agendada. Para isso, basta acessar o menu  **'Sistema' Educacional | Acesso Menu|****Atividades acadêmicas | Central de Comunicações | Agendamento/envio de mensagens.**

A seguir, uma explicação detalhada para cada um dos campos da tela do processo.

**Tipo da Mensagem:**

1. **Pré Configurada:**o tipo de mensagem pré-configurada permite utilizar mensagens cadastradas previamente na central de comunicação através do item de menu **'Sistema' Educacional | Acesso Menu|****Atividades acadêmicas | Central de Comunicações | Mensagens.**
2. **Texto livre:** permite que o conteúdo da mensagem seja criado durante a execução do processo.

   Informação importante

   Mensagens enviadas como sendo do tipo "Texto livre" NÃO serão gravadas para consulta no painel de gestão e seu conteúdo NÃO poderá ser utilizado para envios posteriores.

**Enquete:**o tipo "Enquete" necessita que uma mensagem seja criada previamente na central de comunicação através do item de menu **'Sistema' Educacional | Acesso Menu|****Atividades acadêmicas | Central de Comunicações | Mensagens.** Ao selecionar essa opção o usuário só poderá escolher como modelo de mensagem a ser enviada, mensagens criadas conforme foi citado anteriormente e cuja opção "Enviar como enquete" esteja marcada dentro do cadastro da mensagem, na pasta "eduCONNECT".

# Agendamento /envio das mensagem do tipo "Enquete"

Para enviar as mensagens do tipo enquete, o usuário deverá selecionar o tipo da mensagem: Enquete.

Clicar na lookUp: Mensagens pré configuradas, onde serão exibidas apenas as mensagens onde parametrizadas do como enquete serão exibidas.

Ainda neste processo, o usuário poderá alterar apenas o texto da mensagem.

false

O usuário terá a opção de responder a enquete apenas uma vez.

Após responder a enquete, a mensagem e as opções de enquete ficará disponível para o usuário, porém, não será possível responder novamente.

Informação importante

Para o tipo de mensagem "Pré-configurada" e objetivo "**Boleto próximo ao vencimento**" e que NÃO seja consulta SQL, deve-se informar o parâmetro "**Quantidade de dias para vencimento do boleto**". Informando a quantidade de dias, será possível enviar notificação para os lançamentos (boletos) **em aberto** **(não vencidos)**.

**Exemplo:**

Para enviar notificação aos usuários com esse objetivo e que possuem boletos com vencimento em 10 dias, basta informar o campo "Quantidade de dias para vencimento do boleto" com o valor 10, que ao executar o processo o sistema irá calcular os dias de vencimento do boleto a partir da data atual, e caso encontre algum boleto com vencimento em até 10 dias, estes serão notificados.

Data atual de execução do processo: 01/01/2022

Quantidade de dias para vencimento do boleto: 10

Boleto com vencimento: 09/01/2022

No exemplo acima, temos o boleto com vencimento "09/01/2022", portanto a notificação será enviada pois este possui 9 dias até o vencimento, que é menor que os 10 dias informados para execução do processo.

**Consulta SQL**  
Para que seja possível enviar mensagens por consulta SQL é necessário habilitar o parâmetro do educacional 'Enviar com base em consulta SQL' acessando "**Perfil de usuário | Anexo Parâmetros Educacionais | Central de comunicação",** conforme mostrado no item [03.2 - Permissões de acesso e público alvo](http://tdn.totvs.com/x/7_BbGQ)**.**

Informação importante

Só será permitido envio de mensagens através de consulta SQL caso o tipo de mensagem esteja definido para "Pré-configuradas" e seu objetivo seja "**Enviar mensagens eventuais via e-mail, Fluig ou eduCONNECT**" e/ou "**Boleto próximo ao vencimento**" e NÃO é possível definir um público alvo para esse tipo de envio, uma vez que o público alvo será definido dentro da consulta SQL.

Após selecionar o tipo de mensagem a ser enviada (ou a opção de consulta SQL), o próximo passo dependerá das configurações de permissão de perfil já citadas anteriormente.

Caso o parâmetro "Permitir alteração do conteúdo da mensagem selecionada no processo de envio de Notificação" estiver DESMARCADO o usuário verá a tela com a mensagem a ser enviada, porém não poderá fazer alterações.

Caso contrário, o usuário terá permissão de alterar as informações do template de mensagem que foi selecionado para envio.

Optando por uma mensagem do tipo "Texto Livre" é possível preencher os campos na aba eduCONNECT, já que não será permitido selecionar um modelo de mensagem cadastrado previamente.

Ao avançar etapa, será apresentada a tela para filtro do público alvo definido.

Informação importante

Se a opção **“Seleção de alunos por filtro”** estiver marcada, a funcionalidade filtrará as matrizes aplicadas conforme a parametrização por curso, permitindo selecionar no campo **“Turno”** apenas as matrizes aplicadas que possuam parametrização por curso cadastrada no período letivo selecionado.

Se a opção **“Seleção de aluno por R.A.”** estiver marcada, serão listados apenas os alunos matriculados no período letivo selecionado. O mesmo comportamento se aplica à seleção de **professores** e **coordenadores**.

Caso tenha sido selecionada a opção "Consulta SQL", será habilitado o filtro para seleção da sentença SQL contendo os destinatários para a mensagem.

Informação importante

Para a opção "Consulta SQL":

* Objetivo "**Boleto próximo ao vencimento**", a consulta SQL deverá retornar obrigatoriamente os campos: CODCOLIGADA, CODUSUARIO, EMAIL, RA, NOME, NOMEDESTINATARIO e IDBOLETO.
* Objetivo "**Enviar mensagens eventuais para via e-mail, Fluig ou eduCONNECT**", a consulta SQL deverá retornar obrigatoriamente os campos: EMAIL e  CODUSUARIO.

É importante ressaltar que o campo "CODUSUARIO" corresponde ao usuário vinculado a pessoa retornada pela consulta (pessoa vinculada ao e-mail), este é o mesmo usuário de acesso ao sistema ou portal do aluno.

false

Essa funcionalidade está disponível a partir da release 12.1.26 do TOTVS Educacional.

Na ultima etapa, caso seja possível, poderá ser definido o momento de execução do processo, através do agendamento.

Atenção

Ao término de execução do processo, o sistema poderá exibir uma mensagem de "Atenção", informando que não foi possível enviar a notificação via Push para um ou mais usuários. Mas a mensagem de notificação será salva normalmente na API do eduCONNECT e apenas o momento de enviar o Push para o dispositivo (celular) do usuário poderá ocorrer algum problema.

No exemplo abaixo, mostra que foram "criadas e enviadas" o total de 6 mensagens, mas apenas para um usuário "ES-00101" o sistema não conseguiu enviar o Push (Notificação no celular), mas a mensagem deste usuário foi salva com sucesso, e quando o usuário "ES-00101" acessar o menu "Notificação" (Timeline) a partir do aplicativo Meu eduCONNECT poderá visualizar a mensagem normalmente.
