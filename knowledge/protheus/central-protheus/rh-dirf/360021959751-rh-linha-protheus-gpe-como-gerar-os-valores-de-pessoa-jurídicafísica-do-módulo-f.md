---
article_id: 360021959751
category: RH – DIRF
content_hash: 8216b57cec0273c7a19926a913dbc597a5523705cc74e78c86298ae85dc420fc
fetched_at: '2026-06-28T22:44:06.891483+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar os valores de Pessoa Jurídica/Física
  do módulo Financeiro na DIRF
type: support-article
updated_at: '2025-08-18T14:24:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021959751-RH-Linha-Protheus-GPE-Como-gerar-os-valores-de-Pessoa-Jur%C3%ADdica-F%C3%ADsica-do-m%C3%B3dulo-Financeiro-na-DIRF
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34261795797271)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como gerar os valores de Pessoa Jurídica/Física do módulo Financeiro para a DIRF no Gestão de Pessoal?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Primeiramente se faz necessário gerar os dados para DIRF para o GPE através do módulo Financeiro pela rotina FINA401.   
Para informações de como executar, segue *link* de apoio:   
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA401 - Como gerar os dados do Financeiro para a DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021559532-MP-SIGAFIN-FINA401-Como-gerar-os-dados-do-Financeiro-para-a-DIRF)

Após gerar as informações do financeiro, os valores alimentarão a rotina Manutenção do Arquivo (GPEM560). Lembrando que os valores e informações de dados como CNPJ, Nome, entre outros serão de acordo com o que foi gerado do Financeiro. Então caso esteja errado, será necessário verificar no módulo de origem.  
  
Após gerar os dados para a rotina Manutenção arquivo, as informações podem ser geradas no Arquivo Magnético (GPE590).  
  
**Saiba Mais**  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF?page=2#articles)
