---
article_id: 360028575974
category: GPE - eSocial - Carga Inicial
content_hash: 59a75197c67206752c0955f8c835470e559aeaab5bf59e1f3e5ac61046b2b544
fetched_at: '2026-06-28T22:45:03.117278+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como integrar os eventos de uma nova
  Filial para ao TAF
type: support-article
updated_at: '2024-11-29T16:18:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028575974-RH-Linha-Protheus-GPE-eSocial-Como-integrar-os-eventos-de-uma-nova-Filial-para-ao-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28153805306775) Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**eSocial - Como integrar os eventos de uma nova Filial para ao TAF?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A premissa é que já tenha sido realizado o cadastro da nova Filial no Configurador (SIGACFG), o segundo passo é ajustar o Complemento Cadastral do TAF para essa Filial, para auxílio neste processo acesse o artigo:**[TAF - COMPLEMENTO CADASTRAL (TAFA050)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027279052-TAF-COMPLEMENTO-CADASTRAL-TAFA050-?source=search)**.  
  
O terceiro passo, caso necessário, é fazer os cadastros pertinentes em "**Manutenção de Tabelas**" do SIGAGPE.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042773893)  
  
**As principais tabelas** que influenciam na integração do **GPE** com o **TAF** dos eventos **S-1005** e **S-1020** são:  
**S037 - Encargos Empresa**  
**S038 - Outras Entidades**  
**S119 - Dados eSocial - Matriz/Filiais**  
  
O preenchimento dessas tabelas são de responsabilidade da própria Empresa, pois depende da estrutura de cada Empresa e envolvem informações tributárias.  
  
Caso os seus parâmetros do eSocial já estejam ativos no momento que gravar os registros em cada uma das tabelas do SIGAGPE o Sistema tentará integrar com o TAF os **eventos de Tabela** do eSocial pertinentes em cada situação, para mais informações sobre os parâmetros do eSocial acesso o artigo: [**Parâmetros 3ª Fase esocial**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004981112).  
  
**Em último caso**, se os eventos não forem gerados automaticamente você pode acessar a rotina de **Carga Inicial (GPEM023)** do SIGAGPE e gerar um relatório de inconsistências e/ou realizar essa carga manualmente selecionando somente a nova Filial.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[MP - GPE - eSocial - S-1005 - Como devem ser configurado as tabelas S119 (Dados eSocial) e S120 (Dados eSocial Entidades Educativas) na rotina manutenção de tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025814093)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
