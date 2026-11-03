---
article_id: 34789750279191
category: eConsignado (Crédito do Trabalhador)
content_hash: 140ffa1fcd3f7e3a271364cba380c727c24317e79946ceb4b9dc44ba016bc6b5
fetched_at: '2026-06-28T22:43:07.243360+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização da provisão do eConsignado realizado
  no Adiantamento e devolvido como provento na Folha de Pagamento
type: support-article
updated_at: '2025-09-08T19:32:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34789750279191-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-da-provis%C3%A3o-do-eConsignado-realizado-no-Adiantamento-e-devolvido-como-provento-na-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34789741138455) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como é feita a contabilização referente ao valor de eConsignado provisionado no Adiantamento e devolvido na folha de pagamento como provento.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - a partir da versão 12.1.2210  
  
**Solução**  
Para fins de Contabilização do valor referente a provisão do eConsignado feito no Adiantamento e devolvido na Folha, é necessário criar uma nova verba de Base Desconto, vincular ao id de cálculo 1977![]() e não ter nenhuma incidência, conforme orientação:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34789741138583)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34789972500759)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34789972506007)  
  
Ao calcular a folha de pagamento, a verba será gerada no valor provisionado no mês, possibilitando o devido registro contábil.  
  
**Cálculo do Adiantamento**  
**Valor Provisionado**: R$ 40,40  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34789975549591)  
  
**Cálculo da Folha**  
Verba com id **1977** gerada com o **mesmo valor** provisionado no Adiantamento e devolvido na verba com id **1975.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34789972509847)  
  
**Importante**  
Referente a configuração de **lançamento padrão**, fica a critério e entendimento de cada empregador, portanto **não orientamos** quanto a este preenchimento no cadastro da verba criada e vinculada ao id 1976.  
  
  
**Saiba Mais**

[Manual de Orientação ao Empregador - Crédito Consignado do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)

[Orientações Consultoria de Segmentos Totvs - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.7.2Ovalordoabonopecuni%C3%A1riodevecomporaremunera%C3%A7%C3%A3odispon%C3%ADvelparadescontodocr%C3%A9ditodotrabalhador?)

[Manual Crédito do Trabalhador Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[eConsignado (Crédito do Trabalhador) - Dúvidas frequentes](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
