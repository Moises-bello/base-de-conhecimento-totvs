---
content_hash: a97dcd9bcedbad455e25d4868e9c9fb86c12d4b016f3b00bf7e8b14bc9d58a8a
fetched_at: '2026-06-29T00:10:03.978392+00:00'
page_id: '452719182'
product: rm
source: tdn-rm
title: Parâmetros da Entrada de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719182
version: 2
---

A entrada de dados é um processo de lançamento da folha de pagamento. Geralmente, os lançamentos representam o início de um novo período da folha, porém poderão também ser acrescentados dados a um período já existente, desde que seja o período corrente.   
    
 A entrada de dados destina-se aos lançamentos individuais, como faltas e outros eventos que não podem ser aplicados sem diferenciação a um grupo de funcionários.   
    
 **Observação**: Para lançamentos que são comuns a todos ou a um determinado grupo de funcionários, poderá ser utilizado o recurso de lançamentos de Grupo de Eventos.   
    
 É Possível "Ordenar" a visualização dos funcionários por "Nome" ou "Chapa" no momento da digitação do movimento.  
    
 É possível "Digitar" selecionando o funcionário por "Nome" ou "Chapa" completo no momento da digitação do movimento.  
    
 De acordo com os valores a serem lançados se já existirem no movimento poderá ser tomada as seguintes ações:

* **Ignorar** - Os dados existentes no movimento não serão alterados.
* **Somar -** Os valores digitados serão somados aos dados correspondentes no movimento.
* **Substituir** - Os valores informados nos eventos substituirão os dados correspondentes no movimento.

A função do funcionário poderá ser visualizada selecionando o parâmetro "Mostra função do funcionário" e a situação sempre é visualizada no momento da digitação.  
    
 Ao selecionar o parâmetro "Informa total de minutos para eventos do tipo 'H'" será permitido lançar os eventos do tipo 'H' (hora) digitando total de minutos.  
    
 **Exemplo:** Ao lançar o evento horas normais com o valor 120 minutos serão pago ao funcionário 2 horas.   
    
 Habilitando o parâmetro "Ler próximo funcionário", os funcionários serão visualizados automaticamente de acordo com a seleção e efetuada pelo usuário.  
    
 Utilizando o recurso "Gravar digitação a cada funcionário", serão salvas as alterações a cada registro alterado. Este recurso visa evitar que algum incidente, como um pique de luz, comprometa o trabalho realizado quando estiver inserindo determinadas informações para vários funcionários.  
    
 Habilitando o parâmetro "Mostra Campo Referência", na tela de entrada de dados será apresentada ao lado da coluna "Valor" a coluna "Ref." (referência). Possibilitando informar valor de referência para evento do tipo "Ref" e "Valor", sendo que o mesmo utilizará este valor para tratamento em fórmulas ou utilizará este valor apenas como informativo. Para eventos do tipo Hora não será permitido informar "Ref", seguindo a mesma padronização do Envelope de Pagamento.   
    
 **Observação:** Para eventos do tipo Referência ou Dia quando informados valores nas duas colunas "Valor" e "Ref.", o sistema considerará o valor digitado na coluna "Ref", desconsiderando o que foi informado na coluna "Valor".  
    
 Habilitando o parâmetro "Usar Eventos Fixos", poderão ser selecionados alguns eventos para serem automaticamente mostrados na grade de entrada de dados quando um funcionário for selecionado, esta opção visa facilitar a digitação dos dados de vários funcionários que tenham para a competência em questão os mesmos eventos.  
    
 A "Forma de Seleção" poderá ser selecionada de acordo com a ordenação dos eventos fixados por ordem alfabética ou por ordem de código de eventos. Esta opção somente estará habilitada, quando selecionado o parâmetro "Usar Eventos Fixos".  
    
 **Observação:** Caso haja a opção pela ordenação por Código de Eventos, marcando os eventos e mude a ordenação para Alfabética, a seleção anterior será toda desmarcada e nova seleção deverá ser feita.  
    
 O campo "Selecione Eventos" possibilitará a informação do código do evento e este será marcado, na janela de Eventos Fixos, facilitando a marcação dos eventos que serão fixados para a entrada de dados. Deverá ser digitado o código do evento e clicar no ícone para marcar um evento fixado, para desmarcar deverá fazê-lo na janela de "Eventos Fixos" ou caso queira desmarcar todos, deverá desmarcar a opção "Eventos Fixos" e logo em seguida marcá-la novamente. Esta opção somente estará visível, quando habilitado o parâmetro "Usar Eventos Fixos".  
    
 Habilitando o parâmetro "Ler Ficha Financeira", os dados da ficha financeira do período corrente serão transportados para a janela de Entrada de Dados.   
    
 **Atenção**: Para evitar possíveis conflitos de informações, ao habilitar esta janela, o parâmetro 'Usar eventos fixos' ficará automaticamente desabilitado e vice versa.  
    
 Quando da digitação de novos eventos para o funcionário, serão apresentados todos os eventos gravados na Ficha Financeira e o parâmetro "Posiciona o cursor no final para inserção de novos eventos" marcado posicionará o cursor para digitação de novo evento no próximo registro em branco. Esta opção ficará habilitada quando estiver marcada a opção "Ler Ficha Financeira".  
    
 O parâmetro "Usa consistência através de soma" possibilitará consistir os dados digitados por uma soma realizada antes do início da digitação. Junto pode ser marcado o parâmetro "Somar chapa" e a consistência da soma incluirá também a chapa.   
    
 Neste caso, na janela de Entrada de dados, será disponibilizado o campo "Valor soma", que deverá ser, obrigatoriamente, preenchido.   
    
 **Exemplo:** Lançamento do evento 0002 – Dias Trabalhados com valor de 15 dias, para o funcionário 00001, o resultado para o campo Valor soma seria 18, ou seja, 2 + 15 + 1.  
    
 **Atenção:**

