---
article_id: 15793189382935
category: MDT - PCMSO
content_hash: 165bf9a0db47bb7483f6fa94837ec6240c8346a99eaeda71b212af0c48f40fe6
fetched_at: '2026-06-28T22:44:28.358521+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Como carregar informação no campo TUSS (Terminologia
  Unificada da Saúde) do cadastro de exames?
type: support-article
updated_at: '2025-09-03T14:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15793189382935-RH-Linha-Protheus-MDT-Como-carregar-informa%C3%A7%C3%A3o-no-campo-TUSS-Terminologia-Unificada-da-Sa%C3%BAde-do-cadastro-de-exames
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15793194507159) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como carregar informação no campo TUSS (Terminologia Unificada da Saúde) do cadastro de exames?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**No cadastro de Exames (MDTA020) no menu Atualizações - PCMSO - Exames, tem o campo **"TUSS"** (TM4\_TUSS) que é a junção de procedimentos e eventos médicos que estão padronizados em uma terminologia única. Será utilizada de forma obrigatória por operadoras de plano privado de assistência à saúde e prestadores de serviços de saúde.  
  
Abaixo segue orientação: 

**1°** O ambiente precisa estar atualizado com Acumulado MDT:   
[Pacote e Dicionário Correções Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA.ZIP)**2°** Em **Miscelânea - Implantação - Wizard MDT**, selecionar a opção **TUSS** para carregar as informações.  
  
Obs.: As informações serão carregadas conforme **ANS.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15792713095703)  
  
  
Após carregar, o sistema apresenta mensagem "Processamento terminado com sucesso".  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15792909032727)  
  
  
As informações serão carregadas nas rotinas Grupos TUSS **(MDTA021)**,  Subgrupos TUSS **(MDTA022)** e **TUSS (MDTA023)**.

**1°** Rotina Grupos TUSS **(MDTA021)** na rotina *Atualizações - Cadastros Básicos - Grupos TUSS*. É possível incluir informações em todas rotinas:   
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15793053309079)  
  
  
**2°** Subgrupos TUSS **(MDTA022)** na rotina *Atualizações - Cadastros Básicos - Subgrupos TUSS*.  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15793055903511)  
  
  
**3°** TUSS **(MDTA023)** na rotina *Atualizações - Cadastros Básicos - TUSS*. Essa rotina é composta pelas rotinas de Grupo e Subgrupo TUSS.     
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15793157297559)  
  
Se os menus não constarem em seu sistema, deverá incluir de forma manual. Consulte documentação com orientações:  
[Menu TUSS](https://tdn.totvs.com/display/public/PROT/1325389+MNG-4355+DT+TUSS)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
