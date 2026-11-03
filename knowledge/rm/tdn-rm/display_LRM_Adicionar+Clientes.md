---
content_hash: 6203e116cf5699520c427a29b33fcd24a1e4a249c327c3b4af46bdd7ac93cada
fetched_at: '2026-06-29T00:09:37.381535+00:00'
page_id: '425459599'
product: rm
source: tdn-rm
title: Adicionar Clientes
type: documentation
url: https://tdn.totvs.com/display/LRM/Adicionar+Clientes
version: 1
---

**Adicionar Clientes**   
Uma empresa precisa de marketing para crescer. A Campanha de Relacionamento com os Clientes é um esforço para captar novos clientes ou fidelizar clientes já conquistados. Através dela, o produto/serviço ou marca são divulgados  e o nível de interesse dos clientes são medidos. Para garantir eficiência no empenho investido nas campanhas, os clientes devem ser selecionados de acordo com as perspectivas da organização.   
Selecionar os clientes é o mesmo que segmentar o mercado como um todo em pequenos grupos que atendem aos critérios esperados pela empresa. Os critérios podem ser variados, como por exemplo, demográficos, sociais, econômicos, de acordo com a personalidade/estilo ou até mesmo pela junção de várias características.   
O recurso "Adicionar Clientes" disponibiliza uma lista de todos os clientes (independente do tipo: P = Pessoa, C = Cliente , T = Prospect, A = Aluno ou R = Professor) de todas as coligadas para efetuar a seleção daqueles que irão participar da campanha. Essa seleção pode ser realizada através de:  
Filtros Padrões:  Filtros com campos pré-determinados para utilização.  
Grupo de Cliente: Retorna os clientes do grupo específico criado no Marketing.  
Setença SQL pré-cadastrada: Retorna os clientes que atendem aos critérios estipulados na consulta SQL que está cadastrada na Visão de Dados.  
Setença SQL digitada manualmente: Retorna os clientes que atendem aos requisitos indicados na consulta SQL digitada na caixa de texto da tela de visão. A caixa encontra-se oculta a priori até ser acionada através do botão Setença SQL Personalizada.  
Na utilização de Setenças SQL pré-cadastradas ou digitadas momentaneamente na seleção dos clientes, é necessário que o resultado obrigatoriamente possua as colunas COLIGADA, CODIGO, TIPO, NOME.   
A cada execução do serviço processo será salvo um registro no Histórico de inserção de clientes contendo a data da inserção do cliente, o usuário que executou, a setença SQL e o filtro (ou somente filtro caso não sido executada uma consulta SQL) juntamente com os dados dos cliente adicionados.   
**Observação**  
Os clientes não podem ser editados diretamente da campanha. Mas podem ser excluídos caso não atendam aos critérios de seleção da empresa.
