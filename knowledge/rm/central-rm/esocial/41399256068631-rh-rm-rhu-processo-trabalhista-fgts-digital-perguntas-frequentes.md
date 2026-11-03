---
article_id: 41399256068631
category: eSocial
content_hash: 681625301e8238ff2c0adfb4e9343cb01877d7e63735b5928132fba61e379c65
fetched_at: '2026-06-28T22:47:15.257997+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - Processo Trabalhista - FGTS Digital: Perguntas Frequentes'
type: support-article
updated_at: '2026-06-22T14:54:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41399256068631-RH-RM-RHU-Processo-Trabalhista-FGTS-Digital-Perguntas-Frequentes
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41399262211991) Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Quais são as principais dúvidas referente ao uso do FGTS Digital em Processos Trabalhistas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2506** e **superiores**.  
  
**Solução**  
Esta documentação reúne as principais dúvidas e orientações disponibilizados pelo Governo sobre o uso do FGTS Digital decorrente de Processo Trabalhista, com o objetivo de oferecer respostas rápidas, esclarecer comportamentos do sistema e apoiar na resolução de situações comuns do dia a dia.

#### **PERGUNTAS FREQUENTES SOBRE PROCESSOS TRABALHISTAS**

**02.19 (04/07/2025, atualizado em 07/05/2026) - Enviei um evento de Processo Trabalhista (S-2500) no eSocial, informando todas as bases de cálculo de FGTS para todos os meses reclamados. Apesar disso, as competências desse trabalhador não estão aparecendo como "Regular" no FGTS Digital.**

Até a competência de apuração 04/2026, as empresas realizavam o recolhimento de FGTS com origem em processos trabalhistas via guias SEFIP 650/660. Essas guias ainda não são internalizadas no ambiente do FGTS Digital e não impactam na visualização de regularidade no módulo de Consultas do Empregador. Para competências até essa data não será exibido o status de “Irregular” para competências sem informações de remunerações.

A partir da competência 05/2026, quando se inicia o recolhimento de FGTS com origem em reclamatórias pelo FGTS Digital, o sistema passou a fazer a crítica de regularidade das competências de referência tendo como origem todos os eventos de remuneração do eSocial, inclusive o evento S-2500 (Processo Trabalhista). Portanto, débitos confessados no evento S-2500 precisam ser quitados para que as respectivas competências apareçam como “Regular” nessa consulta. Sobre valores pagos com recursos de depósito judicial/recursal, veja a pergunta frequente nº 03.28.

**02.20 (07/05/2026) Como os valores de base de cálculo declarados no evento S-2500 irão aparecer no FGTS Digital?**

O empregador terá 3 campos no evento S-2500 do eSocial para informar as bases de FGTS para cada competência de referência (período do processo trabalhista):

a) Campo [vrBcFGTSProcTrab] - Valor da base de cálculo de FGTS ainda não declarada em SEFIP ou no eSocial, inclusive de verba reconhecida no processo trabalhista.

b) Campo [vrBcFGTSSefip] - Valor da base de cálculo de FGTS declarada apenas em SEFIP (não informada no eSocial) e ainda não recolhida.

c) Campo [vrBcFGTSDecAnt] - Valor da base de cálculo de FGTS declarada anteriormente no eSocial e ainda não recolhida.

Os campos [vrBcFGTSSefip] e [vrBcFGTSDecAnt] são opcionais (facultativos) e foram criados para facilitar o recolhimento em atraso de todo o FGTS devido ao trabalhador e que deveria ter sido recolhido originalmente via GFIP. Com o FGTS Digital, o empregador poderá gerar apenas uma guia para regularizar todo o FGTS do trabalhador. Cabe destacar que as empresas poderão incluir valores nesses campos apenas até a competência de referência 02/2024, de períodos anteriores ao início do FGTS Digital. Bases de cálculo de FGTS a partir de 03/2024 que não foram reconhecidas no processo trabalhista, mas que ainda estão em aberto, devem ser declaradas nos eventos normais de remuneração do eSocial (S-1200).

