---
article_id: 360031198574
category: eSocial - Cadastros
content_hash: 1f7f6af0fb16f51ffe9fb4d7011e21316b89d19eac4f9fc8709ec34a2e4ff2f2
fetched_at: '2026-06-28T22:47:14.471208+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Código de cálculo 398 - Base de Abono Férias Envelope
type: support-article
updated_at: '2024-06-28T19:49:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031198574-RH-RM-FOP-eSocial-C%C3%B3digo-de-c%C3%A1lculo-398-Base-de-Abono-F%C3%A9rias-Envelope
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24512759779351) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Para que serve o código de cálculo **398 - Base de Abono Férias Envelope**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da 12.1.23  
  
**Solução**A criação do código de cálculo **398 - Base de Abono Férias Envelope** se fez necessário, devido o recibo de férias e o envelope de pagamento utilizarem os mesmos eventos de **Abono de Férias**, **1/3 de Abono de Férias** e **Média de Abono de Férias**. Com isso, ao gerar o evento **S-1210** as verbas eram levadas em duplicidade, pois as verbas eram enviada no **S-1210** (tipo de pagamento **7-Recibo de férias**)e também no **S-1200**, fazendo com que a incidência de **IRRF de Abono** (**75-IRRF de Abono**)ficasse duplicada no eSocial.

Para que o sistema crie o novo código de cálculo na tabela dinâmica (398-Base de Abono Férias Envelope), recalcule o movimento para um ou mais funcionários. Após, cadastre o código de cálculo em **Administração de Pessoal | Eventos**.

Após a criação do evento, ao lançar as férias o evento de código de cálculo **398-Base de Abono Férias Envelope** será visualizado no envelope do funcionário, conforme exemplo abaixo:

![image2019-2-20_11-28-16.png](http://tdn.totvs.com/download/attachments/458769352/image2019-2-20_11-28-16.png?version=1&modificationDate=1550672916200&api=v2)

**Importante**  
Caso existam funcionários que tenham férias lançadas antes da criação do evento com código de cálculo **398-Base de Abono Férias Envelope,** o evento deverá ser inserido manualmente na movimentação destes funcionários e em seguida realizar recálculo.  
  
**Saiba mais**  
Acesse [Para que serve o código de cálculo 398 - Base de Abono Férias Envelope?](http://tdn.totvs.com/pages/releaseview.action?pageId=458769352) para mais informações e exemplos.
