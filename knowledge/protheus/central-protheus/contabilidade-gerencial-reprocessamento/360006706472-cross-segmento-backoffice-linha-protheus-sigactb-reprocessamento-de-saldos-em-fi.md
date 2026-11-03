---
article_id: 360006706472
category: Contabilidade Gerencial - Reprocessamento
content_hash: feb097439ad25d689e0243d6ce23016098a8f700072abc029aea4beee693f8d5
fetched_at: '2026-06-28T22:40:41.991976+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reprocessamento de Saldos
  em Fila (CTBA193)
type: support-article
updated_at: '2025-11-19T13:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006706472-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reprocessamento-de-Saldos-em-Fila-CTBA193
---

**Dúvida**Como utilizar o Reprocessamento de Saldos em Fila (CTBA193)?  
  
  
**Ambiente** Cross Segmento - Backoffice Linha Protheus  -  Contabilidade Gerencial - Versão 12  
  
  
**Solução**Para o sistema realizar o processamento de saldo em fila o usuário deve apenas configurar o schedule CTBA193.

Para isto, realize os seguintes passos:

* No módulo configurações acessar Ambiente > Schedule > Schedule.
* Clicar no ícone da pasta Schedule
* Clicar no botão “Iniciar todos os serviços”
* Clicar na pasta “Agent” > Cadastro
* Clicar Adicionar agents padrão
* Clicar na Pasta Agendamentos
* Selecionar a opção Incluir
* No campo rotina, digite **CTBA193**
* No campo Ambiente, digite o mesmo ambiente de **PRODUÇÃO** (EX. ENVIRONMENT, PRODUCAO)
* Selecione as empresas e Filiais para processamento
* Selecione como módulo o 34 – Contabilidade Gerencial.
* Clique no botão recorrência para configurar a periodicidade que o sistema irá acionar o agendamento

A partir da configuração do agendamento, toda **inclusão**de lançamento contábil, via rotinas manuais (CTBA101,CTBA102 e CTBA103) ou integrações contábeis (CTBA105), não irão gerar saldo online e sim gravará a chave do lançamento na tabela de fila para ser processado em segundo plano pelo agendamento configurado.

**ATENÇÃO: O ambiente de configuração deve ser o mesmo ambiente da PRODUÇÃO, caso seja diferente, a rotina não irá funcionar para versões anteriores a P12.1.33.**  
  
Siga as orientações descritas no link abaixo:  
<http://tdn.totvs.com/display/public/PROT/CTB113_REPROCESSAMENTO_SALDOS_POR_FILA_P12>
