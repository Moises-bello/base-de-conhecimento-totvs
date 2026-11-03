---
article_id: 360015271312
category: RH - Rescisão
content_hash: adfea61fc97498c4cdc5be380d82f302076c149abd37f22ad9e2db13c4194dc5
fetched_at: '2026-06-28T22:43:49.800984+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - O que conferir quando sistema não realiza o calculo
  da rescisão
type: support-article
updated_at: '2025-07-21T14:42:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015271312-RH-Linha-Protheus-GPE-O-que-conferir-quando-sistema-n%C3%A3o-realiza-o-calculo-da-rescis%C3%A3o
---

**Dúvida**Sistema não calculou a rescisão, o que deve ser verificado? Como realizar o calculo de rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para executar o cálculo da rescisão na versão Protheus 12, favor executar o seguinte procedimento:  
  
1. Cadastrar uma verba e atrelá-la ao identificador de cálculo **0072 - Pagamento Férias**. **GPEA040**- **Atualizações/Definições Cálculos/Verbas.**  
2. Cadastrar os tipos de rescisão:  **GPEA320 - Atualizações/Definições de cálculo/Manutenção de tabelas S043.**  
  
3. Na rotina de **Controle Dias de Direito**, ter  vinculada a verba de Férias com ID de cálculo 0072. **GPEA050 - Atualizações/Funcionários/Controle Dias de Direito.**4. Atrelar o funcionário a um código de Processo. **GPE010 - A****tualizações/Funcionário/Funcionários:**5. De acordo com o Processo cadastrado para o funcionário no cadastro de funcionários campo **Cod.Processos**, deverá ser habilitado no período de acordo com os roteiros de  
cálculo, o roteiro RES. **GPEA400 - Atualizações/Definições Cálculos/Período.**  
  
6. Acessar a rotina de Rescisão, para efetuar o cálculo. **GPEM040**- **Miscelânea/Cálculos/Rescisões.**  
![](http://tdn.totvs.com/download/attachments/243012138/image2016-7-6%209%3A16%3A47.png?version=1&modificationDate=1467807780000&api=v2)  
  
7. Verifique se há **roteiros para serem integrados à rescisão**, por exemplo PLA. Pois caso o calculo e integração não seja realizado pelo menu e somente lançados, os valores de plano de saúde de rescisão não serão levados na DIRF.  
Realize o cálculo do plano de saúde somente para o funcionário e depois em rescisão outras ações, realize a integração:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058724734/mceclip0.png)  
  
O **Protheus** permite executar o cálculo da rescisão de forma efetiva ou não, sendo assim, quando informado não, o sistema irá apenas simular o cálculo e quando informado sim, o sistema irá efetivá-la conforme a demonstração abaixo:  
![](http://tdn.totvs.com/download/attachments/243012138/image2016-7-6%209%3A18%3A3.png?version=1&modificationDate=1467807781000&api=v2)  
  
Após **Upgrade** **de release**, é importante renomear a pasta que contém o **repositório de fórmulas (rpofrm),** que fica no diretório do RPO do Protheus (ele é gerado a partir das fórmulas e roteiros do SIGAGPE). Veja a documentação sobre [Procedimento para efetuar a atualização básica do Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=271651871)  
  
**Saiba Mais**  
Para adquirir mais informações acesse o *link*: [GPE005RES12\_Parametrizações\_para\_rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=275311434)
