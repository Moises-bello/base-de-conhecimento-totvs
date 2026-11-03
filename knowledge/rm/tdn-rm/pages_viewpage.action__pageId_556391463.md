---
content_hash: 7de436129a99a51a1e4a0b719c2c164cee753c4b018cf2b5403c166abbe37d66
fetched_at: '2026-06-29T00:10:46.938956+00:00'
page_id: '556391463'
product: rm
source: tdn-rm
title: S-2206 - Alteração Contratual para o eSocial referente a Prorrogação/Antecipação/Cancelamento
  - MP 936/2020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556391463
version: 37
---

false

**A partir das Versões:**

* 12.1.24.305
* 12.1.25.295
* 12.1.26.258
* 12.1.27.240
* 12.1.28.149
* E Superiores.

Objetivo

Demonstrar as formas de geração do evento "S-2206 - Alteração de Contrato de Trabalho" do eSocial para atender ao cadastro do B.E.M. com o Tipo de adesão "Redução da carga horária".

1true1Execução do scriptExecução do script

Para a criação de todos os campos do B.E.M. no cadastro do funcionário é necessário executar o script através do sistema RM.Atualizador.exe.

2B.E.M.B.E.M.

Conforme orientação do eSocial, o empregador deverá enviar o evento "S-2206 - Alteração de Contrato de Trabalho" com as seguintes informações:

* O campo "Data de Alteração" deverá ser igual ao início do período de redução de salário e jornada e, neste evento, informar o valor do salário reduzido e a nova jornada a ser cumprida pelo trabalhador durante esse período.
* O campo "Observação" deverá conter o prazo pactuado para a referida redução e o percentual definido para essa redução proporcional.

Ao preencher no funcionário os dados do B.E.M. com o tipo de adesão "**Redução da carga horária**" será gerado um gatilho do evento "S-2206 - Alteração de Contrato de Trabalho", com as informações referentes ao cadastro, sendo que:

* A tag <dtAlteracao> será igual ao valor do campo "**Data do acordo"**que corresponde ao início do período de redução de salário e jornada;
* A tag <vrSalFx> terá o valor do salário reduzido (valor do campo **"Salário"** menos o valor do campo "**Valor reduzido"**);
* A tag <qtdHrsSem> será a nova jornada a ser cumprida pelo trabalhador (valor do campo **"Jornada semanal"** menos o valor do campo "**Percentual de redução da Jornada"**, sendo que, se o parâmetro "**Desconsiderar % de redução no cálculo da jornada - MP 936/20 (Integração com TOTVS Automação de Ponto)"**estiver marcado será considerada a jornada informada no horário);
* A tag <observacao> será descrito o prazo pactuado da redução (considerando os dias de prorrogação e/ou data da antecipação) e o percentual definido no campo "**Percentual de redução da Jornada"**.

**Atenção:**

* Caso o tipo de recebimento do funcionário seja "H - Horista" ou "P - Horista (Professor)", deverá deixar o campo "**Valor reduzido"** zerado.
* Caso o preenchimento dos campos do cadastro do **B.E.M.**sejam pelo processo global, somente será gerado gatilho se o campo "**Data do acordo"** for preenchido.
* Nos eventos S-2206 referente a alteração salarial por dissídio, as informações do B.E.M serão desconsideradas.

2true2-1Acordo B.E.MAcordo B.E.M

Após preencher no funcionário os dados do B.E.M. com o tipo de adesão "**Redução da carga horária**" será gerado um gatilho do evento "S-2206 - Alteração de Contrato de Trabalho", com as informações referentes ao cadastro.

Exemplo do xml do evento S-2206 conforme cadastro acima.

falseImportante

