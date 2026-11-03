---
content_hash: 85c6ff858351279d8b5b3ab9ba5c51d561627525e97e6a5498d9669c26f6e8e5
fetched_at: '2026-06-29T00:10:03.257678+00:00'
page_id: '452719075'
product: rm
source: tdn-rm
title: Sincronização Centro de Custo global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719075
version: 3
---

Este processo realiza a sincronização no centro de custo do Folha de Pagamento, baseado no centro de custo global utilizado nos outros módulos da linha RM. Após realizar qualquer alteração nos centros de custos globais, que tenham seus códigos cadastrados no centro de custo (Folha de Pagamento), será possível a sincronização das informações automaticamente.  
   
Este processo realiza a atualização dos seguintes campos no centro de custo do Folha de Pagamento.  
 

* Flag 'Ativo'
* Flag 'Permite Lançamento'
* Campo 'Descrição'

O campo 'Código Centro Custo Global', não é atualizado através deste processo.

**Observação:**

A contabilização permite gerar lançamentos contábeis sem a obrigatoriedade de haver Centros de Custos Globais associados ao Centros de Custo (Folha de Pagamento).

Durante o processo de contabilização o sistema precisa verificar se o centro de custo informado está ativo, esta verificação ocorre da seguinte forma:

Se o campo 'Código Centro Custo Global' que fica localizado no cadastro de centro de custo do Folha de Pagamento, estiver:

* Preenchido: O sistema verifica se o centro de custo global está ativo.
* Vazio: O sistema verifica se o centro de custo do Folha de Pagamento está ativo.

A segunda opção possui uma melhor performance uma vez que não é necessário verificar se o centro de custo global está ativo, já que uma vez executado o processo de sincronização a flag 'Ativo' de ambos os centros de custo (Global e Folha de Pagamento) ficarão iguais.