Caso, em uma mesma competência de referência, o empregador informe bases de FGTS em mais de um desses campos, o FGTS Digital irá exibi-los juntos (somados) por tipo valor na tela de Guia Parametrizada e nos relatórios das guias geradas. Foram criados os seguintes tipos valores para esse controle:

71 - FGTS Processo Trabalhista – Mensal 8%

72 - FGTS Processo Trabalhista – Mensal 2%

73 - FGTS Processo Trabalhista - Indenização compensatória do empregado doméstico

Para débitos de indenização compensatória (multa rescisória do FGTS), o empregador deverá utilizar a ferramenta de Gestão de Histórico de Remunerações de Processo Trabalhista e confirmar os valores. Será gerado o tipo valor 991 (FGTS indenização compensatória - Processo Trabalhista), que será compartilhado com o módulo de Gestão de Guias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41399256044311)

**02.21 (07/05/2026) Em decisão judicial, acordo judicial homologado ou termo de conciliação firmado perante Comissão de Conciliação Prévia (CCP) ou Núcleo Intersindical de Conciliação Trabalhista (NINTER), há previsão de depósito de FGTS, mas sem detalhamento da individualização por competência (mês). Como devo declarar essas informações no evento S-2500 do eSocial?**

Nos termos do art. 17-A da Lei nº 8.036/1990, permanece obrigatória a escrituração das informações de FGTS por meio do eSocial, inclusive nos casos decorrentes de processo trabalhista. Dessa forma, as bases de cálculo reconhecidas em decisão judicial ou acordo devem ser declaradas de forma individualizada por competência, observando-se a estrutura dos eventos do eSocial e as regras operacionais do FGTS Digital. A obrigação de detalhamento das competências não é afastada pela ausência dessa informação expressa na decisão judicial ou acordo, cabendo ao empregador promover a correta identificação e escrituração dos valores devidos.

Todo o depósito de FGTS deve ser realizado de forma individualizada, com as bases de cálculo detalhadas por competência. O evento S-2500 foi estruturado nesse sentido, obrigando o empregador a informar separadamente as bases de cálculo de FGTS de cada competência reclamada no processo ou acordo trabalhista.

Se o detalhamento dos meses reclamados não constar na decisão ou acordo, compete à empresa agir de acordo com o que prevê o artigo 18, § 7º, da portaria 240/2024, procedendo ao rateio dos valores nas competências que foram objeto da ação.  
  
**03.24 (12/03/2024, atualizado em 07/05/2026) – Tenho uma sentença anterior a 01/05/2026. Como devo fazer a declaração e o recolhimento de FGTS da Reclamatória Trabalhista?  E como agir com as sentenças a partir de 01/05/2026?**

No caso de recolhimento de FGTS mensal devido a partir da competência de apuração março/2024 até abril/2026, o empregador deve recolher por meio do FGTS Digital todos os valores já declarados ao eSocial no evento S-1200/S-2299/S-2399, e abster-se de transmitir o evento S-2500 a fim de evitar duplicidade de cobrança.

Apenas os valores ainda não declarados ao eSocial e reconhecidos em processo trabalhista com data de sentença até 30/04/2026, devidos a qualquer tempo, devem ser recolhidos via guias SEFIP 650/660, pois o evento S-2500 do eSocial não foi compartilhado com o FGTS Digital durante esse período. Ainda para esse período, deve ser observado o disposto na Nota Orientativa FGTS Digital nº 08/2025, inclusive quanto ao tratamento da indenização compensatória.

Para os processos e acordos trabalhistas com data de sentença a partir de 01/05/2026, todo o recolhimento de FGTS relacionado deve ser realizado pelo FGTS Digital, por meio do envio das bases de cálculo do FGTS no evento S-2500 do eSocial e da funcionalidade de Gestão do Histórico de Remunerações de Processo Trabalhista do FGTS Digital.

Veja outras orientações importantes sobre essa dúvida:

* **Data da sentença até 30/04/2026 com recolhimento de multa rescisória do FGTS para empregado com registro prévio de admissão no eSocial cujo desligamento é a partir de 01/03/2024**

