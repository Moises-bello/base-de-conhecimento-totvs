---
article_id: 360045237814
category: GPE - eSocial - Periódicos
content_hash: ae78d63a58aff61307ae206cc01069d74f67e1c746e2f0c1f1a2c0e4adc79f35
fetched_at: '2026-06-28T22:45:08.766604+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-1210 - A folha de pagamento
  precisa estar fechada para gerar os eventos periódicos S-1200 ou S-1210
type: support-article
updated_at: '2025-07-23T14:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045237814-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-A-folha-de-pagamento-precisa-estar-fechada-para-gerar-os-eventos-peri%C3%B3dicos-S-1200-ou-S-1210
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27473070498455)Tempo aproximado para leitura: **00:02:00min****Dúvida**A folha de pagamento precisa estar fechada para gerar os eventos periódicos S-1200 ou S-1210?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Não é necessário que a folha de pagamento esteja fechada para gerar os eventos S-1200 e S-1210.

Por padrão ao gerar os eventos periódicos o sistema busca informações do **movimento fechado** **(SRD)**, porém ao marcar a opção "**considerar dados do período em aberto**" o sistema também vai buscar registros que estão no **movimento aberto** **(SRC)**.

É muito importante que o usuário tenha **atenção** ao executar a rotina de eventos periódicos no sigagpe, pois caso a **FOLHA esteja aberta,** e a rotina for executada **SEM**a opção "**considerar dados do período em aberto?**" o S-1200 e S-1210 não será gerado ou vai ser gerado sem valores de folha causando erros na apuração dos encargos.   
  
Caminho: SIGAGPE - miscelânea > eSocial > eventos periódicos  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063783073)  
  
**Artigos relacionados:**

* [MP - GPE - eSocial - S-1200 / S-1210 - Como gerar eventos periódicos com a folha aberta (SRC) no sigagpe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044700974-MP-GPE-eSocial-S-1200-S-1210-Como-gerar-eventos-peri%C3%B3dicos-com-a-folha-aberta-SRC-no-sigagpe?source=search)
* [MP - GPE - eSocial - S-1200 / S-1210 - Como gerar eventos periódicos com a folha fechada (SRD) no sigagpe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045208153-MP-GPE-eSocial-S-1200-S-1210-Como-gerar-eventos-peri%C3%B3dicos-com-a-folha-fechada-SRD-no-sigagpe?source=search)

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
