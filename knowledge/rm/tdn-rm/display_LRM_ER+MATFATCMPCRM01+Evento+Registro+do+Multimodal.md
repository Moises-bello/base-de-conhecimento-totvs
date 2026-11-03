---
content_hash: d0e100e5fd1bfa342b8a698c6eaf1b72a10e71963b4a0e5bf9d4fc631a778eea
fetched_at: '2026-06-29T00:08:49.671365+00:00'
page_id: '331853315'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01 Evento Registro do Multimodal
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATFATCMPCRM01+Evento+Registro+do+Multimodal
version: 94
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | MATFATCMPCRM01-2068 | **Subtarefa1** | NA |
| **Chamado/Ticket2** |  | | |
| **País** | Brasil | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## 

## Objetivo

Descrever as alterações necessárias no sistema para que seja possível fazer o envio e consulta do evento Registro do Multimodal.

## 

## Definição da Regra de Negócio

Esse evento é destinado à vinculação das informações dos serviços prestados ao CT-e multimodal.

**Caso seja emitido um CT-e já vinculado ao CT-e multimodal, não é necessário informá-lo por este evento.**

Somente os outros serviços inerentes ao envio de um CT-e multimodal, a saber, coleta, unitização, desunitização, movimentação, armazenagem e entrega de carga ao destinatário, bem como a realização dos serviços correlatos que forem contratados entre a origem e o destino, inclusive os de consolidação e desconsolidação documental de cargas devem ser informados.

O autor desse evento é o emissor do CT-e Multimodal. A mensagem XML do evento será assinada com o certificado digital que tenha o CNPJ base do Emissor do CT-e.

Esse evento exige CT-e Multimodal autorizado.

Visão de Conhecimento de Transporte Eletrônico  
Em Processos | Enviar Evento, deverá ser disponibilizada uma nova opção de evento chamado **Registro do Multimodal**.

Ao acessar esse evento, deverá ser apresentada uma tela em que o usuário deverá informar os seguintes campos:

1. Informações do Documento: campo do tipo caracter, tamanho entre 15 e 1000 caracteres. Campo de preenchimento obrigatório. Deverá ser criada uma consistência para esse campo que não permita a execução do processo caso esse campo não esteja preenchido;
2. Número do Documento: campo do tipo caracter, tamanho entre 1 e 44 caracteres. Campo de preenchimento opcional.

Envio do Evento

Esse evento deve ser enviado conforme leiaute do Schema XML evRegMultimodal\_v9.99.xsd, disponível em <http://www.cte.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=0xlG1bdBass=>. 

Consulta do Evento

Esse evento deverá ser consultado conforme leiaute de Mensagem de Retorno já utilizado para os demais eventos do CT-e.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
