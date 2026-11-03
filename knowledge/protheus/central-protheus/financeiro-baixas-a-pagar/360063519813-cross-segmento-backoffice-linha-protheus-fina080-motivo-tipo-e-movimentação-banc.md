---
article_id: 360063519813
category: Financeiro - Baixas a Pagar
content_hash: dae4c8222d98c3feed83d3fcc349b923d0efe66cd3450e812427ea65cbcd117f
fetched_at: '2026-06-28T22:37:24.841305+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA080 -  Motivo, tipo  e movimentação
  bancária de baixa pagar manual
type: support-article
updated_at: '2026-03-12T18:35:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063519813-Cross-Segmento-Backoffice-Linha-Protheus-FINA080-Motivo-tipo-e-movimenta%C3%A7%C3%A3o-banc%C3%A1ria-de-baixa-pagar-manual
---

**Dúvida**  
Quais os motivos, tipos e movimentação bancária de baixa a pagar manual?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 11.80  
  
**Solução**

Permite efetuar as baixas dos títulos a pagar individualmente. Pela baixa do título é possível determinar seu motivo, mediante cadastro prévio de uma **Tabela de motivo de baixas** (disponível na opção **Miscelâneas**), desta forma, além de identificar os títulos, ela permite que um motivo de baixa possa ou não **Movimentar saldos bancários** e **Gerar cheque**. Este controle é feito através dos campos **Mov. Bancária** e **Cheque**.

Os tipos de baixa que não movimentam o saldo bancário são:

* **BA**– Baixa Automática sem Borderô.
* **JR**– Juros.
* **MT**– Multa.
* **DC**– Desconto.
* **CM**- Correção monetária.
* **D2**- Desconto de título descontado.
* **J2**- Juros de título descontado.
* **M2**- Multa de título descontado.
* **V2**- Valor líquido de título descontado.
* **TL**- Valor baixado com tolerância.
* **CP**- Baixa via compensação.
* **C2**- Correção de título descontado.

Existem seis motivos padrões de baixa de títulos a pagar:

* **Normal (NOR):**títulos de pagamentos normais. Atualiza automaticamente a movimentação bancária, caso tenha sido gerado cheque para o título ou não. Este motivo de baixa tem por objetivo o uso de cheque.
* **Devolução (DEV):**recebimentos referentes a devoluções. Não atualiza a movimentação bancária.
* **Dação (DAC):**ocorre quando algo é oferecido como pagamento de outro. Não atualiza a movimentação bancária.
* **Vendor (VEND):**pagamento de título via empréstimo bancário. O Banco passa a ser o beneficiário, porém, é necessário que a empresa possua um contrato bancário cadastrado para possibilitar este empréstimo. Atualiza automaticamente a movimentação bancária.
* **Débito CC:**debita automaticamente a movimentação bancária sem a necessidade de gerar cheque sobre o título.
* **Mais Prazo (MPR ou conforme parâmetro MV\_MBXTECF):** Utilizado na Integração com TOTVS Mais Prazo. Utilizado na carteira a pagar. Não movimenta saldo bancário, não considera cálculo de comissão e não gera cheque.

**Saiba Mais**  
[Baixas Pagar Manual - FINA080 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12)

[Cadastro de Motivo de Baixa](https://tdn.totvs.com/display/public/PROT/Cadastro+de+Motivo+de+Baixa+-+FINA490)
