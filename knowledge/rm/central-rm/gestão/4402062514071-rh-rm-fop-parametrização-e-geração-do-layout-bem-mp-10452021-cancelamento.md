---
article_id: 4402062514071
category: Gestão
content_hash: ca04688ddcbdf8dfbb29bee6c98a157a1fb54670516f67893418e4dab27c9aeb
fetched_at: '2026-06-28T22:46:48.336416+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: RH - RM - FOP - Parametrização e geração do Layout B.E.M. MP 1.045/2021 - Cancelamento
type: support-article
updated_at: '2025-03-12T20:03:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062514071-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-do-Layout-B-E-M-MP-1-045-2021-Cancelamento
---

**Dúvida**Quais as versões e adequações a serem realizadas no RM Folha de Pagamento para atender ao Layout B.E.M. MP 1.045/2021 referente à Cancelamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.28.293
* 12.1.29.257
* 12.1.31.162
* 12.1.32.104

**Solução**Primeiramente realize a importação do layout acessando: Gestão | Gerador de Saídas | Processos | Importar Layout "[FOPLAY0086 - Layout B.E.M Cancelamento.TotvsGen](https://tdn.totvs.com/pages/releaseview.action?pageId=617174252&preview=/617174252/617174185/FOPLAY0086%20-%20Layout%20B.E.M%20Cancelamento.TotvsGen)"

Após a importação, para gerar o arquivo deve selecionar o layout desejado, ir em Processo | Geração de Saídas. O processo irá abrir a tela abaixo. Nesta tela poderá alterar o caminho onde deseja que o relatório seja armazenado após a geração:  
  
![image2020-6-26_20-43-28.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_20-43-28.png?version=1&modificationDate=1593215008723&api=v2)  
  
Ao avançar, irá apresentar a tela abaixo com os parâmetros da geração, que devem ser preenchidos pelo usuário:  
  
![image2020-6-26_20-45-44.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_20-45-44.png?version=1&modificationDate=1593215144747&api=v2)  
  
No nosso exemplo, foi selecionado o arquivo Layout B.E.M Cancelamento.TotvsGen, e então o uso do filtro 'Filtro do Usuário', usando o campo 'Data do Cancelamento' = '26/06/2020':  
  
![image2020-6-26_20-51-46.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_20-51-46.png?version=1&modificationDate=1593215506263&api=v2)  
  
O arquivo gerado no diretório informado em formato .txt:  
  
![image2020-6-26_20-55-7.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_20-55-7.png?version=1&modificationDate=1593215707653&api=v2)  
  
Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Abrir o arquivo no bloco de notas, ir em arquivo e salvar como e em seguida mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:  
  
![image2020-6-26_21-0-1.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_21-0-1.png?version=1&modificationDate=1593216001720&api=v2)  
  
Após salvar, o arquivo será apresentado conforme abaixo:  
  
![image2020-6-26_21-1-38.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_21-1-38.png?version=1&modificationDate=1593216098867&api=v2)  
  
Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web. Para validar a opção de antecipação do término do contrato, deverá ser selecionada a opção **'Cancelamento'** no validador:  
  
![image2020-6-26_21-4-34.png](https://tdn.totvs.com/download/attachments/545641381/image2020-6-26_21-4-34.png?version=1&modificationDate=1593216274143&api=v2)

**Saiba mais:**  
[Layout B.E.M. MP 1.045– Cancelamento](https://tdn.totvs.com/pages/releaseview.action?pageId=617174252)
