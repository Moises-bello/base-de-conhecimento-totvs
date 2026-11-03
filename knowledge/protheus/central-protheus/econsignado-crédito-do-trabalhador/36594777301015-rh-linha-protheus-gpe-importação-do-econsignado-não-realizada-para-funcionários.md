---
article_id: 36594777301015
category: eConsignado (Crédito do Trabalhador)
content_hash: 4043b28e2f1472889833e6d8fffca635b150a3dd75fad705569ca42371bfaf7d
fetched_at: '2026-06-28T22:43:07.314320+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Importação do eConsignado não realizada para funcionários
  que possuem mais de 10 contratos
type: support-article
updated_at: '2026-05-20T12:27:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36594777301015-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-eConsignado-n%C3%A3o-realizada-para-funcion%C3%A1rios-que-possuem-mais-de-10-contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36594777294103) Tempo aproximado para leitura: **00:01:15 min**  
  
**Ocorrência**  
Ao tentar realizar a **importação** do arquivo do **eConsignado**, onde existem funcionários com **mais de 10 empréstimos**, o sistema está apresentando **apenas 10 posições** disponíveis na tabela **S154 - Verbas Crédito do Trabalhador**.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12

**Causa**  
Esse incidente ocorre devido a **atualização** **pendente**, para suportar o aumento do número de verbas na tabela **S154**. As versões anteriores ainda têm a limitação das **10 posições** para inclusão, porém com as **atualizações** mais **recentes**, o Sistema permite a inclusão de até **50 verbas**.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique a versão do sistema atualmente em uso.
2. Atualize o ambiente do Protheus para a inclusão de até 20 verbas, conforme links abaixo (selecione apenas o link relacionado a versão do seu Sistema).  
   Versão **12.1.2310**: <https://suporte.totvs.com/portal/p/10098/download?e=1123885> >> **SOMENTE PARA CLIENTES COM GARANTIA ESTENDIDA**  
   Versão **12.1.2410**: <https://suporte.totvs.com/portal/p/10098/download#detail/1170810>  
   Versão **12.1.2510**: <https://suporte.totvs.com/portal/p/10098/download?e=1221795>
3. Acesse a tabela S154 e verifique se as **50 posições** para inclusão das verbas estão disponíveis após a atualização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40582361131671)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40582361135127)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40582389950871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40582361137175)  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Econsignado - Informações e atualizações sobre Credito Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-Econsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-Trabalhador-MP1-292-2025)

[RH - Linha Protheus - GPE - Importação do arquivo Crédito trabalhador mês atual com mais de um contrato- eConsignado MP(1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33072630601751-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-arquivo-Cr%C3%A9dito-trabalhador-m%C3%AAs-atual-com-mais-de-um-contrato-eConsignado-MP-1-292-2025)

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
