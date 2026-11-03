---
content_hash: d618f820dd76ec3838511b4bb47c53efa321a3457b151dbb4ed50b50257d8a04
fetched_at: '2026-06-29T00:09:15.592703+00:00'
page_id: '421385421'
product: rm
source: tdn-rm
title: Item de Pedido de Material
type: documentation
url: https://tdn.totvs.com/display/LRM/Item+de+Pedido+de+Material
version: 6
---

---

Para visualizar o item de pedido de material acesse: Totvs Construção, Obras e Projetos/Planejamento/Geração de Pedidos.  
Na aba anexos acesse a opção: Item de Pedido  

Será possível visualizar informações como:

**Código da Tarefa:** Código da tarefa que foi associada ao pedido.

**Descrição da Tarefa:** Descrição da tarefa associada ao pedido.

**Código do Insumo:** Código do insumo associado a tarefa do pedido.

**Descrição do Insumo:** Descrição do insumo associado a tarefa do pedido.

**Código do Produto:** Código do produto no pedido.

**Descrição do Produto:** Descrição do produto no pedido.

**Preço Unitário:** Preço unitário utilizado no pedido.

**Quantidade Pedida:** Quantidade pedida no pedido.

**Quantidade da Necessidade:** Quantidade da necessidade do pedido.

**Quantidade Estorno:** Quantidade estornada do pedido.

**Data da Necessidade:** Data da necessidade do pedido.

**Data de Entrega:** Data da entrega do pedido.

**Data do Pedido:** Data do pedido.

**Contrato:** Número do contrato vinculado ao item do pedido.

**Observação:** Observação referente ao pedido.

**Prazo de Ressuprimento:** Prazo de ressuprimento do pedido.

Na edição do item do pedido, é possível visualizar se o item possui algum vínculo, com Contrato ou :

 

Um pedido poderá ter itens com diferentes vínculos, dependendo da parametrização do projeto, e gerando diferentes tipos de movimentos.

No caso de um projeto que utiliza Acordo Corporativo, é possível definir nos parâmetros qual a [prioridade de utilização ou a ordem para seleção do acordo](https://tdn.totvs.com/pages/viewpage.action?pageId=421385497), assim como um [tipo de movimento específico para pedidos](https://tdn.totvs.com/display/LRM/Tipos+de+Mov.+de+Pedidos) que possuem item de acordo.

Apesar da inclusão do item sugerir o Acordo conforme definição dos parâmetros, o usuário poderá alterá-lo caso houver necessidade.

Os movimentos poderão ser gerados separadamente, dependendo do acordo, assim como da data de entrega.

 

Qualquer alteração deverá ser feita através de processos referente aos itens ou na edição dos mesmos, na tela de Itens de Pedido de Material, não será permitido.  
A geração de movimento adota o comportamento de agrupar os itens de movimento por produto. Se existir o mesmo produto rateado em duas tarefas diferentes será gerado apenas um item de movimento referente ao produto, é enviado nulo na tarefa do item e as tarefas são rateadas no centro de custo do item do movimento.

 

**Exemplo:**  
Tarefas no Totvs Obras e Projetos:  
• Tarefa 1(grupo orçamentário A): Valor R$ 100,00 • Rateio de produto:       - 100% Cimento • Rateio de centro de custo:             - 30% Centro de Custo 1             - 40% Centro de Custo 2             - 30% Centro de Custo 3  
   
• Tarefa 2(grupo orçamentário B): Valor R$ 20,00 • Rateio de produto:       - 100% Cimento • Rateio de centro de custo:             - 100% Centro de Custo 1              Movimentos no Núcleus:       
     Item X - Cimento Valor R$120,00 Rateio de Centro de Custo do item de movimento  
Tarefa 1 - Grupo A - Centro de Custo 1 – R$ 30,00 = 25,00% Tarefa 1 - Grupo A - Centro de Custo 2 – R$ 40,00 = 33,33% Tarefa 1 - Grupo A - Centro de Custo 3 – R$ 30,00 = 25,00% Tarefa 2 - Grupo B - Centro de Custo 1 – R$ 20,00 = 16,67%  
 

Para insumos contratados (Insumos de contratação)  
Quando o pedido de material possuir itens (insumos que possuem detalhamento), insumos contratados não será possível a alteração de alguns itens do item do pedido de material, sendo eles a tarefa, insumo, produto e contrato. Permitindo alteração apenas dos campos de controle do próprio pedido. (Quantidade e data de entrega).
