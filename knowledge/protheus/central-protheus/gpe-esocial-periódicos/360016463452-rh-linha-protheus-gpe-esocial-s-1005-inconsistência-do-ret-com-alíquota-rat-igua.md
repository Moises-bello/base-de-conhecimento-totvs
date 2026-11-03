---
article_id: 360016463452
category: GPE - eSocial - Periódicos
content_hash: 5120d943c872efeede6804fa00e6aea5d8fafe1440c50179ba5773dad5fe44a6
fetched_at: '2026-06-28T22:45:07.605427+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1005 - Inconsistência do RET com Alíquota
  RAT igual a 0 (Zero)
type: support-article
updated_at: '2025-07-17T14:19:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016463452-RH-Linha-Protheus-GPE-eSocial-S-1005-Inconsist%C3%AAncia-do-RET-com-Al%C3%ADquota-RAT-igual-a-0-Zero
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33533389700375) Tempo aproximado para leitura: 00:03:00 min  
  
Ocorrência**Retorno de Inconsistência do RET devido **Alíquota RAT** igual a **0 (Zero)**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**O Retorno de Inconsistência do RET é devido a validação do leiaute do eSocial em que a *tag* AliqRat está com conteúdo diferente de 1, 2 ou 3.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14792285743255)  
  
**Solução**Conforme leiaute vigente eSocial, **nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos {aliqRat} e {fap} com os valores correspondentes. Nesse caso, este evento deve ser enviado após o evento S-1070. Nos demais casos, os referidos campos não devem ser preenchidos.**  
Informar a alíquota RAT, quando divergente da legislação vigente para a atividade (CNAE) preponderante. A divergência só é permitida se existir o grupo com informações sobre o processo administrativo/judicial que permite a aplicação de alíquota diferente.  
**Valores válidos: 1, 2, 3**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.**Acesse o evento S-1005 no TAF através do caminho: Atualização - Eventos eSocial - Tabelas - Estabelecimentos  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14792712246935)  
  
**2.** Localize o evento S-1005 que será necessário realizar alteração  
  
**3.** Altere os campos destacados abaixo, informando a alíquota diferente para a  
atividade CNAE preponderante e o processo referente a alteração da alíquota da RAT, salve e transmita ao eSocial  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14792908180119)  
A alteração efetuada no TAF não influenciará no cálculo de sua folha de pagamento no GPE. Para calcular a folha de pagamento, o sistema irá utilizar a informação que se encontra na tabela S037, devendo estar de acordo para que não gere divergências entre sua folha de pagamento e o governo.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-1005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822873)  
[[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)](http://tdn.totvs.com/x/4JQYEw)
