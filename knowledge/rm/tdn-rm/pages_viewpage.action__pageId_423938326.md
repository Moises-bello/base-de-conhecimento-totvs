---
content_hash: 238cc8dfc4311d393234eb9f3c6b1095f615b1281acc4dc0e31187db202067b5
fetched_at: '2026-06-29T00:09:26.591798+00:00'
page_id: '423938326'
product: rm
source: tdn-rm
title: Liberação de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938326
version: 17
---

Fracionamento de Job

A partir da versão 12.1.2310 este processo passou a oferecer suporte à execução multicoligada e ao Fracionamento de Jobs. Para utilizar o [Fracionamento de Jobs](https://tdn.totvs.com/display/public/LRM/Fracionamento+de+Jobs) é necessário adicionar a classe "**PatLiberaCompetenciaProc**" à configuração de segurança de jobs. Ao ativar o fracionamento e selecionar mais de uma coligada suas competências serão liberadas de acordo com o a quantidade de execuções simultâneas e o máximo de frações informadas.

**Dica:** O fracionamento da Liberação de Competência é realizado por coligada, ou seja, para obter ganho de performance o usuário deverá selecionar duas ou mais coligadas. Caso você deseje obter ganho de performance selecionando apenas uma coligada recomendamos que a opção "Executar Recálculo" permaneça desmarcada durante a execução do processo e, assim que a competência for liberada, o cálculo da depreciação seja realizado através do processo Calcular Cenário, existente no [Cadastro de Cenários](https://tdn.totvs.com/pages/viewpage.action?pageId=423938337).  O cálculo por cenário também oferece suporte ao Fracionamento de Jobs, porém, o fracionamento é realizado por patrimônio, tornando o cálculo mais rápido.

Tem como objetivo alterar o período de cálculo da base de dados bem como realizar o cálculo dos valores do patrimônio de forma a mantê-los atualizados de acordo com o período. Ou seja, a Liberação de Competência realiza a transposição de um mês de cálculo para o próximo mês, garantindo através de validações, que todas as informações referentes ao cálculo e sua contabilização, foram executados e estão apresentados sem qualquer problema evidente.

Exemplo: Patrimônios não baixados e estão sem cálculos, valores calculados e não contabilizados, aquisições não contabilizadas, etc.

O fechamento mensal do sistema aumenta o comprometimento dos usuário com os cálculos naquele determinado mês, promovendo ações de correção, ainda no próprio mês, e não mais no final do período como no modelo anterior.

A Liberação de Competência faz parte do desmembramento do antigo processo de Liberação de Período que conta também com o processo de Fechamento de Período.  
   
**Regras para Liberação de Competência:**

* Todas as ocorrências do período realizadas e seus valores conferidos.
* Todas as integrações do período (Notas, transferências, Aquisições...) do período realizadas.
* Todos os relatórios do período gerados e conferidos.
* Backup da base de dados realizado.
* Contabilização de aquisição (status "a contabilizar") pendente.

O sistema permite que o usuário tenha no máximo um período de 5 anos (60 meses) em aberto. Sendo assim, caso haja 60 meses em aberto será necessário realizar o processo de  para no mínimo um mês, feito isso será possível abrir uma nova competência.

**É extremamente importante que se faça um BACKUP da base de dados antes da execução do processo de Liberação de Competência.** **Se por algum motivo a liberação de competência não se completar deve-se verificar o log gerado ao final do processo, e se necessário restaurar imediatamente o BACKUP e iniciá-lo novamente.**

O serviço de Liberação de Competência possui uma parametrização de recalculo para patrimônios, onde os cálculos dos patrimônios são feitos para o novo mês de cálculo, para isso a opção "executar recálculo" deve estar marcada.

Exemplo: Ao executar o processo de liberação de janeiro para fevereiro os valores de fevereiro serão calculados e exibidos na aba cálculo razão do cadastro de patrimônios.

Caso esta opção não esteja marcada, o processo de cálculo de depreciação deverá ser executado manualmente.

Se existir patrimônios sem cálculo de depreciação/correção para o período de cálculo atual o sistema irá apresentar uma mensagem, solicitando o cálculo, a contabilização e a integração dos mesmos.  Desta forma o usuário será responsável por interromper a Liberação de Competência para realização destes procedimentos ou continuar.

Veja Também
