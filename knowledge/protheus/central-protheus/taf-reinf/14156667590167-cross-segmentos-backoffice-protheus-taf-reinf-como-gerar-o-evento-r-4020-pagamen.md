---
article_id: 14156667590167
category: TAF - REINF
content_hash: abf68d74ec7741d6823509bf4a8ab72b12d88fc52974f3df1284fd76fcfd7e7b
fetched_at: '2026-06-28T22:41:33.663940+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como gerar o evento R-4020
  (Pagamento) manualmente no TAF?
type: support-article
updated_at: '2025-01-10T12:18:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14156667590167-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-gerar-o-evento-R-4020-Pagamento-manualmente-no-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18192788224663) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como gerar o evento **R-4020** via TAF através da baixa?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.  
  
**Solução**

O **IR** calculado na baixa será considerado para a apuração deste evento quando cadastrados  através da rotina de pagamentos **(TAFA535).**

Para incluir  o pagamento  acesse o caminho abaixo:

**Atualizações -> Movimentos REINF ->  Pagamento TAFA535  -> Incluir.**

**Capa do Pagamento**

**Natureza (V3U\_NATTIT):** Apenas serão consideradas Faturas com Natureza = **0 - A Pagar**

![pag1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14156144484631)

**Dt Pagamento (V3U\_DTPAGT):** O **mês/ano** selecionado para apuração deve corresponder ao **mês/ano** da data de **pagamento** da fatura.

![pag2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14156223927063)

**Natureza de Rendimento** **(V3V\_CNATRE):** Para que o item do documento seja considerado, a Natureza de Rendimento deverá possuir conteúdo válido que corresponda a um código da tabela **V3O** - Naturezas de Rendimento:

![pag3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14156256785047)

**Tributos do pagamento:**

**C.Tributo (V47\_CODTRI):** Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código **28- IR Pagamento, 10 - PIS Retenção, 11 - COFINS Retenção, 18 - CSLL:**

**![PAG4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14156299774871)**

**Participantes:**

**Tipo Pessoa (C1H\_PPES ):** Para Beneficiários residentes no Brasil **(C1H\_CODPAI=000001)** Faturas/Documentos Fiscais/Pagamentos cujo Participante seja Pessoa Jurídica serão consideradas:

![TIPO_P.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18192734378391)

**Tipo Pessoa EX  (C1H\_PEEXE ):** Para participantes residentes no exterior **(C1H\_CODPAI <> 000001),** também serão considerados os Participantes que estejam com a opção = **"3 - Outros"** no campo Tipo Pessoa.

Neste cenário é necessário preencher o campo Tipo Pessoa Exterior **(C1H\_PEEXE)** = **1 - Pessoa Jurídica:**

![EX.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18192770877335)

**CNPJ (C1H\_CNPJ):** Para beneficiários residentes no Brasil **(C1H\_CODPAI=000001)** apenas Faturas/Documentos Fiscais/Pagamentos cujo Participante possua **CNPJ** preenchido serão consideradas:

![TESTE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18192770885783)

**IMPORTANTE:** As faturas  para o  evento **R4020** serão demonstradas  somente na rotina **PAINEL REINF**, quando  o parâmetro **MV\_TAFVLRE**  indicar o layout  **2\_01\_02**

Doc complementar:

<https://tdn.totvs.com/display/public/TAF/EFD-Reinf>
