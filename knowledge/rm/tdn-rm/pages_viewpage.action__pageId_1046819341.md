---
content_hash: d8b4cda1a9c45640703c0fbe5bd0ba08b66377995192b3d749181d13ed2e4d1a
fetched_at: '2026-06-29T00:05:51.027934+00:00'
page_id: '1046819341'
product: rm
source: tdn-rm
title: DT Evolução do Painel de Gerenciamento de Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046819341
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Saúde Hospitais e Clinicas |
| Linha de Produto: | Linha RM |
| Segmento: | Saude |
| Módulo: | NEXUS |
| Função: | PROTOCOLOS ASSISTENCIAIS - FORMULÁRIO PEP |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DSAUGHNEXUS-731 |

## **02. SITUAÇÃO/REQUISITO**

**Situação**: O sistema atual apresenta um painel de gerenciamento de risco que exibe apenas alertas de risco gerados, como protocolos e scores, sem fornecer informações sobre o gerenciamento desses riscos pela instituição.

**Problema**: Gestores clínicos e profissionais assistenciais necessitam de uma visão consolidada que permita o acompanhamento efetivo da resposta assistencial e a priorização de ações, visando a melhoria da segurança do paciente e suporte à gestão clínica.

**Objetivo**: Implementar um Painel de Gerenciamento de Risco com dois subpainéis: Alertas, que mantém a funcionalidade atual, e Protocolos, que fornece uma visão operacional-gerencial dos protocolos assistenciais, permitindo a visualização do status e ações necessárias, respeitando as permissões de acesso.

## **03. SOLUÇÃO**

**História do Usuário**

Como gestor clínico ou profissional assistencial, é necessário visualizar alertas de risco e o gerenciamento desses riscos em um único painel. Isso proporciona acompanhamento efetivo, priorização de ações e melhora na segurança do paciente.

Estruturação da Funcionalidade – Gerenciamento de Risco

O novo painel de Gerenciamento de Risco terá dois subpainéis. O subpainel de Alertas retém seu funcionamento atual, exibindo alertas de protocolos e scores com filtros e ordenações existentes. O subpainel de Protocolos oferece uma visão gerencial, mostrando o status de protocolos assistenciais, com informações sobre pacientes e tipos de protocolo. As ações no subpainel são de navegação, não permitindo execução direta, mas possibilitando abertura do prontuário do paciente.

**Critérios de Aceite**

Os dois subpainéis devem ser implementados conforme descrito, mantendo a funcionalidade atual e respeitando as regras de permissão por perfil.

## **04. DEMAIS INFORMAÇÕES**

<Não se aplica>

## **05. ASSUNTOS RELACIONADOS**

        Não se aplica
