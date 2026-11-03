---
content_hash: 940317ee6d249b77b168401bc6dfad85a576857dbcbdcc9801857e120c2beb3d
fetched_at: '2026-06-29T00:08:25.784473+00:00'
page_id: '271155761'
product: rm
source: tdn-rm
title: ER SAUHRM02-332 Histórico de alterações dos laudos de imagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271155761
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar RM | **Módulo** | Unidade de Diagnóstico |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM1** | SAUHRM02-481 |
| **Requisito1** | SAUHRM02-332 | **Subtarefa1** | SAUHRM02-505 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 O objetivo desta implementação é manter e exibir todos os históricos de alterações dos laudos de exames de imagem do sistema.

### (Obrigatório)

## Definição da Regra de Negócio

**RN01: Criação do histórico do Laudo**

Para toda conclusão do laudo, o sistema deve gravar o laudo concluído. Desta maneira, todas as alterações serão salvas na base de dados. Os laudos serão salvos somente neste status por ser o que retrata uma confirmação do profissional que está fazendo.

Será criado a tabela SZPEDEXAMERESULTMODLOG, para gravar as alterações nos laudos.

**RN02: Exibição do histórico**

Será incluído o botão com o rótulo "Histórico" e explicação "Histórico de alterações do laudo", na barra de funcionalidades da tela principal do Controle de Pedido de exames.

Ao clicar no botão, será exibida uma grid com o histórico dos laudos. Para se visualizar um laudo em específico, deve-se dar um duplo clique na linha correspondente.

O conteúdo do laudo será exibido num formulário sem que se possa realizar alterações e inclusões. O mesmo não é exibido em formato de relatório para se evitar a impressão de laudos que não são válidos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Conclusão do Laudo | [Alteração] | [Unidades Diagnóstico -> Controle de Pedido de Exames] | RN01 |
| Exibição do Histórico de alterações do Ludo | [Criação] | [Unidades Diagnóstico -> Controle de Pedido de Exames] | RN02 |

***Tabelas Utilizadas***

* SZPEDEXAMERESULTMODLOG *–* Histórico de alterações dos laudos
* *SZPEDEXAMERESULTMOD -* Laudo médico do exame

### Opcional

## Protótipo de Tela

**Botão com o Histórico**

**Histórico**

**Detalhe**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
