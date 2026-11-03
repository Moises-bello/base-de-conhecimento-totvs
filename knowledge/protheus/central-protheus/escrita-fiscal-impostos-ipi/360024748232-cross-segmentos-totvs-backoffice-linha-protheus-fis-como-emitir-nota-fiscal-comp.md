---
article_id: 360024748232
category: Escrita Fiscal - Impostos - IPI
content_hash: 505d9c5ba4888fcf3ecb5b5120530c68b531005934f30f871ac72b95581f78a8
fetched_at: '2026-06-28T22:39:28.990064+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como emitir nota
  fiscal Complementar de IPI e ICMS em único documento?
type: support-article
updated_at: '2021-07-28T14:15:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024748232-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-emitir-nota-fiscal-Complementar-de-IPI-e-ICMS-em-%C3%BAnico-documento
---

**Dúvida**

Como emitir Nota fiscal Complementar de IPI e ICMS em único documento ?

**Ambiente**

Protheus - Fiscal - A partir da versão 11.80

**Solução**

* **Operações envolvendo somente complemento de imposto IPI**

Tipo do pedido/nota = Complemento de IPI:

1. Informe o mesmo fornecedor/cliente (para fornecedor (EM NOTAS DE SAÍDA), cadastrá-lo como cliente, e para cliente (EM NOTAS DE ENTRADA), cadastrá-lo como fornecedor);

2. Informe um produto da NF original;

3. Digite o valor do complemento do IPI nos campos: **Valor unitário** e **Valor total**;

4. Informe o TES:

5. Vincule a nota fiscal de complemento ao documento original, no campo NF original, tecle **Enter** + **F4**. Para notas fiscais de entrada, digite o número da nota fiscal no campo **Documento Original;**

* **Operações envolvendo somente complemento de imposto ICMS**

Tipo do pedido/nota = Complemento de ICMS:

1. Informe o mesmo fornecedor/cliente (para fornecedor (EM NOTAS DE SAÍDA), cadastrá-lo como cliente, e para cliente (EM NOTAS DE ENTRADA), cadastrá-lo como fornecedor);

2. Informe um produto da NF original;

3. Digite o valor do complemento do ICMS nos campos: **Valor unitário** e **Valor total**;

4. Informe o TES:

5. Vincule a nota fiscal de complemento ao documento original, no campo NF original, tecle **Enter** + **F4**. Para notas fiscais de entrada, digite o número da nota fiscal no campo **Documento Original;**

* **Operações envolvendo complemento de imposto IPI e ICMS em uma única nota.**
* **Tipo de Operação: Entrada**

Tipo do pedido/nota = Complemento de IPI:

1. Informe o mesmo fornecedor;

2. Informe um produto da NF original;

3. Digite o valor do complemento do IPI nos campos:**(D1\_VUNIT - Valor unitário) e (D1\_TOTAL - Valor total)**;

4. O valor do IPI no campo**(D1\_VALIPI - Vlr. IPI)** será preenchido com o valor do campo **(D1\_TOTAL - Valor total)**;

5. Informe o TES:

6. Vincule a nota fiscal de complemento ao documento original, digite o número da nota fiscal no campo **Documento Original;**

7. Digite o valor do complemento do ICMS no campo: (**D1\_VALICM - Vlr. ICMS**);

* **Tipo de Operação: Saída**
* **Implementação:**

Será necessário criar um campo **manualmente** na tabela (SC6 - Itens do Pedido de Venda), para informar o valor do ICMS que será utilizado na nota fiscal de complemento quando a operação de saída conter IPI e ICMS.

Exemplo do campo, que deverá ser criado **manualmente** na tabela (SC6 - Itens do Pedido de Venda).

* Sugestão de nome: **C6\_VALICM**

| **Campo** | **C6\_VALICM** |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 12 |
| **Decimal** | 2 |
| **Formato** | @E 999,999,999.99 |
| **Título** | Valor do ICM |
| **Descrição** | Valor ICMS Compl. IPI+ICM |
| **Val.Usuário** | MafisGet("IT\_VALICM") |
| **Browse** | Sim |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Help** | Informe o valor do ICMS para operações de complemento de IPI e ICMS em uma única nota. O tipo do pedido, campo (C5\_TIPO) deverá ser igual a (P -Complemento de IPI), o valor do IPI será o valor preenchido no campo (C6\_VALOR - Vlr. Total) e o valor do ICMS será o digitado neste campo criado manualmente. |

* **Processo para utilização:**

Tipo do pedido/nota = Complemento de IPI:

1. Informe o mesmo cliente;

2. Informe um produto da NF original;

3. Digite o valor do complemento do IPI nos campos:**(C6\_PRCVEN - Valor unitário) e (C6\_VALOR - Valor total)**;

4. Informe o TES:

5. Vincule a nota fiscal de complemento ao documento original, no campo N.F.Original, tecle **Enter** + **F4****;**

6. Digite o valor do complemento do ICMS no campo criado manualmente conforme o exemplo acima: (**C6\_VALICM****- Valor do ICM**);

* **Cadastro da TES de Complemento.**

* **Aba Adm:**

Tipo: Saída/Entrada;

Cred. ICM e Cred IPI = Não;

Gera Duplic. ICMS= Não; Gera Duplic. IPI = Sim; Gera Duplic.  Sim  para nota fiscal complementar de ICMS e IPI em único documento;

Agrega Valor = "Não" para nota fiscal de complemento de ICMS e "SIM" para nota fiscal de complemento IPI e Agrega Valor = "SIM" para nota fiscal complementar de ICMS e IPI em único documento;

Não atualiza Estoque e Não controla Poder de Terceiros;

Restante fica preenchido como "default".

* **Aba Impostos:**

Calcula ICMS e IPI = Sim;

CFOP da NF Original;

Livros Fiscais: De acordo com o Imposto a ser complementado (ICMS/IPI) = Tributado.

* **Escrituração**

A escrituração da nota é efetuada na coluna tributada e deve ser efetuada conforme determinação da TES. No campo **Observações** deve ser informada a nota de origem, a qual este complemento se refere.
