---
article_id: 9611416114711
category: RH - Portaria 671
content_hash: e2cec5a1e3581813d8f258868062c199f74a67b63bdd30f060ce2e58d9818dd3
fetched_at: '2026-06-28T22:44:44.432128+00:00'
product: protheus
section_id: 32419326556951
source: central-protheus
title: RH - Linha Protheus - PON - REP de acordo com a Portaria 671
type: support-article
updated_at: '2025-12-23T14:35:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9611416114711-RH-Linha-Protheus-PON-REP-de-acordo-com-a-Portaria-671
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646176437655) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**  
Qual os tipos de REP de acordo com a Portaria 671?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A **Portaria nº 671/2021** do Ministério do Trabalho e Emprego modernizou e unificou as regras de controle de jornada e ponto eletrônico, substituindo as **Portarias nº 1510 e 373**. Ela estabelece diretrizes para os sistemas **REP-P (Programa), REP-C (relógio físico/biométrico) e REP-A (alternativo)**, que passam a utilizar o **CPF** como documento obrigatório, permitindo o registro de ponto mesmo por funcionários sem **PIS.**  
  
Com base no ***layout*** do governo, link:<https://in.gov.br/en/web/dou/-/portaria-359094139>  
Destaco as perguntas e respostas especificamente no link do Governo:  
• [Pergunta e Resposta na questão 50](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/fiscalizacao-do-trabalho/Perguntas%20e%20Respostas%20REP)  
  
**Trecho destacado:**

"Há duas possibilidades válidas de preenchimento dos campos CPF para linhas de marcações. Supondo o CPF “XXXXXXXXXXX” e o espaço reservado para o campo tenha tamanho 12(doze), temos as seguintes opções:

a) Alinhamento com zero à esquerda: “0XXXXXXXXXXX”;

b) Alinhamento com espaço à direita: “XXXXXXXXXXX ”."

Veja maiores detalhes com ***layout*** de exemplo para cada REP:  
->**REP A**- se tratam dos **REPs alternativos** que permitem o registro das marcações através de ***Apps*** ou ***Softwares*** em **celulares, tablets e notebooks**. Para esta modalidade de **REP**, **não é gerado** o arquivo fiscal **AEJ ,**e é necessária **formalização em Acordo Coletivo de Trabalho**;  
  
->**REP C**- se tratam dos **REPs físicos** que tem o registro de ponto por **biometria**;  
  
->**REP P**- também se tratam dos **REPs alternativos** que permitem o registro das marcações através de ***Apps*** ou ***Softwares*** em **celulares, tablets e notebooks**. Para esta modalidade de **REP**, é necessário **registro no INPI** (Instituto Nacional de Propriedade Industrial) e **certificação digital ICP**, portanto, **não é necessária formalização em Acordo Coletivo de Trabalho**. Este tipo de **REP** emite os arquivos fiscais **AFD** e **AEJ**.  
  
Para estes três tipos de **REPs**, o ***layout*** do arquivo será tratado através do **CPF completo do funcionário + espaço.**  
Nos casos dos **REPs** de tipo **A** e **C**, o ***layout*** é **exatamente o mesmo**, e ficou conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646176438807)  
  
Para o **REP P**, o ***layout*** será conforme exemplo abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646191742359)  
  
  
Além dos relógios citados, temos também os:   
-> **REPs antigos, homologados pelas antigas portaria 1510 e 373**. Estes equipamentos ficaram divididos em **duas categorias** com a chegada da nova Portaria 671:  
  
**-> REPs que sofreram atualização no equipamento para atender novos layouts de acordo com a portaria 671**= nestes casos, a leitura dos dados será feita através do **dígito 9 + CPF completo do funcionário** ou **dígito 8 + 10 primeiras posições do CPF do funcionário + dígito verificador** (que é calculado pelo equipamento através do número do PIS do funcionário);  
Embasamento do site do goberno:<https://in.gov.br/en/web/dou/-/portaria-359094139>  
Artigo 96:

§ 2º Com relação à geração do arquivo mencionado no § 1º, o preenchimento do campo de doze caracteres reservado ao Programa de Integração Social - PIS para inclusão de empregados nos registradores eletrônicos de ponto certificados nos termos da Portaria MTE nº 1.510, de 2009, deve ser preenchido da seguinte forma:

I - empregados que possuem PIS: colocar "0" na primeira posição do campo e o PIS completo nas próximas onze posições;

II - empregados que não possuem PIS e o REP não faz validação do PIS: colocar "9" na primeira posição e o CPF completo nas próximas onze posições; e

III - empregados que não possuem PIS e o REP faz validação do PIS: colocar "8" na primeira posição, os dez primeiros dígitos do CPF nas posições seguintes e na última posição, o dígito verificador do PIS considerando os dez primeiros dígitos do CPF.  
  
Veja maiores detalhes com ***layout***de exemplo para cada REP:  
**-> REPs que não sofreram atualização no equipamento**= nestes casos, a leitura **permanece da mesma forma e sem alterações**, ou seja, através do **dígito 0 + PIS completo do funcionário ou PIS completo do funcionário + espaço**.  
  
O ***layout*** para ambos casos **permanece basicamente o mesmo** já utilizado, a única diferença é que no primeiro cenário, será usado o CPF(seguindo o recomendado da portaria 671) e no segundo, o PIS(seguindo a portaria 1510).  
  
O ***layout*** ficará desta forma quando for utilizado o **dígito 9 + CPF completo do funcionário**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646191743895)  
  
E desta forma, quando for utilizado o **dígito 8 + 10 primeiras posições do CPF + dígito verificador**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646176442647)  
  
Já para **REPs** que **não sofreram atualização**, o ***layout*** **permanece o mesmo já utilizado**, ou seja: **dígito 0 + PIS ou PIS + espaço**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646191747735)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646191748631)  
  
**Importante:** O ***layout*** para cada tipo de REP terá um formato e isto não é determinado pela TOTVS-PROTHEUS e sim pela Portaria 671 do MTP. Como destacado no link a seguir do site do governo:  
  
**Saiba mais:**  
<https://tdn.totvs.com/display/public/ConSeg/Portaria+671+-+Leitura+do+Novo+Layout+AFD>  
[Leitura de Marcações dos Layouts da Portaria 671](https://tdn.totvs.com/pages/releaseview.action?pageId=684339539)  
[RH - Linha Protheus - PON - Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9610887359895-RH-Linha-Protheus-PON-Portaria-671?source=search)  
[RH - Linha Protheus - PON - Leitura de Marcações de acordo com a Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9608739739415-RH-Linha-Protheus-PON-Leitura-de-Marca%C3%A7%C3%B5es-de-acordo-com-a-Portaria-671?source=search)  
[RH - Linha Protheus - PON - Espelho de Ponto de acordo com a Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9324927169559-RH-Linha-Protheus-PON-Espelho-de-Ponto-de-acordo-com-a-Portaria-671?source=search)  
[RH - Linha Protheus - PON - Arquivo Eletrônico de Jornadas - AEJ - Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9326209981719-RH-Linha-Protheus-PON-Arquivo-Eletr%C3%B4nico-de-Jornadas-AEJ-Portaria-671?source=search)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
