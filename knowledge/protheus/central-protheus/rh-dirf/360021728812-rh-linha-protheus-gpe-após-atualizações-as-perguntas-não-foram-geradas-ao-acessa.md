---
article_id: 360021728812
category: RH – DIRF
content_hash: c370364dfabf73c3af05a17e86d74deeb7d303af477b12251b22debf11b33584
fetched_at: '2026-06-28T22:44:07.846087+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Após atualizações as perguntas não foram geradas
  ao acessar a rotina Arquivo Magnético
type: support-article
updated_at: '2025-08-19T17:27:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021728812-RH-Linha-Protheus-GPE-Ap%C3%B3s-atualiza%C3%A7%C3%B5es-as-perguntas-n%C3%A3o-foram-geradas-ao-acessar-a-rotina-Arquivo-Magn%C3%A9tico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34295834610711)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Após aplicar o pacote de atualização e executar o UPDDISTR, as perguntas de espólio não foram geradas ao acessar a rotina Arquivo Magnético.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**  
Tipo de inscrição não é CPF.  
  
**Solução**O grupo de perguntas **GPM590ESPO,** somente será gerada se no Configurador, em **Configuração de Filiais** for informado nos dados gerais o **Tipo de Inscrição** for **CPF** e não CNPJ. Esse grupo foi criado para atender ao leiaute que trata de pessoa física.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018774212)  
  
Grupo de Perguntas, criado para para preencher os valores dos novos campo no registro DECPF.   
Caso as perguntas **Situação da Decl?** Esteja preenchida como **S** e **Tipo do Evento?** Igual a **1 – Encerramento de espolio** o pergunte **não** é apresentado pois não é necessário o preenchimento desses campos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018648971)

**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)

[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