Para trabalhadores com registro prévio de admissão no eSocial (eventos S-2190/S-2200/S-2300/S-2399), se houver uma rescisão por determinação judicial com data de desligamento a partir de 01/03/2024, o empregador deve prestar essa informação no evento S-2299/S-2399 do eSocial, para informar a data de término na CTPS Digital, além de prestar as demais informações no evento S-2500 (Processo Trabalhista). Como não existe campo da multa trabalhista no evento S-2500, a declaração da base de cálculo sobre essa verba, se devida nos termos da legislação, deve ser realizada via FGTS Digital, pois não é possível recolher a multa do FGTS em guia SEFIP 650/660. O empregador conseguirá informar diretamente no FGTS Digital o histórico de remunerações ou o valor da base para fins rescisórios para o cálculo da multa rescisória.

* **Processo com reconhecimento de vínculo e data da sentença até 30/04/2026 com recolhimento de multa rescisória do FGTS para desligamentos a partir de 01/03/2024**

Até que ocorra a internalização dos eventos de processo trabalhista (S-2500) pelo FGTS Digital, para trabalhadores com processo trabalhista sem registro prévio no eSocial e com reconhecimento judicial do vínculo e desligamento a partir de 01/03/2024, caso exista definição judicial para recolhimento da multa do FGTS, o empregador deverá enviar previamente o evento de admissão S-2200 e o evento de desligamento S-2299, para que o FGTS Digital seja sensibilizado e permita o recolhimento da multa por este sistema. Continua a obrigatoriedade de envio do evento S-2500 com o campo "indContr" = "S" e com as verbas reconhecidas dentro do processo trabalhista. O empregador conseguirá informar diretamente no FGTS Digital o histórico de remunerações ou o valor da base para fins rescisórios para o cálculo da multa rescisória.

 O empregador deve enviar, também, os eventos S-1200 com remuneração zerada, relativos à cada uma das competências do vínculo de emprego, para que o FGTS Digital não aponte ausência de remuneração nessas competências. Para que seja possível o envio de um S-1200 com remuneração zerada, é necessário que seja lançada uma rubrica informativa com valor R$ 0,01 e outra rubrica dedutora com o mesmo valor. Essas rubricas devem ser parametrizadas com o código de incidência [00] para FGTS e contribuição previdenciária e [9] para Imposto de renda. Sobre o envio de eventos S-1200, verifique a [Pergunta Frequente 02.19](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes/perguntas-frequentes/#FAQ-0219) sobre o tema.

* **Data da sentença a partir de 01/05/2026 e recolhimento de multa rescisória do FGTS para desligamentos antes de 1º/03/2024 com registro prévio de admissão no eSocial**

O empregador deve enviar, no evento S-2500 do eSocial, as bases de cálculo do FGTS reconhecidas no Processo Trabalhista e poderá declarar bases de FGTS de competências até 02/2024 anteriormente declaradas em SEFIP ou no eSocial para fins de recolhimento de FGTS. Posteriormente, deve declarar a indenização compensatória sobre essas bases na funcionalidade de Gestão do Histórico de Remunerações de Processo Trabalhista no FGTS Digital. Por meio da funcionalidade Gestão de Guias, o empregador emite a guia para recolhimento.

Já em relação à indenização compensatória (multa rescisória) devida sobre as bases de cálculo de FGTS não declaradas no evento S-2500, o empregador deve utilizar os sistemas da CAIXA para fins de recolhimento.

* **Data da sentença a partir de 01/05/2026 e recolhimento de multa rescisória do FGTS para desligamentos a partir de 1º/03/2024 com registro prévio de admissão no eSocial**

O empregador deve enviar, no evento S-2500 do eSocial, as bases de cálculo do FGTS reconhecidas no Processo Trabalhista e poderá declarar bases de FGTS de competências até 02/2024 anteriormente declaradas em SEFIP ou no eSocial para fins de recolhimento de FGTS. Posteriormente, deve declarar a indenização compensatória sobre essas bases na funcionalidade de Gestão do Histórico de Remunerações de Processo Trabalhista no FGTS Digital. Por meio da funcionalidade Gestão de Guias, o empregador emite a guia para recolhimento.

Já em relação à indenização compensatória (multa rescisória) devida sobre as bases de cálculo de FGTS não declaradas no evento S-2500, o empregador deve utilizar a funcionalidade Gestão de Histórico de Remunerações para declarar a base de cálculo para fins rescisórios.

Ou seja, no eSocial, o empregador declara as bases de cálculo reconhecidas em processo trabalhista de forma separada. No FGTS Digital, o empregador também declara a base da indenização compensatória sobre as bases de cálculo do evento de processo trabalhista (S-2500) na funcionalidade específica. Sobre este tema, veja a pergunta frequente 04.21.

* **Data da sentença a partir de 01/05/2026 e recolhimento de multa rescisória do FGTS para desligamentos com reconhecimento de vínculo**

O empregador deve enviar, no evento S-2500 do eSocial, as bases de cálculo do FGTS reconhecidas no Processo Trabalhista. Posteriormente, deve declarar a indenização compensatória sobre essas bases na funcionalidade de Gestão do Histórico de Remunerações de Processo Trabalhista no FGTS Digital. Por meio da funcionalidade Gestão de Guias, o empregador emite a guia para recolhimento. Sobre este tema, veja a pergunta frequente 04.21.

**03.28 (07/05/2026) Enviei um processo trabalhista com as bases de cálculo do FGTS. Agora, todos esses débitos aparecem como devidos no FGTS Digital, mas parte desses valores de FGTS foram pagos via depósito judicial/recursal. O que devo fazer?**

Com relação ao FGTS, devem ser informadas TODAS as bases de cálculo reconhecidas no processo trabalhista e ainda não declaradas no SEFIP ou no eSocial,  independentemente do período a que se refiram, de conformidade com o art.18, §6º, I da Portaria MTE nº 240/2024, inclusive as bases relativas aos valores eventualmente quitados mediante guia emitida diretamente pela Vara do Trabalho.

Os valores já eventualmente quitados com depósitos judiciais, mediante o ingresso desses valores na conta vinculada do FGTS, podem ser abatidos no momento de geração da guia no FGTS Digital, a fim de evitar o pagamento em duplicidade, desde que haja comprovação inequívoca desses pagamentos por meio de determinação judicial. A operacionalização do reconhecimento desses pagamentos realizados por determinação de alvará judicial observará as orientações a serem disponibilizadas no âmbito do FGTS Digital. O status desses valores como “em débito” no FGTS Digital, até que ocorra a internalização desses recolhimentos realizados diretamente em razão de cumprimento de alvará judicial, não acarretará o lançamento desses valores por parte do Ministério do Trabalho e Emprego e não impactará a regularidade perante o FGTS Digital (CRF).

**03.29 (07/05/2026) Sou empregador doméstico e fui condenado a recolher FGTS em um processo trabalhista, mas os valores que confessei no evento S-2500 não estão parecendo no FGTS Digital.**

Os sistemas da Caixa ainda estão sendo preparados para receber valores de FGTS decorrentes de processos trabalhistas de domésticos via FGTS Digital. Enquanto isso não ocorrer, os empregadores desta categoria deverão seguir as orientações das [perguntas frequentes nº 25.01 e 25.02 do eSocial](https://www.gov.br/esocial/pt-br/empregador-domestico/perguntas-frequentes/perguntas-frequentes/#25--processos-trabalhistas), que orientam sobre a necessidade de emissão de DAE para recolher o FGTS sobre as remunerações do empregado. Para isso, o empregador deverá acessar e reabrir cada uma das folhas de pagamento do período reclamado, clicar no nome do trabalhador, editar manualmente a remuneração e incluir a rubrica “Base de Cálculo do FGTS – Reclamatória Trabalhista” com o valor estabelecido na ação, além de outros procedimentos detalhados no [link acima](https://www.gov.br/esocial/pt-br/empregador-domestico/perguntas-frequentes/perguntas-frequentes/#25--processos-trabalhistas).

**03.30 (07/05/2026) Na decisão judicial está previsto o pagamento em 4 parcelas ao trabalhador das verbas salariais reconhecidas no processo. Como fica o recolhimento do FGTS sobre essas parcelas?**

A previsão na sentença ou acordo de pagamento parcelado de verbas não se aplica ao FGTS. O fato gerador do FGTS será cada competência de referência informada pelo empregador no evento S-2500 e terá acréscimos de encargos desde o vencimento original dessa competência.

Os valores de FGTS com origem em processo trabalhista serão considerados “Irregulares” se não forem quitados até o dia 20 ao mês seguinte da competência de apuração, que corresponde à data da sentença ou acordo (campos dtSent ou dtCCP do evento S-2500), com possível impacto em Parcelamentos, na emissão da CRF e encaminhamento para fiscalização.

**04.20 (07/05/2026) Como será calculada a multa rescisória do FGTS (indenização compensatória) nos casos de processos trabalhistas?**

Nos casos de processos trabalhistas, as bases de cálculo de FGTS mensal são informadas no próprio evento S-2500 do eSocial. No entanto, os valores de indenização compensatória (multa rescisória do FGTS) deverão ser declarados diretamente no FGTS Digital.

Dentro do módulo de REMUNERAÇÕES PARA FINS RESCISÓRIOS, foi criada a funcionalidade GESTÃO DE HISTÓRICO DE REMUNERAÇÕES DE PROCESSO TRABALHISTA. Serão listados apenas trabalhadores com motivos de desligamento, categoria e regime trabalhista com previsão legal de pagamento de indenização compensatória.

Trata-se de uma funcionalidade adicional, cujo campo da multa rescisória tem seu cálculo gerado a partir dos valores do processo trabalhista declarados no evento S-2500 – inclusive os informados nos campos opcionais/facultativos relativos a competências anteriores a 03/24 – e não se confunde com o cálculo da indenização compensatória ordinária, que continuará existindo na funcionalidade principal de Gestão de Histórico de Remunerações. Dessa forma, o empregador deve ter atenção na declaração desta tela, para não duplicar bases de cálculo e, consequentemente, aumentar o valor da multa rescisória devida ao trabalhador.

**04.21 (07/05/2026) Tenho um processo trabalhista que determinou o pagamento de multa rescisória do FGTS (indenização compensatória) maior do que o valor calculado automaticamente pelo FGTS Digital. Como faço para pagar a diferença?**

O FGTS Digital disponibilizou a funcionalidade de GESTÃO DE HISTÓRICO DE REMUNERAÇÕES DE PROCESSO TRABALHISTA apenas para calcular a indenização compensatória (40% ou 20%) sobre bases de cálculo mensais informadas no evento S-2500.

Caso o processo ou acordo trabalhista tenha previsão de um pagamento de multa rescisória em valor superior ao calculado pelo sistema, o empregador deverá utilizar a funcionalidade ordinária (normal) de cálculo da indenização compensatória (funcionalidade “Gestão de Histórico de Remunerações”) e editar o campo “Valor base para fins rescisórios”, de forma que a nova base informada corresponda ao valor que falta pagar da multa.

Se o vínculo foi criado no próprio evento S-2500 (Processo Trabalhista), será necessário que a empresa envie um evento S-2200 (Admissão) com o campo {matAnotJud} preenchido e enviar um evento S-2299 (Desligamento) com o motivo correto de rescisão. Esse procedimento irá criar um cálculo de indenização compensatória para esse vínculo no FGTS Digital. Então, a empresa irá informar a base de cálculo na funcionalidade “Gestão de Histórico de Remunerações” e seguir o mesmo procedimento.

O empregador deve ter especial atenção nesse procedimento para não duplicar bases de cálculo e criar um débito maior que o devido. Se a empresa já utilizou essa ferramenta para pagar um valor de indenização compensatória que não constava no processo trabalhista, deverá acrescentar a nova base de cálculo ao valor que já constava anteriormente. O FGTS Digital não realiza consolidação automática entre essas duas bases, cabendo ao empregador garantir a coerência entre os valores informados.

Veja alguns exemplos:

**Exemplo 1** – com S-2299 prévio no eSocial

* Motivo da demissão: sem justa causa (multa de 40%)
* Valor já pago de indenização compensatória antes do processo trabalhista: R$ 4.000,00 (base de cálculo de R$ 10.000,000)
* Valor de FGTS mensal devido sobre horas extras e comissões do período de 01/2024 até 10/2024, conforme decisão no processo trabalhista: R$ 400,00 para cada mês (base de cálculo de R$ 5.000,00 com alíquota de 8%). Total mensal devido de FGTS: R$ 4.000,00
* Novo valor de indenização compensatória a pagar, fixada após decisão judicial: R$ 2.000,00 (base de cálculo de R$ 5.000,00)
* Valor corretamente calculado pela nova ferramenta de “Gestão de Histórico de Remunerações de Processo Trabalhista”: R$ 1.620,00 (calculado a partir das bases de cálculo mensais informadas no evento S-2500 e atualizadas monetariamente)
* Diferença de indenização compensatória a recolher: R$ 380,00
* Procedimento:
* Confirmar o cálculo de R$ 1.620,00 na funcionalidade de “Gestão de Histórico de Remunerações de Processo Trabalhista”, referente à multa calculada automaticamente com base nos valores mensais declarados no evento S-2500;
* Acessar a funcionalidade de “Gestão de Histórico de Remunerações”;
* Editar o cálculo da indenização compensatória normal desse trabalhador;
* Editar o campo “Valor base para fins rescisórios” de R$ 10.000,00 para R$ 10.950,00), que irá gerar uma multa a pagar de R$ 4.380,00
* Confirmar o cálculo;
* Acessar funcionalidade de Gestão de Guias e pagar os valores de FGTS. Caso a multa original de R$ 4.000,00 já tenha sido paga, esses valores serão automaticamente abatidos no saldo devedor e a empresa irá pagar o valor de R$ 380,00 referente à multa, além de outros valores de FGTS em aberto do trabalhador.

**Exemplo 2** – apenas evento S-2500 no eSocial

* Motivo da demissão: sem justa causa (multa de 40%)
* Valor de FGTS mensal devido sobre descanso semanal remunerado do período de 01/2025 até 05/2025, conforme decisão no processo trabalhista: R$ 200,00 para cada mês (base de cálculo de R$ 2.500,00 com alíquota de 8%). Total mensal devido de FGTS: R$ 1.000,00
* Valor de indenização compensatória a pagar após decisão no processo trabalhista: R$ 2.000,00 (base de cálculo de R$ 5.000,00)
* Valor calculado pela nova ferramenta de “Gestão de Histórico de Remunerações de Processo Trabalhista”: R$ 410,00 (calculado sobre as bases mensais informadas no evento S-2500 e atualizadas monetariamente)
* Diferença de indenização compensatória a recolher: R$ 1.590,00
* Procedimento:
* Confirmar o cálculo de R$ 410,00 na funcionalidade de “Gestão de Histórico de Remunerações de Processo Trabalhista”, referente à multa calculada automaticamente com base nos valores mensais declarados no evento S-2500;
* Enviar pelo eSocial os eventos S-2200 e S-2299 desse trabalhador;
* Acessar a funcionalidade de “Gestão de Histórico de Remunerações” para esse novo vínculo criado;
* Editar o cálculo da indenização compensatória normal desse trabalhador;
* Editar o campo “Valor base para fins rescisórios” para R$ 3.975,00, que irá gerar uma multa a pagar de R$ 1.590,00;
* Confirmar o cálculo;
* Acessar funcionalidade de Gestão de Guias e pagar os valores de FGTS.

**Saiba Mais**  
Para maiores informações, acesse:

- [Manual de Orientação do FGTS DIGITAL](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-de-orientacao-do-fgts-digital-versao-1-60-05-05-2026.pdf)

- [Recolhimentos de FGTS em processos trabalhistas serão efetuados via FGTS Digital a partir de maio/2026](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/comunicados/recolhimentos-de-fgts-em-processos-trabalhistas-serao-efetuados-via-fgts-digital-a-partir-de-maio-2026)

- [Em produção: recolhimentos de FGTS em processos trabalhistas devem ser efetuados via FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/comunicados/em-producao-recolhimentos-de-fgts-em-processos-trabalhistas-devem-ser-efetuados-via-fgts-digital)

- [FGTS Digital: Perguntas Frequentes](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes)

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
