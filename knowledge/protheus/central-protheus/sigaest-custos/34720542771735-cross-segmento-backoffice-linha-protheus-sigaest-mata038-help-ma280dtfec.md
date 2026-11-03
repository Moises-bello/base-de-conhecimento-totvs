---
article_id: 34720542771735
category: SIGAEST - CUSTOS
content_hash: 2344263c0b67b481a46c26a28386746e08134ce05f1a2bf4d007f5efc59fba90
fetched_at: '2026-06-28T22:39:02.028259+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - HELP MA280DTFEC
type: support-article
updated_at: '2026-06-09T15:44:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34720542771735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-HELP-MA280DTFEC
---

Durante o fechamento da jornada no TOTVS Protheus, o erro HELP MA280DTFEC ocorre na última etapa ao tentar virar saldos para a tabela SB9, geralmente por data conflitante no parâmetro MV\_ULMES ou manipulação indevida. A solução requer análise técnica, ajuste in loco dos registros SB9 e atualização correta do parâmetro MV\_ULMES para cada filial. Caso não haja manipulação, recomenda-se abortar o fechamento e revisar logs para manutenção do status do processamento.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34720527929751) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Durante o processamento da jornada de fechamento, ocorre o **HELP MA280DTFEC** ja ultima etapa da jornada, a etapa que vai virar os saldos para SB9, oque fazer?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34720930730647)  
Documentação destinada ao time TECNICO (TI) do cliente.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Apartir da Release 12.1.33.  
  
**Causa**  
Ja existe uma data gravada com a qual você esta tentando virar os saldos na tabela SB9, isso normalmente ocorre devido a manipulação indevida de registros na SB9 ou parametro MV\_ULMES, Ou se o parametro MV\_ULMES, esteja configurado de forma exclusiva para cada FILIAL, caso existe um parametro compartilhado, cujo a data estava diferente do ultimo fechamento gravado, isso pode ter gerado o impacto na ultima etapa, a sugestão aqui é 1 parametro para cada filial nesse contexto.  
  
**Solução**  
**Requer uma analise tecnica.**

Primeiro ponto, sempre certificar que esteja nas ultimas atualizações:

[- Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
- [Smartclient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/search/searchAll) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)  
- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)  
- [Central de Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

Aqui estamos representando o problema, **cujo foi feita alteração indevida no parametro MV\_ULMES de forma proposital**, onde ja possuiamos o fechamento gravado em **20250731**, e propositalmente, configuramos o parametro **MV\_ULMES** com data de **20270701** ou seja, menor que a data de fechamento.

Ao iniciarmos o processamento, e chegarmos ao final da virada de saldos, sera apresentado o HELP em questão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34720930731287)

Abaixo do HELP tera o botão "**Corrigir Fechamento**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34720963317399)

Quando voce aciona esse botão sera apresentado a seguinte tela:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34720963318295)

Ou seja, houve algum comportamento não esperado pelo sistema, **e devera ser ajustado in loco**, pois a validação desse HELP é verificar a gravação da SB9 com a data a qual você quer realizar o fechamento.

Este help está relacionado a alguma data posterior a data de fechamento ou bloqueio, que você está tentando processar. A mensagem é exibida porque o Protheus está tentado realizar a Virada de Saldos com a mesma data que **já está gravada nas tabelas SB9, SBJ e SBK e/ou no parâmetro MV\_ULMES.**

**Isso geralmente ocorre,** **devido a manipulação indevida no parametro MV\_ULMES****, que não deve ser feita, pois esse parâmetro é "Exclusivo" para o Fechamento, ou caso o ambiente esteja desatualizado, em decorrências de queda de conexão ou serviços, a jornada pode já ter gravado os dados nas tabelas físicas, mas não ter atualizado o status das tabelas de log D3X, D3Y e D3W.**

Dessa forma, certifique-se da existencia de registros na tabela SB9, para a filial em questão que aponta o erro, da existencia de dados ja gravados com a data do periodo cujo você esta tentando virar os saldos, **e ajuste IN LOCO se necessario.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34720963322647)

### **Observações:**

**Não foi efetuado manipulação no SB9 ou parametro MV\_ULMES, mas mesmo assim o HELP ocorre?**

