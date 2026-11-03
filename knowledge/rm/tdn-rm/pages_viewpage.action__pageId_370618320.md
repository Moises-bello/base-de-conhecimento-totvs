---
content_hash: e5fcbd35e73fffe0fbb976cdddb771e3bea80432035ef99c202f3b8aceccd970
fetched_at: '2026-06-29T00:09:01.005933+00:00'
page_id: '370618320'
product: rm
source: tdn-rm
title: 2660290 FOPCALCULO01-3550 Rescisão por Comum Acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370618320
version: 3
---

# Rescisão

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Rescisão |
| **Situação/Requisito:** | Cliente solicita que as verbas referentes a projeção do aviso prévio indenizado na rescisão por comum acordo sejam pagas na integralidade, sendo pago apenas aviso prévio pela metade.  Conforme o Art. 484-A ([http://www.planalto.gov.br/ccivil\_03/Decreto-Lei/Del5452.htm#art484a](http://www.planalto.gov.br/ccivil_03/Decreto-Lei/Del5452.htm#art484a "Follow link")), o contrato de trabalho poderá ser extinto por acordo entre empregado e empregador, caso em que serão devidas as seguintes verbas trabalhistas:  I - por metade:  a) o aviso prévio, se indenizado; e  b) a indenização sobre o saldo do Fundo de Garantia do Tempo de Serviço, prevista no § 1º do art. 18 da Lei nº 8.036, de 11 de Maio de 1990;  II - na integralidade, as demais verbas trabalhistas. |
| **Solução/Implementação:** | Criado o parâmetro "Comum Acordo paga metade somente do aviso prévio, projeções consideram período completo" em Configurações | Parâmetros | Parametrizador | Folha de Pagamento | 06.01.06 - Rescisão | Aviso Prévio.  Com este parâmetro marcado, o sistema irá calcular o aviso prévio indenizado, pagando pela metade a parte devida do empregador. As demais verbas que são calculadas sobre a projeção do aviso prévio indenizado (Férias e 13º Salário) serão pagas na integralidade de dias de aviso prévio indenizado.  Com o parâmetro desmarcado, o sistema irá calcular e pagar, o aviso prévio indenizado e as verbas sobre a projeção do aviso prévio, na integralidade. Caso o usuário queria que todas as verbas sejam pagas pela metade, deve informar no campo 'Dias de Aviso Indenizado' no processo de Rescisão, somente a metade dos dias de aviso devido. |
| **Tickets relacionados:** | 2660290; 2614600; 3092802 |
