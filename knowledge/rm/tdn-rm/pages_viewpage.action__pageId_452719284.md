---
content_hash: 43b3d30d26461a6a7b3b03d55f36bff90a049fde141296a82fbb714f37eb02bc
fetched_at: '2026-06-29T00:10:05.351150+00:00'
page_id: '452719284'
product: rm
source: tdn-rm
title: Eventos de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719284
version: 58
---

Eventos são cadastros que representam as verbas a serem lançadas e calculadas na folha de pagamento.  
Os eventos, principalmente os que necessitam de Códigos de Cálculo ou fórmulas, devem ser bem definidos para evitar redundâncias, inconsistências e perda de desempenho em cálculos.  
Através dos eventos são gerados todos os cálculos influentes para a GFIP, GPS, GRRF, Geração de Encargos Contábeis, Contabilizações da Folha, além dos relatórios mensais e relatórios anuais e etc.  
Para melhor visualização dos dados, o cadastro de eventos é dividido em pastas. As pastas e os principais campos estão destacados abaixo.  
 

# **Pasta Identificação**

**Descrição**

Campo destinado para informar uma descrição que identifique o evento. Como boa prática e melhor visualização dos eventos orientamos a não usar descrições iguais para eventos ativos com finalidades diferentes.

**Código de Cálculo**

Código de cálculo é um campo do Cadastro de Eventos, representado por um número, cujo significado está associado a uma tabela criada pela TOTVS. Este número indica ao RM Labore qual a natureza do evento, de forma que o sistema possa calcular o valor de alguns deles (como acontece com o INSS, IRRF, Salário Família, Desconto do Vale Transporte, etc.) e/ou identificar valores para relatórios oficiais (como é o caso de Honorários pagos e Assistência Médica, por exemplo) ou para o próprio cálculo de outros eventos (como é o caso de DSR perdido, Base de INSS em Outros Empregos, Total Entregue de Vale Transporte, etc.).   
Alguns eventos estão previamente vinculados a Códigos de Cálculo, outros exigem a criação de fórmulas para serem calculados. Nada impede, no entanto, que se criem fórmulas para os eventos associados a Códigos de Cálculo. Neste caso, o sistema dará prioridade às fórmulas.   
Alguns códigos de cálculo são mantidos na base de dados apenas por questões de compatibilidade com outros sistemas e não são tratados pelo sistema.

**Chave**

A chave informada será relevante para impressão dos eventos em relatórios que possuem o recurso de seleção de chaves.

 **Prioridade**

A prioridade é um valor a ser definido para ordem de cálculo do evento, compreendido entre 0 a 99. 

A definição de 'Prioridade' faz com que eventos que são dependentes de cálculo entre si sejam calculados por ordem.

O sistema respeita a prioridade pela ordem crescente, ou seja, eventos que possuem prioridade menor, por exemplo, '0' será calculado antes de um evento que possuir prioridade 10.

**Exemplo**

         O evento 'B' possui uma fórmula que depende do cálculo do evento 'A'. Logo o evento 'A' tem que ser calculado antes do evento 'B'. Portanto, o evento 'A' tem que ter uma prioridade menor que a do evento 'B'.

Os eventos com prioridade de 83 (oitenta três) em diante não serão considerados para o cálculo de IRRF e INSS, mesmo que estejam incidindo nos mesmos.  
O evento de empréstimo sempre será o último a ser calculado, independente da prioridade informada em seu cadastro. Nos casos onde o envelope possuir eventos com prioridade igual a 99, esses serão calculados após o evento de empréstimo.  
     **Obs.:** O sistema considerará o evento de empréstimo que foi cadastrado nos empréstimos do funcionário.

Aqueles usuários que utilizam a rotina de Controle de Insuficiência de Saldo de Verbas definido nos Parâmetros do cadastro do Funcionário deverão verificar a Prioridade dos Eventos x Insuficiência de Saldo.

Exceções quando utiliza Cálculo .Net:

1. O evento cujo o cálculo necessitar que as médias já estejam calculadas, precisam ter prioridade 70. Todos os eventos com prioridade 70 serão recalculados após o cálculo da média.

**Atenção:**

        1. O cálculo da média não segue prioridade, sempre é calculado por último, o sistema calcula todo o envelope e depois calcula a média. Porém para atender situações em que o evento precisa do cálculo da média já calculada, este evento deve ter prioridade 70, assim o sistema entende que este evento precisa ser recalculado após as médias.  
**Exemplo:**

Criei a fórmula CALCMED(1) e informei no evento XXXX, porém este evento XXXX entra na média. O evento XXXX deverá ter prioridade 70.

2. A prioridade para os códigos de cálculos abaixo ficam desabilitada e com prioridade definida pelo sistema para que o usuário não altere:

Prioridade 70 => Código de cálculo: 40 e 63.

Prioridade 80 => Código de cálculo: 5, 6 e 149.

Prioridade 81 => Código de cálculo: 3, 11, 26, 27, 30, 31, 68, 73, 82, 89, 90, 91, 92, 103, 108, 110, 130, 131, 132, 133, 135, 137, 138, 153, 171, 172, 179

Prioridade 82 => Código de Cálculo: 13, 113, 120, 121.

Prioridade 83 => 4, 30, 49, 52, 61, 122, 127, 305, 306, 307, 308, 316

3. Quando o evento tem a mesma prioridade, a segunda ordem é o campo 'Ordem de Cálculo'  e a terceira ordem é o código do evento.  
   
**Percentual de Incidência**

Utilizado em eventos que possuem cálculo de adicional sobre o valor do salário horário contratual. O percentual informado será calculado.

**Exemplo:**

         Hora Extra 50%, deve-se definir Percentual de incidência 1,50.

         Hora Extra 100%, deve-se definir Percentual de incidência 2,0.  
   
**Observação:**

         Os Eventos do tipo Valor devem ter o percentual de incidência igual a 0 (zero).  
   
**Proporcionalidade**

Este grupo somente fica visível quando nos parâmetros do RM Labore o parâmetro 'Proporcionaliza eventos' está marcado.  
O sistema automaticamente proporcionaliza os eventos baseando-se nos CheckBox Admissão, Demissão, Férias e Afastamento que estão marcados neste grupo.   
O sistema busca o valor do campo 'Valor Original' do evento divide 30 e multiplica pelos nº de dias de direito do mês.

