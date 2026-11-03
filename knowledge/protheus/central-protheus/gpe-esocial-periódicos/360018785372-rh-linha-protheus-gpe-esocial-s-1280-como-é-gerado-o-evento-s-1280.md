---
article_id: 360018785372
category: GPE - eSocial - Periódicos
content_hash: 3cb5df564ec1f4d010ab2a3a925f0c6ce6d6b4aa2197f154ff8bdecde5bb5961
fetched_at: '2026-06-28T22:45:09.008117+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1280 - Como é gerado o evento S-1280
type: support-article
updated_at: '2023-03-23T21:23:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018785372-RH-Linha-Protheus-GPE-eSocial-S-1280-Como-%C3%A9-gerado-o-evento-S-1280
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: 00:02:00 min **Dúvida**Como é gerado o evento S-1280?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**1. A informação encaminhada para o TAF depende da parametrização correta e do cálculo da Desoneração efetuado através do GPE (GPEM013), para orientações relacionadas aos parâmetros e ao cálculo acesse o link da**[Desoneração da Folha](http://tdn.totvs.com/x/pFkYDQ)**.

No S-1280 o percentual de redução da contribuição **será informado "0 (ZERO)"** para empresas totalmente desoneradas.  
  
O evento S-1280 do **eSocial** envia somente o percentual da contribuição para o governo, os valores de faturamento da desoneração são gerados no **REINF**.  
  
Vale ressaltar que a desoneração sempre será por empresa, se existir 2,3 ou mais filiais haverá a soma dos valores que constam na tabela S033 de todas as filiais para realizar o cálculo. No leiaute do eSocial informa que o evento deve ser enviado com "Raiz do CNPJ (Oito primeiros dígitos)".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13321920037527)  
  
O [**Manual de Orientação do eSocial v. S-1.1 - consolidado até NO nº 02/2023**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-02-2023.pdf) também informa como deve ser efetuado o cálculo da alíquota que deve ser informada através do evento S-1280.

**MOS Layout S1.1 página 181**

**2.2** Se a empresa for totalmente desonerada deverá ser informado Zero, no campo de percentual de redução da alíquota patronal {**percRedContrib**}. Caso a empresa seja desonerada parcialmente a contribuição previdenciária patronal será ajustada ao percentual resultante da razão entre a receita bruta de atividades ou produtos não desonerados e a receita bruta total, devendo ser informado o valor no percentual entre 0 e 100 com duas casas decimais (separadas por ponto).

*Exemplo: Cálculo do percentual relativo as atividades não desoneradas:*  
*a. Valor da receita bruta total=R$ 100.000.000,00*  
*a. Valor da receita bruta das atividades desoneradas = R$ 60.000.000,00*  
*b. Valor da receita bruta das atividades não desoneradas = R$ 40.000.000,00*  
*d. Cálculo do coeficiente de ajuste: **R$ 40.000.000,00: R$ 100.000.000,00 = 40***  
*e. O percentual de 40% deve ser informado no campo {**percRedContrib**} com cinco dígitos sendo duas casas decimais, **no seguinte formato: 040.00 (com o ponto separando os decimais).*****Exemplo Calculo Desoneração SIGAGPE**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015277991/mceclip0.png)  
  
2. Na rotina Eventos Periódicos deve ser selecionado o evento S-1280 e o mês da competência no qual ja foi realizado o calculo da Desoneração (GPEM013).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014919831/mceclip1.png)  
  
3. No TAF o evento S-1280  pode ser visualizado através da rotina **Informações Complementares Periódicos** (**TAFA410**), no **Menu** fica localizado em "**Atualizações  > Eventos Esocial > Periódicos > Info. Complem. Per.**".  
  
Dentro da rotina é possível consultar as informações que serão enviadas ao RET (Governo).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015232632/mceclip1.png)  
  
Vale ressaltar que o **[Leiaute do eSocial](http://portal.esocial.gov.br/institucional/documentacao-tecnica)** prevê que o percentual de redução da contribuição será informado "0 (ZERO)" para empresas totalmente desoneradas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13322062683671)  
  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[MP - GPE - eSocial - DCTFWEB - Minha base de cálculo está correta mas existe uma pequena diferença no valor apurado no Governo com o valor apurado na minha Folha de Pagamento (centavos/dizima periódica)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041109333/)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Chatbot eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
