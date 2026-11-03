---
article_id: 360051384773
category: MDT - EPI
content_hash: a030ba9dabcf55b310d659c65e3b96a92495fb6353e1be16fab8736f62984733
fetched_at: '2026-06-28T22:44:25.416910+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - É possível definir se o sistema irá ler as informações
  do armazém vindo da rotina de Produtos ou da rotina de Indicador de Produtos
type: support-article
updated_at: '2024-11-05T11:09:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051384773-RH-Linha-Protheus-MDT-%C3%89-poss%C3%ADvel-definir-se-o-sistema-ir%C3%A1-ler-as-informa%C3%A7%C3%B5es-do-armaz%C3%A9m-vindo-da-rotina-de-Produtos-ou-da-rotina-de-Indicador-de-Produtos
---

**Dúvida**É possível definir se o sistema irá ler as informações do armazém vindo da rotina de Produtos ou da rotina de Indicador de Produtos?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Sim é possível. O almoxarifado é um campo que aparece preenchido de acordo com o cadastro do EPI na rotina de Produtos (EPI) (MATA010), porém é possível alterá-lo desde que possua outro relacionamento entre o EPI e outro Almoxarifado.  
  
É possível definir se o sistema irá ler as informações do armazém vindo da rotina de Produtos ou da rotina de Indicador de Produtos, para isso, basta realizar a configuração do parâmetro MV\_ARQPROD.  
  
MV\_ARQPROD= Este parâmetro permite definir a tabela que será considerada para coletar as informações. Pode ser configurado com:  
  
SB1: O sistema utiliza os campos da tabela Produtos (SB1) ou  
SBZ: O sistema utiliza os campos da tabela de Indicadores de Produtos (SBZ).  
  
**Saiba Mais**  
[Central de artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT)
