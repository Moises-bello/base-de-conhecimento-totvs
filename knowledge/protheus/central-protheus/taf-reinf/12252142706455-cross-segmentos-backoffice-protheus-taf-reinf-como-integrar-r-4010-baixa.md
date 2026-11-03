---
article_id: 12252142706455
category: TAF - REINF
content_hash: daa9832fcdc1ff981fbdee0ca669db6e8563dce8ff0e3a423e176031fd170e91
fetched_at: '2026-06-28T22:41:33.753137+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como integrar R-4010
  (Baixa).
type: support-article
updated_at: '2023-07-03T12:26:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12252142706455-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-R-4010-Baixa
---

**Dúvida**Como gerar o evento R-4010 baixa manualmente no TAF.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12.   
  
**Solução:**

**O IR calculado na baixa será considerado para a apuração deste evento quando cadastrados na rotina de pagamentos (TAFA535)**

Atualizações -> Movimentos REINF -> Pagamentos.

**Pagamentos**

**Capa do Pagamento**

  Natureza (V3U\_NATTIT): Apenas serão consideradas Faturas com Natureza = 0 - A Pagar;

![B1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12251685969559)

  Dt Pagamento (V3U\_DTPAGT): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de pagamento da fatura;

![B2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12251740360599)

**Natureza de Rendimento**

  Natureza de Rendimento (V3V\_DNATRE): Para que o item do documento seja considerado, a Natureza de Rendimento deverá possuir conteúdo válido que corresponda a um código da tabela V3O - Naturezas de Rendimento.

![B3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12251829328279)

**Tributos do pagamento**

  C.Tributo (V46\_DESTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 28- IR Pagamento.

![B4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12251885783447)

**Participantes**

  Tipo Pessoa (C1H\_PPES )

![F6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12252024232855)

  Para Beneficiários residentes no Brasil (C1H\_CODPAI=000001) Faturas/Documentos Fiscais/Pagamentos cujo Participante seja Pessoa Física serão consideradas.

![F7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12252057334423)

  Tipo Pessoa (C1H\_PPES ): Para participantes residentes no exterior (C1H\_CODPAI <> 000001), também serão considerados os Participantes que estejam com a opção = "3 - Outros" no campo Tipo Pessoa. Neste cenário é necessário preencher o campo Tipo Pessoa Exterior (C1H\_PEEXE) como 1 - Pessoa Física;

![F8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12252062289431)

  CPF (C1H\_CPF): Para beneficiários residentes no Brasil (C1H\_CODPAI=000001) apenas Faturas/Documentos Fiscais/Pagamentos cujo Participante possua CPF preenchido serão consideradas.

![F9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12252063479703)

Mais informações: <https://tdn.totvs.com.br/display/public/TAF/EFD-Reinf#EFDReinf-R-4010-Pagamentos/cr%C3%A9ditosabenefici%C3%A1riopessoaf%C3%ADsica>
