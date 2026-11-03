---
article_id: 360062083174
category: Financeiro - Contas a Receber
content_hash: 66c776fdd20c262aa07b7717ef3811829704ff8d350ed246f52260e8b1d6fe34
fetched_at: '2026-06-28T22:38:13.812635+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus-  SIGAFIN - FINA040 - Como faz para
  preencher o campo tx permanência
type: support-article
updated_at: '2022-04-04T17:04:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062083174-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Como-faz-para-preencher-o-campo-tx-perman%C3%AAncia
---

**Dúvida**Como faz para preencher o campo tx permanência?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – FINA040 - A partir da versão 11.80  
  
**Solução**A taxa de permanência  é o campo **E1\_VALJUR**, ele é alimentado através do parâmetro **MV\_TXPER**, poderá ser alterado pelo módulo **Configurador**.  
  
Pois bem, este parâmetro é a taxa de juros a ser aplicada nos **títulos a receber**.  
  
Quando o mesmo gera a fatura pelo **módulo Faturamento,** são geradas notas e por sua vez, geram os títulos no **Contas a Receber**, certo. Todos esses títulos estão com este campo **E1\_VALJUR** preenchido com a porcentagem de **Juros**.  
  
Ao efetuar a baixa de um titulo vencido será calculado o juros com esta porcentagem gravada neste campo.

**Importante**Este campo só terá funcionalidade se o título estiver vencido.

**Saiba mais:**  
[MP-FAT- Tratamento de juros no módulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024357552-MP-FAT-Tratamento-de-juros-no-m%C3%B3dulo-Faturamento?source=search)
