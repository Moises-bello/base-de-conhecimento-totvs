---
content_hash: 2125929e515e2440fca5acb312e2fbb40ccdcf13f8c2e5cc1a24c63c18dd83f2
fetched_at: '2026-06-29T00:10:00.339610+00:00'
page_id: '452718496'
product: rm
source: tdn-rm
title: Gerar Exames Pendentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Exames+Pendentes
version: 2
---

**Gerar Exames Pendentes**

O processo "Gerar Exames Pendentes" tem a finalidade de gerar no cadastro do funcionário, os exames a serem realizados e pode ser executado a qualquer momento pelo usuário do sistema.  
   
**Observação:**

* No cadastro da Seção possui o campo CNAE, onde deve ser preenchido conforme os CNAE disponíveis no menu: " SSO - PPRA - CNAE ".   
  Para os graus de risco 1 e 2 dispensas da realização do exame demissional em até mais 135 dias, para os graus de risco 3 e 4 dispensas da realização do exame demissional em até mais 90 dias.   
  Na geração dos exames pendentes, se para a seção do funcionário que não houver um CNAE, deverá ser aplicado o menor valor (90 dias).
* Retorno ao trabalho só e gerado a partir do primeiro dia da volta ao trabalho de trabalhador ausente por período igual ou superior a 30 (trinta) dias por motivo de doença ou acidente, de natureza ocupacional ou não, ou parto.

**Exemplo:**

Supondo que no Perfil de Exames do funcionário ele possua o exame "Avaliação Clínica" como Periódico e Demissional. CNAE da seção de grau de risco 1: 90 dias Última data do exame periódico "Avaliação Clínica": 01/08/2016 Data da demissão: 09/09/2016 Neste caso o exame demissional não será gerado, pois possui menos de 90 dias que foi realizado o exame periódico.
