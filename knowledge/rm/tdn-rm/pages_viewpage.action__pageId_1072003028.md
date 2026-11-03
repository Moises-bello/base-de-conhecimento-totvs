---
content_hash: 13c29babf61da6ee473d691a8f75aac17740cdd5cc2faeea7d1b8c22451336e6
fetched_at: '2026-06-29T00:05:53.943636+00:00'
page_id: '1072003028'
product: rm
source: tdn-rm
title: FOPTRP0035 - Encargos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1072003028
version: 5
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

**A partir dos patches:**

+ 12.1.2606 e Superiores
+ [DT - Smart View - Encargos Contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=1072004293)

## **02. V****ISÃO GERAL**

O relatório de **Encargos Contábeis** utiliza o objeto de negócio **`FopEncargosBusinessObject`** para extrair e consolidar os valores de encargos (como provisões de férias, 13º salário, etc.) por funcionário, ano, mês e seção.

#### **Regras de Filtro (Importante)**

Para garantir a performance do banco de dados e a segurança das informações, o relatório exige o preenchimento de parâmetros específicos.

**Importante - Regras de Preenchimento:** Esse relatório possui a manipulação e criação de filtros por parte do usuário. Por padrão vem 

* **Ano:** Informe o ano de competência do encargo.
* **Mês:** Informe o mês de competência do encargo.
* **Matrícula:** Preencha com a chapa do funcionário.

**Filtro do SmartView Padrão:**

|  |  |  |
| --- | --- | --- |
| **Nome no relatório** | **Nome no banco de dados** | **Descrição** |
| Matrícula | PFUNC.CHAPA | Filtra pela chapa do funcionário |
| Ano | PFENCARGO.ANOCOMP | Filtra pelo Ano |
| Mês | PFENCARGO.MESCOMP | Filtra pelo Mês |

A visualização do relatório será baseada no filtro inserido pelo usuário na visão do Smart View. 

O usuário poderá customizar seu filtro via **layout** do Relatório:

**Observação**: Será obrigatório o preenchimento do mês e ano no seu filtro customizado, pois esses dois campos são obrigatórios pela regra do Objeto de Negócio para realizar a busca.

Nesse relatório temos os seguintes campos do objeto de negócio disponíveis:

| Campo do Relatório | Campo da Tabela | Decrição |
| --- | --- | --- |
| Matrícula | PFUNC.CHAPA | Matrícula do funcionário |
| Nome | PFUNC.NOME | Nome do funcionário |
| Código | PENCARGO.CODIGO | Código do Encargo (ex: 001) |
| Encargo | PENCARGO.DESCRICAO | Nome do Encargo (ex: Provisão Acumulada de Férias) |
| Valor do Encargo | PFENCARGO.VALOR | Valor do encargo do funcionário |

## **03.  EXEMPLO DE UTILIZAÇÃO**

1)Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório **FOPTRP0035** e vá em 'Mais Ações', selecione a opção Executar no Smart View, configure os filtros necessários e ao final clique em 'Enviar' para iniciar o processo de geração do relatório. 

3) Filtros:

4) Relatório emitido

**DICAS:**

* É necessário que todos os campos do filtro sejam preenchidos.  Para adicionar um filtro, clique no ícone correspondente.
* A impressão da logo só ocorrerá caso a coligada atual tenha a logo disponível.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.
* É necessário habilitar a permissão em Serviços Globais → Segurança → Perfis → Acesso a Menus:

## **04. TABELAS UTILIZADAS**

* PFUNC
* PENCARGO
* PFENCARGO
* PSECAO
