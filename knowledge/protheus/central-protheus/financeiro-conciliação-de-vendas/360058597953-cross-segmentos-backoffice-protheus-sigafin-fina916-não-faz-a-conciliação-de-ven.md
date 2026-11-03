---
article_id: 360058597953
category: Financeiro - Conciliação de Vendas
content_hash: 2a8e306be790af9590076992968179c943cdcc381829cce782ca3916a7e38296
fetched_at: '2026-06-28T22:37:26.288496+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - FINA916 - Não faz a conciliação
  de vendas
type: support-article
updated_at: '2026-02-04T16:52:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058597953-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-FINA916-N%C3%A3o-faz-a-concilia%C3%A7%C3%A3o-de-vendas
---

**Dúvida**  
Não faz a conciliação de vendas.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA916 - A partir 12.1.27  
  
**Solução**

Verifique a chave de conciliação:

**FIF\_DTTEF = E1\_EMISSAO**  
**FIF\_PARALF = E1\_PARCELA**  
**FIF\_CODFIL = E1\_FILORIG**  
**FIF\_CODAUT = E1\_CARTAUT**  
**FIF\_NSUTEF = E1\_NSUTEF**  
**FIF\_TIPO = E1\_TIPO**

Ao localizar o registro, a chave completa é apresentada nas abas **Conciliado** e **Conciliado Parcialmente**.

A diferença entre as abas **Conciliado** e **Conciliado Parcialmente** está relacionada exclusivamente ao valor conciliado. Quando o valor líquido conciliado (**FIF\_VALLIQ**) for igual ao saldo do título (**E1\_SALDO**), o registro é exibido na aba **Conciliado**. Contudo, existe a **Tolerância em %** (**Margem**) configurada no parâmetro **F12** da rotina. Caso a diferença entre os valores esteja dentro dessa margem, o registro também será apresentado na aba **Conciliado**; caso contrário, será exibido em **Conciliado Parcialmente**.

**Exemplo:**  
Valor no FIF = 900 e valor no E1 = 1.000. Nesse cenário, o registro será exibido como **Conciliado Parcialmente**. Entretanto, se a tolerância percentual estiver configurada em 10%, o registro será exibido na aba **Conciliado**.

O campo de parcela informado pelas operadoras é tratado como numérico. No Protheus, esse campo é tratado como alfanumérico por meio do campo **FIF\_PARALF**.

O parâmetro **MV\_USAMEP** deve estar configurado como **.T.** quando houver utilização da tabela **MEP**. Caso não seja utilizada, a tabela MEP deve conter o valor **.F.**.

**Importante**  
Esta conciliação refere-se exclusivamente à conciliação de vendas. Não é realizada a baixa do título financeiro, ocorrendo apenas a confirmação da venda. O comportamento pode ser comparado à confirmação de entrada de títulos via CNAB, em que há somente a validação da informação, sem a efetiva liquidação do registro.

**Observação**  
A chave de relacionamento é composta pelos seguintes campos: Filial, Estabelecimento, NSU, Parcela, Data de Emissão, Código de Autorização, Tipo (“CD” – Cartão de Débito Automático ou “CC” – Cartão de Crédito Automático) e pela validação de que a diferença entre o valor da venda importada e o saldo do título no financeiro esteja dentro do percentual de tolerância configurado nas perguntas de processamento da rotina.

**Saiba Mais**

A conciliação de pagamentos é realizada pela rotina **FINA918**, por meio da importação de um novo arquivo de pagamentos disponibilizado pelas operadoras.

Consulte a documentação correspondente para mais detalhes.

[Conciliador Pagamentos e Vendas](https://tdn.totvs.com/display/public/PROT/Conciliador+Pagamentos+e+Vendas+-+Financeiro+%28Contas+a+Receber%29+-+P12)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096266694)

Clicando dentro do lay-ou, terá dois um para pagamento e outro para VENDAS

![](https://totvssuporte.zendesk.com/attachments/token/0rtkozkvCYORTgb5HDU2lSC4C/?name=inline-681999466.png)
