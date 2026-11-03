---
article_id: 360040818694
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 45f6bc4760e2e296d3ba26766e6eb5abbb96543df6b6b4f895760baf8f6e77f8
fetched_at: '2026-06-28T22:39:30.560270+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração utilizada
  para venda presencial com retirada no balcão
type: support-article
updated_at: '2021-07-29T14:02:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040818694-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-utilizada-para-venda-presencial-com-retirada-no-balc%C3%A3o
---

**Dúvida**  
Configuração utilizada para venda presencial com retirada no balcão.

**Ambiente**  
Potheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para venda presencial destinada à consumidor final não contribuinte, com retirada no balcão (no ato da compra dentro do estabelecimento), é considerada uma operação INTERNA (Estadual) onde não existe o cálculo de DIFAL e a alíquota praticada também é interna. Para isto, deve ser feita a seguinte configuração abaixo:

Tipo Oper.NF = Saída

**Cadastro de TES:**  
F4\_VENPRES = 1

**Pedido de Vendas:**  
C5\_TIPOCLI = F

C5\_TPFRETE = S

Desta forma, o sistema identifica pelos campos “F4\_VENPRES = 1” e “C5\_TPFRETE = S” que a venda é presencial e considera a UF Destino como UF Origem.
