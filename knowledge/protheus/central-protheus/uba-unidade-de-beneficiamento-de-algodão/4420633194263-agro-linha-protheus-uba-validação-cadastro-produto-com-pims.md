---
article_id: 4420633194263
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 9ac2570d08d35db4524820ccfcef0610acb94a2344d081dea48fcf175916bd2d
fetched_at: '2026-06-28T22:45:35.671768+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Validação cadastro produto com PIMS
type: support-article
updated_at: '2025-06-20T19:43:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420633194263-Agro-Linha-Protheus-UBA-Valida%C3%A7%C3%A3o-cadastro-produto-com-PIMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22094145955351) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Como é feita a validação dos produtos do agronegócio no **PIMS - Plant Information Management System**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - A partir da versão 12.1.17  
  
**Solução**No cadastro de **produto**, no formulário de **produtos agronegócio**, foi adicionado validações nos campos das abas **Macronutrientes**, **Micronutrientes e Nutrientes Benéficos**, sendo que o valor informado em cada campo deve ser menor ou igual a 100, e a soma dos campos menor ou igual a 100.  
Para o **carbono orgânico total**, o valor não pode ser maior que 100.  
A validação das abas é realizada ao salvar o registro, não permitindo salvar e apresentando mensagem ao usuário se a soma da aba for maior que 100.
