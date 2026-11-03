---
article_id: 5615398804759
category: MDT - PCMSO
content_hash: 0b43d97329b852b663e100d2a86f2892829374f7bb16f8e0c5758c8aade45448
fetched_at: '2026-06-28T22:44:28.468913+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - O que deve ser realizado no sistema se o Médico
  Coordenador do PCMSO for desligado da empresa no período de vigência do PCMSO
type: support-article
updated_at: '2025-09-03T14:00:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5615398804759-RH-Linha-Protheus-MDT-O-que-deve-ser-realizado-no-sistema-se-o-M%C3%A9dico-Coordenador-do-PCMSO-for-desligado-da-empresa-no-per%C3%ADodo-de-vig%C3%AAncia-do-PCMSO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25843673438103) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**O que deve ser realizado no sistema se o Médico Coordenador do PCMSO  terminar seu vinculo com a empresa no período de vigência do PCMSO?  
Exemplo: O PCSMO  foi gerado no período 07/01/2021 à 06/01/2022 por **Médico Coordenador A**, este médico foi desligado dentro da vigência deste PCMSO, a partir de abril o **Médico B**, passou a ser o coordenador, como deve ser realizado essa substituição? Visto que não tem como mudar o médico na programação e já existem exames realizados para aquele PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Neste caso deve ser excluído o PCMSO do **Médico A**, onde os **exames não** realizados serão **excluídos**, os exames que foram realizados continuaram no sistema, e deve ser incluído um novo PCMSO para o novo Médico coordenador.  
Importante reforçar que ao clicar em outras Ações - Excluir, não irá apagar de fato o número do PCMSO, irá apenas **excluir os exames ainda não realizados**, pois se o Médico não tem vinculo ativo com a empresa, portanto não tem como controlar os exames ainda não realizados, dito isto a empresa deve cadastrar um novo PCMSO a o novo Médico responsável e será direcionado a ele os exames ainda não realizados, podendo assim realizar o controle da Saúde Ocupacional.  
O sistema manterá o histórico dos exames e médicos conforme os PCMSO cadastrado para o período em questão.  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
