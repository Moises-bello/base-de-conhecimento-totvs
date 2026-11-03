---
article_id: 360017782231
category: eSocial - Gerar XML/ Integração Evento
content_hash: 8884a0dc3d5dd6afbd2e609f76e940fa38b7c62bff825ce083ed520d6e0b9c5c
fetched_at: '2026-06-28T22:47:12.277944+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro de schema ao transmitir XML para o governo
type: support-article
updated_at: '2026-06-15T12:30:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017782231-RH-RM-FOP-eSocial-Erro-de-schema-ao-transmitir-XML-para-o-governo
---

**Ocorrência**Ao transmitir o XML para o governo ocorre erro de *schema **This element is not expected*** ou ***is not a valid value of the local atomic type**.*  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro é apresentado quando o XML enviado não está respeitando as regras de *schema* definidos pelo governo, ou seja, quando a estrutura do XML não está de acordo com o esperado como, por exemplo, alguma *tag* sem valores ou *tag* com valor numérico porém o *schema* de XML não permite valor numérico.  
  
**Solução**Para solucionar o erro, siga os passos de validação abaixo:

**• '' *is not a valid value of the local atomic type***

1. Verifique na mensagem do erro apresentada qual a *tag* inválida. No exemplo abaixo, o erro indica que na *tag* **dia** o valor '' (vazio) não é válido;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062027993/mceclip1.png)

2. Abra os XML do RM e TAF e pesquise pela *tag* indicada no erro. No exemplo abaixo, de acordo com o erro apresentado no passo 1, a *tag* **dia** gerou sem valor sendo assim ocorrerá erro;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062027473/mceclip0.png)

3. Neste caso, procure o atendimento do RM ou TAF (considerando o XML que está gerando a informação errada) com as evidências para análise. 

**• 'x' *is not a valid value of the local atomic type***

1. Verifique na mensagem do erro apresentada qual a *tag* inválida. No exemplo abaixo, o erro indica que na *tag* **codIncCP** o valor **'0'** não é válido;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6844285063959/mceclip1.png)

2. Abra os XML do RM e TAF e pesquise pela *tag* indicada no erro. No exemplo abaixo, de acordo com o erro apresentado no passo 1, a *tag* **codIncCP** gerou valor **0**, porém a *tag* precisa ser gerada como **00** (dois caracteres) conforme definição do leiaute;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6844304797591/mceclip3.png)

3. É importante verificar no leiaute do eSocial que tipo de informação e a quantidade de caracteres necessárias conforme descrição modelo abaixo;

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6844348287895/mceclip7.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6844386071703/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6844387008919/mceclip6.png)

4. Verifique no Mapeamento do eSocial a origem da *tag.* Sendo uma informação preenchida pelo usuário, corrija o campo preenchido no sistema. Sendo uma informação gerada internamente pelo sistema, acione o atendimento técnico com as evidências para análise.

- [Mapeamento dos eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679)

**• *This element is not expected***

1. Verifique na mensagem do erro apresentada qual a *tag* não era esperada e qual era a esperada pelo governo. No exemplo abaixo, o erro indica que a *tag* **ageIntegracao** não era esperada na ordem do XML, pois a *tag* esperada era a **instEnsino**;

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6844590360471/mceclip10.png)

2. Abra os XML do RM e TAF e pesquise pela *tag* indicada no erro. No exemplo abaixo, de acordo com o erro apresentado no passo 1, a *tag* pesquisada foi **ageIntegração**;

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6844464560791/mceclip8.png)

3. Conforme leiaute, o grupo **instEnsino** é obrigatório e, por isso, era esperado antes do grupo **ageIntegracao**;

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6844491121175/mceclip9.png)

4. Sendo assim, verifique no Mapeamento do eSocial a origem da tag. Sendo uma informação preenchida pelo usuário, corrija o campo preenchido no sistema. Sendo uma informação gerada internamente pelo sistema, acione o atendimento técnico com as evidências para análise.

- [Mapeamento dos eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679)

**Saiba mais**  
Acesse o link abaixo para baixar os *layouts* do eSocial:  
      • [Documentação Técnica](https://portal.esocial.gov.br/institucional/documentacao-tecnica)
