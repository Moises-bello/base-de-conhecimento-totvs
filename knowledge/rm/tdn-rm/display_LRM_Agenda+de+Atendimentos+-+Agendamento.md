---
content_hash: 8266831d2860c8f8efa09887a7e6b0feb3e6a1cca0f786e1358c71100c34a520
fetched_at: '2026-06-29T00:10:36.225297+00:00'
page_id: '531031040'
product: rm
source: tdn-rm
title: Agenda de Atendimentos - Agendamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Agenda+de+Atendimentos+-+Agendamento
version: 49
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Pasta indicadores**
3. **Pasta atividades**
4. **Pasta convênios**
5. **Pasta status**
6. **Propriedades da agenda (opções)**
7. **Pasta atividades**
8. **Pasta especialidades**
9. **Pasta Bloqueios**
10. **Pasta período especial**
11. **Pasta exames**
12. **Configuração Personalizada de Períodos da Agenda**
13. **Cadastrando o Período**
14. **Opção semanal**
15. **Opção Mensal**
16. **Personalizada**

sumarioVisão Geral

## **01. VISÃO GERAL**

Importante!

Utilize as setas localizadas nos cantos superior direito e esquerdo do calendário para navegar entre os meses seguintes e anteriores. Essa navegação mantém o dia selecionado no grid inalterado.

