---
article_id: 360045763173
category: GPE - eSocial - Periódicos
content_hash: 716015135223529253eca87b53fa8d23ae33d3a00011f6b51639d315ebc3d0a0
fetched_at: '2026-06-28T22:45:07.665642+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200 - Código da Ocorrência 8: Grupo
  ''Informações relativas ao trabalho intermitente'' não deve ser preenchido. Verifique
  as condições de preenchimento no leiaute.'
type: support-article
updated_at: '2025-07-21T20:24:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045763173-RH-Linha-Protheus-GPE-eSocial-S-1200-C%C3%B3digo-da-Ocorr%C3%AAncia-8-Grupo-Informa%C3%A7%C3%B5es-relativas-ao-trabalho-intermitente-n%C3%A3o-deve-ser-preenchido-Verifique-as-condi%C3%A7%C3%B5es-de-preenchimento-no-leiaute
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33620086202135) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Sequência: 000001 - Tipo: Erro - Código da ocorrência: 8  
Localização: /eSocial/evtRemun/ideTrabalhador  
Descrição: Grupo 'Informações relativas ao trabalho intermitente' deve ser preenchido. Verifique as condições de preenchimento no leiaute.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas Versões  
  
**Causa**Normalmente esse erro de retorno do eSocial ocorre quando não é preenchido o grupo de informações relativas ao trabalho intermitente, essas informações são geradas a partir da convocação para o eSocial através do evento S-1200, conforme leiaute vigente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verificar se foi realizada a **convocação** para o trabalhador intermitente, para acessar o cadastro de convocações no GPE (Atualizações > Funcionários > Gestão de funcionários, selecione o funcionário e clique em "Alterar" ou "Visualizar" e depois Outras ações > Convocações);  
  
2. Caso exista a convocação, verifique se a **data de inicio e fim** da atividade estão dentro do período da folha que esta sendo enviado ao eSocial, essa informação será enviada no evento S-1200 para o TAF;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17643268710167)  
  
Para mais informações acesse: [RH - GPE - eSocial - S-1200 - Como gerar Convocação para Trabalho Intermitente do SIGAGPE para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020492572)  
  
3. Verificar se o grupo de informações relativas ao trabalho intermitente foi preenchido no evento S-1200 no TAF (Atualizações > Eventos eSocial > Periódicos > Folha de pagamento);  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17643343013783)  
  
A informação também pode ser verificada através do xml do S-1200:  
[**TAF**: Como gerar ou comparar os arquivos XML do SIGAGPE e SIGATAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026656853-RH-Linha-Protheus-GPE-eSocial-Como-gerar-ou-comparar-os-arquivos-XML-do-SIGAGPE-e-SIGATAF-dentro-do-m%C3%B3dulo-SIGATAF)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
