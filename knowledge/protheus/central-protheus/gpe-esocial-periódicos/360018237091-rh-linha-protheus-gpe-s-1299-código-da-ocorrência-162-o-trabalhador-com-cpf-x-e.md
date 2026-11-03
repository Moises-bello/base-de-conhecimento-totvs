---
article_id: 360018237091
category: GPE - eSocial - Periódicos
content_hash: ffc120dfc22a7eb6718ffd29a6ee4b6ea41fdc9a8f5c60b587bf9897026c9ee5
fetched_at: '2026-06-28T22:45:09.963324+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - S-1299 - Código da Ocorrência 162: O Trabalhador
  com CPF X e Matricula Y consta na base de dados do Ambiente Nacional do eSocial,
  mas não foi informada sua remuneração.'
type: support-article
updated_at: '2025-07-22T17:03:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018237091-RH-Linha-Protheus-GPE-S-1299-C%C3%B3digo-da-Ocorr%C3%AAncia-162-O-Trabalhador-com-CPF-X-e-Matricula-Y-consta-na-base-de-dados-do-Ambiente-Nacional-do-eSocial-mas-n%C3%A3o-foi-informada-sua-remunera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27284879714455) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Sequência: 000001 - Tipo: Advertência - Código da ocorrência: 162  
Descrição: O Trabalhador com CPF X e Matricula Y consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração. Ação Sugerida: Verificar se a falta de informação e decorrente de dificuldades operacionais ou se e possível efetuar a regularização.  
  
**Causa**Ao enviando um evento de fechamento mensal da folha de pagamento dentro de um determinado período, o RET encontrou matriculas ativas enviadas através do evento S-2200 e para este período não existe o evento S-1200 (folha de pagamento) ou S-2299 (rescisão com remuneração) para esse trabalhador.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Verificar no módulo TAF, na rotina Folha de Pagamento (TAFA250), se existe o evento S-1200 no período de apuração referente ao S-1299 fechamento. Veja na imagem abaixo que não existe o período 2024-08. Caso exista, verificar se foi enviado e protocolado.  
*Caminho: SIGATAF > Atualizações > Eventos eSocial > Periódicos > Folha de Pagamento*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284879724567)

Verificar se existe informações de pagamento dentro do período consultado.

* Se o período do cálculos do **período aberto**, realize a consulta de Cálculo por Funcionário *(Caminho SIGAGPE: Consulta> Cálculos> Por Funcionário)*
* Se o período do cálculos do **período fechado**, realize a consulta no Lançamentos Acumulados *(Caminho SIGAGPE: Consultas> Cadastros> Acumulados)![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284873824407)*

Caso exista, realizar o envio dos eventos periódicos para o TAF utilizando a rotina de eventos periódicos dentro do modulo GPE, conforme documentações abaixo:

* [Como gerar eventos S-1200 e S-1210 com a folha aberta no SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044700974-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Como-gerar-eventos-peri%C3%B3dicos-com-a-folha-aberta-SRC-no-sigagpe)
* [Como gerar eventos S-1200 e S-1210 com a folha fechada no SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045208153-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Como-gerar-eventos-peri%C3%B3dicos-com-a-folha-fechada-SRD-no-sigagpe)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284873827607)

Quando gerado o evento com sucesso é apresentado a mensagem no log:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284873829399)  
  
Após a o envio dos eventos periódicos ao TAF, será necessário enviar ao governo os dois eventos S-1200 e S-1210, em seguida enviar novamente o evento de fechamento S-1299 para realizar o fechamento do período.  
  
**Saiba mais:**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página* [***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
