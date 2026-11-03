---
article_id: 360019656512
category: GPE - eSocial - Periódicos
content_hash: a7132bf9287ec0bd26ea4f9dcbc51cef757e92a9327ed8398ee24e47a6c30ce4
fetched_at: '2026-06-28T22:45:07.325914+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como deve ser enviado para o
  eSocial os valores de diferença de medias/remuneração variável de 13º salário gerados
  após o calculo da 2ª Parcela
type: support-article
updated_at: '2025-07-21T14:31:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019656512-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-deve-ser-enviado-para-o-eSocial-os-valores-de-diferen%C3%A7a-de-medias-remunera%C3%A7%C3%A3o-vari%C3%A1vel-de-13%C2%BA-sal%C3%A1rio-gerados-ap%C3%B3s-o-calculo-da-2%C2%AA-Parcela
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19285101206679)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como deve ser enviado para o **eSocial** os valores de diferença de remuneração variável de 13º Salário gerados após o calculo da **2ª Parcela**?

Pois existe alguns cenários onde deve ser pago medias sobre hora extra ou comissão que ocorreu em Dezembro.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Os ajustes de 13º salário, decorrentes do recebimento de remuneração variável, deverão ser informados na folha de pagamento de Dezembro no evento S-1200.  
  
**Segue abaixo NOTA ORIENTATIVA 2018.13 referente as orientações sobre a folha de 13º salário:**  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-013-2018-13-salario.pdf>  
  
**Caso haja ajustes de 13º salário** decorrentes do recebimento de remuneração variável (comissões sobre vendas, por exemplo), **o complemento deverá ser pago até o dia 10 de** **janeiro** e **informado na folha mensal da respectiva competência** (Dezembro ou Janeiro), em rubrica específica (**natureza de rubrica 5005 – 13º salário complementar**) previamente cadastrada no evento S-1010 com as incidências de 13º para codIncCP, codIncFGTS e codIncIRRF.  
  
No **Protheus** utilizamos o **Identificador para Cálculo 0028**. Veja o *link* abaixo:  
[RH - Linha Protheus - GPE - Como configurar o sistema para gerar automaticamente valores de complemento de 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016519791-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-gerar-automaticamente-valores-de-complemento-de-13%C2%BA-Sal%C3%A1rio?source=search)  
  
No modulo **SIGAGPE** ao gerar os eventos periódicos é necessário informar a competência **12/AAAA** e deixar o campo **Ref. 13º com NÃO** conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19285096163863)  
  
**Atenção**  
Verifique também se a verba de **ID 0028,** não está informada em outra verba no campo **RV\_CODCOM\_ (VerbaP.Diss)** localizado na aba Dissidio, no cadastro de verbas.  
É possível verificar também essa divergência da verba através do relatório do evento S-1200 na aba Inconsistência.   
Veja como gerar: [RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-antes-de-integrar-o-evento-peri%C3%B3dico-para-o-TAF)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes) 

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
