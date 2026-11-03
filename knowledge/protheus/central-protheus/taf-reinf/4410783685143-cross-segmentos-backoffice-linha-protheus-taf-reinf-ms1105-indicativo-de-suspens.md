---
article_id: 4410783685143
category: TAF - REINF
content_hash: acf085dc52e78925b77eb8ea1e956706715d69d104e5087a3d47efd3ce9d1bea
fetched_at: '2026-06-28T22:41:33.428037+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - BackOffice Linha Protheus - TAF - REINF - MS1105 - "Indicativo
  de Suspensão não cadastrado para o processo: tipo {0} número {1}")]'
type: support-article
updated_at: '2023-03-30T16:50:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410783685143-Cross-Segmentos-BackOffice-Linha-Protheus-TAF-REINF-MS1105-Indicativo-de-Suspens%C3%A3o-n%C3%A3o-cadastrado-para-o-processo-tipo-0-n%C3%BAmero-1
---

**Dúvida**

MS1105 - "Indicativo de Suspensão não cadastrado para o processo: tipo {0} número {1}")]  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF - Todas as versões  
  
**Solução**

Essa rejeição ocorre quando a informação do código de suspensão tem inconsistência no preenchimento dos campos de acordo com os parâmetros de validação previstos nos Leiautes / Manuais de Orientações da EFD Reinf. 

A tag codSusp (Código do indicativo da suspensão atribuído pelo contribuinte) esse código deve ser enviado no evento R-1070, para quando enviar a informação do código na tag codSusp em alguns dos eventos que gere essa informação não ocorra a rejeição MS1105 ao transmitir o evento que necessite enviar a informação de suspensão.

**Importante:**

A informação do código indicativo da suspensão deve estar recepcionada no portal do e-CAC, através do evento R-1070

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410783383831/mceclip0.png)**

O evento R-1070 é utilizado para inclusão, alteração e exclusão dos processos judiciais e administrativos que influenciam no cumprimento das obrigações tributárias principais e acessórias.

As informações consolidadas desta tabela são utilizadas para validação de outros eventos da EFD-Reinf e influenciam na forma e no cálculo dos tributos devidos.

Os indicativos de suspensão de exigibilidade {indSusp} que especificam as espécies de decisão, caso sejam favoráveis ao contribuinte, que devem ser informadas na EFD-Reinf são os seguintes:

01 - Liminar em Mandado de Segurança;

02 - Depósito Judicial do Montante Integral;

03 - Depósito Administrativo do Montante Integral;

04 - Antecipação de Tutela;

05 - Liminar em Medida Cautelar;

08 - Sentença em Mandado de Segurança Favorável ao Contribuinte;

09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF;

10 - Acórdão do TRF Favorável ao Contribuinte;

11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte;

12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte;

13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo;

90 - Decisão Definitiva a favor do contribuinte;

92 - Sem suspensão da exigibilidade.

Com relação às implicações dos processos {tpProc} administrativos [1] e judiciais [2] da empresa ou de entidade no cálculo dos tributos abrangidos pela EFD-Reinf, vale destacar o seguinte:

 Se {tpProc} = [1], o campo deve ser preenchido com [03, 90, 92].

 Se {tpProc} = [2], deve ser preenchido com [01, 02, 04, 05, 08, 09, 10, 11, 12, 13, 90, 92].

No TAF a origem dessas informações é a partir do cadastro de Processos Referenciados na rotina TAFA051 e posteriormente está informado na tabela T9Q (Indicativo de suspensão Processos Administrativos e Judiciais)

Processos Referenciados (TAFA051)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410783567639/mceclip1.png)

Processo Referenciado vinculado tabela T9Q no Documento Fiscal

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410791289239/mceclip2.png)

**Informações adicionais:**

Leiautes da EFD-Reinf

<http://sped.rfb.gov.br/arquivo/show/5710>

Tabela de Processos - TAFA051 - TAF -

<https://tdn.totvs.com/display/public/TAF/Tabela+de+Processos++-+TAFA051+-+TAF+-+P12>
