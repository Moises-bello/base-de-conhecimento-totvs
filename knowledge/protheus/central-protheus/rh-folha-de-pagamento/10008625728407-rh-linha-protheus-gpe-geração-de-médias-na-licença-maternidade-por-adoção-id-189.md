---
article_id: 10008625728407
category: RH - Folha de Pagamento
content_hash: ea382fa7ed6748cba02c9ed7f90c0d553b672d18959e6690fdb1586f4e0ac6b9
fetched_at: '2026-06-28T22:44:14.971763+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Geração de médias na licença maternidade por adoção
  (ID 1894)
type: support-article
updated_at: '2025-08-12T13:31:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008625728407-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-de-m%C3%A9dias-na-licen%C3%A7a-maternidade-por-ado%C3%A7%C3%A3o-ID-1894
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26308749388567) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**O sistema gera a média de licença maternidade aglutinado com o salário na verba de ID 0238 nos casos de licença maternidade por adoção, o que ocasiona cálculo incorreto de impostos no eSocial.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**O erro ocorre devido a falta de cadastro da verba com ID 1894.  
  
**Solução**Ajuste no cálculo da folha quando há licença maternidade por adoção para que o valor da média seja gerado separadamente, no novo ID de cálculo **1894 -Base médias auxílio maternidade**; o valor fixo, referente ao salário, continuará sendo gerado no ID 0238 -Base Salário Maternidade.  
  
Deverá ser cadastrado uma verba de tipo Base (Provento) para ser vinculada ao ID 1894 - Base médias auxílio maternidade e como sugestão de configuração, cópia da verba de ID 0238 -Base Salário Maternidade. Para cadastrar a verba acesse Atualizações > Definições de Cálculos > Verbas (GPEA040);  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31972572324503)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como cadastrar os Id's de cálculo relacionados aos adicionais de Licença Maternidade por adoção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11912715269911-RH-Linha-Protheus-GPE-Como-cadastrar-os-Id-s-de-c%C3%A1lculo-relacionados-aos-adicionais-de-Licen%C3%A7a-Maternidade-por-ado%C3%A7%C3%A3o)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
