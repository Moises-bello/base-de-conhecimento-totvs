---
article_id: 360047565634
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 0110489d9fe62a4f54f2e22c61e63b2e6d63e4e884e9b56aeac9b7551d9722e1
fetched_at: '2026-06-28T22:39:20.408029+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar TES
  para notas de ressarcimento ICMS ST?
type: support-article
updated_at: '2022-03-24T16:38:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047565634-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-TES-para-notas-de-ressarcimento-ICMS-ST
---

**Dúvida**Como configurar Tes para notas de ressarcimento ICMS ST?  
   
 **Ambiente**  
Protheus - FIscal  - A partir da versão 11.80  
  
**Solução**

TEs para emissão da nota fiscal de ressarcimento de ICMS ST

Credita ICMS (F4\_CREDICM) = Não

Calcula ICMS (F4\_ICM) = Não

Cod. Fiscal (F4\_CF) = informar o CFOP 5603/ 6603 ou 1603/ 2603

L.Fisc. ICMS (F4\_LFICM) = ICMS observações

Agrega Valor (F4\_AGREG) = Não

Txt Padrão (F4\_TEXTO) = Inserir o texto desejado

Formula (F4\_FORMULA): Criar uma formula para que a mesma seja amarrada à TES

FORMULA: menu Atualizações>Cadastros>Formulas:

Informar Código, descrição, e no campo formula informar o conteúdo:

Exemplo:

“Ressarcimento de ICMS conforme (informar ato legal do RICMS)”

Obs.: texto entre aspas

2º - Cadastro de um Produto

Para geração da nota será necessário criar um produto “Ressarcimento de ICMS” para ser

selecionado no momento do lançamento da Nota.

 3º - Lançar a nota informando o produto, quantidade 1, valor unitário e o total sendo o valor do

ICMS e informar a TES criada para Ressarcimento.

4º - Após a inclusão da Nota Fiscal de Ressarcimento, acessar a rotina de Apuração do ICMS e incluir manualmente em "Outros Créditos" ou “Outros Débitos” o valor do ICMS ST Ressarcido.

MV\_LFAGREG = .F. caso queira escriturar valor contábil zerado.
