---
content_hash: f888817e33e7ed9a02f6359220bde166663e0eb1151eb336da2cab33f3f7bdbb
fetched_at: '2026-06-29T00:10:03.826833+00:00'
page_id: '452719160'
product: rm
source: tdn-rm
title: Cálculo de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719160
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Cálculo de Férias**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Através deste processo são calculadas as férias que foram previamente cadastradas no mês e/ou próximos meses, ou calculado apenas o abono pecuniário cadastrado sem o gozo das férias.  
**Atenção I:**  
O cadastramento das férias deve ser através dos módulos:   
Funcionários | Movimento | Férias ou Férias | Férias Coletivas / Globais.  
   
**Atenção II:**  
São calculadas somente as férias cadastradas com situação das férias igual 'M-Marcadas'.  
   
É possível alterar a data de pagamento das férias, para a data informada no campo 'Nova Data Pagto:'

Na visão do envelope de férias tem o parâmetro Não Recalcular. Caso este parâmetro esteja marcado o envelope de férias e eventos que foram alterados manualmente não serão recalculados. Caso este parâmetro esteja desmarcado, o cálculo será feito para todos os eventos e os mesmos voltarão aos valores originais, inclusive os eventos alterados manualmente.

**Observação:**

Caso o parâmetro '**Não calcula Recibo de Férias**', disponível em **RH | Administração de Pessoal | Funcionários | Informações para o Cálculo | Parâmetros**, esteja 'marcado', o sistema não irá calcular o recibo de férias para o funcionário e também não serão exibidos no cadastro de férias o campo 'Data Pagamento' e os botões de 'Calcular' e 'Visualizar Recibo' de férias.

A mudança da situação do funcionário para 'Férias', continuará sendo feito pelo processo 'Lançar' férias'.

O processo 'Finalizar' férias vai mudar a situação do funcionário de 'Férias' para 'Ativo' e atualizar os dados cadastrais do período aquisitivo de férias.

O sistema não irá consistir na Liberação de Competência se constam no envelope do funcionário os códigos de cálculo específicos de férias para funcionários com o parâmetro marcado.

11Cálculo

Cálculo  
No cálculo do INSS é considerada a tabela do mês de início de gozo e no cálculo do IRRF é considerada a tabela do mês da data de pagamento.  
   
O evento cujo o cálculo necessite que as médias já estejam calculadas, precisam ter prioridade 70. Todos os eventos com prioridade 70 são recalculados após o cálculo da média.  
O cálculo da média não segue prioridade, sempre é calculado por último, primeiro todo o envelope é calculado e depois é calculada a média. Porém para atender situações em que o evento precise do cálculo da média já calculada, este evento deve ter prioridade 70, assim o sistema entende que este evento precisa ser recalculado após as médias.  
   
Caso a variável de fórmula VFER( ) seja utilizada no processo de cálculo de férias, é considerado o valor calculado em memória, e quando utilizada em qualquer outro processo, é considerado o valor do evento gravado no banco de dados, inlcusive na provisão.   
Quando a variável é utilizada fora do cálculo de férias, são considerados os valores do recibo com a maior data de pagamento anterior ao último dia de competência atual.  
   
Quando a variável LIQFERIAS é utilizada no cálculo das férias, é considerado o valor do recibo do cálculo.  
Quando é utilizada no envelope de pagamento, é considerado o líquido do primeiro recibo de férias que esta com a situação diferente de 'F-Finalizada'. Caso não encontre nenhum período 'não finalizado', é retornado o líquido do último recibo de férias 'F-Finalizadas'.  
   
Para atender o recurso onde o usuário pode calcular mais de umas férias para o funcionário, foi criada a variável LIQFERIASDATA().  
   
No cálculo da média HORA do grupo de insalubridade, definido no cadastro de sindicato, é considerado o valor do evento, mesmo quando o evento é do tipo HORA.  
   
Caso o parâmetro 'Desconta empréstimo de folha nas férias' existente nos parâmetros do Labore, esteja marcado, o processo de cálculo das férias guarda o histórico dos empréstimos descontados.  
   
É possível calcular duas férias com o mesmo caixa. Porém somente é permitido calcular o 2º recibo de férias quando o 1º recibo está com a situação de férias igual a 'P-Pagas' e os eventos estão lançados no envelope de pagamento.  
Quando existir mais de uma férias com o caixa diferente, o processo calcula apenas a primeira do período selecionado, as demais devem ser calculadas informando o período específico ou através do processo individual.  
   
**Atenção:**

* Para o cálculo da base de IRRF de férias do segundo recibo, são verificados os eventos de férias no envelope de pagamento e aos eventos de férias do 2º recibo.
* No cálculo do abono pecuniário, sem o preenchimento do gozo de férias, a base para verificação do salário e outros é a data de pagamento, uma vez que não existe o período do abono.
* Ao excluir um Período de férias,  será gerado um evento para o eSocial Evento de Exclusão (S-3000) .

Quando no sindicato o parâmetro 'Permite antecipação de dias de férias do próximo período aquisitivo' está confirmado, as férias proporcionais são demonstradas em dias.  
Isso porque quando ocorrer situação do número de dias de férias não representar um número inteiro de avos, não teria como demonstrar corretamente estes avos.  
   
