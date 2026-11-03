---
article_id: 8660229195415
category: GPE - eSocial - Carga Inicial
content_hash: 301bc7c0b47707e8308be887de6eac38101c913ce5f46f743e7c768b934ed2ce
fetched_at: '2026-06-28T22:45:03.269704+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 - Identificação de Processo -
  Incidência de Contrib. Previdenciaria deve ser preenchido
type: support-article
updated_at: '2024-07-29T14:16:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8660229195415-RH-Linha-Protheus-GPE-eSocial-S-1010-Identifica%C3%A7%C3%A3o-de-Processo-Incid%C3%AAncia-de-Contrib-Previdenciaria-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00min** **Dúvida**Erro ao enviar evento S-1010 para os identificadores 1891 e 1892 - Código da Ocorrência: 8 - Descrição : Grupo "Identificação de Processo" - Incidência de Contrib. Previdenciária; deve ser preenchido.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões**Solução**Os identificadores 1891 e 1892 devem ser criados para casos que existe **suspensão de incidência sobre salário de contribuição em decorrência de decisão judicial em verbas de férias.**  
A obrigatoriedade de cadastro dessas verbas foi corrigida, segue *link* para o acumulado: [Atualização de Arquivos/Fontes RH Expedição Continua](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao_continua)  
  
Caso permaneça, é porque o sistema está validando alguma **outra verba com incidência 91/95,** faça uma analise em seu cadastro de verbas.  
Gere a tabela SRV através da consulta genérica, para facilitar a analise pois é possível gerar em planilha. Verifique se existe alguma outra verba com incidência 91/95 no campo de contribuição previdenciária da aba esocial.   
Após analisar, se houver alguma verba com essa incidência, verifique se é correto ou se existe processo para outro tipo de situação.  
  
**Observação:**Para verbas/rubricas com a incidência previdenciária igual a 91/95 obrigatoriamente deverá existir o grupo com informações relativas ao processo. Caso a empresa não possua, não deverá ser enviado ao esocial e o cadastro poderá ser excluído se já foi realizado.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12756129573655)  
  
O artigo a seguir mostra como gerar tabelas na consulta genérica: [RH - Linha Protheus - GPE - Impressão de Relatório de Funcionários pela Consulta Genérica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052063113-RH-Linha-Protheus-GPE-Impress%C3%A3o-de-Relat%C3%B3rio-de-Funcion%C3%A1rios-pela-Consulta-Gen%C3%A9rica?source=search)  
  
Veja o artigo sobre a criação dos identificadores 1891 e 1892: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/6778582967063>  
  
Para enviar o evento S-1070 veja nosso artigo: [RH - Linha Protheus - GPE - eSocial - S-1070 - Quais são os artigos e documentações relacionados ao evento S-1070 (Processos Administrativos/Judiciais)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052499193-RH-Linha-Protheus-GPE-eSocial-S-1070-Quais-s%C3%A3o-os-artigos-e-documenta%C3%A7%C3%B5es-relacionados-ao-evento-S-1070-Processos-Administrativos-Judiciais-)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
