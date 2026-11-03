---
article_id: 19143860811031
category: TAF - REINF
content_hash: 9d28819262c122bd0053d14f438da4829d68d6ea1945dac77be84c37f3367294
fetched_at: '2026-06-28T22:41:33.716161+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como incluir um pagamento
  com (PCC AGREGADO) para  o evento R-4020 manualmente no TAF
type: support-article
updated_at: '2023-11-17T17:06:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19143860811031-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-incluir-um-pagamento-com-PCC-AGREGADO-para-o-evento-R-4020-manualmente-no-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19143853070743) Tempo aproximado para leitura: 00:04:00 min****Dúvida**Como incluir um pagamento (PCC AGREGADO ) para o evento R4020 manualmente no TAF  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.  
  
**Solução**

Os  valores de PCC (PIS,COFINS e CSLL)  serão  considerados  para a apuração deste evento quando cadastrados  através da rotina de pagamentos**(TAFA535)**

Para incluir  o pagamento  acesse o caminho abaixo:

**Atualizações -> Movimentos REINF ->  Pagamento TAFA535  -> Incluir.**

**Capa do Pagamento**

**Natureza (V3U\_NATTIT):** Apenas serão consideradas Faturas com Natureza = 0 - A Pagar

![pag1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19143831694999)

**Dt Pagamento (V3U\_DTPAGT):** O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de pagamento da fatura.

![pag2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19143845248151)

**Natureza de Rendimento**

**Natureza de Rendimento (V3V\_CNATRE):** Para que o item do documento seja considerado, a Natureza de Rendimento deverá possuir conteúdo válido que corresponda a um código da tabela V3O - Naturezas de Rendimento.

![pag3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19143853081367)

**Tributos do pagamento**

**C.Tributo (V47\_CODTRI):** Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código  29 - CSRF - IMPOSTOS PIS/PASEP, COFINS e CSLL  ou  30 - COSIRF - IMPOSTOS IR, CSLL, PIS/PASEP e COFINS 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19143831698839)

Os valores de PCC agregados serão levados no painel reinf na coluna  valor agregado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19143845260183)

**Participantes**

**Tipo Pessoa (C1H\_PPES ):** Para Beneficiários residentes no Brasil **(C1H\_CODPAI=000001)** Faturas/Documentos Fiscais/Pagamentos cujo Participante seja Pessoa Jurídica serão consideradas;

![TIPO_P.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19143860760471)

**Tipo Pessoa EX  (C1H\_PEEXE ):** Para participantes residentes no exterior**(C1H\_CODPAI <> 000001),** também serão considerados os Participantes que estejam com a opção = "3 - Outros" no campo Tipo Pessoa. Neste cenário é necessário preencher o campo Tipo Pessoa Exterior **(C1H\_PEEXE)** como 1 - Pessoa Jurídica

![EX.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19143839784471)

**CNPJ (C1H\_CNPJ):** Para beneficiários residentes no Brasil **(C1H\_CODPAI=000001)** apenas Faturas/Documentos Fiscais/Pagamentos cujo Participante possua CNPJ preenchido serão consideradas.

![TESTE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19143845269655)

**IMPORTANTE:** As faturas  para o  evento R4020  serão demonstradas  somente na rotina PAINEL REINF, quando  o parâmetro **MV\_TAFVLRE**  indicar o layout  **2\_01\_02**