Se acaso você tenha certeza de que não houve manipulação de dados, e o processo de fechamento por ventura, gravou os saldos na SB9 e atualizou o parametro MV\_ULMES devidamente para esse periodo que esta efetuando o calculo, mas por algum motivo esteja apresentado a inconsistencia no final do processamento, e ja tenha gravado dados na SB9, sugerimos que seja abortado o fechamento com erro em tela.

**Em BASE TESTE/HOMOLOGAÇÃO valide o seguinte:**

* Certifique que o parametro **MV\_ULMES** esteja devidamente com a data gravada da **ultima SB9 da filial**
* Consulte o arquivo **D3Y/D3W** do log de processamento, onde o log com o HELP vai estar da seguinte forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34721269236759)

Solicite ao seu TIME de TI, a manutenção do log com **D3Y\_STATUS = P** onde exista o registro no log **D3W** cujo campo **D3X/D3Y\_IDEXEC** seja o mesmo apresentado do arquivo D3Y. Devera efetuar a manutenção do registro,

exemplo:

**OBS:** Essa é uma manutenção no **LOG** de processamento que se encontra com HELP, onde foi constatado que não existiu algum tipo de "manipulação", e essa é a alternativa para que o log não fique na tela com STATUS de processamento, **não é feito nenhum tipo de AJUSTE de DADOS de saldos.**

![manutencaolog.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/34721285472151)

**Não possuimos um time de TI para executar essa ação, e todo o processo foi feito no padrão:**

Se acaso você tenha certeza de que não houve manipulação de dados, e o processo de fechamento por ventura, gravou os saldos na SB9 e atualizou o parametro **MV\_ULMES** devidamente para esse periodo que esta efetuando o calculo, mas por algum motivo esteja apresentado a inconsistencia no final do processamento, ou esteja em aberto, e ja tenha gravado dados na SB9,

Verificar em suas tabelas **SB9, SBJ e SBK** se possui algum registro com data igual ou posterior do fechamento em questão.

**Por exemplo:** fazer uma consulta em seu banco de dados conforme o exemplo abaixo:  
***➣ Tabela SB9**  - SELECT MAX(B9\_DATA) FROM SB9T10 WHERE D\_E\_L\_E\_T\_= '*  
Assim, irá retornar o valor maior do campo B9\_DATA que pode coincidir com a data que esteja tentando fazer o fechamento.

**➣*****Tabela SBJ -** SELECT MAX(BJ\_DATA) FROM SBJT10 WHERE D\_E\_L\_E\_T\_= '*  
Retornará o valor maior do campo BJ\_DATA que pode coincidir com a data que esteja tentando fazer o fechamento.

***➣ Tabela SBK*** - *SELECT MAX(BK\_DATA) FROM SBKT10 WHERE D\_E\_L\_E\_T\_= '*  
Pois irá retornar o valor maior do campo BK\_DATA que pode coincidir com a data que esteja tentando fazer o fechamento.

Caso haja o diagnóstico de que realmente existem registros nas tabelas de Saldos Iniciais com data igual ou posterior à data ao qual está precisando fazer a Virada de Saldos, é recomendável uma análise interna para melhor entendimento (se já houve de fato uma virada de saldos), e se houve, se foi de forma indevida, avaliar a possibilidade de reabertura do período de estoque, para isso é necessário o acompanhamento de um analista in loco, ou seu time de T.I, para ajustes devidos nas tabelas de logs D3X,D3Y,D3W no parametro MV\_ULMES e dados da SB9/SBJ/SBK.

**QUANDO OS DADOS FORAM GRAVADOS NAS TABELAS SB9, SBJ e SBK MAS A ROTINA FICA EM PROCESSAMENTO:**  
Atualize o parametro MV\_ULMES para DATA DO B9 dessa filial que foi fechada, caso ele não esteja atualizado com a ultima data da SB9, pois ja consta a SB9 pois se ja existe SB9 então o fechamento foi realizado  
  
"No arquivo log D3Y, atualize os campos da ultima sessão em aberto desse fechamento para:   
D3Y\_POSITI para T  
D3Y\_DATAFN para a data do fechamento em questão que existe na SB9  
D3Y\_STATUS para FN  
"  
  
Reinicie os serviços (appserver)  
Acesse novamente a rotina acompanha custos, e valide se foi gravado como concluido.

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)
