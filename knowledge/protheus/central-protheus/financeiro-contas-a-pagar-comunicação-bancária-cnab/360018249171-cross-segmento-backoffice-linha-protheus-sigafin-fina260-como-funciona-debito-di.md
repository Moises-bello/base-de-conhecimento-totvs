---
article_id: 360018249171
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 9c93cf838553d3c38f54414374f3651add8dde40c803eb31a851456a8366a077
fetched_at: '2026-06-28T22:37:55.200892+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA260 - Como funciona
  Debito Direto Autorizado (DDA) no Protheus
type: support-article
updated_at: '2026-05-05T14:14:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018249171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA260-Como-funciona-Debito-Direto-Autorizado-DDA-no-Protheus
---

**Dúvida**  
Como funciona Débito Direto Autorizado (DDA) no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - A partir da versão 11.80  
  
**Solução**  
Ao contrário do processo tradicional de comunicação bancária, quando o *Protheus* gera o arquivo de remessa e o encaminha para Banco, o **DDA** inicia-se quando o banco encaminha o arquivo de retorno e este arquivo é importado em: **Financeiro, Atualizações, Comunicação Bancária>Retorno de Pagamentos (FINA430)**.   
Ao importar o arquivo, são gravadas as informações: **códigos de barras**, **data de vencimento** e **fornecedor** na tabela **FIG**.  
Com as informações gravadas na tabela **FIG**, acesse: **Financeiro, Atualizações, Comunicação Bancária> Conciliação DDA (FINA260)** e efetue conciliação, que nada mais é que gravar o campo: **E2\_CODBAR** baseado nos códigos de barras na tabela: **FIG**.  
  
**Importante**  
Conforme a informação acima, **o processo de DDA não realiza baixa nos títulos**. Apenas efetua a integração dos códigos de barras que constam no arquivo de retorno e grava nos títulos a pagar no campo: **(E2\_CODBAR).**

Após conciliar os títulos pelo processo **DDA**, poderá seguir o fluxo de baixa via processo manual **FINA080**, automática **FINA090** ou até mesmo gerar um arquivo de remessa e encaminhar para pagamento via **CNAB FINA420 e** retorno **FINA430.**

Outro ponto importante é que o DDA **não gatilha** a linha digitável.

**Saiba mais**

[Conciliação DDA (FINA260 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312165346)
