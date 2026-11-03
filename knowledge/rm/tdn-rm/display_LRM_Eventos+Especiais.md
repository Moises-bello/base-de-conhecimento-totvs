---
content_hash: 6042f7d48be666ba213cef10f732fd9ea136f63219634b02003bae7a21ec7c05
fetched_at: '2026-06-29T00:12:03.170123+00:00'
page_id: '904067757'
product: rm
source: tdn-rm
title: Eventos Especiais
type: documentation
url: https://tdn.totvs.com/display/LRM/Eventos+Especiais
version: 22
---

LayoutCampos

A **"Lista dos Eventos Especiais da Apuração"** no layout do **MIT (Módulo de Inclusão de Tributos)** refere-se ao conjunto de eventos societários que impactam a apuração dos tributos e devem ser informados no arquivo.

O campo **"ListaEventosEspeciais"** é opcional, mas se informado, deve conter os dados corretamente estruturados para garantir a validação do arquivo JSON.

As informações são extraídas do Cadastro da Filial - Anexo - Parâmetros ECF- Sub Pasta Dados de Identificação.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Campo** | **Nível** | **Tipo** | **Obrigatório** | **Descrição** | **Origem dos Dados** | **Observação** |
| **ListaEventosEspeciais** | **1** | **Array** | **Não** | **Lista dos eventos especiais da apuração, informados em ordem cronológica** |  | **Quantidade máxima: 5** |
| **Campos obrigatórios se houver ListaEventosEspeciais: Agrupa os dados do evento especial (pode ocorrer mais de uma vez).** | | | | | | |
| IdEvento | 3 | Number | Sim | Número de identificação do evento especial. | Número Sequencial de quantos eventos especiais estiver no período |  |
| DiaEvento | 3 | Number | Sim | Dia do evento especial. | Gerado conforme a Data do Evento Especial  DPARAMSECFFILIAL.DATASITESPECIAL |  |
| TipoEvento | 3 | Number | Sim | Tipo do evento especial, sendo:     **1**: Extinção;     **2**: Fusão;     **3**: Cisão Total;     **4**: Cisão Parcial;     **5**: Incorporação (incorporada);     **6**: Incorporação (incorporadora). | Gerado conforme o Campo situação Especial  DPARAMSECFFILIAL.INDSITESPECIAL |  |

Exemplojstrue
