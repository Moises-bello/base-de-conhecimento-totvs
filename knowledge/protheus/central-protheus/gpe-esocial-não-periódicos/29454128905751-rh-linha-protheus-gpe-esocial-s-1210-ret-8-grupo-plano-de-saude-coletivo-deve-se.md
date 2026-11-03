---
article_id: 29454128905751
category: GPE - eSocial - Não Periódicos
content_hash: 314da2d5781eed65d26131acef4df91e0258e1cfe9ccb31cef59e6d43881b1e7
fetched_at: '2026-06-28T22:45:04.411705+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - RET 8: Grupo ''Plano de saude
  coletivo'' deve ser preenchido.'
type: support-article
updated_at: '2026-06-26T19:55:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29454128905751-RH-Linha-Protheus-GPE-eSocial-S-1210-RET-8-Grupo-Plano-de-saude-coletivo-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29454128884631) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Evento S-1210 com rejeição - Código de Ocorrência 8 - Descrição: Grupo 'Plano de saúde coletivo' deve ser preenchido.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29455732668567)  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Causa**

Quando é enviado algum evento de remuneração ao eSocial o site realiza a comparação entre as rubricas que foram enviadas no S-1010 com as rubricas enviadas no evento de remuneração, com isso, quando encontra alguma divergência retorna com um erro.  
  
O erro mencionado acima acontece quando o S-1200/S-2299 contém alguma rubrica de plano de saúde, porém quando foi enviado o S-1010 dessa rubrica a natureza tributária não estava como 9219 - Desconto de assistência médica ou odontológica, por isso o eSocial encontra divergência entre as informações prestadas anteriormente como as informações prestadas no S-1200/S-2299.  
  
**Solução**Verifique no evento S-1210 rejeitado qual o período de referencia dos pagamentos enviados no evento. Segue documentação para gerar o XML S-1210: [RH - Linha Protheus - GPE - eSocial - S-1210 - Como gerar os arquivos XML do evento S-1210 (Pgto Rend Trab.) no modulo SIGATAF para análise](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006741342-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-gerar-os-arquivos-XML-do-evento-S-1210-Pgto-Rend-Trab-no-modulo-SIGATAF-para-an%C3%A1lise)   
  
Abaixo o exemplo do XML S-1210. Os pagamentos são do roteiro ADI e FOL, ambos com o <perRef> 2025-01:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29454128887959)  
  
  
Gere o relatório de conferência S-1200 desse período e analise qual  é verba com a natureza 9219 - Desconto de assistência médica ou odontológica. Segue documentações para gerar o relatório de conferência do S-1200 ou S-2299 quando for mês do desligamento do colaborador:

* [RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no módulo GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE?source=search)
* [RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299?source=search)

Na analise do relatório irá se deparar com duas opções de cenário:

1. A verba que contem a natureza 9219 esta **correta**, pois a verba **é desconto de assistência médica e/ou odontológica;**
2. A verba que contem a natureza 9219 esta **errada**, pois a verba **não é** **desconto de assistência médica e/ou odontológica.**

**Cenário 1:**A verba que contem a natureza 9219 esta **correta**, pois a verba **é desconto de assistência médica e/ou odontológica.** Abaixo o relatório de conferência do evento S-1200 demonstrando que a verba se trata de desconto de plano de saúde e odontológica.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29455656749847)  
  
Se a verba com natureza 9219 realmente se tratar de um desconto de assistência médica ou odontológica, **é necessário que o plano de saúde seja calculado do roteiro PLA**, e que essa verba esteja com incidencia IRRF = 67. Dessa forma os dados da assistência saúde (dados da operadora, valor do desconto e informações do titular e/ou dependentes) serão geradas no evento S-1210.   
  
Segue materiais de apoio para validação:

* [Novas validações S-1210 Leiaute S-1.3](https://tdn.totvs.com/pages/releaseview.action?pageId=872685259)
* [RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11223604924695-RH-Linha-Protheus-GPE-Quais-as-documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-plano-de-sa%C3%BAde)
* [RH - Linha Protheus - GPE - Configuração da assistência odontológica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025687511-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-da-assist%C3%AAncia-odontol%C3%B3gica)
* [RH - Linha Protheus - GPE - Documentações relacionadas a rotina de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11301756760855-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-coparticipa%C3%A7%C3%A3o)
* [RH - Linha Protheus - GPE - Como fazer o reembolso de assistência medica/odontológica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051315374-RH-Linha-Protheus-GPE-Como-fazer-o-reembolso-de-assist%C3%AAncia-medica-odontol%C3%B3gica)

**Cenário 2:**  
A verba que contem a natureza 9219 esta **errada**, pois a verba **não é** **desconto de assistência médica e/ou odontológica.**  Abaixo a imagem com a natureza indevidamente em uma verba que não é desconto de assistência médica ou odontológica:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29454753034007)  
  
Ajuste a natureza dessa verba e envie o evento S-1010 com o período de referencia a ser ajustado. Após a correção na natureza da verba, retifique o evento S-1200 desse período para que o eSocial não solicite mais os dados de plano de saúde ou odontológicos desse trabalhador, ai sim o S-1210 não seja mais rejeitado com esse motivo.

Veja também: [RH - Linha Protheus - TAF - Periódicos- Grupo 'Plano de saude coletivo' deve ser preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29751776385303-RH-Linha-Protheus-TAF-Peri%C3%B3dicos-Grupo-Plano-de-saude-coletivo-deve-ser-preenchido) 

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
