---
article_id: 4441309263383
category: NFe - Nota Fiscal Eletrônica
content_hash: f4e32d5b815c5c571757d9dee78e721d3158d0824a3ee3347fd3e9f5291b11fe
fetched_at: '2026-06-28T22:40:05.539094+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 941 Rejeição :
  Número do Regime especial inválido.'
type: support-article
updated_at: '2025-07-09T12:25:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441309263383-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-941-Rejei%C3%A7%C3%A3o-N%C3%BAmero-do-Regime-especial-inv%C3%A1lido
---

**Dúvida**Como solucionar a 941 Rejeição : Número do Regime especial inválido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para gerar a **TAG tpAto,** apenas através de ponto de entrada para solucionar essa dúvida, realize os seguintes passos:

1. Se campo ***tpAto* igual a *08* ou 10**verificar se campo ***nProc*** segue o padrão do regime especial da UF. A SEFAZ disponibiliza tabela com padrões e pode ser consultada em na aba ***“Documentos”, opção “Diversos” do Portal Nacional da NF-e.***

*[Clique Aqui](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/N|https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=)*

2. Para gerar a ***TAG procRef,*** somente através do Ponto de Entrada ***PE01NFESEFAZ,***verifique a documentação no link abaixo:

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=274327446)*

{code:java}  
//Processo referenciado  
For nX := 1 To Len(aProcRef)  
    cString += '<procRef>'  
    cString += '<nProc>'+aProcRef[nX][1]+ '</nProc>'  
    cString += '<indProc>'+aProcRef[nX][2]+ '</indProc>'  
    cString += '<tpAto>'+aProcRef[nX][3]+'</tpAto>'  
    cString += '</procRef>'  
Next nX{code}

**Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download?e=1152113)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

* ***Validação da Sefaz:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6501471571863)
