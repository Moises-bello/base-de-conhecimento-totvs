---
article_id: 28057444150551
category: GPE - eSocial - Processo Trabalhista
content_hash: b36bfc9c570289a79df9d37efc17295fad81c32c42c52f70a90abddb8d5fd575
fetched_at: '2026-06-28T22:45:00.475430+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - S-2501 - Como configurar e utilizar o Migrador
  de Tributos do Processo para o leiaute S-1.3
type: support-article
updated_at: '2024-11-28T17:08:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28057444150551-RH-Linha-Protheus-GPE-S-2501-Como-configurar-e-utilizar-o-Migrador-de-Tributos-do-Processo-para-o-leiaute-S-1-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28057444111127) Tempo aproximado para leitura: **00:07:00 min** **Dúvida**Como configurar e utilizar o Migrador de Tributos do Processo para o leiaute S-1.3?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para atender as **alterações** previstas para o **leiaute S-1.3 do eSocial** referente ao evento **S-2501** será necessário realizar a **migração dos dados** das tabelas E0E (Tributos do Processo por Período) e E0F (Tributos do Processo) para as novas tabelas:  
**E0H Tributos do Processo Por Período**   
**E0I Tributos do Processo**

Para utilizar o Migrador realize as **premissas** citadas abaixo:  
**1.** Atualização de dicionário de dados disponivel na pagina de Entregas Legais eSocial: <https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais>  
  
**2.** Cadastrar as consultas **RE0C, RE0P e E0EP** através do módulo **Configurador** conforme a seguir:  
Observação: Essas consultas deverão existir **EXATAMENTE**como demostrado, **para TODOS os grupos de empresa.**Após **acessar o módulo SIGACFG**, selecione a opção Base de Dados > Dicionário > Bases de Dados  
Em seguida, posicione sobre a Empresa Cadastrada para exibir os itens disponíveis, posicione sobre o item **Consultas Padrão** e após no ícone ![](https://tdn.totvs.com/download/thumbnails/870385758/image-2024-9-24_14-5-36.png?version=1&modificationDate=1727198279347&api=v2)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057444113303)

Preencher os dados **exatamente como o exemplo abaixo:**

Onde a consulta se chamará **RE0C**, atuará sobre a tabela **RE0** - Processos, a **expressão** executada é **fConRE0C()** e por fim o **retorno** deverá ser **cProcE0E**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057444114455)![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057449558167)

Após preencher todos os dados, **repita os passos para a consulta RE0P** - Período de Apuração.  
Onde a consulta se chamará **RE0P**, atuará sobre a tabela **RE0** - Processos, a **expressão** executada é **fConRE0P()** e por fim o **retorno** deverá ser **cNrE0E**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057444119191)![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057449561111)

Após preencher todos os dados, **repita os passos para a consulta** **E0EP** - Período de Apuração.  
Onde a consulta se chamará **E0EP**, atuará sobre a tabela **E0E** - Tributos do Processo Por Período, a **expressão** executada é **fConE0EP()** e por fim o **retorno** deverá ser **cPerApE0E**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057449565207)![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057444124567)  
  
**3.**Configurar a rotina do **Migrador - GPEM942** - no **menu** do módulo de Gestão de Pessoal (**SIGAGPE**) através do módulo **Configurador** conforme a seguir:  
Após acessar o módulo **SIGACFG, selecione a opção Ambiente > Cadastros > Menu**Selecione o módulo Gestão de Pessoal (caso não for a sua primeira personalização, irá exibir conforme imagem abaixo):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057449567383)  
  
Adicione os itens de menu através da **opção Adicionar** >> e em seguida cadastre uma nova opção no **submenu Atualizações > Processos Trabalhistas> Processos**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057449572247)  
  
**Atenção aos dados** do novo item de menu:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057444127895)  
  
**4.** Após executar todos os passos anteriores o acesso ao Migrador é liberado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28060576966935)

O migrador permite que o usuário configure filtros diversos de acordo com os campos:  
**Filial do Processo** - Correspondente à Filial ao registro do Processo  
Atenção: Esse filtro mesmo que sejam exibidas os valores integrais da Filial, ele irá considerar o compartilhamento das tabelas RE0 x E0E para filtro dos registros  
**Código do Processo** - Correspondente ao Código cadastrado no cadastro de Processos (APTA100)  
**Número do Processo** - Correpondente ao Número do Processo cadastrado no cadastro de Processos (APTA100)  
**Período de Apuração** - Correpondente ao cadastrado no evento S-2501, formato AAAAMM.  
  
Observação: As consulta padrão do Período de Apuração necessita que ao menos o Código de Processo seja preenchido para retornarem dados na listagem.  
  
As **legendas** disponíveis são:  
**Apto a Migrar** - Os dados não foram migrados para as tabelas E0H e E0I  
**Migrado** - Os dados já foram migrados para as tabelas E0H e E0I.  
  
Caso a **migração ocorra sem falhas** é emitido aviso ao usuário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28060548212247)  
  
Caso a **migração ocorra com falhas** é gerado um Log de Ocorrências, veja exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28060548214039)

O Migrador ainda permite que o usuário migre novamente um Processo que já foi migrado desde que seja realizada sua confirmação.

**Observação**: A rotina não é responsável por realizar um comparativo entre o que está sendo migrado novamente com que já está gravado. **Somente confirme com plena certeza que os registros serão sobrepostos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28060548216727)**Caso as **premissas** a seguir **não sejam atendidas** é emitido um **aviso ao usuário** acerca desta documentação:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28060548218519)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Boletim Técnico Migrador de Tributos do Processo para S-1.3](https://tdn.totvs.com/display/public/PROT/DRHROTPRT-18379+DT+Migrador+de+Tributos+do+Processo+para+S-1.3)  
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
