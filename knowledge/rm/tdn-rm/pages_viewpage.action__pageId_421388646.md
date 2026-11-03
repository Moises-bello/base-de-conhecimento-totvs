---
content_hash: 4b7199fba69dd1881dd4d2687aaf1ac2723ebb165ba5ff51be902040ea9f3edd
fetched_at: '2026-06-29T00:09:17.781150+00:00'
page_id: '421388646'
product: rm
source: tdn-rm
title: FIN - Cotações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388646
version: 7
---

Através deste módulo você pode cadastrar diversas cotações para as moedas e índices.

Na janela principal é possível visualizar de forma simplificada, informações de um ou de vários registros.

Você define quantos e quais registros serão apresentados, criando filtros através do Gerenciados de Filtros (localizado na Barra de Ferramentas).   Ao executar um filtro cada registro será apresentado em uma linha e as informações em colunas.

**Dicas**

Utilizando o gerenciador de filtros você poderá criar várias formas para controlar e comparar as cotações existentes.

Você pode definir quais as colunas que serão apresentadas na janela de visão dos registros, utilizando a funcionalidade "Configurar Colunas", ícone localizado na barra de ferramentas.

**Identificação**

Nesta pasta são apresentadas informações que identificam a Cotação.

Data

Neste campo você deverá informar a data da cotação.

Valor

Corresponde a quantidade.

Símbolo

Neste campo você deverá informar o símbolo que representa o Índice ou a Moeda.

Valor

Corresponde ao valor real da cotação

### **Integração EAI 2.0**

É possível realizar a integração das cotações RM x Microsiga Protheus através do uso da EAI 2.0. Para isso, além das configurações gerais para essa integração, é necessário atentar para que nos "Parâmetros de Integração" seja informado o valor para o parâmetro MOEDAPADRAO. Esse valor deverá ser preenchido com o símbolo de referência da moeda padrão utilizada no sistema, atente-se para que não haja espaços na digitação.

Caso esse valor não seja preenchido, será gerado um erro de Violação de Chave Estrangeira.

**Processos**

[Importar Cotações: API - Banco Central do Brasil](https://tdn.totvs.com/pages/releaseview.action?pageId=655451844)
