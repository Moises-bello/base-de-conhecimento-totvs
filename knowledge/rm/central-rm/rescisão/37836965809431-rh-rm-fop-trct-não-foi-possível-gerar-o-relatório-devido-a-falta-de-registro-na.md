---
article_id: 37836965809431
category: Rescisão
content_hash: 1a41fbbe9bafcb3c98e5821f06b85b8a3ce2ec2031275ed2237b1f5e735d1038
fetched_at: '2026-06-28T22:46:54.143771+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: Não foi possível gerar o relatório devido a falta de
  registro na coligada'
type: support-article
updated_at: '2026-01-22T11:54:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37836965809431-RH-RM-FOP-TRCT-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-relat%C3%B3rio-devido-a-falta-de-registro-na-coligada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37836965788951) Tempo aproximado para leitura: **00:02:09 min**  
  
**Ocorrência**  
No módulo Folha de Pagamento, ao realizar a geração do Termo de Rescisão, o sistema apresenta a seguinte mensagem de erro: **Não foi possível gerar o relatório por falta de registro na coligada.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37837482872855)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O incidente ocorre devido à competência do movimento e ao período de rescisão informados no TRCT, não corresponderem à data da rescisão.  
  
**Solução**  
Quando nos deparamos com esta situação é necessário verificar a data de demissão e o período. Efetue o procedimento abaixo para corrigir a parametrização e gerar sem erros:

1. Acesse: **Funcionários | Rescisão;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37836965795351)

 2. Verifique a data de demissão e o período em que foi realizado o lançamento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37836965795991)

3. Os campos que indicam a grade **Competência do Movimento:** Mês, Ano e Período respectivamente, deverão ser informados obrigatoriamente conforme o cadastro da rescisão que será considerado no TRCT.  
  
As datas dos campos Início e Término da grade **Período de Demissão** são obrigatórias, e determinarão um intervalo para que somente funcionários demitidos dentre o intervalo, tenham o TRCT gerado.

![Exibindo image.png](https://chat.google.com/u/3/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEWD00kOAjISjiSN9q2No3OFlvBqNULyc4DqQTon0mnERWguAD3vYiX42SwvuGa%2FfUCBg9qx%2BpoxqI8tj0QHjOIITyfy5ndjXvR3pyM8zUyN2rQk7DUB9REylUGwf%2B1EkivpNdwyv7KpXOC23HWU%2BO6Pa1LlQTdYYd4hx%2BYJmNi2dQePcGZDZJkkYUFXIsOvdKNP4kQAWqx2gVmoryoqrP4YSeNwHsW88aYet9axDZYcjWkWHIUUdhnF0b2S89C2imcga5eVLjNeIBgDrFyGqBOT1pIG%2BJACQq2Nylt3CpK12UBVlvYlnyYZsUqADIL9kwYiNR%2B60mVmlL%2B3JFWtuHfWdgGUFIXyGPixiXqWTdXyEbtmDWUJHsFkjQgqkiYJE1tOfmzFMhCIdU0Pr0RoGZNz%2BLw2MXypvBD7NvDtd5FpIL7zDLgeQh3uNnNkf70STRGE%2FbcJIq6uBLDS%2BW5SCNdSG6GKpr%2FRG19rETpePJaVbciI2%2FcpQC7%2Fh%2Bb%2B4eU7M0Rejd5S%2FxTvQsF3F7HUA7dEMNT0GF8YQJthRfqhBJLxXf%2BpvkoShUaHfrnHe4VVbQPakGH3M6t8rQTO5mBNvg%3D%3D&allow_caching=true&authuser=3&sz=w1920-h868-rw&auditContext=forDisplay)

*Exemplo:* Funcionário demitido em 12/07/2024, período 9.  
Ao parametrizar o Termo de Rescisão para geração, deve-se informar a competência do movimento como mês 07, ano 2024, período 9.  
O período de demissão deve ser definido de 01/07/2024 a 30/07/2024.

**SAIBA MAIS:**  
  
[RH - RM - FOP - TRCT: parametrização do código de rubricas em eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003040531-RH-RM-FOP-TRCT-parametriza%C3%A7%C3%A3o-do-c%C3%B3digo-de-rubricas-em-eventos)  
[RH - RM - FOP - Parametrização Folha de Pagamento - Emissão TRCT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411690878103-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-Folha-de-Pagamento-Emiss%C3%A3o-TRCT)
