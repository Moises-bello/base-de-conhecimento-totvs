---
content_hash: 47876fafeb4270dbf22505d5e184bbeeefaf4c6f708ae71ac5f9d52f69c65185
fetched_at: '2026-06-29T00:10:15.241326+00:00'
page_id: '463821314'
product: rm
source: tdn-rm
title: Código de cálculo 398- Base de Abono Férias Envelope
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463821314
version: 15
---

Base de cálculo do tipo valor, sem incidências. Esse código de cálculo será utilizado no lançamento de férias.

Serão considerados para o código de cálculo 398-Base de Abono de Ferias, os eventos do envelope de pagamento com códigos de cálculos relacionados a abono de férias e que NÃO tenham incidência ou estorno de IRRF de Férias. Eventos de abono que tenham incidência ou estorno de IRRF de férias serão considerados no código de calculo 381.

**Atenção:**

A criação desse código de cálculo se fez necessário, devido o recibo de férias e o envelope de pagamento utilizarem os mesmos eventos de Abono de Férias, 1/3 de Abono de Férias e Média de Abono de Férias.

Com isso ao gerar o evento S-1210 as verbas eram levadas em duplicidade, pois as verbas eram enviada no S-1210 (tipo de pagamento **7-Recibo de férias)**  e também no S-1200, fazendo com que a incidência de IRRF de Abono (****75-IRRF de Abono)****ficasse duplicada no eSocial.

Este código de cálculo faz o estorno da base IRRF de Abono referente aos eventos enviados no S-1200, com isso a base não ficará mais duplicada no eSocial.

Maiores informações veja TDN:   [http://tdn.totvs.com/pages/releaseview.action?pageId=458769352](https://www.google.com/url?q=http://tdn.totvs.com/pages/releaseview.action?pageId%3D458769352&sa=D&source=hangouts&ust=1552039885407000&usg=AFQjCNE-7_UepIuWP2sMcEF4BLTFvgJHaA)

---

Códigos de Cálculo
