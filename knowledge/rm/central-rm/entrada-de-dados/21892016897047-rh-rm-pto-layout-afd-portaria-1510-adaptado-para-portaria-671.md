---
article_id: 21892016897047
category: Entrada de dados
content_hash: bdadd5f3a8b2a24c8eaec58c3144fc7d0ddbc5800fc2584383f97a41c068aae7
fetched_at: '2026-06-28T22:46:30.550017+00:00'
product: rm
section_id: 1500000835061
source: central-rm
title: RH - RM - PTO - Layout AFD portaria 1510 "adaptado" para portaria 671
type: support-article
updated_at: '2025-01-14T13:10:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21892016897047-RH-RM-PTO-Layout-AFD-portaria-1510-adaptado-para-portaria-671
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21891990501015) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Como utilizar e configurar layout AFD da portaria 1510 na portaria 671?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.2306.210, 12.1.2310.143, 12.1.2402 ou superiores.  
  
**Solução**Primeiramente, para utilização do layout AFD da portaria 1510 na portaria 671 é necessário compreender como é o layout da portaria 1510 original:

O AFD gerado originalmente na 1510 é no formato abaixo:

![LayoutPortaria1510 (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/21892016819607)

Observe que as posições 023-034 é considerado o número PIS do funcionário onde o primeiro dígito, na posição 023 é o '0' (zero), seguido do PIS do funcionário. Por esse motivo o tamanho deste campo é 12 e não apenas 11 para acolher o PIS.

Imagem exemplo de uma linha de registro da portaria 1510 considerando que o PIS seja esse:  **55555555555**  
![2024-03-07 15_00_11-Clipboard.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21892016825751)

Segue abaixo os detalhes da marcação:

000021383 NSR / 3 Tipo de Registro / 04032024 Data / 0800 Hora / **0**55555555555 PIS

A partir desta informação, foi gerado o artigo 96 da portaria 671 com as seguintes considerações:

![2024-03-07 14_43_43-Clipboard.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21892016827799)

Portanto, levando em consideração o artigo 96, segue abaixo um exemplo de uma linha de registro gerada pelo REP considerando o PIS:

![0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21892016835095)

Abaixo um exemplo de uma linha de registro gerada pelo REP para considerar o CPF, supondo que o cpf seja **666.666.666-66**:

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21892016838167)

Segue abaixo os detalhes da marcação:

000021383 NSR / 3 Tipo de Registro / 04032024 Data / 0800 Hora / **9**66666666666 Dígito '9' + CPF

Abaixo um exemplo de uma linha de registro gerada pelo REP em que os empregados não possuem PIS e o REP faz validação do PIS:   
Supondo que o CPF do funcionário seja **666.666.666-66**:

![printnovo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23077739593239)

Segue abaixo os detalhes da marcação:

000021383 NSR / 3 Tipo de Registro / 04022024 Data / 1208 Hora / **8**6666666666**3** Dígito '8' + CPF + verificador PIS.

No módulo RM Totvs Automação de Ponto, para efetuar a leitura do AFD gerado com base na 'adaptação', basta criar um layout que esteja com a opção **Utiliza layout AFD Portaria 1510/2009** selecionado:

![2024-03-07 15_41_48-TOTVS Linha RM - Serviços  Alias_ CorporeRM _ 1-TOTVS SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21892016848023)

No momento de efetuar a importação de batidas, basta selecionar o arquivo AFD (desde que este esteja em um dos formatos explicados acima) e o layout compatível para que a importação ocorra normalmente.

![2024-03-07 15_44_46-Importação de Batidas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21892016850583)

**Importante**

* **Os tipos de validação '0', '9' e '8' são definidos no software do REP. Qualquer dúvida na configuração, deverá avaliar junto ao fabricante para correta geração do arquivo AFD;**
* **O dígito verificador do PIS, com base no número CPF, para empregados que não possuem PIS e o REP faz validação do PIS (tipo '8') é gerado pelo software do REP e inserido ao AFD na posição 34 para posterior importação;**
* **O RM Totvs Automação de Ponto *somente* efetua a leitura do arquivo AFD no formato .txt gerado pelos REP's, desde que o arquivo gerado pelos REP's estejam conforme exigido pelas portarias 1.510/2009 ou 671/2021.**

**Saiba mais**Para maiores detalhes sobre a portaria 671, acesse: [**Portaria 671**](https://in.gov.br/en/web/dou/-/portaria-359094139)  
Para maiores detalhes sobre a portaria 1510/2009, acesse: **[Portaria 1510/2009](https://www.normaslegais.com.br/legislacao/portaria1510_2009.htm)  
[RH - RM - PTO - Tipos de REPs (Registros Eletrônicos de Ponto) de acordo com a Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22760840044183)**
