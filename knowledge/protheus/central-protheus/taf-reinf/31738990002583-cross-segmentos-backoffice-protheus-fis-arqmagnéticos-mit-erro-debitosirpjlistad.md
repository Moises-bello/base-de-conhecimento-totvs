---
article_id: 31738990002583
category: TAF - REINF
content_hash: 483fe01b0f46683855402c6a904f4a5765555385ef9440435d1512917933a35e
fetched_at: '2026-06-28T22:41:33.472159+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - MIT - Erro:
  Debitos.Irpj.ListaDebitos[id 1].CodigoDebito: valor informado inválido'
type: support-article
updated_at: '2025-04-29T13:30:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31738990002583-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MIT-Erro-Debitos-Irpj-ListaDebitos-id-1-CodigoDebito-valor-informado-inv%C3%A1lido
---

**Ocorrência**  
No portal do ECAC, ao tentar realizar a validação do arquivo Json MIT é apresentada o erro Debitos.\*\*\*\*.ListaDebitos[id 1].CodigoDebito: valor informado inválido.

**Ambiente**TOTVS Backoffice (Linha Protheus) - TAF - A partir da versão 12.1.2310  
  
**Causa**Esse incidente ocorre quando não é informado  incorreto o preenchimento do campo código de receita T1A\_CODREC incorreto o cadastro de inclusão do tributo na rotina TAFA632 para a Inclusão do tributo para geração do MIT.  
  
**Solução**  
  
1. Para solucionar essa ocorrência, informe no campo **CodigoDebito** **T1A\_CODREC** código de receita para um dos códigos padrão valido permitidos conforme o tributo cadastrado para gerar a o MIT:  
<https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/DCTFWeb/arquivos/manual-mit-1-0-14-02.pdf>

![codREC.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31738989973015)  
  
2. Acessa o cadastro na rotina TAFA632 para a inclusão do tributo acessa a opções de alterar o preenchimento dos dados para o campo CodigoDebito T1A\_CODREC código de receita com um código valido para gerar o registro:  
![](https://tdn.totvs.com/download/attachments/904594705/image-2025-2-14_15-54-4.png?version=1&modificationDate=1739559244513&api=v2)

3. Para o campo **CodigoDebito T1A\_CODREC** código de receita informa o código de receita valido somente numero sem o hífen/traço (Código de receita + a Variação) Exemplo  512301.  
![TAF_CODREC MIT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31739003663639)

Conforme o padrão, o código de receita para DCTF Web MIT e necessário preencher com o código de receita + a Variação.

MIT - Módulo de Integração de Tributos:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=904594705>

De\Para (TAGS do layout **MIT** x Campos **TAF**)

|  |  |  |  |
| --- | --- | --- | --- |
| ListaDebitos ou ListaDebitosAposEvento | 21 | CodigoDebito | T1A\_CODREC |
