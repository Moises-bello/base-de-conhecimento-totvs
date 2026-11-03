---
article_id: 360012563231
category: RH - Definições de Cálculo
content_hash: bd708f6189c179422030c9ba5baaded03a263cd5017cce2c7cb14e199ce16e07
fetched_at: '2026-06-28T22:43:22.358007+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar modelo padrão de arquivo CSV para importação
  na rotina de manutenção de tabelas
type: support-article
updated_at: '2025-10-02T14:02:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012563231-RH-Linha-Protheus-GPE-Como-criar-modelo-padr%C3%A3o-de-arquivo-CSV-para-importa%C3%A7%C3%A3o-na-rotina-de-manuten%C3%A7%C3%A3o-de-tabelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32841366611479) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como criar modelo padrão de arquivo CSV para importação na rotina de manutenção de tabelas?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Cada tabela contida na rotina de Manutenção de Tabela, segue uma estrutura própria, e essa estrutura esta definida na tabela **RCB - Definição de Tabelas.**Para saber a estrutura do arquivo é necessário verificar na tabela **RCB** os campos presentes na tabela.

Para criar modelo padrão para importação, realize os seguintes passos:

**1.** Verifique em sua tabela **RCB**a ordem correta dos campos, acessando: **Atualizações > Definições de Cálculo > Definição de Tabelas;**  
No exemplo, será criado o arquivo para importação na Tabela S001 - INSS  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32841417194263)

**2.** Abra um novo arquivo do programa ***Microsoft Excel.***

**3.** Crie a tabela com informações que deverão ser importadas, de acordo com a sequência de campos de sua tabela **RCB.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32841417195415)**  
  
​

**4.** Clique em **Arquivo > Salvar Como** e selecione local para salvar seu arquivo;

**5.** Inclua nome para o arquivo e altere o campo **Tipo** para **CSV(separado por vírgulas)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32841417199511)

**6.** Para confirmar, clique em **Salvar.  
  
Importante**A estrutura do CSV tem que ter a mesma quantidade de colunas que consta na estrutura da tabela em definição de tabelas.  
  
Acesse a documentação abaixo para verificar o processo de importação:  
[RH - Linha Protheus - GPE - Como realizar importação na rotina de Manutenção de Tabelas (GPEA320)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012169592-RH-Linha-Protheus-GPE-Como-Realizar-Importa%C3%A7%C3%A3o-na-Rotina-de-Manuten%C3%A7%C3%A3o-de-Tabelas-GPEA320)

**Saiba Mais**  
[Artigos Gestão de Pessoal](%C2%A0https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)  
[Definições de Calculo](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010611534-Defini%C3%A7%C3%A3o-de-C%C3%A1lculos)
