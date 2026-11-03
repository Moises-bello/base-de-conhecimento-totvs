---
article_id: 14230504342935
category: GPE - eSocial - Periódicos
content_hash: 25d510aa99eaa55319ceb9ab2593ad5d69e51a8404d5c8a321b6de37a6ca18b9
fetched_at: '2026-06-28T22:45:08.581067+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Diferença entre Rendimento não
  tributável (7950) e verba transitada pela folha de pagamento (7900)
type: support-article
updated_at: '2025-07-24T18:54:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14230504342935-RH-Linha-Protheus-GPE-eSocial-S-1200-Diferen%C3%A7a-entre-Rendimento-n%C3%A3o-tribut%C3%A1vel-7950-e-verba-transitada-pela-folha-de-pagamento-7900
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24317847939351) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como verificar os valores do IRRF apresentados no eSocial nos tipos 7900 (Verba transitada pela folha) e 7950 (Rendimento não tributável)? **Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões **Solução**Todos as eventos de rendimento enviados a partir da versão S-1.0 que não tem incidência no IRRF, devem ser enviados com um tipo de isenção de IRRF vigente.  
Na **tabela 21 do eSocial** é demonstrada os códigos de incidência tributária das rubricas para o IRRF. As verbas que são isentas de IRRF são 9,  7X e 7XX:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33696088610071)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33696101470103)  
  
Segue abaixo orientações do MOS de como esses valores são exibidos no ambiente do governo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14230382368023)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14230383315607)

Em resumo, todos os eventos que forem enviados sem incidência, e forem desconto ou base de cálculo, irá gerar automaticamente como 9, compondo o campo 7900 no eSocial.  
E os eventos de provento que você isentar com o código 79 no cadastro do evento, irá compor o campo 7950.  
  
Se você entende que algum evento que está indo para o 7900 incorretamente, e deveria ir para o campo 7950, você deve marcar a isenção e selecionar algum dos códigos que começam com 7XX.  
  
Para auxiliar a conferencia deve ser gerado o relatório de conferencia do S-1200 (do mês e do mês anterior) para realizar filtro por incidência do IRRF para auxiliar na identificação e ajustes (se necessário).  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-antes-de-integrar-o-evento-peri%C3%B3dico-para-o-TAF?source=search)  
  
**Fontes:**   
[Manual de Orientações do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-02-2023.pdf) página 102 e 103  
[Tabela 21 do leiaute S-1.3 do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-03-2025/tabelas.html#21)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
