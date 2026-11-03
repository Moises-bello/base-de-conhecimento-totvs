---
article_id: 38347119369879
category: Financeiro - Baixas a Pagar
content_hash: 3404995573db8017f71c2e892fe792c473d19f95a52262ad2a9748f189a4e812
fetched_at: '2026-06-28T22:42:13.597748+00:00'
product: protheus
section_id: 38310054605975
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 -  Como gerar
  o imposto ISS para fornecedor de outro munícipio onde ocorreu a execução do serviço
type: support-article
updated_at: '2026-02-19T19:08:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38347119369879-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-ISS-para-fornecedor-de-outro-mun%C3%ADcipio-onde-ocorreu-a-execu%C3%A7%C3%A3o-do-servi%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38347119361303) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar o imposto ISS para o fornecedor de outro munícipio onde ocorreu a execução do serviço?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**

**1.1 Regra de título**

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código:** defina o codigo
* **Descrição:** defina a descrição
* **Tipo de Movimento (Tp. Movto)** selecione a opção *Impostos*
* **C****ódigo do participante** (fornecedor ou cliente): selecione o fornecedor para o qual será gerado o título de **ISS** referente ao municipio/estado que ocorreu a prestação de serviços,
* **C****arteira:** para este caso defina como *Pagar*;
* **Natureza:** previamente criada para vinculação do tributo;
* **Tipo de título:** defina o tipo

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38347203301655)](https://centraldeatendimento.totvs.com/hc/article_attachments/38347203301655)

**1.2 Regra de vencimento**

   Preencha os campos conforme exemplo

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38347227941399)](https://centraldeatendimento.totvs.com/hc/article_attachments/38347227941399)

**1.3 Regra de cálculo**

Preencha os campos conforme exemplo

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38347119362327)](https://centraldeatendimento.totvs.com/hc/article_attachments/38347119362327)

**1.4 Regra de retenção**

 Preencha os campos conforme exemplo

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38347119362583)](https://centraldeatendimento.totvs.com/hc/article_attachments/38347119362327)

**1.5 Regra Financeira**  
Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a **Regra Financeira** a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a **Regra Financeira** correspondente ao imposto na aba**Dados Gerais**, preenchendo os campos indicados a seguir:

Preenchimento dos campos:

* **Código:**defina o código
* **Descrição:** defina a descrição
* **Início de vigência**: data inicial
* **Fim da vigência**: data final
* **Fato Gerador:** 1– Competência (emissão)  ou  2– Caixa (baixa)
* **Aplica-se à Carteira**: (1– Pagar ou 2– Receber). Neste cas selecione a opção *Pagar*
* **Valor do Título**: (1– Subtrair, 2– Somar ou 3– Sem ação. Neste caso selecione a opção Subtrair)
* **Parcelamento**: opcional, conforme a necessidade
* **Tributo**: imposto a ser cadastrado
* **Classificação do tipo de imposto** (Principal)

**Exemplo de cadastro para o ISS do Paraná**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38347180937239)](https://centraldeatendimento.totvs.com/hc/article_attachments/38347180937239)

Na **Regra Financeira** aba **Regras Gerais** vincule as regras criadas anteriormente às **Regras financeiras**, considerando os campos indicados conforme exemplo.

Preenchimento dos campos:  **Regra de titulo, Regra de cálculo** e **Regra de retenção**

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38347180938135)**](https://centraldeatendimento.totvs.com/hc/article_attachments/38347180938135)

**1.6 Regra Fiscal**

Após configurar a **Regra Financeira**, necessário vincular à **Regra de Cálculo - Documentos Fiscais** cadastrada, conforme exemplo abaixo:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38347180938519)](https://centraldeatendimento.totvs.com/hc/article_attachments/38347180938519)

**1.7**Segue demonstração de um processo com demonstração da **Regra Financeira** vinculada a uma **Regra Fiscal,** o **Documento de Entrada** e a criação do titulo TX do **ISS** no Contas a pagar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38352145664663)

**Obs.** Caso não queira que o título de **ISS** seja gerado com a sigla TG a **Regra Financeira** deve possuir uma regra de retenção, como no exemplo acima, e vinculada a **Regra Financeira**. Com isso, o sistema irá gerar o título do tributo com a numeração da nota ou título, conforme artigo:

[Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Regra financeira - Título com a Sigla TG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34520371038871-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regra-financeira-T%C3%ADtulo-com-a-Sigla-TG)

**Saiba mais**

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com.br/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
