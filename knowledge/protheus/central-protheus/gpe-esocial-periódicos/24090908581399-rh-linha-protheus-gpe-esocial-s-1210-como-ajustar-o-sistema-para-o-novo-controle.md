---
article_id: 24090908581399
category: GPE - eSocial - Periódicos
content_hash: 8672efcc4d77cf6cb4ac9d4abf9557038bebd8ab85e44d8fd88b7c9154b0455e
fetched_at: '2026-06-28T22:45:08.894247+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Como ajustar o sistema para
  o novo controle do IdeDmDev
type: support-article
updated_at: '2025-07-24T19:54:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24090908581399-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-ajustar-o-sistema-para-o-novo-controle-do-IdeDmDev
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24090908543639) Tempo aproximado para leitura: 00:03:00 min** **Dúvida**Como ajustar o sistema para o [Novo Controle do IdeDmDev](https://tdn.totvs.com/display/public/PROT/Novo+Controle+do+ideDmDev)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Antes da melhoria a composição da *tag* IdeDmDev existente nos eventos periódicos dependia da quantidade de vínculos do funcionário. E também, dependendo do tamanho dos campos filial e matrícula, o tamanho do demonstrativo gerado poderia ser mais do que o aceito pelo eSocial.  
  
Agora, com a proposta de evitar erros envolvendo o IdeDmDev, foi criada um **prefixo por funcionário** que será sequencial por **CPF e substituirá os dados de Filial e Matrícula** na composição do valor da tag.  
  
Para implantar a melhoria em seu ambiente é necessário aplicar os últimos pacotes acumulados RH e TAF disponibilizados na página **[Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)** e executar o **UPDDISTR (Dicionário de Dados)**:  
<https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA>  
<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TAF_EXPEDICAO_CONTINUA.ZIP>  
  
Após a execução do **UPDDISTR**, é necessário habilitar o parâmetro **MV\_IDEVTE.**Com o parâmetro ativo, ao processar os eventos S-1200, S-2299 ou S-2399, e caso não esteja retificando ou sobrescrevendo um registro, a tabela RU8 será gerada para guardar o prefixo a cada funcionário, conforme imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24099606313495)  
**Obs.: o campo RU8\_ID será preenchido com um novo conteúdo se houver mais de uma matrícula para o mesmo CPF.**No exemplo abaixo, para melhor entendimento, uma comparação entre as **tags IdeDmDev**do evento S-1200 antes e depois da melhoria:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24091402107415)  
**A tag IdeDmDev deixou de ter a filial + matrícula em sua composição para receber o prefixo (RU8\_ID)**Exemplo: de **AARS 0010002102311052310FOL** para **000120231105202310FOL**.  
  
Composição da chave: **000120231105202310FOL**  
**0001** --> ID  
**20231102** --> Data de Pagamento  
**202310** --> Competência  
**FOL** --> Roteiro  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Boletim Técnico Novo Controle do ideDmDev](https://tdn.totvs.com/display/public/PROT/Novo+Controle+do+ideDmDev)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
