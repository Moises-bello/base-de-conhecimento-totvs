---
content_hash: 7a8ebd3fd1cbb7196a4cdea08ab165f78eb36f300ef7390713339b3d3efe242d
fetched_at: '2026-06-29T00:09:53.771327+00:00'
page_id: '441820361'
product: rm
source: tdn-rm
title: Portaria CAT 42/2018
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=441820361
version: 22
---

Em 22/05/2018 o Governo Estadual de SP, publicou a [Portaria CAT 42/2018](https://portal.fazenda.sp.gov.br/servicos/st/Paginas/Ressarcimento-de-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria-do-ICMS.aspx), que instituiu um novo método para o Sistema de Ressarcimento ou Complemento do ICMS Retido por Substituição Tributária.

A Portaria CAT 42, estabelece as regras e procedimentos deste novo método a serem executadas por contribuintes de ICMS que receberam mercadorias sob o regime de substituição tributária e que por motivo qualquer não tenham o fato gerador do imposto cobrado antecipadamente concluído.

**Registros**

O arquivo será composto dos seguintes registros:

* Registro 0000 - Abertura do Arquivo Digital e Identificação do Contribuinte
* Registro 0150 - Tabela de Cadastro do Participante
* Registro 0200 - Tabela de Identificação do Item
* Registro 0205 - Código Anterior do Item (não obrigados ao SPED)
* Registro 1050 - Registros de Saldos em Estoque
* Registro 1100 – Registro de Documento Fiscal Eletrônico para Fins de Ressarcimento de Substituição Tributária – SP
* Registro 1200 – Registro de Documento Fiscal não-eletrônico para fins de Ressarcimento de Substituição Tributária – SP

**Parametrização**

* Marcar o parâmetro por filial para informar se a mesma controla o ressarcimento de ICMS ST: disponível na pasta  03.02 - Apuração de Tributos →  03.02.01 - ICMS →  Apur. ICMS por Filial →  Apuração do ICMS →  Campo "***Controla Ressarcimento de ICMS ST"**.*
* No cadastro da "Natureza de Operação" na pasta "Outros Dados", o parâmetro **"Operação com Ressarcimento/Complemento de ST"**deverá ser marcado**.**
* No cadastro do produto no anexo "Dados Fiscais do Produto" , aba Tributação é necessário marcar a flag "**Produto Exige Inventário Fiscal**".
* No cadastro do produto no anexo "Dados Fiscais por UF",  é necessário cadastrar a UF da filial que está gerando a rotina, e marcar a flag "**Tributado pelo ICMS ST**".
* No cadastro do "Período de apuração" do tributo ICMS ST foi criado uma aba "Ressarcimento/Complemento de ICMS ST". Nesta aba estão destacadas as entradas e saídas por produto e o saldo de imposto que foi suportado na compra. Nesta aba serão apresentadas as seguintes colunas:

* + Código do produto
  + Data do Lançamento Fiscal
  + Tipo
  + Número inicial do Lançamento Fiscal
  + Número do Item do Lançamento Fiscal
  + Quantidade
  + Valor unitário do ICMSST suportado
  + Valor unitário do ICMSST confronto
  + Valor total do ICMSST suportado
  + Valor total do ICMSST confronto
  + Valor do ressarcimento apurado
  + Enquadramento Legal

**Processo**

* Selecionar os produtos que sejam tributados pelo ICMS ST, cuja data de início da tributação pelo ICMS ST seja igual ou anterior à Data do Inventário, e que possuam saldo em estoque nesta data;
* Para cada um destes produtos, será calculada a Base de Cálculo e o Valor do ICMS ST.
* Nos lançamentos de entrada, serão selecionados os itens suficientes para acobertar a quantidade em estoque considerando somente a quantidade dos itens que não tenham sido referenciados aos itens de saída até aquela data. Quando necessário, será realizada uma média ponderada para chegar ao valor do "imposto em estoque". O valor será a soma do ICMS e ICMSST que incidiu na compra dos itens selecionados.

**O produto NÃO será considerado se:**

* O produto não for tributado pelo ICMS-ST;
* A data de início da tributação pelo ICMS-ST for posterior à data do inventário;
* O produto não possuir saldo em estoque na data do inventário;
* Se o Saldo Físico do produto estiver desatualizado. Deverá ser executado primeiramente o processo de re-geração de Saldos e Custos para que seja considerado;
* Não serão considerados lançamentos inutilizados no registro 0150

**Exemplo:**

Considerando o período de 01/11/2018 a 30/11/2018 teremos:

**Quantidade inicial:** Será considerada a posição do estoque referente ao fechamento do período anterior. Neste exemplo, 31/10/2018.

**Quantidade final:** Será considerada a posição do estoque referente ao fechamento do período atual. Neste exemplo, 30/11/2018.

As saídas consideram as entradas mais recentes para referência do valor suportado, sendo que um item que já foi referenciado na saída não pode ser referenciado novamente. Assim, vamos considerar que para cada entrada exista um saldo disponível para ser referenciado, ou seja, a quantidade que ainda não foi utilizada em um lançamento de saída. Neste caso, nossas entradas estão da seguinte forma:

| Data entrada | Qtd na entrada | Qtd já referenciada em saídas | Saldo disponível da entrada | Imposto suportado unitário |
| --- | --- | --- | --- | --- |
| 01/01/2018 | 20 | 15 **=** (10 (saída dia 01/02 )) + (5 (saída dia 01/10)) | 5 | 20,90 |
| 01/03/2018 | 15 | 15 **=** 15 (saída dia 01/10) | 0 | 22,80 |
| 15/10/2018 | 10 | 0 | 10 | 23,75 |
| 16/11/2018 | 5 | 0 | 5 | 24,70 |

**Valor total do ICMS suportado inicial (31/10/2018):** (10 \* 23,75) + (5 \* 20,90) = 342,00

**Valor total do ICMS suportado final (30/11/2018):** (5 \* 24,70) + (10 \* 23,75) + (5 \* 20,90) = 465,50

**Encerramento do****Período**

Em Obrigações Principais → Período de Apuração →  Processos → Encerramento do Período, este processo irá apurar todas as notas de entradas e saídas para o período informado.

Devoluções: Conforme definido na portaria CAT 42/2018 (tabela abaixo) as devoluções serão geradas conforme abaixo.

1. **Devoluções de Entrada:**
   1. O valor do ICMS suportado será gerado conforme a nota da entrada original.
   2. O valor de confronto não será gerado.
   3. O enquadramento legal não será gerado.
2. **Devoluções de Saída:**
   1. Os valores de ICMS suportado são iguais aos valores gerados na nota original e consequentemente serão gerados no campo valor do ressarcimento apurado dos registros 1100 e 1200.
   2. O campo referente ao enquadramento legal deve é gerado igual ao enquadramento da saída.
   3. Caso a Natureza de Operação esteja parametrizada com **"Operação com Ressarcimento/Complemento de ST"**habilitado, o campo valor de confronto deverá ser gerado e consequentemente, o enquadramento legal e valor total do ICMSST confronto, serão gerados nos registros 1100 e 1200.

| Natureza de Operação | Valor suportado (ICMS\_TOT) | Valor total do confronto (VL\_CONFR) | Enquadramento Legal |
| --- | --- | --- | --- |
| Entrada | Obrigatório | Não é informado | Não é informado |
| Devolução de entrada | Obrigatório (conforme informado na entrada original) | Não é informado | Não é informado |
| Saída | Não é informado | Obrigatório se o enquadramento legal for Venda Interestadual, Regra ICMS Isento, Não incidência ou Consumidor Final.Não é informado se o enquadramento legal for Operação com Ressarcimento/Complemento de ST desmarcado. | Obrigatório |
| Devolução de saída | Obrigatório (conforme informado na saída original) | Obrigatório se o enquadramento legal for Venda Interestadual, Regra ICMS Isento, Não incidência ou Consumidor Final.Não é informado se o enquadramento legal for Operação com Ressarcimento/Complemento de ST desmarcado. | Obrigatório |

**Geração da Rotina**

O processo é gerado pelo  "Gerador de Saídas"  através do layout que está disponível para importação nos objetos gerenciais da Biblioteca RM.

Processos Relacionados

* [Associação dos Lançamentos de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=438273534)
* [Inclusão de Contexto para Cálculo dos valores de Estoque - Registro 1050](http://tdn.totvs.com/pages/viewpage.action?pageId=438282654)
* [Encerramento do período - Ressarcimento/Complemento de ICMS ST](http://tdn.totvs.com/pages/viewpage.action?pageId=441821682)
* [Portaria CAT 42/2018 SP](http://tdn.totvs.com/pages/viewpage.action?pageId=403048724#FISCAL01-6374ERPortariaCAT42/2018SP-5)
