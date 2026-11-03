---
content_hash: 1a08dd2660a4602a12a8ee0d86e4e15258fb90eebb7afb75e415fbafc7a61f73
fetched_at: '2026-06-29T00:05:52.732312+00:00'
page_id: '1059321698'
product: rm
source: tdn-rm
title: Parametrizações Iniciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1059321698
version: 4
---

Esta documentação orienta a parametrização necessária para gerar movimentos de aluguel no módulo **TOTVS Construção Gestão de Imóveis (TCGI)** e a consequente emissão de Notas Fiscais de Serviço eletrônicas (NFSe).

---

## 1. Criar Série Específica

Antes de configurar o movimento, defina uma série exclusiva para identificar as operações de locação.

1. Acesse **Backoffice – Gestão de Estoque, Compras e Faturamento**.
2. Vá em **Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento**.
3. Selecione a etapa **04.01.03 - Numeração do movimento** e clique em **Avançar**.
4. Insira uma nova série (Exemplo: Código: `MLI` / Descrição: `Movimento de Locação de Imóveis`).

---

## 2. Configurar o Tipo de Movimento de Origem (2.1.XX)

Este movimento servirá como a origem dos dados que serão enviados à prefeitura.

1. No mesmo menu de parâmetros, selecione a etapa **04.08.01 – Pedido de Venda** e clique em **Avançar**.
2. Clique em **Inserir**, defina um código do grupo **2.1.XX** e a descrição.

   1. Na aba Campos Obrigatórios, informe os campos conforme sugestão abaixo:
   2. Na aba Séries, insira uma nova série, informando a série criada no passo 1, e campo Principal = Sim.
3. Cliquei em Ok para incluir a série, e Ok novamente para inserir o tipo de movimento.
4. Configure as abas principais conforme as diretrizes abaixo:

| **Aba** | **Campo** | **Configuração Sugerida** |
| --- | --- | --- |
| **Identificação** | Classificação | Pedido de Venda (Vendas) |
| **Identificação** | Edita Numeração | Mostra |
| **Identificação** | Séries | Selecione `MLI` e marque como **Principal** |
| **Emitente/Destinatário** | Emitente | Empresa |
| **Emitente/Destinatário** | Destinatário | Cliente |
| **Item - Identificação** | Tipo de Itens | Serviços |
| **Compra/Venda** | Gera Movimento de Venda | Habilitado |
| **Compra/Venda** | Movimento Gerado (Padrão) | Informe o código do movimento de destino (2.2.XX) |
| **Fiscal - Escrituração** | Gerar Escrituração | **Desabilitado** (A nota oficial será escriturada apenas no destino) |
| **Fiscal - NF-e** | NFSe Municipal | Enviar Manualmente |

## 3. Configurar o Tipo de Movimento de Destino (2.2.XX)

Este movimento será gerado automaticamente após a autorização da nota pela prefeitura, contendo o número oficial da NFSe para escrituração.

1. Crie um novo movimento no grupo **2.2.XX**.
2. Defina a **Classificação** como **Faturamento (Vendas)**.
3. Na etapa **63 - Fiscal - Escrituração Fiscal**, marque a opção **Gerar Escrituração**.

---

## 4. Cadastrar Produto de Serviço

O sistema exige um item cadastrado para compor o movimento de locação.

1. Acesse **Cadastro > Produto**.
2. Na aba **Identificação**, defina o **Tipo** como **Serviço**.
3. Na aba **Detalhes > Outros Dados**, informe o código **NBS** (Nomenclatura Brasileira de Serviços) correspondente.

---

## 5. Vincular Parâmetros no TCGI

Finalize o processo integrando as configurações do Backoffice com o módulo de Imóveis.

1. Acesse o módulo **TOTVS Construção Gestão de Imóveis**.
2. Vá em **Aluguel > Cadastros Aluguel > Parâmetro de Movimento Aluguel**.
3. Preencha os campos:

   * **Tipo de Geração**: Locação de Imóvel.
   * **Tipo de Movimento**: Informe o código **2.1.XX** criado no Passo 2.
   * **Produto**: Informe o serviço criado no Passo 4.

---

> **Dica:** Os valores de tributos como **IBS** e **CBS** serão preenchidos automaticamente no movimento com base na baixa do lançamento financeiro, desde que a fórmula de base de cálculo esteja configurada no item.
