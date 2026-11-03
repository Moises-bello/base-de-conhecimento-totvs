---
article_id: 360043180793
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: dda969013e111d033868df405db7efc4c6aefe5c608ee49d40e221a28194f40a
fetched_at: '2026-06-28T22:39:36.863083+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alteração das casas
  decimais PIS e COFINS apuração
type: support-article
updated_at: '2025-02-17T20:10:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043180793-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Altera%C3%A7%C3%A3o-das-casas-decimais-PIS-e-COFINS-apura%C3%A7%C3%A3o
---

**Dúvida**Como eu faço para alteras as casas decimais para quatro casas no PIS e COFINS, pôr exemplo.

**Ambiente**Protheus - Compras ou Faturamento - 12.1.17  
  
**Solução**

**Por favor, para alteração com 4 casas decimais, seguir o procedimento abaixo:**

Utilize o configurador:

No cadastro de produtos: SB1 (B1\_PPIS e B1\_PCOFINS) SBZ (BZ\_PPIS e BZ\_PCOFINS)  
  
Grupo de tributação(Caso utilize exceção fiscal) SF7 (F7\_ALIQPIS e F7\_ALIQCOF)  
  
Notas de entrada SD1 (D1\_ALQIMP5 (PIS) e D1\_ALQIMP6 (COFINS))  
  
Notas de saída SD2 (D2\_ALQIMP5 (PIS) e D2\_ALQIMP6 (COFINS))  
  
Livro Fiscal Item SFT (FT\_ALIQPIS e FT\_ALIQCOF)

Livro digital de Impostos-SPED (Transmissão de NFe) CD2 (CD2\_ALIQ)  
  
Exemplo para alteração dos campos:  
Tamanho 7  
Decimal 4  
  
Nas tabelas SF1 e SF2, só são gravados valores, portanto não há campos para a alíquota.  
  
Na tabela SF3, o sistema não grava os valores de PIS e COFINS.  
  
Para que o valor da alíquota não seja arredondado no pedido de venda/Doc. Entrada, altere o parâmetro **MV\_DECALIQ para .T.** Sobre o parâmetro.

Obs: Manipulação via banco ou apsdu, responsabilidade do cliente ou do analista programador.
