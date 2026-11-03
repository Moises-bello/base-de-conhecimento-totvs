---
content_hash: 0770649f615b460f8871feafb1b4dcfbb12c602c718682d1f8be508ca1513099
fetched_at: '2026-06-29T00:10:52.155905+00:00'
page_id: '570365112'
product: rm
source: tdn-rm
title: Execução simultânea da escrituração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570365112
version: 16
---

O objetivo do processo de escrituração é criar Lançamentos Fiscais referente as movimentações registradas no módulo de Faturamento. Devido as movimentações não possuírem todas as características fiscais necessárias para cumprir as obrigações legais de cada empresa, este processo se torna essencial no Módulo Fiscal que possui diversas regras e cálculos.

## Comportamento do processo de Escrituração

A escrituração de Movimentos para Lançamentos Fiscais não é um processo simples, podendo gerar um grande consumo de recursos de hardware durante a sua execução de acordo com o tamanho do lote a ser escriturado. Logo, espera-se que o processo seja executado em dias e horários estratégicos de forma que não ocorra impactos na operação díarias. Entretando sabemos que em determinadas situação a escrituração precisa ser realizada de forma imediata.

A partir da versão 12.1.28,  o processo se auto organiza e se divide em várias execuções simultâneas gerando um ganho significativo de performance e consequentemente diminuindo o tempo de processamento para lotes de escrituração que possuem muitos movimentos . Para saber mais como funciona o Fracionamento de Jobs, consulte o [Link Documentação Fracionamento de Jobs](https://tdn.totvs.com/pages/viewpage.action?pageId=547231277)

## Lançamentos Duplicados

A escrituração é processada em memoria durante um longo período e somente quando o processo está próximo do fim os dados são persistidos no banco de dados. Este comportamento é necessário para a correta criação das Situações Tributárias presentes em cada Lançamento. Se durante a execução do processo de escrituração, o mesmo processo for executado novamente a partir de outra estação de trabalho, ao fim da operação Lançamentos Fiscais podem ser duplicados. Neste cenário será necessário estornar o lote escriturado e repetir o processo com apenas uma execução.

## Como evitar Lançamentos duplicados?

A melhor forma de evitar a duplicidade de Lançamentos é realizar o Agendamento de Job para execução da Escrituração. Para isso a TOTVS disponibilizou algumas melhorias importantes no produto:

1º A partir da versão 12.1.28 foi liberado o agendamento de Job para os lotes de escrituração. Desta forma o processo não precisa ser executado manualmente e pode ser agendado para horários de menor demanda do servidor\hardware, contudo ainda é necessário a criação dos lotes para definir os filtros de escrituração.

2º A partir da versão 12.1.29 foi retirada a obrigatoriedade de informar lotes de escrituração, além de ser possível o agendamento recorrente da mesma. Este processo possibilita configurar um Job para ser executado conforme a demanda da empresa, além do job não estar vinculado a períodos Fiscais. Por exemplo: no inicio do ano pode ser configurado o job de escrituração para ser executado uma vez ao dia (ou por hora, ou por semana, etc.), e este job fará todas as escrituração para todos os meses do ano sem a necessidade de novas configurações ou intervenções do usuário.

Para maiores informações consulte o documento  aba "lote de Escrituração Fiscal" sub aba "Escrituração sem Lote"
