---
article_id: 360059269873
category: MDT - Atendimento Médico
content_hash: 01a1548ee8308da98dae3e007a98bfad5666a5b6b5443dfffeffb63419506524
fetched_at: '2026-06-28T22:44:21.436772+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Para que server o relatório de Atestado Clínico
  (MDTR710) e como gerar
type: support-article
updated_at: '2025-07-29T17:09:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059269873-RH-Linha-Protheus-MDT-Para-que-server-o-relat%C3%B3rio-de-Atestado-Cl%C3%ADnico-MDTR710-e-como-gerar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27598074339607) T**empo aproximado para leitura: 00:01:00 min**Dúvida**Para que server o relatório de Atestado Clínico (MDTR710) e como gerar?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**  
Essa rotina permite a emissão do relatório de Atestados clínicos emitidos. Estes atestados podem ser emitidos pelo médico da empresa, como pelos médicos externos. Apresentando todos os funcionários que receberam atestados, bem como a quantidade de dias de afastamento, total de horas e CID relacionada ao atestado.   
  
Para gerar o relatório acesse no modulo **SIGAMDT (35)** o caminho: atualizações - relatórios - atendimento medico - **Atestado Clínico** (MDTR710).  
  
Para esse relatório existem alguns parâmetros que alteram a forma com que os dados são gerados.  
  
Parâmetro **MV\_NG2TUAT**: Para que quando houver um turno cadastrado e os horários forem definidos na rotina de Tab. Horário Padrão(**PONA080**) seja considerado na impressão do atestado clínico, opções:  
  
**1** = Tempo de trabalho perdido conforme o turno   
**2** = Tempo total entre o início e o fim do atestado.  
Exemplos:  
**1.** Com turno cadastrado na rotina de Tab. Horário Padrão (**PONA080**):  
**Turno:** 22:00h às 2:00h e 04:00h às 08:00h  
Conteúdo do Parâmetro: **1**

* **Atestado:** De 20/12/2012às 22:00hAté21/12/2012às 08:00h  
  Impressão: Imprime o atestado como Total de dias igual a **1 (um)** dia.
* **Atestado:** De 22/12/2012 às 22:00hAté23/12/2012às 07:00h  
  Impressão: Imprime o atestado como Total de dias igual a **0 (zero)** dias.

**2.** Com turno cadastrado na rotina de Tab. Horário Padrão (**PONA080**):

**Turno:** 22:00h às 2:00h e 04:00h às 08:00h

Conteúdo do Parâmetro: **2**

* **Atestado:** De 20/12/2012 às 22:00hAté21/12/2012 às 08:00h  
  Impressão: Imprime o atestado como Total de dias igual a **2 (dois)** dias.
* **Atestado:** De 22/12/2012 às 22:00hAté23/12/2012 às 07:00h  
  Impressão: Imprime o atestado como Total de dias igual a **2 (dois)** dias.

Parâmetro  **MV\_NG2HRAT**: indica se na impressão do atestado clínico devem ser consideradas horas ou apenas dias, de acordo com a configuração das seguintes opções:  
  
**1** = **Horas**: apresenta as horas e os dias.  
**2** = **Dias**: exibe apenas os dias.  
  
**Observação**  
Para alterar o conteúdo dos parâmetros acesse no modulo **SIGACFG** o caminho: ambiente > cadastro > parâmetros.  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[MP - MDT - Integração do Atestado Médico com o Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025162074-MP-MDT-Integra%C3%A7%C3%A3o-do-Atestado-M%C3%A9dico-com-o-Ponto-Eletr%C3%B4nico?source=search)