**Exemplo:**   
O funcionário tem direito a 3/12 avos de férias e já antecipou 1 dia. Na rescisão é pago 6.5 dias de férias proporcionais. Não tem como representar este número em avos.  
   
   
O campo 'Situação das Férias' é preenchido conforme abaixo:  
G – Aguardando Aprovação do Gestor (quando o subordinado cadastra a sugestão de férias);  
D – Aguardando Aprovação do DP (quando o gestor aprova a sugestão e não tem permissão de marcar férias);  
M – Marcadas (quando o DP aprova ou quando o gestor tem permissão para marcar);  
P – Pagas (quando calcula as férias e as mesmas são lançadas na movimentação);  
F – Finalizadas (quando fecha o período aquisitivo e abre outro período aquisitivo, independente de ser um novo ou o mesmo);  
X - Finalizadas para o próximo mês (quando é processada a finalização de férias para a próxima competência. Na liberação de competência este campo é alterado para F – Finalizadas).

2Pensão Alimentícia

Pensão Alimentícia  
Para o funcionário com pensionistas, é feita a distribuição dos respectivos valores, gravando na movimentação da pensão com o tipo de pensão igual a '1-Férias' e preenchendo o campo 'Data Pagto. Férias'.  
**Atenção I:**  
O código de cálculo '113-PENSÃO ALIMENTÍCIA SOBRE FÉRIAS' é utilizado apenas no cálculo do recibo de férias. Para calcular a pensão sobre as férias da rescisão, é lançado o código de cálculo '319- PENSÃO ALIMENTÍCIA FÉRIAS NA RESCISÃO'.   
   
**Atenção II:** Para o cálculo da pensão alimentícia no recibo de férias, é considerado como base de cálculo os eventos do recibo de férias mais os eventos que estão no envelope (eventos que incidem em Pensão de Férias).  
Porém para deduzir o valor da pensão já pago (quando o funcionário tem mais de um recibo de férias no mesmo mês) é considerado o valor da pensão do outro recibo de férias, isso somente quando a situação de férias é 'P-Pagas', 'F-Finalizadas' ou 'X-Finalizadas Próximo Mês'.

3Múltiplos Vínculos

Múltiplos Vínculos  
Sempre que o funcionário tiver múltiplos vínculos, é imprescindível que todas as chapas (vinculadas e centralizadora) tenham férias cadastradas no mesmo período de gozo. Caso haja vínculos em outras coligadas, o cálculo das férias deve ser realizado por último na coligada centralizadora.

4Faltas

Faltas  
São consideradas as faltas do período aquisitivo, sendo que:

* caso o parâmetro 'Utiliza controle de faltas para avos' existente nos parâmetros do Labore esteja marcado, são verificadas as faltas do primeiro ao último dia do período aquisitivo, assim como o dia real do estorno da falta indevida.

caso o parâmetro não esteja marcado, são verificadas as faltas do mês posterior ao mês de início do período aquisitivo até o mês fim do período aquisitivo.  
**Exemplo:**  
Período aquisitivo: 16/04/2010 a 15/04/2011  
Período para verificação das faltas   
Parâmetro marcado: 16/04/2010 a 15/04/2011  
Parâmetro desmarcado: 05/2010 a 04/2011

5Salário Família

Salário Família  
Caso o parâmetro 'Lança Salário Família nas Férias' existente nos parâmetros do Labore, esteja marcado, o salário família nas férias somente é calculado quando não existe evento de salário família no envelope de pagamento do funcionário, no mês do gozo das férias.  
**Atenção I:**  
É considerado na base do salário família nas férias, todos os eventos que incidem salário família e estão no envelope de pagamento e recibo de ferias no mês do gozo das férias.  
   
**Atenção II:**  
Caso o parâmetro 'Usa salário nominal' existente nos parâmetros do Labore, esteja desmarcado, é considerado o valor do código de cálculo 38, independente da incidência de evento, na base de cálculo do salário família.

## **02. EXEMPLO DE UTILIZAÇÃO**

Supondo que foram cadastradas férias para determinados funcionários da seção 01.01 na base exemplo no período de 02/05/2023 a 31/05/2023 e será feito o cálculo das mesmas.

Parametrize a tela conforme print abaixo e clique em Executar:

Depois basta acessar as férias no cadastro de funcionário que todos os recibos de férias estarão disponíveis nos respectivos funcionários com os dados acima.

## **03. TELA Cálculo de Férias**

**Principais Campos e Parâmetros**

| Ação | Descrição |
| --- | --- |
| Quebra de Seção | Insira a seção para qual será calculada as férias |
| Período | Insira o período para o qual será calculada as férias |
| Data Pagamento | Será possível alterar a data de pagamento registrada no cadastro para nova data de pagamento. Atente-se para a legislação no momento de alterar a data. |
| Seleção de funcionários | Selecione os funcionários para os quais será calculada as férias |

## 

## **04. T****ABELAS UTILIZADAS**

* PFUFERIASPER
* PFUFERIASRECIBO

Local da Chamada

Processo Visão de Funcionário

Processo Férias | Calculo