* Caso o preenchimento dos campos do cadastro do **B.E.M.** já tenham sido realizados antes das versões que geram automaticamente os gatilhos dos novos campos (versões mencionadas no inicio desta documentação), será necessário gerar o gatilho do evento "S-2206 - Alteração de Contrato de Trabalho" manualmente por funcionário ou através do processo [Gerar Gatilhos em Lotes](https://tdn.totvs.com/display/LRM/Gerar+Gatilhos+em+Lotes) para uma seleção de funcionários (a data de alteração no processo deverá ser igual a data do acordo cadastrada)**.**
2-2Cancelamento B.E.MCancelamento B.E.M

Com a liberação da versão 3.0 do Arquivo do BEM realizada pelo Governo, é possível realizar 3 tipos de operações:

1. Cancelamento

2. Prorrogação

3. Antecipação

Iremos apresentar abaixo exemplos de como irá funcionar para o eSocial quando for um **"Cancelamento"**.

**Exemplo 1 - Evento com Status Aceito RET**

Feito o cadastro do B.E.M. para a data 01/04/2020:

O sistema gera o gatilho do evento S-2206 na fila de eventos e este é enviado ao RET.

Feito o cadastro da data do cancelamento para o dia 02/04/2020:

O sistema verifica se o evento já foi enviado ao RET, caso sim, gera um gatilho S-3000 para exclusão deste evento com as informações do acordo B.E.M.

**Exemplo 2 - Evento com Status Gerado**

Feito o cadastro do B.E.M. para a data 01/04/2020:

O sistema gera o gatilho do evento S-2206 e este encontra-se na fila de eventos com o status "Gerado".

Feito o cadastro da data do cancelamento para o dia 02/04/2020:

O sistema verifica se o evento ainda encontra-se na fila, e caso não foi enviado ao RET apaga o gatilho deste evento da fila de eventos.

falseImportante

* Caso possua alguma outra alteração, exemplo, "mudança de função", com a mesma data do acordo do B.E.M., será necessário a geração do gatilho manual para envio dessas informações.
* Caso o preenchimento dos campos do cadastro do **B.E.M.** já tenham sido preenchidos antes das versões que geram os gatilhos automaticamente dos novos campos (versões mencionadas no inicio desta documentação), será necessário a geração do gatilho manual do evento "S-3000 - Exclusão de Evento" ou "S-2206 - Alteração de Contrato de Trabalho" por funcionário.
3Prorrogação B.E.M.Prorrogação B.E.M.

Com a liberação da versão 3.0 do Arquivo do BEM realizada pelo Governo, é possível realizar 3 tipos de operações:

1. Cancelamento

2. Prorrogação

3. Antecipação

Iremos apresentar abaixo exemplos de como irá funcionar para o eSocial quando for uma **"Prorrogação"**.

falseImportante

* é necessário executar o atualizador na base para habilitar o novo parâmetro "Data Prorrogação BEM"
33-1Primeira prorrogaçãoPrimeira prorrogação

Iremos apresentar abaixo exemplos de como irá funcionar para o eSocial quando for a primeira **"Prorrogação"**.

**Exemplo 1 - Evento com Status Aceito RET**

Feito o cadastro do B.E.M. para a data 01/04/2020:

O sistema gera o gatilho do evento S-2206 na fila de eventos e este é enviado ao RET.

Evento S-2206 foi enviado com a tag observação com o prazo pactuado conforme cadastro.

Feito o cadastro dos dias de prorrogação quantidade 30 dias:

O sistema verifica se o evento já foi enviado ao RET, caso sim, será gerado um novo gatilho de alteração do evento S-2206 com a tag <indRetif> igual a 2-Retificação.

Após a geração do evento S-2206 a tag observação terá o prazo pactuado atualizado considerando os dias de prorrogação.

**Exemplo 2 - Evento com Status Gerado**

Feito o cadastro do B.E.M. para a data 01/04/2020:

O sistema gerou o gatilho do evento S-2206 na fila de eventos e este está com status gerado.

Evento S-2206 foi gerado com a tag observação com o prazo pactuado conforme cadastro.

Feito o cadastro dos dias de prorrogação, sendo a quantidade igual 30 dias:

O sistema verifica se o evento esta na fila e não foi enviado para o RET, caso sim, altera o gatilho para o status de "Pendente".

Após a geração do evento S-2206 a tag observação terá o prazo pactuado atualizado considerando os dias de prorrogação.

3-2Segunda prorrogaçãoSegunda prorrogação

Iremos apresentar abaixo exemplos de como irá funcionar para o eSocial quando for a segunda **"Prorrogação"**.

**Exemplo 1 - Evento de retificação da primeira prorrogação com Status Aceito RET**

Na fila de eventos a retificação da primeira prorrogação já foi enviada.

Histórico atual.

Feito o cadastro do B.E.M. para a data 01/04/2020 e o cadastro de mais uma prorrogação com quantidade 30 dias:

Histórico após o novo cadastro.

O sistema verifica se o evento já foi enviado ao RET, caso sim, será gerado um novo gatilho de alteração do evento S-2206 com a tag <indRetif> igual a 2-Retificação.

Após a geração do evento S-2206 a tag observação terá o prazo pactuado atualizado considerando os dias de prorrogação dos dois históricos.

**Exemplo 2 - Evento de retificação da primeira prorrogação com Status Gerado**

Na fila de eventos a retificação da primeira prorrogação ainda não foi enviada.

Histórico atual.

Feito o cadastro do B.E.M. para a data 01/04/2020 e o cadastro de mais uma prorrogação com quantidade 30 dias:

Histórico após o novo cadastro.

O sistema verifica se o evento esta na fila e não foi enviado para o RET, caso sim, altera o gatilho para o status de "Pendente".

Após a geração do evento S-2206 a tag observação terá o prazo pactuado atualizado considerando os dias de prorrogação dos dois históricos.

  
falseImportante

* Caso o preenchimento dos campos do cadastro do **B.E.M.** já tenham sido realizados antes das versões que geram automaticamente os gatilhos dos novos campos (versões mencionadas no inicio desta documentação), será necessário gerar o gatilho do evento "S-2206 - Alteração de Contrato de Trabalho" manualmente por funcionário ou através do processo [Gerar Gatilhos em Lotes](https://tdn.totvs.com/display/LRM/Gerar+Gatilhos+em+Lotes) para uma seleção de funcionários (a data de alteração no processo deverá ser igual a data do acordo cadastrada)**.**

2-4Antecipação B.E.MAntecipação B.E.M

Com a liberação da versão 3.0 do Arquivo do BEM realizada pelo Governo, é possível realizar 3 tipos de operações:

1. Cancelamento

2. Prorrogação

3. Antecipação

Iremos apresentar abaixo exemplos de como irá funcionar para o eSocial quando for uma **"Antecipação"**.

**Exemplo 1 - Evento com Status Aceito RET**

Feito o cadastro do B.E.M. para a data 01/04/2020:

O sistema gera o gatilho do evento S-2206 na fila de eventos e este é enviado ao RET.

Evento S-2206 foi enviado com a tag observação com o prazo pactuado conforme cadastro.

Feito o cadastro da data de antecipação para o dia 30/05/2020:

O sistema verifica se o evento já foi enviado ao RET, caso sim, será gerado um novo gatilho de alteração do evento S-2206 com a tag <indRetif> igual a 2-Retificação. 

Após a geração do evento S-2206 a tag observação terá o prazo pactuado atualizado considerando a data de antecipação.

**Exemplo 2 - Evento com Status Gerado**

Feito o cadastro do B.E.M. para a data 01/04/2020:

O sistema gerou o gatilho do evento S-2206 na fila de eventos e este está com status gerado.

Evento S-2206 foi gerado com a tag observação com o prazo pactuado conforme cadastro.

Feito o cadastro da data de antecipação para o dia 30/05/2020:

O sistema verifica se o evento esta na fila e não foi enviado para o RET, caso sim, altera o gatilho para o status de "Pendente".

Após a geração do evento S-2206 a tag observação terá o prazo pactuado atualizado considerando a data de antecipação.

falseImportante

* Caso o preenchimento dos campos do cadastro do**B.E.M.** já tenham sido realizados antes das versões que geram automaticamente os gatilhos dos novos campos (versões mencionadas no inicio desta documentação), será necessário gerar o gatilho do evento "S-2206 - Alteração de Contrato de Trabalho" manualmente por funcionário ou através do processo [Gerar Gatilhos em Lotes](https://tdn.totvs.com/display/LRM/Gerar+Gatilhos+em+Lotes) para uma seleção de funcionários (a data de alteração no processo deverá ser igual a data do acordo cadastrada)**.**

true2-5Liberação de competênciaLiberação de competência

Conforme orientação do eSocial, após o período do acordo B.E.M. é necessário o envio do evento de alteração contratual (S-2206) atualizado as informações novamente de salário e jornada do funcionário. Este gatilho ocorrerá de forma automática na liberação da competência a partir das versões citadas neste documento.

falseImportante

* Caso o preenchimento dos campos do cadastro do**B.E.M.** já tenham sido realizados antes das versões que geram automaticamente os gatilhos dos novos campos (versões mencionadas no inicio desta documentação) ou o acordo tenha se iniciado e terminado dentro da mesma competência, será necessário gerar o gatilho do evento "S-2206 - Alteração de Contrato de Trabalho" manualmente por funcionário ou através do processo [Gerar Gatilhos em Lotes](https://tdn.totvs.com/display/LRM/Gerar+Gatilhos+em+Lotes) para uma seleção de funcionários (a data de alteração no processo deverá ser igual a data do acordo cadastrada)**.**
