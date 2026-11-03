---
content_hash: 853dd61db0982de2cbf302326ee3cee6e487f91fbe54a086bbc2ff6da533da0d
fetched_at: '2026-06-29T00:08:37.111658+00:00'
page_id: '284871921'
product: rm
source: tdn-rm
title: RMFIN00006_E_Funcional_Novas variáveis para nome do arquivo de remessa bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284871921
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Financeira |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | N/A |
| **Ambiente:** | RM |
| **Passo a passo:** | N/A |
| **Observações:** |  |

## Objetivo

Disponibilizar novas variáveis para geração do nome do arquivo de remessa bancária (Remessa de cobrança/pagamento) para que o usuário possa definir o nome da forma solicitada pelo banco.

**Definição da Regra de Negócio**

Atualmente é possível definir variáveis no nome do arquivo de remessa bancária que será gerado. Porém, atualmente este recurso está limitado somente as variáveis **para número e data da remessa.**Atualmente a configuração de variáveis permitida são:

 # carácter para definir o número da remessa com zero à esquerda.

DDMMYYYY - informação da data de geração da remessa - a variável de data atualmente não permite o desmembramento, este desmembramento é necessário porque alguns bancos solicitam apenas o dia no arquivo de remessa.

Desta maneira precisamos evoluir esta funcionalidade disponibilizando novas variáveis para serem utilizadas, pois alguns bancos possuem nomenclaturas definidas para o nome do arquivo.

**Exemplos de nomenclaturas solicitadas pelos bancos:**

**Caixa Econômica:**

**EDD#####.REM**, onde:

**E** = fixo  
  
**DD** = dia da geração do arquivo (varável)  
  
**#####** = sequencial da remessa com 5 dígitos (variável)  
  
**Exemplo:** E3100008.REM

**Banco Sicred:**

**Exemplos:**

**CCCCCMDD.CRM**

**CCCCCMDD.RMX**

onde:

 

**CCCCC** = código beneficiário  
**MDD** = cód. do mês e nº do dia da data de geração do arquivo  
**CRM** = Indica que é o 1º arquivo remessa  
**RMX** = Indica que o beneficiário enviou mais de um arquivo remessa na data, onde RM = Remessa e X = seqüência do arquivo remessa. Iniciará sempre em “2” (segundo arquivo remessa gerado no dia) e terá seqüência de acordo com a quantidade de arquivos remessa gerados pelo beneficiário, podendo ser “3”, “4”, “5”, “6”, “7”, “8”, “9” e “0” (décimo e último arquivo remessa que poderá ser gerado pelo beneficiário)

Observação descrita no manual sobre o código do beneficiário:  O código do beneficiário será um número sequencial aleatório criado no sistema da Cooperativa, o seu uso será obrigatório no nome dos arquivos de remessa e retorno;

**Outros exemplos de variáveis solicitadas pelos bancos:**

MM – Mês da geração da remessa

M = mês (1 = jan, 2 = fev, ..., O = Out, N= Nov e D=Dez)

OBSERVAÇÃO: Conforme exemplos citados acima, alguns bancos solicitam a extensão CRM e também RMX para geração dos arquivos, sendo que a extensão RMX indica que o beneficiário enviou mais de um arquivo de remessa na data, onde RM é igual 'Remessa' e  X é igual a sequência do arquivo de remessa. Iniciará sempre em “2” (segundo arquivo remessa gerado no dia) e terá seqüência de acordo com a quantidade de arquivos remessa gerados pelo beneficiário, podendo ser “3”, “4”, “5”, “6”, “7”, “8”, “9” e “0” (décimo e último arquivo remessa que poderá ser gerado pelo beneficiário).

# Impacto no Sistema -

Ao  editar o convênio na pasta **'Remessa Bancária**' permitir que no campo nome do arquivo sejam informadas novas variáveis que possam atender as nomenclaturas solicitadas pelos bancos.

Ao gerar a remessa de cobrança o nome do arquivo será gerado de acordo com a  parte fixa e variável que foi definida.
