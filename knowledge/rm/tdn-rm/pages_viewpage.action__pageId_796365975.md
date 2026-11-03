---
content_hash: 26110008ee67a5c532d34eadc8d54c39dd5551653f4d290ef552a6a3e419b18b
fetched_at: '2026-06-29T00:11:42.762423+00:00'
page_id: '796365975'
product: rm
source: tdn-rm
title: Alterações - S-2501 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=796365975
version: 6
---

false

**A partir das Versões:**

* 12.1.2302.233
* 12.1.2306.181
* 12.1.2310.115 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO** **GERAL**

Este documento visa apresentar as mudanças no evento S-2501 para atender o Leiaute do eSocial versão S-1.2.

## **02. INCLUSÕES E ALTERAÇÕES REALIZADAS**

### **02.01.****GRUPO <calcTrib> - ALTERADA CONDIÇÃO E OCORRÊNCIA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {calcTrib}: alterada condição e ocorrência | **O**  1-360 | **OC**  0-999 |

**Alteração:**Grupo <calcTrib> deixou de ser "O - Obrigatório", passando a ser "OC - Obrigatório se existir informação". Sua ocorrência também passou de 1 até 360 repetições para 0 até 999 repetições. Não ocorreu mudanças no produto.

### **02.02.****CAMPO <vrCR> - ALTERADA VALIDAÇÃO**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Campo {vrCR}: alterada validação do campo | Valor correspondente ao Código de Receita - CR. **Validação**: Deve ser informado de acordo com a legislação em vigor na competência. Deve ser maior que 0 (zero). | Valor correspondente ao Código de Receita - CR. **Validação**: Deve ser informado de acordo com a legislação em vigor na competência. Deve ser maior ou igual a 0 (zero). |

**Alteração:**Campo <vrCR> do grupo <infoCRIRRF>, agora aceita valor igual a zero, passando sua validação a ser "Deve ser maior ou igual a 0 (zero)". Não ocorreu mudanças no produto.

### **02.03.****GRUPO <infoIR> - CRIADO GRUPO E SEUS RESPECTIVOS CAMPOS**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoIR}: criado grupo e seus respectivos campos | - | **OC** |

**Alteração:**Grupo <infoIR> criado juntamente com seus respectivos campos.

No sistema, após editar o trabalhador vinculado e acessar a aba "**Informações de IRRF**", basta incluir/editar um registro para visualizar os devidos campos:

### **02.04.****GRUPO <infoRRA> - CRIADO GRUPO E SEUS RESPECTIVOS CAMPOS**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoRRA}: criado grupo e seus respectivos campos e sub-grupos | - | **O** (se infoCRIRRF/tpCR =[188951]); **N** (nos demais casos) |
| Sub-grupo {despProcJud}: criado grupo, filho do grupo {infoRRA} | - | **OC** |
| Sub-grupo {ideAdv}: criado grupo, filho do grupo {infoRRA} | - | **OC** |

**Alteração:**Grupo <infoRRA> criado juntamente com seus respectivos campos e sub-grupos.

No sistema, após editar o trabalhador vinculado e acessar a aba "**Informações de IRRF**", basta incluir/editar um registro e rolar a tela para baixo para visualizar os devidos campos:

Para incluir as informações vinculadas ao grupo <ideAdv> (sub-grupo de infoRRA), basta expandir o grupo "**Identificação dos Advogados**" e clicar em "Incluir Advogado". Após preencher os devidos campos, clique novamente em "Incluir Advogado" para salvar.

### **02.05.****GRUPO <dedDepen> - CRIADO GRUPO E SEUS RESPECTIVOS CAMPOS**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {dedDepen}: criado grupo e seus respectivos campos | - | N (se infoCRIRRF/tpCR = [188951]); OC (nos demais casos) |

**Alteração:**Grupo <dedDepen> criado como sub-grupo de <infoCRIRRF>.

No sistema, após editar o trabalhador vinculado e acessar a aba "**Informações de IRRF**", basta incluir/editar um registro e rolar a tela para baixo para visualizar os devidos campos. Para incluir as informações basta expandir o grupo "**Dedução do rendimento tributável relativa a dependentes**" e clicar em "Incluir dedução".

