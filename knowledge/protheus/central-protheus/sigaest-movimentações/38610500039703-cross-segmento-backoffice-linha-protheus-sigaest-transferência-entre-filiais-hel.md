---
article_id: 38610500039703
category: SIGAEST - MOVIMENTAÇÕES
content_hash: e4e4bfd4d9795ebb5d8a26a004964eb77618f61b376924270c23a5d50186b969
fetched_at: '2026-06-28T22:38:58.545275+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) – SIGAEST – Transferência entre
  Filiais – HELP A311FILIALDCLI
type: support-article
updated_at: '2026-03-27T11:49:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38610500039703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Transfer%C3%AAncia-entre-Filiais-HELP-A311FILIALDCLI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38610500022167) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Após a criação de uma nova filial, ao tentar realizar **Transferência entre Filiais**, o sistema apresenta a seguinte mensagem:

> **HELP: A311FILIALDCLI**  
> **Problema:** A filial de destino não é cliente da filial de origem.  
> **Solução:** Cadastre a filial destino como cliente na filial de origem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38610491893783)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
A filial de destino **não está cadastrada como cliente** na filial de origem.

Esse cadastro é obrigatório, pois a rotina de transferência:

* Cria automaticamente o **Pedido de Venda** na filial de origem (tendo a filial destino como cliente);
* Gera o **Documento de Saída** na filial origem;
* Gera o **Documento de Entrada** na filial destino.

Ou seja, a rotina funciona como um facilitador que integra as movimentações entre as filiais, sendo necessário que a filial destino esteja previamente cadastrada como cliente na origem.

**Solução**

* Revisar se a filial destino está cadastrada como **Cliente** na filial origem.
* Caso não esteja, realizar o cadastro.
* Após o cadastro, repetir o processo de transferência.

## Configuração da Transferência entre Filiais

Existem dois métodos de configuração:

### 🔹 Método 1

Amarração das filiais por meio de campo no Cadastro do Fornecedor, com o parâmetro **MV\_FILTRF** ativo.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Transferência entre Filiais utilizando o parâmetro MV\_FILTRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF?source=search)

### 🔹 Método 2

Amarração pelo próprio CNPJ do cadastro de Filiais no Configurador, com o parâmetro **MV\_FILTRF** desativado.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar ou revisar a configuração da Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-ou-revisar-a-configura%C3%A7%C3%A3o-da-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus?source=search)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Como definir o Preço de Venda do Pedido de Venda derivado do processo de Transferência entre Filiais ?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021390332-MP-SIGAEST-Custo-do-produto-derivado-do-processo-de-transfer%C3%AAncia-via-MATA311-)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Validação do HelpA311FILIALDCON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22264886227735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Valida%C3%A7%C3%A3o-do-HelpA311FILIALDCON)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
