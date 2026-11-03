---
content_hash: 972c18a25897c7d836ff0aca8253305cee2c61b60d8c4400419583b869c737fd
fetched_at: '2026-06-29T00:10:09.417244+00:00'
page_id: '452719663'
product: rm
source: tdn-rm
title: Processo Gerar Ambiente de Trabalho
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Gerar+Ambiente+de+Trabalho
version: 3
---

**Processo Gerar Ambiente de Trabalho**    
Para realizar a carga inicial dos registros já existentes no sistema poderá utilizar o processo "Gerar Ambiente de Trabalho".

Nesse processo o sistema irá fazer a leitura de todos os registros existentes nos cadastros de origem (Posto, Local, Lotações e Avaliações de Risco para seções) e gerar um registro de ambiente de trabalho para cada.

Serão apresentados 3 parâmetros: Posto de Trabalho, Local de Trabalho e Lotações na tela.

Ao marcar os parâmetros o sistema realizará a leitura apenas do cadastro de Reconhecimento e Avaliação de Risco para geração dos ambientes de trabalho. Ou seja, criará ambientes de trabalho apenas para Posto, Local ou Lotações considerando a avaliação de risco vigente.

São considerados registros do tipo "Avaliação" que possuam vigência ativa dentro do período de competência da Folha de Pagamento.  
Para os ambientes do tipo "Seção" independente de parametrização, o sistema sempre buscará as Avaliações de Risco vigentes do tipo "Seção".

Ex.: Cliente tem 30 registros de Posto de Trabalho, 20 de Locais de Trabalho e 150 registros de Lotações, porém existe avaliação de risco vigente apenas para 2 Postos, 1 Local e 2 Lotações.  
Com isso ao marcar estes parâmetros, serão gerados apenas 5 registros de Ambientes de Trabalho.  
Sem marcar os parâmetros serão gerados 200 registros de Ambientes de Trabalho.

Ex.2: Cliente tem 30 registros de Posto de Trabalho, 20 de Locais de Trabalho e 150 registros de Lotações, porém existe avaliação de risco vigente apenas para 2 Postos, 1 Local e 2 Lotações.  
Foi marcado o parâmetro Posto de Trabalho e os outros dois (Local de Trabalho e Lotação) permaneceram desmarcados.  
Com isso, foi gerado 2 Postos de Trabalho, 20 Locais de Trabalho e 150 registros de Lotações, totalizando 172 registros.

**Observação**

Esse processo irá gerar um cadastro de Ambiente de Trabalho Global para situações de clientes que tenham avaliações de risco para Funções, Pessoas e Tarefas que estejam vigentes na competência atual do Labore.

**Atenção**

O menu e todas as pendências do Ambiente de Trabalho só serão visualizados quando o ambiente no parametrizador do eSocial (RM | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais 1/4) for diferente de 1.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

HelpWiki GDP RH - Folha de Pagamento
