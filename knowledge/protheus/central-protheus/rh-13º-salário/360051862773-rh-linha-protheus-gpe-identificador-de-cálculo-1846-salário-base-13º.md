---
article_id: 360051862773
category: RH - 13º salário
content_hash: 5147f97de801b7fff44f2aac3413b9fa07bfde79ec6146e64d72965211027684
fetched_at: '2026-06-28T22:44:00.819737+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Identificador de cálculo 1846 Salário Base 13º
type: support-article
updated_at: '2025-08-13T14:43:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051862773-RH-Linha-Protheus-GPE-Identificador-de-c%C3%A1lculo-1846-Sal%C3%A1rio-Base-13%C2%BA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19057764279703) Tempo aproximado para leitura: 00:01:30 min**

**Ocorrência**Identificador de cálculo 1846 Salário Base 13º.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Quando o funcionário não está afastado o ano inteiro, ao executar o roteiro 132, Segunda Parcela do 13º Salário, o sistema não gera nenhuma verba, desse modo o evento S-1200 não é gerado para eSocial.  
  
**Solução**No período normal, para um Trabalhador afastado o Sistema gera a Verba de "Salário Base", com isso há uma tratativa para gerar a informação sem movimento ao TAF, porém no caso do roteiro 132 não é gerado nenhuma verba e consequentemente não gera o evento.

Por isso foi criado o identificador de cálculo **1846, Salário Base 13º**, para gerar uma verba de **base** com o valor do **salário no cálculo da segunda parcela do 13º**.  
Para facilitar o cadastro da verba, copiar as informação da verba ID 0318 - Salario do Mês.  
  
Esse identificador **não** é obrigatório.

Saiba Mais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=546252203>

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
