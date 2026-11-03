---
article_id: 22847109379223
category: GPE - eSocial - Não Periódicos
content_hash: 2919ab2c977db7047d81c214fe7166da3e4d779d2521d8fb6579e0cd56541767
fetched_at: '2026-06-28T22:45:05.813828+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar a tag de infoRRA
  quando não existe o valor para IR de RRA
type: support-article
updated_at: '2026-06-16T11:47:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22847109379223-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-a-tag-de-infoRRA-quando-n%C3%A3o-existe-o-valor-para-IR-de-RRA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22847109364119) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como realizar a geração do evento do demonstrativo de RRA mesmo quando não há recolhimento de IR sobre RRA?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Foi criado o **parâmetro MV\_RRASIR** para permitir a geração do evento do demonstrativo de RRA no evento S-2299 mesmo quando não há recolhimento de IR sobre RRA.  
  
O parâmetro **MV\_RRASIR** possui o conteúdo padrão **.F.**, ou seja, mantém o comportamento atual de **não gerar o demonstrativo de RRA** para o cenário apresentado.   
Caso o entendimento seja de **levar o RRA**, independente da ausência do recolhimento de IR, o parâmetro deve ser alterado **.T.**Para verificar o parametro acesse: **SIGACFG > Ambiente > Cadastros > Parâmetros  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22847080700183)**  
Para criação do parâmetro será necessário atualização do dicionário de dados através do pacote de **[Expedição Continua](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao)**. Caso deseje incluir manualmente, verifique o **[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=827307125).**Veja também: [Manutenção dos Rendimentos Recebidos Acumulados (RRA) (GPEA840 - SIGAGPE - V12)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=450142286)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Quais cadastros devem ser preenchidos para geração do evento S-1200 contemplando o processamento de RRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11281526166551-RH-Linha-Protheus-GPE-eSocial-S-1200-Quais-cadastros-devem-ser-preenchidos-para-gera%C3%A7%C3%A3o-do-evento-S-1200-contemplando-o-processamento-de-RRA)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
