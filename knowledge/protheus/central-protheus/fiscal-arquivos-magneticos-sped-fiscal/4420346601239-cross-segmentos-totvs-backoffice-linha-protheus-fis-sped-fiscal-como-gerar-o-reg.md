---
article_id: 4420346601239
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: d8b5fc836f1fc2d8186bc37c2d23ad391fd8447be4188a4bd9be9e1f717d75e4
fetched_at: '2026-06-28T22:42:03.752627+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- SPED FISCAL - Como
  gerar o registro 0400 Sped Fiscal?
type: support-article
updated_at: '2023-03-02T18:45:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420346601239-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-SPED-FISCAL-Como-gerar-o-registro-0400-Sped-Fiscal
---

**Dúvida**Como gerar o registro 0400 Sped Fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Solução**  
Para gerar o registro 0400 do Sped Fiscal temos três formas:

**1-** Pela **Natureza da Operação/Prestação** tabela **(CD1);**

O Sistema busca a informação do campo **Natureza Ope** **(FT\_NATOPER)** e a descrição do campo **Descrição** (**CD1\_DESCR)**. Para alimentar o campo **Natureza Ope (****FT\_NATOPER)** precisa cadastrar no **TES** o campo **Natureza Ope** **(F4\_NATOPER)**;

O conteúdo incluso no campo **F4\_NATOPER** já irá ter alimentado os dados da tabela **CD1.**

**2-** Por meio dos cadastros **de TES** tabela **(SF4);**

O Sistema busca a informação do código do **TES** campo **Cod do Tipo** **(F4\_CODIGO)** e a descrição do campo **Txt Padrão** (**F4\_TEXTO);**

**3-** Pelos códigos da tabela de **CFOPs** no **SX5 (tabela 13);**

Se configurar o parâmetro MV\_SPEDNAT = T, o sistema busca a informação do campo **Cod. Fiscal (FT\_CFOP)** e a descrição do campo **X5\_DESCRI,** realizando o filtro na tabela de **CFOPs** **SX5 (tabela 13);**

Ao gerar o arquivo Sped Fiscal, necessário adicionar a pergunta **Gera registro 0400 - Natureza da Oper = Sim**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12808946406935)

**Importante:**

Conforme orientação do guia prático:

**Este registro não se refere à CFOP. Algumas empresas utilizam outra classificação além das apresentadas nos CFOP. Esta codificação permite informar estes agrupamentos próprios;**

Portanto verifique a necessidade ao gerar o arquivo magnético, pois ao ativar o parâmetro **MV\_SPEDNAT**, os registros são preenchidos com os códigos de CFOP e suas respectivas descrições. Caso contrário, sem utilizar o cadastro de Natureza da Operação (CD1), o controle é feito pelos códigos do Cadastro de TES (SF4).

Mais informações no link abaixo:

<https://tdn.totvs.com/display/public/PROT/FIS0005_SPED_FISCAL>
