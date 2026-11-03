---
article_id: 4416042752151
category: Folha Mensal
content_hash: 18d7994e4c52810bbedf9ea0d255a8888a2d8467b40b93f2e5d8e71870b6b875
fetched_at: '2026-06-28T22:46:59.288740+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: cadastro e parametrização'
type: support-article
updated_at: '2026-01-31T00:43:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416042752151-RH-RM-FOP-Folha-Anal%C3%ADtica-cadastro-e-parametriza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21920776732439) Tempo aproximado para leitura: **00:09:07 min**  
  
**Dúvida**  
Como realizar o cadastro e a parametrização da folha analítica no módulo Folha de Pagamento, e quais as funcionalidades dos parâmetros?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: **Folha Mensal | Folha Analítica**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416035435031)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416042488983)

**Quebra de Seção:** Permite filtrar as seções que serão consideradas na Folha Analítica, selecionando uma seção específica de acordo com seu código ou utilizando uma determinada quebra de seção.  
  
**Seleção de Funcionários:** Permite filtrar os funcionários lotados nas seções referentes à quebra de seção escolhida. O filtro pode ser de acordo com a Situação, Tipo de Funcionário ou Recebimento.  
  
**Competência:** Permite selecionar para qual competência a Folha Analítica será gerada, assim como o caixa e período. Ao selecionar uma competência anterior à atual, a situação considerada para cada funcionário será a última daquela competência, de acordo com seu respectivo histórico de situação. Uma vez que a situação de funcionários voltando ou saindo de F - Férias ou afastamento do tipo: P - Af. Previdência, T - Af. Ac. Trabalho, O - Doença Ocupacional, M - Serv. Militar, L - Licença s/ venc, E - Licença Mater., R - Licença Remun., I - Apos. Invalidez, U - Outros, S - Mandato Sindical, W - Licença Mater. Compl. 180 dias, Y - Licença Paternidade, na competência atual é atualizada durante o processo de Liberação de Competência, ele pode estar em situação de afastamento antes da execução do processo e ter sua situação alterada para A - Ativo após a execução ou vice-versa. Assim, deve-se ficar atento ao gerar uma Folha Analítica referente a competências retroativas, pois alguns funcionários antes selecionados pelo filtro de situação e que constavam como afastados ou ativos nos contadores de funcionários da Seção e Geral, podem constar como ativos ou afastados e possivelmente não atender mais ao filtro.  
  
**Imprimir Funcionários Sem Movimentação:** Ao marcar o parâmetro, o sistema irá trazer todos os funcionários que não possuem movimentação para o período selecionado. Para que seja possível marcar esse parâmetro, a folha analítica deve ser gerada por seção. Ao gerar por centro de custo, o parâmetro é desabilitado automaticamente.  
  
**Filtrar Base de FGTS de Afastados por Período:** Com esse parâmetro marcado, o sistema exibirá os totais apenas das seções onde há funcionários com movimento no período, considerando o fato de que o parâmetro **Imprimir Funcionários Sem Movimentação** esteja desmarcado. Com o parâmetro **Filtrar Base de FGTS de Afastados por Período** desmarcado, o sistema continuará exibindo totais de seções contendo base de FGTS de afastados, mesmo que a seção não tenha funcionários com movimento no período selecionado. Isso ocorre apenas se houver funcionários com afastamento do tipo T - Acidente de Trabalho, M - Serviço Militar e O - Doença Ocupacional lotados na seção, uma vez que mesmo que os funcionários em tais situações não tenham movimento, a empresa precisa continuar depositando o FGTS deles.  
  
**Chaves Ativas:** Permite filtrar quais eventos serão considerados no relatório de acordo com o valor de Chave associado a cada um deles no seu respectivo cadastro. Para verificar qual a chave do evento, acesse: **Administração de Pessoal | Eventos | Eventos**. Caso nenhuma chave seja selecionada, os eventos não serão filtrados por chave.  
  
**Considera Percentuais para INSS da Seção Centralizadora (SAT/Terceiros):** Marque a opção, caso queira que seja considerado os percentuais de INSS - SAT e Terceiros - da seção centralizadora ao invés dos percentuais cadastrados na seção onde o funcionário estiver lotado.  
  
**Desconsidera da Base FGTS as verbas pagas por Dissídio:** Ao marcar esta opção, a folha analítica será gerada sem considerar as verbas pagas por dissídio nas bases de FGTS.  
  
**Totais de Funcionário, Seção e Gerais:** É possível selecionar separadamente quais bases de cálculo serão levadas para os totalizadores de funcionário, seção e geral da folha analítica. Para que a seleção das bases de cálculo funcione, é necessário importar o layout mais recente da folha analítica pdf e txt. Caso o layout do relatório esteja desatualizado, todas as bases de cálculo serão impressas nos totalizadores de funcionário, seção e geral da folha analítica, independente da seleção realizada.  
  
