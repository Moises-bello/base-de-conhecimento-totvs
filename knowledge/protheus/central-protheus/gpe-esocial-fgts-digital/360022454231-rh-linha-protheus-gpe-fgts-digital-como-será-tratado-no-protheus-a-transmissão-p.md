---
article_id: 360022454231
category: GPE - eSocial - FGTS Digital
content_hash: d94378d0d11a7a8b16b0e46f630a74b34e9395b0e489bf69b29ba6844a02080b
fetched_at: '2026-06-28T22:44:59.373291+00:00'
product: protheus
section_id: 17829152532503
source: central-protheus
title: RH - Linha Protheus - GPE - FGTS Digital - Como será tratado no Protheus a
  transmissão para o eSocial
type: support-article
updated_at: '2026-05-26T10:51:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022454231-RH-Linha-Protheus-GPE-FGTS-Digital-Como-ser%C3%A1-tratado-no-Protheus-a-transmiss%C3%A3o-para-o-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16599797813399) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como será tratado no Protheus a transmissão do FGTS Digital para o **eSocial**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões   
  
**Solução**O sistema **Protheus** não faz a geração da Guia de FGTS Digital, assim como ocorre com o **INSS** onde as informações para pagamento ficam disponíveis no ambiente **DCTFWEB**, as informações do FGTS irão ficar disponíveis no ambiente **FGTS Digital**, que poderá ser acessado no endereço abaixo:  
<https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital>  
  
Os valores do FGTS são transmitidos para o **RET** através dos eventos **S-1200**, **S-2299** e **S-2399**. O Governo por sua vez retorna o evento **S-5003** (Informações do FGTS por Trabalhador), e o evento **S-5013** (Informações do FGTS consolidadas por contribuinte) após o envio do evento de fechamento **S-1299**.  
  
Para correta apuração dos valores de FGTS é imprescindível que as rubricas estejam devidamente configuradas com **Incidência FGTS eSocial** conforme previsto no evento S-1010 na *tag* <codIncFGTS>  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16599753664023)  
  
[RH - Linha Protheus - GPE - eSocial - S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-ajustar-incid%C3%AAncia-e-validade-de-rubricas-no-governo-TAF-e-GPE)  
  
Em relação a conferência, para que o sistema **Protheus** esteja preparado para receber os retorno no evento **S-5003/S-5013** é necessário aplicar a atualização de pacote e dicionário diferencial disponível na página [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw).  
  
**Onde localizar o retorno dos eventos S-5003 / S-5013 no TAF?**Os eventos ficam localizados no caminho abaixo:  
**S-5003** No caminho atualizações > eventos eSocial > Totalizadores > FGTS Por Trabalhador.  
**S-5013** No caminho atualizações > eventos eSocial > Totalizadores > FGTS Por Contribuinte.

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital)  
[RH - Linha Protheus - GPE - eSocial - Informações sobre o FGTS Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8581673273879-RH-Linha-Protheus-GPE-eSocial-Informa%C3%A7%C3%B5es-sobre-o-FGTS-Digital?source=search)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
