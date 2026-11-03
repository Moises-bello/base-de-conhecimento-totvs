---
article_id: 360052165074
category: RH - Relatórios Folha
content_hash: acd9d6c35cd6d8548dc78fa0e04426356f315fa734ff92e18f391cab86de410f
fetched_at: '2026-06-28T22:43:17.520480+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionário afastado com situação normal no relatório
  da folha de pagamento
type: support-article
updated_at: '2025-08-01T20:36:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052165074-RH-Linha-Protheus-GPE-Funcion%C3%A1rio-afastado-com-situa%C3%A7%C3%A3o-normal-no-relat%C3%B3rio-da-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25950776259991) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Ao emitir o relatório da folha de pagamento o funcionário afastado esta com situação normal e sem a data do afastamento   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para que o sistema leve as informações para o relatório da folha, serão validados alguns campos no cadastro do funcionário e no lançamento da ausência, verifique os itens abaixo:

**1.** No cadastro do Tipo de Ausência em **Atualizações > Definições de Cálculos > Tipos de Ausências (GPEA430)** verificar se o campo **Tp. Ausência** está cadastrado como tipo 1 - Afastamento ou tipo 2 - Outras Ausências;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25950776264087)  
  
**2.** No cadastro do Tipo de Ausência em **Atualizações > Definições de Cálculos > Tipos de Ausências (GPEA430)** verificar se o campo **Motivo Afast** está cadastrado com o motivo correto;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25950776267799)  
  
**3.** No cadastro do funcionário em **Atualizações > Funcionários > Funcionários (GPEA010)** na aba Funcionais, verificar se os campos **Sit. Folha** e **Cod. Afa. FGTS** estão preenchidos conforme o afastamento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25950776270231)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25950776273047)  
  
**4.** No lançamento da ausência do funcionário em **Atualizações > Lançamentos > Ausências (GPEA240)** verificar se os campos **Num. Dias, Dias Empresa, Dias a Pagar, Saldo de Dias** e **Dias Pagos** estão estão condizentes com a data inicial e a data fim do afastamento.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25950776275863)  
 **Observação:** Quando não existe uma data fim do afastamento, o campo **Num. Dias** deverá ser 999.

**Saiba mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
