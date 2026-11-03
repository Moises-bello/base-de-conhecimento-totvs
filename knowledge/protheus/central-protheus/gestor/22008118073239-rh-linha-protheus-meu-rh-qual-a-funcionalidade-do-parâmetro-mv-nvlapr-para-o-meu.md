---
article_id: 22008118073239
category: GESTOR
content_hash: f5dc32d0c96cd5a9e577b8d0839786d4011aa3bb04b079ac6942cf30e6564577
fetched_at: '2026-06-28T22:44:35.476602+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - Meu RH - Qual a funcionalidade do parâmetro MV_NVLAPR
  para o Meu RH
type: support-article
updated_at: '2026-06-24T18:13:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22008118073239-RH-Linha-Protheus-Meu-RH-Qual-a-funcionalidade-do-par%C3%A2metro-MV-NVLAPR-para-o-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22008118040087) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Qual a funcionalidade do parâmetro MV\_NVLAPR para o Meu RH  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
O parâmetro **MV\_NVLAPR** tem o conceito de, impor ao fluxo de aprovações das requisições feitas pelos funcionários, uma nova maneira de serem direcionadas aos Gestores.  
  
Caso o parâmetro **MV\_NVLAPR**estiver habilitado como ".T." e o campo Nível de Aprovação estiver com o conteúdo "0", informa que essa solicitação não possui superior, ou seja, qualquer requisição realizada **será direcionada automaticamente para a avaliação final do RH**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22008112034199)  
  
Nível de Aprovação na **rotina Menus do módulo 18 - SIGATCF:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22008112035607)  
  
Caso o parâmetro **MV\_NVLAPR**estiver habilitado como ".F." ou mesmo não existir em sua base de dados, e o campo Nível de Aprovação estiver com o conteúdo "0", a aprovação **será submetida as avaliações para todos os níveis da sua estrutura organizacional.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22008118048791)**  
  
**IMPORTANTE:**  
Caso houver necessidade de **reduzir a quantidade de aprovações**, é possível mediante cenário a seguir:  
  
**O parâmetro MV\_NVLAPR nesse caso, precisará estar desabilitado.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30111202139159)  
  
O nível de aprovação de cada requisição, será definido no menu **Portal RH de número 000006**, na rotina **Atualizações > Configurações > Menu dentro do módulo 18 do Protheus.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30111196422935)  
  
Clique em **Outras Ações > Menu**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30111196423447)  
  
No menu Solicitações, escolher o processo que precisará ser reduzida a quantidade de aprovações.  
  
Marcação de Ponto por exemplo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30111196423959)  
  
Com isso, **toda requisição de Marcação de Ponto, terá somente 1 nível de aprovação**, ou seja, apenas um Gestor irá aprovar, mesmo que tenha que um Superior, antes do RH atender dentro do Protheus.  
  
Lembrando que a **última aprovação sempre, em qualquer hipótese, será da equipe do RH** dentro do Protheus.  
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
