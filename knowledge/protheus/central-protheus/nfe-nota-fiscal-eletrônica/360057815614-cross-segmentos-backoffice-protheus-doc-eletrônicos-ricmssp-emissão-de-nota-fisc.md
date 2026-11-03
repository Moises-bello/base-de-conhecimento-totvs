---
article_id: 360057815614
category: NFe - Nota Fiscal Eletrônica
content_hash: 54d5da68f82994211fc4b4994120b2cec688af1c8ad58e650a7c507e4ae2f7f5
fetched_at: '2026-06-28T22:40:00.185824+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: '   Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - RICMS/SP - Emissão
  de Nota Fiscal com a Expressão - Diversos/Brindes'
type: support-article
updated_at: '2021-10-08T17:11:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057815614--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-RICMS-SP-Emiss%C3%A3o-de-Nota-Fiscal-com-a-Express%C3%A3o-Diversos-Brindes
---

**Dúvida**Como configurar no Protheus RICMS/SP - Emissão de Nota Fiscal com a Expressão - Diversos/Brindes ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

*1 - no quadro “Destinatário/Remetente”, no campo **“Nome/Razão Social”, a expressão “Diversos - Brindes”** e nos demais campos, os dados do emitente;*

* Preencher no cadastro de cliente os campos **Nome A1\_NOME e N Fantasia A1\_NREDUZ**

![cliente.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100286293/cliente.png)

* **Observação:**

Caso seja cadastro de fornecedor, preencher os campos **Razão Social A2\_NOME e N Fantasia A2\_NREDUZ**

![forne.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100290233/forne.png)

*2 - no campo “Código Fiscal de Operações e Prestações - **CFOP”, o código 5.949;***

* Preencher o CFOP no TES da nota no campo **Cod****. Fiscal "F4\_CF"**

![cfop.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098028194/cfop.png)

*3 - no campo “Informações Complementares”, a expressão “Nota Fiscal emitida nos termos do inciso II do art. 456 do RICMS - Nota Fiscal de aquisição nº ..., de.../.../...”;*

* Utilizar os campos padrões do sistema para gerar a **mensagem em informações complementares, conforme os links abaixo:**

[MP-NFE- Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)

[MP-NFE- Gerar mensagem em informações complementares do Danfe utilizando fórmula ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

***Caso não possa realizar os processos acima,** para que o XML e o Danfe atenda sua necessidade há **duas opções de processos** a ser seguido:  
  
1-Primeira opção pode ser customizado o **NFESEFAZ .**  
  
[MP - NFE - Documentos Eletrônicos NFe / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493-MP-NFE-Documentos-Eletr%C3%B4nicos-NFe-NFSe-MDFe-MDe-?source=search)  
  
**Rdmake disponível no link acima.**  
  
2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)***

* ***Saiba mais:***

*[Parecer da consultoria](https://tdn.totvs.com/pages/viewpage.action?pageId=571789783)*
