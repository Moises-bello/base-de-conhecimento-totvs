---
content_hash: c2fe37580b8c7fc04485c67a7c00c0da078985df85f58c2b736946347e10383c
fetched_at: '2026-06-29T00:10:08.929061+00:00'
page_id: '452719608'
product: rm
source: tdn-rm
title: Envelope de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Envelope+de+Pagamento
version: 8
---

No envelope de pagamento serão visualizados os dados referentes ao pagamento do funcionário, após ter sido feita a sua entrada de dados e recálculo do movimento. Para impressão, deve-se usar o Gerador de Relatórios.  
   
Os dados exibidos aqui são inicialmente referentes ao salário base, mês, ano e período da competência atual, mas a visualização dos dados referentes a outros períodos pode ser facilmente acessada através da troca do valor de um destes campos de mês, ano e período.  
   
**Atenção:**  
Para Inserir, Excluir, Editar ou Recalcular eventos no envelope dos funcionários, o Usuário Supervisor (Usuário mestre) deverá dar permissão para utilizar os botões do envelope no cadastro de perfis.  
   
Os eventos são mostrados conforme a seguinte legenda:  
Em Azul  Proventos  
Em vermelho  Descontos  
Em Verde  Base de Cálculo  
   
Além das operações de inclusão, edição e exclusão de eventos no envelope de pagamento, é possível realizar o recálculo da movimentação do funcionário, sendo que este é executado (se necessário) cada vez que se troca de um funcionário para outro, quando se ativa a janela e quando se sai da janela. Para inibir esta função, clique no botão **"Não recalcular"** neste momento o envelope tem a descrição de "Valores Forçados". Casos particulares (como funcionários com dados alterados manualmente, admitidos no próximo mês) são tratados separadamente.  
   
**Observações:**

1. O recálculo da movimentação de eventos para funcionários demitidos em meses anteriores estará desativado. Se houver necessidade de recalcular eventos para estes funcionários, deve-se fazer através do processo de cálculo de Rescisão Complementar.
2. Os eventos que forem incluídos/alterados/excluídos no envelope de pagamento de rescisão complementar não serão recalculados. Apenas as bases poderão ser recalculadas pelo botão Recalcular Base.
3. As inclusões/alterações/exclusões somente serão liberadas para funcionários que tem Data de último movimento maior ou igual a competência atual, ou seja, desde que tenha calculado a rescisão complementar alterando a Data do último Movimento.
4. Caso o evento seja incluído no envelope não será excluído no recálculo pelo processo de rescisão complementar, apenas será recalculado caso não esteja marcado o parâmetro valor forçado. A mesma informação serve para o evento excluído que não será incluído automaticamente.
5. Caso o envelope de pagamento da rescisão complementar seja cancelado e existam eventos com o parâmetro 'Forçar valor' marcado, estes somente serão cancelados se o parâmetro 'Cancela eventos alterados manualmente' estiver marcado no processo do cancelamento.
6. O envelope somente será recalculado ou cancelado pelos respectivos processos se o parâmetro 'Forçar Valores do Envelope' não estiver marcado.
7. Utilizando o parâmetro "Utiliza Cálculo por Centro de Custo" e o  "Não Recalcular" desmarcado no envelope, no momento de Incluir/Excluir/Alterar um evento no envelope de pagamento do funcionário , a ficha financeira, o centro de custo e o envelope de pagamento estarão dessincronizados aparecendo no envelope valores forçados e na ficha financeira o aviso de não sincronizado.
8. Caso o envelope do funcionário nunca tiver sido recalculado, o recalculo será efetuado obrigatoriamente na primeira vez.
9. O parâmetro "Lança Grupo de eventos sem recalcular o envelope" não afetará o funcionamento dessa tela.

Importante

**Recálculo automático**

Quando as tabelas de cálculo das finalidades de INSS e IRRF são alteradas, e a competência atual da folha de pagamento está dentro da vigência dessas tabelas, os envelopes de pagamento calculados anteriormente passam a ficar pendentes de recálculo.

Quando o Cadastro de Eventos é alterado, os envelopes de pagamento calculados anteriormente passam a ficar pendentes de recálculo.

Quando o parâmetro “Lança Grupo de Eventos sem recalcular envelope” em Configurações | Parametrizador | Folha Normal | Geral 1/2  estiver marcado, os envelopes de pagamento afetados pelo lançamento do grupo de eventos passam a ficar pendentes de recálculo.

Ao acessar o envelope de pagamento e for detectado que há recálculo pendente — devido a alguma das alterações listadas acima — o envelope será recalculado automaticamente.

Durante esse processo, o sistema exibirá o progresso do recálculo e o log de depuração para conferência. O usuário pode interagir com o processo em tempo real, inclusive tendo a opção de cancelá-lo.

Nas versões anteriores à 12.1.2406, o recálculo também era executado automaticamente, porém sem permitir interação com o usuário.

Informações Técnicas

Se a data e hora na tabela PPARAM for maior que a data e hora na tabela PFUNC o envelope fica pendente de recálculo.

Tabela: PPARAM.

Campos: ULTMODCALCULODATA e ULTMODCALCULOHORA

e

Tabela: PFUNC.

Campos: ULTIMORECALCULODATA e ULTIMORECALCULOHORA  

A opção de visualizar o envelope de pagamento por centro de custo somente estará visível quando o parâmetro Utiliza Cálculo por Centro de Custo nos parâmetros do sistema estiver marcado. Ao acessar o envelope "Por Centro de Custo" será apresentada a visualização do movimento distribuído por centro de custo de acordo com a ficha financeira.  
   
**Observações:**  
1.   O usuário poderá selecionar o mês e ano competência, o período e o Centro de Custo. Qualquer mudança nestes campos, o sistema selecionará "Todos" como opção de Centro de Custo e a visão da movimentação será atualizada.  
2.   Para integração do Folha de Pagamento com Educacional, a coluna "referência" descreve o número de horas/aula referente à competência em questão.  
3.   Para integração do Folha de Pagamento com Educacional, os usuários têm a opção de associar fórmulas de **HORA** e **REFERÊNCIA** em eventos do tipo **VALOR.**  
4.   Quando houver **Atrasos,** no envelope o campo referência será informado em minutos e quando houver **Faltas,** no envelope, o campo referência será informado dias/aulas do professor, ou seja, se o professor faltar duas aulas ele terá duas faltas demonstradas no envelope.

Para visualizar os eventos com valores zerados no envelope, será necessário marcar o parâmetro '**Visualização de eventos com valores zerados no envelope**', disponível em **RM | RH | Folha de Pagamento | Configurações | Folha de Pagamento | Folha Normal | Ficha Financeira**. Como esse parâmetro está vinculado ao usuário, para sua manipulação, será necessário que o usuário tem permissões de acesso aos parâmetros do sistema.

A partir da versão **12.1.2310.1**, estará disponível o botão '**Eventos Zerados'** que ao clicar serão exibidos os eventos com valores zerados na grid de eventos do envelope. Para que seja apresentado o botão no envelope de pagamento, o parâmetro '**Visualização de eventos com valores zerados no envelope**', disponível em **RM | RH | Folha de Pagamento | Configurações | Folha de Pagamento | Folha Normal | Ficha Financeira**,deverá estar **desmarcado**.

Ao selecionar uma coluna na visão do envelope e agrupar será feita a soma de valores de acordo com o agrupamento.  
   
**Exemplo:**  
Selecionar a coluna INSS  
Serão separados os eventos que incidem INSS e os eventos que não incidem INSS  
Será feita a soma dos valores dos eventos que incidem INSS e dos eventos que não incidem INSS

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
