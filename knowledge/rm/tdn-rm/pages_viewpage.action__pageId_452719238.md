---
content_hash: 8998c0c66d2ccaf7db4284aededbd9f52acb71aa4469e7212e14f06e3df0c72e
fetched_at: '2026-06-29T00:10:04.709832+00:00'
page_id: '452719238'
product: rm
source: tdn-rm
title: Verificação da Base
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719238
version: 3
---

Este processo tem o objetivo de identificar as inconsistências encontradas na base de dados. Essas inconsistências serão definidas em dois niveis, sendo eles:

* Erros: Impossibilitam a execução de processos, senão gera inconsistências.
* Avisos: São pontos de atenção, mas não impossibilitam NECESSARIAMENTE a utilização do sistema  
    
  Para verificação de inconsistências na base de dados, será verificado o histórico de horários do funcionário, consistência de horários ativos, interseção de períodos, incompatibilidade de parâmetros com o cálculo por jornada e se considera ou não os funcionários demitidos.   
     
  Toda verificação será processada de acordo com a seleção de funcionários definida pelo usuário.  
     
  Para o parâmetro "Considera horários e sindicatos sem vínculo com funcionários" será feita a consistência conforme regra de negócio dos sindicatos/horários que não possuem funcionários associados. Além de gerar avisos dos horários/sindicatos que não estão associados a nenhum funcionário.  
  Esse parâmetro ajuda a evitar que alguns cadastros desnecessários continuem na base de dados.  
     
  **Observação**  
  Com esse parâmetro marcado, além das consistências realizadas conforme a seleção de funcionários definida pelo usuário será considerada também os horários que não tenham nenhum vínculo com quaisquer funcionários para verificação das informações conforme a regra de negócio. O mesmo se aplica ao sindicato.  
     
  Abaixo o detalhamento de cada item a ser considerado no processo de verificação da base de dados:  
     
  **Funcionário**   
  É verificado o histórico de horários dos funcionários quais funcionários estão com histórico nulo.  
  Se existir algum funcionário sem histórico preenchido, deverá ser gerado erro, pois impede o cálculo do sistema.  
  *No final da verificação: Erro*  
  *Será gerado erro por ausência de dados no cadastro do funcionário.*  
  *Inconsistências do histórico de horários dependem da intervenção do usuário para definir qual será o horário associado ao funcionário.*   
  **Observação**  
  *Caso seja um professor, tenha integração com o classis e considera o horário do classis não será gerado erro.*  
     
  Também será verificado se a seção atual do funcionário existe no histórico de seções.  
  *No final da verificação: Erro*  
     
  **Horários**   
  A consistência de horários valida informações em comum para todos os tipos de horários e valida também os dados específicos para cada tipo de horário. Na validação de informações comuns a todos os tipos de horários são validados:  
     
  Intervalos de compensado:  
  ·     Não pode existir interseção entre os intervalos de compensado com qualquer outro tipo de intervalo cadastrado (Descanso, Intervalos de batidas nula, Intervalos com tempo planejado, intervalos núcleo, intervalos da jornada planejada, intervalos de ausência planejada, intervalos de trabalho, intervalos núcleos e intervalos de limite de compensação de extras e atrasos).  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*  
     
  Intervalos de descanso:  
  ·     Não pode existir interseção entre os intervalos de descanso com qualquer outro tipo de intervalo cadastrado (Intervalos compensados, Intervalos de batida nula, Intervalos com tempo planejado, intervalos núcleo, intervalos da jornada planejada, intervalos de ausência planejada, intervalos de trabalho, intervalos núcleos e intervalos de limite de compensação de extras e atrasos).  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*
* Horário Rígido:  
               Intervalos de trabalhado:   
  ·     Horário rígido não pode existir intervalos com tempo planejado.  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*  
  ·     Não pode existir interseção entre os intervalos da ausência planejada com os  intervalos de trabalho.  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*  
  *Usuário deverá definir qual dos intervalos está correto e corrigir o outro.*  
  ·     Não permite intervalos de limite de compensação de extras e atrasos.  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*  
  ·     Não podem existir intervalos não compensáveis cadastrados.  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*
* Horário Flexível:  
              Intervalos de trabalho:  
  ·     Não pode haver interseção entre o intervalo com tempo planejado e o intervalo trabalhado.  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*  
  *Usuário deverá definir qual dos intervalos está correto e corrigir o outro.*  
  ·     Não podem existir intervalos não compensáveis cadastrados.  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*
* Horário Semi-flexível:  
              Intervalos de trabalho:  
  ·     Não pode existir intervalos não compensáveis cadastros.  
  *No final da verificação: Aviso*  
  *Será gerado aviso por excesso de informações cadastradas para esse tipo de horário.*  
     
  Na verificação de horários, além de informações dos tipos de horários com seus respectivos cadastros, será feita a validação também do tipo de horário definido no cadastro do funcionário em relação ao tipo de horário do próprio horário.  
  *No final da verificação: Aviso*  
  *Será gerado aviso, pois não impede o cálculo, mas pode gerar diferenças de valores.*  
  *Usuário deverá definir qual dos cadastros está correto.*  
     
     
  **Períodos**   
   A verificação da interseção de períodos consiste em validar se os períodos criados na base estão fazendo interseção com outros períodos. Conceitualmente para cada período criado no sistema, temos informações do período mensal, quinzenal e semanal.  
  Na verificação da interseção de períodos deverão ser considerados:
* Período mensal:  
  Na verificação do período mensal, é considerado o intervalo de início e fim do período se faz interseção com algum outro período mensal cadastrado.  
  *No final da verificação: Erro*  
  *Não impede a execução do recálculo, mas pode torná-lo inconsistente.*  
  *Usuário deverá definir qual dos intervalos está correto e corrigir o outro.*  
     
  *-* Período quinzenal:  
  Na verificação do período quinzenal, é considerado o intervalo de início e fim do período se faz interseção com algum outro período quinzenal cadastrado.  
  *No final da verificação: Erro*  
  *Não impede a execução do recálculo, mas pode torná-lo inconsistente.*  
  *Usuário deverá definir qual dos intervalos está correto e corrigir o outro.*  
     
  *-* Período semanal:  
  Na verificação do período semanal, é considerado o intervalo de início e fim do período se faz interseção com algum outro período semanal cadastrado.  
  *No final da verificação: Erro*  
  *Não impede a execução do recálculo, mas pode torná-lo inconsistente.*  
  *Usuário deverá definir qual dos intervalos está correto e corrigir o outro.*  
     
     
  **Parâmetros**   
  Atualmente  são feitas validações dos seguintes parâmetros do sindicato e do funcionário que possuem alguma inconsistência:
* Distribuição de extras:  
  Se o funcionário estiver parametrizado para realizar a distribuição de extras diária, é verificado se o sindicato associado também está parametrizado para distribuição diária.  
  *No final da verificação: Erro*  
  *Não impede a execução do recálculo, mas pode torná-lo inconsistente.*  
  *Usuário deverá definir o(s) parâmetro(s) correto(s) e corrigir o outro.*
* Banco de horas:  
  Quando o banco de horas está definido como diário e a distribuição das horas extras no sindicato está parametrizada para ser por período.  
  *No final da verificação: Erro*  
  *Impede a execução do recálculo.*  
  *Usuário deverá definir o(s) parâmetro(s) correto(s) e corrigir o outro.*
