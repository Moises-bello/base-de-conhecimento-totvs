---
article_id: 9326209981719
category: RH - Arquivos Magnéticos
content_hash: a96d9df6d96ccfe394f58b62ad0aca3e31e1cb0ae74f940cb2591946647410b8
fetched_at: '2026-06-28T22:44:55.283736+00:00'
product: protheus
section_id: 32302371669783
source: central-protheus
title: RH - Linha Protheus - PON - Arquivo Eletrônico de Jornadas - AEJ - Portaria
  671
type: support-article
updated_at: '2026-06-19T14:41:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9326209981719-RH-Linha-Protheus-PON-Arquivo-Eletr%C3%B4nico-de-Jornadas-AEJ-Portaria-671
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21038671948439) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como gerar o novo Arquivo Fiscal AEJ (Arquivo Eletrônico de Jornadas) de acordo com a Portaria 671?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A **Portaria 671,** trouxe o **novo arquivo AEJ - Arquivo Eletrônico de Jornadas** para **substituir** os arquivos **AFDT** - Arquivo Fonte de Dados Tratados e o **ACJEF** - Arquivo de Controle de Jornada para Efeitos Fiscais.   
Para isso, foi **criada a nova rotina PONM450,** e para ter acesso e gerar o arquivo, é necessário estar com o ambiente atualizado com o pacote de [expedição contínua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus).  
  
-> Caso ainda não possua o grupo de perguntas **PONM450** na **SX1, será** necessário executar o **UPDDISTR** do dicionário diferencial para **criação,** conforme abaixo:  
[**- P2310;**](https://suporte.totvs.com/portal/p/10098/download?e=1123885)  
[**- P2410;**](https://suporte.totvs.com/portal/p/10098/download?e=1123885#detail/1167445)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30965580152471)  
  
-> Incluir a rotina **PONM450** via **Configurador** no Menu do Ponto Eletrônico, conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9325588340119)  
  
  
A nova rotina disponibiliza **filtros para impressão** do arquivo conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30965580154647)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30965563704471)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30965580156951)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30965563706775)

O arquivo **AEJ** pode ser impresso para períodos de apontamento abertos ou fechados, bem como para qualquer intervalo de datas, ou seja, é possível gerar o arquivo para 1 ano, 1 mês, entre outros.

O usuário responsável pela geração do arquivo precisa possuir acesso ao diretório indicado na pergunta **"Arquivo Destino"**, caso contrário, o arquivo não será gerado.

**\*\*É obrigatório o processamento do Cálculo Mensal dos períodos para alimentar a tabela RFF (Períodos Abertos);**  
**Para períodos já fechados, as informações da tabela RFF vão para a** **tabela RFG, caso contrário, o arquivo não será gerado.**  
  
O arquivo segue o ***layout*** previsto na nova **Portaria 671**, e será gerado desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30965563707159)  
  
Para mais detalhes do ***layout,*** consulte o anexo VI [deste link.](https://in.gov.br/en/web/dou/-/portaria-359094139)  
  
Ao gerar o arquivo **AEJ**, podem ser exibidas algumas mensagens informativas no log, como:  
  
**- Funcionário sem Marcações**: será gerada quando o funcionário realmente não tiver marcações no período de impressão do AEJ ou caso o funcionário seja isento de registro de ponto.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21039015447831)  
  
**- CPF inválido:** será gerando quando o cadastro do funcionário estiver com o campo de CPF em branco ou com a numeração inválida.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21038955647639)  
  
  
Cabe ressaltar que mesmo com as mensagens sendo geradas no log, elas **não impedem** que o arquivo seja gerado para outros funcionários que tenham marcações e estejam com o CPF cadastrado corretamente, pois ambas são apenas de **caráter informativo**.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[Boletim Técnico - AEJ](https://tdn.totvs.com/pages/releaseview.action?pageId=706906445)
