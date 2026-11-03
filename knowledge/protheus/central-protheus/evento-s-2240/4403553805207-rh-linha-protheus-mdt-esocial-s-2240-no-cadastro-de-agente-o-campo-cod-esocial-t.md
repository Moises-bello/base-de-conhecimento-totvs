---
article_id: 4403553805207
category: Evento S-2240
content_hash: 4e1555ce76d244f709dd8c79c6a435a6f70767c6a2b71ff5a262200bbb5abc75
fetched_at: '2026-06-28T22:45:23.685160+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - No cadastro de Agente o campo
  Cod. eSocial (TMA_ESOC) não demonstra os códigos e descrições de acordo com a Tabela
  24 (Agentes Nocivos e Atividades) do layout Simplificado S.1
type: support-article
updated_at: '2025-03-11T18:25:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403553805207-RH-Linha-Protheus-MDT-eSocial-S-2240-No-cadastro-de-Agente-o-campo-Cod-eSocial-TMA-ESOC-n%C3%A3o-demonstra-os-c%C3%B3digos-e-descri%C3%A7%C3%B5es-de-acordo-com-a-Tabela-24-Agentes-Nocivos-e-Atividades-do-layout-Simplificado-S-1
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25310575135895)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**No cadastro de **Agentes** (MDTA182) o campo **Cod. eSocial** (TMA\_ESOC) não demonstra os códigos e descrições de acordo com a **Tabela 24** (Agentes Nocivos e Atividades) do layout Simplificado S.1  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Esse erro ocorre quando não foi aplicado na base o pacote e dicionário diferencial do eSocial liberado a partir de 31/05/21, ou caso a consulta padrão do campo esteja incorreta, pois a consulta deve buscar os dados da tabela V5Y e não T3E.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o sistema foi atualizado com o **pacote** e **dicionário diferencial** do **MDT** e **eSocial,** caso tenha atualizado prossiga para o **item 2**. Caso precise atualizar vou deixar os links abaixo:

* [Pacote Correções e Dicionário Diferencial eSocial](https://suporte.totvs.com/portal/p/10098/download#000052/all/all/search/TAF_ESOCIAL_REINF_PROTHEUS.ZIP)
* [Pacote e Dicionário Correções Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA.ZIP)

2. Se mesmo após a atualização o erro persiste, é devido a consulta padrão do campo estar incorreta, para a solução será necessario seguir as orientações do link: **[Campo TMA\_ESOC com Códigos Antigos ao Invés dos Novos da Tabela 24 do Leiaute do eSocial](https://tdn.totvs.com/x/c-APJQ)**  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
