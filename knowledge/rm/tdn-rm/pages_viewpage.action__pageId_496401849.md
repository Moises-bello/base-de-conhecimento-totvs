---
content_hash: 9b3c186726df8b208b10c12b4fb88a99fe699389a0ca3601d72d71ac6d0d379a
fetched_at: '2026-06-29T00:10:22.465825+00:00'
page_id: '496401849'
product: rm
source: tdn-rm
title: Gerar Movimento com Número da Prefeitura Automático (Job)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496401849
version: 14
---

Conteúdo

## **01. Introdução**

A **Geração Automática de Movimentos com Número da Prefeitura** é um processo destinado a otimizar a criação de movimentos (códigos `2.2.xx`) vinculados à NFS-e (Nota Fiscal de Serviço Eletrônica), especialmente para emissores de alto volume. Em vez de executar manualmente para cada registro, o processo pode ser **agendado** para rodar em horários de baixa demanda do sistema, evitando sobrecarga na rede e conflitos com usuários ativos.

> **Observação:** Este recurso de agendamento está disponível apenas em [Ambiente de Três Camadas](http://tdn.totvs.com/pages/viewpage.action?pageId=273982231) e requer pré-configuração do [Job Server](http://tdn.totvs.com/pages/viewpage.action?pageId=63277426).

## **02. Pré-requisitos**

Antes de iniciar, verifique se:

* O **Job Server** está habilitado e configurado corretamente.
* O sistema RM está operando em **Ambiente de Três Camadas**.
* O horário de agendamento escolhido **não coincida com picos de uso** (ex.: madrugada ou finais de semana).
* Todas as NFS-e já foram **enviadas e autorizadas** pela prefeitura.

## **03. Passo a Passo para Agendamento**

### **03.1. Preparação Inicial**

1. Acesse a **visão de NFS-e** no sistema RM.
2. **Envie todas as NFS-e pendentes** para autorização.
3. **Crie um filtro** para selecionar apenas as NFS-e que exigem geração do movimento:
   * *Dica:* Se não aplicar um filtro, o processo será executado para **todas as NFS-e autorizadas** com *Tipo de Movimento* parametrizado para `2.2.xx`.

### **03.2. Configuração do Agendamento**

1. Acesse: **Processos > Gerar Movimento com Número da Prefeitura Automático (JOB)**.
2. No *wizard* exibido:
   * Clique em **Opções** (canto inferior esquerdo).
   * **Desmarque** a opção *Aguardar Execução do Processo*.
   * Clique em **Avançar**.
3. Na tela seguinte:
   * Defina **Data e Hora** do agendamento (ex.: `02:00h`).
   * Clique em **Executar** para confirmar.

### **03.3. Fracionamento**

Este processo pode operar com o fracionamento de Jobs para garantir uma melhor utilização dos recursos de hardware e oferecer uma execução mais rápida. Se o fracionamento não estiver habilitado o processo gera apenas 1000 movimentos a cada execução.

Para habilitar o fracionamento para este processo faça o cadastro de  para classe de job "FisNFSeGerarMovimentoData".

### **03.4. Resultado**

* Os movimentos `2.2.xx` serão gerados **apenas no horário agendado**.
* O sistema **não bloqueará** a interface do usuário durante a execução.

## **04. Observações Importantes**

* **Agendamento sem seleção prévia de registros:** Recomenda-se **não selecionar NFS-e específicas** ao criar o *Job*. Assim, o processo será executado automaticamente para **todas as novas NFS-e autorizadas** no horário agendado, sem intervenção manual.
* **Quando usar o processo normal:** Se houver necessidade **imediata** de geração de movimentos, execute o processo  manualmente (sem agendamento).
* **Horário ideal:** Agende sempre para períodos de **baixa atividade**, garantindo desempenho do sistema e ausência de usuários logados.

## **05. Como Verificar o Resultado**

1. Acesse: **Ambiente > Gerenciamento de Jobs**.
2. Utilize um **filtro personalizado** para localizar seu *Job* (ex.: nome do processo ou data).
3. Clique em **Editar** e analise o **log de execução** para confirmar:
   * Sucesso: Movimentos `2.2.xx` criados conforme esperado.
   * Erros: Identifique inconsistências nas NFS-e não processadas (ex.: notas não autorizadas).