Nesta tela você poderá visualizar todas as Agendas de Atendimentos filtradas por tipo e Unidade de Atendimento, visualizar uma Agenda específica de um profissional ou sala selecionando-a no menu a esquerda da tela, visualizar dias em que a Agenda funciona e que tem horários livres em verde no calendário. Ao lado do calendário, foi implementada a opção de se visualizar fotos dos pacientes cadastrados no momento do Registro de Atendimento (Externo e Interno).Caso haja arquivo de foto associado ao paciente, quando o mesmo for carregado na funcionalidade, a imagem será carregada.  
Na parte de cima da tela temos algumas ferramentas como:  
**Visualizar:** Gera um relatório simples da Agenda selecionada por período, mostrando todos os horários livres e ocupados.  
**Opções:** Acessa as Propriedades da Agenda de Atendimento selecionada.  
**Localizar:** Caixa de texto onde é possível pesquisar, pelo nome da especialidade, sala ou profissional do qual se deseja encontrar a Agenda de Atendimento.  
**Pesquisar:** Chama a tela de Pesquisa Paciente, onde é possível visualizar todos os agendamentos existentes incluindo os futuros, para o paciente pesquisado.  
**Atend. Externo:** Permite Registrar um Atendimento Externo para o paciente selecionado.  
Prontuário: Permite acessar o Prontuário Eletrônico do Paciente através da Agenda de Atendimentos.  
**Observação:** Para que esse botão seja habilitado, é necessário que o usuário tenha permissão de acesso ao PEP no Cadastro de Prestador e tenha perfil de Médico definido em Parâmetros Gerais/Prontuário Eletrônico além de o paciente em questão ter um Registro de Atendimento.  
No calendário à direita da tela, após ser escolhido uma agenda, os dias com horários livres passam a ser coloridos de verde.  
**Observação:** Os dias sem horários livres ficarão em branco.  
Mostra também agendamentos da data selecionada, na grade de horários localizada na parte inferior dessa tela, sendo possível incluir ou editá-los clicando 2 vezes em cima da linha da grade.  
**Atenção:** Não será possível incluir e nem editar agendamentos em dias que já se passaram.  
Acima da grade de horários temos uma barra de tarefas que realiza operações nos agendamentos que são:  
**Dia Anterior Livre (F11):** Vai para o primeiro dia livre anterior ao dia selecionado.  
**Próximo dia livre (F12):** Vai para o primeiro dia livre posterior ao dia selecionado.  
**Inserir Encaixe (Insert):** Insere um encaixe no dia selecionado.  
**Observação:** O número máximo de encaixes deve ser respeitado.  
**Remover agendamento (Del):** Exclui o agendamento selecionado.  
**Alterar agendamento (Duplo Click):** Abre o Agendamento selecionado para alterar.  
**Observação:** Não será possível alterar agendamentos em dias que já se passaram.  
**Copiar Agendamento (Ctrl+C):** Copia o agendamento selecionado para ser colado em outro horário / dia.  
**Observação:** No processo de cópia do agendamento, algumas regras são observadas:  
O Convênio de origem deve ser aceito pelo médico de destino.  
A Atividade de origem deve ser aceita pelo médico de destino.  
**Copiar Todos Agendamentos:** Copia Todos os agendamentos do dia para ser colado em outro horário / dia, seguindo as mesmas regras da Copiar Agendamento individual.  
**Observação:** Os agendamentos que são "Encaixes" não serão copiados.  
Mover Agendamento (Ctrl+X): Move o Agendamento selecionado para outro horário / dia.  
**Observação:** No processo de mover agendamentos, algumas regras são observadas:  
O Convênio de origem deve ser aceito pelo médico de destino.  
A Atividade de origem deve ser aceita pelo médico de destino.  
**Mover Todos Agendamentos:** Move todos os Agendamentos do dia para outro horário / dia.  
**Observação:** Os agendamentos que são "Encaixes" não serão movidos.  
Colar Agendamento (Ctrl+V): Cola o(s) agendamento(s) copiado(s) ou movido(s) para o novo horário.  
**Filtrar Encaixes:** Exibe na grade somente os horários que são do tipo "Encaixe".  
Número Prontuário (Ctrl+P): Exibe na Tela o número do prontuário do paciente selecionado.  
**Log de Agendamento:** Irá exibir o Log de alterações (inserção, edição, exclusão e bloqueio) realizadas na Agenda de atendimentos no dia agrupados por horário.  
**Estatísticas:** Irá exibir a Tela de Estatísticas contendo alguns indicadores sobre a Agenda.  
**Atualizar Visão (F5):** Atualiza as informações da grade de Agendamentos selecionada.  
**Informações sobre Agendamento:** Exibe informação sobre quando e quem realizou o primeiro agendamento, e a ultima alteração.  
**Observações da Agenda:** Exibe o conteúdo dco campo complementar do prestador quando preenchido. A tela contendo este campo também pode ser acessada através da tecla de atelho F10 ou clicando no ícone representado pelo "Raio amarelo"..  
**Atenção:**  
Para o status da agenda de atendimento mudar para atendido ao acessar o Pep o sistema deve estar parametrizado em Parametros Gerais\Prontuário Eletrônico\na Aba Geral deve estar marcado a seguinte função:Queixa prncipal e conduta obrigatorios.  
**Atenção:**  
Antes de iniciar a parametrização das Agendas de Atendimento, é importante que se defina quais serão as Agendas que deverão ser criadas e as características do processo de agendamento dos Tipos de Agenda que serão abertas.  
Essas definições podem ser feitas em:  
Agendas  
Atividades  
Motivos  
Status do Agendamento  
Tipo Indicação  
Indicação  
Motivo Exceção  
Estatísticas  
Nesta tela, você poderá visualizar Estatísticas da Agenda de Atendimento por período e profissional.

PastasPasta indicadores 

## **02. PASTA INDICADORES**

Agendamentos Registrados: Exibe a quantidade de todos os agendamentos na Agenda.  
Número de Cancelamentos: Exibe a quantidade de todos os agendamentos cujo Status seja "Cancelado".  
Pacientes Atendidos: Exibe a quantidade de todos os agendamentos cujo Status seja "Atendido";  
Percentual de Ocupação da Agenda: Exibe o Percentual de Ocupação da Agenda realizando o seguinte calculo: AGENDAMENTOS REALIZADOS / TOTAL DE AGENDAMENTOS DISPONIVEIS \* 100;  
Exemplo: Considere uma agenda que possua 10 horários livres e realizo 6 agendamentos nessa mesma agenda. Logo o calculo de percentual de ocupação será: 6 / 10 \* 6 = 60%  
Taxa de Efetivação de Atendimentos: Exibe o Percentual da Efetivação de Atendimentos realizando o seguinte calculo: TOTAL DE AGENDAMENTOS CUJO STATUS SEJA "ATENDIDO" / AGENDAMENTOS REALIZADOS \* 100;  
Exemplo: Continuando o exemplo acima, dos 6 agendamentos realizados 3 foram confirmados como "Atendido". Logo o calculo de efetivação de atendimento será: 3 / 6 \* 100 = 50%

