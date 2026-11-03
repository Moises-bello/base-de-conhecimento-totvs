---
content_hash: 516bf9d7e06c271155f95d117288a62c6d1cdac4ec030addbd66ef82b593215b
fetched_at: '2026-06-29T00:11:44.754035+00:00'
page_id: '815583965'
product: rm
source: tdn-rm
title: Exames Pendentes - Fracionamento de Jobs
type: documentation
url: https://tdn.totvs.com/display/LRM/Exames+Pendentes+-+Fracionamento+de+Jobs
version: 12
---

### **Disponível a partir das Versões: 12.1.2302.247, 12.1.2306.196, 12.1.2310.129 ou superiores**

## **ÍNDICE**

1. **Visão Geral**
2. **Pré Requisitos**
3. **Inclusão Fracionamento de JOBS**
4. **Utilização**

**01. VISÃO GERAL**

O fracionamento de Jobs é uma prática que possibilita a execução de um processo de forma distribuída, utilizando múltiplos Jobs (tarefas). O principal propósito dessa abordagem é diminuir o tempo total de execução do processo, além de otimizar a capacidade de processamento dos servidores. Ao dividir o processo em tarefas menores, é possível realizar a execução de forma paralela, resultando em uma conclusão mais rápida e eficiente.

**02. PRÉ REQUISITOS**

Para garantir o funcionamento adequado, é necessário habilitar a utilização do sistema em três camadas.

Maiores informações estão disponíveis no link:  

**03. INCLUSÃO FRACIONAMENTO DE JOBS**

Para usar esse recurso, é necessário que o perfil do usuário esteja vinculado ao processo. Essa configuração pode ser é realizada através do caminho:

*Ambiente => Segurança de Jobs Fracionáveis*

* + **Perfil:**Selecionar o perfil que será utilizado.
    - **Obs.:** Estarão disponíveis para seleção somente os perfis do contexto atual.
  + **Classe de Job:** Processo que está sendo utilizado. Para fracionamento dos exames pendentes a Classe que deverá ser utilizada é a **SmtGerarExamesPendentesProcess.**

**Importante:**

Se a Classe de Job *"SmtGerarExamesPendentesProcess"* não estiver visível na lista, será preciso excluir o Broker e reiniciar o Host.

Quanto aos números de *Frações*, a escolha fica a carga da parametrização realizada. Se, por exemplo, o mínimo for definido como 2, todos os usuários do perfil configurado dividirão o processo em 2 jobs. Essa lógica se aplica até o máximo de frações escolhido.

Maiores informações a **Segurança** **- Fracionamento de Jobs** estão disponívies no link**:**

**04. UTILIZAÇÃO**

Após a execução dos passos mencionados, ao iniciar o processo **Gerar Exames Pendentes**, você será direcionado para a tela de agendamento. Nessa tela, é possível definir a quantidade de partes em que o processo será dividido.

O sistema permite informar essa quantidade com base nos valores mínimo e máximo de frações configurados no módulo de *Segurança - Fracionamento de Jobs.*
