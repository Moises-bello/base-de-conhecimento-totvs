---
article_id: 360015506452
category: eSocial - Cadastros
content_hash: 824545fba7e2925ce12b1a2e8f4b756d8da6d9445c7ddaf287427c566bf04926
fetched_at: '2026-06-28T22:47:14.513456+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Identificação da origem da Lotação Tributária
type: support-article
updated_at: '2024-10-21T11:59:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015506452-RH-RM-FOP-eSocial-Identifica%C3%A7%C3%A3o-da-origem-da-Lota%C3%A7%C3%A3o-Tribut%C3%A1ria
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22926105153687)**Tempo aproximado para leitura:**00:03:15 min  
  
Dúvida**Como identificar qual registro deu origem à Lotação Tributária?   
  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Lotação tem o conceito estritamente tributário e não físico e influi no método de cálculo da contribuição previdenciária para um grupo de segurados específicos, não refletindo, necessariamente, o local de trabalho do empregado. Identifica a classificação da atividade para fins de atribuição do código **FPAS**, a obra de construção civil, o contratante de serviço, ou uma condição diferenciada de tributação. A condição diferenciada ocorre quando uma determinada unidade da empresa possui um código de **FPAS**/Outras Entidades e Fundos distintos.

Desta forma, o sistema irá gerar lotações conforme abaixo:  
• Empresas que **não utilizam** tomadores de serviço  
Será gerado:  
    1 registro para cada **seção centralizadora** de CNPJ  
  
Ou em caso de uso de quebra de **FPAS**:  
    1 registro para cada **seção** que se enquadre na **quebra de FPAS**

• Empresas que **utilizam** tomadores de serviço  
Será gerado:  
    1 registro para cada **seção centralizadora+tomador global** +   
    1 registro para cada **seção centralizadora+tomador** em que houver tomador alocado para algum funcionário  
  
Ou em caso de uso de quebra de **FPAS**:  
    1 registro para cada **seção+tomador global** +   
    1 registro para cada **seção+tomador** em que houver tomador alocado para algum funcionário +   
    1 registro para cada **seção** que se enquadre na **quebra de FPAS**

**Saiba mais**  
Para mais informações sobre Lotação Tributária, acesse:  
   • [Como identificar qual registro deu origem à Lotação Tributária?](http://tdn.totvs.com/pages/viewpage.action?pageId=504807048)  
   • [Lotação tributária (S-1020) quando não utilizado tomadores de serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033722793)  
   • [Lotação tributária (S-1020) para empresas que utilizam tomadores de serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015470032)
