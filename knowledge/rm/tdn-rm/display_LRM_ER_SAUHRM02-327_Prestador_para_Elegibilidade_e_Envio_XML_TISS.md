---
content_hash: 010f3379dba4ea57fecb7494da3e9e6ee0e27239b469db7c1c5e85fe317cb2bc
fetched_at: '2026-06-29T00:08:23.204669+00:00'
page_id: '269550984'
product: rm
source: tdn-rm
title: ER_SAUHRM02-327_Prestador_para_Elegibilidade_e_Envio_XML_TISS
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM02-327_Prestador_para_Elegibilidade_e_Envio_XML_TISS
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM02-346 |
| **Requisito** | SAUHRM02-327 | **Subtarefa** | SAUHRM02-456 |
| **País** | ( X  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   

### Objetivo

 *Este documento tem como objetivo especificar o requisito de escolha de prestador para as transações de envio arquivos XML TISS.*

### Definição da Regra de Negócio

**RN001 -**  Criar parâmetro nas condições contratuais,  informando qual o código do prestador que deve ir no arquivo xml. As opções são CPF,CNPJ ou  código na operadora  e não utilizar, o que mantem o restador conforme as regras já existentes.

                    As transações que serão alteradas são: Solicitação de Procedimento, Solicita Status Autorização, Verifica Elegibilidade e Cancela Guia.

**RN002  -**   Criar rotina para retornar  o código do prestador e o tipo (CPF/CNPJ,código na operadora), a ser chamada nas chamadas das rotinas que geram o arquivo xml.

**RN003  -**Relatórios TISS devem ser adaptados para os novos parâmetros.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Condições Contatuais | [Alteração] | Cadastros/ Faturamento / Condições Contratuais | RN001 |
| Atendimento Interno | [Alteração] | Atendimento/Internação/Registro de Informações | RN002 |
| Atendimento Externo | [Alteração] | Atendimento/Pronto Atendimento/Ambulatorio/ Registro de Atendimentos Externos | RN002 |
| Agendamento de Atendimento | [Alteração] | Atendimento/Agendamento/Agenda de Atendimentos | RN002 |
| Gerador de relatórios | [Criação] | Relatórios/ Gerador .NET | RN003 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
