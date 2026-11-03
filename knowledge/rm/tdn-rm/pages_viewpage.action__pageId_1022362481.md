---
content_hash: 9a698ce173a18465aa559a5e2b94d5ffc6f855f3f28be5dcd951d2a84950be9a
fetched_at: '2026-06-29T00:05:48.042228+00:00'
page_id: '1022362481'
product: rm
source: tdn-rm
title: Aplicação da Regra da Alíquota do ISS com Base na Aderência dos Municípios
  à NFS-e Nacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1022362481
version: 41
---

# Conteúdo

2Conteúdo

# 1. Introdução

Tem como objetivo assegurar que, a partir da ativação da NFS-e Nacional para determinado município, o comportamento do sistema seja adequado às diretrizes do projeto nacional, evitando o carregamento da alíquota de ISS em situações onde isso não deve ocorrer.

# 2. Parametrização

A remoção da alíquota do ISS dependerá da configuração dos parâmetros descritos abaixo:

ParametrosleftParâmetros GeraisfalsefalseParametrizações GeraisAmbiente NFS-e

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NFS-e> | Ambiente NF-e. O parâmetro **Layout Nacional** deve estar marcado**.**

ImagemParâmetros do Movimento

Parâmetros do Tipo de Movimento:

O Tipo de Movimento deve obrigatoriamente iniciar com **2.1.xx**. Dessa forma, apenas o processo de tributação e geração da DPS (2.1.xx) será afetado pela alteração.

Parametrizações Tipo MovimentoFis - NF-e

* ETAPA 67 - Fis - NF-e: O campo “**NFS-e Municipal (Modelo Nacional)**” deve obrigatoriamente ser preenchido com um valor distinto de “**Não Integrado**”.

  Imagem

* Parametrização dos Tributos a opção: "Procurar Alíquota Em" deve estar como "Serviço"
* Parâmetro "Editar Base de Calculo" deve estar Marcado.

ImagemDados Fiscais do Município

Nos Dados Fiscais do Município, é possível informar a Data de Ativação da integração municipal ao Layout Nacional da NFS-e

Parametrizações do Município

* Informar o campo **Data de Ativação da NFS-e Nacional**:

  Imagem

  Com base na lista oficial exportada da **NFS-e Nacional (gov),** foi realizado atualização do campo **Data de Ativação da NFS-e Nacional** dos municípios aderentes automaticamente com a atualização do patch.

  O sistema irá levar em consideração o município de incidência do ISS, ou seja, aquele informado no movimento, aba Integrações Fiscal:

  Imagem
Importante

**A Filial não pode ser Optante pelo Regime Simplificado.**

# 3. Impactos:

Quando a "**Data de Ativação da NFS-e Nacional"** estiver preenchida e for menor ou igual à "**Data de competência**" ou "**Data de Emissão**" do movimento, o sistema **não carregará a alíquota de ISS** no tributo do movimento.

Quando a "**Data de Ativação da NFS-e Nacional"** estiver ausente ou for posterior à "**Data de competência**" ou "**Data de Emissão**", o sistema manterá o carregamento da alíquota de ISS de acordo com a regra já existente.

O sistema realizará primeiramente a comparação utilizando a "**Data de Competência",** caso ela não esteja preenchida, será considerada a **Data de Emissão.**

Importante

**Movimentos vindos do faturamento não possuem Data Competência, portanto, para estes movimentos o sistema irá considerar a Data de Emissão.**

## 3.1 Criação do Movimento

Quando parametrizado corretamente, ao criar um movimento 2.1.XX, o sistema passará a zerar automaticamente o valor da alíquota do ISS:

Aba - Tributos do item do movimento:

## 3.2 XML da NFS-e

Durante a geração do XML da NFS-e (Processo: Enviar NFS-e) , o sistema removerá automaticamente a tag <**pAliq**>:

xmlEclipse1XML NFS-e sem aliquota ISStrue

200.00


4
1

0
]]>

## 3.3 Grupo de informações dos tributos do serviço prestado

Detalhes: [Grupo](https://tdn.totvs.com/pages/viewpage.action?pageId=822688854) [trib/tribMun](https://tdn.totvs.com/pages/viewpage.action?pageId=822688854)

Obs.: A Alíquota será zerada pelo serviço de Tributação quando o Município do Serviço estiver com o Campo "**Data Ativação da NFS-e Nacional**" preenchido em Dados Fiscais do Município:

## 3.4 Consulta da NFS-e

Ao realizar a consulta da NFS-e e a mesma for **Autorizada**, será criado um movimento 2.2.XX incluindo a Alíquota retornada pela prefeitura.

Consulta da NFS-e Nacional a Prefeitura Retornar a Tag: **pAliqAplic,**este valor será atualizado no Movimento:

xmlEclipse1XML NFS-e sem aliquota ISStrue
130.00
  5.00
6.50
6.50
123.50
]]>
