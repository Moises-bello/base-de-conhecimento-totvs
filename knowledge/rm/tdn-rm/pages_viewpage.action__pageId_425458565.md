---
content_hash: 464119b8987a980c6fc96ada027fb3c2bed5b1a1beba418168ec1a6245b901d2
fetched_at: '2026-06-29T00:09:30.925370+00:00'
page_id: '425458565'
product: rm
source: tdn-rm
title: Confirmação de matrícula por pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458565
version: 23
---

O objetivo de executar o processo de Confirmação de Matrícula é automatizar a validação do pagamento de uma ou várias parcelas do contrato de um aluno ou vários alunos.

É comum a seguinte situação: Aluno faz matrícula nas disciplinas do próximo período letivo. Entretanto, não efetua o pagamento da 1ª parcela (referente à matrícula). Sendo assim, a instituição de ensino não permite que seja efetivada a matrícula daquele aluno enquanto não realizar o pagamento da primeira parcela.

Este processo permite que as instituições façam o gerenciamento das parcelas dos alunos para a realização da matrícula.

Acesse: Matrícula e Avaliação | Matrícula  | Mais... | ***Confirmação de matrícula por pagamento***

Será aberta uma tela de filtro, selecione para quais alunos o processo será executado.

Após selecionar os alunos, é necessário informar qual parcela e cota serão analisadas, bem como a situação de matrícula que será alterada no período letivo, além do motivo de alteração, dada às condições de parcela baixada (FLAN. STATUSLAN = 1) ou parcela não baixada (FLAN. STATUSLAN <> 1).

**Exemplo de aplicação:**

Tenho um aluno e desejo validar o status dos lançamentos da parcela 1 e cotas 1,2 e 3.

Se a parcela 1 tem 3 cotas e dessas cotas o aluno pagou 2 e a terceira ainda vencerá, o sistema confirmará a matrícula desse aluno pois esse boleto em questão ainda não venceu. Para se obter o comportamento esperado, de forma que o sistema não confirme a matrícula do aluno, seria necessário que as datas de vencimento dos lançamentos vinculados a parcela estivessem vencidas no momento da execução do processo de confirmação de matrícula.

A tela permite que sejam feitos filtros para seleção dos alunos por consulta SQL, seleção de matriz aplicada ou até mesmo um único aluno.

Este processo possui os seguintes parâmetros para a alteração da situação de matrícula:

* **Verificar o comportamento da inadimplência da bolsa de crédito**

  Ao habilitar este parâmetro, a confirmação da matrícula passará a considerar a configuração da bolsa de crédito na validação de inadimplência do aluno.

  + **Quando a bolsa de crédito do aluno estiver configurada para “Verificar inadimplência do outro sacado”**: o sistema verificará se os lançamentos do outro sacado da bolsa de crédito estão baixados antes de permitir a confirmação da matrícula.
  + **Quando a bolsa de crédito do aluno não estiver configurada para “Verificar inadimplência do outro sacado”**: o sistema não realizará a validação sobre os lançamentos do outro sacado e confirmará a matrícula, desde que os demais lançamentos do filtro aplicado estejam em conformidade.

  Caso o parâmetro esteja **desabilitado**, todos os lançamentos do aluno — **relacionados ou não à bolsa de crédito** — serão verificados de acordo com o filtro aplicado no processo.

* **Alterar data da matrícula conforme data do pagamento**

Ao habilitar este parâmetro, a data da matrícula assumirá o mesmo valor da data de pagamento na confirmação da matrícula.

* **Verificar assinatura do contrato**

Ao habilitar este parâmetro, a confirmação da matrícula será feita somente para alunos que possuam contratos assinados que não estejam cancelados e sejam do tipo plano.

***Exemplo:***Para os alunos que efetuaram o pagamento da 1ª parcela a matrícula será confirmada e a situação alterada para 'Cursando'. Aqueles que não efetuaram o pagamento,  por ora, terão sua matrícula pendente e a situação alterada para 'Pré-matriculado'.

Ao avançar o processo é necessário selecionar qual serviço será verificado durante a execução da rotina. É usual que o serviço avaliado neste caso seja 'Matrícula'.

A partir da versão **12.1.2402,** para alterar a situação de matrícula para **alunos com parcela baixada**, o processo irá verificar se há pelos menos um pagamento registrado na parcela, cota e tipo de serviço selecionados.

Já para alterar a situação de matrícula para **alunos com parcela não baixada**, o processo irá verificar se a parcela da cota e tipo de serviço selecionados está vencida.

A situação de matrícula do aluno só será alterada caso atenda a esses critérios.

***Observação:*** *lembre-se de que podemos ter a mesma parcela para serviços distintos.*

Execute o processo após a seleção do serviço a ser validado.

Após a execução será apresentado um log, que apresentará os registros modificados.

Os alunos terão suas situações alteradas conforme o pagamento (ou não) da parcela/serviço validado.

Outra possibilidade de realizar a rotina é através agendamento do processo, afim de determinar qual é a sua periodicidade de execução , quando se utiliza o ambiente em n camadas.

Caso queira realizar o fracionamento de jobs, acesse: 

Ambiente | Processos | Segurança de Jobs Fracionáveis
