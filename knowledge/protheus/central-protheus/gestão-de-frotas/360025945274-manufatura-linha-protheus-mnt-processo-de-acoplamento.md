---
article_id: 360025945274
category: Gestão de Frotas
content_hash: eb7971aa5362320057078c9b95330e2feda13a82f58dd17fe904662cb084db84
fetched_at: '2026-06-28T22:42:39.582942+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Processo de Acoplamento
type: support-article
updated_at: '2026-03-10T17:05:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025945274-Manufatura-Linha-Protheus-MNT-Processo-de-Acoplamento
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38938566660247)* Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como funciona o processo de **Acoplamento - T9\_ACOPLA**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas (SIGAGFR) - Todas as versões  
  
**Solução**  
No módulo de **Manutenção de Ativos** é possível acoplar e desacoplar bens ou veículos. Para este processo é necessário estabelecer através do campo **Acoplamento** que o bem ou veículo pode utilizar este conceito.   
Após isso, basta realizar o processo de **Acoplamento/Desacoplamento**através da opção que está presente em **Outras Ações**do **Cadastro de Veículos - MNTA084**.  
Podemos citar como exemplo de **Acoplamento** a adição de uma carreta à um cavalo.  
Na tabela **Cadastro de Veículos - ST9**, o veículo **CA001** e **CA002** são dados como exemplo de**Veículo Pai - Cavalo** e **Veículo Filho - Carreta** respectivamente.  
No Sistema, em **Atualizações / Controle de Oficina / Bens / Veículos - MNTA084**, incluir dois veículos informando o campo **Acoplamento** como **Sim**.  
  
**Acoplamento**

* Após a inclusão do veículo, posicionar sobre o veículo **CA001** e clicar em **Alterar. Em Outras Ações,** clicar sobre **Acoplamento / Desacoplamento**.
* Selecionar o veículo **CA002** no campo **componente** e na opção **Tipo Mov.** informar **Acoplamento.**

**Desacoplamento**

* Após a inclusão do veículo, posicionar sobre o veículo **CA001** e clicar em **Alterar**. Em **Outras Ações**, em seguida clicar sobre **Acoplamento/Desacoplamento.**
* Selecionar o veículo **CA002** no campo **Componente** e na opção **Tipo Mov.** informar **Desacoplamento**.
* Ao término do processo, é possível visualizar a movimentação de saída na estrutura através da rotina de **Estrutura de bens - MNTA090**.

**Importante**  
A opção de **Acoplamento/Desacoplamento** está presente apenas no**MNTA084**.
