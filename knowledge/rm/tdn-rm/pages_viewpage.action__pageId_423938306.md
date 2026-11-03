---
content_hash: 99a820fb80ede8e872f591914cf5743f53ccf68238c48fba8f9edfd155be38d2
fetched_at: '2026-06-29T00:09:26.503211+00:00'
page_id: '423938306'
product: rm
source: tdn-rm
title: Pré – Validador do SPED Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938306
version: 2
---

Este processo tem como função fazer uma pré-validação dos dados que serão gerados para a Escrituração Contábil Digital antes da geração propriamente dita do arquivo digital do SPED Contábil, indicando previamente inconsistências que seriam levantadas somente no momento em que os dados do arquivo digital fossem submetidos à validação pelo Programa Validador da Receita Federal. Desta forma, o tempo gasto na geração do SPED será otimizado, uma vez que os resultados das validações realizadas serão apresentados, com detalhamentos das regras validadas e orientações de procedimentos e possíveis soluções para ajustes dos dados inconsistentes.   
Antes de executar a pré-validação, os processos à seguir devem ser executados para garantir que os dados relacionados aos lançamentos estejam consistentes, o exercício contábil esteja corretamente encerrado, assim como as contas contábeis estejam corretamente associadas às contas paralelas.

* Consitência de Lançamentos
* Relatórios Balancetes/Balanço Patrimonial
* Validação da Associação do Plano Paralelo para o SPED Contábil  
     
  Feitos os passos anteriores, execute o Pré-Validador indicando os parâmetros corretamente. Atente-se aos parâmetros indicados, pois os dados da base serão analisados conforme estas indicações. Por exemplo, se a escrituração for Descentralizada os dados serão validados levando-se em consideração as informações existentes na base relacionadas à Matriz ou Filial Escriturada indicada. Da mesma forma, se Centralizada os dados serão validados levando-se em consideração os parâmetros seguintes informados para este tipo de escrituração. Atente-se também, neste caso, para Filtros de Filiais, pois a utilização destes implica em selecionar os dados a serem enviados. Lembre-se de que a utilização de Filtros de Filiais é de inteira responsabilidade da sua Empresa.  
     
  Caso necessite de informações à respeito dos parâmetros que deverão ser preenchidos, consulte o help do processo Gerar SPED Contábil, uma vez que os parâmetros aqui definidos devem ser os mesmos a serem usados na geração do SPED.  
     
  Os últimos parâmetros utilizados na Pré-Validação ficam gravados em memória. Desta forma, ao executar novamente o Pré-Validador os dados já virão preenchidos conforme a última execução, podendo, contudo ser alterados conforme sua necessidade.   
     
  A pré-validação deve ser executada para cada forma de escrituração a ser enviada para o SPED Contábil e os parâmetros indicados para a pré-validação devem ser os mesmos que serão utilizados no momento da Geração do SPED Contábil. No final da execução do Processo do Pré-Validador, os resultados das validações realizadas serão apresentados, com detalhamentos das regras validadas e orientações de procedimentos e possíveis soluções para ajustes dos dados inconsistentes. Se desejar, o resultado de cada validação executada poderá ser gravado em arquivo. Para isto, utilize o respectivo botão, localizado no canto esquerdo inferior da tela para Salvar o log. Existem no canto esquerdo inferior da tela, três botões com suas respectivas funções:
* Salvar o log da última execução em arquivo para que estes dados possam ser utilizados em futuras análises.
* Abrir um log anteriormente gravado para que este possa ser analisado.
* Retornar à tela da última execução do Pré-Validador.
