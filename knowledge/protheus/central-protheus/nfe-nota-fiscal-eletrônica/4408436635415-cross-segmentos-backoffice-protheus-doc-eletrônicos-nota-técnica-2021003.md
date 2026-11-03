---
article_id: 4408436635415
category: NFe - Nota Fiscal Eletrônica
content_hash: 6d503156d6b2765e7d605375b273ee0a905889cb75c63f7a670e7520ad45a677
fetched_at: '2026-06-28T22:40:07.021361+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2021.003
type: support-article
updated_at: '2025-06-17T19:27:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408436635415-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2021-003
---

**Dúvida**Quais serão as alterações da Nota Técnica 2021.003  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Prezados Clientes,**

Para a adequação à Nota Técnica **2021.003 Versão 1.20.**

**O prazo previsto para a Nota Técnica 2021.003 v1.20 é:**

* Ambiente de Homologação (ambiente de teste das empresas): **04/07/2022 etapa 1**
* **Ambiente de Produção: 12/09/2022 etapa 1**

* Ambiente de Homologação (ambiente de teste das empresas): **06/03/2023** **etapa 1**
* **Ambiente de Produção: 12/06/2023 etapa 2**

As regras de ***validação do GTIN*** serão implantadas por etapas, conforme plano de implantação a seguir. A etapa inicial já ocorreu, com as exceções que podem ser vistas na Tabela 2, e corresponde às regras que foram ativadas em função do disposto na versão ***1.20 da NT 2017.001.***

• Etapa 1: testes em 04 de julho de 2022, produção em 12 de setembro de 2022  
o Regras ***I03-30, I12-60, U01-30, 9I03-10 e 9I12-10***  
• Etapa 2; testes em 06 de março de 2023, produção em 12 de junho de 2023  
o Regras ***9I03-20***

Entretanto, algumas aplicações autorizadoras já implementaram estas regras, não valendo, portanto, as datas expostas acima. A Tabela 2 a seguir detalha a situação de cada regra em cada aplicação autorizadora:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8020116133655)

A respeito da Tabela 2 valem as seguintes definições:  
***Células com fundo verde:*** regras estão implementadas e seguirão implementadas, sem nenhuma alteração;  
***Células com fundo vermelho:*** regras serão implementadas na etapa 2;  
***Células com fundo bege***, terão implementação em data futura, a ser definida;  
***Todas as demais células:*** regras serão implementadas na etapa 1

Para que não ocorra as rejeições previstas na NT, será necessário cadastrar o código de barras, Cest e NCM conforme previsto nas regras de validações, não será necessário **realizar *nenhuma atualização no sistema.***

1. Para realizar os cadastros de ***Gtin (Código de barras)*** temos um artigo no link abaixo para cadastro:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar as TAGS cEAN e cEANTrib referente ao código de barras no XML ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044935094)

#### 2. Para cadastrar o ***CEST*** temos o link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 806 Rejeição: Operação com ICMS-ST sem informação do CEST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017811471)

3. Se necessário alterar o ***NCM* ou cadastrar temos o link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de schema na Tag NCM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046709113)

* ***Saiba mais:***

Acesse o espaço legislação  [Clique Aqui](https://www.totvs.com/blog/fiscal-clientes/nf-e-nota-tecnica-2020-003-validacao-do-gtin/)

*O Ajuste **SINIEF 07/05 e o Ajuste SINIEF 19/16** obrigam o preenchimento dos campos **cEAN e***  
***CEANTrib na Nota Fiscal Eletrônica (NF-e)** e na Nota Fiscal de Consumidor Eletrônica (NFC-e) quando o produto comercializado possui código de barras com GTIN.*

*Há um parecer da **consultoria no link abaixo:***

[***Clique Aqui***](https://tdn.totvs.com/pages/releaseview.action?pageId=694112512)

4. Para a correção das ***rejeições desta NT, segue os KCSs abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 611 : GTIN (cEAN) inválido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005006951--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-611-GTIN-cEAN-inv%C3%A1lido-?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 612 Rejeição : GTIN da unidade tributável (cEANTrib) inválido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055777674-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-612-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-cEANTrib-inv%C3%A1lido?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 882 Rejeição: GTIN (cEAN) com prefixo inválido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055777954--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-882-Rejei%C3%A7%C3%A3o-GTIN-cEAN-com-prefixo-inv%C3%A1lido?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 883 Rejeição: GTIN (cEAN) sem informação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8687242057879--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-883-Rejei%C3%A7%C3%A3o-GTIN-cEAN-sem-informa%C3%A7%C3%A3o?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 884 Rejeição: GTIN da unidade tributável (cEANTrib) com prefixo inválido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057624333--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-884-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-cEANTrib-com-prefixo-inv%C3%A1lido-?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 885 Rejeição : GTIN informado, mas não informado o GTIN da unidade tributável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006460752--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-885-Rejei%C3%A7%C3%A3o-GTIN-informado-mas-n%C3%A3o-informado-o-GTIN-da-unidade-tribut%C3%A1vel?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 886 Rejeição : GTIN da unidade tributável informado, mas não informado o GTIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059186273--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-886-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-informado-mas-n%C3%A3o-informado-o-GTIN-?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 887 Item de Serviço e informado GTIN diferente de SEM GTIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8733408691735--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-887-Item-de-Servi%C3%A7o-e-informado-GTIN-diferente-de-SEM-GTIN?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 888 Rejeição: GTIN da unidade tributável (cEANTrib) sem informação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8687601681687--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-888-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-cEANTrib-sem-informa%C3%A7%C3%A3o?source=search)

* Excluída a ***rejeição 889***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 890 Rejeição: GTIN inexistente no Cadastro Centralizado de GTIN (CCG)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8732711655575--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-890-Rejei%C3%A7%C3%A3o-GTIN-inexistente-no-Cadastro-Centralizado-de-GTIN-CCG-?source=search)

* Excluída as ***rejeições 891 e 892:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 894 Rejeição: GTIN da unidade tributável inexistente no Cadastro Centralizado de GTIN (CCG)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8732114728599-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-894-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-inexistente-no-Cadastro-Centralizado-de-GTIN-CCG-?source=search)

* Excluída a ***rejeição 896***

***Novos  891 e 892 :***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 891 Rejeição: GTIN incompatível com a NCM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11592861572759-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-891-Rejei%C3%A7%C3%A3o-GTIN-incompat%C3%ADvel-com-a-NCM-?source=search)
