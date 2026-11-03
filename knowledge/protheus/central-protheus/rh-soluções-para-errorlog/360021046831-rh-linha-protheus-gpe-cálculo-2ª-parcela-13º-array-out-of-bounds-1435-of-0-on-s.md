---
article_id: 360021046831
category: RH - Soluções para error.log
content_hash: d31e8fa24bcc634ede760ea9a65a3fb7d987fc6a677a6e3f7e2d1ce021a2acd9
fetched_at: '2026-06-28T22:44:08.791551+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo  2ª Parcela 13º - array out of bounds (1435
  of 0) on S_LTABELAS (S_LTABELAS.PRG)
type: support-article
updated_at: '2025-08-21T18:51:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021046831-RH-Linha-Protheus-GPE-C%C3%A1lculo-2%C2%AA-Parcela-13%C2%BA-array-out-of-bounds-1435-of-0-on-S-LTABELAS-S-LTABELAS-PRG
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34352623958807)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**No módulo **Gestão de Pessoal**, ao tentar realizar o cálculo da **2° parcela de 13° salário** é apresentado o *error log*, ***array out of bounds ( 1435 of 0 ) on S\_LTABELAS (S\_LTABELAS.PRG).***  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Causa**   
Esse incidente ocorre, pois não existe cadastro na rotina de **manutenção de tabelas nas tabelas: S001 - INSS****, S002 - IRRF****, S003 - Salário Família****, S004 -** Salário Mínimo **e/ou S037 - Encargos Empresa** para o ano da competência de cálculo.  
  
**Solução**  
Para solucionar essa ocorrência, realizar a atualização do último pacote de Expedição Contínua de RH, e cadastrar as tabelas citadas acima. Para obter o pacote de RH, **[clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**

**Saiba Mais:**Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>
