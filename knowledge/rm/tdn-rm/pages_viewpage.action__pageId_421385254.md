---
content_hash: b153c0af5a9daa31dc3fdd5ccdbbfe54bfeb0f77f4d5465fa2be518f85881db6
fetched_at: '2026-06-29T00:09:14.783776+00:00'
page_id: '421385254'
product: rm
source: tdn-rm
title: Especializar Insumo 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385254
version: 1
---

**Especializar Insumo** ----   
A especialização de insumos possibilita criar um novo insumo contendo as mesmas características de um insumo original para utilização no projeto.  
Para utilizar este processo e verificar onde os insumos utilizados podem causar impactos foram criados alguns anexos:  
Impactos em pedidos, Impactos em contratos, Impactos em atividades, Impactos em serviços, Impactos em atividades que possuam pedidos ainda não enviados para Suprimentos/Faturamento.   
O usuário deve analisar os impactos que o insumo origem podem sofrer, e decidir se o processo é viável ou não. Sendo viável o insumo é selecionado e em Processos -> Especialização de Insumos o processo é requisitado e a tela para inserção dos dados é aberta. A tela inicial do processo exibe informações referentes à execução do mesmo e o usuário pode opcionalmente preencher a descrição do processo.  
Na próxima etapa o usuário deve definir uma descrição para o insumo a ser especializado, a descrição pode ser inserida manualmente ou pode copiar a descrição do insumo origem.  
Como a especialização de insumos pode ser realizada para insumos de qualquer grupo DNIT, temos uma particularidade para insumos que pertencem ao grupo DNIT materiais, para estes a especialização só pode ocorrer caso o mesmo possua um produto associado, para outros grupos DNIT não existe esta validação. Portanto no processo com insumos do Grupo DNIT material é apresentada uma nova tela onde a associação de produtos do insumo origem para o insumo especializado deve ser realizada, sendo obrigatória a definição de um produto principal para o insumo especializado, somente assim o processo pode ser avançado.  
Com a inclusão da especialização sem nenhum produto associado, a validação acima só entrará em vigor para os insumos a serem especializados que não possuam produtos associados, ou que o projeto não esteja no status "A Executar";  
O processo de especialização de insumos sem produtos associados só pode ser executada se o projeto estiver com o status "A Executar", o insumo for grupo DNIT Material e a flag "SEMPRODASSOCIADO" estiver marcada como "S"(Flag encontrada apenas na grade de insumos da tela de cadastros, não existe o campo no banco de dados).  
   
Observação:   
Não é possível associar o produto principal do insumo origem ao insumo especializado. Um alerta é exibido na tela, indicando o produto que não pode ser associado. Caso o usuário deseje associar o produto principal, o mesmo deve acessar o cadastro do respectivo insumo e tornar esse produto não-principal.  
Caso o insumo origem esteja vinculado a alguma requisição de material ainda não enviada para Suprimentos/Faturamento, surgirá uma tela com os materiais requisitados e uma opção de cancelamento da requisição, o processo só prossegue quando a requisição é cancelada.  
Observação:  
Uma vez canceladas as requisições, as mesmas permanecem na base apenas para consulta, não permitindo edição. E se o Log para Requisição de Materiais estiver definido, a ação de cancelamento é gravada no Log de Usuários do sistema.  
Realizadas todas as etapas o insumo especializado é criado, o mesmo possui a seguinte característica: Código (Insumo Origem), com o sufixo '.####' (4 caracteres numéricos).  
Observações:  
Os insumos especializados são enviados no backup do projeto.  
Na cópia de itens caso o subprojeto, tarefa ou composição possuam o insumo especializado o processo de cópia é abortado emitindo uma mensagem de aviso antes mesmo do processo ser iniciado.  
Na cópia de insumos o insumo especializado não é listado entre os insumos do projeto, pois insumos especializados não podem ser copiados.  
A alteração do grupo de custo do insumo especializado é bloqueada, já a alteração do grupo de custo do insumo origem é liberada, porém se alterado o grupo de custo do insumo origem, esta alteração será propagada, alterando também o grupo de custo do insumo especializado.  
Atenção:  
O processo só pode ser executado com insumos locais.  
O processo não pode ser executado para insumos já especializados.  
O processo não pode ser executado se o insumo origem estiver vinculado a algum contrato.  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Impacto em Pedidos Impactos em Contratos  
Impactos em Atividades Impactos em Serviços Impactos em atividades que possuam pedidos ainda não enviados para Suprimentos/Faturamento
