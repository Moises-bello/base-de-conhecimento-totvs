---
article_id: 360026469571
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 621d4d4f1aa42a91bfc3ac3c8d4caef826ab83971da88a1d6f83ac2b3f304fe0
fetched_at: '2026-06-28T22:42:02.632764+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos -  Como Gerar
  o Campo 02 - CST_ICMS no Registro H020?
type: support-article
updated_at: '2023-03-01T18:26:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026469571-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-Gerar-o-Campo-02-CST-ICMS-no-Registro-H020
---

**Dúvida**Como gerar o campo **02 - CST\_ICMS** para o registro **H020 - Informação Complementar do Inventário?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Existem três formas de gerar o campo **02 -** **CST\_ICMS** para que seja apresentado corretamente no arquivo:

**1.** Através do Cadastro de produto (tabela **SB1**) preenchendo os campos **Class. Fiscal  - B1\_CLASFIS** e **Origem - B1\_ORIGEM.** Os campos em questão precisam estar preenchidos em todos os produto a serem apresentados no **Bloco H**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12780373725079)  
  
Com base no preenchimento dos campos, o **Protheus** aglutina as informações da **Classificação Fiscal** e da **Origem do Produto** de forma que o campo **02 do H020** seja gerado com **tamanho três** conforme exigido pelo guia prático do **Sped Fiscal**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12780728658455)

**Exemplo:**

**Campo Class. Fiscal  - B1\_CLASFIS** = 00

**Campo Origem - B1\_ORIGEM** = 0

**Sped Fiscal: Origem + CST de ICMS**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12780652801303)  
  
**Importante:**

É possível gerar as informações do campo **02 do H020** com base tanto na tabela **SBZ - Indicadores de Produtos** quanto na **SB1 - Cadastro de Produtos.**  
  
O que define se serão validados os dados de uma tabela ou de  outra é o parâmetro **MV\_ARQPROD**. O conteúdo deste parâmetro indica se as informações serão consideradas de acordo com a tabela **SB1** ou ou **SBZ**.  
  
**2.** Através de ponto de entrada  **SPEDH020**, onde o usuário irá retornar todos os valores do **H020**:  
  
*Link:* [SPEDH020 - SPEDFISCAL - Registro H020](http://tdn.totvs.com/display/public/PROT/SPEDH020+-+SPEDFISCAL+-+Registro+H020)  
  
Nesta opção, ajuste o valor a ser retornado para o campo no ponto de entrada, onde deverá possuir tamanho 3. **Origem do produto + CST de ICMS**.

**3.** Através da  manutenção do produto diretamente na rotina **FISA116** (**Composição de valores para registro H020 do arquivo magnético SPED fiscal**), veja a documentação e processo disponibilizado:  
*Link:*<http://tdn.totvs.com/display/public/PROT/ARQ0013_H020_SPED_FISCAL>  
  
Realize o preenchimento do campo correto, **CST** de **ICMS**. //Novo tratamento pela rotina **FISA116** (**tabela F0M**).

**aAdd (aRegH020[nPosH020], F0M->F0M\_CST)**