**Imprimir por Centro de Custo:** Ao marcar esta opção os seguintes campos serão habilitados.

* **Usar filtro:** O sistema filtra os centros de custo dos funcionários considerando somente os de tamanho igual ou inferior ao tamanho do filtro informado, além de comparar cada caractere do centro de custo com máscara do filtro.

**Exemplo:**

Funcionário Centro de Custo  
00001 02  
00002 02.1  
00003 02.1.1  
00004 02.1.2  
00005 01  
00006 01.1.1  
00007 03.1  
00008 03.1.2   
Informando o filtro 02, o sistema irá gerar somente o funcionário 00001;  
Informando o filtro ??, o sistema irá gerar somente o funcionário 00001 e 00005;  
Informando o filtro 02.1, o sistema irá gerar os funcionários 00001 e 00002;  
Informando o filtro 0?.1, o sistema irá gerar os funcionários 00001, 00002, 00005 e 00007;

* **Usar código de quebra:** O sistema verifica a movimentação por centro de custo de todos os funcionários, desde que o código do centro de custo esteja dentro da quebra informada ou em quebra superior. Tratamento semelhante ao da quebra por seção.

**Exemplo:**  
Funcionário Centro de Custo  
00001 02  
00002 02.1  
00003 02.1.1  
00004 02.1.2  
00005 01  
00006 01.1.1  
00007 03.1  
00008 03.1.2  
   
Informando a quebra 02, o sistema irá gerar os funcionários: 00001, 00002, 00003 e 00004;  
Informando a quebra ??, o sistema irá gerar todos os funcionários;  
Informando a quebra 02.1, o sistema irá gerar os funcionários: 00002, 00003 e 00004;  
Informando a quebra 0?.1, o sistema irá gerar os funcionários: 00002, 00003, 00004, 00006, 00007 e 00008.  
Caso no rateio fixo do funcionário 00003 tenha dois centros de custos informados, 02.1.1 e 02.1, ao imprimir a folha analítica informando a quebra 0?.1, a movimentação do funcionário será agrupada.  
  
**Importante**  
O sistema sempre irá quebrar por seção dentro da quebra de centro de custo.

* **Ordenar por seção:** O sistema irá ordenar por seção quebrando o relatório por centro de custo.

**Exemplo:**  
Chapa   Centro de Custo   Seção  
--      --          
 00001           01.1               01.04  
                      01.4  
   
 00002           01.4               01.05  
                      01.5  
               
 00003           02.1               03.01  
                      04.3  
   
 00004           01.4               03.01  
                      01.7  
   
   
 00005           01.5               02.02  
   
 00006           01.4               01.04  
                       01.7  
   
  00007           01.1               01.05  
   
  00008            02.1              01.01  
                        04.3

**Resultado:**  
           Campo Ordenar por seção : MARCADO  
           Quebra da seção:??  
   
             Ordenado  por  Seção  
             Chapa   Centro de Custo    Seção  
             --     ---         -  
             00001        01.1                 01  
             00007        01.1                 01  
             00001        01.4                 01  
             00002        01.4                 01  
             00006        01.4                 01  
   
             00002        01.5                 01  
             00006        01.7                 01  
   
             00008        02.1                 01  
             00008        04.3                 01  
   
             00005        01.5                 02  
   
             00004        01.4                 03  
             00004        01.7                 03  
   
   
             Ordenado por centro de custo  
             Chapa   Centro de Custo  Seção  
              -     ---         
             00001        01.1                 01  
             00007        01.1                 01  
             00001        01.4                 01  
             00002        01.4                 01  
             00006        01.4                 01  
   
             00004        01.4                 03  
             00002        01.5                 01  
             00005        01.5                 02  
             00006        01.7                 01  
             00004        01.7                 03  
             00008        02.1                 01  
             00003        02.1                 03  
             00008        04.3                 01  
             00003        04.3                 03

**Importante**  
Para geração da Folha Analítica de 13º, devido não o sistema não possuir um relatório padrão especifico, poderá utilizar-se dá folha analítica padrão, porém selecionando apenas as bases de 13º.   
  
**Saiba Mais**  
[RH - RM - FOP - Folha Analítica: Parametrização de Fórmulas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015423792-RH-RM-FOP-Folha-Anal%C3%ADtica-Parametriza%C3%A7%C3%A3o-de-F%C3%B3rmulas)

[Considerar dados do histórico de funcionário ao gerar Folha Analítica na competência atual](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719263&draft=true)
