---
content_hash: 65f974212a09cf729316a6a766aefbd254b82b9efc453935b6d6503a86eb0010
fetched_at: '2026-06-29T00:09:14.354646+00:00'
page_id: '421385213'
product: rm
source: tdn-rm
title: Projeto (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385213
version: 9
---

**Fórmula de Consistência**

Para que seja realizado uma consistência do Projeto, é necessário cadastrar uma fórmula e parametrizá-la no campo Fórmula de Consistência. Esta fórmula informada será utilizada na Consistência de Projeto.

**Fórmula para Consistir a Análise do Valor Agregado**

Para realizar um tipo de consistência diferente dos resultados padrões obtidos nos cálculos dos índices,  é necessário cadastrar uma fórmula e parametrizá-la em:

- Fórmula de Consistência p/ COTA

- Fórmula de Consistência p/ COTR

- Fórmula de Consistência p/ CRTR

Caso o usuário não defina nenhuma Fórmula, o resultado apresentado será como descrito nos itens de cada Índice.

**Exemplo:**

Para o COTA, caso não exista uma fórmula parametrizada, ele trará o Valor do Cronograma Previsto.

**Utilizar Linha Base como Valor Planejado (COTA):**

Ao marcar esse parâmetro, muda-se o conceito para obtenção dos valores de COTA.

Com o parâmetro DESMARCADO, ou seja, com o funcionamento atual, ao efetuar copia de linha base, os valores de COTA são obtidos da seguinte forma:  
   
COTA VP = Valor do Cronograma Planejado  
COTR VA = Valor do Cronograma Realizado  
CRTR|CR = Valor do Cronograma Medido  
   
Com o parâmetro MARCADO, ou seja, Utilizando a Linha Base, passa-se a obter os valores de COTA da seguinte forma:  
   
COTA VP = Valor da Linha Base  
COTR VA = Valor agregado, considerando custo unitário da linha base.  
                 Formula: COTR (VA) = Quantidade Realizada (Cronograma Realizado) \* ( Valor da Linha Base / Quantidade da Linha Base). Para cada período e tarefa.  
CRTR|CR = Valor Apropriado.

**Incluir tabelas de curvas na revisão simples**

Este parâmetro irá copiar para o relatório revisado os dados das Curvas ABC e S, permitindo a geração de relatórios.

Para acessar a documentação onde existe um exemplo da criação de uma fórmula para o cálculo de Analise de Valor Agregado [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=421385390).

---
