---
article_id: 17214767758871
category: GPE - eSocial - Não Periódicos
content_hash: 635c81b97c780f39177b122b9fbd11984f566963f379aa4ec6e96d42b58b5e22
fetched_at: '2026-06-28T22:45:04.500172+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Como retificar categoria eSocial
  de 101 para 103 no cadastro do trabalhador
type: support-article
updated_at: '2026-06-16T12:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17214767758871-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-retificar-categoria-eSocial-de-101-para-103-no-cadastro-do-trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17214735413271) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como retificar categoria eSocial de 101 para 103 no cadastro do trabalhador?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução****Importante:** É necessário que o ambiente esteja atualizado com o acumulado mais recente disponibilizado na página [Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais).A alteração da categoria eSocial deve ser realizada através de uma retificação do evento S-2200, pois não pode ser gerado o evento S-2206 no caso de alteração de categoria de 101 para 103. Conforme regra do [Leiaute S-1.1](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-01-2024-rev-03-10-2024/regras.html) do eSocial:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28090605506327)  
  
**Obs.**: O governo aceita os eventos em ordem cronológica, então será necessário excluir eventos que já tenham sido enviados, como por exemplo, eventos de remuneração (S-1200/S-2299 e S-1210).  
  
O parâmetro **[MV\_RETSOC](https://tdn.totvs.com/pages/releaseview.action?pageId=450143939)** deve estar preenchido com **".T.",** pois o parâmetro foi criado para gerar retificação.  
  
Para alterar a categoria do funcionário, acesse o módulo **SIGAGPE**, rotina **Gestão Funcionário**.

*Caminho: Atualizações > Funcionários > Gestão Funcionário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17211418123415)*  
Selecione o funcionário desejado e vá em *Funcionários > Funcionários > Alterar:*![](https://centraldeatendimento.totvs.com/hc/article_attachments/17211767987735)  
  
Na aba **Funcionais**, altere o campo **Cat. eSocial** de 101 para 103 e clique em **Salvar**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17213664068503)  
  
Será apresentada a mensagem se **Deseja Gerar Retificador**, clique em **Sim**. E, por fim, o registro será enviado para o TAF com sucesso.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17213727600535)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17213794604055)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-2200 - Como retificar evento S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033905013-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-retificar-evento-S-2200?source=search)  
[Boletim técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=780016208)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
