---
article_id: 360021939512
category: Financeiro - Contas a Pagar
content_hash: 6e96a662bc25296ed1ebd91383b9fe9e14e5f28f0fddbee3a488ff8b1defe98f
fetched_at: '2026-06-28T22:38:07.124018+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA290 - Processo
  de geração de Faturas a Pagar
type: support-article
updated_at: '2025-11-18T13:37:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021939512-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA290-Processo-de-gera%C3%A7%C3%A3o-de-Faturas-a-Pagar
---

**Dúvida**  
Como efetuar o recebimento de um boleto para várias notas fiscais de um fornecedor.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – FINA290 - A partir da versão 11.80  
  
**Solução**

Em determinados tipos de negociação, pode surgir a dúvida de como **gerar uma única fatura a partir de vários títulos existentes para um mesmo fornecedor**.

Esse processo **cria um novo título consolidado**, representando o valor total da fatura, **enquanto os títulos originais são automaticamente baixados**.

A prática é especialmente útil para **empresas que emitem ou recebem múltiplas notas fiscais** relacionadas a um mesmo fornecedor e desejam **centralizar o pagamento ou recebimento em uma única fatura**.

Para os novos títulos gerados, é especificada uma condição de pagamento que definirá a estruturação desses títulos. Adicionalmente, é possível configurar a emissão desses títulos tanto para a loja associada ao título principal quanto para todas as lojas do fornecedor.

O sistema permite a seleção, ou seja, o filtro dos títulos a serem aglutinados, com base no período de emissão, código do fornecedor e valor total da fatura.

Para efetuar uma **Fatura a Pagar** acesse:

**Atualizações** > **Contas a Pagar** > **Faturas a Pagar**​  
  
![fina290 ajuste.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25470395983767)

**Principais Parâmetros:**  
  
**Prefixo**: informa o prefixo que terão os títulos a pagar gerados pelo processo de fatura.  
**Tipo**: informa o tipo de título que terão os títulos a pagar gerados pelo processo de fatura.  
**Número da Fatura**: informa o número de identificação que terão os títulos a pagar gerados pelo processo de fatura.  
**Natureza**: informa o código da natureza financeira que terão os títulos a pagar gerados pelo processo da fatura.  
**Moeda:** informa a moeda que terão os títulos a pagar gerados pelo processo da fatura a receber.  
**Emissão De/Até:** informa o intervalo de datas de emissão dos títulos a pagar filtrados para o processo de fatura.  
**Valor da Fatura:** informa o valor máximo da fatura a pagar para seleção dos títulos a pagar filtrados para o processo de fatura.  
**Cliente/Loja:** informa o código de identificação e o código de filial do cliente que deseja filtrar e gerar as faturas a pagar.  
**Código:** informa o código da condição de pagamento que será utilizado para geração dos títulos a receber da fatura.

**Importante**

Não é permitido gerar uma nova fatura a partir de uma fatura já existente.

**Saiba Mais**[Faturas a Pagar - FINA290 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Faturas+a+Pagar+-+FINA290+-+Financeiro+-+P12#FaturasaPagarFINA290FinanceiroP12-06.CONTABILIZA%C3%87%C3%83O)

[Liquidação a pagar - FINA565](https://tdn.totvs.com/pages/releaseview.action?pageId=312167645)
