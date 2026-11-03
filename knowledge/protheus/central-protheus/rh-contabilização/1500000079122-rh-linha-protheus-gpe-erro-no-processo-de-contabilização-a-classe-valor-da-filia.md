---
article_id: 1500000079122
category: RH - Contabilização
content_hash: 36e70bd1a20fde445e14adf0e04fbe0989af51e408f2325ffdc89b9863f21c31
fetched_at: '2026-06-28T22:43:46.115927+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro no processo de Contabilização - A Classe
  Valor da Filial não foi encontrado no: CTH'
type: support-article
updated_at: '2025-07-30T02:22:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000079122-RH-Linha-Protheus-GPE-Erro-no-processo-de-Contabiliza%C3%A7%C3%A3o-A-Classe-Valor-da-Filial-n%C3%A3o-foi-encontrado-no-CTH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33810952438295) Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**Erro no processo de Contabilização - A Classe Valor da Filial não foi encontrado no: CTH  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois uma ou mais verbas não estão gerando a informação nas colunas **Cl Vlr Deb** e/ou **Cl Vlr Cred** da **Contabilização - GPEM110**, esta informação é gerada pelo **Lançamento Padrão - CTBA080** atribuído a verba no campo **Lcto. Padrão (RV\_LCTOP)** do cadastro de **Verbas - GPEA040**.

**Solução**Erro apresentado:  **![log_CLASSE_VALOR.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101168933)**

Para solucionar essa ocorrência siga os procedimentos:   
  
1- Identifique na tela de dados da contabilização os lançamentos que não estão gravando a informação de Classe Valor Débito e/ou Classe Valor Crédito, no print abaixo é possível identificar os lançamentos sem esse conteúdo.  
![contabiliza__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360098951834)  
  
2 - Verifique a parametrização dos campos **Cl Vlr Deb** e/ou **Cl Vlr Crd** na rotina **Lançamento Padrão** das verbas que estão apresentando este problema, no exemplo abaixo o motivo foi ausência de informação.  
Acessar: **Atualizações** -> **Cadastros** -> **Lançamento Padrão**: na aba **Entidades** validar o conteúdo e ajustar.  
![lan_amento_padrao_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000077641)**Obs.**: No cadastro de Verbas também é possível verificar o conteúdo destes campos, mas o ajuste deve ser realizado diretamente na rotina **Lançamento Padrão**.  
  
Outro situação que pode provocar esse erro é a ausência de conteúdo no campo **RD\_CLVL** da tabela **SRD - Acumulados,** este campo é preenchido na execução do cálculos **Por Roteiros - GPEM020** ou **Cálculo Múltiplos - GPEM020A,** a rotina coleta a informação do campo **Classe Valor (RA\_CLVL)** do cadastro de **Funcionários - GPEA010  
![funcionarios.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000077881)**  
3 - Efetue a **Contabilização - GPEM110** novamente e valide se a rotina passou a apresentar conteúdo para as colunas **Cl Vlr Deb** e/ou **Cl Vlr Cred**.  
Acessar: **Miscelânea** -> **Fechamentos** -> **Contabilização**  
![contabiliza__o_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000078142)
