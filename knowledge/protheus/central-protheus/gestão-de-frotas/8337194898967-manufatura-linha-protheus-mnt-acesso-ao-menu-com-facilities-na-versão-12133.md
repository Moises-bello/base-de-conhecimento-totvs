---
article_id: 8337194898967
category: Gestão de Frotas
content_hash: 497ce594ef89b5a27610f814fbc216d1e979980700e785a589b3b5408d935dbe
fetched_at: '2026-06-28T22:42:39.270032+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Acesso ao menu com Facilities na versão
  12.1.33
type: support-article
updated_at: '2023-08-08T21:12:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8337194898967-Manufatura-Linha-Protheus-MNT-Acesso-ao-menu-com-Facilities-na-vers%C3%A3o-12-1-33
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16624178789143)* Tempo aproximado para leitura: **00:02:10 min  
  
Dúvida**Como acessar as rotinas do **Facilities** a partir da *release* **12.1.33** pelo módulo do **Manutenção de Ativos** e **Gestão de Frotas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - A partir da versão 12.1.33  
  
**Solução**Realize o ajuste do **Menu** via **SIGACFG - Configurador**, adicionando as rotinas do **Facilities** conforme passo-a-passo abaixo:

* Em **Ambientes > Cadastros > Menus** selecione o módulo de **Manutenção de ativos**.

![image2022-8-17_16-26-14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8336665466775)

* Procure pela opção de **Solicitação Serv.** no **Menu** e remova as opções **Executantes S.S - MNTA300**, **Distribuição de S.S. - MNTA295**, **Distribuição Lote - MNTA315** e **Fechamento - MNTA290**.

![image2022-8-17_17-3-21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8336717035927)

* Após a remoção das rotinas, o agrupador de **Solicitação Serv** deverá ficar com essa estrutura:

![image2022-8-17_17-9-58.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8336722369943)

* Realize a inclusão dos itens da tabela abaixo no agrupador **Solicitação Serv.** do **Menu**:  
    

  |  |  |  |
  | --- | --- | --- |
  | **Descrição** | **Programa** | **Módulo** |
  | **Funcionários** | **MNTA020** | **Manutenção de Ativos** |
  | **Diagnósticos** | **MNTA299** | **Manutenção de Ativos** |
  | **Criticidade** | **MNTA293** | **Manutenção de Ativos** |
  | **Critérios de Distribuição** | **MNTA298** | **Manutenção de Ativos** |
  | **Definições de Atendimento** | **MNTA294** | **Manutenção de Ativos** |
  | **Distribuição** | **MNTA296** | **Manutenção de Ativos** |
  | **Atendimento** | **MNTA291** | **Manutenção de Ativos** |
  | **Grupo de Perguntas** | **MNTA306** | **Manutenção de Ativos** |
  | **Questionário de Satisfação** | **MNTA307** | **Manutenção de Ativos** |
  | **Relação Executante/Workflow** | **MNTW030** | **Manutenção de Ativos** |
* Após a inclusão dos cadastros relacionados a **S.S. - Solicitação de Serviço**, procure em **Consultas** o agrupador **Solicitações** e adicione os itens da tabela abaixo:  
    

  |  |  |  |
  | --- | --- | --- |
  | **Descrição** | **Programa** | **Módulo** |
  | **Nivelamento de MDO** | **MNTC815** | **Manutenção de Ativos** |
  | **Consulta S.S** | **MNTC286** | **Manutenção de Ativos** |
* Após a inclusão dos cadastros e consultas relacionados a **S.S.**, procure em **Miscelânea** o agrupador **Sistema** e adicione o item da tabela abaixo:  
    

  |  |  |  |
  | --- | --- | --- |
  | **Descrição** | **Programa** | **Módulo** |
  | **Complemento de Usuário** | **MNTA909** | **Manutenção de Ativos** |
* Após realizar as alterações supracitadas, basta gerar o **Menu**.

![image2022-8-17_19-17-55.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8336988538135)

* Selecionar a opção **Sim**

![image2022-8-17_19-18-4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8336983609367)
