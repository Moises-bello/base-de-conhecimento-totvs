---
article_id: 360048966994
category: ADVPL - Classe e Função
content_hash: 0e968846ea64a5439a1c4e439c05d276ec1782b43366c63a65ff128bae5ae531
fetched_at: '2026-06-28T22:40:19.501346+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FWMarkBrowse propriedade
  setDescription: Dinâmico'
type: support-article
updated_at: '2022-01-11T14:15:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048966994-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FWMarkBrowse-propriedade-setDescription-Din%C3%A2mico
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Utilizando a **FWMarkBrowse** é possível alterarmos a propriedade **setDescription** em tempo de execução?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.17  
  
**Solução**A **FwMarkBrowse** é uma classe raiz que não utiliza herança direta das outras classes de browse.  
Porém, ela tem um atributo de Browse que é da classe **FwMBrowse**, que herda da FwFormBrowse, que por sua vez herda da FwBrowse, que contém um atributo de Browse que é responsável pela interface com o usuário.  
Quando é chamada a **SetDescription** da **FwMarkBrowse** são feitas indireções até chegar à raiz e a configuração da descrição no componente de interface.  
Todas essas classes de Browse funcionam no modelo de configuração prévia com ativação posterior e por isso o **SetDescription** precisa ser feito antes da ativação da classe.  
Caso ela tenha uma alteração depois da ativação, ela não irá ser refletida na tela, pois o componente visual já foi carregado e não passa por nenhum processo de atualização.
