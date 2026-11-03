---
article_id: 4587931907223
category: GPE - eSocial - Não Periódicos
content_hash: f287d38cc85c1e9829ff3f435d04c71b4b0995197a5a790cfbf9c967f6bb254f
fetched_at: '2026-06-28T22:45:04.673596+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Ao alterar o tipo de contrato
  de trabalho de determinado para indeterminado sem excluir a data término de contrato
  o sistema grava mas não envia ao TAF
type: support-article
updated_at: '2026-06-16T11:51:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4587931907223-RH-Linha-Protheus-GPE-eSocial-S-2206-Ao-alterar-o-tipo-de-contrato-de-trabalho-de-determinado-para-indeterminado-sem-excluir-a-data-t%C3%A9rmino-de-contrato-o-sistema-grava-mas-n%C3%A3o-envia-ao-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25827953571735)**Tempo aproximado para leitura: **01:00:00 min****Ocorrência**Ao alterar o tipo de contrato de trabalho de determinado para indeterminado sem excluir a data termino de contrato o sistema grava mas não envia ao TAF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Isso ocorre porque foi alterado o tipo de contrato mas o campo data do contrato continua preenchido, ou seja, como **para o tipo indeterminado não existe data de contrato** o sistema entende que não houve uma alteração contratual.  
  
**Solução**Para que o evento S-2206 seja enviado ao TAF ao alterar o tipo de contrato de prazo determinado para indeterminado deverá ser feita a exclusão da data campo Tp.Cont.Trab.  (RA\_TPCONTR) para indeterminado e apague o conteúdo do campo Dt Term Cont (RA\_DTFIMCT). Após esse procedimento clique em salvar para o sistema gerar o S-2206 com a alteração de contrato.  
  
Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4583201818519)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
