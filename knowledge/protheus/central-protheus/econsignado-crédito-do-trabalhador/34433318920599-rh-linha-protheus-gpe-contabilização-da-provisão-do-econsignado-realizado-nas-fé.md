---
article_id: 34433318920599
category: eConsignado (Crédito do Trabalhador)
content_hash: ae43a1e9bf3ea571412fd0ac053a8cbf4a066ce04c32dbc42cbf9a882718a8af
fetched_at: '2026-06-28T22:43:07.159036+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE -  Contabilização da provisão do eConsignado realizado
  nas férias e devolvido como provento na Folha de Pagamento
type: support-article
updated_at: '2026-06-26T14:36:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34433318920599-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-da-provis%C3%A3o-do-eConsignado-realizado-nas-f%C3%A9rias-e-devolvido-como-provento-na-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34433281258135) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como é feita a contabilização referente ao valor de eConsignado provisionado nas férias e devolvido na folha de pagamento como provento.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - a partir da versão 12.1.2210  
  
**Solução**  
Para fins de Contabilização do valor referente a provisão do eConsignado feito nas férias e devolvido na Folha, é necessário **criar** uma nova verba de **Base Desconto**, vincular ao **id de cálculo** **1976**![]() e não ter nenhuma incidência, conforme orientação:  
  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34433375150359)  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34433725329559)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34433738417815)  
  
  
Ao calcular a folha de pagamento, a verba será gerada no valor provisionado no mês, possibilitando o devido registro contábil.  
  
**Cálculo das férias**  
**Valor Provisionado**: R$ 4.968,69  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34433738418967)  
  
  
**Cálculo da Folha**  
Verba com id **1976** gerada com o **mesmo valor** provisionado nas férias e devolvido na verba com id **1973.**  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34433725335063)

**Importante**  
Referente a configuração de **lançamento padrão**, fica a critério e entendimento de cada empregador, portanto **não orientamos** quanto a este preenchimento no cadastro da verba criada e vinculada ao id 1976.  
  
  
**Saiba Mais**  
[Manual do Crédito Consignado do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)  
[Orientações Consultoria de Segmentos - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.7.2Ovalordoabonopecuni%C3%A1riodevecomporaremunera%C3%A7%C3%A3odispon%C3%ADvelparadescontodocr%C3%A9ditodotrabalhador?)  
[Manual Crédito do Trabalhador Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)

![]()
