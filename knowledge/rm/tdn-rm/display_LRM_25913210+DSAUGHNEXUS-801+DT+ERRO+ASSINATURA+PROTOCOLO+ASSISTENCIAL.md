---
content_hash: 185c2583c86f7f7082dc6be48aaa1e6b2c8772899d246d555e20e27a54fbcfa6
fetched_at: '2026-06-29T00:05:51.081709+00:00'
page_id: '1046836857'
product: rm
source: tdn-rm
title: 25913210 DSAUGHNEXUS-801 DT ERRO ASSINATURA PROTOCOLO ASSISTENCIAL
type: documentation
url: https://tdn.totvs.com/display/LRM/25913210+DSAUGHNEXUS-801+DT+ERRO+ASSINATURA+PROTOCOLO+ASSISTENCIAL
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Saúde Hospitais e Clinicas |
| Linha de Produto: |  |
| Segmento: | Saude |
| Módulo: | PRONTUARIO ELETRÔNICO DO PACIENTE |
| Função: | PROTOCOLO TEV |
| Ticket: | 25913210 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DSAUGHNEXUS-801 |

## **02. SITUAÇÃO/REQUISITO**

\*\*Situação:\*\* A tela de Protocolo Assistencial deve exibir um pop-up para o preenchimento do PIN ao final de cada etapa, garantindo que a assinatura seja executada corretamente. A validação do PIN já ocorre em outras telas que o usuário acessa.

\*\*Problema:\*\* A rotina de validação e exibição da modal de PIN não está sendo acionada na tela de Protocolo Assistencial, resultando em erros de assinatura. O comportamento inconsistente entre telas compromete a experiência do usuário e a segurança do sistema.

\*\*Objetivo:\*\* Ajustar a validação para que a modal de PIN seja aberta corretamente na tela de Protocolo Assistencial sempre que necessário, assegurando a execução adequada da assinatura, o cumprimento das regras de segurança e a consistência com as demais telas do sistema.

## **03. SOLUÇÃO**

Diagnóstico: A causa raiz do problema é a ausência de acionamento da rotina de validação do PIN na tela de Protocolo Assistencial.

Fluxo esperado: O usuário deve ser solicitado a inserir o PIN ao final de cada etapa, garantindo a assinatura correta.

Fluxo atual: A modal de PIN não aparece, resultando em falha na assinatura.

Proposta de correção: Implementar a chamada da rotina de validação do PIN no final de cada etapa do Protocolo Assistencial.

Ajustes no front-end: Garantir a exibição do pop-up de PIN de acordo com o fluxo de interação do usuário.

Ajustes no back-end: Verificar e integrar a lógica de validação de PIN com a arquitetura do Protocolo Assistencial.

Regras de negócio: Respeitar as diretrizes de segurança e assegurar a consistência na validação do PIN.

Tratamento de sessão: Manter o estado da sessão do PIN durante a navegação no sistema.

Estratégia de regressão: Implementar testes automatizados para verificar a integridade do fluxo após modificações.

Sugestão de testes: Criar testes unitários para a validação do PIN e testes integrados para o fluxo na tela de Protocolo Assistencial.

## **04. DEMAIS INFORMAÇÕES**

<Não se aplica>

## **05. ASSUNTOS RELACIONADOS**

        Não se aplica
