---
content_hash: d82ab4a011ffac3c9e0ac27082861f6acec7b2f5c3a9e6e11275c5612119ad50
fetched_at: '2026-06-29T00:08:15.885859+00:00'
page_id: '244926388'
product: rm
source: tdn-rm
title: Embasamento Contábil / Normas Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244926388
version: 1
---

|  |  |
| --- | --- |
| Descrição | Normas Contábeis |
| Observações | Será apresentada toda norma contábil utilizada na criação do recurso. |

**Aderência a Norma Brasileira Contábil**

|  |
| --- |
| *“36.Os arrendadores devem reconhecer os ativos mantidos por arrendamento mercantil financeiro nos seus balanços e apresentá-los como conta a receber por valor igual ao investimento líquido no arrendamento mercantil. “* |

A contabilização do imóvel como ativo deve ser feita manualmente no sistema contábil adotado.Já as contabilizações das operações de locação ou arrendamento serão geradas automaticamente pelo TIN conforme parametrização da coligada.

 Se o imóvel for 100% próprio deve gerar a contabilização de reconhecimento no Ativo conforme Valor Total Venal ou valor de Custo, se o imóvel for parcialmente próprio deve ser contabilizada apenas sua proporção sobre o valor venal.

 As contas contábeis e naturezas de cada ativo será determinada pelo evento contábil que deve ser parametrizado pelo usuário.

|  |
| --- |
| *“37.Num arrendamento mercantil financeiro, riscos e benefícios inerentes à propriedade legal são substancialmente transferidos pelo arrendador e, portanto, os pagamentos do arrendamento mercantil a serem recebidos são tratados pelo arrendador como amortização de capital e receita financeira para reembolsá-lo e recompensá-lo pelo investimento e serviços.”* |

A amortização deve ser parametrizada no Evento Contábil (lançamento Padrão no Protheus) relacionado a baixa (pagamento) de cada parcela, portanto não sofrerá tratamento no TIN.

**Custos Diretos Iniciais**

*“38.         Os **custos diretos iniciais são muitas vezes incorridos** por parte dos arrendadores e incluem valores como **comissões**, **honorários** legais e custos internos que sejam incrementais e diretamente atribuíveis à negociação e estruturação do arrendamento mercantil. Esses custos excluem gastos gerais como aqueles que são incorridos por equipe de vendas e marketing. Para arrendamentos mercantis financeiros que não sejam os que envolvem arrendadores fabricantes ou comerciantes (quando isso for permitido legalmente), os custos diretos iniciais são incluídos na mensuração inicial da conta a receber de arrendamento mercantil financeiro e reduzem o valor da receita reconhecida durante o prazo do arrendamento mercantil. A **taxa de juros** implícita no arrendamento mercantil é definida de tal forma que os custos diretos iniciais são automaticamente incluídos na conta a receber de arrendamento mercantil financeiro e não há necessidade de adicioná-los separadamente. Os custos incorridos pelos arrendadores fabricantes ou comerciantes relacionados com a negociação e a estruturação de um arrendamento mercantil estão excluídos da definição de custos diretos iniciais. Como resultado, os referidos custos são excluídos do investimento líquido no arrendamento mercantil e são reconhecidos como despesa quando o lucro da venda for reconhecido. Normalmente, em um arrendamento mercantil financeiro, esse lucro é reconhecido no começo do prazo do arrendamento mercantil.”*

Somente as comissões poderão ser tratadas pelo sistema quando da sua geração, em tempo de projeto deve ser avaliado como a comissão contabilizar, se linear ou não, já que o valor pode desaparecer no período do contrato (contrato longo).

**Reconhecimento da Receita**

*“39.         O reconhecimento da receita financeira deve basear-se em modelo que reflita a **taxa de retorno periódica constant**e sobre o investimento líquido do arrendador no arrendamento mercantil financeiro.”*

Nas demonstrações deve ser apresentado os valores por períodos

* Até um Ano;
* Mais de um ano e até cinco anos;
* Mais de cinco anos;

*“50.         A receita de arrendamento mercantil proveniente de arrendamentos mercantis operacionais deve ser reconhecida na receita em **base linear durante o prazo do arrendamento mercantil,** a menos que outra base sistemática seja mais representativa do modelo temporal em que o benefício do uso do ativo arrendado seja diminuído.*

*51.          Os custos, incluindo a depreciação, incorridos na obtenção da receita de arrendamento mercantil são reconhecidos como despesa. **A receita de arrendamento mercantil** (excluindo recebimentos de serviços proporcionados tais como seguro e manutenção) **é reconhecida em base linear durante o prazo do arrendamento mercantil mesmo se os recebimentos não forem em tal base,** a menos que outra base sistemática seja mais representativa do modelo temporal em que o benefício de uso do ativo arrendado seja diminuído.**”*

Os custos não serão reconhecidos pelo TIN. A contabilização Linear será gerada pelo TIN conforme processo relacionado.

Referente ao item 53: depreciações deverá ocorrer no módulo de patrimônio do sistema (RM ou Protheus).

 O TIN não possui recursos de identificação de *Leaseback* como um pacote fechado e neste caso caberá ao usuário identificar as contas contábeis apropriadas para atender a locação de Imóvel que represente a operação de leaseback não tendo nenhuma relação direta com contrato de empréstimo tendo como garantia o imóvel, ou suas operações adjacentes. As demais operações fora o contexto do contrato de locação devem ser feitas manualmente ou por recursos diferentes do TIN.
