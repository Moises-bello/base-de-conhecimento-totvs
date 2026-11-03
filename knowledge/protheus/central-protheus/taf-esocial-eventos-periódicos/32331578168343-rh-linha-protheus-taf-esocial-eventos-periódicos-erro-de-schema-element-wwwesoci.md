---
article_id: 32331578168343
category: TAF - eSocial - Eventos Periódicos
content_hash: 354f09cd26348bf1b9f71d7cada01cf1364d9ddd462844b6a6a53be6925e05d5
fetched_at: '2026-06-28T22:45:18.977478+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - Erro de schema:
  Element ''{www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00}instFinanc'' - nrDoc'':
  [facet ''pattern''] The value ''xxxxxxx'' is not accepted by the pattern ''\d{8,12}''.'
type: support-article
updated_at: '2026-06-26T11:17:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32331578168343-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-Erro-de-schema-Element-www-esocial-gov-br-schema-evt-evtDeslig-v-S-01-03-00-instFinanc-nrDoc-facet-pattern-The-value-xxxxxxx-is-not-accepted-by-the-pattern-d-8-12
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32331592931991) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Ao tentar transmitir ao eSocial o evento S-1200 de colaboradores que possuem informação de empréstimo eConsignado, ocorre os erros de Schemas abaixo:

***Element '{http://www.esocial.gov.br/schema/evt/evtRemun/v\_S\_01\_03\_00}instFinanc': [facet 'pattern'] The value '' is not accepted by the pattern '\d{3}'.***

***Element '{http://www.esocial.gov.br/schema/evt/evtRemun/v\_S\_01\_03\_00}nrDoc': [facet 'pattern'] The value 'xxxxxxx' is not accepted by the pattern '\d{8,12}'.***  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - e-Social - Eventos Periódicos - S-1200 (TAFA250) - Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social - Á partir da versão 12.1.33

**Solução**Os erros de Schemas ocorrem devido a falta de atualização da tabela autocontida T8D, que contém os códigos das instituições financeiras, conforme a tabela 37, oficial do eSocial;  
E pela falta de atualização do TSS.

**ATENÇÃO!**

**Para sanar o ERRO é de EXTREMA importância  seguir TODOS os passos na sequência:**

**1.** Valide se seu ambiente está atualizado, com a última expedição contínua do TAF - OBRIGATÓRIO (a partir de 04/2025)  
Abra a tela de diagnóstico e verifique a data da última atualização, a data do dicionário, RPO e se a autocontida está atualizada:  
[RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063)  
  
*Demarcamos os campos que precisam ser validados:*   
Verificar se a data á partir de 04/2024 e as autocontidas á partir da versão 1033.75

Neste exemplo, o ambiente está desatualizado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331592932503)

**2.** Se necessário, atualize o TAF com a última Expedição Contínua, o documento abaixo possui os links e explica como atualizar.  
[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)  
  
  
**3.** Após aplicar a patch, rode primeiro o UPDDIST (caso não tenha rodado UPDDISTR quando atualizou a expedição continua).  Aplicando a patch do passo 3, atualize as autocontidas (Wizard de Conf. TAF);  
[RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Executando UPDDISTR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034765854)

[RH - Linha Protheus - TAF - eSocial - Configuração - Como atualizar as tabelas autocontidas no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017826812)

**4**. Atualize os **SCHEMAS do  TSS,** utilizando a documentação abaixo:

[RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Links para atualizar o TSS - Transmissão de Documentos Eletrônicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7658806742679)

**5**. Exclua o evento do TAF e integre novamente.

**SAIBA MAIS**

Para saber mais consulte os links abaixo: 

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
