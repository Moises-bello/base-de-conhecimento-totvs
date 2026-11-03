---
content_hash: 1482092ac37557bb46ad69f980e98f704b4377204c8960aad66e3e622f07f286
fetched_at: '2026-06-29T00:11:50.569412+00:00'
page_id: '842705365'
product: rm
source: tdn-rm
title: Importação de Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=842705365
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Conferindo a integração**

Dica

Esta rotina foi projetada para ser executada através de um "agendamento do processo", onde o cliente pode escolher o padrão de execução e repetição desejado para o processo.

itensVisão Geral

## **01. VISÃO GERAL**

Este recurso permite a identificação dos registros constantes no cadastro de Centro Custos - Financeiro que não estão inseridos na estrutura de Centro de Custo da Saúde. Após a identificação estes registros são inseridos e disponibilizados para serem utilizados na Unidade de Atendimento.

Esta rotina também identifica os Centros de Custos que estão na estrutura da Saúde e que não estão mais na estrutura Financeira, desativando-os para não serem utilizados na Unidade de Atendimento.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Acesso ao recurso é feito através do menu Utilitários > Outros > Importação de Centro de Custo

Caso o ambiente esteja configurado em duas camadas, a tela com a opção executar será exibida, cliquem em Executar para realizar a processamento da rotina.

Caso o ambiente esteja configurado em N camadas, será exibida a tela de agendamento, com ela será possível configurar a recorrência definida pelo usuário para que a rotina seja executada automaticamente

Atenção

Para saber mais cobre configuração em N Camadas, consultar nossa documentação [Arquitetura N Camadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016141092-Framework-Linha-RM-Frame-Arquitetura-N-Camadas)

O processo é executado, caso esteja em duas camadas, o retorno do processamento será feito após a conclusão da Execução. Caso esteja configurado via agendamento de processo, o mesmo poderá ser consultado através da tela de Jobs.

Conferindo a integração

## **03. Conferindo a Integração**

1 – Acesso ao Centro de Custo Global – Gestão Financeira

2 – Cadastro e manutenção de centro de custo global

3 – Acesso ao recurso de Importação de Centro de Custo – Unidade de Atendimento - Saúde

4 – Acesso e utilização de Centro de Custo pelas Unidades de Atendimento - Saúde
