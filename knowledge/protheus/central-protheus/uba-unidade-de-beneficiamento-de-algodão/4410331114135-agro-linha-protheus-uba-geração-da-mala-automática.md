---
article_id: 4410331114135
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 3f87bd8dd0037f7ec31e3cd0fc464bcf97ccf7135feb20d7ca1cfa6d90bc6be3
fetched_at: '2026-06-28T22:45:35.608489+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Geração da mala automática
type: support-article
updated_at: '2025-06-18T20:30:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410331114135-Agro-Linha-Protheus-UBA-Gera%C3%A7%C3%A3o-da-mala-autom%C3%A1tica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21881564093079) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Qual a regra de negócio da **geração da mala automática** no beneficiamento?  
  
**Ambiente**TOTVS Agro **–** TOTVS Agro **–** Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão **–** A partir da versão 12.1.17  
  
**Solução**No **Beneficiamento - AGRA615**, ao finalizar o processo, o Sistema irá verificar se há malas abertas para a safra corrente. Caso exista, será realizado o vínculo da amostra de classificação com a mala, caso contrário, será automaticamente criada uma mala para que seja possível relacionar a ela as amostras retiradas dos fardinhos beneficiados.   
Para cada mala gerada automaticamente, o Sistema irá gerar um código de barras, nesse processo não haverá interação de usuário. Ao finalizar uma mala, será possível realizar a manutenção da mesma incluindo, alterando ou excluindo amostras para a correção de eventuais incoerências. Também será permitido, após o processo de manutenção, realizar o fechamento da mala **Malas Internas** **– Visual** **Pendente**, **Malas Externas – HVI Pendente**.   
A geração de malas automáticas é facultativa, para que seu uso seja possível, é necessário marcar o parâmetro correspondente **MV\_AGRMALA -** **É Mala Automática** como verdadeiro.
