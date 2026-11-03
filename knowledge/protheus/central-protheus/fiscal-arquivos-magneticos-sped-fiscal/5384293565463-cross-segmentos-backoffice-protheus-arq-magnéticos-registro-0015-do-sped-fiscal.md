---
article_id: 5384293565463
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 461f05aec24f9e205a15fb4ad69a8c37285be5c05b371c550cf50fa3a98abc42
fetched_at: '2026-06-28T22:42:00.810373+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Arq. Magnéticos -  Registro 0015 do
  Sped Fiscal gerado indevidamente
type: support-article
updated_at: '2022-07-25T16:47:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5384293565463-Cross-Segmentos-Backoffice-Protheus-Arq-Magn%C3%A9ticos-Registro-0015-do-Sped-Fiscal-gerado-indevidamente
---

**Ocorrência**Ao gerar o arquivo texto do **Sped Fiscal** está sendo apresentado o registro **0015 - Dados do Contribuinte Substituto ou Responsável pelo ICMS Destino** indevidamente.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta quanto as inscrições estaduais ou porque há dados de inscrição estadual cadastradas indevidamente.  
  
**Solução**

Para gerar informações neste registro o sistema valida as seguintes informações:

1. 1 - Conteúdo do **parâmetro MV\_SUBTRIB**

Caminho: **Configurador** -> **Cadastro** -> **Parâmetros** -> **Pesquisar**

O parâmetro deverá ser preenchido com as **Inscrições** **Estaduais** onde a empresa é **Contribuinte de ICMS**.

Exemplo: **MV\_SUBTRIB**=SP123456789/MG123456789/

**UF + Numeração de Inscrição Estadual**

**![](https://tdn.totvs.com/download/attachments/238035285/image2016-6-3%2021%3A47%3A51.png?version=1&modificationDate=1464997321000&api=v2)**

**2- Tabela CLO - Tabela de Inscrição Estadual**

Tabela alimentada através da rotina **FISA097 - Inscrição Estadual**  
  
Se não for preciso gerar o registro para a **UF** em questão, não pode haver informação para a **UF** no parâmetro **MV\_SUBTRIB** e nem na tabela **CLO - Tabela de Inscrição Estadual**
