---
article_id: 23477930254999
category: RH - Folha de Pagamento
content_hash: cf211908a94a438032cbb847a259aeebdc88991cc1e4d656aa5da405235b569c
fetched_at: '2026-06-28T22:44:11.994196+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - AUDESP - Alteração Folha Ordinária e Suplementar
  - Código do Cargo
type: support-article
updated_at: '2025-07-23T17:30:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23477930254999-RH-Linha-Protheus-GPE-AUDESP-Altera%C3%A7%C3%A3o-Folha-Ordin%C3%A1ria-e-Suplementar-C%C3%B3digo-do-Cargo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23477914647063)  Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Como gerar o campo Código do Cargo no XML Remunerações - Folha Ordinária  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.33.  
  
**Solução**Conforme informado no Comunicado [**AUDESP 23/2023**](https://www.tce.sp.gov.br/legislacao/comunicado/alteracao-folha-ordinaria-e-suplementar-codigo-cargo)**,** reiteramos a todos os jurisdicionados (Estado e Municípios) que os documentos de **Remunerações** passaram por alteração, exigindo que o cargo seja informado **obrigatoriamente.**  
  
Desta forma, será necessário **remover** o elemento **Estagiário** e incluir **um dos três abaixo**:

* + **CodigoCargo;**
  + **CodigoFuncao;**
  + **OutraOcupacao;**

Efetuado ajuste na rotina Audesp - Atos de Pessoal (GPEM920) para alteração no XML Remunerações - Folha Ordinária.

A geração do campo **OutraOcupacao** utilizará a configuração da **Categoria do eSocial (RA\_CATEFD)** Conforme abaixo:

1 **Estagiário** (901)

2 **Conselheiro** (305/301)

3 **Bolsista**  (903)

4 **Jovem Aprendiz** (103)

Para o tipo 5 - **Aposentado,** será utilizado a situação do Cadastro de Agentes Públicos RS9\_SITUAC (2 - Aposentado)  
  
Caso o funcionário não pertença a nenhuma categoria ou situação acima, será gerado como **CodigoCargo** ou **CodigoFuncao.**  
  
**Exemplo:**

- XML da Folha Ordinária, categoria E-social 301:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23479563054231)

Neste caso gerou o campo **OutraOcupação:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23479563060759)

- XML da Folha Ordinária, categoria E-social 101:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23479524243607)

Neste caso gerou o campo CódigoFunção:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23479524253335)

**Saiba mais:**<https://www.tce.sp.gov.br/legislacao/comunicado/alteracao-folha-ordinaria-e-suplementar-codigo-cargo>  
<https://www.tce.sp.gov.br/legislacao/comunicado/campo-obrigatorio-documentos-remuneracao-fase-iii-sistema-audesp>  
<https://www.tce.sp.gov.br/audesp/documentacao?tipo=61&termo=>  
<https://www.tce.sp.gov.br/legislacao/comunicado/atualizacao-audesp-fase-iii-remuneracoes>  
<https://tdn.totvs.com/pages/releaseview.action?pageId=834822425>  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058619654-RH-Linha-Protheus-GPE-AUDESP-Como-gerar-verbas-remunerat%C3%B3rias-na-folha-ordin%C3%A1ria>
