---
content_hash: f1635b6c90d8e396348434f2764d7fa2e7f5bcb1e26e0a0aa9e574618b8875a3
fetched_at: '2026-06-29T00:09:14.252217+00:00'
page_id: '421385171'
product: rm
source: tdn-rm
title: Integração MS Project Parâmetros do Projeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385171
version: 3
---

**Integração MS Project - Parâmetros do Projeto**

---

**Forma de Sincronismo**  
 Antes de realizar o primeiro sincronismo com um projeto do é necessário definir para quais colunas do Project serão enviadas as informações do TOP e vice-versa.  
 Para isso acesse: Projeto | Construção e Projetos | Gerais | Aba Configuração do MS Project.  
 No filtro "Unidade Horária" defina as unidades que serão adaptadas para o MS Project.

**Linha Base para envio da Duração e das Datas Programadas no Sincronismo com o MS-Project:** Este parâmetro permite escolher o  campo do MS-Project para qual será enviado os valores do Plano Programado, podendo escolher também o não envio com a opção nenhum.

Na parte de equivalência de campos defina para os campos:

Descrição, Unidade de Medida, Código Auxiliar, Campo Livre 1, Campo Livre 2, Campo Livre 3, Campo Livre 4, Campo Livre 5, Moeda de Valor, Quantidade da Tarefa, Campo Livre 1 - Valor, Campo Livre 2 - Valor, Campo Livre 3 - Valor, Campo Livre 4 - Valor, Campo Livre 5 - Valor; se deseja envia-los e para qual campo (de tipo de dado compatível) relacionar.   
 A integração deve ser parametrizada com o vínculo de um único arquivo do MS Project, através dos parâmetros do projeto, menu: Projeto | Construção e Projetos | Projetos (F6) | Aba Integração | sub aba MS Project.  
 Para que o sincronismo com o MS Project ocorra corretamente é aconselhável que o vínculo seja iniciado em uma das situações listadas abaixo:   
 1- O projeto do TOP com dados cadastrados e um arquivo do MS Project recém criado (sem modificações).

2- Um arquivo do MS Project com dados cadastrados e o projeto do TOP recém criado (sem modificações).

3- Iniciar o sincronismo com as duas fontes de dados (arquivo do MS Project e projeto no TOP) recém criados.  
    
 **Observação** Após o vínculo é aconselhável que seja executado o sincronismo inicial do projeto.  
 **Sem vínculo:** Marque essa alternativa se o projeto não estiver vinculado a um arquivo do MS Project, ou seja, na exportação de dados para o MS Project sempre será criado um arquivo novo.  
 **Com vínculo:** Marque essa alternativa se o projeto estiver vinculado a um arquivo o MS Project, ou seja, na exportação de dados para o MS Project sempre será aberto o arquivo vinculado e o mesmo será sincronizado com o RM TOP. Na janela de parametrização do sincronismo, as duas partes ficam habilitadas pois o usuário pode optar por apenas enviar o que foi alterado no RM TOP para o MS Project ou somente buscar do MS Project as alterações feitas.  
 **Arquivo do Project vinculado (Localização + Arquivo):** Caso a forma de sincronismo seja com vínculo, informe a localização e o nome do arquivo. Caso não exista o arquivo vinculado no local informando, ao executar a primeira vez o Sincronismo Totvs Obras e Projetos com o MS Project o arquivo será criado e as com as seguintes flags habilitadas: 'Criar novo arquivo', 'Sincronizar Plano Programado', 'Completo'. Caso exista o sistema irá utiliza-lo para realizar o Sincronismo.

Com o intuito de permitir que o TOP trabalhe de forma autônoma da solução da Microsoft, os processos de exportação e importação para MS Project foi modificado, removendo a obrigatoriedade da utilização de licenças no MS-Project.   
 **Atenção:** Devido a retirada da obrigatoriedade do MS Office, o campo de versão será descontinuado.   
 **Importante:**  
 Para ambiente 3 camadas é necessário informar o diretório relativo onde o arquivo se encontra, e esse mesmo diretório deverá ter permissão de leitura e escrita para o usuário do Host:  
 Ex:   
 ·          Diretório local: C:\Temp\ArquivoProject.mpp  
 ·          Diretório relativo: \\NOME\_DO\_COMPUTADOR\_OU\_IP\Temp\ArquivoProject.mpp  
 ·          A pasta "Temp" deverá estar compartilhada e permitir leitura e escrita para o usuário do Host.
