---
article_id: 27451839338263
category: GPE - eSocial - Periódicos
content_hash: adfba0261f55253fb978aaaca11f5376bc3aa15e29de393663283675dd9085da
fetched_at: '2026-06-28T22:45:07.143511+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como gerar valores referente ao eConsignado
  nos eventos de remuneração
type: support-article
updated_at: '2026-01-29T19:30:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27451839338263-RH-Linha-Protheus-GPE-eSocial-Como-gerar-valores-referente-ao-eConsignado-nos-eventos-de-remunera%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27451856258327)** Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como gerar valores referente ao eConsignado nos eventos de remuneração?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão P12.1.2310  
  
**Solução**  
Segue abaixo os requisitos necessários para geração do grupo [descFolha](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-01-2024-rev-03-10-2024/index.html#1200_dmDev_infoPerApur_ideEstabLot_remunPerApur_itensRemun_descFolha) com informações de desconto do empréstimo em folha eventos S-1200, S-2299 e S-2399 (categoria 721) considerando as regras do **eConsignado** de acordo com o Leiaute S-1.3.  
  
Verifique o [Manual de Orientação do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-publicado-com-marcacoes.pdf) (a partir da pag. 71)  
  
As informações devem ser cadastradas na rotina de **Valores Futuros**, [**Boletim Tecnico Crédito do Trabalhador**](https://tdn.totvs.com/pages/releaseview.action?pageId=925350852).  
  
No modulo SIGAGPE, acesse o menu: Atualizações > Lançamentos > Valores Futuros  
  
**1.** Ter uma verba cadastrada com Natureza de Rubrica 9253 e Incidência FGTS 31, deve ser **criada uma nova verba,** **não reutilizar verbas de empréstimo**. Em caso de duvidas, consulte o [boletim técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=864997809);  
**2.** Na rotina Valores Futuros, atenção para os campos destacados na imagem abaixo, pois serão as informações desses campos que serão integradas no grupo **descFolha.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27460722965271)**

**Emp. Cons.** - Indicativo do tipo de desconto (tpDesc)  
**Nr.Contrato** - Número do contrato referente ao empréstimo (nrDoc)  
**Mat.Inst.Con**- Código da Instituição Financeira concedente do empréstimo (instFinanc)  
**Obs. eConsig** - Outras informações do desconto. (observacao)  
  
Imagem do evento S-1200 no TAF demonstrando as informações integradas  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27461392003351)  
  
Imagem do evento S-1200 com o grupo **descFolha** preenchido  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27451839331479)  
  
Acesse o artigo abaixo para consultar as **Informações relativas ao desconto do eConsignado** no Totalizador FGTS  
[RH - Linha Protheus - TAF - eSocial - Totalizadores - S-5003 - Como visualizar a informação do desconto do eConsignado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27440877409047-RH-Linha-Protheus-TAF-eSocial-Totalizadores-S-5003-Como-visualizar-a-informa%C3%A7%C3%A3o-do-desconto-do-eConsignado)  
  
**Importante:**Incluir uma nova verba com a configuração do eConsignado. Não utilizar verbas com empréstimos existentes. **Não reaproveitar** por conta do histórico.  
  
**Atenção**: Para a **natureza ser apresentada no cadastro de verbas** é necessário estar com ambiente atualizado, **atualizar a tabela S047** e as autocontidas.  
  
[RH - Linha Protheus - GPE - eSocial - Como atualizar as tabelas S047, S048, S049, S054, S056 e S057, quando existe alteração das tabelas oficias no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034614474-RH-Linha-Protheus-GPE-eSocial-Como-atualizar-as-tabelas-S047-S048-S049-S054-S056-e-S057-quando-existe-altera%C3%A7%C3%A3o-das-tabelas-oficias-no-eSocial)  
  
[RH - Linha Protheus - TAF - eSocial - Configuração - Como atualizar as tabelas autocontidas no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017826812-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-atualizar-as-tabelas-autocontidas-no-TAF)  
  
As **atualizações** estão disponiveis na pagina [**Entregas Legais**](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)**.**  
  
Veja **como funciona a contratação, legislação e regras:** [RH - Linha Protheus - GPE - eSocial - eConsignado - Como funciona a contratação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30758384672151-RH-Linha-Protheus-GPE-eSocial-eConsignado-Como-funciona-a-contrata%C3%A7%C3%A3o)  
   
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
Boletim: <https://tdn.totvs.com/pages/releaseview.action?pageId=864997809>  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Perguntas frequentes FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [*TOTVS Informa*](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".
