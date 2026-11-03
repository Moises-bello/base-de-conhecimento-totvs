---
article_id: 360034970894
category: GPE - eSocial - Periódicos
content_hash: 052ddd1b0f58a38964f2280d6c5cd856e88c33c733c35b6320a6a7ce0e116641
fetched_at: '2026-06-28T22:45:08.884051+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - Código da Ocorrência 686: O
  CNPJ deve estar ativo no Cadastro de CNPJ da RFB.'
type: support-article
updated_at: '2025-07-21T19:43:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034970894-RH-Linha-Protheus-GPE-eSocial-S-1210-C%C3%B3digo-da-Ocorr%C3%AAncia-686-O-CNPJ-deve-estar-ativo-no-Cadastro-de-CNPJ-da-RFB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27150891039127) Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Sequência: 000001 - Tipo: Erro - Código da ocorrência: 686  
Localização: /eSocial/evtPgtos/ideBenef/infoIRComplem/planSaude/cnpjOper  
Descrição: O CNPJ deve estar ativo no Cadastro de CNPJ da RFB. Ação Sugerida: O CNPJ informado devera estar ativo (CNPJ não poderá pertencer a pessoa jurídica Inapta (situação=4) pelo motivo de Inexistência de Fato (motivo=15)) no Sistema CNPJ, na data atual.  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal- Todas as Versões  
  
**Causa**   
Esse retorno ocorre devido a estar incorreto o **CNPJ** do fornecedor de assistência medica ou odontologia vinculado ao plano de saúde do trabalhador que está sendo enviado no **S-1210**.  
 **​​****Solução**Para correção efetue os seguintes procedimentos:  
  
1. Acesse no modulo SIGAGPE (07) na rotina manutenção de tabelas no caminho abaixo e verifique se **CNPJ** e **ANS**código estão corretos nas tabelas **S016** e **S017**.  
Caminho: *atualizações > definições de Cálculo > Manutenção de Tabelas   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33618772019223)  
S016 - Assistência Médica - Fornecedor   
S017 - Assistência Odontológica - Fornecedor;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33618807009175)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33618807010967)  
**Observação:** O **CNPJ** e código **ANS** devem ser números validos.*

2. Após ajuste efetuar uma nova geração do evento **S-1210** e transmita para o governo.  
  
3. Caso necessário, gere o XML do S-1210 ERP e TAF e valide o conteúdo da tag cnpjOper  
[RH - Linha Protheus - GPE - eSocial - S-1210 - Como gerar os arquivos XML do evento S-1210 (Pgto Rend Trab.) no modulo SIGATAF para análise](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006741342-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-gerar-os-arquivos-XML-do-evento-S-1210-Pgto-Rend-Trab-no-modulo-SIGATAF-para-an%C3%A1lise)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
