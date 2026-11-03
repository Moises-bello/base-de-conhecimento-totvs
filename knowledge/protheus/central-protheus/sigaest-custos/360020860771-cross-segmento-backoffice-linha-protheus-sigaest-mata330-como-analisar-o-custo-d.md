---
article_id: 360020860771
category: SIGAEST - CUSTOS
content_hash: 2faa5595364c2da2209de133bfd5bd1ce4588b9536f9605f7f4588d359024516
fetched_at: '2026-06-28T22:39:00.387094+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como analisar
  o custo do produto no Protheus passo a passo?
type: support-article
updated_at: '2025-09-17T11:12:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34175167127063)*** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Como realizar a análise do cálculo de custo médio no Protheus (MATA330) e Acompanha Custos (MATA038) e interpretar o relatório KARDEX por Período (MATR900) para identificar distorções e validar se o custo está correto?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Tópicos:**

1. [Manter a rotina de custo médio atualizada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo#:~:text=1.%20Manter%20a%20rotina%20de%20custo%20m%C3%A9dio%20atualizada%3A)
2. [Executar a rotina de Custo Médio (MATA330)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo#:~:text=2.%20Executar%20a%20rotina%20de%20Custo%20M%C3%A9dio%20(MATA330))
3. [Periodo de Analise](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo#:~:text=3.%20Per%C3%ADodo%20de%20an%C3%A1lise)
4. [Parametrização do relatório MATR900](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo#:~:text=4.%20Parametriza%C3%A7%C3%A3o%20do%20relat%C3%B3rio%20MATR900)
5. [Como avaliar o relatório MATR900 após o recálculo do custo médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo#:~:text=5.%20Como%20avaliar%20o%20relat%C3%B3rio%20MATR900%20ap%C3%B3s%20o%20rec%C3%A1lculo%20do%20custo%20m%C3%A9dio)
6. [Meu custo está incorreto no Kardex do período atual. Como identificar o problema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo#:~:text=6.%20Meu%20custo%20est%C3%A1%20incorreto%20no%20Kardex%20do%20per%C3%ADodo%20atual.%20Como%20identificar%20o%20problema%3F)
7. [Caso ainda persista divergência no custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo#:~:text=7.%20Caso%20ainda%20persista%20diverg%C3%AAncia%20no%20custo)
8. [Duvida de custo diferente entre filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-analisar-o-custo-do-produto-no-Protheus-passo-a-passo#:~:text=8.%20Duvida%20de%20custo%20diferente%20entre%20filiais)

**Solução**

A análise de custo de estoque deve ser feita de forma criteriosa. Para maior precisão, recomenda-se avaliar um único produto por vez, seguindo as premissas apresentadas a seguir:

### **1**. **Manter a rotina de custo médio atualizada:**

É fundamental que o ambiente esteja atualizado com o último fonte da rotina de Custo Médio (MATA330), juntamente com o pacote de acumulados do BackOffice mais recente.

Atualizações periódicas corrigem possíveis inconsistências no cálculo, portanto manter o sistema atualizado ajuda a reduzir divergências e evita erros recorrentes.

Recomenda-se também reinstalar as procedures 17 e 19, que são utilizadas no processo de apuração do custo, garantindo que todos os cálculos sejam realizados com a versão correta.

[Pacote acumulado Backoffice:](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602)

### **2. Executar a rotina de Custo Médio (MATA330)**

Após garantir que o sistema está atualizado, o próximo passo é executar a rotina de recálculo de custo médio.

Isso permite atualizar os valores de custo dos produtos no sistema e preparar os dados para análise no relatório KARDEX (MATR900).

**2.1 Procedimento:**

1. Acesse o módulo **SIGAEST**
2. Acessar **-> Miscelânea  -> Cálculos→  Recálculo de Custo Médio MATA330**

**2.2** **Período de analise:**

**Data inicial:**

 A data inicial é  um dia posterior ao último fechamento é identificado pelo parâmetro **MV\_ULMES**.

**Exemplo:** se o fechamento do estoque foi em 31/05, a data inicial será **01/06**.

**Data final (parâmetro Data Limite Final):**

 Informe a data até a qual deseja que o sistema execute o recálculo do custo médio.

 Essa data define até quando o sistema atualizará os custos dos produtos durante a execução da rotina.

 Exemplo: se você deseja analisar todo o mês de junho, a Data Limite Final será **30/06**.

**2.3** **Perguntas da execução do Custo Médio (MATA330)**

Durante a execução da rotina de recálculo do custo médio, existem diversas perguntas que podem influenciar o cálculo do custo dos produtos.

É importante que o cliente esteja ciente dessas opções para compreender como o sistema processa os lançamentos.  
Para mais detalhes sobre cada pergunta e seu impacto, consulte a documentação oficial:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

**2.4** **Método de Apropriação:**

Uma das perguntas importantes da execução da rotina é o "Método de Apropriação":

* O método de apropriação define como o sistema ordena as movimentações de estoque (entradas e saídas) para calcular o custo médio. A escolha do método impacta diretamente no cálculo do custo dos produtos.
* **Opções disponíveis:**

  + **Mensal:** O sistema apura todas as entradas do mês, calcula o custo médio ponderado e valoriza todas as saídas com este custo.
  + **Diário:** O sistema calcula o custo médio diariamente, considerando todas as entradas do dia para valorizar as saídas do mesmo dia.
  + **Sequencial:** O sistema valoriza as movimentações na ordem em que foram registradas, independentemente da data.
* **Relevância:** A escolha do método de apropriação deve ser feita com base na política de controle de estoque da empresa e pode afetar a precisão dos custos apurados.
* Para mais detalhes sobre cada método e suas implicações, consulte a documentação oficial:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Quais são os Métodos de Apropriação para execução do Recálculo do Custo Médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033673914-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Quais-s%C3%A3o-os-M%C3%A9todos-de-Apropria%C3%A7%C3%A3o-para-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

**2.5** **Configure o parâmetro MV\_DBLQMOV:**

Defina com a **última data do período**. Isso garante que movimentações em aberto ou lançamentos fora do período não interfiram no recálculo, evitando divergências temporárias nos saldos e custos.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o bloqueio de Movimentações no Estoque durante o Fechamento de Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-o-bloqueio-de-Movimenta%C3%A7%C3%B5es-no-Estoque-durante-o-Fechamento-de-Estoque)

**2.6** **Recursividade na base de dados:**

Caso ocorra recursividade ao executar a MATA330, execute primeiro o relatório [**MATR331 (“Análise de Recursividade”)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018402631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Recursividade-no-processamento-do-recalculo-do-custo-m%C3%A9dio-MATA330) e corrija os problemas identificados.

Somente após resolver a recursividade, execute novamente a rotina de custo médio (MATA330).

***O Recálculo reordena os custos dos produtos de forma que apresente os dados corretamente após as movimentações durante um período.***

### **3. Período de análise**

A análise do custo deve abranger o **período de estoque aberto**, ou seja, do **dia seguinte ao último fechamento de estoque** até a **Data Limite Final** utilizada no processamento do recálculo do custo médio.

Para verificar a variação do custo e validar o valor final dos produtos, utilize o **relatório Kardex por Período (MATR900)**.

Mais informações sobre a configuração correta do relatório podem ser consultadas na documentação oficial:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)

Segue também o vídeo how to de como fazer a parametrização do relatório:

[How To | MP-SIGAEST Configurando Kardex Por Periodo-MATR900 #TOTVS\_Backoffice\_Linha\_Protheus](https://www.youtube.com/watch?v=-bjl1lSyC0E)

### **4. Parametrização do relatório MATR900**

Para analisar as informações de maneira assertiva, é de suma importância parametrizar os filtros do relatório de forma correta. Segue algumas informações de como parametrizá-las:

- **Data inicial**: Data do último fechamento de estoque + 1 dia, por exemplo: se o último fechamento de estoque foi em 31/03, a data inicial do relatório deverá ser 01/04.

**- Data final**: Data limite utilizada no processamento do recálculo do custo médio.

**OBS:** Se não colocar a data inicial corretamente, irá pegar os saldos iniciais da SB9 de um período anterior e não irá mostrar o cálculo de forma devida.

- **Sequência de impressão**: Selecionar **Cálculo**, para exibir saldo, entradas, saídas e custo médio.

**OBS:** Se for selecionado por digitação, o relatório irá mostrar como o usuário digitou no sistema e não irá apresentar como a rotina calculo e ordenou.

- **Verificação do parâmetro MV\_CUSFIL:**

Este parâmetro permite o custo ser aglutinado por Armazém (A), Filial (F) ou Empresa (E).

* Caso esse esteja configurado como **A**, imprimir o Kardex apenas do armazém analisado;
* Caso esteja configurado como **F**, imprimir o Kardex com a informação \*\* no campo armazém;
* Caso esteja como **E**, imprimir o relatório de todas as filiais, considerando ## no campo armazém;

Para mais informações sobre qual é o conceito do parametro MV\_CUSFIL acesse nossa documentação:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do parâmetro MV\_CUSFIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CUSFIL)

**Importante:** Para não correr riscos do relatório imprimir algum resultado diferente por conta dos demais usuários que estão operando o sistema, o parâmetro **MV\_DBLQMOV** deve estar configurado com a data do ultimo dia do período em validação. No nosso exemplo, seria o dia 30/04 (Ultimo dia do mês em que está sendo processado o relatório)

### **5. Como avaliar o relatório MATR900 após o recálculo do custo médio**

Após a execução da rotina MATA330, é essencial verificar se os dados no relatório MATR900 – Kardex por Período estão consistentes. Siga os passos abaixo:

**5.1 Verifique os saldos iniciais na SB9**

Acesse a tela SB9 – Saldo Inicial de Estoque.

Consulte os saldos iniciais dos produtos no período analisado.

Compare esses saldos com o saldo inicial apresentado no relatório MATR900.

Se houver divergências, investigue possíveis causas, como o último fechamento de estoque incorreto.

**5.2 Análise da ordenação dos movimentos**

Verifique se os movimentos de estoque (entradas, saídas e transferências internas) seguem a ordem correta, respeitando o método de apropriação definido na MATA330 (Diário, Sequencial ou Mensal).

Para mais detalhes sobre interpretação do relatório e análise do custo antes e depois do recálculo, consulte:

[Como é feita a ordenação dos movimentos após recálculo do custo médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-ap%C3%B3s-rec%C3%A1lculo-do-custo-m%C3%A9dio)

[MATR900 – Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Interpretando-o-Custo-no-Kardex-antes-e-depois-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

### **6. Meu custo está incorreto no Kardex do período atual. Como identificar o problema?**

Caso o custo apresentado no **relatório MATR900** esteja divergente, siga os passos abaixo para diagnosticar a causa:

**6.1 Analisar os períodos anteriores**

Imprima o **Kardex por Período (MATR900)** dos três últimos períodos.

Verifique se houve **fechamento incorreto**, conferindo se os **Saldos Iniciais** correspondem aos **Saldos Finais** do período anterior.

**6.2 Verificar o Custo Médio Unitário (B2\_CM1) por Armazém**

Observe se existem valores muito elevados nesse campo, pois podem **distorcer o custo** e até gerar **estouro de campo** no processamento da rotina **MATA330 – Recálculo do Custo Médio**.

**6.3 Conferir o saldo inicial (SB9)**

Avalie os saldos iniciais provenientes do **último fechamento de estoque (B9\_VINI1…5)**.

A causa do problema pode estar em períodos anteriores, sendo necessário rastrear a origem da divergência.

**6.4 Analisar a ordenação das movimentações**

Confira se os **movimentos de entradas, saídas e transferências internas** estão processados na **sequência correta**, conforme o **método de apropriação** configurado na rotina (Diário, Sequencial ou Mensal).

A ordenação correta é fundamental para que o **custo médio seja calculado de forma precisa** e reflita os valores reais no MATR900.

### **7. Caso ainda persista divergência no custo**

Se após todas as verificações anteriores o custo ainda estiver incorreto, solicitamos que nos  envie informações detalhadas para análise:

**7.1 Método de apropriação utilizado**

Diário, Sequencial ou Mensal.

**7.2. Execução do Recálculo do Custo Médio**

Foi executado o **MATA330** no período em questão?

Caso não, consulte [como rodar a rotina de custo médio (MATA330)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio).

**7.3 Parâmetros da rotina**

Envie **prints dos parâmetros** utilizados no processamento da rotina do Custo Médio / Acompanha Custos.

**7.4 Pontos de entrada**

Informe se algum **ponto de entrada** foi utilizado no processo.

**7.5 Inspetor de objetos / Central de Diagnóstico**

Anexe o **Inspetor de objetos** do sistema.

**7.6 Relatório MATR900**

Isolando um produto com problema, anexe o **relatório MATR900 em formato PDF com a pagina de parametros e apontando onde que acha que está a inconsistência:**

⚠️ É importante que o MATR900 esteja configurado conforme o boletim:  
[MATR900 – Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-fazer-uma-an%C3%A1lise-de-Custos-no-Protheus)

**7.7 Tabelas de log para validação de apropriações e cálculos**

**Log CV8** (se executado recálculo via MATA330)

Filtre pelo campo **CV8\_PROC = 'MATA330'** da última execução do período.

Envie em formato **.dtc**.

**Log D3X** (se executado via rotina Acompanha Custos – MATA038)

Filtre pelo campo **D3X\_PROC = 'MATA330'**.

Envie em formato **.dtc**.

### **8. Duvida de custo diferente entre filiais**

Caso o custo apresentado entre as filiais seja divergente, valide o boletim abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST – Custo nas transferências entre filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024874171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-nas-transfer%C3%AAncias-entre-filiais)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
