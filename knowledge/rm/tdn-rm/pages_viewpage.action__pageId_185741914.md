---
content_hash: cdeabb31688e47687aac488a3016f460b82536b4e31858e66b3beb784b182245
fetched_at: '2026-06-29T00:05:58.175334+00:00'
page_id: '185741914'
product: rm
source: tdn-rm
title: Cadastro de horários .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185741914
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Automação de Ponto |
| **Processo** | **:** | Horários |
| **Subprocesso** | **:** | Cadastro de horários .Net |
| **Versão** | **:** | 11.20 |

# Introdução

---

Este roteiro visa demonstrar o procedimento para cadastro de horários nas telas .Net.

# Procedimento

---

 A forma de cadastrar horários foi alterada nas telas .Net.

 Para criar novos horários, será necessário acessar o módulo, **Cadastros/Tabelas auxiliares/Horários**.

Após clicar no botão incluir, será apresentada a seguinte tela:

Imagem (clique aqui)

Informar o código, a descrição, o tipo do horário e a parametrização do mesmo.

**Observação:** Os tipos de horário, antes informados no cadastro do funcionário, agora devem ser informados diretamente no cadastro de horário.

Parâmetros

*Horário Inativo:*Um horário quando inativo não ficará visível para escolha nos parâmetros do funcionário, em alterações globais de horário ou no RM Portal.

*Considera feriados no cálculo:*Por default, esse parâmetro vem marcado e irá considerar os feriados cadastrados no calendário associado à seção do funcionário. Caso ele seja desmarcado, o sistema não irá considerar os feriados.

*Horário de Escala:*Determina se o horário será de escala. O horário será apresentado no menu de alteração global de escala.

*Considera feriado no início da jornada do dia anterior:*Para considerar o dia anterior ao feriado como início do feriado e seu término será no próprio dia em que o feriado foi cadastro.

Segue abaixo, um exemplo de criação de um horário do tipo Rígido:

Imagem (clique aqui)

Após selecionar o tipo do horário, clicar no botão ‘Salvar’. Selecionar a opção **Anexos/Jornada**. Será apresentada na tela uma nova aba: "Jornada". Nesta aba, será necessário selecionar a opção Processos/Criar jornada planejada

Imagem (clique aqui)

 Será aberto um assistente para a montagem do horário. Basta preencher as informações e clicar no botão avançar.

Imagem (clique aqui)

Na tela **Índice da jornada**, será necessário informar a letra que será associada ao primeiro índice (letra não obrigatória como em versões anteriores). Nas telas .Net, ao cadastrar a jornada, o primeiro índice sempre será igual ao primeiro dia do período atual.

Imagem (clique aqui)

Na tela, **Tipo da jornada**, será necessário informar se o índice que está sendo criado se trata de um dia trabalhado, compensado, descanso ou um dia com batida nula.

Imagem (clique aqui)

Na próxima tela, **Intervalos Planejados da Jornada**, será cadastrado o intervalo de trabalho do funcionário. Para criar o segundo intervalo, basta clicar no botão incluir que está no canto superior esquerdo da tela. Também será possível informar a tolerância de extras e atrasos, na saída e entrada do Intervalo Planejado.

Imagem (clique aqui)

Na tela seguinte, **Ausência Planejada**, será cadastrado o período em que o funcionário estará ausente para cumprir seu intervalo de refeição.

Imagem (clique aqui)

A tela que será apresentada a seguir, **Visualização da Jornada**, demonstrará a jornada cadastrada para este índice. Será possível informar os seguintes campos:

*Índice Fim*

Caso seja necessário altere o índice fim conforme intervalos planejados da jornada. Normalmente essa alteração só se faz necessária quando a jornada é de um dia para o outro.

*Falta*

Caso queira que o sistema calcule um número de horas de falta diferente do que será calculado conforme a jornada cadastrada, informe neste campo o número de horas de falta que deseja.

**Exemplo:**

Intervalos Planejados da Jornada (Intervalos de Trabalho)  
[08:00 12:00] [14:00 18:00] = 08:00 Horas  
 Falta  
08:30  
 Funcionário não efetuou as batidas. Serão calculadas 08:30h de falta para ele.

*Extra para Lançamento de Batidas*

Caso queira lançar horas extras para o funcionário no momento do lançamento global de horários, informe neste campo o valor a ser lançado.

Após cadastrar um valor neste campo, no momento do lançamento global de horários, o parâmetro "Lança Horário lançando horas extras" deve ser habilitado.

