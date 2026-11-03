---
article_id: 360023124831
category: Escrita Fiscal - Impostos - ICMS - Complemento de ICMS/IPI
content_hash: d3ab04fee3c0b5a5a7ce201c9c04b0614956b4e71a88a8d41c353166ee479fc9
fetched_at: '2026-06-28T22:39:21.317044+00:00'
product: protheus
section_id: 1500001538701
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - FIS - Nota Fiscal Complementar
  de ICMS e  IPI
type: support-article
updated_at: '2022-08-17T15:02:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023124831-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-Fiscal-Complementar-de-ICMS-e-IPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como emitir/ Lançar nota fiscal complementar de ICMS e IPI ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

**Complemento de IPI e ICMS**

Tipo do pedido/nota = Complemento de IPI ou ICMS:

1.       Informe o mesmo fornecedor/cliente (para fornecedor (EM NOTAS DE SAIDA), cadastrá-lo como cliente, e para cliente (EM NOTAS DE ENTRADA), cadastrá-lo como fornecedor);

2.       Informe um produto da NF original;

3.       Digite o valor do imposto nos campos: **Valor unitário** e **Valor total**;

**Informe o TES:**

Vincule ao documento original no campo NF original, tecle **Enter** + **F4**. Para fornecedor digite o número da nota fiscal no campo **NF ORIGINAL** ou vice/versa.

**Cadastro da TES de Complemento:**

**Aba Adm:**

Tipo: Saída/Entrada;

Cred. ICM (F4\_CREDICM) e Cred IPI (F4\_CREDIPI)= Não;

Gera Dupl. (F4\_DUPLIC)= Não

Não atualiza Estoque e Não controla Poder de Terceiros;

Restante fica preenchido como "default".

**Aba Impostos:**

Calcula ICMS (F4\_ICM) e IPI (F4\_IPI) = Sim;

Cod. Fiscal (F4\_CF) = Utilizar seguindo a mesma operação da NF Original;

L. Fisc. ICM (F4\_LFICM): De acordo com o Imposto a ser complementado (ICMS/IPI) = Tributado.

Agrega Valor (F4\_AGREG)= Não para NF de complemento de ICMS, para IPI = SIM;

**Restante fica preenchido como "default".**

**Escrituração**

A escrituração da nota é efetuada na coluna tributada e deve ser efetuada conforme determinação da TES. No campo **Observações** deve ser informada a nota de origem, a qual este complemento se refere.
