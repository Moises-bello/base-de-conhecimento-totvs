---
content_hash: 6c2cf0587dff3b7e23aa2b96a22ee02639ef3c88840abf042e62404a3b75b7d1
fetched_at: '2026-06-29T00:09:54.210410+00:00'
page_id: '442961591'
product: rm
source: tdn-rm
title: Renumerar Períodos Estorno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=442961591
version: 2
---

O sistema irá refazer a numeração dos períodos de estorno, para que não haja "buracos" na numeração dos mesmos, por exemplo, depois da exclusão de período(s).

**Períodos de Estorno**:  
   
 Incluir: Insere um novo período de estorno.  
   
 Excluir: Exclui um período de estorno existente  
   
 A geração de período de estorno ocorre de duas formas:  
   
 1- Ao executar o processo de "Cancelamento de Liberação" 

Será gerado um período de estorno medido e liberado de forma AUTOMÁTICA com o mesmo valor do período ao executar o Cancelamento de Liberação caso o status do seu movimento relacionado seja PENDENTE.  
   
 2- Geração manual do período

Quando o status do movimento gerado é diferente de PENDENTE, o usuário deve criar um período de estorno manualmente e realizar a medição para estorno das tarefas.

Ao abrir o processo de Medição de Contrato para períodos de estorno (não liberados) a grid será automaticamente preenchida com os valores da liberação do período a estornar.  
   
 Para incluir um período de estorno, basta dar duplo clique no período já liberado na tela de edição do mesmo e será exibido do lado direito os campos de criação dos períodos de estorno.  
   
 A inserção e exclusão segue o mesmo padrão dos período complementares.  
   
 O período de estorno é referente a apenas um período e seus complementares do contrato, sendo sua validação feita nos itens medidos e liberados do período.  
   
 Os períodos gerados são visualizadas suas informações no anexo de períodos de contratos.

**Importante:** Existe uma coluna, chamada "Vl. Medido - Previsto" do anexo "Períodos do Contrato" que tem seu calculo da seguinte forma: Valor Medido - Valor Previsto - Valor Retido.  
 O valor medido é caracterizado pelo gasto naquele período. O valor previsto é, como seu próprio nome diz, a previsão em seu planejamento.  
   
 **Importante:** Existem agora períodos de Reajuste, que são gerados após aplicar um reajuste por item em um período já liberado. Esse período é gerado com código 0001R001. Saiba mais de reajuste por item do contrato: [Reajuste por item](http://tdn.totvs.com/display/LRM/Reajuste+do+Item+Associado+-+Contrato)
