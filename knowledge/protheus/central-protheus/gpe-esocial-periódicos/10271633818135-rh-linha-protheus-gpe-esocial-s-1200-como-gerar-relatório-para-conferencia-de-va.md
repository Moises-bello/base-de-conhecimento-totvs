---
article_id: 10271633818135
category: GPE - eSocial - Periódicos
content_hash: 2f0d33e1230cf9785a8677f6dd08f356b4556bed4eecdaa6cc0fa3da336611cd
fetched_at: '2026-06-28T22:45:07.720617+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório para conferencia
  de valores rescisórios de TSV
type: support-article
updated_at: '2025-07-24T20:00:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10271633818135-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-para-conferencia-de-valores-rescis%C3%B3rios-de-TSV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25159777478935) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como emitir relatório para conferência de valores rescisórios de TSV gerados no evento S-1200?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**De acordo com o [MOS S-1.2](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf), no evento S-2399 (Trabalhador Sem Vínculo de Emprego/Estatutário - Término), a informação relativa às verbas rescisórias devidas deve ser prestada, neste evento, no grupo [verbasResc] **apenas em relação aos diretores não empregados com FGTS - categoria [721].** Nos demais casos, **as verbas rescisórias devidas devem ser informadas nos eventos S-1200 ou S-1202,** **conforme o regime previdenciário do trabalhador.**  
  
Dessa maneira, é possível gerar o **relatório do evento S-1200** para realizar as devidas conferências antes de enviar o xml.  
  
**Após o calculo da rescisão**, será necessário **integrar o roteiro RES e estar com a folha calculada**.  
  
**1.** Acesse o no SIGAGPE o caminho: miscelânea > eSocial > eventos periódicos;  
**2.** Na tela dos eventos periódicos, selecione a competência e na opção processo > relatório;  
**3.** Selecione o evento S-1200, caso a folha esteja aberta marque a opção considerar dados do período em aberto.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25159777485335)  
**4.** Após gerar o relatório, será apresentada as seguintes informações:  
  
A aba **Demonstrativo Verbas** irá exibir as verbas geradas no grupo <*infoPerApur*>, além do código de natureza e as incidências para INSS, IRRF e FGTS, tanto para o eSocial quanto para a Folha.

A aba **Dem. Plano de Saúde** irá exibir as verbas geradas no grupo <*infoSaudeColet*>, além do código do fornecedor e o código do dependente.

A aba **MV - Outras Empresas** irá exibir as verbas geradas nos grupos <*indMV*> e <*remunOutrEmpr*>.

A aba **Dem. Meses Anteriores-PLR** irá exibir as verbas geradas no grupo <*infoPerAnt*>, além do código de natureza e as incidências para INSS, IRRF e FGTS, tanto para o eSocial quanto para a Folha.

A aba **S-2299-S-2399** irá exibir os funcionários que não terão o evento S-1200 devido a existência de um evento S-2299 ou S-2399 no período.

A aba **Inconsistências** irá exibir inconsistências gerais que ocasionam que o evento não seja gerado e também as verbas que são desprezadas da geração do evento devido natureza ou incidência para IRRF, por exemplo verba do desconto de IRRF ou pensão alimentícia, que apenas são geradas no evento S-1200. Outro exemplo são verbas de pagamento da diferença do dissídio que ao invés de ser gerada no grupo <*infoPerApur*> é gerada no grupo <*infoPerAnt*>, nessa aba também é demonstrada as verbas que não estão sendo enviadas no evento S-1200, isso ocorre pois a verba esta informada no campo **RV\_CODCOM\_** de outra verba indevidamente.   
  
A aba **Legenda** irá exibir a descrição para os códigos de Tipos de Estabelecimento, Indicador do Simples, Tipo da Verba, Tipos de Dependente e Indicador de Tipo de Recolhimento do Múltiplo Vínculo.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-1200- Como calcular Rescisão para Estagiário através da rotina de Rescisão do SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026466213)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
