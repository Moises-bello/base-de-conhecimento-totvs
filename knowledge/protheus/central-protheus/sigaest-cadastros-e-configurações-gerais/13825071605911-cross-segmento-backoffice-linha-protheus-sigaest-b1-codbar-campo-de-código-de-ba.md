---
article_id: 13825071605911
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: f7e00ed50104c68233127e328a08b6c2550680d7cd535c35e8d6ca1fe18071d7
fetched_at: '2026-06-28T22:39:08.046039+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - B1_CODBAR - Campo
  de código de barras permite duplicidade
type: support-article
updated_at: '2023-04-14T10:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13825071605911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-B1-CODBAR-Campo-de-c%C3%B3digo-de-barras-permite-duplicidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Na rotina ***Cadastro de Produtos (MATA010)*** o campo **Código de Barras (B1\_CODBAR)** esta duplicado em alguns registros.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

No padrão o campo de ***Código de Barras (******B1\_CODBAR)*** **não faz parte da chave de pesquisa da tabela**, por isso não tem a proteção que valida a se a informação existe em outro cadastro. Essa configuração fica livre ao usuário realizar a própria validação, ou seja, deve customizar conforme necessidade específica.

Seguem abaixo links com instruções sobre integridade no Protheus

***Integridade Referencial no Protheus***

***<https://tdn.totvs.com/display/public/framework/Integridade+Referencial>***

***Rotina CheckDupl – Verifica a Integridade de Registros Duplicados***

***<https://tdn.totvs.com/pages/releaseview.action?pageId=242386686>***

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
