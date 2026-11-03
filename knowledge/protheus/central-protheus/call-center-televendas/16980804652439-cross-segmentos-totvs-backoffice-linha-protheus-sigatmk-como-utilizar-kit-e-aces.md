---
article_id: 16980804652439
category: Call Center - Televendas
content_hash: 3ed4c08ba8abd4435f7263da4f80355fd69cb89870656aaf1de1717e219a1be5
fetched_at: '2026-06-28T22:41:30.367973+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Como utilizar
  Kit e acessórios no Televendas '
type: support-article
updated_at: '2025-01-10T19:29:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16980804652439-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-utilizar-Kit-e-acess%C3%B3rios-no-Televendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16980827259671) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como utilizar Kit e acessórios no televendas   
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - a partir da versão 11.  
  
**Solução**

Neste cadastro são informados os produtos que podem ter a venda associada à de outro produto. O objetivo é sugerir, no momento da venda na rotina "Call Center" (TMKA271) Televendas. Os produtos que poderão ser utilizados como acessórios de um produto principal de venda, sugerindo produtos vinculados, ou para kits de produtos (conjuntos).  
  
Para utilizar essa funcionalidade deve ser efetuado o cadastro de um produto principal e um ou mais  subprodutos vinculados.   
  
A funcionalidade pode ser utilizada de duas formas, sendo as seguintes opções;  
  
**1- Sugestão automática**  
Ao realizar a inclusão do produto principal no campo "Produto" (UB\_PRODUTO), os subprodutos vinculados na rotina de Acessórios" (TMKA030) serão inclusos de forma automática.     
  
Para utilizar essa opção siga os seguintes passos abaixo:   
  
1-Configure o parâmetro MV\_TMKKIT com o conteúdo (T)   
2- Acesse a rotina "Acessórios" (TMKA030), através do menu Atualizações>Cadastros>Televendas> Acessórios.  
3- Selecione o produto principal no campo "Produto" (SUG\_PRODUTO).  
4- Selecione o produto acessório/kit no campo "Acessório" (U1\_ACESSOR).    
5- Marque a opção do campo "Kit" (U1\_KIT) como SIM  
  
**2- Visualização dos produtos para sugestão manual.**  
Habilita uma visualização dos produtos e subprodutos vinculados através do botão lateral (Toolbar) na rotina de Televendas e permite selecionar de forma manual.   
  
Para utilizar essa opção siga os seguintes passos abaixo:   
  
1-Acesse a rotina "Acessórios" (TMKA030), através do menu Atualizações>Cadastros>Televendas> Acessórios.  
2- Selecione o produto principal no campo "Produto" (SUG\_PRODUTO).  
3- Selecione o produto acessório/kit no campo "Acessório" (U1\_ACESSOR).    
4- Utilize a opção do botão lateral "Cadastro de acessórios"  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/16981033263639)  
5- Selecione o produto principal no campo "Produto" (SUG\_PRODUTO).

Observação: Caso o botão lateral "Acessório" não esteja disponível para uso, habilite através do cadastro do Operador na opção Tool bar. Dúvidas no processo de configuração da Toolbar, acesse a documentação: [Cadastro do Operador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015816612-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Cadastro-de-Operador)
