---
content_hash: fa6d3d51b9a9bd47954105a4fb677d7c41110e1020644824f19d7c0326dae57a
fetched_at: '2026-06-29T00:09:15.384430+00:00'
page_id: '421385363'
product: rm
source: tdn-rm
title: Cenários Cópia de Itens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385363
version: 2
---

---

Para permitir a cópia de itens entre Cenários foi criado a aba Cenários onde é possível verificar os campos origem e destino da cópia, sendo que as Planilhas de Atividades e Serviços não ficam disponíveis como destino.   
 Todo Cenário somente poderá ser copiado por inteiro e para que não haja duplicidade de dados caso o Cenário de destino contenha dados, é necessário marcar a opção "Excluir informações do cenário destino antes da cópia", caso contrário o processo de cópia será abortado e o Cenário não será copiado.

Como as planilhas principais, Atividades e Serviços, compartilham a mesma base de informações (Insumos e Composições), no momento da copia serão considerados apenas Insumos e Composições associados a atividades e serviços.

**Atenção:**  
 Não serão copiados insumos cadastrados que não estiverem associados como recurso a Atividades ou Serviços. Não serão copiados insumos vinculados a uma composição que não esteja vinculada como recurso de uma Atividade ou Serviço. Não serão copiadas Composições cadastradas que não estiverem associadas como recurso de uma Atividade ou Serviço.

**Observações:**   
 Ao ser copiado um conteúdo de um Cenário, ele todo será copiado, ou seja, não é possível copiar apenas alguns dados de uma planilha/cenário para outra.

Quando a cópia for efetuada dentro de um mesmo projeto, o cenário origem deve ser diferente do cenário destino.
