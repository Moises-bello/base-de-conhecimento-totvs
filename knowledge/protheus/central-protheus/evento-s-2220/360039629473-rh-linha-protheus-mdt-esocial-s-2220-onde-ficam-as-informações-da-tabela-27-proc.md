---
article_id: 360039629473
category: Evento S-2220
content_hash: fcdce268e5b37ae86c5bd9525a58d7c3af950cd32d53393c280a8ab96235e1ae
fetched_at: '2026-06-28T22:45:25.460058+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 -  Onde ficam as informações da
  Tabela 27 (Procedimentos Diagnósticos) no SIGAMDT
type: support-article
updated_at: '2024-08-13T21:32:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039629473-RH-Linha-Protheus-MDT-eSocial-S-2220-Onde-ficam-as-informa%C3%A7%C3%B5es-da-Tabela-27-Procedimentos-Diagn%C3%B3sticos-no-SIGAMDT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25627506720791)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Onde ficam as informações da Tabela 27 (Procedimentos Diagnósticos) no modulo Medicina e Segurança do Trabalho?  
 **Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
 **Solução**No layout do eSocial é necessário informar um Procedimento Realizado (tag  **procRealizado**) para transmissão do evento S-2220, essa informação tem códigos específicos que estão previstos na Tabela 27 do Anexo I do layout do eSocial, elas devem ser informadas no campo **Proc. Realiz** (TM4\_PROCRE) na rotina de Exames localizado no caminho: Atualizações > PCMSO > Exames do módulo de Medicina e Segurança do Trabalhador (SIGAMDT).  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052286753)  
  
No Protheus, os códigos da Tabela 27 estão localizados nas tabelas dinâmicas do TAF (autocontida V2K). É possível visualizar acessando o módulo 84 (SIGATAF) no caminho: Consultas > Tabelas Dinâmicas" e filtrar o Código **V2K** (Procedimentos Diagnósticos).  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051401574)  
  
Caso não visualize a tabela ou o seu conteúdo você deverá verificar se está atualizado com os pacotes disponíveis em nossa página [**eSocial | Protheus - Entregas Legais**](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais) e realizar os procedimentos indicados no artigo abaixo: **[MP - SIGATAF - Como realizar a atualização das Tabelas Autocontidas no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-realizar-a-atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas)****Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
