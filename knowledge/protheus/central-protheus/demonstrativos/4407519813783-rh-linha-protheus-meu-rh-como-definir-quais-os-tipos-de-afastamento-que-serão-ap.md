---
article_id: 4407519813783
category: DEMONSTRATIVOS
content_hash: fbf4d11d5b92dbb56a8916b7025fd69c72ea04d72274788cf527bf57b85dabce
fetched_at: '2026-06-28T22:44:38.412221+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como definir quais os tipos de afastamento que
  serão apresentados na rotina Atestado Médico no Meu RH
type: support-article
updated_at: '2026-06-22T19:16:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407519813783-RH-Linha-Protheus-MEU-RH-Como-definir-quais-os-tipos-de-afastamento-que-ser%C3%A3o-apresentados-na-rotina-Atestado-M%C3%A9dico-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24770168262935) Tempo aproximado para leitura: **00:02:00 min****Dúvida**  
Como definir quais os tipos de afastamento que serão apresentados na rotina Atestado Médico no Meu RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Foi disponibilizado o campo "**Perm. Portal?**" (**RCM\_PORTAL**) na tabela Tipos de Ausências (**RCM**).  
  
Por meio desse campo será possível definir quais os tipos de afastamento que serão apresentados na rotina Atestado Médico no Meu RH.   
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Aplicar o último acumulado do RH e atualizar o dicionário executando o **UPDDISTR;**<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO_CONTINUA>   
  
2. Após executar o passo 1, acesse no **SIGAGPE** o menu > Atualizações > Definições de cálculo > Tipos de ausências e acesse como alterar um tipo de ausência e preencha o campo **RCM\_PORTAL** com "Sim" para apresentar no MEU RH ou "Não" para não apresentar no MEU RH.  
![zwbaCFSHSN.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4407519593111)  
  
**Documentação completa: [Tipos de Ausências para o Meu RH](https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=621402583)**  
  
**Saiba Mais**  
**[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH) **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**[para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
