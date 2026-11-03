---
article_id: 28860865081495
category: GPE - eSocial - Carga Inicial
content_hash: 487f9a0bf7102a90927893d7078dc47f4b95e6b829e68473aec87ead18302388
fetched_at: '2026-06-28T22:45:03.258613+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 - Como informar a incidência PIS/Pasep
type: support-article
updated_at: '2024-12-30T20:12:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28860865081495-RH-Linha-Protheus-GPE-eSocial-S-1010-Como-informar-a-incid%C3%AAncia-PIS-Pasep
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28860860771863) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como informar a incidência para compor a base de calculo para o PIS/Pasep?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**De acordo com o **[MOS](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-02-2024.pdf)**, pagina 104:  
**21.** Contribuição para o PIS/Pasep  
**21.1.** O campo {**codIncPisPasep**} do grupo [dadosRubrica] deve ser utilizado para **indicar a incidência da Contribuição para o PIS/Pasep sobre a folha de pagamento**, nas rubricas constantes nos demonstrativos de remuneração, para o cálculo dos totalizadores, desde que o campo {indTribFolhaPisPasep} esteja com o status = [S] no evento S-1000.  
**21.2.** Caso o contribuinte tenha processo cadastrado no evento S-1070 com medida judicial indicando a suspensão da incidência da Contribuição para o PIS/Pasep, o campo {codIncPisPasep} deve ser preenchido com os códigos [91, 92].  
  
Para o Protheus, foi criado **campo RV\_INCPIS** no Cadastros de Verbas (tabela SRV) e adicionadas validações referentes a seu preenchimento conforme leiaute S-1.3 do eSocial:

Para incidência **00 (não é base de cálculo do PIS/PASEP)**, o campo RV\_PIS **não** deve ser preenchido com "**S**";  
Para as **incidências 11 e 12**, o campo **RV\_PIS deve estar com "S";**  
Para as **incidências** **91 e 92** (suspensas), **o campo RV\_PIS não será validado**. Porém, deve haver registro correspondente de **Processo da Verba (tabela RJG) com o novo tipo: 5 - PIS.**Para o campo **Cd.Inc. PIS** acesse a **aba eSocial** do cadastro de verbas  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28860865071255)  
  
Para o campo **RV\_PIS**, acesse a **aba incidências** do cadastro de verbas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28860865072535)

Ao confirmar a alteração se atente a data da competência informada. Esse processo gerará o evento S-1010.  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Boletim Técnico](https://tdn.totvs.com/pages/viewpage.action?pageId=887739380)  
[RH - Linha Protheus - GPE - eSocial - Como retificar ou reprocessar os Totalizadores (DCTFWEB) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254-RH-Linha-Protheus-GPE-eSocial-Como-retificar-ou-reprocessar-os-Totalizadores-DCTFWEB-no-eSocial?source=search)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[Agenda de Eventos Tira Dúvidas Suporte](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
