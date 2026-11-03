---
article_id: 17736594538647
category: GESTOR
content_hash: 7542cd2db96571f41ba8468dd5b76b7dad3dd52f85a04f8b30fbb425cd7ee484
fetched_at: '2026-06-28T22:44:35.513202+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - Meu RH - Cadastro de hierarquia de departamentos somente
  aceita Gestor e Funcionários da mesma filial
type: support-article
updated_at: '2025-11-05T21:18:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17736594538647-RH-Linha-Protheus-Meu-RH-Cadastro-de-hierarquia-de-departamentos-somente-aceita-Gestor-e-Funcion%C3%A1rios-da-mesma-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17736623909911) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Cadastro de hierarquia de departamentos somente aceita Gestor e Funcionários da mesma filial  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Esta particularidade de quando o Gestor é de uma filial e o time de outra, somente irá ser aceita pelo Sistema, para montagem de hierarquia, se **a tabela SQB - Departamentos, for totalmente compartilhada,** porém, **se a tabela for exclusiva**, como premissa da hierarquia de aprovação, faz-se necessário que o **Gestor esteja na mesma filial de seus subordinados**, não sendo possível o time estar em uma filial e o Gestor em outra.  
  
Exemplo de uma SQB exclusiva:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17736260072727)  
  
Exemplo de uma SQB compartilhada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17736377245591)  
  
Ou seja, **quando a tabela SQB é exclusiva, não é possível criar uma hierarquia com departamentos de filiais distintas**.   
  
Para se criar uma hierarquia entre os departamentos, independente a qual filial elas pertençam, a tabela **SQB deverá ser compartilhada**.   
  
O comportamento do sistema é dessa forma, sendo necessário uma abertura de uma sugestão de melhoria na nossa central colaborativa.  
[RH - Linha Protheus - Meu RH - Como abrir um processo de Melhoria para o App Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10563960514327-RH-Linha-Protheus-Meu-RH-Como-abrir-um-processo-de-Melhoria-para-o-App-Meu-RH?source=search)  
 **Importante!**Está orientação  é válida especificamente ao conteúdo do parâmetros **MV\_ORGCFG = 0**, ou seja, a hierarquia de aprovação totalmente voltada ao Cadastro de Departamentos  
  
**Saiba Mais**[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**  
[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)[Artigos sobre Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-Meu-RH)**
