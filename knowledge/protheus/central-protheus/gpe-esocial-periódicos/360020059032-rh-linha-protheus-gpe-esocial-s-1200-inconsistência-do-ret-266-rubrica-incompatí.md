---
article_id: 360020059032
category: GPE - eSocial - Periódicos
content_hash: ef24369f8082614cf8add3a7a3fbe6f0a99470c77dae5081a96e373300c19b7c
fetched_at: '2026-06-28T22:45:07.266322+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência do RET - 266
  - Rubrica incompatível com Contribuinte Individual
type: support-article
updated_at: '2025-07-21T15:36:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020059032-RH-Linha-Protheus-GPE-eSocial-S-1200-Inconsist%C3%AAncia-do-RET-266-Rubrica-incompat%C3%ADvel-com-Contribuinte-Individual
---

**Ocorrência** **S-1200 - Inconsistência do RET - 266 - Rubrica incompativel com Contribuinte Individual**  
  
Acao Sugerida:Se for relativa a contribuinte individual, nao podem ser utilizadas rubricas cuja classificacao de incidencia tributaria informada nos campos, codigos de incidencia tributaria de Contribuicao Previdenciaria e codigos de incidencia tributaria de IRRF, seja especifica de segurados empregados.

Portanto, nao sao aceitas rubricas cujo:- Codigo de Incidencia tributaria de Contribuicao Previdenciaria igual a: [12, 21, 22, 32, 51,92, 93, 94], exceto se categoria de trabalhador = [771];- Codigo de Incidencia tributaria de IRRF igual a: [12,13,14,32,33,34];- Codigo de Incidencia tributaria de Contribuicao Previdenciaria seja igual a [34] se a CATEGORIA do respectivo trabalhador for diferente de [711,712,734];- Codigo de Incidencia tributaria de Contribuicao Previdenciaria classificado como [31] se a classificacao tributaria do contribuinte for igual a [21,22] (Pessoa Fisica) e Categoria = Contribuinte individual (7XX), pois nao existe previsao legal de desconto de contribuicao do segurado contribuinte individual que e contratado por outro contribuinte individual, exceto se o tipo de Lotacao da respectiva lotacao = [22] (obra de pessoa fisica).</descricao>  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**A própria mensagem de inconsistência descreve o erro e propõe ação para correção, em outras palavras, o erro ocorre na tentativa de envio do **evento S-1200 de um Trabalhador Sem Vínculo identificado como Contribuinte Individual com Rubricas (S-1010) configuradas com Incidências Tributárias incompatíveis com tal categoria de Trabalhador.**  
  
Portanto, **NÃO** são aceitas Rubricas cujo:  
  
**1.** **Código de Incidência tributaria de Contribuição Previdenciária** igual a:   
12 = Base de Cálculo da Contribuição Previdenciária sobre 13º Salário;  
21 = Base de Cálculo da Contribuição Previdenciária Salário Maternidade;  
22 = Base de Cálculo da Contribuição Previdenciária Salário Maternidade - 13º Salário;  
32 = Contribuição Descontada do Segurado - 13º Salário;  
51 = Salário-Família;  
92 = Incidência suspensa em decorrência de decisão judicial (BC 13º Salário);  
93 = Incidência suspensa em decorrência de decisão judicial (BC Sal. Maternidade);  
94 = Incidência suspensa em decorrência de decisão judicial (BC Sal. Maternidade - 13º Sal.);  
exceto se **categoria de trabalhador** for igual a**:**771 - Contribuinte individual - Membro de conselho tutelar, nos termos da Lei nº 8.069, de 13 de julho de 1990.  
  
**2.** **Código de Incidência tributaria de IRRF** igual a:  
12 = Base de Cálculo do IRRF - 13º Salário;  
13 = Base de Cálculo do IRRF - Férias;  
14 = Base de Cálculo do IRRF - PLR;  
32 = Valor do IRRF - 13º Salário;  
33 = Valor do IRRF - Férias;  
34 = Valor do IRRF - PLR.  
  
**3.** **Código de Incidência tributaria de Contribuição Previdenciária** seja igual a:  
34 = Contribuição Descontada do Segurado - SEST  
se a **CATEGORIA do respectivo trabalhador** for diferente de:  
711 = Contribuinte individual - Transportador autônomo de passageiros;  
712 = Contribuinte individual - Transportador autônomo de carga;  
734 = Contribuinte individual - Transportador Cooperado que presta serviços por intermédio de cooperativa de trabalho.  
  
**4.** **Código de Incidência tributaria de Contribuição Previdenciária** classificado como:  
31 = Contribuição Descontada do Segurado;  
se a **classificação tributaria do contribuinte** for igual a:   
21 = Pessoa Física, exceto Segurado Especial;  
22 = Segurado Especial;  
e **Categoria** igual a Contribuinte individual (7XX), pois não existe previsão legal de desconto de contribuição do segurado contribuinte individual que e contratado por outro contribuinte individual, exceto se o **tipo de Lotação da respectiva lotação** igual a:  
22 = obra de pessoa física.  
  
**Solução****1.**Esteja atualizado com os últimos pacotes disponibilizados através da página [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw);  
  
**2.** O RET (Governo) efetua a **validação de acordo com as Rubricas informadas no evento S-1200**, com a parametrização enviada no S-1010 para cada rubrica.  
Dessa forma, **verifique no TAF se o evento S-1200 está com as Rubricas correspondentes as Verbas informadas no cálculo da folha de pagamento do GPE.**

Cálculo GPE:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016059652)  
S-1200 TAF:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016059752)  
  
  
**3.** O **RET** (Governo) também efetua a **validação das Natureza e da Incidência Tributária** informado no cadastro das Rubricas e enviado através do e**vento S-1010**, sendo assim, verifique as validações trazidas na própria mensagem de inconsistência, para isso é importante que:

**3.1** Verifique no cadastro de Verbas do GPE se todas as verbas informadas no evento S-1200 inconsistente estão preenchidas com a Natureza e Incidência Tributária conforme validação informada na mensagem de inconsistência;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016058692)  
  
**3.2** Efetue a mesma verificação no cadastro de Rubricas do TAF, porém vale ressaltar que podem existir 2 (duas) ou mais Rubricas no TAF relacionadas a mesma Verba do GPE, é importante que verifique se ambas estão corretas e o seu **Inicio de Validade**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016105851)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016105671)

**3.3** No exemplo citado acima foi integrado com o TAF o evento S-1200 referente ao período 06/2018, porém no cadastro de Rubricas há 2 (duas) Rubricas, uma com inicio de validade em 01/2017 e outra com inicio de validade em 11/2018, sendo assim, o evento S-1200 referente ao período de 06/2018 levou em seus registros a Rubrica ID 000290 com inicio de validade em 01/2107. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016105851)****![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016059752)  
  
3.4** Por fim, caso a inconsistência persista após as validações anteriores será necessário que verifique a informação diretamente através do Portal do eSocial e conferir se não há divergência com a informação do TAF. Também é importante verificar se existe mais de um Identificador de Tabela e se em todos a informação está correta.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016059052)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016106331)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
