---
content_hash: 59f75bca79ec074ba5a01fd6d1291f2639602e8e38efc3550348b3d77094993a
fetched_at: '2026-06-29T00:09:33.847671+00:00'
page_id: '425459064'
product: rm
source: tdn-rm
title: Cálculo do valor do Contrato X Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459064
version: 9
---

---

O valor total financeiro de um contrato se dá através da soma de suas parcelas, porem, o valor do contrato a ser contabilizado pelo regime de competência, algumas vezes, pode não corresponder ao valor financeiro, devido ao *tipo de parcela* que o compõe e até mesmo ao tipo de *serviço* vinculado à parcela.

Por definição interna do sistema, somente as parcelas do tipo '**Parcela do Plano**' farão parte do cálculo do valor total do contrato a ser contabilizado pelo regime de competência.   
Parcelas do tipo '**Parcela** ***Extra***' e do tipo '**Parcela** ***Adicional***' somente entrarão no cálculo e farão parte da contabilização dos contratos se o sistema estiver parametrizado para considerar tais parcelas no processo de contabilização. Se quiserem considerar estas parcelas na contabilização dos contratos, marquem os parâmetros '***Contabiliza parcela do tipo Extra***' e '***Contabiliza parcela do tipo Adicional***' disponíveis em *Ambiente | Parâmetros | TOTVS Educacional | Integração | Contabilidade,* caso contrário, somente as parcelas do tipo '*Parcela do Plano*' farão parte do cálculo do valor total do contrato a ser contabilizado pelo regime de competência.

Além disso, somente os serviços vinculados às parcelas que tiverem o campo "**Compõe contabilização por competência**" marcado entrarão no cálculo para a contabilização.

**Exemplo:**  
Vamos supor que o contrato do aluno possui:

* 6 parcelas do tipo '*Parcela do Plano*' para o serviço 'Mensalidade' no valor de 2.000,00 cada uma.
* 1 parcela do tipo '*Parcela do Plano*' para o serviço 'Seguro' no valor de 50,00.
* 1 parcela do tipo '*Parcela Extra*' para o serviço 'Mensalidade' no valor de 500,00.
* 1 parcela do tipo '*Parcela Extra*' para o serviço 'Material coletivo' no valor de 150,00.
* o serviço 'Mensalidade' possui o campo "*Compõe contabilização por competência*" marcado.
* o serviço 'Seguro' possui o campo "*Compõe contabilização por competência*" desmarcado.
* o serviço 'Material coletivo' possui o campo "*Compõe contabilização por competência*" desmarcado.
* os parâmetros '*Contabiliza parcela do tipo Extra*' e '*Contabiliza parcela do tipo Adicional*' estão desmarcados.

=> o total Financeiro deste contrato será = R$ 12.650,00  
=> o total a ser contabilizado pelo regime de competência será = **R$ 12.000,00**, pois irá considerar somente as 6 parcelas do tipo '*Parcela do Plano*' para o serviço '*Mensalidade*' no valor de 2.000,00 cada uma. As parcelas do tipo '*Extra*' não entrarão neste cálculo, pois o sistema está com o parâmetro '*Contabiliza parcela do tipo Extra*' desmarcado, além disso somente o serviço 'Mensalidade' possui o campo "*Compõe contabilização por competência*" marcado.

Quando o contrato do aluno possuir **descontos** aplicados às parcelas, o valor do desconto contabilizado do contrato será registrado na tabela SCONTRATO, no campo DESCONTO. Se ocorrer um aumento ou redução desse valor em algum momento, ao realizar uma nova contabilização, o campo DESCONTO será atualizado refletindo o novo valor.

Quando houver estorno total da contabilização, o valor desse campo será atualizado para zero.
