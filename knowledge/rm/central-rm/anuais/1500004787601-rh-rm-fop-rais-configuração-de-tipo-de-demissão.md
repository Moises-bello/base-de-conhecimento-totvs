---
article_id: 1500004787601
category: Anuais
content_hash: 2c4485216f3e63c085fadcae43c4f229a985a90b31de20893191f50745dafd0b
fetched_at: '2026-06-28T22:46:51.149729+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - RAIS: Configuração de Tipo de Demissão'
type: support-article
updated_at: '2025-03-14T10:03:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004787601-RH-RM-FOP-RAIS-Configura%C3%A7%C3%A3o-de-Tipo-de-Demiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida**Como configurar o tipo de demissão na RAIS por ordem judicial?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A RAIS não possui tipo de desligamento por determinação judicial. Para atender a esses tipos de desligamento, deve-se adiciona-los em uma das etapas da rotina da geração da RAIS. Acesse: **Anuais | RAIS:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5169731462935/mceclip0.png)  
  
Na etapa Configuração Tipo de Demissão, clique em incluir. Será apresentada uma tela com os seguintes campos:

* **Tipo de Demissão:** Rescisão Determinada pela Justiça;
* **Motivo Demissão:** Motivo atribuído ao funcionário na rescisão;
* **Tipo de Demissão RAIS:** Deve-se verificar as duas situações.

Para configurar o tipo de demissão na RAIS por ordem judicial, segue orientações:

* Se o tipo de demissão for por ordem judicial + funcionário ganhou a causa na justiça = ***rescisão de contrato sem justa causa.***![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006455642/mceclip6.png)
* Se o tipo de demissão for por ordem judicial + funcionário perdeu a causa na justiça = ***rescisão de contrato com justa causa.***![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006455602/mceclip5.png)

O **Motivo Demissão** deve ser combinado ao **Tipo Demissão** para que seja transmitido à RAIS o **Tipo Demissão RAIS** correspondente que desejo. Por exemplo, Se configuro o Tipo Demissão B - Rescisão Determinada pela justiça e o Motivo Demissão como 03 - Sem razão específica, defino abaixo que esta combinação deve enviar para RAIS o **Tipo Demissão RAIS 10 - Rescisão de contrato de trabalho por justa causa**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5169768159895/mceclip1.png) **Saiba mais**[RH - RM - FOP - RAIS: Versões para geração da RAIS 2022 Ano-Base 2021](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024451952)

***Informações gerais sobre a RAIS 2022*** *Foi publicado no* [*Portal da RAIS*](https://www.rais.gov.br/sitio/index.jsf) *no dia 15/03/2022 o Manual e o Leiaute relativos ao Ano Base 2021. A adequação é apenas no campo de identificação do trabalhador* ***PIS/PASEP/NIT****, passando a ser facultativo, de acordo com o Manual de Orientação da RAIS ano-base 2021. O Programa Validador da RAIS –* ***GDRAIS2022****, está disponível no portal para download, então já é possível preparar-se para a transmissão da RAIS, uma vez que* ***para a linha RM, não será necessária adequação do produto****. As versões que atenderão a rotina serão as mesmas que atenderam a DIRF 2022:*

* *12.1.32.241 ou superiores;*
* *12.1.33.178 ou superiores;*
* *12.1.34.100 ou superiores.*

*Ressaltamos que, a entrega da RAIS para os Grupos 1 e 2 já foram substituídas pelo envio mensal dos eventos de remuneração no eSocial desde 2019, e para estes grupos está bloqueado o envio através do GDRAIS.*
