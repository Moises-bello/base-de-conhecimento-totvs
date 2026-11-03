---
content_hash: 898c3a1b298a74400483eec0503d9b04ef8018360999e00e5f08bc7e932291b1
fetched_at: '2026-06-29T00:08:47.041824+00:00'
page_id: '317322765'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01-1305 Tratamento do CT-e/CT-e OS de Anulação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317322765
version: 101
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** | MATFATCMPCRM01-1305 |
| **Requisito/Story/Issue1** | MATFATCMPCRM01-2021 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Com a mudança do leiaute do CT-e 2.0 para 3.0, foi criado um novo evento chamado de Prestação de Serviço em Desacordo. Este evento é emitido pelo tomador do CT-e e dessa forma, o emitente é quem deverá emitir um CT-e de Anulação (entrada) e posteriormente um CT-e de Substituição (saída).

Serão necessários alguns ajustes no sistema para permitir o envio de CT-e de entrada e algumas melhorias de usabilidade.

## 

## Definição da Regra de Negócio

Parâmetros - Tipo de Movimento

- Nos tipos de movimento de entrada (1.x.xx), na etapa Fis - Conhecimento de Transporte, no ComboBox **Tipo de Operação do Conhecimento de Transporte** (TITMTMV.USARCTRC), além das opções já existentes, devem ser apresentadas as opções "Emitir CT-e" e "Emitir CT-e OS".

- Nos tipos de movimento de entrada (1.x.xx), na etapa Fis - Conhecimento de Transporte, quando o **Tipo de Operação do Conhecimento de Transporte** (TITMTMV.USARCTRC) for igual a "Emitir CT-e" ou "Emitir CT-e OS", deve ser apresentado o ComboBox **Modal**(TTMVEXT.MODAL), conforme apresentado nos tipos de movimento de saída (2.x.xx).

Tela de Edição do Movimento  
- Quando o parâmetro **Tipo de Operação do Conhecimento de Transporte** (TITMTMV.USARCTRC) do tipo de movimento for igual a "Emitir CT-e" ou "Emitir CT-e OS", em Transporte | Identificação, no ComboBox **Tipo CT-e**, alterar o nome da opção "Anulação de Valores" para "Anulação". Isso se faz necessário porque a anulação pode ser de valores ou para alteração de tomador do CT-e. As demais opções se mantêm inalteradas.

- Quando o parâmetro **Tipo de Operação do Conhecimento de Transporte** (TITMTMV.USARCTRC) do tipo de movimento for igual a "Emitir CT-e OS", em Transporte | Identificação, deverá ser criado o ComboBox **Tipo do Serviço** que deverá apresentar as mesmas opções que são apresentadas no parâmetro **Tipo do CT-e** **OS** (TTMVEXT.TIPOSERVICOCTEOS) do tipo de movimento. Esse ComboBox apresentará por default a opção informada no parâmetro **Tipo do CT-e****OS**  (TTMVEXT.TIPOSERVICOCTEOS) do tipo de movimento, permitindo a edição pelo usuário.

**Obs.:** Tratar todos os pontos do sistema que faziam verificação do parâmetro **Tipo do CT-e** **OS** (TTMVEXT.TIPOSERVICOCTEOS) do tipo de movimento para que verifiquem a opção informada no campo **Tipo do Serviço** do movimento.

Envio do CT-e  
Não houve alteração na rotina de envio do CT-e de anulação.

**Tabelas Utilizadas**

* TMOVTRANSP - Dados de Transporte
* TITMTMV - Tipos de Movimento - Complemento
* TTMVEXT - Tipos de movimento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
