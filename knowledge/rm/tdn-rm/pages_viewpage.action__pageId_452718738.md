---
content_hash: 8ddb70256bcc9c4738738a9e2723316473f640a0ea09211226db9f008725b307
fetched_at: '2026-06-29T00:10:01.452571+00:00'
page_id: '452718738'
product: rm
source: tdn-rm
title: Fechar Avaliação de Desempenho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718738
version: 82
---

**Fechar Avaliação de Desempenho**

Essa opção irá finalizar a avaliação. Após esse procedimento não será mais possível nenhuma alteração.

Ao selecionar essa opção o campo "Data de Fechamento" será preenchido automaticamente. No fechamento da avaliação de desempenho, será exibida uma janela apresentando as sugestões (coluna "Nova Graduação") de alteração na graduação das competências dos participantes avaliados.

Todas as competências que o funcionário não possuía e forem adquiridas pela avaliação podem ser identificadas pelo valor exibido na coluna "Graduação atual" que apresentará o valor Não possui e nos demais casos, apresentará o valor atual não atualizado com a avaliação de desempenho.

Ainda nesta janela é possível visualizar uma coluna "Alteração" que exibe:

* uma imagem de uma seta para cima de cor verde que indica que a competência teve sua graduação elevada;
* uma seta pra baixo de cor vermelha que indica que a competência teve sua graduação reduzida;
* um sinal de + (mais) azul, indicando que a competência foi adquirida pelo funcionário na avaliação de desempenho.

Quando não houver alteração na graduação da competência do funcionário, nenhuma imagem será mostrada.

O usuário deverá selecionar apenas o check box referente à linha que contém a competência que opte por atualizar. Todas as linhas marcadas serão atualizadas pelo sistema.

As competências que tiverem as graduações atualizadas (não tiverem sido acrescentadas pela avaliação) vão gerar um histórico de alteração no cadastro do funcionário.

Veja em Cadastros| Pessoas, pasta identificação, Anexos| Histórico das Competências.

**Regra para atualização das competências:**

**1) Será comparada a nota obtida no item avaliado na avaliação com o ponto de corte definido para a mesma onde poderão ser gerados os seguintes resultados:**

- **Nota obtida corresponde ao ponto de corte:**

Se o funcionário possuir a competência, a graduação será alterada para a graduação da definição do Mapa de Conhecimento;  
Se o funcionário não possuir a competência, será concedida a competência na graduação da definição do Mapa de Conhecimento.

- **Nota obtida está acima do ponto de corte:**

Se o funcionário possuir a competência numa graduação abaixo da graduação exigida / desejada, a graduação do funcionário será elevada para o nível da graduação da definição do Mapa de Conhecimento;   
Se o funcionário possuir a competência na mesma graduação exigida / desejada, a graduação do funcionário será elevada em um nível;   
Se o funcionário possuir a competência numa graduação acima da graduação exigida / desejada, nada será feito;  
Se o funcionário não possuir a competência, será concedida a competência na graduação da definição do Mapa de Conhecimento.

   
- **Nota obtida está abaixo do ponto de corte:**

Se o funcionário possuir a competência numa graduação abaixo da graduação exigida / desejada, nada será feito;   
Se o funcionário possuir a competência na mesma graduação ou acima da exigida / desejada, a graduação do funcionário é reduzida um nível da graduação abaixo da graduação atual do funcionário;  
Se o funcionário não possuir a competência, será concedida a competência na graduação mínima. 

**Observação:**

Se o parâmetro "Atualizar competências de acordo com a graduação definida na escala" estiver marcado, as regras acima mudam e são consideradas as graduações definidas diretamente na escala.

**Observação**

- Na montagem da avaliação de desempenho, no momento da configuração, definimos o PONTO DE CORTE, editando as escalas existentes pela opção "Alterar Escala (Notas)". O padrão do ponto de corte é a escala ATENDE.

- Pela opção "Ver detalhes", na tela de fechamento da avaliação, é possível visualizar com mais precisão o cenário no qual a avaliação foi realizada, o resultado da avaliação desta competência e a ação proposta a ser realizada para o fechamento da avaliação.

- Caso o funcionário não possua uma competência exigida /desejada, em que ele tenha sido avaliado na avaliação de desempenho, será considerado que o mesmo a possui na menor graduação existente. - Atualmente no sistema o cargo não possui competências, então estão sendo consideradas como competências do cargo todas as competências mapeadas para as funções nele contidas.
