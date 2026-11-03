---
article_id: 360050645454
category: RH - Benefícios
content_hash: 74151dca1d8892f9a8796e97df569d832e8e30298595a9fb969550bc005e51f7
fetched_at: '2026-06-28T22:44:03.865427+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar o cálculo de Seguro de Vida sobre
  Salário Incorporado (P_SALOUBEN)
type: support-article
updated_at: '2025-12-10T13:46:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050645454-RH-Linha-Protheus-GPE-Como-realizar-o-c%C3%A1lculo-de-Seguro-de-Vida-sobre-Sal%C3%A1rio-Incorporado-P-SALOUBEN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27060784403351) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como realizar o cálculo de Seguro de Vida sobre Salário Incorporado (P\_SALOUBEN)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
Para possibilitar esse cálculo, foi implementado o **mnemônico P\_SALOUBEN**.   
Para configurar o mnemônico acessar em **Atualizações> Definições de Cálculos> Mnemônicos (GPEA300) >** Pesquise pelo mnemônico **P\_SALOUBEN > Alterar**:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27060830586135)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27060784412439)**  
  
Por padrão do sistema o mnemônico é configurado com .F., caso esse mnemônico esteja configurado com **.T.**, **o sistema irá considerar o salário incorporado** do funcionário para o cálculo de todos os benefícios definidos na rotina de Outros Benefícios:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27060784415127)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27060830590487)

Para que seja calculado dessa forma, a configuração do beneficio deve estar configurado para calcular sobre Salário Base.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36911928789911)

**Exemplo**:  
Funcionário possui salário base de 1000,00 e adicional de confiança de 10% incorporado ao salário.  
Cadastro do beneficio configurado para calcular sobre salário base.

**Mnemônico com .F.** - Será considerado 1000,00 para base de cálculo  
**Mnemônico com .T.** - Será considerado 1100,00 para a base de cálculo.  
  
**Obs.:** No exemplo acima para que seja considerado o salário incorporado, a verba de adicional de confiança deve ser configurado com **Incorp Sal = Sim.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36911928795543)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como fazer o cadastro de Outros Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058024473-RH-Linha-Protheus-GPE-Como-fazer-o-cadastro-de-Outros-Benef%C3%ADcios)  
[RH - Linha Protheus - GPE - Relatório de Outros Benefícios em planilha (GPER065)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053377014-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Outros-Benef%C3%ADcios-em-planilha-GPER065)  
[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de Outros Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12234024328599-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-Outros-Benef%C3%ADcios)
