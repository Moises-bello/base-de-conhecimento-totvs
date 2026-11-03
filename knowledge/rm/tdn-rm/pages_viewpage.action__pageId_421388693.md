---
content_hash: 0abc5af2eef12f4ef3de5886383d8d4795969327891bfc799417c6347c5e8893
fetched_at: '2026-06-29T00:09:18.440142+00:00'
page_id: '421388693'
product: rm
source: tdn-rm
title: Aba Efetivação - Template
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388693
version: 8
---

**Efetivação do Acordo**

O objetivo da efetivação do acordo é concretizar no sistema a conclusão da execução do processo e a realizar a inclusão de registros referente ao acordo gerado.  
A forma de efetivação pode ser definida por regras, cada regra gera resultados diferentes na execução do processo, são elas:

Ao aprovar  
O acordo será efetivado somente após aprovação.  
Será gerado o acordo no sistema, porém o mesmo aguarda que a aprovação seja realizada conforme definida a forma no campo "Utilizar Aprovação".  
Após a aprovação, a baixa por acordo do lançamento de origem é processada e as parcelas (lançamentos) desse acordo serão geradas no sistema.

Ao Criar  
O acordo será efetivado ao concluir a execução do processo "Gerar Acordo".  
Assim que concluído a execução do processo de acordo as parcelas (lançamentos do acordo) serão geradas instantaneamente no sistema.

Ao Pagar primeira parcela  
O acordo será efetivado somente após a quitação (baixa) da primeira parcela gerada no sistema.  
O acordo é gerado e a primeira parcela (lançamento) desse acordo é inserida no sistema. Quando realizada a quitação (baixa) desse lançamento, o sistema vai gerar as demais parcelas (lançamentos) do acordo e o mesmo será efetivado.

Obs: Essa regra de efetivação do acordo tem o objetivo de diminuir a quantidade de lançamentos gerados no sistema quando o acordo não é honrado ou seja enquanto o cliente não realizar o pagamento da primeira parcela. O sistema não gera os lançamentos do acordo e também não permite que seja gerado novo acordo para esse Cli/For. O sistema barra a inclusão de novo acordo apresentando a seguinte mensagem:

"Cliente/Fornecedor x-xxxxx possui um ou mais acordos financeiros não efetivados. É necessário efetivá-los antes de gerar novos".  
Caso seja necessário gerar novo acordo o anterior poderá ser cancelado.

**Utilizar Aprovação**  
Caso o acordo necessite de aprovação é possível definir se será usada ou não a aprovação.

Não utiliza  
Não será solicitada aprovação.

Aprovação Simples  
Será executada via processo na visão de Acordo por usuário que tenha permissão no Menu.

Work Flow CRM  
Nesse caso será preciso preencher os campos de "Integração com o Módulo CRM".

**Obter aceite dos Termos do Acordo**  
Quando marcada a opção será necessário informar relatório para obter aceite da proposta de negociação, será apresentado os dados do Acordo.

**Status do Acordo**  
O controle, verificação do status e demais campos pode ser realizado através da tabela FACORDO.

Em Aberto  
Acordo criado, mas ainda não passou pelo processo de aprovação / efetivação.

Reprovado  
Quando o template faz controle de aprovação indica que o acordo não foi aprovado.

Não Efetivado  
Indica que o acordo gerado foi cancelado.

Efetivado  
Indica que o acordo gerado foi gerado.

 Informações Complementares

* [Aprovação via Workflow](http://tdn.totvs.com/x/L_EdGQ)
