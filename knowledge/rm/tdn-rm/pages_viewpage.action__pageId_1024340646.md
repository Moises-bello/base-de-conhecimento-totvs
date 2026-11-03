---
content_hash: e5e01c654664f9bf98556b4f512c46b92012b2c744baf1b9f10d3aa0b7613936
fetched_at: '2026-06-29T00:05:48.256645+00:00'
page_id: '1024340646'
product: rm
source: tdn-rm
title: Geração de lançamento financeiros - Locação, Aluguel Complementar e Aluguel
  em Dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024340646
version: 29
---

---

![Reforma Tributária](https://tdn.totvs.com/download/attachments/1025239488/1025239500/ReformaTributaria.png)


# Geração do Lançamento Financeiro, Aluguel Complementar e Aluguel em Dobro

Reforma tributária
Gestão de Imóveis

Nesta etapa do processo, ocorre a geração do
**lançamento financeiro do aluguel**, bem como o tratamento das
informações tributárias relacionadas à Reforma Tributária, de forma integrada
entre os módulos envolvidos.

]]>

## 🔁 **Etapas do Processo**

**1. Geração do lançamento financeiro**

* + - O lançamento financeiro é gerado normalmente, com o **valor original** do contrato (por exemplo, o valor do aluguel).
    - Esse valor **não é alterado** pelas regras tributárias.  
      **1.1** Este processo inclui:
      * Geração de Parcelas de Locação (mensal) e Aluguel em dobro.
      * Geração de Aluguel Complementar;

Para lançamentos de aluguel complementar ou aluguel em dobro, não será necessário deduzir o redutor social na base de cálculo, pois o redutor social só se aplica para **imóveis residenciais**, e a receita de aluguel complementar só pode ser aplicada em imóveis comerciais.

**2. Envio automático das informações tributárias ao Financeiro**

* + - No momento da geração do lançamento, o sistema **envia automaticamente** as informações tributárias para o módulo Financeiro.
    - Esse envio ocorre junto com o lançamento, permitindo que ambos os processos sejam tratados como **um único passo**.

**3. Cálculo da base de cálculo e dos tributos**

                Para realizar o cálculo dos tributos, o sistema utiliza as seguintes informações:

* + - A regra tributária associada em "Informações Adicionais" no contrato de locação;
    - O tipo do imóvel (residencial ou comercial) de acordo com o **Tipo de Destinação** informado no campo de tipo de locação definido em "Identificação" do contrato de locação;
    - [Regra redutora](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1024340522)(por exemplo, aplicação do redutor social);
    - [Percentuais e alíquotas configuradas](https://tdn.totvs.com.br/pages/releaseview.action?pageId=1024340579).

Com base nessas informações, o sistema realiza o cálculo de:

* + - Base de cálculo
    - Alíquota
    - Valor do tributo

**4. Armazenamento das informações tributárias**

* + As informações tributárias **não são gravadas no valor principal** do lançamento financeiro.
  + Esses dados são armazenados em uma tabela específica de tributos do lançamento, identificada como **FTRBLAN**.
  + Quando forem devidamentes configurados, para cada lançamento financeiro, serão geradas:
    - Uma linha referente ao imposto **IBS**
    - Uma linha referente ao imposto **CBS**
  + Cada registro conterá as seguintes informações:
    - Base de cálculo
    - Alíquota
    - Valor do imposto
    - Regra tributária aplicada

Dessa forma, o sistema garante que o lançamento financeiro preserve o valor
original do contrato, ao mesmo tempo em que realiza o
**cálculo, registro e controle das informações tributárias**
exigidas pela Reforma Tributária, de forma integrada e segura.

]]>

---

### Etapas seguintes do processo

1. O Financeiro gera o boleto
2. [O locatário realiza o pagamento](https://tdn.totvs.com.br/display/LRM/Pagamento+e+baixa+do+aluguel)
3. O Financeiro realiza a baixa
4. O sistema busca os valores baixados
5. Com base nesses valores, é gerado o [movimento no Gestão de Estoques, Compras e Faturamento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1024340825)

Informações

Quando o locatário paga o boleto, o lançamento financeiro é baixado no sistema após a confirmação do pagamento por meio da conciliação bancária (processo utilizado pelo Financeiro para identificar que o lançamento foi efetivamente quitado).

Esse ponto é fundamental, pois somente os aluguéis pagos e devidamente conciliados poderão gerar movimentos fiscais e notas fiscais.