Imagem (clique aqui)

Após isso, este índice estará criado.

Imagem (clique aqui)

As próximas jornadas trabalhadas, podem ser criadas manualmente, como no processo anterior, ou o índice 1 poderá ser copiado, para facilitar a criação do horário. Para efetuar a cópia de um índice já criado, basta selecionar este índice e selecionar a opção **Processos/Copiar Jornada Planejada**.

Imagem (clique aqui)

Neste exemplo, irei efetuar a cópia duas vezes, criando os índices 2 e 3 (quinta-feira e sexta-feira, respectivamente).

Imagem (clique aqui)

Para criar os índices de descanso e compensado, basta efetuar o mesmo processo anterior, porém, na tela **Tipo de Jornada**, deverão ser marcados os campos **Compensado** ou **Descanso**.

Imagem (clique aqui)

Uma particularidade do cadastro de um dia de descanso ou compensado no cálculo .Net, é que eles devem começar às 00:00h de um dia e terminar às 00:00h do próximo dia. No caso deste horário, o dia compensado (sábado) irá iniciar às 00:00h do dia 04/12/2010 e terminar ás 00:00h do dia 05/12/2010, conforme o print abaixo:

Imagem (clique aqui)

Após a criação dos índices de descanso e compensado, deverão ser criados os dois índices restantes, neste caso, índices 6 e 7 (segunda-feira e terça-feira, respectivamente). O processo de **Copiar Jornada Planejada**, poderá ser usado na criação destes índices.

Imagem (clique aqui)

Caso um índice tenha sido criado incorretamente, ele poderá ser alterado ou excluído. Isto poderá ser realizado através das opções **Processos | Configurar Jornada Planejada** ou **Remover | Configurar Jornada Planejada**.

Imagem (clique aqui)

Uma vez que todos os índices foram criados, o horário poderá ser visualizado através da opção **Anexos | Visualizar Horário**.  Será aberta uma nova aba onde poderão ser visualizados todos os dias do período.

Imagem (clique aqui)

Poderão ser informados os Limites de Tolerância para a jornada planejada, através da opção **Anexos | Limite de Tolerância**.

Imagem (clique aqui)

O limite de tolerância serve para limitar dentro do período, da semana ou do dia, o número de vezes ou o número de horas que será aplicada a tolerância cadastrada nos Intervalos Planejados da Jornada. O mesmo deve ter um tipo de ocorrência associado e deve ser associado a um horário.

 Maiores informações sobre esta funcionalidade [acesse](http://wikihelp.totvs.com.br/WikiHelp/RHU/PTO.limiteTolerancia.aspx).

# **Horários do tipo Flexível e Semi-flexível**

---

No cadastro dos horários do tipo ‘Flexível’ e ‘Semi-flexível’, a tela ‘Ausência Planejada’, será alterada para ‘Intervalo com Tempo Planejado (Limite de Refeição)’. No novo cálculo .Net, será possível informar Intervalos de Ausência para os horários do tipo ‘Flexível’.

**Observação:** o cadastro do Intervalo com Tempo Planejado, somente é obrigatório para horário Semi-Flexível.  Para horário Flexível, este cadastro é opcional.

*Tempo Mínimo*

Cadastre o tempo mínimo que o funcionário deverá realizar no Intervalo de Ausência. Caso o funcionário tenha uma ausência menor que o tempo mínimo cadastrado, o sistema irá calcular hora extra até o tempo mínimo, o restante não será calculado.

**Exemplo:**

Intervalos Planejados da Jornada (Intervalos de Trabalho)  
[08:00 11:00] [15:00 18:00]

Intervalo com Tempo Planejado  
[11:00 15:00]

Intervalo de Ausência  
[12:00 14:00] = 02:00

 Tempo Mínimo  
[01:00]

Funcionário executou as batidas  
[08:00 12:40] [13:30 18:00]  
[12:40 13:30] = 00:50 Minutos

O sistema irá calcular 00:10 de hora extra.

Se não houvesse o tempo mínimo cadastrado o sistema calcularia 01:10 de hora extra.

Imagem (clique aqui)

**Horário Núcleo**

---

 Podem ser definidos intervalos dentro do horário em que o funcionário deve respeitar rigorosamente as batidas cadastradas. Os outros intervalos do horário, serão intervalos compensáveis.

**Observação:** o cadastro do Intervalo com Tempo Planejado é opcional para este tipo de horário.

Imagem (clique aqui)
