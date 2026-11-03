---
content_hash: 5d3a1693ef6aa7ea1e24188332afb8407ba27cbb1308604682de16ff616be505
fetched_at: '2026-06-29T00:08:44.564422+00:00'
page_id: '309041231'
product: rm
source: tdn-rm
title: RMCTB009_Apuração Virtual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309041231
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Apuração Virtual |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo:**  O presente processo atende às exigências da Escrituração Contábil Fiscal para empresas tributadas pelo Lucro Real ou Presumido com levantamento de balanço anual a fim de que o validador consiga identificar os encerramentos trimestrais e não gere erros na validação do bloco K. Podemos utilizá-lo também para avaliações gerenciais, quando o período de encerramento realizado no TOTVS Gestão Contábil não coincide com o encerramento previsto na legislação.    **Regras Gerais:**  A parametrização básica do processo está vinculada ao cadastro das contas de prejuízo e lucro do período, bem como dos grupos de despesa e receita, conforme cadastrado no plano de contas contábeis.    **Parametrização Necessária:**  1 - Acesse o caminho Escrituração Contábil/Apuração Virtual e informe os dados necessários para que o sistema execute o processo, principalmente as contas de lucro/prejuízo, bem como os grupos de contas que serão apurados. Confira nas figuras abaixo:          Em destaque os principais dados a serem informados:        2 - Cadastrados os dados acima, o processo já pode ser executado, sendo que deve ser informado o período que será apurado, podendo ser executado o processo apenas quando este não for utilizado na ECF, sendo que neste caso, somente é possível executar a simulação do processo.        3 - Após a execução do processo o sistema mostra o resultado apurado por período, conforme cadastrado na tela anterior.      **Validação:**  Caso exista algum lançamento manual realizado para conta de lucro ou prejuízo , ou seja, lançamento que o próprio usuário criou para a conta em função de alguma apuração manual ou ajuste, o mesmo será somado ao valor processado pela apuração virtual e será apresentada a mensagem abaixo no LOG  Registro K155 |Apuração Virtual |Identificamos que existe movimentação que não é de encerramento para a conta “{0}” no período de {1} á {2}, e a ECF Contábil esta parametrizada para executar a apuração virtual, esta situação poderá resulta em advertências no PVA.  Normalmente esta situação ocorre quando o usuário executa a apuração do lucro/prejuízo manualmente e realiza o lançamento, sugerimos que este processo seja realizado automaticamente pelo processo de Transferência de Grupos Contábeis ou que o lançamento realizado manualmente seja identificado por um histórico de fechamento |
| **Observações:** | Este processo só deve ser utilizado quando o período da Apuração de Resultado informado no processo de Transferência de Grupos Contábeis não for o período a ser levado para a Escrituração Contábil Fiscal (ECF), caso seja, não será preciso executar a Apuração Virtual. |
