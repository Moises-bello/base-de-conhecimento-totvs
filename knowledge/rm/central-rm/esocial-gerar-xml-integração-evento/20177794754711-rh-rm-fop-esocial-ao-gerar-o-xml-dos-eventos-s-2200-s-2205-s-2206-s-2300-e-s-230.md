---
article_id: 20177794754711
category: eSocial - Gerar XML/ Integração Evento
content_hash: 78fd718c2b7530a799256d8e9c06fd6dcbc58cb43c7c057d50a6bf1b03c475d5
fetched_at: '2026-06-28T22:47:11.923780+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Ao gerar o XML dos eventos S-2200, S-2205, S-2206,
  S-2300 e S-2306 ocorre erro de Schema codMunic
type: support-article
updated_at: '2026-04-17T19:29:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20177794754711-RH-RM-FOP-eSocial-Ao-gerar-o-XML-dos-eventos-S-2200-S-2205-S-2206-S-2300-e-S-2306-ocorre-erro-de-Schema-codMunic
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20177794720023) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o XML dos eventos S-2200, S-2205, S-2206, S-2300 e S-2306 ocorre o(s) erro(s) de Schema codMunic abaixo:  
  
Erro de schema: Element '{<http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00>}codMunic': [facet 'pattern'] The value 'XXXXX' is not accepted by the pattern '\d{7}'.  
Ou:  
Erro de schema: Element '{[http://www.esocial.gov.br/schema/evt/evtAltCadastral/v\_S\_01\_02\_00}codMunic](http://www.esocial.gov.br/schema/evt/evtAltCadastral/v_S_01_02_00%7DcodMunic)': [facet 'pattern'] The value '03957' is not accepted by the pattern '\d{7}'.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**  
O erro ocorre quando é gerado no XML um Código de Município diferente do que consta na Tabela do IBGE.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20177794723735)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **eSocial | Endereços | Municípios**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20177783513879)

2. Identifique e selecione o **Município do cadastro do Funcionário | Anexos | Codificação de Município;**

![](https://totvssuporte.zendesk.com/attachments/token/VbzXG7eL48QDW6Gc1kCRTeFCM/?name=image.png)

3. Alterar a Codificação de Município do RM de acordo com o Código da Tabela de Municípios do IBGE(o código informado deve possuir 7 dígitos);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20177842461847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20177794728855)

**Saiba mais**  
Para mais informações, acesse:  
- [Códigos dos municípios IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php)   
- [Como realizar a liberação de acesso aos cadastros de endereço na aba eSocial?](https://tdn.totvs.com/pages/viewpage.action?pageId=361449123)
