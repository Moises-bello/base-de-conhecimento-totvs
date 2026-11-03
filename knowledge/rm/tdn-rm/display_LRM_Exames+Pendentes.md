---
content_hash: ae550ba178d5bc56c9f1c8c620bdcf1e6935d015bfd4ac816a719a939663d02d
fetched_at: '2026-06-29T00:10:06.051583+00:00'
page_id: '452719309'
product: rm
source: tdn-rm
title: Exames Pendentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Exames+Pendentes
version: 12
---

Por este cadastro é possível visualizar os exames pendentes que ainda devem ser realizados pela pessoa.

Os exames serão visualizados aqui de acordo com a definição do parâmetro **"Utilizar "Associação PPRA como origem na geração de exames pendentes"** como origem na geração dos exames pendentes" localizado em Opções| Parametrizador| Exames II:

Com o parâmetro **"Utilizar "Associação PPRA como origem na geração de exames pendentes"** **desabilitado**Perfis de Exame deverão ser associados a: Função, Seção e Lotação para geração dos exames pendentes.

Com o parâmetro **"Utilizar "Associação PPRA como origem na geração de exames pendentes"** **habilitado**os Perfis de Exame deverão ser associados a: Risco ou Nível de Risco, Reconhecimento e Avaliação de Risco, Pessoa para geração dos exames pendentes.

 **Atenção**

Caso o parâmetro **"Utilizar "Associação PPRA" como origem na geração dos exames pendentes"**estiver habilitado, através do parametrizador > Exames II,  a funcionalidade/parâmetro **Mudança de Risco Ocupacional - Quantidade de dias a considerar** estará disponível.

### 

Neste campo será definido o número de dias a considerar para remoção de um Exame Pendente do tipo Mudança de Risco Ocupacional após realização da consulta/exame.

Exemplo:

* + Existe um exame pendente do tipo Mudança de Risco Ocupacional apresentado nos anexos do funcionário.
  + No parametrizador está definido o número de dias como 30.
  + A data da geração do exame pendente é 20/06/2022.

Através do prontuário quando lanço a consulta e o exame com uma data até 30 dias antes da data em que o exame foi gerado como pendente (20/06/2022), o esse exame pendente será removido.

Caso a data de lançamento seja maior que 30 dias anteriores a data em que o exame pendente foi gerado,  o exame continuará como pendente até que um novo exame seja lançado para o funcionário com uma data que abranja o range

**OBSERVAÇÃO**:

Caso o campo "**Mudança de Risco Ocupacional - Quantidade de dias a considerar"** não seja preenchido, por default será considerado o total de 60 dias para validar se existe um exame realizado de **Mudança de Risco Ocupacional**para validação do exames pendentes.

**IMPORTANTE:**

Para que os exames pendentes sejam gerados corretamente e assim suas devidas datas de realização e atualização fiquem corretas, é **recomendado** que os exames pendentes dos funcionários sejam **gerados diariamente**.

Assim é garantida uma correta atualização dos exames e cadastros.

**Dica:**

Na linha RM existe uma forma de automatização de processos para execução. Para maiores informações basta acessar .

**Observação:**

* Os exames só deixarão de ser pendentes após terem sido cadastrados no Prontuário do Funcionário, estando na condição de Apto, e sua data de realização estiver válida conforme a periodicidade do mesmo.

O processo "Gerar Exames Pendentes" tem a finalidade de gerar no cadastro do funcionário, os exames a serem realizados e pode ser executado a qualquer momento pelo usuário do sistema.

A NR- 7 apresenta a seguinte informação:

"7.4.3.4.1. Para fins desta NR, entende-se por mudança de função toda e qualquer alteração de atividade, posto de trabalho ou de setor que implique a exposição do trabalhador ao risco diferente daquele a que estava exposto antes da mudança. ([{+}](http://www010.dataprev.gov.br/sislex/paginas/05/mtb/7.htm)<http://www010.dataprev.gov.br/sislex/paginas/05/mtb/7.htm+>) ".

Sendo assim, o processo de exames de mudança de função está diretamente relacionando com a mudança do perfil de exame no qual possuía um exame de tipo diferente expondo o funcionário e um novo risco.

O processo de Gerar Exames Pendentes pode ser automatizado pelo agendamento de processo utilizando o JobServer 3 camadas. Esse recurso só estará disponível quando o JobServer estiver configurado para executar em modo 3 Camadas. Para configurá-lo basta adicionar a seguinte configuração no arquivo: RM.Host.exe.config ou RM.Host.Service.exe.config:  
   
<?xml version="1.0" encoding="utf-8" ?> <configuration> <appSettings>  <add key="JobServer3Camadas" value="true"/> </appSettings> </configuration>  
   
   
**Campo 'Data prox. exame'**

A data do próximo exame será a soma da data do último exame do funcionário com a periodicidade da bateria de exame se:

* O exame na bateria de exame não possuir data de início de exigência (campos 'Exigido a partir de').
* Se a soma da data do último exame do funcionário com a periodicidade da bateria de exame resultar em uma data igual ou maior que a data de início de exigência da bateria.

Nos casos que não se encaixarem nos 2 itens acima, a data do próximo exame será a data de início de exigência da bateria de exame.

Maiores informações sobre a geração dos exames pendentes consulte:

**Funcionamento dos Exames Pendentes**

1) Verificação dos Perfis de Exames associados à Pessoa, de acordo com o tipo de associação realizada (Associação de Perfis de Exame e Associação no PPRA);

2) Com os Perfis de Exames selecionados são verificados os Exames que estão associados;

3) Serão considerados para verificação dos exames pendentes os seguintes Tipos de Exames:

* Exames Periódicos
* Exames Admissionais
* Exames Demissionais
* Exames de Retorno ao trabalho
* Exames de Mudança de Função

**OBSERVAÇÃO:** Para exames pendentes do tipo Retorno ao Trabalho, caso este retorno seja proveniente de afastamento de licença maternidade, este exame não será gerado como é regido para **NR-07 - Item 7.5.9**que afirmar que:

               "No exame de retorno ao trabalho, o exame clínico deve ser realizado antes que o empregado reassuma suas funções, quando ausente por período igual ou superior a 30 (trinta) dias por motivo de doença ou acidente, de natureza ocupacional ou não. "

 O sistema verifica se para cada Exame associado ao Perfil de Exames, e que se encaixe em alguma das cinco opções acima, já existe um exame realizado. Se o Exame não for encontrado no Prontuário da Pessoa ele será considerado como "Exame Pendente", mas, para que isto aconteça o tipo de exame ou o exame devem ser diferentes daqueles que se encontram no Prontuário da Pessoa. A exibição dos exames na pasta "Exames Pendentes" acontecerá conforme o fluxo:

Exames Admissionais:

    
  
   
Exames Demissionais:   
   
   
   
  
   
Exames de Retorno ao trabalho:  
   
   
   
  
   
Exames de Mudança de Risco Ocupacional:

    
   
Exames Periódicos
