---
article_id: 4403022584727
category: eSocial - Tabelas/Não Periódicos
content_hash: 0b54f64fac5c6d6985166164cb2b4a4b1a923d52f60b62369389f74cadc5f0f5
fetched_at: '2026-06-28T22:47:10.322780+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 244 ao enviar S-1010: Natureza da rubrica inválida'
type: support-article
updated_at: '2024-06-26T18:02:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403022584727-RH-RM-FOP-eSocial-Erro-244-ao-enviar-S-1010-Natureza-da-rubrica-inv%C3%A1lida
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446237626647)**Tempo aproximado para leitura: **00:01:30 min  
  
Ocorrência**Ao enviar o S-1010 ocorre o erro de código **244: Natureza de rubrica inválida**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6345805896215)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando a natureza de rubrica enviada através da *tag* **natRubr** do S-1010 está com **validade expirada** ou o **código está incorreto**.​​​​

**Solução**

1. Acesse o XML S-1010 que consta com o erro e identifique a **natRubr** no XML;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403022532759)

2. Acesse a Documentação Técnica do Governo, **[Tabelas de Natureza das Rubricas](https://frontend.esocial.gov.br/adm/Home/Index)** e identifique se a validade consta com a data Término preenchida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24446839437079)

3. Caso esteja com a data término vencida, será necessário alterar a Natureza da Rubrica do evento para uma que esteja vigente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24446854736407)

4. Após regere o XML S-1010 e integre com o governo. 

**Importante**  
A TOTVS não orienta qual natureza de rubrica deve ser informadas nas verbas, ficando tal escolha a cargo da própria empresa. O que podemos orientar é que a natureza esteja condizente com o Anexo I do *Layout* eSocial utilizado.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:

* [Documentação Técnica - eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
* [Onde informar a natureza de rubrica eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403023133719)
