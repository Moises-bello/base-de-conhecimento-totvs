---
content_hash: ebe0bdbcc70e1c2adf532f34724223490cac468e04f3da90bb870d9492952efe
fetched_at: '2026-06-29T00:10:31.904826+00:00'
page_id: '525011996'
product: rm
source: tdn-rm
title: Inclusão de bolsas retroativas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525011996
version: 5
---

---

O processo de bolsa retroativa é utilizado para instituições que desejam cadastrar bolsas para seus alunos depois que o lançamento já foi gerado e baixado.  
  
Processo para inclusão da bolsa retroativa:

*Acesse: Financeiro / Contábil > Assistentes > Incluir/Excluir bolsas retroativas.*

Na primeira etapa do assistente selecione o aluno, selecione o aluno e a opção de “Incluir” a bolsa retroativa.

Em seguida selecione a bolsa, serviço, parcela e percentual que serão inseridos e clique em “Adicionar”:

*Lembre-se de que essa parcela já foi gerada e baixada anteriormente pelo aluno.*

Avance e conclua o processo!

A bolsa é inserida no contrato do aluno:

Agora o aluno passou a ter um crédito de 500 reais. Esse valor já tinha sido pago anteriormente antes da inclusão da bolsa.

Para conferir acesse a conta corrente do aluno em *‘Anexos> Conta Corrente do aluno’*:

Para ser feito o aproveitamento deste valor, o financeiro poderá gerar um lançamento a pagar para o aluno com o valor do crédito da bolsa que foi cadastrada. Para que seja feito este processo, o cliente fornecedor tem que estar parametrizado como ambos no TOTVS Gestão Financeira.

Quer outra forma de aproveitar esse valor de 500 reais de Crédito?

Gere a parcela seguinte com o valor da bolsa de crédito, mas antes de gerar são necessárias configurações em ambos os sistemas:

Acesse: Parâmetros – TOTVS Gestão Financeira > 02.01.01.01 – Lançamentos: > Valores Opcionais.

Crie um valor Opcional, informe a ação como Descontar.

Acesse: Parâmetros do TOTVS Gestão Educacional > 15.05 – Integração > 15.05.03 – Financeiro > 15.05.03.01 Educacional > Fin - Vlrs. Opcionais/Integração 2/3.

Marque o parâmetro para ‘Efetuar operação com valor total na próxima mensalidade’ e informe se será controlado por valor opcional ou integração.

Nesse caso, geramos a 2ª parcela para o aluno. Ao selecionar o lançamento gerado e processar a baixa, ele identifica que o  possui um crédito na conta corrente:

O sistema efetua o desconto dos 500 Reais na baixa da parcela sequente.

Em caso do Valor no campo opcional ultrapassar o valor Original da parcela o valor restante fica para ser descontado na parcela seguinte.  
Exemplo : Valor C.Corrente = 1.100 Reais.  
Ao processar a baixa na 2º parcela, o valor líquido seria 0 (zero reais), porque foram subtraídos da conta corrente o valor de 1000 reais da parcela em questão. Restaram ainda 100 reais de crédito para a 3º parcela, que terá o seu valor líquido igual a 900 reais.
