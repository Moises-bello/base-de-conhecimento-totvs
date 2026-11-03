---
content_hash: 516c8e560bef03adef47690045bc0f2fc53cd0b8e30530ad945e281f576d05da
fetched_at: '2026-06-29T00:09:25.195958+00:00'
page_id: '423938056'
product: rm
source: tdn-rm
title: Simplificado (Apontamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938056
version: 8
---

**Conceito**

Nesse tipo de apontamento é possível apontar atividades de forma rápida.   
 Esse tipo de apontamento pode ser utilizado em processos que não há necessidade de realizar o apontamento das atividades conforme a ordenação calculada.

**Importante**

Como o Apontamento Simplificado permite apontar atividades em qualquer ordenação, os custos podem ser indevidamente valorados, por isso, após apontar uma ordem de produção através desse apontamento, a mesma deve ser obrigatoriamente recalculada. Dessa forma todas as ordens apontadas por esse tipo de apontamento serão gravadas na lista de ordens com pendência de recálculo de custo.  
 Para efetuar o recálculo de custo, todas as pendências de ordens de produção da base de dados devem ser acertadas, essas pendências são do tipo:

* Ordens com Necessidade de Baixa,
* Ordens com Material para dar Entrada
* e Ordens com Material para Desempenhar.

*****Atenção!*****Sugerimos atenção após iniciar o uso do apontamento simplificado, pois se um determinado item de ordem produzido não tiver seu custo recalculado após o prazo máximo para apontamento irregular o sistema irá bloquear novos apontamentos até que o recálculo do item de ordem seja executado.  
    
 **Processo de Apontamento Simplificado**

O acesso a esse apontamento está disponível através da tela específica para Apontamento Simplificado.  
 No Apontamento Simplificado estão disponíveis as seguintes opções:

**Leitura do Código de Barras**

Através da leitura do código de barras é possível abrir a tela de apontamento conforme a ordem de produção, item de ordem e atividade informados na leitura do código.

*Layout do Código de Barras:*  
*ID!OP-0025/11!001.01.02!BASE!1*

*Onde:*  
   
*ID: Identificador padrão de início de código de barras*  
*OP-0025/11 = Código da Ordem*  
*!: Separador Padrão*  
*001.01.02 = Código da Estrutura*  
*BASE: Código do Modelo da Estrutura*  
*1: Identificador da atividade.*
