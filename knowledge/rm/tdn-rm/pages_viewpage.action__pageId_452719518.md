---
content_hash: 09cd02c031d0859355a67a68d2dab7577063f43332e83fe2ee5346a2777c14aa
fetched_at: '2026-06-29T00:10:08.457910+00:00'
page_id: '452719518'
product: rm
source: tdn-rm
title: GRRF - Guia de Recolhimento Rescisório do FGTS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719518
version: 2
---

A Caixa Econômica Federal (CEF) disponibiliza um sistema que valida a Guia de Recolhimento Rescisório do FGTS – GRRF e através da Conectividade Social gera a guia para pagamento.  
 A emissão do relatório referente aos funcionários demitidos será feita pelo módulo de folha de pagamento em conformidade com as normas do layout emitido pela Caixa Econômica Federal (CEF).  
    
 Para a emissão é necessário preencher os dados do processo de Rescisão no módulo GRRF – Guia de Recolhimento Rescisório do FGTS.  
    
 Para o parâmetro de Dissídio: Sim/Não, somente deverá informar "Sim" quando for recolhimento referente a dissídio coletivo ou acordo trabalhista.  
    
 Quando este parâmetro for marcado como "Sim" o sistema procederá de acordo com a circular 321/04 da CEF:15.4.2.  
 O recolhimento da Multa Rescisória correspondente ao valor de dissídio/acordo e comissões/percentagens deve ser efetuado por meio do formulário GRFC conforme os procedimentos abaixo:

* A data de movimentação (campo 19) será a do efetivo desligamento do trabalhador;
* Deve ser informada a data de pagamento da comissão/percentagem ao trabalhador, no campo 21 da GRFC, tendo em vista a similaridade com os casos de dissídio.

Preencher a "Data de Dissídio/Acordo" somente quando se tratar de recolhimento referente a dissídio coletivo ou acordo trabalhista, informando a data da sua homologação/publicação.   
    
 No campo "Ind.Correção FGTS" deve ser informado o índice de correção conforme tabela liberada pela CEF para o cálculo sobre o valor do dissídio. Este índice ficará gravado de acordo com o perfil e quando o usuário for gerar outra GRRF sem correção deverá limpar os dois campos.  
 **Observação:**  
 Para os valores dos índices o usuário deverá informar os mesmos com vírgula (,) e não com ponto (.).  
    
 O parâmetro "Desconsiderar o acréscimo de 10% na multa do FGTS" é utilizado no cálculo do lançamento financeiro.  
    
 Caso a empresa faça o recolhimento de FGTS centralizado o parâmetro "Recolhimento Centralizado (CNPJ da Matriz)" deve ser marcado, para que o CNPJ da centralizadora seja informado no arquivo.   
    
 A informação da "Fórmula para cálculo de horas semanais", se utilizada, o resultado da fórmula terá prioridade sobre o cálculo interno utilizado pelo sistema. Caso contrário o sistema utilizará o calculo interno (jornada mensal dividido por 5).  
    
 **Observações:**  
 **1** – Os parâmetros citados acima estão disponíveis para todas as coligadas ou separadamente para cada coligada, caso a opção seja que cada coligada seja emitida com parâmetros específicos. Exceto a "Fórmula para cálculo de horas semanais" que está disponível apenas para parâmetros específicos.  
 **2** - Para a emissão da GRRF de rescisões do próximo mês com Tomador de Serviço será considerado o cadastro na pasta Tomador de Serviço do funcionário no mês competência atual. Se o usuário desejar que a emissão da GRRF do funcionário demitido no próximo mês seja feita para a empresa cedente ou outro tomador, ele deve modificar o cadastro na pasta Tomador de Serviço e distribuir novamente na competência da rescisão.  
 **3** - Caso tenha sido marcada a opção "Gerar Lançamentos Financeiros" na pasta Lançamentos Financeiros, para que o valor dos campos "Mês de Competência" e "Ano de Competência" sejam informados no campo "Mês/Ano de Competência" na pasta Opcionais do lançamento no sistema Controle Financeiro (RM Fluxus), basta que o parâmetro "Usar mês de competência" esteja habilitado na pasta "DATAS" da parametrização do sistema financeiro - RM Fluxus.  
 **4** - Caso tenha sido marcada a opção "Gerar Lançamentos Financeiros" na pasta Lançamentos Financeiros, e tenha sido marcada também a opção para ratear o lançamento por departamento, será gerado apenas UM lançamento financeiro e o rateio por departamento ficara interno à esse lançamento.  
    
 **Atenção:**  
 **1** - O usuário deve sempre verificar os dias a serem distribuídos, pois o total de dias a ser distribuído do mês atual pode ser diferente do total de dias a ser distribuído das rescisões no próximo mês.  
 **2** - Para a emissão correta deve distribuir primeiro o mês atual e depois o próximo mês, caso contrário não será emitida a GRRF os valores referente a rescisão no próximo mês.  
 **3** - Sempre que o usuário for emitir uma GRRF e no mesmo mês de competência tiver rescisão normal e rescisão complementar ele deverá selecionar o período para emitir cada uma das GRRF.   
 **4 -** A distribuição do movimento referente ao mês anterior será armazenada para a emissão da GRRF com valor no campo mês anterior à rescisão.  
 **5 -** Para preenchimento do campo "Pensão Alimentícia" no arquivo da GRRF, o sistema irá seguir o seguinte critério:

