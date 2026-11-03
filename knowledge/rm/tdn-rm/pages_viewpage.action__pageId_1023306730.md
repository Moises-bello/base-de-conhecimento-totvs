---
content_hash: a6b59db1f7d5ad942d5ed783a864efd081b18679eca4d5ed08b80872718ed7d0
fetched_at: '2026-06-29T00:05:48.159270+00:00'
page_id: '1023306730'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro rateados pela Natureza Orçamentária Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023306730
version: 8
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Lançamento Financeiro |
| País: | Brasil |
| Issue: | [DRHCALCRM-9363](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9363) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2506
* 12.1.2510 e posteriores

## **03. SITUAÇÃO/REQUISITO**

Permitir realizar da geração de lançamentos financeiros, rateando a natureza financeira por eventos e encargos

## **04. SOLUÇÃO**

Foi disponibilizada a possibilidade de geração de lançamentos financeiros, rateando a natureza financeira por eventos e encargos, conforme telas abaixo:

1. Lookup criado no cadastro de Eventos | Dados Contábeis / Financeiro: Natureza Financeira

   
2. Flag criada no processo de Geração dos Lançamentos: Usar Natureza Financeira do Evento.  
OBS: Já implementando comportamento do parâmetro de habilitado e desabilitado.

3. Parametrizador da gestão Financeira:   
Módulo BackOffice | Gestão Financeira | Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar | Baixa |  Recursos Adicionais  
Verificar se está usando Rateio Ambos ou Natureza, para habilitar os campos criados anteriormente.

4.Tela que verifica se está integrado o RM Folha x Gestão Financeira(RM Fluxus) | Ambiente

5. Tela onde busca a natureza financeira default: Encargos | Cadastros Financeiros | Parâmetros (Smart UI)

6. Encargos | Financeiro | Lançamentos. Só aparece nesta lista após executar o processo.

7. Ao editar o lançamento abrirá a tela abaixo:  
Na aba de Dados Adicionais onde são rateados as naturezas financeiras por centro de custo.

OBS: Só aparece o rateio pela natureza financeira se gerar os lançamentos marcando a flag “Gerar Lanctos rateados por centro de custo” no processo.

## **05.****ASSUNTOS RELACIONADOS**

<https://tdn.totvs.com/display/public/LRM/Cadastros+Financeiros>
