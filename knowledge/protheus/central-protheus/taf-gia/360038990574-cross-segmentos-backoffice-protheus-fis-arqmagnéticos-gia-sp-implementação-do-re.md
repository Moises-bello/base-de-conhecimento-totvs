---
article_id: 360038990574
category: TAF - GIA
content_hash: 0fe62daffde6365d5ae0336b31a12456f21aafedc0927af493765ef4211eb322
fetched_at: '2026-06-28T22:41:32.371590+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-SP - Implementação
  do Relatório da Nova GIA SP, rotina TAFRGSP
type: support-article
updated_at: '2024-06-04T19:14:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038990574-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIA-SP-Implementa%C3%A7%C3%A3o-do-Relat%C3%B3rio-da-Nova-GIA-SP-rotina-TAFRGSP
---

**Dúvida**  
Como implementar no Protheus o **Relatório da GIA SP**.  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Aplique o *patch* conforme a versão e *release* do **Protheus**, que está em anexo;  
  
2. Execute o compatibilizador **UPDDISTR** (**versão 12**) com o dicionário de dados que está em anexo, para criar o **grupo de perguntas** (**SX1**): \*  
- Baixe o arquivo diferencial **sdfbra.txt** na pasta *systemload*;   
- Execute o compatibilizador **upddistr**;  
- Aguarde a execução do **upddistr**.  
  
\* Recomendamos sempre realizar um *backup* e efetuar a primeira atualização no ambiente de homologação.  
  
3. Crie manualmente o menu da rotina **TAFRGSP**No **Configurador (SIGACFG)** acesse **Ambiente/ Cadastros/ Menus** e inclua, no *menu* do módulo **TOTVS Automação Fiscal (SIGATAF)**, a opção para execução do relatório **Conferência NOVA GIA SP**, conforme especificação a seguir:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051134054)

Importante:  
Para mais informações sobre inclusão de rotinas no **menu**:   
PSIGABD0006 - **CFGX013** - Inclusão de rotina no **Menu**.

*Link*: <http://tdn.totvs.com/pages/releaseview.action?pageId=219693837>

Segue *link* do procedimento para execução do **UPDDISTR**:

[https://tdn.totvs.com/x/nJLYCg](https://www.google.com/url?q=https://tdn.totvs.com/x/nJLYCg&sa=D&source=hangouts&ust=1574770327926000&usg=AFQjCNFkDSkih5Xm_a0Kzd4pZ7OiCiinpQ)Anexo, documento técnico da correção efetuada no fonte TAFRGSP.PRW - **Nova GIA SP**:

<https://tdn.totvs.com/pages/releaseview.action?pageId=516220646>