Será preenchido com "N - Não existe Pensão Alimentícia", quando:  
 Não existir evento de PENSÃO ALIMENTÍCIA  
 ou existir evento com os códigos de cálculo: 13-PENSÃO ALIMENTÍCIA JUDICIAL, 53-PENSÃO ALIMENTÍCIA JUDICIAL INFORMADA (FOLHA), 54-PENSÃO ALIMENTÍCIA JUDICIAL INFORMADA (13º SALÁRIO), 113-PENSÃO ALIMENTÍCIA SOBRE FÉRIAS, 120-PENSÃO ALIMENTÍCIA SOBRE 13º SALARIO ou 121-PENSÃO ALIMENTÍCIA SOBRE PARTICIPAÇÃO NOS LUCROS   
 e o somatório dos eventos for menor ou igual a zero.

Será preenchido com "P - Percentual da Pensão Alimentícia", quando:  
 Existir eventos com os códigos de cálculo: 13-PENSÃO ALIMENTÍCIA JUDICIAL, 53-PENSÃO ALIMENTÍCIA JUDICIAL INFORMADA (FOLHA), 54-PENSÃO ALIMENTÍCIA JUDICIAL INFORMADA (13º SALÁRIO), 113-PENSÃO ALIMENTÍCIA SOBRE FÉRIAS, 120-PENSÃO ALIMENTÍCIA SOBRE 13º SALARIO ou 121-PENSÃO ALIMENTÍCIA SOBRE PARTICIPAÇÃO NOS LUCROS;  
 e o somatório dos valores for maior que zero;  
 e soma dos percentuais de pensão alimentícia dos dependentes for maior que zero e menor que 100.

**Observação:**

Neste caso, será informado que a pensão alimentícia e por percentual e será levado o valor da soma dos percentuais dos dependentes.

Será preenchido com "V – Valor da Pensão Alimentícia", quando:  
 Existir eventos com os códigos de cálculo: 13-PENSÃO ALIMENTÍCIA JUDICIAL, 53-PENSÃO ALIMENTÍCIA JUDICIAL INFORMADA (FOLHA), 54-PENSÃO ALIMENTÍCIA JUDICIAL INFORMADA (13º SALÁRIO), 113-PENSÃO ALIMENTÍCIA SOBRE FÉRIAS, 120-PENSÃO ALIMENTÍCIA SOBRE 13º SALARIO ou 121-PENSÃO ALIMENTÍCIA SOBRE PARTICIPAÇÃO NOS LUCROS;  
 e o somatório dos valores for maior que zero;  
 e soma dos percentuais de pensão alimentícia dos dependentes for igual a zero ou maior ou igual a 100.

**Observação:**  
 Neste caso, será informado que a pensão alimentícia e por VALOR e será considerado à soma dos valores dos eventos de pensão.
