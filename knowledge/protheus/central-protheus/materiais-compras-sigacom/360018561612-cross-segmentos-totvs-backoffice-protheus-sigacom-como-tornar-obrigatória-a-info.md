---
article_id: 360018561612
category: Materiais - Compras (SIGACOM)
content_hash: abbb1394eeb3c3e14ddb4c230e084bf4aec10655dd4c239252b558532af6bf9d
fetched_at: '2026-06-28T22:41:16.067710+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como tornar obrigatória
  a informação de um motivo para a escolha do Fornecedor na Análise da Cotação ?
type: support-article
updated_at: '2022-12-06T20:05:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018561612-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-tornar-obrigat%C3%B3ria-a-informa%C3%A7%C3%A3o-de-um-motivo-para-a-escolha-do-Fornecedor-na-An%C3%A1lise-da-Cota%C3%A7%C3%A3o
---

**Dúvida**Como tornar obrigatória a informação de um motivo na troca de fornecedor vencedor na Análise da Cotação ? - MV\_MOTIVOK - Help A161MOTIVO  
  
**Ambiente**Microsiga Protheus – Estoque e Custos – A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o módulo Configurador (SIGACFG);  
2. Acesse o caminho Base de Dados - Dicionário - Base de Dados;  
3. Selecione a opção Parâmetros;  
4. Localize o parâmetro ***MV\_MOTIVOK***;  
5. Configure o parâmetro como .T.  
  
Com este parâmetro habilitado, ao realizar a análise da cotação será sempre solicitado o preenchimento do campo "Observações", e não somente quando o ganhador for escolhido manualmente.

Caso não preenchido, será retornado o Help ***A161MOTIVO***, solicitando o preenchimento.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
