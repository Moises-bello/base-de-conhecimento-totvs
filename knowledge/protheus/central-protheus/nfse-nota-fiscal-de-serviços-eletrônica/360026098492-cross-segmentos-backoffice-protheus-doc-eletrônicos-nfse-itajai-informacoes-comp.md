---
article_id: 360026098492
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d894c3a340381324567971437d3afb836909af20fcd5dc9483ba4a27d54d966d
fetched_at: '2026-06-28T22:39:57.519390+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Itajai:
  Informacoes Complementares '
type: support-article
updated_at: '2025-07-02T14:16:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026098492-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Itajai-Informacoes-Complementares
---

**Dúvida**Como incluir Informações complementares na NFSe de Itajaí-SC?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Para que a tag InformacoesComplementares seja destacada no XML enviado a prefeitura de Itajaí-SC é preciso executar o procedimento abaixo:  
  
A informação complementar deve ser preenchida no campo C5\_MENPAD por meio de fórmula.  
Informe no wizard.config da rotina FISA022 versão 3.00.  
Utilize NFSEXMLENV e TSS atualizados conforme disponível no portal do cliente.  
Parâmetro MV\_NFSEMOD=.T.