**Exemplo:**

         O funcionário tem 10 dias de férias no mês de 30 dias.   
         Supondo que o evento PRODUTIVIDADE tem o campo 'Férias' marcado no grupo 'Proporcionalidade'.   
         Neste mês o funcionário tem R$90,00 no evento PRODUTIVIDADE.  
         O cálculo é: R$90,00 / 30 \* 20= R$60,00

**Atenção:**  
         1. Esta PROPORCIONALIDADE não é válida para os códigos de cálculo 1 e 2.  
         2. As opções de proporcionalidade estarão disponibilizadas somente quando o evento é do tipo Valor.  
         3. Para funcionário com o código de recebimento 'H-Horista' o sistema divide pelo número de dias do mês ao invés de fixar 30.  
   
**Fórmula de Crítica**

Fórmulas de crítica é utilizada para verificar se determinado evento foi ou não calculado para um funcionário ou grupo de funcionários, quando executado módulo 'Crítica da Folha'.   
Somente Fórmulas cadastradas como 'Crítica Global' podem ser associada ao campo 'Fórmula de Crítica' do cadastro de Eventos.

**Exemplo:**

         Fórmula de Crítica para validar se o Evento '0005-Salário Família' foi calculado para o funcionário no movimento atual:

         SE C('0005') > 0

         ENTAO 'PAGOU SALARIO-FAMILIA'

         SENAO 'NÃO PAGOU SALARIO-FAMILIA'

         FIMSE

**Código Rubrica**

Informe nesse campo o código da rubrica relacionada ao tipo de verba que o evento possui. 

**Atenção:**

         1. Caso o evento não se enquadre na rubricas existentes, será possível cadastrar mais rubricas na tabela dinâmica HOMOLOGRUB. Entretanto, no momento de cadastrar essas rubricas deve-se observar o manual do Homolognet, pois já foram definidas as rubricas numeradas de 001 a 034, e exige que as novas rubricas sejam cadastradas a partir do número 100.

   
         2. No Homolognet são considerados os envelopes das 80 competências anteriores (ou desde a competência de contratação, caso o tempo de casa seja menor). Portanto, como não é possível definir quais eventos eram utilizados na época e atualmente não são mais, recomendamos preencher esse campo em todos os eventos.  
 

**Segue Rateio de Tomadores**

Os eventos que tiverem este parâmetro confirmado serão proporcionalizados conforme alocação em tomadores de serviço. Entende-se como 'Alocação', a associação do cadastro do Tomador de Serviço ao cadastro do Funcionário e a informação da quantidade de dias para rateio.  
**Observação:**

           1. Este campo será visível no cadastro de seções apenas quando nos parâmetros do RM Labore o parâmetro 'Utiliza Tomadores de Serviço' estiver marcado.  
           2. Eventos que não tiverem o campo 'Segue Rateio de Tomadores' marcado, terão seus valores rateados para o tomador principal da empresa, definido nos parâmetros do RM Labore.   
           3. Defini-se tomador principal da empresa, para a identificação da alocação de funcionários 'administrativos', ou seja, funcionários que não são alocados a tomadores terão seus eventos rateados para tomador principal, não sendo necessária a associação de tomador no cadastro destes funcionários.

**Incide no Custo do Funcionário**  
Farão parte do cálculo das horas pagas ao funcionário os eventos e os encargos que tiverem esse parâmetro marcado, caso contrário ele não fará parte do cálculo de horas pagas para o funcionário.

**Observação:** Este parâmetro é utilizado para integração RM Labore e RM Chronus com o TOP (Totvs Obras e Projetos).  
   
**Evento de Provento Obrigatório**

Este campo permite que os eventos sejam pagos obrigatoriamente, mesmo havendo insuficiência de saldos.

**Atenção:**

           Conforme legislação trabalhalista, os eventos Salário Família (CC5), Dif. Salário Família (CC65) e PIS (CC125) devem ser pagos obrigatoriamente para o funcionário, não necessitando da parametrização específica acima citada.  
   
**Observação:** Quando utiliza o parâmetro 'Utiliza controle de Saldo de Verbas' existente no Cadastros do Funcionários, o sistema paga o evento (Provento), mesmo quando a quantidade de descontos é maior que  o provento, guarda o evento desconto na pasta 'Verbas c/Insuficiência de saldo' da Ficha Financeira, e desconta em movimentação subsequente.   
Escolhendo esta parametrização o sistema não utiliza o processo automático de arredondamento.  
   
**Incide substituição**

Esse campo deve ser marcado quando o usuário trabalhar com adicional de substituição.   
Neste caso, o evento é considerado no momento do cálculo de médias e no cálculo do valor da hora de substituição.  
O sistema consulta o cadastro de substituição do funcionário (existente na ficha financeira) para calcular o valor das horas de substituição. O valor de cada hora de substituição é valorizado de acordo com a diferença entre o salário de quem é substituído e o valor do salário de quem substitui.

**Observação:**

            1. Este parâmetro somente fica habilitado quando o evento é do tipo hora ou referência, exceto para os eventos com códigos de cálculo 1 e 2, para o valor ser duplicado, porque já considera automaticamente o salario nominal do funcionário a ser substituído.  
            2. Se marcado, o usuário poderá visualizar na Ficha Financeira, pasta Substituição.

**Compõe Comissão**

Este campo é utilizado para calcular o Salário Comissão de funcionários comissionistas ou mistos.

**Observações:**

            1. Os eventos que compõem comissão não podem fazer parte dos eventos que incidem em média.  
   
            2. Para cálculos de médias parametrizadas no sindicato dos funcionários comissionistas, o sistema considera o Salário Comissão com base na totalização dos eventos que compõe comissão, assim realizando os  cálculos das médias.  
   
            3. Se o funcionário deixa de ser assalariado e passa a ser comissionista, para que os dias trabalhados em regime de comissão tenham incidência em comissão será necessário editar os eventos de dias trabalhados, marcar a opção "Compõe Comissão" e efetuar os recálculos. 

    
**Compõe Remuneração Base de Professor**  
Este campo é utilizado para calcular a Remuneração base de Professor, onde o usuário irá marcar os eventos cujo valores serão utilizados para apuração dessa Remuneração.

