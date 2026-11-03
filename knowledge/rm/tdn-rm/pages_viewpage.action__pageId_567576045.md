---
content_hash: e0c7136dddf93daf4cb807e783884d59445f743f2ce1dbaa07b7a280fa18b883
fetched_at: '2026-06-29T00:10:51.373633+00:00'
page_id: '567576045'
product: rm
source: tdn-rm
title: Valida Função de Prestador Incompatível
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=567576045
version: 11
---

itensVisão Geral

## **01. VISÃO GERAL**

Esta validação ocorre entre 2 honorários dentro da mesma parcial e do mesmo prestador.  
Cada honorário é validado com os demais, considerando para isso o primeiro honorário como A e o segundo como B

Esta validação irá bloquear o encerramento da conta se:

* O prestador do honorário A for diferente do prestador pricipal da parcial
* O código do honorário A estar dentro da faixa de cirurgia
* A classe do prestador A ser diferente de Cooperativa de Médicos (classe  3)
* A função do prestador no honorário A não pode ser compatível com a função do mesmo prestador no honorário B

### **EXEMPLO**

Prestador principal: João

Prestador A: Marcos, Honorário de cirurgia, **função Pediatra**

Prestador B: Marcos, Honorário de cirurgia. **função Cirurgião**

Neste exemplo, o prestador Marcos possui uma função incompatível.
