---
article_id: 23611621524503
category: GPE - eSocial - Periódicos
content_hash: 7fd350130b430cc4ade8d3ce125d54a8067f6b10a9cb50086a7a9decfdebcb07
fetched_at: '2026-06-28T22:45:07.424418+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - esocial - S-1280 - Como ajustar as informações
  no eSocial tendo em vista a decisão do STF, de 17/05/2024
type: support-article
updated_at: '2025-07-24T19:54:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23611621524503-RH-Linha-Protheus-GPE-esocial-S-1280-Como-ajustar-as-informa%C3%A7%C3%B5es-no-eSocial-tendo-em-vista-a-decis%C3%A3o-do-STF-de-17-05-2024
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23611621506967) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como ajustar as informações no eSocial tendo em vista a decisão do STF, de 17/05/2024, que suspendeu por 60 dias os efeitos da decisão cautelar na Ação Direta de Inconstitucionalidade (ADI) 7633, relativa à Lei nº 14.784/2023 Quais as providências devem ser adotadas no eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Foi atualizada em 19/05/2024 a pergunta [10.37](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes) do perguntas e respostas eSocial.  
Considerando [nota](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2024/maio/nota-de-esclarecimento-1) publicada no portal da Receita Federal do Brasil, o ministro Cristiano Zanin, do  
Supremo Tribunal Federal (STF), adiou por 60 dias os efeitos da decisão cautelar na Ação Direta de Inconstitucionalidade (ADI) 7633, relativa à Lei nº 14.784/2023, que prorroga a desoneração da folha de pagamento de municípios e de diversos setores produtivos até 2027.  
As alterações nos cálculos do eSocial para ajustar o sistema à nova decisão foram implantadas em produção em 18/05/2024.  
Orientamos às empresas, aos órgãos gestores de mão de obra (OGMO) e municípios a realizarem os seguintes procedimentos:  
  
**1. Caso já tenha fechado a folha de abril/2024:**  
1.1 [Reabrir a folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038011533-Automa%C3%A7%C3%A3o-Fiscal-PERI%C3%93DICOS-Como-acessar-a-rotina-de-Reabertura-Peri%C3%B3dicos-S-1298)   
1.2 No caso das empresas e OGMO (Órgão Gestor de Mão de Obra) enviar o [evento S-1280](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018785372-RH-Linha-Protheus-GPE-eSocial-S-1280-Como-%C3%A9-gerado-o-evento-S-1280) com as informações sobre a desoneração;  
1.3 Fechar a folha novamente enviando o [S-1299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022286212-RH-Linha-Protheus-GPE-eSocial-S-1299-Como-gerar-o-evento-S-1299-fechamento-peri%C3%B3dicos-para-transmitir-ao-RET). O sistema recalculará as contribuições e enviará a nova apuração para a DCTFWeb.  
  
**2. Caso ainda não tenha fechado a folha de abril/2024**  
No caso de empresas e OGMO (Órgão Gestor de Mão de Obra), enviar o [evento S-1280](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018785372-RH-Linha-Protheus-GPE-eSocial-S-1280-Como-%C3%A9-gerado-o-evento-S-1280) com as informações sobre a desoneração e encerrar a folha ([S-1299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022286212-RH-Linha-Protheus-GPE-eSocial-S-1299-Como-gerar-o-evento-S-1299-fechamento-peri%C3%B3dicos-para-transmitir-ao-RET)).  
  
**3. Municípios com fator populacional inferior a 4 (alíquota de 8%)**Reabrir a folha ([S-1298](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038011533-Automa%C3%A7%C3%A3o-Fiscal-PERI%C3%93DICOS-Como-acessar-a-rotina-de-Reabertura-Peri%C3%B3dicos-S-1298)) e encerrá-la novamente ([S-1299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022286212-RH-Linha-Protheus-GPE-eSocial-S-1299-Como-gerar-o-evento-S-1299-fechamento-peri%C3%B3dicos-para-transmitir-ao-RET)). O sistema recalculará as contribuições e enviará a nova apuração para a DCTFWeb.  
  
**Importante**: Em qualquer dos casos, é necessário previamente ajustar o S-1000 para informar a opção pela desoneração (empresas e municípios). O S-1000 vigente deverá ter o campo {indDesFolha}=[1 – Empresa enquadrada nos critérios da legislação vigente], para empresas e OGMO (Órgão Gestor de Mão de Obra) abrangidos pela desoneração; ou {indDesFolha}=[2 – Município enquadrado nos critérios da legislação vigente] para municípios com fator populacional inferior a 4.  
  
**Para alterar**, acesse o módulo Automação Fiscal - Atualizações - Configurações TAF - Complemento Cadastral. Após alteração transmita para o eSocial o evento S-1000

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23611621508375)****Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Noticia eSocial desoneração - 17/05/2024](https://www.gov.br/esocial/pt-br/noticias/stf-suspende-por-60-dias-os-efeitos-de-sua-decisao-que-reconheceu-a-inconstitucionalidade-da-lei-no-14-784-2023)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
