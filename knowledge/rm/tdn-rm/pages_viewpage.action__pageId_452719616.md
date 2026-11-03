---
content_hash: bfcdc9f19c2a65a82453779ace35bdb3680c2f780363b35f716fc2146b06cb13
fetched_at: '2026-06-29T00:10:08.969663+00:00'
page_id: '452719616'
product: rm
source: tdn-rm
title: Código de Cálculo 315 – Base de FGTS de Afastados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719616
version: 4
---

Evento Base de Cálculo e com incidência em FGTS obrigatória.  
   
Este código de cálculo foi criado com o objetivo de facilitar a composição da **Base de FGTS** do Funcionário afastado por **Acidente de Trabalho(T) e** **Doença Ocupacional(O).**  
   
O lançamento do evento para o Envelope de Pagamento é automático e realizado no momento do lançamento dos códigos de cálculos **1-Horas Normais, 2-Dias Trabalhados** ou **145-Atestado Médico**, quando identificado que o funcionário possui o afastamento registrado no mês corrente.  
   
**Atenção:**  
Caso o evento com código de cálculo **1-Horas Normais, 2-Dias Trabalhados** ou **145-Atestado Médico** possua fórmula, o sistema não lança o evento com código de cálculo 315 automaticamente, o usuário deve lançar através do grupo de eventos ou diretamente no envelope do funcionário.   
   
Lembrando que, o valor do código de calculo 315 é calculado automaticamente, somente o lançamento do evento deve ser manual.  
   
Quando no momento da geração do SEFIP ou da GRRF não existir o evento com código de cálculo 315 no envelope do funcionário (afastado por Acidente de Trabalho e Doença Ocupacional) o sistema realiza o cálculo da base de FGTS para geração destes processos, porém não lança o evento com código de cálculo 315 no envelope. Fica a cargo do usuário o lançamento deste evento no envelope do funcionário.   
O usuário deve ficar atento para que não haja incoerência entre as bases de FGTS do SEFIP e do envelope do funcionário.  
   
Como este código de cálculo é obrigatório para os funcionários afastados por Acidente de Trabalho e Doença Ocupacional, caso no processo de Liberação de Competência o evento é automaticamente inserido no envelope do funcionário e como 'Data de Pagamento' o sistema utiliza a informação contida em Configurações | Parâmetros | Parametrizador | Folha de Pagamento | Configuração de Competência.  
   
A não existência do evento com código de cálculo 315 no cadastro de eventos ocasiona no impedimento da liberação de competência.   
Neste caso, o sistema informa que o evento deve ser cadastrado, abortando o processo.   
   
Para funcionário de código de recebimento P-Professor Horista, quando o parâmetro 'Calcula Salário Considerando Movimento de Ensino' existente em Configurações | Parâmetros | Parametrizador | Integrações | Gestão Educacional estiver marcado não é realizado o lançamento automático deste código de cálculo, devendo o mesmo ser lançado manualmente no movimento.  
   
Para empresas que utilizam **Tomadores de Serviços**, no ato do cadastramento do afastamento pode ser informado o código do tomador desejado, e neste caso o comportamento do sistema é da seguinte maneira:  
   
Para funcionário que possui mais de um afastamento no mês, caso o tomador não seja informado no afastamento, o rateio é realizado de acordo com a lotação do funcionário na Obra/Construção Civil. Caso seja informado o tomador de pelo menos um dos afastamentos, o rateio é realizado de acordo com a parametrização do afastamento.   
   
**Exemplo:**  
Afastamento de 01/06 a 16/06 sem tomador informado  
Afastamento de 18/06 a 20/06 sem tomador informado  
Afastamento de 22/06 a 30/06 com tomador informado  
   
O sistema considera os dois primeiros afastamentos acima para a Empresa, e apenas o último afastamento para o Tomador, mesmo que o funcionário esteja locado os 30 dias. Somente se nenhum dos afastamentos possuír Tomador informado é que o rateio é realizado de acordo com os dias locados do Cadastro do Funcionário, e o evento de CC315 deve estar parametrizado para Seguir Rateio por Tomador.  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