* Quando habilitado o parâmetro "Mostra Campo Referência", sistema apresentará na tela de entrada de dados a coluna "Ref", porém os valores digitados nessa coluna não serão considerados para consistência de soma.
* Ao confirmamos o parâmetro acima, os valores digitados em horas serão considerados como valores inteiros (sem máscaras) no valor da soma da movimentação.

**Exemplo:** Hora Extra - 008:25 será considerado o valor 825 no valor da soma da movimentação. Considerando o exemplo anterior: Lançamento do evento 0002 – Dias Trabalhados com valor de 15 dias e do evento 0082 – Hora Extra com o valor hora de 008:25 para o funcionário 00001, o resultado para o campo Valor soma seria 925, ou seja, 2 + 15 + 82 + 825 + 1.  
 O parâmetro "Completar o número da chapa com a esquerda" possibilitará a opção de ser preenchida ou não com um caractere à esquerda da chapa na digitação dos funcionários.  
    
 **Exemplo:**

1) O Parâmetro **Completar o número da chapa com à esquerda** DESMARCADO:  
 Chapa do funcionário = 00001  
 O usuário deverá informar a chapa do funcionário completa = 00001  
 2) O Parâmetro **Completar o número da chapa com 0 à esquerda** MARCADO:  
 Chapa do funcionário = 00001   
 Tamanho da chapa = 5 e máscara = #####  
 O usuário deverá informar apenas 1 na chapa que o sistema automaticamente irá preencher com 0(zeros) à esquerda até completar o tamanho da chapa.  
 3) O Parâmetro **Completar o número da chapa com 9 à esquerda** MARCADO:  
 Chapa do funcionário = 99991   
 Tamanho da chapa = 5 e máscara = #####  
 O usuário deverá informar apenas 1 na chapa que o sistema automaticamente irá preencher com 9(nove) à esquerda até completar o tamanho da chapa.  
    
 O parâmetro "Grava movimento digitado" possibilita gravar em um arquivo-texto os dados lançados manualmente. Será habilitado um campo para informação do caminho e o nome do arquivo. O nome "default" (padrão ) é RMMOV (número do período de movimentação).TXT.   
    
 **Exemplo:** RMMOV1.TXT se for o primeiro período; RMMOV2.TXT, se for o segundo período e assim por diante.   
    
 No canto inferior esquerdo da tela existe um campo onde poderão ser salvos os parâmetros de impressão e seleção, que será denominado como "Perfil de Parâmetros".   
    
 Para salvar os parâmetros de uma impressão:

* Definir na tela os parâmetros que considerar necessário para impressão.
* Digitar um nome para o novo perfil.
* Clicar em "Incluir perfil".

E assim deve ser feito para as demais variedades de perfis que o usuário quiser que fiquem armazenadas, para não ter trabalho no futuro de marcar ou de desmarcar opções de impressão e seleção.  
    
 Para excluir um perfil gravado escolha o perfil que se deseja excluir e clicar no botão "Excluir perfil".

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Entrada de Dados  
 Entrada de Dados por Centro de Custo  
 Entrada de Dados por Tomador
