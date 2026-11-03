---
content_hash: a61f904d0267a1b1ee890543f0899cbd3768901d5aa48e2cd46e704d0e9e9bad
fetched_at: '2026-06-29T00:09:25.178533+00:00'
page_id: '423938047'
product: rm
source: tdn-rm
title: Cadastro do Item da Ordem
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+do+Item+da+Ordem
version: 2
---

O cadastro do Item da Ordem de Produção permite adicionar as estruturas que serão produzidas, ou seja, os produtos que irão compor a ordem de produção.   
Selecione a Estrutura e os demais campos serão preenchidos automaticamente. Informe uma data e hora prevista para o início da produção e a quantidade desejada a produzir.   
Ao realizar o cálculo, os campos data e hora final prevista e custo total da produção serão preenchidos.   
O custo total é composto pelo custo da atividade  o custo indireto  o percentual do debita custo do subproduto gerado (caso esteja marcado). No cálculo da ordem, o campo prioridade é apenas informativo.   
***Observações***: O campo prioridade será consistido apenas no momento da alocação da grade de programação através do menu Produção | Realocar Grade da Programação, onde será verificada a prioridade da execução do item de ordem, realocando toda a grade da programação.   
Quando não utilizado na funcionalidade de realocação, o campo é apenas informativo, proporcionando a confecção de relatórios para acompanhamentos dos itens de ordens.

**Intervenção de Equipamento**

Caso o parâmetro "Intervenção Manual nos Equipamentos" esteja marcado, ao efetuar o cálculo será exibida a tela para intervenção nos equipamentos.   
A escolha do equipamento que será utilizado na produção poderá ser "CALCULADO PELO MRPII", ou seja, o cálculo irá escolher o equipamento para produção.   
O equipamento principal cadastrado para estrutura ou qualquer um dos seus substitutos, se houver.  
***Observações***: O equipamento principal terá sempre eficiência igual a 100%, o que significa que se o principal produz 100 peças em 1 hora, se for cadastrada uma eficiência de 30% para o alternativo, será equivalente que este produzirá 30 peças em 1 hora.   
O custo também influencia na escolha, pois se o custo do alternativo estiver fora dos 12 meses anteriores, o custo dele será zero.   
Então, mesmo com eficiência menor, ele sempre será escolhido porque o custo é igual a zero.   
Se não quiser fazer a intervenção manual de equipamentos, clique no botão confirmar e o sistema irá alocar o equipamento escolhido pelo cálculo do MRPII, de acordo com as regras citadas acima.   
Caso clique no botão cancelar o sistema irá cancelar todo processo de cálculo.

**Pasta Subproduto**

Nesta pasta é possível efetuar o cálculo da quantidade de subproduto a ser gerado. Informe o subproduto e sua quantidade a ser gerada. Informe qual estrutura possui a atividade geradora do subproduto e o sistema calculará a quantidade necessária do produto acabado que deverá ser produzido para obter a quantidade de subproduto solicitado.  
 *Observações**:*** A quantidade de subproduto a ser produzido deverá ser múltipla da quantidade do subproduto gerado na estrutura.  
 **Exemplo:** Se a estrutura possuir uma atividade que gera subproduto com uma quantidade 1,5 ml, então a quantidade de subproduto a ser produzido deverá ser múltipla de 1,5 (Exemplo: 9 ml).

**Pasta Etapas da Produção**

Nesta pasta, após o cálculo é possível visualizar todas as informações do roteiro produtivo.

**Composição do Custo**

Nesta pasta, após o cálculo será apresentado toda a composição do custo do item de ordem de produção, permitindo visualizar o custo por entidades e custo total do processo produtivo. Os valores da coluna 'Custo Previsto' se referem aos custos que compõe o custo total do item de ordem, enquanto na coluna 'Custo (Informativo)' são apresentados os custos que não afetam a composição do custo do item de ordem.

**Necessidade de Materiais**

Nesta pasta serão apresentadas as informações referentes à programação dos materiais necessários para a fabricação do produto.  
 ***Observações*:** Caso a quantidade da matéria prima no estoque seja inferior à quantidade necessária, o sistema irá destacar a linha do componente em cor vermelha.

**Roteiro Padrão**

Após o cálculo será apresentado nesta pasta o roteiro de todas as atividades.

**Equipamentos**

Após o cálculo será apresentado nesta pasta os equipamentos alocados para as atividades com data e hora de início e fim.

**Mão de Obra**

Nesta pasta, após o cálculo, serão apresentadas todas as mãos de obra alocadas para as atividades com data e hora de início e fim.   
A alocação da mão de obra baseia-se no número de pessoas necessárias para a realização da atividade, nas habilidades e nas funções registradas no cadastro de atividades.   
Para alocar mãos de obra também é verificado, pelo sistema, o número de pessoas disponíveis e os intervalos de alocações existentes na base de dados.   
Quando houver número de pessoas disponíveis que seja maior que o número de pessoas necessárias, a alocação iniciará com a que tem o menor custo.   
Caso possuam o mesmo custo, será alocada a mão de obra que possuir maior período de ociosidade (parte do tempo em que a mão de obra não está alocada para uma determinada atividade).   
Quando não houver a possibilidade de alocação de mão de obra necessária para a execução da atividade, o sistema registrará a informação no log de cálculo do MRPII.  
Postos Nesta pasta, após o cálculo serão apresentados todos os postos de trabalho para cada atividade.

**Log de Cálculo**

Após o cálculo, nesta pasta serão apresentadas todas as restrições para a produção.  
 **Exemplo:** Mão de Obra não habilitada para execução de uma atividade.  
 **Dica:** Em relação a Mãos de Obra, observe as seguintes situações:

Para solucionar pendências de falta de mão de obra em atividades no log, revise o cadastro das mesmas (menu Cadastros | Atividades – pasta Recursos, atentar para grupos de mão de obra – quantidade necessária, habilidades e/ou funções);  
Somente serão consideradas para alocações as mãos de obra que estiverem em situação "ativa" no TOTVS Planejamento e Controle da Produção (menu Cadastros | Mão de Obra);   
Com integração ao TOTVS Folha de Pagamento, o sistema fará consistência da situação do funcionário (ativo, férias, licença, etc) e/ou sua função, caso informe funções para a execução da atividade (menu Cadastros | Atividades, pasta Recursos | Funções);  
Com integração ao TOTVS Automação de Ponto, o sistema obedecerá ao horário de trabalho determinado para o funcionário e verificará sua compatibilidade com o horário do posto de trabalho, onde a atividade é executada (menu Cadastros | Calendários de Produção).