**Atenção:** Após preencher os devidos campos, clique novamente em "Incluir dedução" para salvar.

### **02.06.****GRUPO <penAlim> - CRIADO GRUPO E SEUS RESPECTIVOS CAMPOS**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {penAlim}: criado grupo e seus respectivos campos | - | **OC** |

**Alteração:**Grupo <penAlim> criado como sub-grupo de <infoCRIRRF>.

No sistema, após editar o trabalhador vinculado e acessar a aba "**Informações de IRRF**", basta incluir/editar um registro e rolar a tela para baixo para visualizar os devidos campos. Para incluir as informações basta expandir o grupo "**Informação dos beneficiários da pensão alimentícia**" e clicar em "Incluir pensão".

**Atenção:** Após preencher os devidos campos, clique novamente em "Incluir pensão" para salvar.

### **02.07.****GRUPO <infoProcRet> - CRIADO GRUPO E SEUS RESPECTIVOS CAMPOS**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoProcRet}: criado grupo e seus respectivos campos e sub-grupos | - | **N** (se infoCRIRRF/tpCR =[188951]); **OC** (nos demais casos) |
| Sub-grupo {infoValores}: criado grupo, filho do grupo {infoRRA} |  | **OC** |
| Sub-grupo {dedSusp}: criado grupo, filho do grupo {infoValores} |  | **OC** |

**Alteração:**Grupo <infoProcRet> criado como sub-grupo de <infoCRIRRF>. Possui o sub-grupo <infoValores> que também possui um sub-grupo, chamado <dedSusp>.

* **infoProcRet - Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais**

No sistema, após editar o trabalhador vinculado e acessar a aba "**Informações de IRRF**", basta incluir/editar um registro e rolar a tela para baixo para visualizar os devidos campos. Para incluir as informações basta expandir o grupo "**Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais**" e clicar em "Incluir processo".   
 **Atenção**: Para salvar a informação preenchida, clique novamente em "Incluir processo". Em caso de edição, o botão será exibido com o nome "Editar processo"

* **infoValores - Informações de valores relacionados a não retenção de tributos ou a depósitos judiciais**

Para a inclusão de valores (sub-grupo <infoValores>), dentro da expansão "**Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais"**,clique no ícone de edição, conforme abaixo, presente na área "**Informações de valores relacionados a não retenção de tributos ou a depósitos judiciais**":

Na tela que será aberta, clique em "Incluir valores" e preencha os campos que serão exibidos na tela conforme necessidade.

**Atenção**: Para salvar a informação preenchida, clique novamente em "Incluir valores". Em caso de edição, o botão será exibido com o nome "Editar valores"

* **dedSusp - Detalhamento das deduções com exigibilidade suspensa**

Para a inclusão de deduções com exigibilidade suspensa (sub-grupo <dedSusp>), dentro da tela "**Informações de valores relacionados a não retenção de tributos ou a depósitos judiciais"**,clique no ícone de edição, conforme abaixo, presente na área "**Detalhamento das deduções com exigibilidade suspensa**":

Na tela que será aberta, clique em "Incluir dedução"  e preencha os campos que serão exibidos na tela conforme necessidade.

**Atenção**: Para salvar a informação preenchida, clique novamente em "Incluir dedução". Em caso de edição, o botão será exibido com o nome "Editar dedução"

* **benefPen - Informação das deduções suspensas por dependentes e beneficiários da pensão alimentícia**

Para a inclusão de deduções suspensas por dependentes e beneficiários de pensão (sub-grupo <benefPen>), dentro da tela "**Detalhamento das deduções com exigibilidade suspensa**",basta expandir o grupo "Informação das deduções suspensas por dependentes e beneficiários da pensão alimentícia" e clicar em "Incluir informação":

**Atenção**: Para salvar a informação preenchida, clique novamente em "Incluir informação". Em caso de edição, o botão será exibido com o nome "Editar informação"

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + - [Evento S-2501](https://tdn.totvs.com/display/LRM/Evento+S-2501)
