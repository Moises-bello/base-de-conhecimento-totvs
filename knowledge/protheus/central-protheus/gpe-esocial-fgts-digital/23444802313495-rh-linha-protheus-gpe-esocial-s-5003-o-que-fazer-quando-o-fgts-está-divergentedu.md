---
article_id: 23444802313495
category: GPE - eSocial - FGTS Digital
content_hash: 51ef957065025c4224cfab9bdbf0f2ee58e74e312c94111e98e0d96716c8bed0
fetched_at: '2026-06-28T22:44:59.339438+00:00'
product: protheus
section_id: 17829152532503
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5003 - O que fazer quando o FGTS está
  divergente/duplicando no eSocial
type: support-article
updated_at: '2024-05-13T19:56:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23444802313495-RH-Linha-Protheus-GPE-eSocial-S-5003-O-que-fazer-quando-o-FGTS-est%C3%A1-divergente-duplicando-no-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23444802291863) Tempo aproximado para leitura: **00:03:00 min****Dúvida**O que fazer quando o FGTS está divergente/duplicando no eSocial?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A tratativa do sistema junto com a entrega das informações é a mesma do INSS. É enviada as verbas do cálculo do pagamento pelo S-1200/S-2299 para o eSocial e o cálculo dos encargos são realizados de acordo com a base de FGTS, que será composta pela configuração das incidências FGTS de cada verba enviada anteriormente pelo S-1010.   
  
Os valores apresentados no portal do eSocial são computados de acordo com a incidência das rubricas informado no sistema, mas o cálculo é realizado pelo próprio RET (Governo).   
  
A configuração das Verbas/Rubricas com relação a Natureza e as Incidências Tributárias é algo particular de cada Empresa e que deve ser analisado em conjunto com o departamento Jurídico e Contábil, o que podemos fazer é certificar que essas informações estão saindo do Protheus da forma esperada pelo leiaute do eSocial.  
  
![](https://totvssuporte.zendesk.com/attachments/token/rL8FeyXTW5Su78Egr9TOhLaDD/?name=image.png) **1. Caso a divergência ocorra para funcionários de férias,**  
Verifique se as verbas de contra partida de férias de ID 1872 (mensal) e/ou 1882 (13º salário) estão cadastradas e calculadas corretamente. Para mais detalhes, verifique a documentação a seguir:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - O INSS, FGTS e IR ficam incorretos no eSocial (DCTFWEB) quando existe Férias no mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422759630487-RH-Linha-Protheus-GPE-eSocial-S-1200-O-INSS-FGTS-e-IR-ficam-incorretos-no-eSocial-DCTFWEB-quando-existe-F%C3%A9rias-no-m%C3%AAs?source=search)  
  
**2. Para os demais casos,**  
Realize a geração do relatório de conferência filtrado pelo CPF do funcionário do S-1200 ou S-2299 para que seja possível conferir as verbas cadastradas no sistema e suas respectivas incidências, valores e tipo:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE)   
[RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299)  
  
Faça a conferência através do relatório onde é possível filtrar pela chave ideDmDev e selecionar somente os cálculos de Folha, Férias ou Adiantamento, por exemplo.  
No exemplo abaixo, filtrei somente para a chave com os valores de folha e, neste cenário, temos o código da verba, o tipo, valor, natureza, incidência FGTS eSocial e incidência FGTS Folha.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23444780491799)  
  
Devemos sempre **analisar** se os **valores gerados nos cálculos estão corretos**, pois se base de FGTS ou o desconto estiver com valor errado, para o eSocial os valores também ficarão incorretos.   
  
Essa analise pode ser realizada antes de enviar os eventos periódicos, caso considere necessário.   
  
Com base nas informações do relatório, devemos conferir também o que foi enviado ao eSocial, se condiz com a parametrização do sistema.   
Os dados enviados no evento S-1010 é a forma que o governo vai calcular os valores de FGTS. Qualquer alteração de verbas, deve ser feita no Protheus e depois enviado ao eSocial.   
[RH - Linha Protheus - GPE - eSocial - S-1010 - Como consultar no site do eSocial dados do evento S-1010 (Tabelas de Rubricas)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043153534-RH-Linha-Protheus-GPE-eSocial-S-1010-Como-consultar-no-site-do-eSocial-dados-do-evento-S-1010-Tabelas-de-Rubricas)   
  
Portanto devemos analisar as verbas enviadas ao eSocial no evento S-1200 por exemplo e conferir as rubricas que estão com incidência no campo Cd. Inc. FGTS, do cadastro de verbas (SRV), aba eSocial e confrontar com as informações enviadas ao eSocial através do evento S-1010.  
  
Abaixo exemplo do campo Cd. Inc. FGTS  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23444802296727)  
[RH - Linha Protheus - GPE - eSocial - S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-ajustar-incid%C3%AAncia-e-validade-de-rubricas-no-governo-TAF-e-GPE)  
  
Em caso de ajustes no Protheus e/ou envio do S-1010 com início de validade anterior ao período com divergência para ajuste da verba no eSocial, realize o reprocessamento dos eventos para ajuste dos valores no eSocial:  
- Excluir o evento S-1210 dos funcionários identificados com divergência;  
- Enviar o evento S-3000 gerado;  
- Retificar o evento S-1200/S-2299 dos funcionários identificados com divergência;  
- Gerar e transmitir o evento S-1210;  
  
Para mais detalhes verifique a documentação abaixo:  
[RH - Linha Protheus - GPE - eSocial - Como retificar ou reprocessar os Totalizados (DCTFWEB) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254-RH-Linha-Protheus-GPE-eSocial-Como-retificar-ou-reprocessar-os-Totalizados-DCTFWEB-no-eSocial?source=search)  
  
No dia 12/09/2023 realizamos um evento para a conferência do FGTS Digital. Este conteúdo está bem completo encontra-se disponível no link: [Conferência de FGTS (S-5003) eSocial Protheus RH](https://www.youtube.com/watch?v=-H61al9kqBo&feature=youtu.be)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
