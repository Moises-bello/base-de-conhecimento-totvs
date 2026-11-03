---
article_id: 27151404432791
category: Rental by ItUp Business
content_hash: e6609d0f06cc28b3562618c8c63f2558914aa877b1c548f4efab4a80d3282646
fetched_at: '2026-06-28T22:36:20.611159+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Emissão de Contrato Sem Definição
  de Equipamento (BEM) no Momento da Criação
type: support-article
updated_at: '2026-04-09T12:58:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27151404432791-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Emiss%C3%A3o-de-Contrato-Sem-Defini%C3%A7%C3%A3o-de-Equipamento-BEM-no-Momento-da-Cria%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27151419839639) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como efetuar a emissão de Contrato Sem Definição de Equipamento (BEM) no Momento da Criação.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**

O parâmetro **MV\_LOCX305** permite que você crie contratos sem precisar informar o equipamento de imediato, deixando essa tarefa para a rotina **LOCA059** **Apontador de AS**, onde o equipamento deve ser informado antes de aceitar o serviço.

#### **O que acontece quando o parâmetro está ativado (S)?**

* **Criação ágil:** Você pode criar contratos de locação sem informar o equipamento na hora.
* **Vinculação posterior:** O equipamento pode ser associado mais tarde, durante a rotina de apontamento de AS.

#### **O que acontece quando o parâmetro está desativado (N)?**

* **Exigência de informação:** O sistema exigirá que você informe o equipamento no momento da criação do contrato. Não será possível prosseguir sem essa informação.

### Cenário de Uso

Esse parâmetro é útil em situações em que você precisa criar contratos rapidamente, mas o equipamento ainda não foi definido ou não está disponível. Ele oferece flexibilidade, permitindo que o apontador de AS faça a alocação do equipamento no momento apropriado, sem atrasar a criação do contrato.

### Configuração do Parâmetro

* **Chave:** MV\_LOCX305
* **Tipo:** Caractere
* **Valores possíveis:**
* **MV\_LOCX305 = 'S':**
  + Ao gerar um contrato de locação, o sistema não pedirá o equipamento imediatamente. No apontador de serviços, o equipamento será obrigatório para finalizar o aceite.
* **MV\_LOCX305 = 'N':**
  + O sistema exigirá que você informe o equipamento durante a criação do contrato.
