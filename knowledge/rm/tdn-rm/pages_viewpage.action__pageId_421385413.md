---
content_hash: e9fc7cc19ec8fa4200a4154e717c2bf071e0acb031f13a94555792e553ec5821
fetched_at: '2026-06-29T00:09:15.570620+00:00'
page_id: '421385413'
product: rm
source: tdn-rm
title: Lançar Cronograma Automaticamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385413
version: 3
---

---

Lança o cronograma previsto, realizado ou medido através das seguintes informações: data início e fim do período, se trabalha aos sábados e se considera feriados.

Calcular Dias:

Ao clicar no ícone "Calcular dias" exibe o número de dias corridos, dias úteis (considerando o sábado, caso ele seja útil), sábados, domingos e feriados (considera o calendário selecionado) do período.

**Atenção:**

A opção de cálculo existe somente para informar ao usuário, estatística do período: Dias Corrido, Dias Úteis, Sábados, Domingos e Feriados.

Não é necessário realizar o cálculo para que o processo ocorra.

Os campos digitáveis (Data de Início, Data de Fim e Cronograma) são necessários.

Se o parâmetro de projeto "Utiliza PERT" estiver marcado, a opção "Considerar Datas do PERT" também estará marcada, não permitindo a edição das datas ou períodos, significando que o processo deverá considerar as datas do PERT, porém desmarcando a opção, o comportamento do processo desconsiderará as datas do PERT.

Cálculo do Percentual a ser Lançado:

Dado o intervalo de datas, calcular para cada período: número de dias úteis do período número de dias úteis no intervalo informado. Percentual Será Dado por C= (A/B)\*100

Os campos Período Inicial e Final servem como auxílio para a definição das datas.

**Atenção:**

Para o primeiro período considerar para efeito de cálculo a data inicial informada.

Para o ultimo período considerar para efeito de cálculo a data final informada.

Atentar ao parâmetro Trabalha sábado, trabalha domingo e trabalha feriado.

Verificar se no calendário utilizado existe feriados cadastrados.

Se houver algum preenchimento o processo de Lançamento automático irá excluir os dados existentes.

Não é possível executar o processo sem antes definir os períodos do cronograma.

Caso a data de Fim seja maior que o último período o lançamento percentual ficará acumulado desproporcionalmente no último período.

Caso exista ao menos um período com informações lançadas no calendário da tarefa, o processo deverá adotar a forma de lançamento a partir dessas informações, caso contrário, deverá seguir o comportamento padrão citado anteriormente.

Se o parâmetro de projeto "Utiliza PERT" estiver marcado, as seguintes regras deverão ser seguidas:

A opção "Considerar Datas do PERT" também estará marcada, não permitindo a edição das datas ou períodos, significando que o processo deverá considerar as datas do PERT, porém desmarcando a opção, o comportamento do processo desconsiderará as datas do PERT.

Se várias tarefas tiverem sido selecionadas, o botão "Calcular dias" deverá estar desabilitado e se apenas uma tarefa tiver sido selecionada, o intervalo de datas será o intervalo das datas planejadas do PERT, permitindo o cálculo dos dias.

O lançamento poderá ser feito nos três cronogramas (Previsto, Medido e Realizado), baseado nas datas planejadas da tarefa no PERT.

Se a opção de "Alterar Quantidade pelo Cronograma" da tarefa estiver marcada, os percentuais não serão lançados para a respectiva tarefa e no log do processo será apresentada a mensagem: "A tarefa 001.01.01 - Escavação de tubulões realiza somente lançamentos por quantidade no cronograma previsto, não permitindo lançamentos percentuais".

Consistências Realizadas para Execução do Processo:

As datas devem ser informadas. Pelo menos um cronograma deve ser informado. A data de início deve ser menor que a data fim.

 Informações Complementares

---

 Como Fazer

---

 Recursos Adicionais

---

Veja Também
