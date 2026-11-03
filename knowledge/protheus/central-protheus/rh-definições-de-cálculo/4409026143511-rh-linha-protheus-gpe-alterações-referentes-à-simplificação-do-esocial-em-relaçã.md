---
article_id: 4409026143511
category: RH - Definições de Cálculo
content_hash: 9cf84367a2801017d2de9c687750eaed27dd372e2b5204140f8893e10bcf6699
fetched_at: '2026-06-28T22:43:22.562965+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Alterações referentes à Simplificação do eSocial
  em relação à tabela de verbas, novos campos na tabela SRV
type: support-article
updated_at: '2025-06-16T14:57:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409026143511-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%B5es-referentes-%C3%A0-Simplifica%C3%A7%C3%A3o-do-eSocial-em-rela%C3%A7%C3%A3o-%C3%A0-tabela-de-verbas-novos-campos-na-tabela-SRV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32844503676311) Tempo aproximado para leitura: 00:02:00 min****Dúvida**Alterações referentes à Simplificação do eSocial em relação à tabela de verbas, novos campos na tabela SRV.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1- Alterar o campo RV\_INCIRF para 4 dígitos - Leitura da nova tabela S138 - Incidência IRRF;  
2- Criação do campo RV\_TETOP;  
3- Excluir opções 23, 24, 61 para incidência de INSS (opções válidas apenas para leiautes anteriores ao S-1.0);  
4- Criar lista de opções para o campo RV\_INCOP;  
5- Alterar para o campo RV\_INCFGTS a descrição dos tipos 21/91 e incluir tipo 92/93;  
6- Incluir verificação dos leiautes TAFxGPE considerando 9.0.00 para S-1.0, emitindo aviso de gravação apenas no GPE ou finalização da rotina em caso de divergência de versões com MV\_RHTAF=.T..  
  
**Ajustes na rotina de Cadastro de Verbas** efetuados em conformidade com a versão 9.0.00, leiaute S-1.0 da simplificação do eSocial. Acesse o Boletim Técnico abaixo para verificar os campos:  
[DRHESOCP-20070 DT Tabela de Verbas: Dicionário V.1 e rotina de Cadastro de verbas](https://tdn.totvs.com/pages/viewpage.action?pageId=590020960)

Ao acessar a rotina com o ambiente GPE atualizado e integração com TAF ativada, caso haja divergência com a versão do TAF (MV\_TAFVLES), será exibido o aviso:![](https://tdn.totvs.com/download/attachments/590020960/image2021-1-19_13-27-53.png?version=1&modificationDate=1611073674107&api=v2)

Selecionando [Não], a rotina será finalizada; Ao selecionar [Sim], acessa a rotina de Cadastro de Verbas porém as edições não serão enviadas ao TAF, apenas salvas no ambiente GPE, para futura integração após atualização de ambos os leiautes.

****Saiba Mais****

[DRHESOCP-20261 DT Novo controle de versões](https://tdn.totvs.com/pages/viewpage.action?pageId=588703973)

[DRHESOCP-20258 DT Tabela S138 - Códigos de Incidência Tributária da Rubrica para o IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=589521541)
