---
article_id: 10390346192663
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: bb7dd0670238dbb72a3a48fecc2b312ec0e0fb3d7e9d10628517ba34e874cd4a
fetched_at: '2026-06-28T22:42:06.591359+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Controle de Retenções de PIS (Rotina FISA216) e COFINS (Rotina FISA217) '
type: support-article
updated_at: '2022-11-23T13:00:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10390346192663-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Controle-de-Reten%C3%A7%C3%B5es-de-PIS-Rotina-FISA216-e-COFINS-Rotina-FISA217
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00 min **Dúvida**Como gerar os registros **1300** e **1700** do **EFD Contribuições** pelas **Rotinas Controle de Retenções.  
Controle de Saldo de retenção de PIS (Rotina FISA216) - Tabela SFV  
Controle de Saldo de retenção de COFINS (Rotina FISA217) - Tabela SFW**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Quando não existe Nota Fiscal, para gerar valores de **PIS** e **COFINS** retidos na **Apuração do EFD Contribuições,** acesse a rotina da **Apuração do EFD Contribuições** (**FISA001**) e Inclua os valores das retenções de **PIS** e **COFINS**, através das Rotinas abaixo:  
**Controle de Saldo de retenção de PIS (Rotina FISA216) - Tabela SFV  
Controle de Saldo de retenção de COFINS (Rotina FISA217) - Tabela SFW**Para gerar os valores de retenção de **PIS** e **COFINS** na **Apuração EFD Contribuições**, através de lançamento de **Nota Fiscal**, gere um documento fiscal conforme as configurações do *link* abaixo para o cálculo de **PIS** e **COFINS** retido:  
  
[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições como gerar o registro F600, 1300 e 1700 do Sped Contribuições](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016177611-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-o-registro-F600-1300-e-1700-do-Sped-Contribui%C3%A7%C3%B5es?source=search)

Após o processamento da **Apuração do EFD Contribuições**, se os valores das **retenções de PIS e COFINS** for maior que os valores das **contribuições de PIS e COFINS** calculadas no período, sobrará **valores retidos de PIS e COFINS** para serem **utilizados em períodos futuros**, o sistema gravará automaticamente nas tabelas **Controle de retenção de PIS (Tabela SFV) e Controle de Saldo de retenção de COFINS (Tabela SFW).**

Quando em determinado mês houver apuração, logo deverá ser feita a dedução da retenção no período mais antigo que possuir valor disponível maior que zero desde que o mesmo não esteja marcado como "**1 - Sim**" no campo **Reserva Ret**, por sua vez, os valores retidos da contribuição serão gravados nas tabelas **SFV** e **SFW**, portanto, para cada período que ainda houver valor disponível será gerado um **registro 1300 para PIS retido** e um **registro 1700 para COFINS retido**, até que todo o valor disponível do período seja igual a zero.  
  
O sistema permite a **reserva de** **saldo excedente da retenção**, para que desta forma não sejam utilizados automaticamente no mês subsequente, possibilitando que sua utilização seja somente realizada via o **Pedido de Ressarcimento ou Compensação (PERD/Comp) da Receita Federal do Brasil**.  
  
Exemplo:

Geração da **Apuração EFD Contribuições (FISA001)**com saldo a ser transportado para o mês subsequente.  
Valor de R$: 500,00 a ser transportado para o próximo período:![Imagem_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389341458839)

Tela de Controle de Retenções do **PIS:**

![imagem_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389371162519)

Acrescentado no sistema os campos, **Ressarcimento, Compensação e Reserva Ret.,**tanto para a tela de **Controle do** **PIS** quanto para a tela de controle de **COFINS:**

**![imagem_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389432299415)  
Reserva Ret = Não.** Utilização integral no próximo mês.Caso não haja nenhuma alteração nos campos desta tela o valor do campo **Vl. Disp** será transportado e utilizado no mês sub-sequente para deduções.

Conforme imagem abaixo:

![image_4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389472847383)

Utilização parcial para o próximo mês, caso haja necessidade de solicitar o **ressarcimento/compensação** de saldo proveniente de **retenções de PIS/COFINS** o mesmo deverá ser feito via pedido **PER/DComp.** Para tal deverá ser gerado e enviado o arquivo do mês atual, antes do preenchimento dos campos **(Ressarcimento e (ou) Compensação)** à ser solicitado.  
  
Caso haja necessidade de solicitar **Ressarcimento** deverá se informar o valor solicitado no campo **Ressarcimento.**Caso haja necessidade de solicitar a compensação para outros impostos, deverá se informar o valor solicitado no campo **Compensação**.  
  
Caso os valores dos campos **Ressarcimento e(ou) Compensação**seja menor que o valor do campo **Vl. Disp.**e o campo **Reserva Ret.** esteja como **NÃO**, a diferença da subtração dos campos (**Vl. Disp. - Ressarcimento - Compensação)**será gerado uma linha no **Controle de Retenção** e disponibilizará o resultado para utilização na apuração do mês subsequente .

Conforme imagens abaixo:

![imagem_5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389547307031)

![imagem_6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389534122135)

**Reserva Ret = Sim**, Reserva integral, caso o campo **Reserva Ret.**esteja como **Sim,**o sistema bloqueará todo o valor do campo **Vl. Disp.** e será gerado uma linha no **Controle de Retenção**, não o disponibilizando para utilização na apuração do mês subsequente e o somará no total a ser transportado para o próximo mês.

![imagem_7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389588037271)

![imagem_8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389592377751)

![imagem9.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389633598231)

**Reserva parcial, com utilização parcial (Ressarcimento/Compensação)**, caso o campo **Reserva Ret.** esteja como **SIM** e os campos **Ressarcimento e(ou) Compensação**estejam com valores preenchidos, e seja apurado o mês subsequente será gerado uma linha no **Controle de Retenções** respectiva ao mês apurado com os valores   dos campos **(Vl. Disp. - Ressarcimento - Compensação)**idênticos ao do mês posterior, mas o valor a ser transportado para o próximo período (apuração) já vira com os valores deduzidos.

Exemplo:  500,00   -  50,00   -   100,00 = 350,00 (valor somado ao campo de saldo de retenção a transportar para o próximo período).

![imagem_10.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389692174231)

![imagem_11.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389729385111)

Liberando saldo para utilização no mês sub-sequente, caso queira utilizar um saldo **Reservado** em meses anteriores, deverá localizar o registro no **Controle de Retenção**respectivo (que contenha valor de saldo) e colocar o campo **Reserva Ret.** como **NÃO**liberando assim seu saldo para utilização no mês subsequente.

![imagem_12.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389773224343)

![imagem_13.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389774877591)

![imagem_15.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10389847535255)

Observação:   
**Leds Vermelhos : Campo Reserva Ret = Sim (Valor de Saldo bloqueado)**  
**Leds Verdes : Campo Reserva Ret = Não (Valor de Saldo disponível para utilização no mês sub-sequente).**
