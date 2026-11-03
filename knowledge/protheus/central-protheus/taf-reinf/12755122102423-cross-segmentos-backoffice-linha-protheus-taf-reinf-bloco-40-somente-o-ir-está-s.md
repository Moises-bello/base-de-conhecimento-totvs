---
article_id: 12755122102423
category: TAF - REINF
content_hash: 6718e83ba3360e09001b604c4c6cfb3caec676ca00add570f99009ba7909d8cf
fetched_at: '2026-06-28T22:41:33.376900+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos -  Backoffice Linha Protheus - TAF - REINF  - BLOCO 40 - Somente
  o IR está sendo considerado na Apuração, os valores de PCC estão zerados
type: support-article
updated_at: '2023-12-05T14:27:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12755122102423-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-BLOCO-40-Somente-o-IR-est%C3%A1-sendo-considerado-na-Apura%C3%A7%C3%A3o-os-valores-de-PCC-est%C3%A3o-zerados
---

**Dúvida**Ao efetuar a integração dos dados referentes a apuração dos eventos do bloco R-4000, somente o IR está apresentando os valores no Painel Reinf, o PCC está com o valor zerado.

![print_kcs_ir_pcc.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12803589005079)  
  
**Ambiente**  
Microsiga Protheus – TAF – A partir da versão 12.1.27  
  
**Solução**

O bloco de eventos R-4000 possui a particularidade, tratando-se do PCC (Pis, Cofins, CSLL), de ser gerado no **pagamento/baixa** e não na emissão.

O layout do Extrator Fiscal responsável por levar as informações de movimentos para o TAF são:

T013 - Documento Fiscal - Alimenta tabela C20 e filhas - rotinas TAFA026E/TAFA026S

T154 - Fatura/Recibo - Alimenta tabela LEM e filhas - rotina TAFA448

T158 - Pagamento/Baixa - Alimenta V3U e filhas - rotina TAFA535

Nos casos em que somente o valor do IR estiver sendo considerado na apuração do Painel Reinf, possivelmente ocorreu o seguinte:

* O registro T158 não foi marcado no extrator fiscal ou ocorreu erro de integração do layout T158.
* Não foi efetuado a baixa do título principal no Financeiro.

Os valores do PCC só serão considerados na apuração, se atenderem aos seguintes critérios:

* Pagamentos
  + Capa do Pagamento
    - Natureza (V3U\_NATTIT): Apenas serão consideradas Faturas com Natureza = 0 - A Pagar;
    - Dt Pagamento (V3U\_DTPAGT): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de pagamento da fatura;
  + Natureza de Rendimento
    - Natureza de Rendimento (V3V\_CNATRE): Para que o item do documento seja considerado, a Natureza de Rendimento deverá possuir conteúdo válido que corresponda a um código da tabela V3O - Naturezas de Rendimento.
  + Tributos do pagamento
    - C.Tributo (V47\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 28- IR Pagamento.

Caso possua alguma dúvida com relação a baixa do título ou caso o extrator fiscal não gerar o layout T158, por gentileza acionar o time Protheus Financeiro.

Para mais detalhes: [EFD-REINF - R-4010/R-4020](https://tdn.totvs.com/display/public/TAF/EFD-Reinf#EFDReinf-R-4010-Pagamentos/cr%C3%A9ditosabenefici%C3%A1riopessoaf%C3%ADsica)
