---
article_id: 360015658231
category: RH - Férias
content_hash: cb15fcca2d4482f0990bed0ed66827535a3c3296519dc11ca54106337ffb559c
fetched_at: '2026-06-28T22:43:58.053871+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular férias na versão 12
type: support-article
updated_at: '2025-09-12T18:13:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015658231-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-na-vers%C3%A3o-12
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24308815121047) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como calcular férias através da rotina GPEM030?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
1. Verifique se o **Cadastro de Períodos** está corretamente cadastrado com o **Roteiro de Férias** para o mês que se iniciará e terminará o gozo das férias e **Ativo** para cálculo (campo **Per. Selec.** = Sim).

![](http://tdn.totvs.com/download/attachments/240299713/image2016-6-21%2014%3A15%3A23.png?version=1&modificationDate=1466526723000&api=v2)  
  
2. Configure as **verbas de mês seguinte** conforme documentação abaixo caso seja um cálculo de férias partidas: [Verbas Mês Seguinte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027941171-MP-GPE-Como-configurar-verbas-de-f%C3%A9rias-m%C3%AAs-seguinte-para-calculo-na-folha-de-pagamento)  
  
3. Verifique se a rotina **Controle de** **Dias de Direito** contém a informação de **períodos aquisitivos,** dias de **referência** preenchido, **dias vencidos** ou **proporcionais** disponíveis para cálculo e se está informada a verba com **ID 0072**;

![](http://tdn.totvs.com/download/attachments/240299713/image2016-6-21%2014%3A16%3A52.png?version=1&modificationDate=1466526724000&api=v2)

![](http://tdn.totvs.com/download/attachments/240299713/image2016-6-21%2014%3A23%3A49.png?version=1&modificationDate=1466526725000&api=v2)

4. Acesse a rotina de **Férias** através do menu **Miscelânea > Cálculos > Férias**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10657352019735)**

5. Selecione o funcionário e clique em **Cálculo,** informe **campos obrigatórios** apresentados no cabeçalho;

![](http://tdn.totvs.com/download/attachments/240299713/image2016-6-21%2014%3A28%3A56.png?version=1&modificationDate=1466526727000&api=v2)

6. Clique em **Outras Ações > Calcular** ou utilize atalho **F6** para que o calculo seja executado.

![](http://tdn.totvs.com/download/attachments/240299713/image2016-6-21%2014%3A29%3A38.png?version=1&modificationDate=1466526728000&api=v2)

**Observações**:  
Caso tenha necessidade de realizar lançamento de verbas manualmente, clique em **Outras Ações** e em **Lançamentos**.

**Saiba Mais**[RH - Linha Protheus - GPE - Parâmetro MV\_REFTRAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050966774-RH-Linha-Protheus-GPE-Par%C3%A2metro-MV-REFTRAB-?source=search)[RH - Linha Protheus - GPE - Como calcular férias programadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004091821-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-programadas?source=search)  
[RH - Linha Protheus - GPE - Recalculo de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420404618903-RH-Linha-Protheus-GPE-Recalculo-de-F%C3%A9rias-?source=search)  
[RH - Linha Protheus - GPE - Impressão Relatório de Férias Calculadas - GPER550](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035142854-RH-Linha-Protheus-GPE-Impress%C3%A3o-Relat%C3%B3rio-de-F%C3%A9rias-Calculadas-GPER550-?source=search)  
[RH - Linha Protheus - GPE - Como calcular férias coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000101721-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-coletivas?source=search)  
[RH - Linha Protheus - GPE - Ao calcular férias, Sistema traz período aquisitivo ou dias de férias incorreto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017554792-RH-Linha-Protheus-GPE-Ao-calcular-f%C3%A9rias-Sistema-traz-per%C3%ADodo-aquisitivo-ou-dias-de-f%C3%A9rias-incorreto?source=search)
