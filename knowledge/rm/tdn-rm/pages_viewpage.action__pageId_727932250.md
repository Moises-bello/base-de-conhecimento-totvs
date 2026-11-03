---
content_hash: f38c1c896021fc7e54d42cebc882758e7b9be9fd8254a87bdf3c95087a88215c
fetched_at: '2026-06-29T00:11:27.600471+00:00'
page_id: '727932250'
product: rm
source: tdn-rm
title: Condições Contratuais - Parâmetros 2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=727932250
version: 12
---

Informações

Nessa aba temos diversos parâmetros que definem o comportamento dos lançamentos e impressos. Essas configurações são realizadas através da tela de Condições Contratuais com Convênio.

## **01. Exige Faturamento por Competência**

Se ativo, durante o processo de **Faturamento para Convênios** (Faturamento > Faturamento para Convênios), o campo **Competência** será de preenchimento obrigatório para execução do processo.

## **02. Número máximo de dias p/ Geração de Recurso após registro das Glosas**

Se preenchido o sistema passa a validar os dias para geração do recurso.

## **03. Número de dias de antecedência ao término do prazo p/ Geração do Alerta**

Gera um mensagem de alerta na rotina de Processo de Mensagens para as parciais que estão no controle de glosa pendentes para geração do recurso, informado no item 2.

Exemplo: Se o item 2 configurado para 90 dias, e nesse parâmetro 60 dias, quando o controle de glosa estiver dentro dos 30 dias finais, serão geradas mensagens de alerta para cada dia em que a Parcial estiver pendente de recurso.

## **04. Utiliza 4 casas decimais para valores de itens lançados na conta**

Informação

Esse parâmetro só é habilitado para convênio IPASGO.

Informa se utiliza 4 casas decimais nos itens lançados na Parcial. 

## **05. Fatura conta de Pacientes Internados**

Indica se contas dos paciente serão faturados.

## **06. Arredonda lançamentos com fator hora para cima**

Se habilitado, arredonda os lançamentos do fator hora.

## **07. Arredonda valor unitário de MAT/MED**

Se habilitado, os preços dos materiais e medicamentos serão arredondados utilizando as regras de arredondamento da norma ABNT NBR 5891.

## **08. Exige Laudo impresso ao encerrar a conta**

Será obrigatório a impressão do Laudo, conforme uma das opções escolhida.

## **09. Honorários somente em nome do Prestador Principal**

Se ativo, só será possível informar o Prestador nos lançamentos nos itens da Parcial o Prestador Principal informado no Registro do Atendimento.

## **10. Adicional Data e Hora Extra**

Se um Honorário lançado para equipe, define como se adicional de hora extra será aplicado aos médicos e instrumentadores.

## **11. Cálculo para diferença de honorário para gastos particulares**

Se preenchido, define qual tabela deverá ser precificado o item ao transferir o honorário para gastos particular.

## **12. Fator de acomodação enfermaria p/ cálculo de diferença de honorário**

Ao realizar a troca de categoria para enfermaria, define qual fator de acomodação será utilizado.

## **13. Prioriza fator de acomodação do plano para paciente interno**

Se habilitado, se utilizado um plano, o mesmo será priorizado em relação ao fator do convênio durante o atendimento do paciente interno.

## **14. Cobrança de Atendimentos seriados**

Defina a forma que serão cobrados os atendimentos realizados através das sessões, podendo ser um para atendimento para cada sessão ou um único atendimento para todas as sessões.

## **15. Acumular Quantidade e Valor**

Atenção!

Esse parâmetro, anteriormente exclusivo do relatório Delphi foi descontinuado na versão 12.1.2406, junto com a descontinuação do RM Saúde Delphi.

Define quais grupos de gastos serão agrupados ou não durante a impressão do relatório de Conta Médica Hospitalar. Se algum grupo de gasto preenchido, o mesmo será priorizado para o mesmo parâmetro disponível nos Parâmetros Gerais.

## **16. Informar especialidade do Médico Executante**

Atenção!

Esse parâmetro, anteriormente exclusivo do relatório Delphi foi descontinuado na versão 12.1.2406, junto com a descontinuação do RM Saúde Delphi.

Se habilitado, será impressa a especialidade médica do médico executante no relatório de Conta Médica Hospitalar.

## **17. Imprimir CRM do Médico Executante**

Atenção!

Esse parâmetro, anteriormente exclusivo do relatório Delphi foi descontinuado na versão 12.1.2406, junto com a descontinuação do RM Saúde Delphi.

Se habilitado, será impressa o CRM do medico executante no relatório de Conta Médica Hospitalar.

