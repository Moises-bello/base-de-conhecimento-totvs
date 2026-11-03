---
article_id: 38849877867927
category: esocial - Periódicos
content_hash: f25c0e4cd439875b0b6421ea12bc5c06cde027ba67eaf431b10c27dc99ad1b92
fetched_at: '2026-06-28T22:47:09.179995+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Código De Cálculo 492 - Base Excedente FGTS 13º a
  Compensar no FGTS Folha
type: support-article
updated_at: '2026-06-15T13:11:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38849877867927-RH-RM-FOP-eSocial-C%C3%B3digo-De-C%C3%A1lculo-492-Base-Excedente-FGTS-13%C2%BA-a-Compensar-no-FGTS-Folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38849846978711) Tempo aproximado para leitura: **00:00:20 min**  
  
**Ocorrência**  
No cálculo da **rescisão de funcionário que recebeu adiantamento de 13º salário**, pode ocorrer situação em que o **valor do adiantamento seja maior que o valor do 13º proporcional calculado na rescisão**, gerando dúvidas sobre o ajuste da **base de FGTS** e sobre a utilização do **Código de Cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Essa situação ocorre quando **o FGTS já foi recolhido sobre o adiantamento do 13º salário em valor superior ao que deveria ser considerado na rescisão**.

Nesse cenário, o sistema precisa **estornar o valor excedente da base de FGTS**, registrando essa diferença no **Código de Cálculo 492**, para que o valor seja compensado corretamente no cálculo do FGTS da folha.

**Solução**  
O sistema realiza automaticamente o controle do excedente através do **Código de Cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha**. Para entendimento do funcionamento, considere o exemplo abaixo.

Exemplo de utilização:

Funcionário recebeu **1ª parcela do 13º salário em fevereiro** e foi **demitido em abril**.

![](https://tdn.totvs.com.br/download/attachments/1043712337/image-2026-2-20_9-19-4.png?version=1&modificationDate=1771589947153&api=v2&effects=border-simple,shadow-kn)![](https://tdn.totvs.com.br/download/attachments/1043712337/image-2026-2-20_9-23-13.png?version=1&modificationDate=1771590195163&api=v2&effects=border-simple,shadow-kn)

No cálculo da rescisão com data de demissão **30/04**, temos:

* **R$ 1.064,27** – Provento de 13º salário proporcional *(codIncFGTS = 12)*
* **R$ 1.596,40** – Desconto da 1ª parcela do 13º *(codIncFGTS = 12)*
* **R$ 3.192,80** – Provento de saldo de salário *(codIncFGTS = 11)*
* **R$ 532,13** – Base de cálculo de FGTS *(codIncFGTS = 11 | Tipo 4 – Dedutora)* – gerada pela verba com **CC 492**

Resultado das bases

* **Base de FGTS de 13º salário:**  
  R$ 0,00  
  *(R$ 1.064,27 − R$ 1.596,40)*
* **Base de FGTS da folha:**  
  R$ 2.660,67  
  *(R$ 3.192,80 − R$ 532,13)*

![](https://tdn.totvs.com.br/download/attachments/1043712337/image-2026-2-20_9-38-19.png?version=1&modificationDate=1771591101637&api=v2)

Nesse cenário, o **Código de Cálculo 26 - FGTS Quitação** será calculado **considerando o desconto da verba com Código de Cálculo 492**, que representa a **base excedente do FGTS do 13º a ser compensada no FGTS da folha**.

![](https://tdn.totvs.com.br/download/attachments/1043712337/image-2026-2-20_9-28-43.png?version=1&modificationDate=1771590525377&api=v2&effects=border-simple,shadow-kn)

Para mais detalhes sobre a compensação do FGTS do 13º salário, consulte:

* [FGTS Digital - Compensação do valor pago a título de 13º Maior do que a rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=877870673)
* [Nota Orientativa nº 11/2025 - Leiaute S-1.3 - FGTS DIGITAL](https://tdn.totvs.com/pages/releaseview.action?pageId=1024335823)

[Código De Cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha](https://tdn.totvs.com.br/pages/releaseview.action?pageId=1043712337)

Tabelas utilizadas

* **PFPERFF**
* **PFFINANC**
