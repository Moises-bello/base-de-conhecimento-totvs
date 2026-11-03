---
content_hash: ff39fb3d9586061cf62adb81ae080b77fc14d8447746a081c7125169f0c466f9
fetched_at: '2026-06-29T00:11:59.598971+00:00'
page_id: '874203128'
product: rm
source: tdn-rm
title: Objeto de Negócio - Relatórios de CIAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=874203128
version: 41
---

# Conteúdo

4Conteúdo

## **1. Visão Geral**

O **relatório CIAP** (Controle de Crédito do Ativo Permanente) tem a função de controlar o **crédito de ICMS** (Imposto sobre Circulação de Mercadorias e Serviços) relacionado à **aquisição de bens do ativo imobilizado** de uma empresa.

### O que é o CIAP?

CIAP é a sigla para **Controle de Crédito de ICMS do Ativo Permanente**. Ele se refere à **apuração mensal dos créditos de ICMS** aproveitáveis sobre os bens adquiridos para o ativo imobilizado da empresa (como máquinas, equipamentos, veículos, etc.).  
O crédito de ICMS desses bens **não pode ser aproveitado de forma integral de imediato**, como acontece com insumos. Em vez disso, ele deve ser **aproveitado de forma proporcional ao longo de 48 meses (4 anos)**, conforme regras estabelecidas pela legislação do ICMS.

### Para que serve o relatório CIAP?

O relatório CIAP serve para:

1. **Registrar as aquisições de bens do ativo imobilizado** que geram direito a crédito de ICMS.
2. **Controlar a apropriação mensal dos créditos**, dividindo-os em 48 parcelas mensais.
3. **Integrar as obrigações acessórias**, como a Escrituração Fiscal Digital (EFD ICMS/IPI).

## **2. Cálculo do CIAP**

Para correta Geração do Relatório é necessário que o cálculo do CIAP tenha sido realizado.   
Verifique a parametrização necessária e como executar o processo a partir da Documentação [Cálculo CIAP](https://tdn.totvs.com/pages/viewpage.action?pageId=422545962)

## **3. Download e Geração**

O Download e importação dos Relatórios pode ser realizado a partir do [Totvs Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento).  
  
Estão disponíveis dois Relatórios:  
  
***FISTRP0017 - Relatório CIAP Consolidado  
FISTRP0018 - Relatório CIAP Individual***

Demonstração - Importação do Layout e Geração do Relatório

## **4. Exemplos de Relatórios do CIAP**

Exemplos de relatóriosRelatório Consolidado

Clique para visualizar a imagem:

ImagemExemplo PDF

Exemplo do Relatório CIAP Consolidado (Modelo C) em PDF

250

Relatório Individual

Clique para visualizar a imagem:

ImagemExemplo PDF

Exemplo do Relatório CIAP Individual em PDF

250

O relatório é separado anualmente é deve ser filtrado com períodos de 4 anos. O mesmo só deve retornar valores caso tenha movimentação no período.

## **5. Campos**

Atualmente, o Relatório é baseado no

## **6. Outras informações**

Há quatro parâmetros a serem preenchidos tanto para o objeto de negócio quanto para o relatório, sendo eles:

* Código da coligada;
* Código da filial;
* Ano inicial período;
* Ano final período;

**Todos os parâmetros são obrigatórios e o período deve corresponder a 4 anos.**
