---
article_id: 12247685490711
category: TAF - REINF
content_hash: 501721b6767c30aedd6cc56b898a8e227f5965b575bbd98326101dc55cc992ff
fetched_at: '2026-06-28T22:41:33.757082+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como integrar R-4010
  (Emissão) por Fatura no TAF.
type: support-article
updated_at: '2023-03-31T16:56:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12247685490711-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-R-4010-Emiss%C3%A3o-por-Fatura-no-TAF
---

**Dúvida**Como gerar o evento R-4010 manualmente no TAF por fatura.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12.   
  
**Solução**

**Para que os documentos faturas/recibos (TAFA448) a pagar sejam considerados no evento R-4010 → Pagamentos/créditos a beneficiário pessoa física o imposto calculado na nota fiscal deve ser o IR na emissão (ID TAF = 000012 - IR Emissão).**

Atualizações -> Movimentos REINF -> Faturas/Recibos.

**Capa da Fatura :**

   Natureza (LEM\_NATTIT): Apenas serão consideradas Faturas com Natureza = 0 - A Pagar;

![F1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12247321632791)

  Dt Emissão (LEM\_DTEMIS): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão da fatura;

![F2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12247330906135)

**Natureza de Rendimento:**

  Natureza de Rendimento (V3S\_CDNATR): Para que o item do documento seja considerado, a Natureza de Rendimento deverá possuir conteúdo válido que corresponda a um código da tabela V3O - Naturezas de Rendimento.

![F3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12247419003543)

**Tributos do Item**

  C.Tributo (V47\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 12-IR emissão.

![F4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12247505519895)

**Participantes**

  Tipo Pessoa (C1H\_PPES )

![F6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12247636960407)

  Para Beneficiários residentes no Brasil (C1H\_CODPAI=000001) Faturas/Documentos Fiscais/Pagamentos cujo Participante seja Pessoa Física serão consideradas;

![F7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12247638214807)

  Tipo Pessoa (C1H\_PPES ): Para participantes residentes no exterior (C1H\_CODPAI <> 000001), também serão considerados os Participantes que estejam com a opção = "3 - Outros" no campo Tipo Pessoa. Neste cenário é necessário preencher o campo Tipo Pessoa Exterior (C1H\_PEEXE) como 1 - Pessoa Física;

![F8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12247610126487)

  CPF (C1H\_CPF): Para beneficiários residentes no Brasil (C1H\_CODPAI=000001) apenas Faturas/Documentos Fiscais/Pagamentos cujo Participante possua CPF preenchido serão consideradas.

![F9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12247641733527)

Mais informações: <https://tdn.totvs.com.br/display/public/TAF/EFD-Reinf#EFDReinf-R-4010-Pagamentos/cr%C3%A9ditosabenefici%C3%A1riopessoaf%C3%ADsica>
