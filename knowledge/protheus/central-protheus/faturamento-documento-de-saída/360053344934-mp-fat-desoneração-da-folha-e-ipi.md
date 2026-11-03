---
article_id: 360053344934
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 51142b65a5420a06fe83bfcec927deee89deb5391fbb1b238a3f27ce4f684d88
fetched_at: '2026-06-28T22:38:45.169979+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Desoneração da Folha e IPI
type: support-article
updated_at: '2021-04-28T15:12:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053344934-MP-FAT-Desonera%C3%A7%C3%A3o-da-Folha-e-IPI
---

**Dúvida**

Desoneração da Folha e IPI.  
  
**Ambiente**

Microsiga Protheus - a partir da release 12.1.25.  
  
**Solução**

Produto configurado para gerar ***Tipo de receita 1***:

A NF gerada pelo Tipo de Pedido " Normal ", com calculo de IPI agregando ao total da NF, vai gerar registro Tipo 1 e:

O " Valor Base para Calculo " sem imposto agregado  
O " Valor da Receita Bruta " com Imposto agregado  
O valor do Imposto na Coluna " Valor dos Impostos "

A NF gerada pelo Tipo de Pedido " Complemento de IPI ", com calculo de IPI, vai gerar registro **Tipo 2** e:

O " Valor Base para Calculo " é o valor da NF  
O " Valor da Receita Bruta " zero  
O valor do Imposto na Coluna " Valor dos Impostos " o valor negativo da NF  
  
Verificar também o Link abaixo

**<https://tdn.totvs.com/x/XS4wDg>**

**Saiba Mais sobre desoneração no Faturamento:**

**[MP-FAT-Configuração para Faturamento e a Desoneração da Folha de Pagamento - Tabela S033](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023351171-MP-FAT-Configura%C3%A7%C3%A3o-para-Faturamento-e-a-Desonera%C3%A7%C3%A3o-da-Folha-de-Pagamento-Tabela-S033)**

**[MP - FAT - Desoneração da Folha - Parâmetro MV\_FOLMES Versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017658492-MP-FAT-Desonera%C3%A7%C3%A3o-da-Folha-Par%C3%A2metro-MV-FOLMES-Vers%C3%A3o-12)**

**[MP - FAT - Desoneração - Criação da Tabela SV5](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049591434-MP-FAT-Desonera%C3%A7%C3%A3o-Cria%C3%A7%C3%A3o-da-Tabela-SV5)**
