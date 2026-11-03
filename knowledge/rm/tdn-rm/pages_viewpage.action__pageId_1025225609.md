---
content_hash: f03a1ddba76e07957b21a766ceb22c76fe5e069fba027f6b1d410b6c7245e028
fetched_at: '2026-06-29T00:05:48.563048+00:00'
page_id: '1025225609'
product: rm
source: tdn-rm
title: 2 - Parametrização de Layout no cadastro de Bancos e Agências
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1025225609
version: 13
---

Nesta etapa será realizada a **parametrização do Layout de Registro Online**, responsável por definir quais informações serão enviadas ao banco no momento do **registro do boleto híbrido**.

Por meio desse layout são configurados, por exemplo:

* **Multa**
* **Juros**
* **Desconto**
* **Regras de pagamento após vencimento**
* Outros parâmetros exigidos pelo banco

⚠️ **Importante**  
Cada banco possui **regras próprias** para esses campos. Caso seja enviada uma modalidade não suportada pelo banco, **o registro do boleto não será realizado e retornará erro**.

No menu do sistema, acesse:

**Movimentações Bancárias → Bancos e Agências**

Localize e selecione o **banco desejado**.

Com o banco selecionado, acesse:

**Anexos → Layout de Registro Online**

Para inserir um novo layout, clique no botão:

**( + ) Inserir**

No exemplo desta documentação serão criados **layouts para o banco Itaú**, mas o mesmo processo pode ser aplicado para os demais bancos.

Os layouts disponíveis podem ser consultados no link de referência da documentação.

## **Layouts de registro online disponíveis no [link](https://tdn.totvs.com/pages/releaseview.action?pageId=980993042)**

Este layout define **qual será a modalidade da multa aplicada ao boleto**.

**Campo**  
`TBoletoHibrido.Due.AmountDetails.Fine.Modality`

**Descrição**  
Modalidade da Multa

Este layout define **o valor da multa que será aplicado ao boleto**.

**Campo**  
`TBoletoHibrido.Due.AmountDetails.Fine.Value`

**Descrição**  
Valor da Multa

Este layout define **como os juros serão calculados pelo banco**.

**Campo**

TBoletoHibrido.Due.AmountDetails.Interest.Modality

**Descrição**  
Modalidade de Juros

Este layout define **o valor do juros aplicado ao boleto**.

**Campo**

TBoletoHibrido.Due.AmountDetails.Interest.Value

**Descrição**  
Valor do Juros

Este layout define **quantos dias após o vencimento o boleto ainda poderá ser pago**.

**Campo**

TBoletoHibrido.Due.DayValidAfterDue

**Descrição**  
Dias permitidos após o vencimento

Este layout define **a data limite para primeiro desconto condicional**.

**Campo**

TBoletoHibrido.Due.AmountDetails.Discount.FixedDate1.Date

**Descrição**  
Data limite para o primeiro desconto

Este layout define **a data limite para primeiro desconto condicional**.

**Campo**

TBoletoHibrido.Due.AmountDetails.Discount.FixedDate1.Value

**Descrição**  
Valor do primeiro desconto

É possível configurar até **3 descontos condicionais** para o mesmo boleto.

Para isso, deverão ser configurados os layouts correspondentes a:

* Segunda data limite de desconto;
* Segundo valor de desconto;
* Terceira data limite de desconto;
* Terceiro valor de desconto.

> ⚠️ Importante: Antes de realizar a configuração, verifique se o banco utilizado suporta o envio de múltiplos descontos condicionais. Caso a instituição financeira não disponibilize essa funcionalidade, o registro do boleto será rejeitado e retornará erro no processamento.

Essa parametrização deve ser realizada **em todos os cadastros de bancos utilizados para registro de boleto híbrido**.

Isso garante que cada banco possua **seu próprio layout de registro configurado corretamente**.

Após a configuração dos layouts:

* O sistema enviará corretamente as **informações de multa e juros ao banco**
* O **registro online do boleto híbrido** será realizado sem inconsistências
* As regras de **pagamento após vencimento** serão respeitadas
