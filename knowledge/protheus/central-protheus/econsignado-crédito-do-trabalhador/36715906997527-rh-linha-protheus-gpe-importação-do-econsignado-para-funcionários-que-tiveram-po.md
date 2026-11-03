---
article_id: 36715906997527
category: eConsignado (Crédito do Trabalhador)
content_hash: ae290ca14137c9cd81b5c20d6525fa68c159196aa043ecb626cb7dd5c142fffb
fetched_at: '2026-06-28T22:43:07.317876+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Importação do eConsignado para funcionários que
  tiveram portabilidade de um empréstimo Consignado
type: support-article
updated_at: '2025-12-03T13:48:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36715906997527-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-eConsignado-para-funcion%C3%A1rios-que-tiveram-portabilidade-de-um-empr%C3%A9stimo-Consignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36715906996375) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
No módulo **GPE**, ao realizar a importação do arquivo do **eConsignado** para funcionários que tiveram **portabilidade** de um **empréstimo Consignado**, o sistema não apaga o empréstimo antigo, resultando em descontos para dois bancos na **folha de pagamento**.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE - Gestão de Pessoal - A partir da versão 12.1.2310

**Causa**  
Esse incidente ocorre, pois o Protheus identifica as informações disponibilizadas pelo Governo através do arquivo de importação e nele não existe nenhum dado que informe esta portabilidade. Desta forma, não é possível incluir esta identificação automaticamente para os usuários do Sistema.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse no GPE **Atualizações > Lançamentos > Conta Corrent**e **Valores Futuros**;
2. Selecione o funcionário e localize o lançamento do desconto do **empréstimo consignado** anterior;
3. Altere seu status para **Suspenso** e salve a alteração.
4. Recalcule a folha de pagamento

Para facilitar a identificação dos funcionários que possuem lançamento de outros empréstimos consignados, gere o relatório dos **Valores Futuros** para confirmar quais funcionários possuem lançamentos ainda **com saldo** em aberto.

**Saiba Mais**

[RH - Linha Protheus - GPE - Impressão de relatório de Valores Futuros GPER570](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052070034-RH-Linha-Protheus-GPE-Impress%C3%A3o-de-relat%C3%B3rio-de-Valores-Futuros-GPER570)

[RH - Linha Protheus - GPE - Como suspender valores lançados na rotina de Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017555452-RH-Linha-Protheus-GPE-Como-suspender-valores-lan%C3%A7ados-na-rotina-de-Valores-Futuros)
