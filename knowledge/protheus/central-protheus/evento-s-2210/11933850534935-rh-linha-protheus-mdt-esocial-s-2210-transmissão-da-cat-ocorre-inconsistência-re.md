---
article_id: 11933850534935
category: Evento S-2210
content_hash: f3e9d31305b7319f41fa6be823eb0de6388d1cae4ecf4e962e0f2adc0384779f
fetched_at: '2026-06-28T22:45:24.528636+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2210 -​ Transmissão da CAT ocorre inconsistência
  referente as tags ultDiaTrab e houveAfast
type: support-article
updated_at: '2024-07-10T15:21:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11933850534935-RH-Linha-Protheus-MDT-eSocial-S-2210-Transmiss%C3%A3o-da-CAT-ocorre-inconsist%C3%AAncia-referente-as-tags-ultDiaTrab-e-houveAfast
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24790046591767) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Na transmissão do evento S-2210 no TAF está apresentando inconsistência:   
  
Campo de preenchimento obrigatorio: Ultimo Dia Trabalhado. - Localização : /eSocial/evtCAT/cat/**ultDiaTrab**  
Campo de preenchimento obrigatorio: Houve Afastamento. - Localização : /eSocial/evtCAT/cat/**houveAfast**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**De acordo com layout eSocial, os campos "último dia trabalhado" (TNC\_DTULTI) e "houve afast" (TNC\_AFASTA) no cadastro de Acidente (MDTA640) do módulo Medicina e Segurança do Trabalho, passaram ser obrigatórios se a data do acidente for maior ou igual que **16/01/2023**.  
A inconsistência é apresentada se o ambiente não estiver com as últimas atualizações do Acumulado MDT, TAF e Schemas do TSS, essas atualizações são importantes para a geração dos eventos de acordo com alteração do Layout do Governo.   
  
**Solução**Verifique se o seu sistema está atualizado com dicionários e pacotes de expedição continua do MDT, pacote de acumulado do eSocial, e as atualizações de Schemas do TSS liberados a partir de 12/2022, conforme links a seguir, pois essas atualizações são necessários para que o sistema gere eventos de acordo com a alteração de leiaute.  
  
Links:  
1. [Pacote Correções e Dicionário Diferencial eSocial](https://suporte.totvs.com/portal/p/10098/download#000052/all/all/search/TAF_ESOCIAL_REINF_PROTHEUS.ZIP)   
2. [Pacote e Dicionário Correções Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA.ZIP)   
3. [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)  
  
Após atualização, deverá gerar novamente o evento S-2210 no MDT para o TAF e efetuar a transmissão ao RET. Se no retorno do Governo, a inconsistência continuar sendo apresentada, é necessário que envie no ticket os arquivos XML do módulo MDT e TAF, conforme artigo:   
[Como gerar o XML do evento S-2210 (Comunicação de Acidente de Trabalho) no modulo MDT e TAF para analise do suporte técnico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5754090383383-RH-Linha-Protheus-MDT-eSocial-S-2210-Como-gerar-o-XML-do-evento-S-2210-Comunica%C3%A7%C3%A3o-de-Acidente-de-Trabalho-no-modulo-MDT-e-TAF-para-analise-do-suporte-t%C3%A9cnico)  
  
**Observação:** É necessário que retorne com os dois XMLs conforme orientação do artigo.  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
