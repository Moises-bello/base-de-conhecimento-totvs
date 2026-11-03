---
article_id: 11821936684183
category: Financeiro
content_hash: 87536ecdd93d7155adb658265b78139c6f03cc8f530aec19d5e68fec203a998d
fetched_at: '2026-06-28T22:38:03.402079+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA090 - Cadastrar
  Taxas de Moeda automaticamente via Schedule FINXTAXA
type: support-article
updated_at: '2026-03-25T19:35:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11821936684183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA090-Cadastrar-Taxas-de-Moeda-automaticamente-via-Schedule-FINXTAXA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24672948700055) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como efetuar o cadastro de taxas de moedas automaticamente via JOB do Schedule

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Foi disponibilizado o JOB **FINXTAXA,** que efetua a atualização das taxas de moedas automaticamente para as moedas padrões e novas moedas cadastradas. 

Para popular os dados de taxas das moedas automaticamente, deve inicialmente cadastrar o JOB na rotina **CFGA010 - Schedule via módulo Configurador.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24672980142871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24672980147095)

Nos parâmetros da rotina, serão definidos os dias retroativos em que serão populados os dados das taxas de moeda. No exemplo abaixo, deixamos 365 dias, que serão atualizados 365 dias D-1 anterior a data de execução do JOB.

Período: 365 dias   
**Exemplo 1 :** data de execução 20/01/2023  
Irá atualizar Data de 19/01/2022 até 19/01/2023  
No próximo dia 21/01/2023, será somente atualizada a taxa do dia 20/01/2023

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24672948726423)

Para definir quais moedas serão atualizadas e qual código BACEN será utilizado, devemos inicialmente verificar no site do [SGS - Sistema Gerenciador de Séries Temporais](https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries) e verificar o código da série Bacen.

**Exemplo 2: DÓLAR** - código da série Bacen = 1  
  
![mceclip2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11821795961751)

Após localizar o código da série Bacen, deve criar um parâmetro em que será informado o código da série.  
  
**Importante**

A tabela **SM2** não possui o campo filial. Caso o job seja configurado para execução em mais de uma filial, é recomendado que o parâmetro **MV\_MOEBCX**, seja criado com uma filial.

Assim, a atualização da taxa da moeda não será solicitada para cada filial de execução do job.

Para a atualização de taxa de moedas na tabela **SM2,** é necessário criar e configurar o parâmetro **MV\_MOEBCX, em que** o **X**deve ser substituído pelo número da moeda desejada.

O seu conteúdo deve ser o código da série do Bacen;

**Exemplo de configuração para Série**: - Taxa **de câmbio - Livre - Dólar americano (venda) - Diário**

| FILIAL | 01 |
| --- | --- |
| Parâmetro | MV\_MOEBC2 |
| Tipo | Caractere |
| Descrição | Código da Série Bacen para a moeda 2 do sistema. |
| Conteúdo | 1 |

**MV\_MOEBC2**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11821853235863)  
  
Após o agendamento via *Schedule* ser processado, verifique na rotina **MATA090** se as taxas foram cadastradas.   
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11821919338391)

* Data para as moedas

**Data do BACEN**: Considera a data recebida pelo serviço da **BACEN**para gravar as taxas.

**Próx. dia útil:** considera o próximo dia útil da data recebida pelo serviço da **BACEN** para gravar as taxas.

* Data para os índices

**Data do BACEN**: Considera a data recebida pelo serviço da **BACEN**para gravar os índices.

**Próx. dia útil:** Considera o próximo dia útil da data recebida pelo serviço da **BACEN** para gravar os índices.

Importante!

Quando os parâmetros da rotina Data para os índices  ou Data para as moedas estiverem com conteúdo igual a **Prox. dia útil,** o valor será replicado para os dias não uteis dentro do período. Exemplo:

* DataBase 11/04/2022
* Cadastrar um índice financeiro conforme o tópico - [Índices Financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=680255528#Jobatualiza%C3%A7%C3%A3odetaxasBACENFINXTAXA-05.%C3%8DNDICESFINANCEIROS)
* Parâmetros da rotina  
  + Atualiza moeda?  = Não
  + Período em dias ? = 3
  + Data para as moedas ? = Prox. dia útil
  + Data para os índices? = Prox. dia útil
* Serão retornados pela API os dias 08/04/2022 e 11/04/2022
* O valor do dia 08/04 será replicado para os dias 09, 10 e 11
* O valor do dia 11/04 será jogado para o dia 12, conforme regra do parâmetro
* No exemplo acima, a data só será alterada para o dia 12 caso exista taxa da moeda cadastrada no dia 11, já que a adição da nova taxa depende da existência da taxa do dia anterior.

**Saiba mais**  
[Job atualização de taxas BACEN - FINXTAXA](https://tdn.totvs.com/pages/viewpage.action?pageId=680255528)
