---
content_hash: 8d612f66fadfbe34a8ebe8d5b40db51aef24fbe2cbce764563485d440c674176
fetched_at: '2026-06-29T00:06:13.953942+00:00'
page_id: '208348728'
product: rm
source: tdn-rm
title: ER_PCREQ-7808_Unidade de Medida - UnitOfMeasure
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7808_Unidade+de+Medida+-+UnitOfMeasure
version: 129
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Estoque |
| **Segmento Executor** | TOTVS Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-7808 | **Subtarefa1** | PDR\_CP\_MOV008-47 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Unidade de Medida com o PDV Protheus, viabilizando assim o CRUD completo do cadastro por envio de mensagem de integração.

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração do cadastro de Unidade de Medida (UnitOfMeasure), estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito.

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Unidades de Medida | Inclusão/Alteração/Exclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Estoque, Compras e Faturamento \ Mais\ Tabelas Auxiliares \ Unidade | - |

**Restrições e Pontos de atenção:**

* Visto que a base Protheus possui carga de unidades de medida padrões, que obrigatoriamente constam na base de dados, deve-se efetuar o cadastro destas unidades no RM respeitando o mesmo código do Protheus para viabilizar a integração de registros que utilizem estas como parâmetro. A lista de unidades que existem no Protheus e devem ser cadastradas no RM com o mesmo código de descrição são:

  | Código | Descrição |
  | --- | --- |
  | AR | ARROBA |
  | BD | BALDE |
  | CC | CENTIMETRO CUBICO |
  | CM | CENTIMETRO |
  | CT | CENTO |
  | CX | CAIXA |
  | DM | DECIMETRO |
  | DZ | DUZIA |
  | FL | FOLHAS |
  | FT | PES |
  | G | GRAMA |
  | GL | GALAO |
  | GZ | GROZA |
  | HR | HORA |
  | JG | JOGO |
  | KG | QUILOGRAMA |
  | KT | KIT |
  | L | LITRO |
  | LB | LIBRA |
  | LT | LATA |
  | M2 | METRO QUADRADO |
  | M3 | METRO CUBICO |
  | ML | MILILITRO |
  | MM | MILIMETRO |
  | MT | METRO |
  | OZ | ONCA |
  | P | PAR |
  | PC | PECA |
  | PL | POLEGADAS |
  | TL | TONELADA LIQUIDA |
  | UN | UNIDADE |
  | YD | JARDA |
* O Protheus irá efetuar a consistência do tamanho do campo Código da Unidade com o tamanho recebido na mensagem.
  + Caso o usuário parametrizar o dicionário de dados do Protheus para gerar automaticamente o código da unidade, a consistência referente ao tamanho do campo código não será realizada.
  + Caso o tamanho do campo código seja maior do que o permitido no Protheus será apresentada mensagem de consistência ao integrar o registro, deixando ao usuário as opções de contorno abaixo.
    1. Efetuar manualmente o cadastramento de unidades de medida com código com tamanho válido e efetuar o relacionamento com o código do RM na base do Protheus e posteriormente efetuar a carga para que todos os parâmetros no Protheus sejam alterados conforme a base RM (mandatária).
       1. Caso o cliente não utilize as unidades de medida com código de tamanho maior que o permitido em produtos integrados, o mesmo pode somente efetuar customização nas fórmulas visuais de gatilho para não enviar estas ao Protheus.
    2. Configurar o Protheus para gerar código da unidade automático, conforme o primeiro item deste sessão.
       1. Esta opção não gera problemas de usabilidade pois no Protheus o usuário não seleciona a unidade de medida, mas o código que aparecerá no cupom fiscal será o gerado automaticamente.

**Tabelas Utilizadas**

* TUND - Unidades

**Entidades de Integração**

* DataServer envolvido
  + EstUndData
* Transformação
  + Id: UnitOfMeasure
  + Versão: 2.000
* Fluxo da mensagem
  + Saída
* Tipo de Envio:
  + Síncrono.
* Fórmula Visual
  + 04\_PDV\_UnidadeDeMedida.TotvsWF
  + 04.Sincronização de Unidade de Medida - PDV: fórmula visual para carga de dados.

**Gatilhos de Integração**

Foram disponibilizadas as duas fórmulas visuais de gatilho listadas no item acima, ficando a cargo do cliente ou implantador a customização das mesmas caso não tenha interesse de integrar todas as unidades de medida ao Protheus.

Exemplo de filtro de gatilho: "Somente enviar Unidades de Medida"

Expressão na Fórmula Visual de gatilho: " this.Fields["CODUND"].AsString.Length <= 2 "

Filtro na Consulta SQL da Fórmula Visual de Carga: "... AND LEN(CODUND) <=2 "

## Fluxo do Processo

## Mapeamento dos campos

* **Mensagem UnitOfMeasure 2.000**

 

| **Mensagem Padrão** | **Descrição** | **RM** | | |
| --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Observação** |
| **Code** | Código Unidade. Medida | TUND | CODUND | São selecionados os 6 primeiros caracteres |
| **InternalId** | Chave da Entidade | TUND | CODUND |  |
| **Description** | Descrição Unidade Medida | TUND | DESCRICAO |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
