---
content_hash: cc9f9f58b170e6de7b3eeb5f3c7e5a69798990de8e6ecf6ae09b8f87f4cc5164
fetched_at: '2026-06-29T00:09:47.732163+00:00'
page_id: '435105055'
product: rm
source: tdn-rm
title: Reajuste das Vendas
type: documentation
url: https://tdn.totvs.com/display/LRM/Reajuste+das+Vendas
version: 18
---

true

Na tela de Reajuste de Parcela iremos reajustar monetariamente os contratos gerados no sistema. Automaticamente será marcada a coligada qual o usuário está conectado e seus empreendimentos

Poderá ser informado um período mensal aos campos de data  para a filtragem de reajustes pendentes, e também será possível visualizar as pendências de reajuste através do botão [Reajustes Pendentes] .

**Seleção de coligadas:** Exibe as coligadas quais o usuário conectado ao sistema possui permissão de acesso e execução do reajuste. Através desta funcionalidade é possível fazer o reajuste de vendas  em empreendimentos de diversas coligadas. O botão [Todos] permite também a seleção  de todas as coligadas ou a remoção de marcação de todas as coligadas.

**Seleção de Empreendimentos:** Inicialmente, ao abrir a tela do processo, todos os empreendimentos da coligada qual o usuário está conectado são  exibidos selecionados. O botão [Todos] permite também a seleção  de todos os empreendimentos ou a remoção de marcação de todos.

**Reajustes Pendentes:** Nesta opção, será mostrado todas as Vendas / Alugueis com reajustes pendentes,  com datas superior ou inferior a data do sistema.  Para visualizar as datas desejadas, crie um filtro com a data do próximo reajuste menor igual a hoje

**Reajustar até o dia de vencimento da parcela:** Caso marcado indica que deve reajustar até o dia de vencimento da parcela. Se estiver desmarcado indica que deve reajustar até o dia que o usuário informar no caso de antecipação de parcela.

**Pesquisar somente venda com distrato efetivado:** Com este parâmetro marcado, ao mandar pesquisar, o sistema apresentará somente as Vendas/Alugueis que foram distratadas e tem reajustes a serem efetuados.

**Geração de Boleto no RM Fluxus:** Ao mandar reajustar as vendas com este parâmetro marcado, o sistema irá reajustar somente no Fluxus, no SGI as parcelas não sofrerão alterações.

**Filtrar vendas com Boleto Gerado:** Ao pesquisar o mês com este parâmetro marcado, o sistema apresentará somente as venda que já foram reajustadas somente no Fluxus.

**Consultar Log:** Consulta o Histórico de reajustes com as mensagens de erro.

**Data para cálculo:** Este campo será preenchido automaticamente ao pesquisar as vendas, de acordo com a data de pesquisa. Ao alterar este campo com uma nova data, o sistema irá levar em consideração esta nova data para efetuar os cálculos. Os contratos serão reajustas até esta nova data informada.

**Filtro por:** Este filtro será utilizado somente no quadro Vendas programadas para reajuste para filtrar Venda ou Cliente que designa do mesmo.   \*Observação:\* Será apresentado somente Vendas/Alugueis que já tenham o Plano de Financiamento gerado e já foram integrados com o Financeiro.

falseContabilização do Reajuste

Para contabilizar o reajuste é necessário informar no Contrato de Venda no grupo Dados Gerais, item Contabilidade, os eventos contábeis para Reajuste. Estes eventos podem ser por percentual ou por fórmula.   
  
**1 - Eventos Contabeis.**  
     **1.1 - Itens Evento**   
             Ao configurar os itens do evento tenha muita atenção com o campo "Classif. Conta:", este campo é utilizado na busca para o preenchimento correto dos valores dos itens. Caso o mesmo possua espaços ou tenha sido cadastrado com alguma diferença poderá ocorrer divergência no cálculo do contábil para registrar os valores de debito e credito.  
**Sugestão:** O valor digitado na conta que terá seus vinculos criados, copie e cole nos defaults.  
**Exemplo:** Nos itens do evento contábil foi definido que o default contábil virá da subunidade, então, no default contabil da subunidade cadastramos qual é a conta contábil, percentual e a classificação da conta e iremos informar (CMCREDTOTVS).  
Agora vamos preparar os itens do evento que será utilizado na contabilização, informaremos que o default será a subunidade e os campos necessários, já o campo Classif. Conta informamos o valor informado no cadastro do default contábil cadastrado no empreendimento (CMCREDTOTVS).   
Com está configuração os valores irão bater corretamente.  
Caso ao informar em um dos dois campos um valor diferente como o que apresentamos aqui (CMCRED) irá ocorrer divergência entre credito x debito   
**Lembrete:** O campo classificação da conta é um campo livre, você digita o valor que desejar para configurar.

