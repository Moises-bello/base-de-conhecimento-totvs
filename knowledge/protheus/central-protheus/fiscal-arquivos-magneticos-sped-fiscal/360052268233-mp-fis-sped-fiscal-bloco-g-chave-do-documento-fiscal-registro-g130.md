---
article_id: 360052268233
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e6514a586cb0f75504887dc96840bbac8adbb3e18ce1ff4bced150b6c594d7ac
fetched_at: '2026-06-28T22:42:03.832959+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'MP - FIS - SPED FISCAL - BLOCO G - CHAVE DO DOCUMENTO FISCAL - REGISTRO G130 '
type: support-article
updated_at: '2021-04-28T14:24:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052268233-MP-FIS-SPED-FISCAL-BLOCO-G-CHAVE-DO-DOCUMENTO-FISCAL-REGISTRO-G130
---

**Ocorrência**

Ao gerar o arquivo do **Sped Fiscal** ocorre o erro de validação no registro **G130 - Campo 7**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082354993/mceclip0.png)  
  
 **Ambiente**

Microsiga Protheus – Livros fiscais– A partir da versão 12.1.17  
   
 **Causa**

O erro acontece pois falta a informação da **Chave NFe** nos campos necessários.  
O Parâmetro **MV\_F9SKPNF** define de qual tabela o **SPED** buscará a informação para este campo.

Se **MV\_F9SKPNF** = **.F.** - > Será considerado as informações da nota fiscal **SD1, SF1, SF3 e SFT.**  
Se **MV\_F9SKPNF** = **.T.** - > Será considerado as informações do bem tabela **SF9.**

**Solução**

Se **MV\_F9SKPNF** = **.F.** - > Verifique se os campos **F3\_CHVNFE** e **FT\_CHVNFE** estão preenchidos corretamente nas tabelas **SFT** e **SF3**.  
Se **MV\_F9SKPNF** = **.T.** - >  Siga o procedimento abaixo:

1- Crie um campo na tabela **SF9**, exemplo **F9\_CHVNFE** com as mesmas propriedades do **F3\_CHVNFE**:

Campo **F9\_CHVNFE**  
Tipo: Carácter  
Tamanho: 44  
Formato: @!  
Contexto: Real  
Titulo: Num. NFE   
Texto: Informa numero da Chave eletrônica   
Help: Informa numero da chave eletrônica da nota fiscal para preenchimento do campo **07 CHV\_NFE\_CTE** registro 0300 **SPEDFISCAL**  
  
2- Amarre o campo ao parâmetro:

**MV\_F9CHVNF** = **F9\_CHVNFE**

3- Se a chave de acesso já esta preenchida no campo **F9\_CHVNFE** e ainda ocorre o erro, verifique se o campo **F9\_ESPNF** esta informando a **Espécie** da nota.

4 - Se não estiver o campo **F9\_ESPNF**, crie com as informações abaixo:

Campo **F9\_ESPNF**  
Tipo; Caracter  
Tamanho: 5  
Formato: @!  
Contexto: Real  
Titulo: Especie NF  
Texto: Informa Especie da nota fiscal  
Help: Informa Espécie da nota fiscal para preenchimento do campo **04** do registro **G130 SPEDFISCAL**

5- Amarre o campo ao parâmetro:

**MV\_F9ESP = F9\_ESPNF**

Mais Informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=226527899>
