---
article_id: 1500002279721
category: RH - FGTS / SEFIP
content_hash: b018fd1c8869c99f23afe18e41416e9fcc3df44b98bb183ba0553377a2966c34
fetched_at: '2026-06-28T22:43:41.242333+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - ERRO 300550 na Sefip - Base de cálculo 13º salário
  previdência social para funcionários demitidos antes 15 primeiros dias de janeiro
type: support-article
updated_at: '2025-08-14T17:48:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002279721-RH-Linha-Protheus-GPE-ERRO-300550-na-Sefip-Base-de-c%C3%A1lculo-13%C2%BA-sal%C3%A1rio-previd%C3%AAncia-social-para-funcion%C3%A1rios-demitidos-antes-15-primeiros-dias-de-janeiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185819387543) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**Ao importar o arquivo da Sefip onde contém funcionários demitidos antes dos 15 primeiros dias de janeiro, é apresentado o erro **3000550** - base de cálculo 13º salário previdência social - referente a competência do movimento não deve ser informada quando houver afastamento definitivo com menos de 15 dias trabalhados no ano.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**O erro ocorre pois na Sefip constam funcionários que foram desligados antes dos 15 primeiros dias de janeiro e foi calculado 13º sobre aviso, e por uma deficiência da própria Sefip, ela não aceita valores de 13º em desligamentos que ocorrem antes dos 15 primeiros dias de janeiro.  
  
**Solução** **Deve ser feito ajuste manual diretamente na Sefip**, pois a Sefip não esta preparada para receber valores de 13º em casos de demissão antes dos 15 primeiros dias de janeiro.  
  
Abaixo descrição do Manual de erros da Sefip, a caixa orienta que só deve informar valores para este campo para os funcionários com mais de 15 dias trabalhados no ano:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103270353)  
  
Embasamento Legal IN RFB nº 925:  
  
[Conforme a  IN RFB nº 925 de 2009. Art 6º.](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=15886&visao=anotado)  
*"*Art. 6º As pessoas jurídicas ou os contribuintes equiparados que efetuarem rescisão de contrato de trabalho de seus empregados e pagarem aviso prévio indenizado, deverão preencher o SEFIP da seguinte forma:  
  
I - o valor do aviso prévio indenizado não deverá ser informado; e  
  
**II - o valor do décimo-terceiro salário correspondente ao aviso prévio indenizado deverá ser informado no campo "Base de Cálculo 13º salário da Previdência Social", exceto no caso de empregado que tenha trabalhado por um período inferior a 15 (quinze) dias durante o ano, cuja informação não poderá ser prestada até que o SEFIP seja adaptado.**  
Parágrafo único. Nas hipóteses previstas neste artigo, a GPS gerada pelo SEFIP deverá ser desprezada, devendo ser preenchida GPS manualmente com os valores efetivamente devidos, incluindo as contribuições incidentes sobre o aviso prévio indenizado e sobre o décimo-terceiro salário correspondente ao aviso prévio indenizado, observado o disposto no art. 7º."  
  
**Observação:** Caso tenha dúvidas do procedimento a ser realizado, entre em contato com a CEF-Caixa Econômica Federal.

**Saiba mais:**

[RH \_ FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
