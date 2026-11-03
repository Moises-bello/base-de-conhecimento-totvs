---
article_id: 360021046132
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 2ede48ea857ae82b0fc8c353af0058ee189f04d9c0914e69b52ea8f8772f1f72
fetched_at: '2026-06-28T22:42:06.603585+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  e Sped Fiscal - Ponto de Entrada SPDFIS001 - Alteração do Item Registro 0205
type: support-article
updated_at: '2023-01-25T18:17:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021046132-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-e-Sped-Fiscal-Ponto-de-Entrada-SPDFIS001-Altera%C3%A7%C3%A3o-do-Item-Registro-0205
---

**Dúvida**  
Ponto de entrada **SPDFIS001** utilizado para tratar tipos de produtos no **campo 07 (TIPO\_ITEM)** da **EFD Contribuições** ou **Sped Fiscal**, registro **0205**.   
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
  
**Solução**Este ponto de entrada foi disponibilizado para tratar tipos de produto criados pelo usuário, relacionando-os com os tipos descritos no registro **0200** do **Ato Cotepe 09/2008**, conforme a tabela a seguir:

**00 – Mercadoria para Revenda;**

**01 – Matéria-Prima;**

**02 – Embalagem;**

**03 – Produto em Processo;**

**04 – Produto Acabado;**

**05 – Subproduto;**

**06 – Produto Intermediário;**

**07 – Material de Uso e Consumo;**

**08 – Ativo Imobilizado;**

**09 – Serviços;**

**10 – Outros insumos;**

**99 – Outras.**

**Programa Fonte**

```
SPEDFISCAL.PRW / FISA008.PRW / MATXSPED.PRW
```

**Sintaxe**

**SPDFIS001** - Trata tipos de produtos **( < aTipo> ) --> aTipo**  
Parâmetros:

| Nome | Tipo | Descrição | Obrigatório |
| --- | --- | --- | --- |
| **aTipo** | **Array of Record** | Array com os tipos de produto padrão do sistema | X |
| **cAliasSB1** | **Caractere** | Alias da tabela SB1 do produto processado no momento |  |

Observação: O parâmetro **cAliasSB1** não está disponível nas execuções do ponto de entrada na geração do **Bloco K** do **SpedFiscal** (**MATXSPED.PRW**).

Retorno  
 **aTipo**

()* **Array** com os tipos de produto padrão do sistema acrescidos dos tipos criados pelo usuario

Observações:

O ponto de entrada será chamado a cada produto novo a ser lançado no registro **0200**.  
É passado como parâmetro um **array** (**aTipo**) contendo o relacionamento dos tipos de produto que o sistema tem por padrao, e a sua correspondencia com a tabela de tipos do **SPED Fiscal**.

**aTipo    :=    { {"ME","00"},;**  
**{"MP","01"},;**  
**{"PA","04"},;**  
**{"MC","07"},;**  
**{"MO","09"} }**

**Importante**

Para a correta utilização deste ponto de entrada na geração do **Bloco K**, caso haja necessidade de informar mais de um tipo vinculado a um código, deve-se preencher utilizando *Pipe* "|" para o correto funcionamento da *Query* utilizada, conforme exemplo abaixo:

**aTipo    :=    { {"ME|PA|MC","00"},;**  
**{"MP","01"},;**  
**{"MO","09"} }**

O ponto de entrada deve acrescentar tipos que o usuário tenha criado e retornar o **array** com a mesma estrutura.

Exemplos

**User Function SPDFIS001**  
**Local aTipo := ParamIXB[1]**

**alert("Ponto de entrada SPDFIS001")**  
**AADD(aTipo,{"XX","00"})**

**Return aTipo**

*Link* Boletim Técnico:

<https://tdn.totvs.com/display/public/PROT/PE+-+SPDFIS001+-+Trata+tipos+de+produtos>
