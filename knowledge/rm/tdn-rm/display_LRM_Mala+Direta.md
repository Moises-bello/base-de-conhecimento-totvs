---
content_hash: cd2e2242367f3d6454e2a9a181d94851288ac114140bd04e501474da9e626340
fetched_at: '2026-06-29T00:09:32.519110+00:00'
page_id: '425458865'
product: rm
source: tdn-rm
title: Mala Direta
type: documentation
url: https://tdn.totvs.com/display/LRM/Mala+Direta
version: 17
---

Este assistente permite ao usuário gerar arquivos de mala direta para registros de uma determinada consulta SQL, com base em um template pré-definido, existindo também a possibilidade do conteúdo do arquivo ser enviado no corpo do e-mail.  
No primeiro passo é realizada a seleção das pessoas que receberão a mala de direta. Para isto é preciso informar uma consulta SQL, após executar é possível visualizar todos os registros retornados, além disso, no mesmo processo o usuário tem a opção de remover os registros retornados pela consulta.  
Ao avançar para o passo: 'Parâmetros de envio da mala de direta' o usuário terá que:

* Informar o conteúdo da mala direta O usuário tem a opção de importar um arquivo template para a mala direta, criar um novo arquivo ou editar um existente. Além de ter a opção de salvar toda a alteração no formato de interesse. No conteúdo, é possível incluir *Tags*. Estas são marcações inteligentes que serão substituídas por textos específicos durante o processo de montagem dos conteúdos da Mala Direta.

**Importante**: O arquivo template poderá usar Tags que serão substituídas pelas colunas da sentença SQL. Para que esta substituição ocorra corretamente, as Tags deverão ser definidas entre "[ ]" e obrigatoriamente ter o mesmo nome da coluna.  
Exemplo: Sua matrícula foi efetuada com sucesso e seu registro acadêmico será [RA], você fará parte da turma [TURMA] localizada no prédio [PREDIO].

* Definir os parâmetros É possível enviar o conteúdo por e-mail ou gerar arquivos.

**Enviar por e-mail:**  
Nesta opção o usuário precisa informar o "Assunto do e-mail" e o "Tipo de Remente". Para este último, poderá ser selecionado como remetente:  
1. Usuário logado no sistema;  
2. Coligada atual;  
3. Coligada global;  
4. Parâmetros globais (parametrização padrão de envio de mensagens definido na tela de parâmetros de Globais na aba Envio E-mails);  
5. Personalizado: o usuário poderá informar um e-mail e nome do remetente a ser identificado. Esta lista de e-mail(s) personalizado precisa ser informado em Parâmetros | Secretaria | Geral 4/4.

**Importante 1:** Para que seja possível enviar e-mails a consulta SQL utilizada precisa conter a coluna  EMAIL.  
**Importante 2:** Para que funcione a escolha de um Tipo de Remetente diferente do definido nos [Parâmetros Globais](https://tdn.totvs.com/display/public/LRM/Envio+de+email+-+LINHA+RM) é necessário verificar se o serviço SMTP permite isso. Algumas orientações estão no documento  , nos itens 'Importantes'.

**Gerar arquivos:** Para a gerar arquivos de mala direta, é necessário informar um diretório físico onde serão gravados os arquivos criados. Caso o usuário tenha carregado um arquivo de template no editor de texto, o nome do arquivo será carregado no campo "prefixo para nome dos arquivos", podendo o usuário alterar o seu conteúdo. E por último é informado em "Salvar como" qual extensão será gerados os arquivos. O usuário terá como opção às seguintes extensões: rtf, doc, docx, html e pdf. Utilizando a opção de geração de arquivos, é possível utilizar cabeçalho e rodapé no documento.   
**Observações:**   
1. Para arquivo gerado em formato html, o sistema não incluirá o cabeçalho e rodapé mesmo que existam no documento.   
2. Na versão 18.2 do DevExpress, presente a partir da versão 12.1.24 do sistema, as imagens ancoradas ao texto não estão compatíveis com o Word Office ao exportar o arquivo. Os demais formatos não sofreram alterações, o que os tornam alternativas a esses arquivos com imagens ancoradas, sendo que o formato .rtf pode ser visualizado normalmente no Word Office.  
**Identificador dos registros no log** é um campo comum para as duas formas de execução, pois através dele será informado qual das colunas será utilizado como identificador dos arquivos e do *log*. É importante que seja selecionado a coluna que permita identificar o usuário que será enviado o e-mail ou gerado o arquivo.  
Durante a execução do processo o usuário poderá executa-lo em segundo plano. Para isto é só iniciar a execução e fechar a janela do processo, permitindo assim realizar outras tarefas. No momento que o processo é finalizado é informado que o assistente da Mala Direta foi finalizado.

Importante

O processo de mala direta é executado do lado cliente do ambiente do TOTVS RM, ou seja, não é executado nos servidores de aplicação, sendo assim, é necessário que os acessos ao SMTP (endereço e porta configurados nos [Parâmetros Globais](https://tdn.totvs.com/display/public/LRM/Envio+de+email+-+LINHA+RM)) estejam liberados no computador que está executando o processo.

Esta regra também se aplica a clientes que utilizam o TOTVS RM no ambiente Cloud, ou seja, a liberação do SMTP deve ser feita no computador que está executando o processo.

**Importante:** Ainda não é possível o envio de arquivos anexos através da Mala Direta.  
 Veja Também

---

[Boletim Técnico Mala direta](http://tdn.totvs.com/display/rm/EDU_BT_Mala_direta_PCREQ_3292)
