---
article_id: 360036197934
category: RH - Transferência
content_hash: 8f23a30a6b8b2897b3dc6cd45a2219e44548e89c66bc38ac405c929997b96d46
fetched_at: '2026-06-28T22:43:23.462256+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Transferência entre Filiais quando a tabela de
  Verbas - SRV é exclusiva
type: support-article
updated_at: '2025-07-14T12:00:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036197934-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-entre-Filiais-quando-a-tabela-de-Verbas-SRV-%C3%A9-exclusiva
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33449349071511) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como funciona a **transferência entre Filiais** quando a tabela de **Verbas (SRV)** é exclusiva? O sistema leva para o Destino o Acumulado (SRD)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de pessoal - todas as versões  
  
**Solução**A rotina de transferência, ao verificar que a tabela de verbas **é exclusiva**, emitirá uma mensagem informando ao usuário e perguntando se deseja continuar ou não o processo.   
  
**Se selecionar a opção Não**, o sistema abortará e não fará a transferência, **se selecionar Sim**, o sistema levará os dados do funcionário para o destino, **com exceção dos acumulados (SRD)**, onde manterá na origem para futuras conferências.   
  
Isso porque não há uma forma de fazer um De/Para sendo que os códigos referem-se a verbas distintas entre as Filiais. **Assim, após a transferência, qualquer consulta de histórico acumulado anterior a mesma, deve ser feita na Filial origem.**

**Importante**Para que o controle das transferências seja efetuado corretamente, o arquivo de transferências - SRE deve estar no modo de acesso compartilhado entre filiais e também entre empresas, ou seja, deverá ser configurado na SX2 para modo de acesso compartilhado e, além disso, se existir mais de uma empresa, o mesmo arquivo deve ser indicado.

**Saiba Mais**[Manual Transferências](https://tdn.totvs.com/pages/viewpage.action?pageId=815569538)  
[RH - Linha Protheus - GPE - Movimentação de Tabelas em Transferência entre Empresas/Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhucBXVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzIzNzYxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTW92aW1lbnRhJUMzJUE3JUMzJUEzby1kZS1UYWJlbGFzLWVtLVRyYW5zZmVyJUMzJUFBbmNpYS1lbnRyZS1FbXByZXNhcy1GaWxpYWlzBjsIVDoOc2VhcmNoX2lkSSIpNWZiNDFhMjYtNmRmYy00MDFkLTgwOWItNDg2NWUwMjg2OWNiBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJjUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIE1vdmltZW50YcOnw6NvIGRlIFRhYmVsYXMgZW0gVHJhbnNmZXLDqm5jaWEgZW50cmUgRW1wcmVzYXMvRmlsaWFpcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--570ff4fba852a2b6b4b77f4a54a796f485d8f601)  
[RH - Linha Protheus - GPE - Transferência de funcionário, vindo de outro Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413843598743-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-de-funcion%C3%A1rio-vindo-de-outro-Sistema?source=search)
