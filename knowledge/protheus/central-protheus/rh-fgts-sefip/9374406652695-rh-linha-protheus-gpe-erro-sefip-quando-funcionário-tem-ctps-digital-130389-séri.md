---
article_id: 9374406652695
category: RH - FGTS / SEFIP
content_hash: adf17b890a850402a4c6398e0ab22cbb8971776e0b28c4ed10a3103bf6d6a990
fetched_at: '2026-06-28T22:43:41.300099+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro Sefip quando funcionário tem CTPS digital
  - 130389 - Série CTPS Inválida
type: support-article
updated_at: '2025-08-07T22:00:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9374406652695-RH-Linha-Protheus-GPE-Erro-Sefip-quando-funcion%C3%A1rio-tem-CTPS-digital-130389-S%C3%A9rie-CTPS-Inv%C3%A1lida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34012812264087) Tempo aproximado para leitura: **00:01:00 min** **Ocorrência**Erro Sefip quando funcionário tem CTPS digital - 130389 - Série CTPS Inválida.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.25  
  
**Causa**  
Dado inválido no campo Série CTPS no cadastro do funcionário ou alteração da CTPS no cadastro.  
  
**Solução**Quando a CTPS do Funcionário é digital, os campos **Cart.Profis.** e **Série CTPS** da aba **Documentos** do cadastro do Funcionário devem ficar em branco, pois o sistema esta preparado para considerar o CPF automaticamente como CTPS na geração da Sefip:  
Caminho rotina Funcionários **>Atualizações >Funcionários >Funcionários**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9374238984983)  
  
Além disso, o campo **Alt.Car.Prof** deve ficar com **Não**, pois se ficar com SIM e existir registro de alteração de carteira, o sistema irá buscar a informação do Histórico de alterações cadastrais (tabela SR9) e o mesmo erro será apresentado:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9374290582807)  
  
  
**Saiba mais**  
[RH - Linha Protheus - GPE - Qual adequação foi feita no Protheus para atender a CTPS digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050559414)

[RH - FGTS /SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