Pasta atividades 

## **03. PASTA ATIVIDADES**

Gráfico de distribuição de Atividades do período: Exibe um gráfico em forma de "pizza", com a utilização de Atividades cadastradas na Agenda;

Pasta convênios 

## **04. PASTA CONVÊNIO**

Gráfico de distribuição de Convênios por período: Exibe um gráfico em forma de "pizza", com a utilização de Convênios informados no momento do agendamento;

Pasta status 

## **05. PASTA STATUS**

Gráfico de distribuição dos Status dos Agendamentos por período: Exibe um gráfico em forma de "pizza", com a utilização de Status informados no Agendamento;

Pasta atividades 

## **06. PASTA ATIVIDADES**

Através desta Pasta, você poderá definir quais Atividades cadastradas, o profissional irá atender / realizar.  
As mesmas podem ter restrições pelos dias da semana, informando uma quantidade máxima ou mínima, e também poderá ter restrições por faixa etária de idade em um período de data informado.

Pasta especialidades

## **07. PASTA ESPECIALIDADES**

Nesta Pasta, você define quais Especialidades o Profissional irá atender.  
Quando selecionado a agenda de um profissional dentro da arvore de agendas o RM deixará como default marcado no registro de agendamento a especialidade selecionada.

Pasta Bloqueios 

## **08. PASTA BLOQUEIOS**

Por esta Pasta, você pode definir bloqueios na Agenda de Atendimento, em um dia específico.

Pasta período especial 

## **09. PASTA PERÍODO ESPECIAL**

Através desta Pasta, será possível definir um dia com horário de atendimento especial.  
Atenção: O Período Especial sobrepõe (tem efeito sobre) o Período Normal Cadastrado na Pasta Período, já o Bloqueio, sobrepõe (tem efeito sobre) o Período Normal e o Período Especial.  
Checagem de Disponibilidade Agenda de Cirurgia  
A Agenda de Cirurgia usa os recursos da Agenda de Atendimento para pesquisar disponibilidade de horários de cirurgiões e bloquear os horários na Agenda de Atendimentos quando a cirurgia é marcada para o profissional em questão.  
Checagem Coberturas  
O cheque de coberturas é "chamado" automaticamente pela Agenda de Atendimentos, validando algumas Condições Contratuais com Convênio, situações de coberturas checadas pelo Faturamento.  
   
Exemplo 1: Agendo uma consulta cuja especialidade seja Cardiologia. Caso essa especialidade não esteja autorizada, em Condições Contratuais com Convênio, a Agenda de Atendimentos irá alertar ao atendente sobre essa restrição.  
Exemplo 2: Agendo uma consulta cuja atividade seja "Consulta Principal". Associado a esta atividade esta o serviço "Consulta em Pronto Socorro". Caso esse serviço esteja como proibido, em Condições Contratuais com Convênio, a Agenda de Atendimentos irá alertar ao atendente sobre essa restrição.  
   
   
No registro de agendamento o campo Código do Beneficiário. Ao lado foi adicionado um botão para verificação da elegibilidade junto ao convênio, através de web service que deve ter a URL cadastrada na condição contratual página "Eletrônico III".

Pasta exames

## **10.   Pasta exames**

Através desta pasta, será possível adicionar os exames que a agenda selecionada pode atender, assim como a restrição por faixa etária se a mesma foi identificada, caso contrário segue a restrição informada no cadastro do exame.

É válido ressaltar que o campo **Qtde Horários (Duração)**define a quantidade de horários que o exame em questão irá ocupar na agenda, bloqueando os horários subsequentes da agenda até atingir o número de horários definidos nesse campo.

