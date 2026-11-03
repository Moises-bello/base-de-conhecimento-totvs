---
article_id: 360006989632
category: GPE - eSocial - Periódicos
content_hash: 20ca0691282cbe7f22de292d6e13a94c40ea899e253a076e5b760969de1d7075
fetched_at: '2026-06-28T22:45:07.239138+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Deve ser gerado S-1200 de adiantamento
  para funcionário que foi desligado no mesmo mês
type: support-article
updated_at: '2025-07-21T15:34:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006989632-RH-Linha-Protheus-GPE-eSocial-S-1200-Deve-ser-gerado-S-1200-de-adiantamento-para-funcion%C3%A1rio-que-foi-desligado-no-mesmo-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33610829085591) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Funcionário recebeu adiantamento e depois foi desligado, gerando e enviando o evento **S-2299**. Deve ser gerado no mesmo período o evento S-1200 com o adiantamento?  
  
Funcionário recebeu adiantamento e depois foi desligado, gerando e enviando o evento **S-2299**. No processamento periódico foi gerado um arquivo **S-1200** com a informação do demonstrativo do adiantamento, mas retornou com erro de que o trabalhador está desligado e não deve ter o *tpPgto* = 1. Se não enviou o S-1200, apenas o **S-1210**, com um bloco *infoPgto* informando na tag *tpPgto* = 1 e outro bloco *infoPgto* com *tpPgto* = 2, o erro retornado é de que não há *ideDmDev* correspondente no **S-1200**. Como devo estruturar o **S-1210** neste cenário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Essa pergunta foi respondida pelo governo no item **10.18** das [Perguntas Frequente site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes#10--remunera--o--pagamento-e-encerramento-de-eventos-peri-dicos)  
Neste caso, o demonstrativo do adiantamento (**grupo** [*dmDev*]) deve ser informado no evento de desligamento (**S-2299**), não no **S-1200**. Deverá ser criado um demonstrativo para informar o adiantamento e outro com as verbas rescisórias propriamente ditas, no qual constará o desconto do adiantamento feito.   
  
O evento **S-1210** referenciará esses demonstrativos do **S-2299** no bloco *infoPgto* informando na tag *tpPgto* = 2 (Informações enviadas pelo evento S-2299)  
  
  
**Saiba Mais**

Para adquirir mais conhecimento acesse os links abaixo:   
[Manual de Orientação do FGTS](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-0-18-08-2023.pdf)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