**Eventos por Percentual**

É necessário escolher no item do evento o valor de incidência que será usado na contabilização e o percentual dele que será considerado. São várias possibilidades, escolha atentamente de acordo com sua necessidade.

**Eventos por Fórmula**

Nessa opção a fórmula é sempre executada duas vezes. Uma para o contexto de **Correção Monetária** e outra para o contexto de **Juros de Contrato**. É necessário que a fórmula identifique qual contexto do reajuste está sendo executado no momento e com esta informação proceda com o cálculo correto da contabilização para este contexto. Para isso é necessário ter um item para Correção Monetária e outro para Juros de Contrato. E em cada item, deve ser usada uma fórmula específica para ele. Sendo assim, no item de Correção Monetária, deve ser verificado qual o contexto de contabilização está sendo executado. Se for de Correção Monetária, a fórmula deve fazer o cálculo e retornar o valor esperado. Se for o contexto de Juros de Contrato, a fórmula deve retornar 0. Assim se garante que o valor gerado na fórmula de Correção Monetária, seja contabilizado apenas no lote de Correção Monetária evitando que ele seja incluído também no lote de Juros de Contrato. Para a contabilização de Juros de Contrato deve-se proceder de forma análoga.

A verificação de qual contexto está sendo executado é feita pela variável de contexto **TIPOREAJUSTE** que terá um dos dois valores, **CM** para Correção Monetária e **JUROS** para Juros de Contrato.

***Exemplo de Fórmula a ser usada no item de contabilização de Correção Monetária:***

***SE CONTEXTO('TIPOREAJUSTE') = 'CM' ENTAO***

***1000***

***SENAO***

***0***

***FIMSE;***

***Exemplo de fórmula a ser usada no item de contabilização de Juros de Contrato:***

***SE CONTEXTO('TIPOREAJUSTE') = 'JUROS' ENTAO***

***500***

***SENAO***

***0***

***FIMSE;***

Nos exemplos acima foram usados valores fixos, sendo 1000 para Correção Monetária e 500 para Juros de Contrato. Porém, é possível fazer vários cálculos para se chegar no valor desejado, declarando e usando variáveis, usando funções de fórmulas, chamada de outras fórmulas, chamadas de consultas SQL, além claro de operações matemáticas.

Os trechos dos códigos que retornam 0 são para garantir que quando o contexto não é o desejado para aquela fórmula o valor considerado seja 0.  Isso faz com que não seja gerada nenhuma linha de contabilização em lotes indesejados.

**ATENÇÃO:**

1 - O processo de reajuste será executado automaticamente pelo módulo financeiro, ao executar os processos de baixa e cancelamento de baixas de parcelas. Também será executado a contabilização do reajuste desta parcela alterada Ao baixar uma parcela no Financeiro, será executado o reajuste do Imobiliário, verificando a data da baixa, para que esta parcela fique reajustada até a data da baixa da parcelas. Ao cancelar uma baixa de parcelas, será executado o reajuste do Imobiliário, verificando a ultima data de reajuste do grupo, para que esta parcela fique reajustada igual as demais parcelas do seu grupo de financiamento. Caso o reajuste seja até o vencimento da parcela e no grupo haja alguma parcela cancelada em uma data posterior ao reajuste a parcela será considerada no reajuste até a data de cancelamento.

2 - Ao reajustar todos os componentes do plano de financiamento de uma venda a data de último reajuste será atualizado tanto na parcela quanto na venda.

Observação: Com o reajuste on-line somente a data de último reajuste da parcela é atualizado.

**Observação:** Alguns parâmetros de reajuste serão retirados do sistema a partir da versão 12.1.23. Caso esses parâmetros estiverem habilitados, ao executar um reajuste, aparecerá no log do processo uma mensagem de aviso, informando quais parâmetros serão descontinuados do TIN. São eles:

* Utiliza data vencimento para definir se a correção será com índice antes ou após.
* Calcula Correção Monetária sobre o Saldo Devedor Total Amortizado.
* Calcula Juros de Contrato sobre o Saldo Devedor Total Amortizado.
* Valores calculados na correção serão arredondados mês a mês.

Reajuste Revitalizado ( Clientes de MG )

Com a revitalização do processo de reajuste de venda , temos um grande ganho de performance e flexibilidade , possibilitando que o cliente customize o cálculo de uma forma mais simples.