**Observação:** A Remuneração Base será aplicável apenas para funcionários do tipo P – Professor que utilizem o sindicato que está devidamente parametrizado para esse cálculo.  
*Opções de rateio por centro de custo*

**Centro de Custo do Evento**  
Este campo determina o centro de custo em que o evento é rateado, ignorando assim, o rateio fixo registrado no cadastro do funcionário.  
**Observação:**  
            Quando este campo é preenchido o campo 'Código do Rateio que o Evento Segue' fica desabilitado.

**Código do Rateio que o Evento Segue**  
Deve ser informado neste campo o código do rateio definido em Cadastros | Rateio de Eventos.   
O preenchimento deste campo tem prioridade sobre o centro de custo informado no rateio fixo do funcionário.   
Caso os eventos cadastrados no Rateio de Eventos não existam no envelope do funcionário será considerado o centro de custo do Rateio Fixo do funcionário.  
   
Observação: Maiores informações/exemplos de uso do parâmetro acima para a contabilização da folha do professor, verifique o tópico [DT Rateio Contábil da folha do professor](https://tdn.totvs.com.br/pages/viewpage.action?pageId=271184164).

   
**Período para Cálculo de Rateio**  
Este campo é obrigatório quando o campo 'Código do Rateio que o Evento Segue' está preenchido.   
Serão disponibilizados os seguintes períodos:  
          1 – Mês Atual   
          2 – Período Aquisitivo  
          3 – Ano de Competência  
          4 – Mês Anterior  
 

**Não calcula diferença desse evento**

Marcando este parâmetro, o evento não será considerado para o cálculo de todas as Diferenças (Salarial, 13º Salário, Férias). Este parâmetro deve ser marcado no **evento original**, devendo estar desmarcado no evento de diferença.

**Observação:**  
          1. Para caso de diferença de férias, deverá ser marcado para os eventos que constam no Recibo de Férias.

**Evento para Diferença Salarial**  
Neste campo é necessário preencher com eventos de diferença que serão considerados no cálculo das diferenças (salarial, férias, 13º Salário e rescisão complementar).

**Observação:**  
          1. Serão listados apenas os eventos do tipo valor e sem código de cálculo, ou com código de cálculo 37-Diferença Salarial, 14-Assistência Médica e 65-Dif. Salário Família.  
   
          2. Sempre que um evento não tiver o evento de diferença, o sistema lança o valor no evento com código de cálculo 37-Diferença Salarial, seja, desconto ou provento.   
              Sendo assim torna-se obrigatório para os eventos de desconto, o preenchimento deste campo quando houver qualquer diferença que não possa estornar a diferença salarial nos cálculos de impostos       (INSS/IRRF/FGTS).

          3. O evento de diferença deve ter as mesmas incidências do evento original.

 **Exemplo:**

Com evento de diferença cadastrado em eventos de descontos

Aumento salarial de R$100,00 para R$200,00

Evento diferença salarial = R$100,00

Desconto Ticket Restaurante 5% do salário = de R$ 5,00 para R$ 10,00

Evento Diferença Ticket = R$ 5,00

Incide INSS/IRRF/FGTS = Salário R$200,00 + Diferença Salarial R$100,00 = R$ 300,00  
   
Sem evento de diferença cadastrado em eventos de descontos

Aumento salarial de R$100,00 para R$200,00

Evento diferença salarial = R$95,00

Desconto Ticket Restaurante 5% do salário = de R$ 5,00 para R$ 10,00

Não tem evento para diferença de desconto Incide INSS/IRRF/FGTS = Salário R$200,00 + Diferença Salarial R$95,00 = R$295,00

**Atenção:**  
O sistema lança de acordo com o processo executado, ou seja, se o evento de desconto foi lançado no envelope de férias o sistema desconta a diferença do evento de desconto do evento de diferença de férias, e caso o desconto tenha ocorrido dentro do envelope de pagamento mensal o sistema descontará a diferença do evento de desconto do evento de diferença salarial.   
   
**Evento de Insuficiência de Saldos**

Este campo somente é habilitado para eventos do tipo desconto e quando existe pelo menos um funcionário com o campo 'Utiliza Controle de Saldo de Verbas' marcado.  
As insuficiências são os eventos cujos descontos são maiores que os proventos.  
Os descontos com mesma prioridade e que possuem menor valor são descontados primeiro.

**Exemplo:**

Se o funcionário está com débito de R$700,00 de farmácia conveniada à empresa, e possui total de proventos R$500,00 o sistema armazenará o saldo relativo à diferença entre proventos e descontos (R$200,00) na tabela PFVERBAS.

**Observações:**

1. As 'Verbas c Insuficiência de Saldo' poderão ser visualizadas através da ficha financeira.  
2. Para lançar o débito do mês ou periodo anterior, é necessário marcar o parâmetro 'Lançar Verbas com Insuficiência de Saldo do mês ou período anterior' existente no módulo de Lançamento de Grupo de Eventos ou Rescisão.

Quando utiliza Cálculo .Net

A ordem de lançamento dos eventos de descontos que geraram saldo negativo é por ordem de prioridade do evento. Quando os eventos tem a mesma prioridade, a segunda ordem é o código do evento. Porém o INSS, IRRF e Pensão Alimentícia tem prioridade de desconto superior a qualquer ordem.  
 

# **Pasta Anotações**

Deve registrar as informações importantes sobre o evento: objetivo, forma de cálculo, em que processos são utilizados, etc.

# **Pasta Acumuladores**

Os acumuladores são utilizados para agrupar eventos com características comuns em fórmulas e/ou relatórios. Devem ser incluído na tabela dinâmica INT34, em Cadastros | Tabelas Dinâmicas.

**Observações:**

Poderão existir no máximo 100 acumuladores inseridos na tabela dinâmica INT34.   
   
**Exemplo:**

É necessário montar a fórmula de cálculo de uma gratificação, utilizando a soma de 8 (oito) eventos diferentes.   
Ao montar a fórmula, não será necessário mencionar todos os eventos, apenas utilizar um mesmo acumulador para todos eles.

# **Pasta Dados Contábeis**

Estes dados são utilizados na parametrização da contabilização da movimentação da folha de pagamento.  
   
**Conta Contábil  
Conta para Débito**Este campo é um agrupador de eventos utilizado para contabilização.  
   
Este grupo tem como objetivo facilitar a montagem do plano de contas no RM Labore, evitando que o usuário tenha que criar um item no plano de contas para cada evento.

Os grupos devem ser criados em Cadastros | Tabelas Dinâmicas, tabela GRPCONT, de acordo com o nível de detalhamento que a contabilidade exige, ou seja, eventos que tenham o mesmo destino na contabilidade provavelmente usarão o mesmo grupo de conta.  
**Tem integração contábil**Quando o evento tem este campo marcado, significa que o sistema usa o grupo de conta débito mais o código de integração atribuído à seção ou ao centro de custo do funcionário para determinar a conta contábil correta no plano de contas.   
O cadastro dos códigos deverão ser feitos previamente na tabela CODINTCONT em Cadastros | Tabelas Dinâmicas.  
   
**Tem integração por funcionário**Quando o evento tem este campo marcado, significa que o sistema agrega ao grupo de conta débito o código de integração informado no funcionário (Cadastro | Funcionários | Dados Contábeis) para determinar a conta no plano de contas.   
Os campos integração contábil e integração por funcionário são independentes entre si, portanto, se o campo 'Tem integração contábil' também está marcado, a procura no plano de contas será por: grupo de conta débito + código integração + código integração por funcionário.  
O cadastro dos códigos deverão ser feitos previamente na tabela INTCONTFUN em Cadastros | Tabelas Dinâmicas.  
   
**Conta para Crédito**Como normalmente se contabiliza os valores creditando em uma conta e debitando em outra, é necessário indicar um grupo de conta para débito e outro para crédito, bem como indicar se existe 'Integração contábil' e 'Integração por funcionário' para cada caso. Este campo, portanto, é idêntico ao grupo de conta débito exceto o fato de ser destinado a conta de crédito.  
   
**Contabilização Parcial**Este campo determina se a contabilização tem apenas conta crédito ou conta débito, parte ausente será contabilizada posteriormente de uma outra forma. Podendo ser por exemplo através do líquido.  
Quando este campo não está marcado, obrigatoriamente deve-se informar as duas contas, crédito e débito.  
  
**Conta Gerencial  
Conta para Débito**Idem a conta débito da conta contábil, porém direcionada para contabilização gerencial.  
O cadastro dos códigos deverão ser feitos previamente na tabela GRPGER em Cadastros | Tabelas Dinâmicas.   
  
   
**Tem integração contábil**Idem a conta débito da conta contábil, porém direcionada para contabilização gerencial com integração contábil.  
O cadastro dos códigos deverão ser feitos previamente na tabela CODINTGER em Cadastros | Tabelas Dinâmicas.  
  
   
**Tem integração por funcionário**Idem a conta débito da conta contábil, porém direcionada para contabilização gerencial com integração por funcionário.  
O cadastro dos códigos deverão ser feitos previamente na tabela INTGERFUN em Cadastros | Tabelas Dinâmicas.  
  
   
**Conta para Crédito**Idem a conta crédito da conta contábil, porém direcionada para contabilização gerencial.  
  
   
**Número do Histórico Padrão**O histórico deve ser previamente cadastrado em Cadastros | Contabilização | Histórico Padrão.  
Em caso de bases integradas com RM Saldus (Contabilidade gerencial), o cadastro de Histórico Padrão não é visualizado pelo RM Labore e o cadastramento é feito através do RM Saldus.  
   
**Fórmula para complemento de histórico**O uso da fórmula não elimina o conteúdo existente no complemento de histórico e, sim, acrescenta informação.

> > **Exemplo:**Complemento de Histórico: Contabilização ref ao mês:   
> > Fórmula para Complemento de Histórico: MES (fórmula retorna o Mês competência atual).   
> > Ao contabilizar este evento ou encargo o Complemento de histórico gerado será: Contabilização ref ao mês: 02 (sendo o mês usado no exemplo o Mês de Fevereiro).
> >
> > **Observações:**
> >
> > 1. Entre os campos Complemento do Histórico e a Fórmula do Complemento do Histórico será acrescentado, no lançamento contábil, um espaço em branco para separar as informações entre estes dois campos.
> >
> > 2. Informando uma fórmula com a variável PAR, serão levados para o complemento do histórico do lançamento contábil o mês, o ano e o(s) período(s) da competência que está sendo gerado o lote.  
> > O retorno da variável PAR assume dois formatos:
> >
> > Formato 1 - Quando for(em) selecionado(s) período(s) específico(s) na competência:
> >
> > MM-AAAA-P, onde:  
> > MM = Mês da competência  
> > AAAA = Ano da competência  
> > P = Período(s) [quando houver mais de um período, aparecem separados por vírgula]
> >
> > **Exemplos:**
> >
> > 1. 01-2004-1,2 onde
> >
> > 01 = Janeiro
> >
> > 2004 = Ano de 2004
> >
> > 1,2 = Períodos 1 e2
> >
> > Formato 2 - Quando NÃO for(em) selecionado(s) período(s) específico(s) na competência
> >
> > MM-AAAA, onde:
> >
> > MM = Mês da competência
> >
> > AAAA = Ano da competência
> >
> > 2. 12-2003 onde:
> >
> > 12 = Dezembro
> >
> > 2003 = Ano de 2003
> >
> > **Atenção:**
> >
> > O retorno da variável PAR na contabilização é sempre STRING, e os valores de Mês, Ano e Período(s) da competência são separados por hífen (-).

****Segue rateio movimento temporário****Esse parâmetro apenas ficará visível quando a integração com outros BackOffices estiver ativa e se o Folha de Pagamento estiver integrado com o Automação de Ponto. Ele será utilizado no processo de contabilização e lançamentos financeiros para identificar o rateio a que o evento será direcionado, agrupando por centro de custo, item contábil ou classe de valor. Esses dados serão buscados do movimento de integração(PFMOVTEMP) integrado com o Automação de Ponto. Se esse parâmetro for marcado, o “Segue rateio movimento ensino na geração dos lançamentos contábeis” será desabilitado.

**Segue rateio movimento ensino**

Esse parâmetro apenas ficará visível quando a integração com outros BackOffices estiver ativa e se o Folha de Pagamento estiver integrado com o Educacional. Ele será utilizado no processo de contabilização e lançamentos financeiros para identificar o rateio a que o evento será direcionado, agrupando por centro de custo, item contábil ou classe de valor. Esses dados serão buscados do movimento de ensino(PFMOVENSINO) integrado com o Educacional. Se esse parâmetro for marcado, o “Segue rateio movimento temporário na geração dos lançamentos contábeis” será desabilitado.

 Observação: Para maiores informações/exemplos de uso dos parâmetros "Segue rateio movimento/ensino" para a contabilização da folha do professor, verifique o tópico "Parametrizar o sistema para recebimento do rateio contábil" no link "Como fazer - Rateio da folha do professor".

# **Pasta Inc. Proventos**

Proventos são todos os eventos que são somados para o rendimento dos funcionários: horas extras, salário família, comissão e etc. Marque os campos correspondentes (com um clique do mouse) ou deixe-os em branco para que o sistema não proceda a incidência.  
**INSS**

Quando este parâmetro estiver marcado, o evento é somado à base de cálculo do INSS.

Para emitir o relatório de AAS com verbas discriminadas, preencha o campo Grupo AAS com a referência do grupo a que pertence o evento. Os grupos são cadastrados na tabela INT35 em Cadastros | Tabela Dinâmica.  
**Observações:** 1. O campo 'Grupo AAS' somente é habilitado quando o parâmetro 'Usa AAS Discriminado' existente em Opções | Parâmetros | RM Labore | Outros Parâmetros | pasta Parâmetros II estiver marcado.  
2. Quando o parâmetro 'Usa AAS discriminado' existente em Opções | Parametros | RM Labore | Outros Parametros | Parâmetros III estiver marcado, o campo Grupo AAS será habilitado se: - o evento incidir em INSS; - o evento tiver o código de cálculo 189; - o evento tiver sido informado em Opções | Parâmetros | RM Labore | Parâm. Cálculo, nos campos de Salário   Maternidade.

**Atenção:**

Quando o parâmetro 'INSS 13º Salário' estiver marcado, o campo 'Grupo de AAS', não será habilitado. O décimo terceiro salário embora seja considerado salário de contribuição para fins de recolhimento previdenciário, desde a publicação da Lei nº 8870/94 (Boletim TL, página 470) ele passou não integrar o salário de benefício para cálculo de qualquer benefício mantido ou pago pelo INSS. Assim, ao fazer a relação dos salários-de-contribuição, o 13º salário não deve ser inserido.

**Incidências de pensão**

Este parâmetro é utilizado para o cálculo da pensão alimentícia parametrizada no dependente do funcionário.

**Informe de Rendimentos**

Todo provento que incidir em: IRRF, IRRF Férias ou IRRF 13º Salário, devem também incidir no Informe de Rendimentos.

**Grupo AAS**

Este campo deve ser informado para a emissão da relação de salários de contribuição com verbas discriminadas. Informe o código do grupo AAS breviamente cadastrado na tabela INT35 em Cadastros | Tabelas Dinâmicas. No momento da liberação de competência serão transferidos para as tabela BASE AAS os proventos adicionados e os descontos estornados do grupo correspondente.

**Incide Salário**

Marcando este parâmetro o evento é somado ao salário no momento do cálculo de um evento do tipo hora, dia ou referência.

**Exemplo:**

O evento Insalubridade tem o parametro 'Incide salário' marcado e foi lançado no envelope de pagamento. Ao calcular o evento de hora extra, este será calculado sobre a soma do salário mais o evento de insalubridade.

**Atenção:**

Para maior transparência, quando utilizar Cálculo .Net, o sistema deixa de tratar as incidências dos eventos internamente, passando a verificar exatamente o que esta parametrizado no evento, exceto os eventos de INSS e IRRF.

**Exemplo:**

No código fixo existe o cc120-Pensão alimentícia sobre 13º salário do tipo Folha, e no envelope do funcionário existe um evento que incide em pensão de 13º salário, com isto o .NET calcula a pensão 13º Salário. Em DELPHI não calcula porque o cc120 está parametrizado internamente ao código de cálculo de 13º salário e a rotina de lançamento do 13º salário.

**INSS**

* **Incidência exclusiva do segurado**

Marcando este parâmetro o sistema irá desconsiderar o evento na base de cálculo de INSS para o cálculo dos impostos: **Percentual Empresa, Terceiros e Acidente de Trabalho**.

**Observação:**  O eventos será desconsiderado nas rotinas: GPS, Folha Analítica e Encargos.

* **Incidência exclusiva do empregador**

Este parâmetro tem como objetivo atender a legislação do eSocial em situações onde o empregador não irá descontar do seu funcionário o valor do INSS, porém irá recolher os impostos da parte da empresa.

Ao gerar o XML do evento **S-1010-Tabelas de Rubricas** será levado na tag **<codindCP>** o valor **13-Exclusiva do Empregador - mensal**.

[Folha analítica e GPS - Incidência Exclusiva do segurado e Incidência Exclusiva do Empregador](http://tdn.totvs.com/pages/viewpage.action?pageId=520101874)

[Folha analítica e GPS - Incidência Exclusiva do segurado no 13° salário.](http://tdn.totvs.com/pages/viewpage.action?pageId=520671442)

Em versões inferiores a 12.1.27 é imprescindível a execução do Script Oracle(ESOCIALFOP01-10695.ORA) ou SQL server (ESOCIALFOP01-10695.SQL) de acordo com o banco de dados utilizado. 

Maiores informações acesse o link: <http://tdn.totvs.com/display/LRM/Executor+de+Scripts+RM>

**INSS**

* **Não é base de cálculo em função de acordos internacionais:**

                    Este parâmetro tem como objetivo atender a legislação do eSocial em situações onde o funcionário é expatriado, ao qual seu pais de origem mantem um acordo internacional de bitributação, identificando se o evento que NÃO incide em INSS será  considerado como "00 - Não é base de cálculo" ou "01 - Não é base de cálculo em função de acordos internacionais de previdência social" no evento **S-1010 - Tabela de Rubricas**. Veja mais detalhes no mapeamento do evento S-1010         <http://tdn.totvs.com.br/display/LRM/S-1010+-+Tabela+de+Rubricas>.  
   
**Atenção:**  
Este parâmetro somente ficará habilitado quando o  evento NÃO incidir em INSS.  
Esta informação é exclusivamente para o eSocial. Ainda não influenciam no cálculo da folha.  
   
   
 **IRRF**

* **Rendimento não tributável em função de acordos internacionais de bitributação:**

Este parâmetro tem como objetivo atender a legislação do eSocial em situações onde o funcionário é expatriado, ao qual seu pais de origem mantem um acordo internacional de bitributação, identificando se o evento que NÃO incide em IRRF será considerado como "00 - Rendimento não tributável" ou "01 - Rendimento não tributável em função de acordos internacionais de bitributação" **codIncIRRF descontinuado com a versão S-1.0.**  
no evento **S-1010 - Tabela de Rubricas**. Veja mais detalhes no mapeamento do evento S-1010.  
<http://tdn.totvs.com.br/display/LRM/S-1010+-+Tabela+de+Rubricas> .   
 

**INSS 13°**

Marcando este parâmetro o sistema irá desconsiderar o evento na base de cálculo de INSS 13º Salário para o cálculo dos impostos: **Percentual Empresa, Terceiros e Acidente de Trabalho**.

**Observação:**  O eventos será desconsiderado nas rotinas: GPS, Folha Analítica e Encargos.

**Atenção:**  
Este parâmetro somente ficará habilitado quando o  evento NÃO incidir em IRRF.  
Esta informação é exclusivamente para o eSocial. Ainda não influenciam no cálculo da folha.  
   
Cálculo .Net

Para maior transparência, o Cálculo .Net deixa de tratar as incidências dos eventos internamente, passando a verificar exatamente o que esta parametrizado no evento, exceto os eventos de INSS e IRRF.

**Atenção:**

Com este novo comportamento, em obedecer exatamente o que for parametrizado pelo usuário, pode influenciar em várias situações do cálculo. Sendo importante revisar as incidências dos eventos.

**Incidência(s) suspensa(s) em decorrência de decisão judicial**

Os parâmetros existentes dentro deste agrupador, são utilizadas para informar ao eSocial que existe suspensão de alguma das incidências (INSS, IRRF, FGTS ou Contribuição Sindical).

**Atenção:**

1. Os parâmetros de incidência presente neste agrupador ficarão habilitados apenas quando não possuir marcação de seu correspondente no agrupador "Folha" ou "13º Salário".
2. A flag "Incidência IRRF PLR" ficará habilitado caso possua código de cálculo 126 e atenda a regra anterior.
3. A flag "Incidência Contribuição Sindical" é habilitada quando o evento incide em salário.
4. A flag "Exclusiva do Empregador" será habilitada quando o evento possuir marcação no agrupador "Folha" -INSS  ou  "13 Salário" -INSS 13 salário.

* Caso o campo “Incidência Suspensa em Decorrência de Decisão Judicial / Exclusiva Empregador” esteja preenchido, entende-se que a incidência INSS é somente para segurado. Isso ocorre quando existe um evento que tem incidência de INSS para segurado e empregador, porém devido a um processo judicial o evento deixa de ter incidência para o empregador, devendo gerar o evento S-1010 tag codInCP com os valores de suspensão (91, 92....)

**Isento de IRRF**  
Ao marcar esse parâmetro, será disponibilizada uma lista onde o usuário poderá escolher qual valor irá para o campo codIncIRRF do evento S-1010. Essa lista contém os casos em que existe a isenção do IRRF:  
 70 - Parcela Isenta 65 anos - Remuneração mensal;

71 - Parcela Isenta 65 anos - 13° salário;

72 - Diárias;

73 - Ajuda de custo;

76 - Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - Remuneração Mensal;

77 - Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - 13° salário;

78 - Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e alugueis; **codIncIRRF descontinuado com a versão S-1.0.**

79 - Outras isenções (o nome da rubrica deve ser claro para identificação da natureza dos valores);

700 - Auxílio moradia; **codIncIRRF criado com a versão S-1.0 ele só será aceito nessa versão.**

701 - Parte não tributável do valor de serviço de transporte de passageiros ou cargas. **codIncIRRF criado com a versão S-1.0 ele só será aceito nessa versão.**

Obs.: Apenas ficará disponível para marcação, caso o evento não possua nenhuma incidência relativa a IRRF.

**F****orçar codIncCP eSocial**

Ao marcar esse parâmetro, será disponibilizada uma lista onde o usuário poderá forçar o valor de incidência tributária que será levado no campo codIncCP do evento S-1010. Essa lista contém apenas os valores correspondentes a incidência tributária:  
31 - Mensal (Contribuição descontada do segurado sobre salário de contribuição)

Ao forçar a incidência tributária, o valor informado irá sobrescrever a regra adotada pelo sistema conforme o [Mapeamento do evento S-1010](http://tdn.totvs.com/display/LRM/Evento+S-1010).

Obs: Apenas ficará disponível para marcação, caso o evento não possua nenhuma incidência relativa a INSS.

**F****orçar codIncIRRF eSocial**

Ao marcar esse parâmetro, será disponibilizada uma lista onde o usuário poderá forçar o valor de incidência tributária que será levado no campo codIncIRRF do evento S-1010. Essa lista contém apenas os valores correspondentes a incidência tributária:  
00 - Rendimento não tributável; **codIncIRRF descontinuado com a versão S-1.0.**

09 - Outras verbas não consideradas como base de cálculo ou rendimento.

33 - Férias

43 - Previdência Social Oficial - PSO - Férias

53 - Pensão alimentícia - Férias

Ao forçar a incidência tributária, o valor informado irá sobrescrever a regra adotada pelo sistema conforme o [Mapeamento do evento S-1010](http://tdn.totvs.com/display/LRM/Evento+S-1010).

Obs: Apenas ficará disponível para marcação, caso o evento não possua nenhuma incidência relativa a IRRF.

**Contribuições RPPS/Regime Militar**

Este campo é utilizado para enviar o código de incidência da rubrica para as contribuições do Regime Próprio de Previdência Social - RPPS/regime militar, atender a geração da tag <codIncCPRP> no evento S-1010 do eSocial.

**Observação:** conforme MOS

 

# **Pasta Inc. Descontos**

Esta pasta registra as parametrizações do evento do tipo Descontos, isto é, os eventos que deduzem os rendimentos dos funcionários. Marque os campos correspondentes (com um clique do mouse) ou deixe-os em branco para que o sistema não proceda a dedução. 

**Grupo AAS**

Este campo deve ser informado para a emissão da relação de salários de contribuição com verbas discriminadas.

Informe o código do grupo AAS breviamente cadastrado na tabela INT35 em Cadastros | Tabelas Dinâmicas.

No momento da liberação de competência serão transferidos para as tabela BASE AAS os proventos adicionados e os descontos estornados do grupo correspondente.

**Desconto Perdoado**

Marque este parâmetro caso o evento cause insuficiência de saldo e deve ser perdoado no próximo movimento do funcionário. O sistema ao lançar o evento na verbas com insuficiência de saldo, grava o campo PFVERBAS.DESCONTADO com 1, para não ser lançado no movimento.  
Cálculo .Net

Para maior transparência, o Cálculo .Net deixa de tratar as incidências dos eventos internamente, passando a verificar exatamente o que esta parametrizado no evento, exceto os eventos de INSS e IRRF.

**Atenção:**

Com este novo comportamento, em obedecer exatamente o que for parametrizado pelo usuário, pode influenciar em várias situações do cálculo. Sendo importante revisar as incidências dos eventos.

**F****orçar codIncCP eSocial**

Ao marcar esse parâmetro, será disponibilizada uma lista onde o usuário poderá forçar o valor de incidência tributária que será levado no campo codIncCP do evento S-1010. Essa lista contém apenas os valores correspondentes a incidência tributária:  
31 - Mensal (Contribuição descontada do segurado sobre salário de contribuição)

Ao forçar a incidência tributária, o valor informado irá sobrescrever a regra adotada pelo sistema conforme o [Mapeamento do evento S-1010](http://tdn.totvs.com/display/LRM/Evento+S-1010).

Obs: Apenas ficará disponível para marcação, caso o evento não possua nenhuma incidência relativa a INSS.

**F****orçar codIncIRRF eSocial**

Ao marcar esse parâmetro, será disponibilizada uma lista onde o usuário poderá forçar o valor de incidência tributária que será levado no campo codIncIRRF do evento S-1010. Essa lista contém apenas os valores correspondentes a incidência tributária:  
00 - Rendimento não tributável; **codIncIRRF descontinuado com a versão S-1.0.**

09 - Outras verbas não consideradas como base de cálculo ou rendimento.

33 - Férias

43 - Previdência Social Oficial - PSO - Férias

53 - Pensão alimentícia - Férias

Ao forçar a incidência tributária, o valor informado irá sobrescrever a regra adotada pelo sistema conforme o [Mapeamento do evento S-1010](http://tdn.totvs.com/display/LRM/Evento+S-1010).

Obs: Apenas ficará disponível para marcação, caso o evento não possua nenhuma incidência relativa a IRRF.

 

# **Pasta RM Portal**

O objetivo desta pasta é permitir ao usuário definir quais eventos estarão disponíveis na entrada de dados do RM Portal.  
 

# **Pasta Gestão Educacional**

Esta pasta somente ficará visível quando utilizar integração com o RM Classis ou utilizar importação do movimento de ensino de sistema acadêmico de terceiros e o parâmetro 'Reprogramação salarial detalhada por Centro de Custo' existente em Opções | Parâmetros | RM Labore | Gestação Educacional está marcado.  
Deve ser cadastrada a fórmula que calcula o valor do evento relacionado informado no Salário Composto do funcionário.  
Para o cálculo do valor de um evento relacionado através de fórmula valor temos os seguintes passos:

* No salário composto do funcionário deve informar o evento relacionado. Sendo permitido cadastrar este evento sem preencher o valor, desde que tenha uma fórmula cadastrada conforme item acima.
* É utilizada a prioridade do cálculo de acordo com os eventos cadastrados no anexo 'Eventos Relacionados Reprogramação Salarial' do cadastro de eventos.
* O evento relacionado por fórmula é calculado no processo de Reprogramação Salarial quando os parâmetros 'Eventos relacionados' e 'Altera eventos relacionados editados ou cadastrados' são marcados.
* O evento cadastrado manualmente é identificado no módulo de Composição Salarial e somente é excluído manualmente.

**Contribuições RPPS/Regime Militar**

Este campo é utilizado para enviar o código de incidência da rubrica para as contribuições do Regime Próprio de Previdência Social - RPPS/regime militar, atender a geração da tag <codIncCPRP> no evento S-1010 do eSocial.

**Observação:** conforme MOS

Dica

Quando o Cadastro de Eventos é alterado, os envelopes de pagamento calculados anteriormente passam a ficar pendentes de recálculo.

Veja Seção IMPORTANTE sobre o Recálculo Automático do envelope no TDN do [Envelope de pagamento](https://tdn.totvs.com.br/display/public/LRM/Envelope+de+Pagamento)

# **Pasta eSocial**

### **De/Para de Eventos**

Essa aba tem como objetivo configurar o **de/para** dos eventos relacionados às férias na geração dos XMLs do eSocial, garantindo que as informações sejam enviadas corretamente, conforme as regras exigidas pelo governo, além de proporcionar maior visibilidade ao usuário.

Adicionalmente, essa aba centraliza todas as informações relacionadas ao eSocial, permitindo a gestão em um único local, de forma mais organizada e eficiente.

**Antecipação de Férias (Provento/Desconto):**

Para atender às recentes alterações normativas e atualizar as rubricas de férias, implementamos a funcionalidade **De/Para** diretamente no cadastro de eventos. Seguindo a lógica anteriormente utilizada no **Parametrizador (Configurações Gerais 6/7)**, o sistema substitui as verbas originais apenas durante a geração do XML. Isso garante a declaração correta da antecipação de férias e suas incidências exclusivas de IRRF, preservando integralmente os cálculos do recibo de férias. Abaixo o detalhamento dos eventos mapeados para realizar a vinculação no cadastro de eventos.

* + Evento Antecipação de Férias (Vencimento):

Essa verba será utilizada para envio dos valores da antecipação de férias para eSocial (leiaute S-1.0).

O valor gerado nessa verba será:

 evento com código de cálculo 38

 proventos sem código de cálculo e com incidência em INSS

 descontos sem código de cálculo e com incidência em INSS ou o código de cálculo 447 para verde amarelo.

**ATENÇÃO**:

A verba informada no campo acima deverá ser do tipo "Provento" e com incidência somente em IRRF de férias. 

Caso possua verbas de médias no recibo de férias essas também serão somadas as verbas de antecipação de férias.

* + Evento Antecipação Terço de Férias (Vencimento):

Essa verba será utilizada para envio dos valores da antecipação do terço de férias para eSocial (leiaute S-1.0).

O valor gerado nessa verba será:

 evento com código de cálculo 40

 evento com código de cálculo 310

**ATENÇÃO**: A verba informada no campo acima deverá ser do tipo "Provento" e com incidência somente em IRRF de férias.

* + Evento INSS Antecipação de Férias(Desconto):

Essa verba será utilizada para envio dos valores da provisão de INSS de férias para eSocial (leiaute S-1.0).

O valor gerado nessa verba será:

 evento com código de cálculo 82 e código de cálculo 130

**ATENÇÃO**: A verba informada no campo acima deverá ser do tipo "Desconto" e sem incidências. 

Importante!

Após a inserção da verba neste parâmetro, torna-se imprescindível gerar e enviar o XML S-1010 correspondente a essa verba. Essa etapa é fundamental para garantir a correta geração das tags **<codIncCP>** e **<codIncIRRF>**.

* + Evento Antecipação Primeira Parcela 13º nas Férias(Provento):

Essa verba será levada no S-1200 substituindo o valor do código de calculo 9 existente no envelope. 

O valor gerado nessa verba será:

 evento com código de cálculo 9

**ATENÇÃO**: A verba informada no campo acima deverá ser do tipo "Provento" e sem incidências em FGTS 13. 

* + Evento Salário Família Antecipação de Férias (Provento):

Essa verba será utilizada para envio dos valores da antecipação do salário família nas férias para eSocial.

O valor gerado nessa verba será:

 evento com código de cálculo 149

**ATENÇÃO:**A verba informada no campo acima deverá ser do tipo "Provento". 

**Envelope de Pagamento (Provento) / Envelope de Pagamento (Desconto)**

Substituindo o cadastro do **Parametrizador (Configurações Gerais 7/7)**, essas verbas vem para apresentar corretamente as incidencia INSS/FGTS e IRRF e liquido de férias, após ultima atualização sistemica  o sistema substitui as verbas ou complementa pelos novos eventos apenas durante a geração do XML.

**Lógica de Substituição:**

* **Preenchimento Parcial:** Caso seja informado apenas o evento de provento (ou apenas o de desconto), o sistema gerará o evento original acompanhado de seu respectivo par correspondente.
* **Preenchimento Integral:** Caso ambos os campos (provento e desconto) estejam preenchidos, o sistema desconsidera o evento original e reporta apenas os dois novos eventos parametrizados.

**Incidências eSocial**

Aqui é exibido as incidências que serão geradas no xml, trazendo facilidade e mais clareza para os cadastros do dia a dia.

**Natureza da Rubrica (eSocial):**

Informe nesse campo o código da rubrica para atender ao leiaute eSocial.

A Lista de Rubricas do eSocial está registrada conforme leiaute na "Tabela 03 - Natureza das Rubricas da Folha de Pagamento".

As Rubricas estão disponíveis em "Globais | Administração | Tabelas Dinâmicas", contexto "RH | Folha de Pagamento" identificada pelo código "NATRUBRICA".

          **Observação:**

          Esta é uma tabela fechada, ou seja, não é permitida a inclusão, edição ou exclusão de registros.

**Evento de Diferença de Salário Negativa (eSocial)**  
Preencher com o evento que será considerado na geração do S-1200 referente as diferenças desse evento.

Existem situações onde ao calcular a diferença salarial de um provento o valor recalculado ficará menor do que o valor pago anteriormente, neste caso o sistema lança o evento original com um valor negativo na tabela PFVERBASDIS, e esse valor será abatido nos demais proventos quando lançado no evento de diferença salarial (código de cálculo 37).

**Exemplo:**

Foi lançado o provento X001 com o valor de R$1.000,00, porém ao calcular a diferença salarial o valor correto seria R$800,00, neste caso o sistema lança na PFVERBASDIS o evento X001 com o valor de R$-200,00.

Porém, de acordo com o leiaute do eSocial referente ao evento S-1200, os valores pagos têm que ser discriminados em suas rubricas no cálculo da diferença salarial, e o valor da rubrica gerada no xml deve ser maior que zero. Para isso, foi implementado esse campo, onde o usuário poderá informar o evento correspondente.

No exemplo acima, o usuário deverá informar um evento correspondente com as mesmas incidências, porém de estorno.

**Exemplo:**

Informar um evento de desconto com as mesma incidências do X001, porém estornando, assim ao calcular a diferença salarial o sistema irá lançar o valor de R$200,00, e não irá lançar o evento X001 com o valor negativo.

**Observação:** 

* Quando o eventos for do tipo "Provento" deve ser informado evento do tipo "Desconto".
* Quando o eventos for do tipo "Desconto" deve ser informado evento do tipo "Provento".
* Quando o eventos for do tipo "Base" deve ser informado evento do tipo "Base".

**Atenção:**

1. O Evento de Diferença de Salário Negativo não poderá ser repetido em mais de um evento no cadastro de evento.
2. Esses eventos deverão ter a mesma incidência do original, exceto quando base de cálculo, que deverá ter sua incidência invertida.

**Exemplos:**  
Quando for um "Provento" com incidência em "INSS", deverá informar um "Desconto" com incidência em "Estorna INSS".  
Quando for uma "Base de Cálculo" com incidência em "INSS (Inc. Proventos)", deverá informar uma "Base de Cálculo" com incidência em "Estorna INSS (Inc. Descontos)".

**Importante:**

Para a liberação desse campo nas versões 12.1.22, 12.1.23 e 12.1.24 é necessário executar o script "LB.2019.04-03", disponível na central de downloads. 

**Compõe Teto Remuneratório (art.37,XI, da CF/1988)**  
Este campo é utilizado para atender a geração da tag <tetoRemun> no evento S-1010 do eSocial.

**Observação:** Será gerada somente quando a natureza jurídica do declarante for Administração Pública (grupo [1]).

**Mais informações**

Códigos de Cálculo

Eventos de Média  Base de Salário Composto

Eventos Relacionados Reprogramação Salarial

Processo de Suspensão de Incidência

Folha de Pagamento

**Veja também**

Copiar evento entre Coligadas   
[Rateio da folha do professor](http://tdn.totvs.com/pages/viewpage.action?pageId=271184164)
