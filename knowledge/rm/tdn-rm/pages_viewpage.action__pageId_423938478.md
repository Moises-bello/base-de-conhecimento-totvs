---
content_hash: b5237d7ec1ead4a772ed73ad6041be5fe687c4914b9d8cdb713e4be9badf6885
fetched_at: '2026-06-29T00:09:27.282333+00:00'
page_id: '423938478'
product: rm
source: tdn-rm
title: Índice de Acompanhamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938478
version: 6
---

Através do cadastro de Índice de Acompanhamento o usuário pode cadastrar os valores do índice que será utilizado para aferir a qualidade de um objeto de manutenção através de medição periódica.   
São estabelecidos, no momento da criação do índice, valores mínimo e máximo aceitáveis de qualidade.   
Baseado neste intervalo, o sistema classifica o objeto da seguinte maneira: valor do índice abaixo do mínimo, valor do índice dentro da faixa, valor do índice acima do máximo.  
***Atenção!***Os valores mínimos e máximos escolhidos para os índices de acompanhamento podem variar dentro do conjunto dos números racionais (-4,124; -3; 0; 9; 17,865).  
Ao cadastrar um índice de Acompanhamento e o Objeto de Manutenção for do tipo Pneu irá aparecer o flag "Decrescente", marcando o flag, só será possível lançar índice de Acompanhamento para o Objeto de Manutenção com valores decrescente.  
***Observação***: O parâmetro 'modelo' conterá informações caso seja informado um tipo de objeto de manutenção.   
Sendo assim serão visualizados somente modelos de tipos de objetos escolhidos, não permitindo escolher um modelo sem antes informar o tipo de objeto.  
O parâmetro 'sub-modelo' conterá informações caso seja informado um modelo relacionado, visualizando somente sub-modelos do modelo informado.

Exemplos de cadastramento de índices de acompanhamento

| Objeto de Manutenção | Motor |
| --- | --- |

Campos  Conteúdo dos campos  
 Nome: Folga no cabeçote do motor  
 Unidade de Medição: mm  
 Valor Mínimo:  0  
 Valor Máximo:  5

| Objeto de Manutenção | Ar Condicionado |
| --- | --- |

Campos  Conteúdo dos campos  
 Nome: Temperatura de resfriamento atingida  
 Unidade de Medição: ºC (graus Celsius)  
 Valor Mínimo: 10  
 Valor Máximo: 30

***Observação***: Os campos Tipo de objeto, Modelo e Sub-modelo ficaram desabilitados para edição no cadastro de índice de acompanhamento quando:

1. Existir histórico do índice no objeto de manutenção.
2. Existir apropriação direta para o índice.
3. Existir índice definido para o Produto do Objeto de Manutenção.
4. Existir índice definido para o Produto do Tipo de Objeto de Manutenção.

---
