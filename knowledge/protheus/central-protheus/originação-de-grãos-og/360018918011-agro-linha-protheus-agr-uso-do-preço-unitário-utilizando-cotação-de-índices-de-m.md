---
article_id: 360018918011
category: Originação de Grãos (OG)
content_hash: f645fdb67b202e8fa93da9fba9ad7490f2bbc8eb8c3aeda72b4b83a5cd7d306f
fetched_at: '2026-06-28T22:45:45.219171+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Uso do preço unitário utilizando Cotação de índices
  de mercado
type: support-article
updated_at: '2025-06-21T16:15:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018918011-Agro-Linha-Protheus-AGR-Uso-do-pre%C3%A7o-unit%C3%A1rio-utilizando-Cota%C3%A7%C3%A3o-de-%C3%ADndices-de-mercado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20595684754967)*** Tempo aproximado para leitura:**00:01:35 min**  
 **Dúvida**Procedimento de como utilizar a **Cotação de Índices** nas rotinas de **OGA250 -****Romaneios** e **OGA251 - Romaneio sem pesagem**, utilizando registros do **tipo 2 -** **Remessa para Depósito** ou **tipo 3** - **Entrada para Depósito**?   
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para realizar o processo corretamente, realize os seguintes passos:  
  
 **1.** Acesse a rotina **OGA080 -** **Í****ndices do Mercado**. Clique em **Incluir** e insira as informações necessárias, se atentando para a **Unid. Med**, **Moeda**, **TP.****Índice** e **Dt. Venc**;

* A **Unidade de Medida** é a unidade que vai ser usada para possíveis **Conversões**, **Tipo de****Índices**, **D = Diário |** **A = Mais Atual.**

![image2018-10-31_9-23-42.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018551052)

**2.** Outro cadastro importante para o processo é o de **Cotação de****Índices.** Em **Atual. de****Índices** virão os índices cadastrados e no campo **Valor** se indicará o valor do **P****reço do Dia**;

![image2018-10-31_9-55-45.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018430571)

**3.** Acesse o **OGA270** - **Contrato Depto Em 3** e crie um contrato. Depois de inserir as informações necessárias, se atentar para a pasta **Financeiro**, em que o valor base é obrigatório, assim como o campo **UM. Preço - Unidade de Medida do Produto** e também o **Índice**;

![image2018-10-31_9-10-24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018551332)

**4.** O final do processo é realizado pela inclusão do **Romaneio** do **tipo 2** - **Remessa para Depósito** ou **tipo 3** - **Entrada para Depósito**;

![image2018-10-31_10-48-12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018551532)

* O campo **Vlr. Unit** **- Valor Unitário** só deve ser preenchido se for dar um preço, se for utilizar o **Preço da Cotação de índice**, o campo deve ficar **vazio**.
* Na pasta **Comercialização,** nos **Itens de Comercialização**, o campo **Vlr. Unit** irá ser preenchido com o valor cadastrado do índice quando o romaneio for atualizado.

![image2018-10-31_10-55-43.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018430791)
