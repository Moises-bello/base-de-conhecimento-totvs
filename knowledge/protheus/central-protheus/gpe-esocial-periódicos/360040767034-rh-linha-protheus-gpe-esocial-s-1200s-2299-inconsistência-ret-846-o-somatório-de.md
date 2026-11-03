---
article_id: 360040767034
category: GPE - eSocial - Periódicos
content_hash: e8483eecd42e87847c55662c3cd78b71ebed4fea8b69ae29d0b6f9e0e3e09edb
fetched_at: '2026-06-28T22:45:08.835182+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Inconsistência RET 846
  - O somatório de cada um dos descontos de Contribuição Previdenciária (codIncCP
  = [31, 32, 34, 35]) e de IRRF (codIncIRRF = [31, 32, 33, 34]) não pode ser negativo,
  ou seja,
type: support-article
updated_at: '2025-07-23T11:50:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040767034-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Inconsist%C3%AAncia-RET-846-O-somat%C3%B3rio-de-cada-um-dos-descontos-de-Contribui%C3%A7%C3%A3o-Previdenci%C3%A1ria-codIncCP-31-32-34-35-e-de-IRRF-codIncIRRF-31-32-33-34-n%C3%A3o-pode-ser-negativo-ou-seja
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24426932234903)** Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**  
Sequência: 000001 - Tipo: Erro - **Código da Ocorrência: 846** - Descrição: O somatório de cada um dos descontos de Contribuicao Previdenciaria (codincCP = [31, 32, 34, 35]) e de IRRF (codincIRRF = [31, 32, 33, 34]) não pode ser negativo, ou seja, os vencimentos não podem ser superiores aos descontos. - Localização:  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**A inconsistência 846 ocorre porque no evento S-1200/S-2299 do funcionário em questão, as rubricas/verbas com **Incidência INSS eSocial** [31, 32, 34, 35] e **Incidência IRRF eSocial** [31, 32, 33, 34], estão com divergências no cadastro ou o valor está incorreto.

**Validação**Para as rubricas cujo {codIncCP} em S-1010 = [31, 32, 34, 35] e {codIncIRRF} em S-1010 = [31, 32, 33, 34], o somatório do valor das rubricas cujo {tpRubr} em S-1010 = [2, 4] deverá ser maior ou igual ao somatório do valor das rubricas cujo {tpRubr} em S-1010 = [1, 3], considerando cada {codIncCP} e {codIncIRRF} individualmente.  
  
Imagem do leiaute 1.1 - [Regra Demonstrativo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/regras.html)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12424567363479)  
  
**Solução**1. Verifique **dentro do TAF** no evento S-1200 se existe alguma **rubrica com valor negativo**, caso exista encaminhe o print da rubrica, pois o sistema não pode gerar valor negativo no S-1200, caso esteja correto pule para o passo 2;  
  
2. Verifique se todas as **verbas calculadas na folha de pagamento** foram **integradas no evento S-1200** desse trabalhador. Utilize o **relatório de conferência do evento S-1200** para identificar as verbas integradas e a incidência de cada uma delas.  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-antes-de-integrar-o-evento-peri%C3%B3dico-para-o-TAF?source=search)  
  
Caso a inconsistência 846 seja apresentada na transmissão do evento S-2299, utilize o relatório **relatório de conferência do evento S-2299.**[RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia em lote do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13271348438295-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-em-lote-do-evento-S-2299?source=search)  
  
3. Verifique no relatório de conferencia se consta alguma verba desprezada. Essa informação será apresentada na aba **Inconsistência**.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27447620355351)  
  
4. Faça um filtro nas colunas **Incidência INSS eSocial** com os códigos [31, 32, 34, 35] ou **Incidência IRRF eSocial** com os códigos [31, 32, 33, 34]. Normalmente as verbas com tais incidências são do tipo Descontos, contudo, se houver calculo de Férias no mês, serão geradas as verbas de contrapartida e deve ser observado a **somatória dessas verbas com o tipo 2 e 4 que deve ser maior ou igual a somatória das verbas com o tipo 1 e 3**.  
  
**Legenda para Tipo de Verba:**  
1 - Provento  
2 - Desconto  
3 - Base Provento (Informativa)  
4 - Base Desconto (Informativa Dedutora)  
  
**Observação**: configuração das verbas presentes neste relatório é meramente ilustrativa.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12423919239703)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12423973281559)  
  
5. Caso seja identificado verbas que não deveriam ter incidência INSS [31, 32, 34, 35] e/ou incidência IRRF [31, 32, 33, 34], será necessário ajustar o cadastro das verbas e enviar o evento S-1010 referente a alteração.  
O ajuste de verbas (S-1010) realizado no sistema, deve ser enviado ao esocial com competência igual ou anterior a competência do evento de pagamento (S-1200/S-2299).  
  
**Exemplo:**

**1)** É esperado que apenas a verba de INSS (Id 0064) tenha **Incidência INSS eSocial** (codincCP) = 31. Havendo outra (s) verba (s) com a mesma incidência, será necessário revisar o cadastro.  
**2)** Se houver calculo de Férias no período, a **Incidência INSS eSocial** (codincCP) = 31 também deverá constar no cadastro das verbas com Id 0065 e 1871  
  
[RH - Linha Protheus - GPE - eSocial - S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512-MP-GPE-eSocial-S-5001-Como-ajustar-incid%C3%AAncia-e-validade-de-rubricas-no-governo-TAF-e-GPE?source=search)  
  
6. O valor calculado na verba de INSS com **Natureza 9201** e **incidência INSS eSocial 31** não pode ser superior ao valor do teto de desconto de INSS (tabela vigente do INSS).  
  
Após ajuste de verbas, o evento de pagamento deve ser excluído do eSocial e gerado novamente no GPE para envio e ajuste do eSocial.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página ***[TOTVS Informa](https://informa.totvs.com/)*** selecione em categorias a área e pesquise por "**Eventos**".
