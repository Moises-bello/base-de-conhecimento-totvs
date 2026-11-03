---
content_hash: a82c8a80fc25f2dc42a5346a5d6a8dd738486bb0380faf37bb64c6f4f2e51352
fetched_at: '2026-06-29T00:12:03.592715+00:00'
page_id: '911862426'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Cálculos - Despesa Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911862426
version: 2
---

Na tela de **Fechamento**, ao executar o processo de **Apurar Condomínio** para o item de **Despesas Financeiras**, serão gerados registros que irão compor o valor total dos lançamentos referentes ao condomínio para a subunidade selecionada. Desta forma, todas as Despesas Financeiras associadas ao Fechamento calculado serão apuradas para a geração dos respectivos lançamentos.

Para o fácil entendimento do Cálculo de Despesas Financeira, vamos ver o seguinte exemplo:

O motor do portão de entrada do Shopping X parou de funcionar, dessa forma foi necessário solicitar o serviço de um técnico para o seu conserto. O serviço custou R$ 2.000,00 e terá que ser rateado para todas as Lojas.   
Para este exemplo, terá que ser realizado o cadastro de Fechamento para calcular essa despesa. Após isso, deverá ser associado ao Fechamento uma Despesa Financeira, onde será inserido o(s) Lançamento(s) a Pagar no qual(is) representa o pagamento do serviço do conserto do motor do portão. Na Despesa Financeira, poderá ser escolhida a forma de rateio do valor do serviço, as opções são:

* [Valor Fixo](http://tdn.totvs.com/pages/viewpage.action?pageId=435105104)
* [Rateio por CRD](http://tdn.totvs.com/pages/viewpage.action?pageId=435105196)
* [Rateio por Fração Ideal](http://tdn.totvs.com/pages/viewpage.action?pageId=435105183)
* [Rateio por M² Construído](http://tdn.totvs.com/pages/viewpage.action?pageId=435105299)
* [Rateio por M² Locado](http://tdn.totvs.com/pages/viewpage.action?pageId=435105202)
* [Rateio Linear por Total de Subunidade do Empreendimento](http://tdn.totvs.com/pages/viewpage.action?pageId=435105092)
* [Rateio Linear por Total de Subunidade da Unidade](http://tdn.totvs.com/pages/viewpage.action?pageId=435105215)
* [Rateio Linear por Total de Subunidades](http://tdn.totvs.com/pages/viewpage.action?pageId=435105093)

No exemplo citado, o rateio ideal seria "Rateio Linear por Total de Subunidade do Empreendimento", no qual será dividido o valor do serviço para todas os apartamentos.   
No cadastro de Despesa Financeira, temos como campo obrigatório o Item de Cobrança, no qual é utilizado para compor o valor do lançamento a ser gerado , pois no cadastro de Itens de Cobrança existe um espaço para associar um ou mais **Valores de Integração**. Lembrando que os registros de Valores de Integração tem origem no **TOTVS Gestão Financeira.**  
Após realizar o processo de Calcular Fechamento, serão gerados os registros para cada subunidade selecionada no cálculo, com o valor rateado conforme o modelo de cálculo acima.  
Cada subunidade que fez parte da apuração terá um registro calculado no anexo Apurações do Condomínio, bem como seus valores já rateados.

ObservaçãoO valor considerado no processo, será tratado conforme o status do(s) lançamento(s) a pagar da(s) Despesa(s) Financeira, segue mais detalhes:

* **Lançamento em Aberto:** Será calculado com o valor corresponde a data de execução do processo. Dessa forma o lançamento estando em atraso serão incluídos encargos financeiros, tais como multa e juros mora;
* **Lançamento Parcialmente Baixado:** Será calculado o valor já baixado mais o valor correspondente a data da execução do processo do restante do lançamento. Dessa forma o lançamento estando em atraso serão incluídos encargos financeiros, tais como multa e juros mora;
* **Lançamento Baixado:** Será calculado com o valor baixado lançamento. Caso o lançamento foi pago em atraso, gerando encargos financeiros, esses serão calculados pelo processo;

Lembrando que para criar registros de Despesa Financeira, basta acessar **Menu de Condomínio / Fechamento Individualizado/ Anexo Despesa Financeira** do **TOTVS Incorporação**.

Veja Também

**Considerar despesas anteriores no fechamento**

O processo de **Apurar Condomínio** considera as despesas de períodos anteriores que não tenham sido calculadas ou integradas no fechamento de sua competência. Todas as despesas em aberto anteriores à competência do fechamento devem ser consideradas.

Exemplo:Caso alguma subunidade do fechamento na competência de 01/2018 já esteja com seu status Calculado ou Integrado, quando o usuário cadastrar alguma despesa de reserva para esta competência (01/2018), ao salvar esta despesa, ele receberá a seguinte mensagem:  
"Você está incluindo uma reserva para uma competência que já possui o Fechamento calculado ou integrado. Se preferir continuar o cadastro, a reserva somente será considerada para esse Fechamento se for realizado o Recalculo, caso contrário será calculada em um próximo Fechamento. Deseja continuar com a inclusão da reserva?"  
Desta forma, caso o usuário realize o recalculo no fechamento com competência em 01/2018, a despesa inserida será vinculada ao fechamento. Porém caso o usuário realize o cálculo do fechamento de uma competência superior (Exemplo: 02/2018), então esta despesa de reserva será vinculada à este fechamento.
