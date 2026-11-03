---
article_id: 13403244147735
category: GPE - eSocial - Periódicos
content_hash: cc2995d1d0cbef43417505a60619351014d072bc8115003bd7561405a558c7af
fetched_at: '2026-06-28T22:45:07.578150+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Instrução Normativa  RFB Nº 2.137, DE
  21 DE MARÇO DE 2023 relativos ao IRRF na DCTFWeb
type: support-article
updated_at: '2025-07-24T19:53:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13403244147735-RH-Linha-Protheus-GPE-eSocial-Instru%C3%A7%C3%A3o-Normativa-RFB-N%C2%BA-2-137-DE-21-DE-MAR%C3%87O-DE-2023-relativos-ao-IRRF-na-DCTFWeb
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15248851533975) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Foi publicada**a [IN 2137/2023](https://www.in.gov.br/en/web/dou/-/instrucao-normativa-rfb-n-2.137-de-21-de-marco-de-2023-472363492),** ratificando que os IRRFs originários do eSocial serão incluídos no controle de DCTFWeb e inserindo também o art. 19-B na IN 2005/2021.   
Qual atualização é necessária para o IR na DTCFWeb? O que parametrizar no sistema para o IR na DCTFWeb?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Conforme link da IN 2137/2023: <https://www.in.gov.br/en/web/dou/-/instrucao-normativa-rfb-n-2.137-de-21-de-marco-de-2023-472363492>  **“**Art. 19-B. A**DCTFWeb substituirá a DCTF** como instrumento de confissão de dívida e de constituição de créditos tributários **relativos ao IRRF** decorrentes**da relação de trabalho**, apurados**por meio do eSocial**, cujos **fatos geradores ocorrerem a partir do mês de maio de 2023**.  
§ 1º O disposto no caput aplica-se aos códigos de receita 0561, 0588, 0610, 1889, 3533, 3562 e 0473.  
§ 2º Caso a retenção relativa aos códigos previstos no § 1º se refira a rendimentos que não possam ser informados no eSocial, o IRRF deverá ser informado na DCTF, mediante utilização dos códigos 0561-14, 0588-07, 1889-02, 3533-02, 3562-02 ou 0473-04.” (NR).” (nota adicionada em 24/03/2023)

**IMPORTANTE:**

O código de Receita é definido com base na Categoria do eSocial e informações relativas a residentes no exterior, esse código não é enviado em nenhum evento do eSocial, **ele é apresentado apenas no retorno do governo no evento S-5002.**

[Substituição da DCTF pela DCTFWeb em relação ao IRRF decorrente das relações de trabalho, apurado por meio do eSocial, ocorrerá a partir do mês de maio de 2023](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2023/marco/receita-federal-comunica-a-substituicao-de-tributos-da-dctf-pela-dctfweb)  
  
O **DCTFWeb apura os valores com base nos dados enviados através dos eventos eSocial**, dessa forma orientamos para que sejam revistos os seguintes pontos:  
  
1 - Confira o campo Código Incidência **IRRF (****RV\_INCIRF)**, **atualizando** todas as verbas e especial atenção para as **verbas de retenção de IRRF.** [RH - Linha Protheus - GPE - eSocial - S-1010 - Após a transmissão dos eventos iniciais (carga inicial), como enviar um único registro para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341633)  
**Atenção com a competência** enviada no evento S-1010, pelo menos anterior ao mês que está sendo enviado o evento de pagamento.

2 - Os códigos da Consulta Padrão são lidos da Tabela **S138 - Incidência Tributária Rubrica IRRF.** Atenção ao **Término de Validade do Código**. Se necessário valide com a [tabela 21 do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1.1-nt-01-2023/tabelas.html#21)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13403031197847)

3 - Alimente corretamente a tabela de Histórico de Contratos (RGE) para funcionários expatriados.  (Atualizações\Funcionários\Histórico Contratos)

4 - Confira através do **relatório** disponível na geração de periódicos, se há verba com o RV\_INCIRF incorreto, para isso, na rotina de **Geração de Eventos Periódicos** utilize essa opção: [RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-antes-de-integrar-o-evento-peri%C3%B3dico-para-o-TAF)

![](https://tdn.totvs.com/download/attachments/747330825/image2023-3-24_15-57-6.png?version=1&modificationDate=1679684226353&api=v2)

5 -  Estará disponível na tabela Excel o campo Incidência IRRF eSocial

![](https://tdn.totvs.com/download/attachments/747330825/image2023-3-24_16-38-35.png?version=1&modificationDate=1679686716147&api=v2)  
  
O sistema deve estar **atualizado com os pacotes disponíveis em Atualizações da pagina de entregas legais:** <https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais>   
  
Consultoria de segmentos:

[**Novo Cálculo de Imposto de Renda**](https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/)

* Folha de Pagamento Abril/2023 paga em Maio/2023 – Não há instrução oficial quanto a reabertura da folha, o empregado pode realizar o ajuste na declaração anual de Imposto de Renda.

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
