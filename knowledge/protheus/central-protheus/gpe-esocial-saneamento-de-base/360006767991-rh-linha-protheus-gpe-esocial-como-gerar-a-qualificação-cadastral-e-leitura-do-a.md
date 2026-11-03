---
article_id: 360006767991
category: GPE - eSocial - Saneamento de Base
content_hash: 7bbc29c9a5274b8a102827bdad3a64aa6060c04bddf710833346e94afb206e35
fetched_at: '2026-06-28T22:45:01.613879+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como gerar a Qualificação Cadastral e
  Leitura do Arquivo de Retorno no Protheus, existe uma rotina própria
type: support-article
updated_at: '2024-11-29T18:41:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006767991-RH-Linha-Protheus-GPE-eSocial-Como-gerar-a-Qualifica%C3%A7%C3%A3o-Cadastral-e-Leitura-do-Arquivo-de-Retorno-no-Protheus-existe-uma-rotina-pr%C3%B3pria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28157358932247) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como gerar a Qualificação Cadastral e Leitura do Arquivo de Retorno no Protheus, existe uma rotina própria?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No Protheus existe a rotina GPEM045 (**arquivo magnético**) para gerar o arquivo com extensão TXT, esse arquivo deve ser importado no site do [eSocial](https://portal.esocial.gov.br/institucional/consulta-qualificacao-cadastral). E o próprio governo retorna um outro arquivo TXT que pode ser lido no sistema na rotina GPEM046 (**ler retorno**). Acesse o manual completo da rotina no *link*: [Manual Qualificação Cadastral](http://tdn.totvs.com/x/A4BhEw)

**ESOCIAL SIMPLIFICADO**  
Com a versão simplificada do eSocial, o NIS – Número de Identificação Social **não mais será informado**. Portanto, possíveis inconsistências na base do PIS/PASEP/CNIS não serão impeditivas para o envio dos eventos de admissão/cadastramento inicial.  
A validação de consistência de dados cadastrais será feita **exclusivamente** na base do **CPF**.  
Apesar da **não utilização do NIS** no **eSocial**, a **qualificação cadastral continua sendo imprescindível** para que os eventos enviados sejam apropriados corretamente pelo CNIS, sobretudo para identificação de inconsistências no cadastro referentes a trabalhadores que já possuíam vínculo anterior ao eSocial.  
Ressaltamos a necessidade da consulta e saneamento dos dados cadastrais principalmente para os trabalhadores do serviço público, considerando que a grande maioria destes trabalhadores não tem seus benefícios concedidos pelo INSS, com isso a possibilidade de existir inconsistências cadastrais é grande.  
Para atender à necessidade de consulta dos dados de trabalhadores e beneficiários que não possuem NIS, a Consulta Qualificação Cadastral - CQC foi adaptada para permitir a informação de um NIS padrão, a saber: 13333333332. O NIS padrão pode ser utilizado tanto na consulta online quanto na consulta em lote.   
Em um mesmo lote é possível inserir dados de trabalhadores com NIS real e com o NIS Padrão.  
Quando o NIS Padrão for informado, a validação dos dados cadastrais será realizada apenas na base do CPF.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[Consulta Qualificação Cadastral](https://www.gov.br/esocial/pt-br/empresas/consulta-qualificacao-cadastral)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
