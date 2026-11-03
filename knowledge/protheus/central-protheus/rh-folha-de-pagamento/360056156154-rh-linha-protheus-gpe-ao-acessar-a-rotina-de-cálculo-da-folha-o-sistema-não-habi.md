---
article_id: 360056156154
category: RH - Folha de Pagamento
content_hash: b45431f6c0a67a5e806ef26bcf2937717c6472edc13af31da9aa00891eebba7c
fetched_at: '2026-06-28T22:44:11.778312+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE  - Ao acessar a rotina de cálculo da folha o sistema
  não habilita os botões de filtro e de calcular.
type: support-article
updated_at: '2026-06-22T18:06:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056156154-RH-Linha-Protheus-GPE-Ao-acessar-a-rotina-de-c%C3%A1lculo-da-folha-o-sistema-n%C3%A3o-habilita-os-bot%C3%B5es-de-filtro-e-de-calcular
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26355003651735) Tempo aproximado para leitura: 00:04:00 min**

**Ocorrência**No módulo gestão de pessoal, ao tentar preencher os parâmetros para calculo o sistema habilita apenas os botões **Parâmetros** e **Sair**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097584773)

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - GPE - Todas as versões  
  
**Causa**Situação ocorre pois não foi realizado a carga nas rotinas **Fórmulas** e **Roteiros de Cálculo** para que o sistema atualize as informações no banco de dados.

**Solução**

Para corrigir a situação, acessar a rotina Atualizações -> Definições Cálculo -> Fórmulas:

- Aguardar o sistema carregar a tabela **RC2/RC3.**

Acessar a rotina Atualizações -> Definições Cálculo -> Roteiros de Cálculo:

**-** Aguardar o sistema carregar a tabela**SRY/SRM****.**

Após o procedimento o sistema será carregado o conteúdo da tabela RY\_ALIAS e permitirá executar o cálculo por roteiro GPEM020.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