## **18. Imprimir Fabricante na Conta**

Atenção!

Esse parâmetro, anteriormente exclusivo do relatório Delphi foi descontinuado na versão 12.1.2406, junto com a descontinuação do RM Saúde Delphi.

Se habilitado, será impressa o Fabricante do MATMED no relatório de Conta Médica Hospitalar.

## **19. Imprimir dados do paciente em todas as páginas**

Atenção!

Esse parâmetro, anteriormente exclusivo do relatório Delphi foi descontinuado na versão 12.1.2406, junto com a descontinuação do RM Saúde Delphi.

Se habilitado, será impressa em todas as páginas os dados do paciente no relatório de Conta Médica Hospitalar.

## **20. Imprimir Data/Hora paciente externo**

Atenção!

Esse parâmetro, anteriormente exclusivo do relatório Delphi foi descontinuado na versão 12.1.2406, junto com a descontinuação do RM Saúde Delphi.

Se habilitado, será impresso a data e hora do paciente externo no relatório de Conta Médica Hospitalar.

## **21. Imprimir descrição do Feriado**

Atenção!

Esse parâmetro, anteriormente exclusivo do relatório Delphi foi descontinuado na versão 12.1.2406, junto com a descontinuação do RM Saúde Delphi.

Se habilitado, será impressa descrição do feriado no relatório de Conta Médica Hospitalar.

## **22. Não imprime no relatório itens zerados na conta.**

Atenção!

Esse parâmetro, anteriormente exclusivo do relatório Delphi foi descontinuado na versão 12.1.2406, junto com a descontinuação do RM Saúde Delphi.

Se habilitado, não serão impressos os itens zerados no relatório de Conta Médica Hospitalar.

## **23. Tipo de Relatório**

Informa se irá utilizar relatórios do Gerador Antigo criados na MDI Antiga (Delphi) ou do Gerador Novo na nova MDI (DOTNET) nas opções 24 e 25 dos relatórios abaixo.

Atenção

Esse parâmetro foi descontinuado na versão 12.1.2310 junto com a descontinuidade do Gerador de Relatórios Delphi. Caso tenha algum relatório do gerador antigo, utilizar a ferramenta "Aceleração de Migração de Relatórios Delphi para .NET", para mais informações acessar nossa [FAQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008951631-Cross-Segmentos-Backoffice-RM-BI-Acelerador-de-migra%C3%A7%C3%A3o-de-relat%C3%B3rios-Delphi-para-NET-Reports).

## **24. Impressão de Conta Médica Hospitalar**

Informa qual relatório do gerador deverá ser utilizado na impressão do relatório de Conta Médica Hospitalar.

O produto disponibiliza o relatório padrão **SAUREL0036 Conta de Serviços Médicos Hospitalares** e deve ser instalado através da ferramenta [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento).

Informações

Caso o cliente deseja customizar o relatório, deverá ser feita um cópia do relatório padrão e em seguida alterar a cópia utilizando a ferramenta RM Reports.

## **25. Impressão de Relatório Recurso de Glosa**

Informa qual relatório do gerador deverá ser utilizado na impressão do relatório de Recurso de Glosa

O produto disponibiliza o relatório padrão **SAUREL0134 Relatório Recurso de Glosa** e deve ser instalado através da ferramenta [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento).

Informações

Caso o cliente deseja customizar o relatório, deverá ser feita um cópia do relatório padrão e em seguida alterar a cópia utilizando a ferramenta RM Reports.

## **26. Impressão de Extrato de Débitos**

Informa qual relatório do gerador deverá ser utilizado na impressão do relatório de Extrato de Débitos

O produto disponibiliza o relatório padrão **SAUREL0037 Extrato de Conta Hospitalar**  e deve ser instalado através da ferramenta [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento).

Informações

Caso o cliente deseja customizar o relatório, deverá ser feita um cópia do relatório padrão e em seguida alterar a cópia utilizando a ferramenta RM Reports.

## **27. Aplicar Valor de CH Não Credenciado**

Se habilitado, irá aplicar o valor do CH para os médicos não credenciados ao convênios. E possível controlar a cobrança dos pacientes Internos ou Externos.

## **28. Utiliza fator de multiplicação diferenciado para exames**

Se habilitado, irá aplicar o fator de multiplicação informado no item 28 para todos os exames lançados neste contrato.

## **29. Fator de multiplicação para exames**

Se o item 27 habilitado, deverá ser informado o valor do fator de multiplicação que será utilizado para todos os exames lançados neste contrato.
