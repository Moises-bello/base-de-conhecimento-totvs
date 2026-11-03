---
article_id: 11898883231127
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 60cef0872c8da977a91d5982e96351c70f1daa00d70e91ecad07ef37e4d4d17c
fetched_at: '2026-06-28T22:42:02.261636+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar os registros C855/C857 a partir do layout 17?
type: support-article
updated_at: '2023-01-24T13:39:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11898883231127-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-os-registros-C855-C857-a-partir-do-layout-17
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar os registros **C855 - Observação do Lançamento Fiscal (Modelo 59)** e **C857 - Outras Obrigações Tributárias, Ajustes e Informações provenientes de Documento Fiscal**  a partir do Layout 017 do Sped Fiscal?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

**Registro tipo C855 – OBSERVAÇÕES DO LANÇAMENTO FISCAL (CÓDIGO 59) - Perfil A**

Este registro é gerado a partir do livro fiscal, fazendo o relacionamento do documento com a observação lançada no registro **0460**, quando o documento tiver algum lançamento de apuração ou quando tiver as informações lançadas na coluna **Observação**na escrituração dos **Livros Fiscais de saídas.**No sistema, a espécie que trata automaticamente o **modelo 59** é a **SATCE**.

**Registro tipo C857 – OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE VALORES PROVENIENTES DE DOCUMENTO FISCAL (CÓDIGO 59) - Perfil A**

Este registro é gerado a partir da tabela de lançamentos do documento fiscal **(CDA)** para apuração. O campo **Lançamentos de Apuração de ICMS (CDA\_TPLANC)** passa a ser obrigatório quando inserido manualmente no documento fiscal.

Para códigos de lançamento iniciados por **"9"** é possível configurar o valor a ser gravado através do campo **"Vl.Reg.197" (CE0\_VL197)** no cadastro de códigos de reflexo (**FISA072**), determinando sua gravação no campo **07-VL\_ICMS** ou **08-VL\_OUTROS**.   
Para mais informações da rotina **FISA072**, acesse o *link*:   
<https://tdn.totvs.com/pages/releaseview.action?pageId=640907320>

Também é possível configurar o comportamento da apresentação dos valores neste registro via Configurador de Tributos.   
Para mais informações sobre essa opção consulte o *link*:   
<https://tdn.totvs.com/pages/releaseview.action?pageId=673778506>