Caso um **exame de imagem**seja associado à agenda e a sua duração seja menor ou igual à duração dos horários da agenda e o campo **Qtde Horários (Duração)**esteja preenchido para ocupar mais de um horário na agenda, a informação do  campo **Qtde Horários (Duração)**irá ter prioridade sobre a duração real do exame

Utilizando **um exemplo prático** dentro do RM

Na configuração do exame **RX DE CRANIO SELA TURCA**, esse exame está configurado para ocupar apenas 20 minutos na agenda. 

A agenda da unidade de atendimento **RECEPÇÃO DO CENTRO DIAGNÓSTICO**está configurada para ter horários com duração de 20 em 20 minutos.

Caso fosse realizado um agendamento em um dos horários e o exame **RX DE CRANIO SELA TURCA**fosse associado ao agendamento, a quantidade de horários que seriam ocupados pelo exame seria definida pelo campo **Qtde Horários (Duração).**

Nesse exemplo, esse exame, nessa agenda, **está configurado para ocupar 4 horários** (mesmo que sua duração na prática ocupe o intervalo de tempo de um agendamento, exame = 20 minutos e duração de horário da agenda = 20 minutos.

Sendo assim, ao realizar o agendamento com esse exame, haverá o bloqueio de 4 horários para esse agendamento.

Caso a quantidade de horários ocupada pelo exame seja 1, não haverá bloqueio e o exame estará diretamente associado à duração do agendamento.

Caso o campo **Qtde Horários (Duração)** não esteja preenchido, o cálculo para definir se haverão bloqueios será determinado pela duração padrão da agenda se o horário do exame for menor ou igual à duração da agenda

Caso o **Qtde Horários (Duração)** não esteja preenchido, o  o cálculo para definir se haverão bloqueios será definido pelo tempo que o exame excede a agenda. Exemplo abaixo:

**Exame** configurado para durar 30 minutos sendo que o tempo da agenda é de 20 minutos

**Qtde Horários (Duração)** não esteja preenchido

Como a diferença entre a duração do exame (30 minutos) e da agenda (20 minutos) é 10, para que esse exame seja realizado, seriam necessários 2 horários. Logo haverá bloqueio do próximo horário.

Essa lógica serve para toda duração de exame. Os bloqueios ocorrerão até que os horários sejam suficientes para executar o exame.

Propriedades da agenda (opções) 

## **11. PROPRIEDADES DA AGENDA (OPÇÕES)**

Na Agenda de Atendimentos, temos o botão "Opções" que abre a tela de Propriedades da Agenda, onde podemos configurar algumas opções da mesma. Essa tela é composta pelas Pastas Períodos, Atividades, Especialidades, Bloqueios, Períodos Especiais e Restrições de faixa etária.  
Pasta Períodos:  
Períodos são calendários de atendimento contendo os horários em que o médico irá atender durante a semana. A partir da versão 12.1.2310 não será permitido excluir períodos ou alterar a duração, dia, hora inicio e fim de períodos com agendamentos futuros.  
Fazem parte da Pasta Período:  
Padrões de Agendamento e Duração  
Data Máxima: Determina uma data máxima limite para a realização de agendamentos.  
Antecedência Máxima: Determina em dias, um limite máximo para a realização de agendamentos, a contar do dia atual.  
Minutos de Duração: Determina em minutos, qual será a duração padrão das consultas do médico.  
Observação: Nessa mesma tela ainda temos os botões: Incluir, Editar e Excluir.  
Período por especialidade: Permite cadastrar um período especifico para alguma especialidade especifica.  
Restrições de faixa etária: Permite cadastrar faixas etárias que restringem a idade do paciente que a Agenda em questão irá atender ou não. 

Configuração Personalizada de Períodos da Agenda

## **12.   CONFIGURAÇÃO PERSONALIZADA DE PERÍODOS DA AGENDA (disponível a partir da 12.1.2402)**

Importante!

* Não é possível cadastrar uma agenda para a mesma sala ou o prestador caso existam horários conflitantes. Verifique as agendas cadastradas existentes antes de prosseguir.
* Evite usar o agrupador "Médico" quando a agenda tiver especialidades com durações diferentes no mesmo dia. Utilize o agrupador de especialidade.

Cadastro de período de agenda.

Na Agenda teremos a opção de personalizar os períodos de atendimento da Agenda

Ao clicar para Inserir ou Editar um período, será necessário informar o seguinte campo : Recorrência da Agenda.

**Diária:**  o período de atendimento será de segunda a sexta-feira com opção marcar sábado e domingo

**Semanal:**  será selecionado um dia na semanal para atendimento .

**Mensal:**  será selecionado um dia do mês para atendimento, caso o dia selecionado seja 31 e esse dia não tenha em algum mês, exemplo Novembro vai até o dia 30, no mês de novembro não terá agenda disponível 

**Personalizada:**  Onde ele poderá selecionar ( Semana ou Mês ) e quantas vezes ele vai se repetir exemplo: Mensal repetir a cada 2 meses  e selecionou o dia 15.  Vai atender 15/01, 15/03 e assim sucessivamente.

             

Caso ao inserir um período o campo Ocorrência da Agenda estiver em branco ocorrera o seguinte erro:

## **13.** **Cadastrando o Período**

Ao configurar um período na agenda, é importante que a duração total dos agendamentos se encaixe perfeitamente dentro do intervalo definido.  
Caso a duração da agenda não se encaixe exatamente no intervalo do período, o sistema exibirá uma mensagem de erro, sugerindo um novo horário final ajustado para que não haja sobra de tempo.

OpçãoOpção Semanal

## **14.   OPÇÃO SEMANAL**

Ao selecionar opção semanal na recorrência da agenda, o mesmo permitira escolher apenas um dia da semana.

Não permitindo adicionar mais dias da semana diferente do dia escolhido.

Assim a grade de horário é montada de acordo com a recorrência escolhida, respeitando os horários informados.

Oção mensal

## **15.   OPÇÃO MENSAL**

Ao selecionar opção mensal você poderá selecionar o dia do mês que ocorrerá a recorrência da agenda, o mesmo permitira escolher apenas um dia do mês.

Com essa opção seja  selecionada, você não terá acesso aos dias da semana, você poderá escolher os dias de 1 a 31

Observação caso você escolha o dia 31 a recorrência ocorrera apenas nos meses que tem dia 31 nos meses que não tem exemplo o de novembro, não terá agenda,

No meu exemplo o dia escolhido foi o dia 25

Caso queria agendar uma recorrência mensal e uma recorrência diária em um período onde os dois tenham conflito não terá problema se  as especialidades forem diferentes

conforme as imagens abaixo.

Recorrência Diária para a especialidade Consultas

E a recorrência mensal com a especialidade Clinica Médica

No dia 20 de fevereiro tenho uma agenda com bloqueio ate o médio dia. Ja no próximo horário ela esta livre

Por isso vemos aqui o dia 20 de fevereiro como livre

Agora uma agenda com recorrência mensal para duas especialidades diferentes e dias diferentes

Dia 15 de Fevereiro a agenda esta bloqueada o dia todo, por isso esta amarelo.

Personalizada

## **16.   Personalizada**

Para inserir uma agenda personalizada você pode escolher Semana ou Mês.

O funcionamento do Personalizado por semana, é bastante parecido com a opção Semanal, mas você poderá escolher mais de um dia da semana

conforme exemplo abaixo

Como você pode notar a agenda esta semanal com a recorrência de a cata de 3 semanas

Personalizada repetir a cada 4 meses

Agendamento em Grupo

Segue abaixo um passo-a-passo de como criar um agendamento em grupo e os atendimentos para os pacientes deste agendamento.

Na tela do compromisso marque o Checkbox **Grupo,** preencha os dados e clique em salvar

Depois selecione a aba Grupo e adicione os pacientes

**Obs:** Foram adicionados três pacientes.

Para exibir os pacientes do grupo, clique no botão identificado na imagem abaixo

Para criar o atendimento, selecione o paciente e clique no botão **Atendimento Externo**

Informe os dados necessários para a criação do atendimento e clique no botão Ok

Observe na imagem abaixo com fica após criar dois atendimentos neste grupo que foi gerado para três pacientes

## **Assista as pequenas guias!**
