---
article_id: 9608739739415
category: RH - Leitura e Apontamento
content_hash: 63610ff955eb52ff5dd5c93de08babc1c21a284707377a00eab9719ecfd2aeb5
fetched_at: '2026-06-28T22:44:45.966707+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Leitura de Marcações de acordo com a Portaria 671
type: support-article
updated_at: '2026-04-10T14:47:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9608739739415-RH-Linha-Protheus-PON-Leitura-de-Marca%C3%A7%C3%B5es-de-acordo-com-a-Portaria-671
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19437474706071) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Leitura de Marcações de acordo com a Portaria 671?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A **Portaria nº 671/2021** do Ministério do Trabalho e Emprego modernizou e unificou as regras de controle de jornada e ponto eletrônico, substituindo as **Portarias nº 1510 e 373**. Ela estabelece diretrizes para os sistemas **REP-P (Programa), REP-C (relógio físico/biométrico) e REP-A (alternativo)**, que passam a utilizar o **CPF** como documento obrigatório, permitindo o registro de ponto mesmo por funcionários sem **PIS.**  
  
Segue detalhes do modelo de cada **TIPO REP**:  
-> **REP A** - se tratam dos **REPs alternativos** que permitem o registro das marcações através de ***Apps*** ou ***Softwares*** em **celulares, tablets e notebooks**. Para esta modalidade de **REP**, **não são emitidos** os arquivos fiscais **AFD** e **AEJ,** e é necessária **formalização em Acordo Coletivo de Trabalho**;  
-> **REP C** - se tratam dos **REPs físicos** que tem o registro de ponto por **biometria**;  
-> **REP P** - também se tratam dos **REPs alternativos** que permitem o registro das marcações através de ***Apps*** ou ***Softwares*** em **celulares, tablets e notebooks**. Para esta modalidade de **REP**, é necessário **registro no INPI** (Instituto Nacional de Propriedade Industrial) e **certificação digital ICP**, portanto, **não é necessária formalização em Acordo Coletivo de Trabalho**. Este tipo de **REP** emite os arquivos fiscais **AFD** e **AEJ**.  
  
Para estes três tipos de **REPs**, o ***layout*** do arquivo será tratado através do **CPF completo do funcionário + espaço.**  
  
Nos casos dos **REPs** de tipo **A** e **C**, o ***layout*** é **exatamente o mesmo**, podendo ser de acordo com os exemplos abaixo:  
  
**> CPF + Espaço:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9609579330327)  
  
**> 0 + CPF:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19437489388823)  
  
Para o **REP P**, o ***layout*** será conforme exemplo abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9609679678231)  
  
Além dos relógios citados, temos também os **REPs antigos, homologados pelas antigas portaria 1510 e 373**. Estes equipamentos ficaram divididos em **duas categorias** com a chegada da nova Portaria:  
**-> REPs que sofreram atualização no equipamento para atender novos layouts de acordo com a portaria 671** = nestes casos, a leitura dos dados será feita através do **dígito 9 + CPF completo do funcionário** ou **dígito 8 + 10 primeiras posições do CPF do funcionário + dígito verificador** (que é calculado pelo equipamento através do número do PIS do funcionário);  
**-> REPs que não sofreram atualização no equipamento** = nestes casos, a leitura **permanece da mesma forma**, ou seja, através do **dígito 0 + PIS completo do funcionário ou PIS completo do funcionário + espaço**.  
  
O ***layout*** para ambos casos **permanece basicamente o mesmo** já utilizado, a única diferença é que no primeiro cenário, será usado o CPF e no segundo, o PIS.  
  
O ***layout*** ficará desta forma quando for utilizado o **dígito 9 + CPF completo do funcionário**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9609784572055)  
  
E desta forma, quando for utilizado o **dígito 8 + 10 primeiras posições do CPF + dígito verificador**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9609825889687)  
  
Já para **REPs** que **não sofreram atualização**, o ***layout*** **permanece o mesmo já utilizado**, ou seja: **dígito 0 + PIS ou PIS + espaço**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9609875025431)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9609877765399)  
  
O ***layout*** detalhado pode ser consultado [aqui.](https://in.gov.br/en/web/dou/-/portaria-359094139)  
  
No Protheus, o cadastro dos **REPs** deverá seguir as regras abaixo:  
**-> REPs adquiridos recentemente e já homologados pela nova Portaria 671**, no campo **"Tipo do REP"** deverá ser selecionada a opção **correspondente ao tipo do REP**, ou seja: **A, C ou P**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35471394907031)  
  
**-> REPs antigos, homologados pelas portarias 1510 e 373 que tenham ou não sofrido atualização no equipamento**, deve ser selecionada a **opção 1510 ou manter o campo em branco**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35471426394007)  
  
Na tabela **RFE**, foram **criados campos** para tratamento dos dados presentes nos novos **AFDs**, ou seja: **CPF, códigos CRC, HASH e etc**:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9610249893911)  
  
É extremamente importante estar com o pacote de [**Expedição Continua Acumulado de RH**](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO) aplicado no ambiente, bem como processar o UPDDISTR para atualização do dicionário, ou seja, criação do campo **"Tipo do REP"** na rotina de Cadastro de Relógios + novos campos da tabela RFE.  
  
**Saiba mais:**  
[Leitura das Marcações conforme Portaria 671](https://tdn.totvs.com/pages/releaseview.action?pageId=684339539)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
