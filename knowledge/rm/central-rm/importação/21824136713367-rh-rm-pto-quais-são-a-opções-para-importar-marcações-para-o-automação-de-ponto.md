---
article_id: 21824136713367
category: Importação
content_hash: 206edab849998d6066eb5868c73eff4d0b54b40fdae8a5a621e4646d965fa58a
fetched_at: '2026-06-28T22:46:33.714343+00:00'
product: rm
section_id: 6045469428631
source: central-rm
title: RH - RM - PTO - Quais são a opções para importar marcações para o Automação
  de Ponto
type: support-article
updated_at: '2025-01-14T13:17:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21824136713367-RH-RM-PTO-Quais-s%C3%A3o-a-op%C3%A7%C3%B5es-para-importar-marca%C3%A7%C3%B5es-para-o-Automa%C3%A7%C3%A3o-de-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21824136693783) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais são as opções para importar as batidas para o Automação de Ponto?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.20  
  
**Solução**

O Automação de Ponto oferece as seguintes opções de importação:

* **Importação do AFD (Arquivo Fonte de Dados) conforme portaria 671:** Este layout valida o CPF e/ou PIS do funcionário.
* **Importação do AFD (Arquivo Fonte de Dados) conforme a portaria 1510:** Este layout valida o PIS do funcionário.
* **Importação através de layout customizado:** Um exemplo de customização seria a validação por chapa.
* **Importação automática de batidas integrado com Suricato (Telemática):** O Suricato é uma plataforma de gestão integrada que oferece recursos como monitoramento gráfico, CFTV, biometria facial, impressão digital, gestão de identidade e controle de acesso.
* **Importação automática de batidas integrado com Clock-In (Carol):** O Clock-In é um aplicativo de registro de ponto eletrônico para tablets que pode ser utilizado em qualquer ambiente, com ou sem conexão com a internet. Este aplicativo é integrado e distribuído pela plataforma Carol.

É **importante** ressaltar que os aplicativos Suricato e Clock-In, que são integrados automaticamente, realizam a **importação diretamente do terminal de coleta/dispositivo** (relógio de ponto, celulares, tablets, Totens, Quiosques, etc.) para o sistema de Automação de Ponto. **As demais opções requerem a extração de um arquivo** em formato .txt do terminal de coleta e a **execução manual do processo de importação** para o sistema de Automação de Ponto. Para obter detalhes sobre cada cadastro e processo de importação, recomendo consultar os documentos a seguir:

* [RH - RM - PTO - Como cadastrar terminal de coleta no Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21862558711191)
* [RH - RM - PTO - Cadastrar layout do terminal de coleta (relógio) no Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000485588)
* [RH - RM - PTO - Como importar as marcações para o Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000486068)
* [RH - RM - PTO - Como agendar o processo para importar as batidas de forma automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014195451)
* [RH - RM - PTO - Tipos de REPs (Registros Eletrônicos de Ponto) de acordo com a Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22760840044183)
* [RH - RM - PTO - Layout AFD portaria 1510 "adaptado" para portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21892016897047)
* [RH - RM - PTO - Relógios de marcação de ponto homologados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000288487)
* [RH - RM - PTO - Como realizar a integração entre o Automação de Ponto x Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5108092531095)
* [RH - RM - PTO - Importação de batidas via API de integração com Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13618422681367)
* [RH - RM - PTO - Como realizar a integração entre o Automação de Ponto x Carol Clockin Importação de Batidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407497605399)
* [RH - RM - PTO - Importação automática de batidas com integração via Clockin (Carol)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427635287319)
* [RH - RM - PTO - Erro ao importar batidas na integração com a Carol/Clock In.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062421874)
* [RH - RM - PTO - Erro ao importar batidas: Não encontrado o funcionário conforme o filtro de seleção e o CPF ou PIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17884073444119)
* [RH - RM - PTO - Ao importar batidas através de processo agendado ocorre o "Erro na execução do processo de batida:"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020657431)

**Saiba Mais:**[Clock In - Carol](https://tdn.totvs.com/display/TCI/Clock+In+Backoffice)[Suricato - Telemática](https://telematica.com.br/solucoes/suricato/)
