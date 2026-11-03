---
article_id: 360029010132
category: GPE - eSocial - Não Periódicos
content_hash: 8b91f4bae496aefc013eb66a74a56497ad9819fe4b606fca614e8a4a718d3013
fetched_at: '2026-06-28T22:45:05.744266+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2230 - Erro de Predecessão, não foi
  possível encontrar o registro predecessor
type: support-article
updated_at: '2026-06-15T19:48:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029010132-RH-Linha-Protheus-GPE-eSocial-S-2230-Erro-de-Predecess%C3%A3o-n%C3%A3o-foi-poss%C3%ADvel-encontrar-o-registro-predecessor
---

**Ocorrência**  
No módulo Gestão de Pessoal, ao tentar incluir um afastamento no cadastro de ausência, ocorre o erro de predecessão, não foi possível encontrar o registro predecessor  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**   
Esse incidente ocorre, pois existem afastamentos anteriores que foram enviados para o TAF, porém o campo **R8\_INTGTAF** de integração com o TAF ficou em branco, ou existem afastamentos que estão preenchidos somente o campo **TAFKeyInicio** ou **TAFKeyFinal** no cadastro de ausência.  
  
Conheça mais sobre o RDMAKE responsável por realizar o ajuste dos campos:  
[DRHESOCP-19610 DT RDMAKE Com ajuste dos campos R8\_TAFKI e R8\_TAFKF](https://tdn.totvs.com/display/public/PROT/DRHESOCP-19610+DT+RDMAKE+Com+ajuste+dos+campos+R8_TAFKI+e+R8_TAFKF)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Atualizar o ambiente com o ultimo acumulado do Esocial:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
