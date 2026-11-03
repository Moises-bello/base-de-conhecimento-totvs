---
content_hash: 43f2a820c3aed83aae4e85c39ae6f84bec92131be8aaa36b0891e8ee0bbe0bb3
fetched_at: '2026-06-29T00:10:02.490262+00:00'
page_id: '452718923'
product: rm
source: tdn-rm
title: Layout de Relógio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718923
version: 8
---

**Layout de Relógio**

O TOTVS Automação de ponto importa qualquer arquivo com extensão TXT, desde que as informações do layout estejam conforme o arquivo gerado, portanto, é compatível com qualquer marca de relógio de ponto que grave em um arquivo desse tipo.

O Layout de relógio é utilizado na importação de batidas, pois o relógio que coleta as batidas dos funcionários ou visitantes gera um arquivo texto com as informações das batidas. No cadastro do Layout informamos para o sistema o formato que devem ser lidas as informações geradas pelo relógio. A criação do layout é simples, basta informar as posições e tamanho dos campos conforme arquivo texto que é gerado pelo terminal de coleta.

**Utiliza layout AFD para importação *(Utiliza layout AFD Portaria 1510/2009)***

Utilize esse parâmetro caso queira realizar a importação de batidas conforme o layout AFD da Portaria 1510/2009. Ao marcá-lo, o menu "Layout" ficará inativo, passando a considerar o layout conforme o MTE (Ministério do Trabalho e Emprego) para a importação de batidas.

**Utiliza layout AFD da portaria 671 para importação *(Utiliza layout AFD Portaria 671/2021)***

Utilize esse parâmetro caso queira realizar a importação de batidas conforme layout da Portaria nº 671/2021. Ao marcá-lo, o menu "*Layout*" ficara desabilitado, passando a considerar o layout conforme o MTE (Ministério do Trabalho e Emprego) para a importação de batidas da Portaria nº 671/2021**.** Conforme estabelecido na portaria, Registro do tipo "3", posição 035-046, será reconhecido o PIS, CPF ou sua composição, sendo a leiturainiciada da esquerda para direita,  contendo os 12 dígitos iniciando com o 0 , 8 e 9 ou contendo apenas o CPF nas 11 primeiras posições e na 12º posição com espaço.

**Utiliza layout AFD Portaria 671/2021, contém somente CPF**

Utilize esse parâmetro caso queira realizar a importação de batidas conforme layout da Portaria nº 671/2021. Ao marcá-lo, o menu "*Layout*" ficara desabilitado. Esta opção deverá ser utilizada quando os registradores de pontos que gerem o AFD apenas com o CPF do funcionário noRegistro do tipo "3", posição 035-046. Nesta posição o CPF poderá ser preenchido com o zero na 1º posição ou com espaço na 12º posição. Para maiores informações Acesse : :<https://tdn.totvs.com/display/public/ConSeg/Portaria+671+-+Leitura+do+Novo+Layout+AFD>

**Layout**

Esta pasta é utilizada para informar todos os dados que são gerados por um relógio de ponto e que são utilizados pelo sistema RM Automação de Ponto na importação de batidas.

**Arquivo de Batidas**

Caso queira fazer um teste e verificar se o arquivo texto gerado pelo relógio de ponto está compatível com o cadastro de layout. Para fazer esta validação basta informar o caminho onde se encontra o arquivo no campo abaixo. No campo linha você pode selecionar uma linha do arquivo que queira validar.

Após informar o caminho onde se encontra o arquivo e a linha, é necessário clicar no botão Testar. O sistema preencherá os campos de Teste do layout com os dados do arquivo informando de acordo com os parâmetros de posição e tamanho informado nesta pasta.

**Parâmetros**  
No campo abaixo informe a posição e o tamanho de cada registro informado no layout do relógio que será utilizado na importação de batidas.

**Posição**

O Sistema chama de posição a coluna no arquivo-texto que começa um determinado campo.

**Tamanho**

É número de colunas que cada campo ocupa.

O campo chapa ocupa até 16 colunas, o campo hora ocupa até 5 colunas, os campos dia e mês ocupam até 2 colunas e o campo descrição ocupa até 50 colunas.

**Observação:** O campo descrição será utilizado para justificar a falta do colaborador e estará visível apenas para os layouts customizados, ou seja, layout AFD não terá descrição.

As posições ocupadas pelos elementos serão preenchidas da seguinte maneira na Estrutura do Layout:

'G' - posições com a coligada;

'C' - posições com a chapa;

'h' - posições com a hora;

'm' - posições com o minuto;

'M' - posições com o mês;

'R' - posições com o número do relógio;

'D' - posições com o dia;

'F' - posições com a função.

´D' -posições com a Descrição

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Terminal de coleta  
Importação de Batidas  
   
   
HelpWiki - RH - Automação de Ponto
