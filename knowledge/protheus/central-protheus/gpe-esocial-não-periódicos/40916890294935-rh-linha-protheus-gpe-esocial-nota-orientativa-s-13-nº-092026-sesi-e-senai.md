---
article_id: 40916890294935
category: GPE - eSocial - Não Periódicos
content_hash: fae5dd316720869be6dec5539c43ea036cc26d15eca875213796c7262d32f4ba
fetched_at: '2026-06-28T22:45:04.385203+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Nota Orientativa S-1.3 Nº 09/2026 - SESI
  e SENAI
type: support-article
updated_at: '2026-06-03T12:30:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40916890294935-RH-Linha-Protheus-GPE-eSocial-Nota-Orientativa-S-1-3-N%C2%BA-09-2026-SESI-e-SENAI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40916876975767) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O que fazer para atender às orientações da Nota Orientativa S-1.3 Nº 09/2026 do eSocial, referente às contribuições do SESI e SENAI?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para que o eSocial possa gerar as contribuições corretamente, as empresas impactadas devem atualizar as suas Tabelas de **Lotação Tributária (S-1020) com o FPAS relacionado à indústria [507] ou à agroindústria [833]**, alterando o código de terceiros {codTercs} de [0067], [0071] ou [0075] exclusivamente para [0079].  
A atualização deve ser realizada mediante a criação de nova vigência nas tabelas, com **início de validade 05/2026**.

Para isso, não é necessário atualizar nenhuma pacote, somente atualizar os dados no sistema:

**Para a geração do evento S-1020, o usuário poderá adotar dois modelos:**

**Modelo 1:** Cadastro do tipo de lotação apenas no centro de custo.  
Nesse modelo o modo de acesso das tabelas de centro de custo deverá ser exclusivo por empregador.

**Modelo 2:** Rotina para novo controle de lotações. (desobriga o usuário a alterar o compartilhamento da tabela CTT)

Nesse modelo o modo de acesso das tabela de centro de custo pode ser utilizado de forma compartilhada, e as tabelas do novo controle de lotação que serão exclusivas.  Saiba Mais Acesse: [RH - Novo Controle de Lotações](https://tdn.totvs.com/x/PCcxHQ)

**O campo Data de Inicio de Validade é muito importante para cumprimento da Nota Orientativa, então vamos entender como ele funciona:**

**Data Inicio de Validade:**

A geração do evento S-1020 pode utilizar dados provenientes de tres locais:

1 - Tabela S038: Outra Entidades - Data base do sistema

2 - Tabela de CTT: Centro de Custo - Data base do sistema

3 - Tabela RJ3: Lotações do eSocial - Data do Cadastro - Informada em tela

4 - Carga Inicial: Data Informada em tela

Como é feita a geração do evento S-1020, caso alguma tabela dessas seja alterada?

**1 - Tabela S038: Outra Entidades**

1.1 - Em Atualizações\ Definições de Cálculos\Manutenção de Tabelas

1.2 - Escolha a Tabela S038 - Outras Entidades, campo Código de Terceiros e altere conforme a orientação do eSocial

1.3 - Neste momento o programa irá gerar um novo registro S-1020 - Lotação Tributária, do tipo Inclusão, com a tag***iniValid*** com o mês a ano da Data base do Sistema

(Atenção, o código FPAS e terceiros dos Centros de Custo sempre serão considerados acima do que está na tabela S038)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40916876976791)  
  
**2 - Tabela CTT: Centro de Custo**

1.1 - Em Atualizações\ Cadastros\Centro de Custo

1.2 - Alterar os campos Cod FPAS e Cod Terceiros, conforme a orientação do eSocial

1.3 - Neste momento o programa irá gerar um novo registro S-1020 - Lotação Tributária, do tipo Inclusão, com a tag***iniValid*** com o mês a ano da Data base do Sistema

![](https://tdn.totvs.com/download/attachments/1068187402/image-2026-5-14_14-10-7.png?version=1&modificationDate=1778779862243&api=v2)

**3 - Tabela RJ3: Lotações do eSocial**

1.1 - Em Atualizações\ Cadastros\Lotações eSocial

1.2 - Escolha a opção Incluir

1.3 - Inclua os dados da lotação e informe o Mês de Inicio 05/2026

1.3 - Nesse momento o programa irá gerar um novo registro S-1020 - Lotação Tributária, do tipo Inclusão, com a tag***iniValid*** com o mês a ano informado no campo Data Início

[DRHESOCP-12005 DT Novo Controle de Lotações](https://tdn.totvs.com/pages/viewpage.action?pageId=489760572)

Importante:  
  
Inicio em 05/2026, entrega dos eventos 15/06  
  
**Data base:**

![](https://tdn.totvs.com/download/thumbnails/1068187402/image-2026-5-14_14-13-44.png?version=1&modificationDate=1778779862170&api=v2)  
  
**Atenção, o código FPAS e terceiros dos Centros de Custo sempre serão considerados acima do que está na tabela S038.**  
  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/rh/?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-#) selecione em categorias a área e pesquise por "**Eventos**".  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
