---
content_hash: 1ba31f0e307ebbc91617ffb11f91c7d5e635d6690f45d3368c6b26c0868a5d84
fetched_at: '2026-06-29T00:10:38.632614+00:00'
page_id: '54429934'
product: rm
source: tdn-rm
title: Como Fazer - Exportar cotação para a Web
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=54429934
version: 2
---

| Produto | RM |
| --- | --- |
| Versões | 10.60 a 11.82 |
| Avaliação | 1 |
| Sintoma | Este documento tem por finalidade auxiliar em todo o processo de cotação online. O processo pode ser dividido em partes, são elas: exportação para web, recebimento pelo fornecedor, preenchimento e importação dos dados fornecidos. |
| Environment | Unspecified |
| RM Nucleus (Usuário do sistema)  Exportar Orçamento para Web | 1º passo: crie a cotação em Movimentos | Cotações...  2º passo: clique no primeiro botão da barra de ferramentas da cotação (imagem).    3º passo: selecione “Exportar Orçamento p/Web”...    **IMPORTANTE: Para que a opção “Exportar Orçamento p/Web” seja mostrada o parâmetro encontrado em Opções | Parâmetros | RMNucleus | Avançar > | 04.06 – Gestão Compras | 04.06.02 – Cotação | Avançar > | Definições Gerais 2/3 | campo “Usar Orçamento via Web” deve estar marcado.**  **OBSERVAÇÃO: Caso tenha sido informada a filial na cotação os parâmetros obedecidos serão os que constam na opção “Definição de Escopo - Filial” encontrada no caminho descrito acima.**  **Será mostrada a mensagem abaixo, leia atentamente:**    **4º passo: Selecione os fornecedores que participaram da cotação via web (somente se já tiver feito algum comunicado para esta cotação) e clique em OK.**  **A mensagem abaixo será mostrada caso o processo ocorra com sucesso:**  *"Cotação 2013.000020 exportada com sucesso."* |
| Portal (Fornecedor)  Lançando os dados no portal / Cotação Online | 1º passo: O Fornecedor receberá uma mensagem de e-mail onde constará seu LOGIN e SENHA para acesso a Cotação On-line, como mostra a imagem abaixo:    2º passo: O fornecedor ao acessar o portal deverá entrar no link Cotação On-line.  Obs.: Este link pode ser passado pelo e-mail enviado anteriormente, basta alterar o relatório utilizado passando o link para o portal da empresa    3º passo: Serão exigidos o LOGIN e a SENHA enviados ao e-mail do Fornecedor, como mostra imagem abaixo.    4º passo: Será aberta uma janela com as informações relativas ao fornecedor como pode ser visualizado logo abaixo:    5º passo: Clicando em Item do Orçamento no menu a esquerda da tela o fornecedor poderá informar o preço e o valor do IPI para cada produto da cotação.       Deve-se clicar no produto desejado e depois em Editar. A janela abaixo será mostrada e nela é possível informar o valor do produto, do IPI e uma observação.    Depois de Salvar/Fechar os valores serão mostrados na tela dos Itens de Orçamento.    **IMPORTANTE: O fornecedor deverá voltar ao menu Principal e SALVAR a cotação, caso contrário os dados não serão levados ao sistema. Após salvar a cotação a janela do portal poderá ser fechada.** |
| RM Nucleus (Usuário do sistema)  Importando os dados da Web | O usuário deverá acessar o menu Sistema | Server | Processos Agendados... Aqui o usuário pode ver que foi criado um agendamento para “Importação de cotação da web” para o dia 25/04/2013 as 00:01:00 pois a data limite para resposta da cotação é de 24/04/2013.    Acessando o menu Sistemas | Server | Executar Processos | será mostrada uma janela onde o usuário deverá clicar em “Iniciar” para que o processo de coleta das informações na web seja iniciado.    Caso a data limite já tenha sido contemplada este processo irá buscar os dados referentes a cotação e atualizar automaticamente na cotação criada no início deste texto.  Ao acessar | Movimentos | Cotação | e selecionar a cotação desejada poderá ser observado que os valores já estarão preenchidos.  O processo de cotação pode ser concluído normalmente daqui em diante. |
