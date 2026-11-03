---
content_hash: a9d38c30d3fa7450555b2fd5f263d2257f0b34adc921ce7287e7b3304fcea566
fetched_at: '2026-06-29T00:08:34.930864+00:00'
page_id: '274854159'
product: rm
source: tdn-rm
title: DT Registro Online de Boletos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Registro+Online+de+Boletos
version: 101
---

# Registro Online de Boletos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Cadastros Iniciais:** | *Cadastro de Boletos* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FINANCEIRO01-828 |

## Descrição

A funcionalidade de Registro OnLine de Boletos, tem como objetivo efetuar o registro online junto ao banco do convênio, para os boletos que já foram criados  e não foram registrados no momento da inclusão. Somente os boletos com status de remessa "Não remetido" e com status de boleto "Em aberto" ou "Baixado Parcialmente" poderão ser registrados online.

## Procedimento para Configuração

```
No Serviço Globais, menu Segurança | Perfil, selecione o perfil do usuário e libere a permissão de acesso na funcionalidade de Registro Online de Boletos.
```

 No TOTVS Gestão Financeira, menu Contas a Pagar / Receber | Boletos, selecione os boletos que serão registrados online.

No menu Processos execute a funcionalidade Registro Online de Boletos.

Para ambiente três camadas ao avançar etapa será apresentado as opções de agendamento do processo.

divs
