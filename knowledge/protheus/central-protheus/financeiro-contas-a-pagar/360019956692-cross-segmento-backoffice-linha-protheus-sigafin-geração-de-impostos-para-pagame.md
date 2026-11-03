---
article_id: 360019956692
category: Financeiro - Contas a Pagar
content_hash: fe8a343d008f5130ff5a41263456bf7b8910db6d7b54d29e8acf68628cecfc24
fetched_at: '2026-06-28T22:38:06.927923+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN -  Geração de impostos
  para pagamento antecipado e compensação de adiantamento
type: support-article
updated_at: '2025-09-12T20:13:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019956692-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Gera%C3%A7%C3%A3o-de-impostos-para-pagamento-antecipado-e-compensa%C3%A7%C3%A3o-de-adiantamento
---

**Dúvida**Como gerar impostos para pagamento antecipado e compensação de adiantamento?   
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**A geração dos impostos do valor pago antecipadamente se dará pelo seguinte processo: 

* Incluir a **NF** e o **PA**, que calcule impostos.
* A geração do **PIS**/ **COFINS**/**CSLL** será na inclusão do PA.
* Compensando os títulos o Sistema considera o  valor bruto informado no PA.

Por exemplo:

* Incluir um **PA** de R$ 10.000,00 com retenção **PIS**/**COFINS**/**CSLL**, supondo que o total da retenção seja de 300,00. O Sistema gera um título de R$ 9.700,00 e os **TX's** totalizando R$ 300,00.
* Incluir uma **NF** de R$ 25.000,00.
* Ao compensar, o sistema irá baixar R$ 10.000,00 da **NF** e baixar totalmente o **PA**, assim, quando for efetuada a baixa do saldo da **NF**, será gerado o **PIS**/**COFINS**/**CSLL** somente sobre os R$ 15.000,00 (saldo restante).

**Informações complementares:**   
Toda vez que a retenção do imposto no parâmetro **MV\_BX10925** ocorrer na emissão e a natureza estiver configurada para gerar impostos, o **PA** gerará um título do tipo **TXA** ao invés de **TX**. Isso para que possa ser compensado com os impostos **TX** do título **NF** ou **DP**.

Por exemplo:

O **TXA** gerado a partir do **PA** vai para pagamento no banco por meio de borderô.

* Seu processamento de retorno não gerará o movimento de pagamento do imposto, porém seu saldo continua em aberto. Em seguida esse **TXA** é compensado com um **TX** gerado por **NF** ou **DP** que gera movimentação bancária.
* Para que este processo funcione de forma correta, verifique o parâmetro **MV\_BXTXA**:

           Tipo: *Caracter*

           Conteúdo: 1 = Permite Baixar; 2 = Não zera o saldo.

Na rotina de compensação a pagar, deve ser configurado o parâmetro **Compensa Títulos** como **impostos**. Assim, para efetuar a compensação, deve ser selecionado o título **TX** e, na tela seguinte, virá o **TXA**. Para voltar a compensar **PA** e **NF**, o parâmetro **Compensa Títulos** deve ser configurado como **normal**.

**Saiba mais**

[Cross Segmento - Backoffice Linha Protheus - Parâmetros para ajustes de Retenção de PCC no Módulo (06) Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027163451-Cross-Segmento-Backoffice-Linha-Protheus-Par%C3%A2metros-para-ajustes-de-Reten%C3%A7%C3%A3o-de-PCC-no-M%C3%B3dulo-06-Financeiro)
