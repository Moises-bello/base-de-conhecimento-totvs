---
article_id: 360059545133
category: RH - Banco De Horas
content_hash: 00df0e711e97377cfd64590395a5ad46ede077296b4df5611bd8ea6d8b6e369c
fetched_at: '2026-06-28T22:44:54.225673+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Como levar apenas o Saldo de Banco de Horas para
  os Resultados
type: support-article
updated_at: '2025-09-16T12:41:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059545133-RH-Linha-Protheus-PON-Como-levar-apenas-o-Saldo-de-Banco-de-Horas-para-os-Resultados
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34971944562583) Tempo aproximado para leitura: 00:01:30 min**Dúvida**Como levar apenas o Saldo para os resultados após Fechamento do Banco de Horas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Foi criada uma **nova pergunta** na rotina de **Fechamento de Banco de Horas** para indicar se deve ser gerado apenas o **Saldo** ou as verbas de **provento** e **desconto**.  
  
**IMPORTANTE:** Em casos de transferências de Centro de Custo, caso queira que o saldo do período do banco seja enviado para a rotina de Resultados no centro de custo destino, é necessário que antes da transferência seja informado no parâmetro MV\_ARQTRAN a tabela SPI-Movimento do Banco de Horas, assim, no momento da transferência o sistema irá transferir os movimentos da tabela para o novo centro de custo.  
  
Caso a transferência seja executada sem a tabela no parâmetro, os dados da tabela não serão transferidos e na baixa do banco, esses mesmos lançamentos ficarão no centro de custo origem.

* [RH - Linha Protheus - GPE - Como executar a transferência migrando os registros das tabelas do Ponto para a Filial e Centro de Custo Destino](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013366292-RH-Linha-Protheus-GPE-Como-executar-a-transfer%C3%AAncia-migrando-os-registros-das-tabelas-do-Ponto-para-a-Filial-e-Centro-de-Custo-Destino)
* [Exemplo de Uso](https://tdn.totvs.com/pages/releaseview.action?pageId=733188283#tabs-passo1)
* [Informações Técnicas](https://tdn.totvs.com/pages/releaseview.action?pageId=733188283#tabs-passo2)

Abaixo exemplo: Lançamentos no Banco de Horas **resultam em um Saldo positivo de 2 horas:** 

![Lançamento de Banco de Horas](https://tdn.totvs.com/download/attachments/733188283/image2023-1-13_15-41-22.png?version=1&modificationDate=1673636333953&api=v2&effects=drop-shadow "Lançamento de Banco de Horas")

No momento do **Fechamento do Banco de Horas,** a nova pergunta **Apenas Saldo nos Resultados?** foi parametrizada com **Sim:**

![Nova pergunta na rotina de fechamento de banco de horas](https://tdn.totvs.com/download/attachments/733188283/image2023-1-13_15-43-23.png?version=1&modificationDate=1673636333843&api=v2&effects=drop-shadow "Nova pergunta na rotina de fechamento de banco de horas")

Nos Resultados, **apenas a verba de provento será gerada**, com as duas horas de saldo do Banco:

![Verba gerada nos resultados](https://tdn.totvs.com/download/attachments/733188283/image2023-1-13_15-44-31.png?version=1&modificationDate=1673636333720&api=v2&effects=drop-shadow "Verba gerada nos resultados")

Caso a pergunta **Apenas Saldo nos Resultados?** esteja com **Não,** serão geradas as verbas de **Provento e Desconto:**![Verbas de Provento e Desconto geradas nos resultados](https://tdn.totvs.com/download/attachments/733188283/image2023-1-13_15-51-6.png?version=1&modificationDate=1673636333587&api=v2&effects=drop-shadow "Verbas de Provento e Desconto geradas nos resultados")  
  
****Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**[RH - Linha Protheus - PON - Como efetuar o fechamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas?source=search)  
[RH - Linha Protheus - PON - Após o Fechamento de Banco de Horas, como fazer para as verbas não sumirem com um novo cálculo mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057318554-RH-Linha-Protheus-PON-Ap%C3%B3s-o-Fechamento-de-Banco-de-Horas-como-fazer-para-as-verbas-n%C3%A3o-sumirem-com-um-novo-c%C3%A1lculo-mensal)  
[RH - Linha Protheus - PON - Fechamento banco de horas não está sendo processado para os resultados do ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035129974-RH-Linha-Protheus-PON-Fechamento-banco-de-horas-n%C3%A3o-est%C3%A1-sendo-processado-para-os-resultados-do-ponto)
