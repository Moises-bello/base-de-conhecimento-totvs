---
article_id: 115008352827
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 4ae3ac707bfdef72ad97bf83a12e10dad69c65b9f935f4d37c9a2f638c11d0e7
fetched_at: '2026-06-28T22:40:47.400987+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - o valor '01' informado
  no campo cod natureza cta/grp (C1O_CODNAT) não existe na base de dados.
type: support-article
updated_at: '2025-05-15T19:36:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008352827-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-o-valor-01-informado-no-campo-cod-natureza-cta-grp-C1O-CODNAT-n%C3%A3o-existe-na-base-de-dados
---

**Ocorrência**

Erro apresentado ao importar o ECF para o TAF

O valor '01' informado no campo Cod Natureza Cta/Grp (C1O\_CODNAT) não existe na base de dados.

**Ambiente**  
  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 11.80

**Solução**

Neste caso confira se o valor ‘01’ esta correto para a conta informada

Confira também se na rotina do TAF – bloco J050 no campo natureza existe a opção de pesquisa de natureza para este campo, caso não exista ,esta então faltando a tabela auto-contida para este campo verifique atualização no modulo TAF para este tratamento.

Campo 3 - COD NAT

Código da natureza da Conta Analítica ou Sintética

01 – Contas do Ativo

02 – Contas do Passivo

03 – Contas do Patrimônio Líquido

04 – Contas de Resultado

05 – Contas de Compensação

09 – Outra

* Rotina - [**TAFA060** (Cadastro de Plano de Contas)](https://tdn.totvs.com/pages/releaseview.action?pageId=284465420)
* Veja que o campo C1O\_CODNAT busca a informação na tabela autocontida C2R

C2R - TABELA AUTOCONTIDA

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407603571479)

Veja se a tabela autocontida C2R esta atualizada , caso não esteja atualizado veja   como realizar [Atualização das Tabelas Autocontidas](https://tdn.totvs.com/pages/releaseview.action?pageId=241698504)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407603789591)

<http://sped.rfb.gov.br/estatico/D5/2BF489D2C4AAFB80402C9D5892E7D0F7CACE47/Manual_de_Orienta%c3%a7%c3%a3o_da_ECF_2016_05_25.pdf>

Pagina 110

Saiba Mais:

# [Erro\_000009\_registro\_não\_integrado\_C1O\_CODNAT\_C1O\_CTASUP](http://tdn.totvs.com/pages/releaseview.action?pageId=241698504)

[MP - SIGACTB - CTBS001 - Atualização das Tabelas Autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGACTB-CTBS001-Atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-)  
[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)
