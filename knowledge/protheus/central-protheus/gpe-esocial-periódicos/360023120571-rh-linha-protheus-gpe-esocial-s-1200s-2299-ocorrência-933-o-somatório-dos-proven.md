---
article_id: 360023120571
category: GPE - eSocial - Periódicos
content_hash: 6c45640b7bc1cb086ddaa5b4b6c6aab893f06f97eafcb16c920561eade460cf6
fetched_at: '2026-06-28T22:45:07.350070+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Ocorrência 933 - O somatório
  dos Proventos deve ser maior ou igual ao somatório dos Descontos no Demonstrativo
  de Pagamento X. Valor Encontrado: -Y'
type: support-article
updated_at: '2025-07-23T11:45:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023120571-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Ocorr%C3%AAncia-933-O-somat%C3%B3rio-dos-Proventos-deve-ser-maior-ou-igual-ao-somat%C3%B3rio-dos-Descontos-no-Demonstrativo-de-Pagamento-X-Valor-Encontrado-Y
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27176607669527)** Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Código da Ocorrência **933** - Descrição : O somatório dos Proventos deve ser maior ou igual ao somatório dos Descontos no Demonstrativo de Pagamento X. Valor Encontrado: -Y.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Essa é uma mensagem de inconsistência do **RET (Governo)** que retorna quando o **Evento Periódico S-1200** é enviado com **somatório dos Descontos sendo maiores que os Proventos**, consequentemente o valor enviado é **negativo**.  
  
**Solução**Verifique abaixo algumas verificações que devem ser realizadas:  
  
**Cenário de erro 1: A soma dos descontos está maior que dos proventos**Deve ser verificado o tipo das verbas presentes no calculo. No relatório do evento S-1200 é possível filtrar as verbas de acordo com o Tipo. Sendo: 1 - **Provento** (vencimento), 2 - **Desconto**, 3 - **Base Provento** (Informativa) e 4 - **Base Desconto** (Informativa Dedutora). A somatória das verbas do tipo Desconto NÃO pode ser maior do que a somatória das verbas do tipo Provento.  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-antes-de-integrar-o-evento-peri%C3%B3dico-para-o-TAF?source=search)  
  
Em caso de mês de desligamento, gerar o relatório do S-2299 conforme documentação   
[RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299?source=search)   
  
Imagem do relatório - filtro Tipo da Verba = 1 - **Provento**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12754000408471)  
  
imagem do relatório - filtro Tipo da Verba = 2 - **Desconto**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12754435361559)  
  
**Cenário de erro 2:** esse erro pode ocorre também quando **a configuração incorreta do campo Verbas para Dissidio RV\_CODCOM**.  
  
Nesse cenário alguma(s) verba(s) da folha de pagamento não são enviadas ao **TAF** na aba de remuneração período de apuração (**infoPerApur**), porque estão erroneamente configuradas para dissídio no campo **Verbas p. Diss.** (RV\_CODCOM) do SIGAGPE. Gerando diferença onde o valor de desconto fica maior que provento.  
  
Para ajuste siga as orientações do artigo: **[Minha verba X não aparece no evento S-1200, como saber se ela está configurada no Protheus como verba de diferença de Dissidio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035981593-MP-GPE-eSocial-S-1200-Minha-verba-X-n%C3%A3o-aparece-no-evento-S-1200-como-saber-se-ela-est%C3%A1-configurada-no-Protheus-como-verba-de-diferen%C3%A7a-de-Dissidio-?source=search)****Cenário de erro 3:** Verifique no relatório de conferencia se consta alguma verba desprezada. Essa informação será apresentada na aba 'Inconsistência'.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27447718461719)  
  
**Atenção**  
- Após ajustes deve ser gerado novamente o evento S-1200;  
- Caso seja identificado que existem mais Descontos do que Proventos, deve ser analisado o calculo, entender se os valores são devidos e, se o tipo da verba está correto, pois pode ser que houve um erro de cadastro;  
- Se identificado erro no cadastro da (s) verba (s), deve ser realizado ajuste, envio do S-1010, exclusão do evento da base do TAF e nova integração do mesmo no GPE;  
- Importante que seja revisado o cadastro das verbas relacionadas no Protheus e no RET (Governo), a fim de garantir que ambos estão iguais;  
Para retificação Verbas/Rubricas acesse: **[S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512)**  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Quais verbas serão enviadas para o eSocial nos casos de Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018355852-RH-Linha-Protheus-GPE-eSocial-S-1200-Quais-verbas-ser%C3%A3o-enviadas-para-o-eSocial-nos-casos-de-Dissidio-Retroativo)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
 *Para conhecimento dos eventos futuros, acessa a nossa página* [***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
