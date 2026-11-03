---
content_hash: b5b02b5211b74871733b74b57a5b6270590a899f7a4dd871b2bead577bf1c399
fetched_at: '2026-06-29T00:10:08.001523+00:00'
page_id: '452719495'
product: rm
source: tdn-rm
title: Contribuição Patronal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719495
version: 2
---

Neste cadastro será possível informar os valores de Contribuição Patronal para cada competência de apuração. Este cadastro é acessado em Administração de Pessoal | Cadastros | Seções | Anexos | Dados Anuais da RAIS - eSocial | Anexo | Contribuição Patronal.  
 Os dados deste cadastro serão considerados no evento S-1300, onde será retornado o valor da contribuição conforme informado neste cadastro por período.    
    
 **Campos**  
 Tipo de Contribuição  
 O usuário deve selecionar o tipo de contribuição patronal, sendo elas:

* Compulsória
* Associativa
* Assistencial
* Confederativa

Após salvar o cadastro, o usuário não poderá mais escolher outro tipo de contribuição. Caso queira mudar o tipo de contribuição, deverá excluir este cadastro e inserir um novo.   
    
 Ano Base  
 Neste campo irá retornar o ano base informado na aba identificação do cadastro de Dados Anuais da RAIS | eSocial. Este campo não é editável.   
    
 Mês Recolhimento  
 Neste campo irá informar o mês da competência de recolhimento da contribuição Sindical. Após salvar o cadastro, este campo não poderá mais ser alterado. Caso queira mudar o mês de recolhimento, deverá excluir este campo e inserir um novo.   
    
 Valor  
 Neste campo será informado o valor de recolhimento da contribuição Patronal. Este campo pode ser alterado.  
    
 **Observação**  
 Quando é gerado o evento S-1300, é validado o período de apuração com o mês de recolhimento informado neste cadastro, retornando no *xml* somente os valores referentes ao mês período de apuração. Caso não exista nenhum tipo de contribuição informado para o mês selecionado, é retornado uma mensagem de erro que não existe nenhum tipo de contribuição patronal recolhida para o mês/ano.  
 Não é retornado o valor acumulativo do tipo de contribuição caso existe mais de um cadastro com mesmo tipo de contribuição com mês de recolhimento diferente.  
 O sistema valida duplicidade de cadastro para o mesmo mês de recolhimento e tipo de contribuição.  
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Cadastro de Seções
