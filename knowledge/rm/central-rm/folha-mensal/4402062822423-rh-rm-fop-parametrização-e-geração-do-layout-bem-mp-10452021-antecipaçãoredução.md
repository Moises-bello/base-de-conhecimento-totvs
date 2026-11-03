---
article_id: 4402062822423
category: Folha Mensal
content_hash: 32c074be4e5aad6453b60053dc6ada2937d91e5c469e700020b97bcf9c1d3733
fetched_at: '2026-06-28T22:46:59.395722+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Parametrização e geração do Layout B.E.M. MP 1.045/2021 - Antecipação/Redução
type: support-article
updated_at: '2025-03-07T14:52:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062822423-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-do-Layout-B-E-M-MP-1-045-2021-Antecipa%C3%A7%C3%A3o-Redu%C3%A7%C3%A3o
---

**Dúvida**Quais as versões e adequações a serem realizadas no RM Folha de Pagamento para atender ao Layout B.E.M. MP 1.045/2021 referente à Antecipação/Redução?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.28.293
* 12.1.29.257
* 12.1.31.162
* 12.1.32.104

**Solução**Primeiramente realize a importação do layout acessando: Gestão | Gerador de Saídas | Processos | Importar Layout "[FOPLAY0087 - Layout B.E.M Antecipacao.TotvsGen](https://tdn.totvs.com/pages/releaseview.action?pageId=617174252&preview=/617174252/617174187/FOPLAY0087%20-%20Layout%20B.E.M%20Antecipacao.TotvsGen)"

Após a importação, para gerar o arquivo deve selecionar o layout desejado, ir em Processo | Geração de Saídas. O processo irá abrir a tela abaixo. Nesta tela poderá alterar o caminho onde deseja que o relatório seja armazenado após a geração:  
  
![image2020-6-26_16-37-6.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_16-37-6.png?version=1&modificationDate=1593200226627&api=v2)  
  
Ao avançar, irá apresentar a tela abaixo com os parâmetros da geração, que devem ser preenchidos pelo usuário:  
  
![image2020-6-26_16-55-1.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_16-55-1.png?version=1&modificationDate=1593201301277&api=v2)  
  
No nosso exemplo, foi selecionado o arquivo Layout B.E.M Cancelamento.TotvsGen, e então o uso do filtro 'Filtro do Usuário', usando o campo 'Data do Cancelamento' = '26/06/2020':  
  
![image2020-6-26_17-3-43.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_17-3-43.png?version=1&modificationDate=1593201823977&api=v2)  
  
O arquivo gerado no diretório informado em formato .txt:  
  
![image2020-6-26_18-27-15.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_18-27-15.png?version=1&modificationDate=1593206835153&api=v2)  
  
Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Abrir o arquivo no bloco de notas, ir em arquivo e salvar como e em seguida mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:  
  
![image2020-6-26_19-48-0.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_19-48-0.png?version=1&modificationDate=1593211680823&api=v2)  
  
Após salvar, o arquivo será apresentado conforme abaixo:  
  
![image2020-6-26_19-51-21.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_19-51-21.png?version=1&modificationDate=1593211881493&api=v2)  
  
Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web. Para validar a opção de antecipação do término do contrato, deverá ser selecionada a opção **'Redução'** no validador.   
  
![image2020-6-26_19-57-1.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_19-57-1.png?version=1&modificationDate=1593212221253&api=v2)

**Saiba mais:**  
[Layout B.E.M. MP 1.045– Antecipação/Redução](https://tdn.totvs.com/pages/releaseview.action?pageId=617174252)
