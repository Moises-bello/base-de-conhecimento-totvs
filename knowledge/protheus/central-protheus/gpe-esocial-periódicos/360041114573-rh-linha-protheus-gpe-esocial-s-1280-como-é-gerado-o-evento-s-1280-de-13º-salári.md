---
article_id: 360041114573
category: GPE - eSocial - Periódicos
content_hash: fe12f36835fd968a877db09b92599153fd2b79ea5b402fb3ca9125d98a5cd3f1
fetched_at: '2026-06-28T22:45:09.014968+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1280 - Como é gerado o evento S-1280
  de 13º Salário
type: support-article
updated_at: '2025-07-21T18:24:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041114573-RH-Linha-Protheus-GPE-eSocial-S-1280-Como-%C3%A9-gerado-o-evento-S-1280-de-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19447029227287)** Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como é gerado o evento S-1280 de 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. É necessário que esteja atualizado com os pacotes disponíveis em nossa página [**eSocial | Protheus - Entregas Legais**](http://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais#);2. A informação encaminhada para o TAF depende da parametrização correta e do cálculo da Desoneração do roteiro de 13º Salário (132) efetuado através do GPE (GPEM013), para orientações relacionadas aos parâmetros e ao cálculo acesse o *link* da**[Desoneração da Folha](http://tdn.totvs.com/x/pFkYDQ)**.  
  
O evento S-1280 do **eSocial** envia somente o percentual da contribuição para o governo, os valores de faturamento da desoneração são gerados no **REINF**.  
  
Vale ressaltar que a desoneração sempre será por empresa, se existir 2, 3 ou mais filiais, haverá a soma dos valores que constam na tabela S033 de todas as filiais para realizar o cálculo. No [leiaute vigente do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#REGRA_MESMO_PROCEMI) informa que o evento deve ser enviado com o número de inscrição do contribuinte conforme informado no S-1000  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27085200529303)  
  
O**[Manual de Orientações eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023-com-marcacoes.pdf) página 187** também informa como deve ser efetuado o cálculo da alíquota que deve ser informada através do evento S-1280.  
  
2.1. Se a empresa for totalmente desonerada deve ser informado [0] no campo de percentual de  
redução da alíquota patronal {**percRedContrib**}. Caso a empresa seja desonerada parcialmente, a  
contribuição previdenciária patronal é ajustada ao percentual resultante da razão entre a receita  
bruta de atividades ou produtos não desonerados e a receita bruta total, devendo ser informado o  
valor no percentual entre 0 e 100 com duas casas decimais (separadas por ponto).  
  
**Exemplo**: Cálculo do percentual relativo as atividades não desoneradas:  
a. Valor da receita bruta total=R$ 100.000.000,00  
b. Valor da receita bruta das atividades desoneradas = R$ 57.500.000,00  
c. Valor da receita bruta das atividades não desoneradas = R$ 42.500.000,00  
d. Cálculo do coeficiente de ajuste: **R$ 42.500.000,00: R$ 100.000.000,00 = 42,50**  
e. O percentual de 42,50% deve ser informado no campo **{percRedContrib}** com cinco dígitos sendo duas casas decimais, **no seguinte formato: [042.50] (com o ponto separando os decimais).**  
**Exemplo Calculo Desoneração de 13º Salário no SIGAGPE:**  
Preenchimento da tabela S033, no módulo do GPE, localizada no menu: Atualizações > Definições Cálculo > Manutenção Tabelas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19447029260823)  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9830456684183)**Log de ocorrência da rotina de Desoneração, localizada no menu: Atualizações - Definições Cálculo - Manutenção Tabelas![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9830511601559)  
  
3. Na rotina de Eventos Periódicos deve ser selecionado o evento **S-1280**, o mês **12/2022** com a opção **Referente a 13º** igual a **SIM**;![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9830517278871)

4. No TAF o evento S-1280  pode ser visualizado através da rotina **Informações Complementares Periódicos** (**TAFA410**).  
Menu: Atualizações  > Eventos Esocial > Periódicos > Info. Complem. Per.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19447029263767)  
  
Dentro da rotina é possível consultar as informações que serão enviadas ao RET (Governo).  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9830597672727)  
  
Vale ressaltar que o **[Leiaute do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)** prevê que o percentual de redução da contribuição será informado "0 (ZERO)" para empresas totalmente desoneradas.  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9830785788311)  
  
  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - DCTFWEB - Minha base de cálculo está correta mas existe uma pequena diferença no valor apurado no Governo com o valor apurado na minha Folha de Pagamento (centavos/dizima periódica)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041109333/)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
