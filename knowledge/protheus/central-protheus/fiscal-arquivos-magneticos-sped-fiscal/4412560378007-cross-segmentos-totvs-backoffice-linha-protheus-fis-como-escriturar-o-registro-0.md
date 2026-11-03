---
article_id: 4412560378007
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 0eedf05df8c7467dcb73e8c633e55c9a727e8035dbf1ff42196c852bd616f6ec
fetched_at: '2026-06-28T22:42:03.703585+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como escriturar o
  registro 0015  Dados do Contribuinte Substituto ou Responsável pelo ICMS Destino
  na EFD ICMS/IPI?
type: support-article
updated_at: '2021-11-08T11:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412560378007-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-escriturar-o-registro-0015-Dados-do-Contribuinte-Substituto-ou-Respons%C3%A1vel-pelo-ICMS-Destino-na-EFD-ICMS-IPI
---

**Dúvida**

 Como escriturar o registro 0015 Dados do Contribuinte Substituto ou Responsável pelo ICMS Destino na EFD ICMS/IPI?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

As informações contidas neste registro terão origem nas inscrições estaduais informadas no parâmetro MV\_SUBTRIB, localizado dentro do configurador do Protheus.

**Caminho:**Configurador -> Cadastro -> Parâmetros -> Pesquisar

O parâmetro deverá ser preenchido com as inscrições estaduais onde a empresa é contribuinte de ICMS.

**Exemplo:**MV\_SUBTRIB=SP123456789/MG123456789/

UF + Numeração de Inscrição Estadual

**![](https://tdn.totvs.com/download/attachments/238035285/image2016-6-3%2021%3A47%3A51.png?version=1&modificationDate=1464997321000&api=v2)**

Caso utilize o cadastro de Inscrição Estadual na rotina FISA097, será considerado no registro 0015 a informação cadastrada na rotina FISA097 tabela CLO.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412552650263/mceclip0.png)
