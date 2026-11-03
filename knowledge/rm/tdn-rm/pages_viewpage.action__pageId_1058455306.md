---
content_hash: 2ee4903222f9735569345fe7ee7b31d135e9bf9ed36197d109b982563e20f081
fetched_at: '2026-06-29T00:05:52.648971+00:00'
page_id: '1058455306'
product: rm
source: tdn-rm
title: Alterações ECF 2026 - Layout 12
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058455306
version: 16
---

# Alterações

Alterações

# 1. Registro 0000

**Registro 0000: Abertura do Arquivo Digital e Identificação da Pessoa Jurídica**

* Campo 3: **COD\_VER** - (Código da versão do leiaute) de acordo com o layout 12, Para o ano-calendário 2025 e situações especiais de 2026, o leiaute a ser informado deverá ser = 0012.
* Campo 6: **IND\_SIT\_INI\_PER** - Indicador do Início do Período - foi incluída uma nova opção para este registro:
  + 7 - Retorno às atividades de empresas inativas.

Este campo é gerado conforme a informação em *Cadastro da Filial – Anexo Parâmetros da ECF – Campo Indicador do Início do Período*.

Imagem

Para mais informações, acesse:

# 2. Registro 0020

**Registro 0200: Parâmetros Complementares**

Neste registro houve a **inclusão dos campos** abaixo:

* Campo 31: **POSSUI\_CEBAS** -(Entidades isentas e imunes que possuem CEBAS – Certificado de Entidade Beneficente de Assistência Social)
  + Entidades nas áreas de assistência social, saúde ou educação que atendam aos requisitos de possuírem CEBAS e o possuem, devem indicar SIM neste campo.
* Campo 32: **CEBAS** - Número CEBAS que a entidade possui.
  + O campo é habilitado para empresas que tenha definido a tributação onde o Tipo de Entidade Imune ou Isenta seja:

    - 01-Assistência Social
    - 02-Educacional
    - 16-Saúde

Este campo é gerado conforme a informação em *Cadastro da Filial – Anexo Parâmetros da ECF – Abas Tributação e Sub Pasta Complementares*.

Imagem

Para mais informações, acesse:

# 3. Registro 0021

**Registro 0021: Parâmetros de Identificação dos Tipos de Programa**

Neste registro houve a **inclusão do campo** abaixo:

* Campo 18: **IND\_REDATA** -Regime Especial de Tributação para Serviços de Datacenter – REDATA

Este campo é gerado com valor fixo "N".

Para mais informações, acesse:

# 4. Registro Y730 (novo)

**Registro Y730: Identificação de donatários/destinatários de deduções do IRPJ/CSLL.**

Foi incluído o novo Registro Y730, com os seguintes campos:

* Campo 1: **REG**
* Campo 2: **DEDUÇÃO**
* Campo 3: **TIPO**
* Campo 4: **DATA**
* Campo 5: **TIPO\_DESTINAT**
* Campo 6: **DESTINATARIO**
* Campo 7: **VALOR**
* Campo 8: **OBSERVACAO**

Para mais informações, acesse:

# 5. Tabelas Dinâmicas

As Tabelas Dinâmicas são planilhas que estão disponíveis no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816). Para utilizá-las, basta baixar os arquivos mais recentes disponíveis:

* FISPLA0001
* FISPLA0002
* FISPLA0003
* FISPLA0004

Para mais informações, acesse:

# 6. Layout ECF 2026

* O Layout ECF 2026 está disponível no [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento), sob o nome "FISLAY0014 - ECF.TotvsGen".

Imagem

# 7. Versões para atualização

A solução está disponível a partir dos patches:

Biblioteca RM

* [12.1.2506.305](https://suporte.totvs.com/portal/p/10098/download?e=1249738)
* [12.1.2510.228](https://suporte.totvs.com/portal/p/10098/download?e=1249694)
* [12.1.2602.146](https://suporte.totvs.com/portal/p/10098/download?e=1250090)

##
