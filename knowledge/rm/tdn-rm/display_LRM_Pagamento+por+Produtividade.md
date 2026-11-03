---
content_hash: 2dedf37b141e24c4aaebe80295b7743c2d996ed553b9875b1fb47cc77152d890
fetched_at: '2026-06-29T00:10:15.370811+00:00'
page_id: '464962970'
product: rm
source: tdn-rm
title: Pagamento por Produtividade
type: documentation
url: https://tdn.totvs.com/display/LRM/Pagamento+por+Produtividade
version: 19
---

---

Acesse em Menu Controle | Mnha Obra | Mão de Obra | Pagamento por Produtividade.

Esta tela detalha os valores referentes aos pagamentos da folha de produtividade por funcionário e tarefa (Anexo Item de Pagamento por Produtividade).

**Calcular Pagamento por Produtividade**

O percentual do Avanço Físico depende do período de apuração selecionado, como no exemplo abaixo:

* 30% em 01/01/2019
* 40% em 03/01/2019
* 50% em 05/01/2019
* 70% em 20/01/2019
* Ex.1: Período de Apuração: 05/01/2019 à 31/01/2019
  + Percentual real: 70 - 40 = 30%
* Ex.2: Período de Apuração: 01/01/2019 à 31/01/2019
  + Percentual real: 70%

Este processo terá como parâmetros data inicial e final, ano, mês e período de competência, evento da folha de pagamento e data de pagamento.

Após a geração dos dados, será possível gerar o arquivo com os dados do pagamento para a importação do mesmo.

* No período de apuração, a "Data final" deve abranger a data em que foram registrados os apontamentos de avanços físicos e que esses registros estejam validados dentro das folhas de tarefas encerradas.

Para o campo "Evento", existe o parâmetro de projeto em Mobilidade/Folha Tarefa que é o valor padrão que será considerado no processo. Para permitir a alteração desse valor na tela, é necessário alterar a permissão de alteração no cadastro de perfis do usuário.

Após a execução do processo, é exibido no log do mesmo, informando todo o relato do cálculo do pagamento para os funcionários:

O log é dividido em 3 partes. A parte **superior** informa o período escolhido e quantos dias serão apurados, no **meio** temos os valores a ser pago para cada membro de folha de produtividade do período e na parte **inferior** temos o totalizador a ser pago no período.

Na parte dos membros temos temos os valores discriminados por tarefa e folha de produtividade, onde o cálculo se diferencia entre pagamento por **peso** e por **valor fixo**.

No pagamento por valor fixo, o valor a ser pago é referente à % de avanço físico multiplicada pelo valor fixo.

**Exemplo:** Funcionário Alessandro  
Folha tarefa 2 - Tarefa 001.02.01 = 100% \* 200 = 200  
Folha tarefa 2 - Tarefa 001.02.02 = 20% \* 300 = 60

Já no pagamento por peso, o log informa a % do peso, que é a % que o funcionário deve receber em cima do valor concluído da tarefa na folha à ser distribuído para os membros de peso.

**Exemplo:** Folha produtividade apenas com peso  
Folha tarefa 3 - Tarefa 001.03.01  
Alessandro: 3350 \* 26.840% = 899.13  
       Beatriz: 3350 \* 43.290% = 1450.22  
   Ana Luiza: 3350 \* 29.870% = 1000.65

**Exemplo 2:** Folha produtividade com peso e valor fixo  
Folha tarefa 2 - Tarefa 001.02.01  
Valor concluído: 800  
Pagamento por valor fixo: 200 (Alessandro) + 200 (Beatriz) = 400  
Valor à ser distribuído entre os membros de peso: 800 - 400

Pagamento por peso: 400 \* 100% (Ana Luiza)

Como Ana Luiza é o único membro da folha com peso, ela recebe o restante do valor. Caso existissem outros membros, o valor seria divido de acordo com a proporção de peso informado no cadastro do membro (como é mostrado no exemplo de cálculo por peso).

## Processo para geração de um novo arquivo

O arquivo poderá ser gerado no formato para RM ou Protheus.

Foi criado um novo processo para geração do arquivo com os dados do pagamento de Produtividade, Menu Controle | Mobilidade | Pagamento por Produtividade | Processos | Gerar Arquivo de Pagamento por Produtividade;

Para execução do processo de geração de arquivo foi criado um objeto gerencial '**TOPLAY0005 - Exportação de Dados- Pagamento Por Produtividade**';

* Informe o Layout Gerador de Saida;
* Informe o local onde serão gerado o(s) arquivo(s);
* O nome do arquivo é parametrizado no gerador de saídas. Caso não esteja informado o sistema irá importar o arquivo com o nome padrão: "Arquivo de Pagamento por Produtividade"
* Arquivo gerado sem parametrização no gerador de saídas:

* Arquivo gerado com parametrização informada no gerenciador de saídas:

**Importação do Arquivo - Folha de Pagamento**

Para realizar a importação do(s) arquivo(s) gerado(s), deve-se cadastrar um layout de importação. No módulo de Folha de Pagamento acesse Menu Configurações | Importações | Layout de Importações;

O cadastro deve seguir a seguinte estrutura:

Após o cadastro o sistema estará apto a receber a importação para o Envelope de Pagamento. Acesse Menu Configurações | Importações | Layout de Importações | Processos | Importação da Ficha Financeira;

* Selecione o arquivo gerado através do processo;
* Escolha a ação desejada referente a importação para o envelope;
* Executar;

Procedimento para importação no Protheus: 

---
