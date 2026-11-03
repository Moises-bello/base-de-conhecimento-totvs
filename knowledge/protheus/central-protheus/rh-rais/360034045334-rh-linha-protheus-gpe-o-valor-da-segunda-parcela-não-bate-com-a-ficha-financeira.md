---
article_id: 360034045334
category: RH - RAIS
content_hash: c4febb255c8be41578e382e5e4f7f2bfb369728888452db60686f0d853e7a283
fetched_at: '2026-06-28T22:44:05.774946+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - O valor da segunda parcela não “bate” com a ficha
  financeira e com a tabela SR2. As verbas estão com incidência correta para a rais.
type: support-article
updated_at: '2021-06-09T12:08:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034045334-RH-Linha-Protheus-GPE-O-valor-da-segunda-parcela-n%C3%A3o-bate-com-a-ficha-financeira-e-com-a-tabela-SR2-As-verbas-est%C3%A3o-com-incid%C3%AAncia-correta-para-a-rais
---

**Dúvida**O valor da segunda parcela não “bate” com a ficha financeira e com a tabela SR2. As verbas estão com incidência correta para a rais.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  Todas as versões  
  
**Solução**

Deverá verificar no **acumulado**, tabela **SRD** em **Consulta/Cadastro/Acumulado,**as verbas que estão sendo pagas na primeira parcela, roteiro 131 e na segunda parcela, roteiro 132.

Para o eSocial as verbas do roteiro 131 não podem ser as mesmas do roteiro 132, por conta das incidências de INSS, IRRF.

Caso seja identificado que existe a mesma verba sendo paga no roteiro 131 e no roteiro 132:

Deverá verificar a incidência desta verba para a rais, campo **RV\_RAIS**, neste caso deverá ter a incidência para a primeira parcela e para a segunda parcela de décimo terceiro.

Vale lembrar que a ficha financeira na versão 12, é levar os valores dos roteiros 131 e 132 na coluna décimo terceiro.

No caso as verbas de primeira parcela devem ser diferentes da segunda parcela, como dito acima.
